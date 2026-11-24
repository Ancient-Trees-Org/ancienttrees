#!/usr/bin/env python3
"""Rewrite the repo owner in the files that name it, for the move of
hidde-ancient-trees/ancienttrees into a GitHub organisation (2026-11-24,
Hidde: a second owner needs an organisation; checklist in
.github/ORG_MOVE.md).

    python3 scripts/move_to_org.py <org>            dry run: prints what changes
    python3 scripts/move_to_org.py <org> --write    writes the files

The commit identity lines in the workflows (git config user.name
"hidde-ancient-trees") stay: that account still exists and still pushes.
"""
import pathlib
import sys

OLD_OWNER = "hidde-ancient-trees"
ROOT = pathlib.Path(__file__).resolve().parent.parent

# Every place that names the owner as part of a repo path, found with
# git grep on 2026-11-24. A new one goes here.
FILES = [
    "scripts/brief.py",
    "scripts/daily_digest.py",
    "scripts/geo.py",
    "scripts/judge_budget.py",
    "scripts/release.py",
    "site/src/lib/site-config.ts",
    "supabase/reader-judge-trigger.sql",
]
REPOS = ["ancienttrees-open", "ancienttrees"]  # longest first


def rewrite(text, org):
    for repo in REPOS:
        text = text.replace(f"{OLD_OWNER}/{repo}", f"{org}/{repo}")
    return text


def main(argv):
    if len(argv) < 2 or argv[1].startswith("-"):
        print(__doc__)
        return 2
    org = argv[1]
    write = "--write" in argv
    changed = 0
    for rel in FILES:
        path = ROOT / rel
        old = path.read_text()
        new = rewrite(old, org)
        if old == new:
            print(f"  unchanged  {rel}")
            continue
        changed += 1
        for a, b in zip(old.splitlines(), new.splitlines()):
            if a != b:
                print(f"  {rel}\n    - {a.strip()}\n    + {b.strip()}")
        if write:
            path.write_text(new)
    print(f"{changed} file(s) {'written' if write else 'would change'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
