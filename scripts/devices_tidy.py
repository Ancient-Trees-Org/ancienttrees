#!/usr/bin/env python3
"""Keep the Mac's test phones and spare checkouts from filling the disk.

Hidde, 2026-11-26, with 248 MB left of 460 GB: "hoe zorgen we dat dit niet
steeds gebeurt want elke keer als we gaan testen worden er teveel emulators op
mn mac gezet". 39 GB of iPhone simulators, 19 GB of Android emulators and 19 GB
of worktrees. Nothing was wrong with any one of them. Each test phone grows by
every build installed on it (2 to 5 GB), sessions made their own simulator
("AT dark hertz") or a second copy of a fixed one when they could not find it,
and a session's worktree outlives the session. Xcode and Android Studio never
clear any of it.

A rule asking sessions to reuse phones and clean up after themselves would not
hold: the duplicate "iPhone SE (sweep)" exists because a session did not find
the first. So this script enforces the set instead, and runs at every session
start (the SessionStart hook in .claude/settings.json) but only does anything
when the disk is getting full:

    python3 scripts/devices_tidy.py               # say what it would do
    python3 scripts/devices_tidy.py --apply       # do it
    python3 scripts/devices_tidy.py --if-low 40   # the hook: apply only under 40 GB free

What it does, and only to things nobody used in the last IDLE_HOURS:
- iPhone simulators. The fixed set is KEEP_NAMES (what appsweep.py, CI and the
  other scripts ask for by name, with or without " iOS <version>"). A shut-down
  simulator outside it that holds anything is deleted; a second one with the
  same name on the same runtime is deleted; one inside it that has grown past
  ERASE_OVER_GB is erased (it keeps its name and id, its app data goes).
- Android emulators. Quick-boot snapshots of an emulator that is not running
  are deleted (the next start is a cold boot, once). App data past
  ANDROID_DATA_WARN_GB is only reported: wiping it is a cold boot of its own.
- Worktrees under .claude/worktrees that checkouts.py would call removable
  (clean, no commit that is not on origin/main) and that nobody touched lately.

It never touches anything running: a booted simulator, a live emulator, a
worktree with uncommitted files. Those are a session at work.
"""

import argparse
import datetime
import json
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

HOME = pathlib.Path.home()
AVD_DIR = HOME / ".android" / "avd"
WORKTREES = ROOT / ".claude" / "worktrees"

# Every simulator name a script, CI or a memory note asks for. appsweep.py adds
# " iOS <version>" to these, so the version suffix is allowed on any of them.
KEEP_NAMES = {
    "iPhone SE (sweep)",
    "iPhone 17 Pro",
    "iPhone 17 Pro Max",
    "iPhone 17",
    "iPhone 16 Pro Max",
    "iPhone 16 Plus",
    "iPhone 15 Pro Max",
}
IDLE_HOURS = 12
ERASE_OVER_GB = 1.5
DELETE_OVER_MB = 100      # Xcode's own empty defaults (18 MB) are left alone
SNAPSHOT_OVER_GB = 1.0
ANDROID_DATA_WARN_GB = 6.0
GB = 1024 ** 3


def base_name(name):
    return re.sub(r" iOS \d+(\.\d+)*$", "", name)


def parse_time(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=datetime.timezone.utc)
    except (TypeError, ValueError):
        return None


def idle(last, now):
    """Not used within IDLE_HOURS. Never used counts as idle."""
    return last is None or (now - last).total_seconds() > IDLE_HOURS * 3600


def plan_simulators(devices, now):
    """[(action, udid, name, why)] from `simctl list devices -j`'s "devices".

    Pure, so the test can hand it a made-up list."""
    actions = []
    for runtime, devs in devices.items():
        by_name = {}
        for d in devs:
            if d.get("isAvailable") is False:
                continue
            by_name.setdefault(d["name"], []).append(d)
        for name, same in by_name.items():
            # Newest boot first; the rest are copies somebody made by accident.
            same.sort(key=lambda d: parse_time(d.get("lastBootedAt"))
                      or datetime.datetime.min.replace(tzinfo=datetime.timezone.utc),
                      reverse=True)
            for i, d in enumerate(same):
                if d.get("state") != "Shutdown":
                    continue
                if not idle(parse_time(d.get("lastBootedAt")), now):
                    continue
                size = d.get("dataPathSize") or 0
                kept = base_name(name) in KEEP_NAMES
                if i > 0:
                    actions.append(("delete", d["udid"], name, "a second copy of this name"))
                elif not kept and size > DELETE_OVER_MB * 1024 ** 2:
                    actions.append(("delete", d["udid"], name,
                                    f"not in the fixed set, {size / GB:.1f} GB"))
                elif kept and size > ERASE_OVER_GB * GB:
                    actions.append(("erase", d["udid"], name, f"grown to {size / GB:.1f} GB"))
    return actions


def dir_size(p):
    total = 0
    for f in p.rglob("*"):
        try:
            if f.is_file() and not f.is_symlink():
                total += f.stat().st_size
        except OSError:
            pass
    return total


def newest_mtime(p):
    try:
        t = max(f.stat().st_mtime for f in p.iterdir())
    except (OSError, ValueError):
        return None
    return datetime.datetime.fromtimestamp(t, datetime.timezone.utc)


def running_avds():
    out = subprocess.run(["ps", "-axo", "command"], capture_output=True, text=True).stdout
    names = set()
    for line in out.splitlines():
        if "qemu" not in line and "emulator" not in line:
            continue
        m = re.search(r"(?:-avd\s+|@)([\w.\-]+)", line)
        if m:
            names.add(m.group(1))
    return names


def plan_android(now):
    actions, notes = [], []
    if not AVD_DIR.is_dir():
        return actions, notes
    live = running_avds()
    for avd in sorted(AVD_DIR.glob("*.avd")):
        name = avd.stem
        if name in live or not idle(newest_mtime(avd), now):
            continue
        snaps = avd / "snapshots"
        if snaps.is_dir():
            size = dir_size(snaps)
            if size > SNAPSHOT_OVER_GB * GB:
                actions.append(("snapshots", snaps, name, f"{size / GB:.1f} GB of quick-boot snapshots"))
        data = sum(f.stat().st_size for f in avd.glob("userdata-qemu.img*") if f.is_file())
        if data > ANDROID_DATA_WARN_GB * GB:
            notes.append(f"{name} holds {data / GB:.1f} GB of app data; to clear it: "
                         f"~/Library/Android/sdk/emulator/emulator -avd {name} -wipe-data")
    return actions, notes


def plan_worktrees(now):
    import checkouts
    actions = []
    for w in checkouts.worktrees()[1:]:
        path = pathlib.Path(w["path"])
        if WORKTREES not in path.parents:
            continue
        s = checkouts.state(path)
        can, _ = checkouts.removable(s)
        if not can:
            continue
        gitfile = path / ".git"
        last = None
        try:
            gitdir = pathlib.Path(gitfile.read_text().split("gitdir:", 1)[1].strip())
            last = newest_mtime(gitdir)
        except (OSError, IndexError):
            continue
        if not idle(last, now):
            continue
        actions.append(("worktree", path, path.name, "clean and on origin/main"))
    return actions


def free_gb():
    return shutil.disk_usage(str(HOME)).free / GB


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--if-low", type=float, metavar="GB",
                    help="apply, but only when less than this many GB are free; silent otherwise")
    args = ap.parse_args()

    before = free_gb()
    if args.if_low is not None:
        if before >= args.if_low:
            return 0
        args.apply = True
        print(f"devices_tidy: {before:.0f} GB free, under {args.if_low:.0f}, tidying test phones and worktrees")

    now = datetime.datetime.now(datetime.timezone.utc)
    sims = {}
    if shutil.which("xcrun"):      # not on a Linux runner
        sims = json.loads(subprocess.run(["xcrun", "simctl", "list", "devices", "-j"],
                                         capture_output=True, text=True).stdout or "{}").get("devices", {})
    actions = plan_simulators(sims, now)
    android, notes = plan_android(now)
    actions += android
    actions += plan_worktrees(now)

    if not actions and not notes:
        if args.if_low is None:
            print("nothing to tidy")
        return 0

    for kind, target, name, why in actions:
        label = {"delete": "delete simulator", "erase": "erase simulator",
                 "snapshots": "clear snapshots of", "worktree": "remove worktree"}[kind]
        if not args.apply:
            print(f"would {label} {name} ({why})")
            continue
        if kind in ("delete", "erase"):
            r = subprocess.run(["xcrun", "simctl", kind, target], capture_output=True, text=True)
            ok = r.returncode == 0
        elif kind == "snapshots":
            for child in target.iterdir():
                shutil.rmtree(child, ignore_errors=True) if child.is_dir() else child.unlink()
            ok = True
        else:
            r = subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", str(target)],
                               capture_output=True, text=True)
            ok = r.returncode == 0
        print(f"{'did' if ok else 'COULD NOT'} {label} {name} ({why})")
    if args.apply:
        subprocess.run(["xcrun", "simctl", "delete", "unavailable"], capture_output=True)
    for n in notes:
        print("note: " + n)
    if args.apply:
        print(f"devices_tidy: {before:.0f} GB free before, {free_gb():.0f} GB after")
    return 0


if __name__ == "__main__":
    sys.exit(main())
