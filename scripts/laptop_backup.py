#!/usr/bin/env python3
"""Nightly encrypted backup of what lives only on Hidde's laptop.

Hidde, 2026-11-24: "maar hebben we dan niet nog steeds een probleem als ik deze
laptop kwijt raak?" GitHub holds the code and Supabase the database; this
covers the rest:

  - the key and env files in the home folder (~/.ancienttrees-*), the Android
    upload key among them
  - repository files that are not on GitHub: changed and untracked files, and
    the gitignored private files under data/ and drafts/ (outreach, replies)
  - Claude's project memory (~/.claude/projects/<this repo>/memory)

One archive, AES-256 with openssl (pbkdf2), written to the Ancient Trees Google
Drive (hidde@ancienttrees.app, Drive for desktop), the last KEEP kept. The
passphrase lives in the Mac keychain, put there by Hidde himself:

    security add-generic-password -a "$USER" -s ancienttrees-backup -w

(it asks for the passphrase twice; nothing else ever sees it). Keep the same
passphrase in his password manager: without it no archive opens.

    python3 scripts/laptop_backup.py            make tonight's archive
    python3 scripts/laptop_backup.py --verify   open the newest and list it
    python3 scripts/laptop_backup.py --dry-run  list what would go in

Restore: openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 -in <file> -out b.tar.gz
then tar -xzf b.tar.gz (paths inside are home/..., repo/..., memory/...).
Runs nightly from ~/Library/LaunchAgents/app.ancienttrees.laptop-backup.plist.
"""
import datetime
import os
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

HOME = Path.home()
REPO = Path(__file__).resolve().parent.parent
MEMORY = HOME / ".claude/projects/-Users-hidde-Developer-Ancienttrees/memory"
DRIVE = HOME / "Library/CloudStorage/GoogleDrive-hidde@ancienttrees_app/My Drive"
DEST = DRIVE / "Ancient Trees backup"
KEEP = 14
ITER = "200000"
KEYCHAIN_SERVICE = "ancienttrees-backup"
# Ignored files are taken only from these folders: the rest (build output,
# worktrees, out/, photos) is rebuildable or lives elsewhere.
IGNORED_FROM = ("data/", "drafts/", "android/local.properties",
                ".claude/settings.local.json")
MAX_FILE = 50 * 1024 * 1024


def git_list(*args):
    out = subprocess.run(["git", "-C", str(REPO), "ls-files", "-z", *args],
                         capture_output=True, check=True).stdout
    return [p for p in out.decode().split("\0") if p]


def repo_files():
    changed = git_list("-m", "-o", "--exclude-standard")
    ignored = [p for p in git_list("-o", "-i", "--exclude-standard")
               if p.startswith(IGNORED_FROM)]
    files = []
    for rel in sorted(set(changed + ignored)):
        p = REPO / rel
        if p.is_file() and p.stat().st_size <= MAX_FILE:
            files.append((p, "repo/" + rel))
    return files


def home_files():
    return [(p, "home/" + p.name) for p in sorted(HOME.glob(".ancienttrees-*"))
            if p.is_file()]


def memory_files():
    if not MEMORY.is_dir():
        return []
    return [(p, "memory/" + str(p.relative_to(MEMORY)))
            for p in sorted(MEMORY.rglob("*")) if p.is_file()]


def passphrase():
    r = subprocess.run(["security", "find-generic-password", "-s",
                        KEYCHAIN_SERVICE, "-w"], capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip():
        sys.exit("No passphrase in the keychain (service "
                 f"'{KEYCHAIN_SERVICE}'); see the docstring for the command.")
    return r.stdout.rstrip("\n")


def openssl(mode, src, dst, pw):
    env = dict(os.environ, AT_BACKUP_PASS=pw)
    cmd = ["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-iter", ITER,
           "-pass", "env:AT_BACKUP_PASS", "-in", str(src), "-out", str(dst)]
    cmd.insert(2, "-d" if mode == "decrypt" else "-salt")
    subprocess.run(cmd, env=env, check=True)


def archives():
    return sorted(DEST.glob("laptop-*.tar.gz.enc"), key=lambda p: p.stat().st_mtime)


def make(dry):
    files = home_files() + repo_files() + memory_files()
    total = sum(p.stat().st_size for p, _ in files)
    print(f"{len(files)} files, {total / 1e6:.1f} MB before compression "
          f"(home {len(home_files())}, memory {len(memory_files())})")
    if dry:
        for _, name in files:
            print("  " + name)
        return
    if not DRIVE.is_dir():
        sys.exit(f"Drive folder not found: {DRIVE}")
    pw = passphrase()
    DEST.mkdir(exist_ok=True)
    for stale in DEST.glob("*.part"):
        remove(stale)
    # A file Drive is still uploading cannot be overwritten or deleted, so
    # every archive gets its own name and nothing is ever replaced.
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    out = DEST / f"laptop-{stamp}.tar.gz.enc"
    with tempfile.TemporaryDirectory() as tmp:
        tgz = Path(tmp) / "b.tar.gz"
        with tarfile.open(tgz, "w:gz") as tar:
            for p, name in files:
                tar.add(p, arcname=name, recursive=False)
        part = out.with_suffix(".part")
        openssl("encrypt", tgz, part, pw)
        part.rename(out)
    print(f"wrote {out.name} ({out.stat().st_size / 1e6:.1f} MB)")
    for old in archives()[:-KEEP]:
        remove(old)


def remove(path):
    """Delete, or leave it for the next night when Drive holds it."""
    try:
        path.unlink()
        print(f"removed {path.name}")
    except PermissionError:
        print(f"kept {path.name} for now (Drive is busy with it)")


def verify():
    found = archives()
    if not found:
        sys.exit("no archive yet")
    newest = found[-1]
    with tempfile.TemporaryDirectory() as tmp:
        tgz = Path(tmp) / "b.tar.gz"
        openssl("decrypt", newest, tgz, passphrase())
        with tarfile.open(tgz) as tar:
            names = tar.getnames()
    groups = {}
    for n in names:
        groups[n.split("/")[0]] = groups.get(n.split("/")[0], 0) + 1
    print(f"{newest.name} opens: {len(names)} files {groups}")


if __name__ == "__main__":
    if "--verify" in sys.argv:
        verify()
    else:
        make("--dry-run" in sys.argv)
