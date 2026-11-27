#!/usr/bin/env python3
"""emulator_lock.py - one session at a time on the one Android emulator.

Found 2026-11-10: a flow walk failed with "Process crashed" because another
session ran `am force-stop app.ancienttrees.map` on the same emulator in the
middle of it. Several Android sessions share Hidde's one emulator, so every
script that installs, starts or photographs the app takes this lock first and
waits while another holds it. The lock is the operating system's (flock), so a
session that dies lets go by itself.

    from emulator_lock import emulator
    with emulator("android_parity"):
        ...

    python3 scripts/emulator_lock.py --who      # who holds it now

THE EMULATOR, NEVER HIS PHONE (2026-11-24): with Hidde's Samsung on the USB
cable and no emulator running, a bare `adb` reached the phone, and a ButtonWalk
uninstalled his Play copy of the app ("another build's signature") and put a
debug build in its place. Holding the lock now pins ANDROID_SERIAL to a running
emulator (every adb and gradle call underneath inherits it) and refuses when
none runs. A script meant for his phone does not take this lock.
"""
import contextlib
import fcntl
import os
import pathlib
import subprocess
import sys
import time

LOCK = pathlib.Path.home() / "Library" / "Caches" / "ancienttrees-emulator.lock"
ADB = str(pathlib.Path.home() / "Library" / "Android" / "sdk" / "platform-tools" / "adb")


def emulators(listing):
    """Serials of emulators in `adb devices` output; a phone on a cable is never one."""
    out = []
    for line in listing.splitlines()[1:]:
        parts = line.split()
        if len(parts) >= 2 and parts[1] == "device" and parts[0].startswith("emulator-"):
            out.append(parts[0])
    return out


def pin_to_emulator():
    """ANDROID_SERIAL set to a running emulator, or exit: never a real phone."""
    try:
        listing = subprocess.run([ADB, "devices"], capture_output=True, text=True, timeout=20).stdout
    except (OSError, subprocess.TimeoutExpired) as e:
        sys.exit(f"adb did not answer ({e}); start the emulator first")
    found = emulators(listing)
    wanted = os.environ.get("ANDROID_SERIAL")
    if wanted and wanted not in found:
        sys.exit(f"ANDROID_SERIAL={wanted} is not a running emulator; refusing (a real phone is never tested on)")
    if not found:
        sys.exit("no emulator running; refusing to use a phone on the cable. Start the emulator first.")
    # One emulator at a time (Hidde, 2026-11-27: "zullen we onthouden dat niet tegelijk
    # meer te doen"): two emulators beside a Gradle build froze his 16 GB Mac and every
    # run was lost. Stop the other one first.
    if len(found) > 1:
        sys.exit(f"{len(found)} emulators are running ({', '.join(found)}); the Mac freezes with two. Stop all but one first.")
    os.environ["ANDROID_SERIAL"] = wanted or found[0]
    return os.environ["ANDROID_SERIAL"]


@contextlib.contextmanager
def emulator(who, wait_minutes=30):
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    f = open(LOCK, "a+")
    deadline = time.time() + wait_minutes * 60
    told = False
    while True:
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            break
        except BlockingIOError:
            if not told:
                f.seek(0)
                print(f"emulator busy ({f.read().strip() or 'unknown'}); waiting", flush=True)
                told = True
            if time.time() > deadline:
                f.close()
                sys.exit(f"emulator still busy after {wait_minutes} minutes")
            time.sleep(5)
    f.seek(0)
    f.truncate()
    f.write(f"{who}, pid {os.getpid()}, since {time.strftime('%H:%M:%S')}\n")
    f.flush()
    try:
        pin_to_emulator()
        yield
    finally:
        f.seek(0)
        f.truncate()
        fcntl.flock(f, fcntl.LOCK_UN)
        f.close()


if __name__ == "__main__":
    if "--who" in sys.argv:
        print(LOCK.read_text().strip() if LOCK.exists() and LOCK.read_text().strip() else "free")
