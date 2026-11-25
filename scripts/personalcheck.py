#!/usr/bin/env python3
"""Refuse a push that writes Hidde's personal situation into this public repo.

Hidde, 2026-11-25: "mss goed idee om niet meer dit soort persoonlijke dingen
erin te zetten", after the logs were found to name his job ending, his old
work address and a benefits question. The repository is public: his job, his
income, a benefits agency, his employer or his own circumstances do not belong
in it. They go in Claude's memory or the private store (private_store.py).

Reads only the lines a push ADDS, so research notes that quote other founders'
day jobs, and history already scrubbed, never trip it. The generic words live
here; anything too revealing to write into a public file (an employer's name
or domain) goes one per line in ~/.ancienttrees-personal-terms, which never
enters the repository and travels in the laptop backup.

    python3 scripts/personalcheck.py [<base>] [<head>]   default origin/main HEAD
"""
import re
import subprocess
import sys
from pathlib import Path

TERMS = [
    r"\bUWV\b",
    r"\bWW-",
    r"uitkering",
    r"unemployment benefit",
    r"\bhis (day )?job\b(?! to)",
    r"\bzijn baan\b",
    r"\bmijn baan\b",
    r"\b(his|zijn) (employer|werkgever)\b",
    r"\b(his|zijn) (salary|salaris|income|inkomen)\b",
    r"\bontslag",
]
PRIVATE = Path.home() / ".ancienttrees-personal-terms"
TEXT = (".md", ".txt", ".py", ".yml", ".yaml", ".json", ".ts", ".astro",
        ".swift", ".kt", ".html")


def patterns():
    pats = [re.compile(t, re.I) for t in TERMS]
    if PRIVATE.is_file():
        for line in PRIVATE.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                pats.append(re.compile(re.escape(line), re.I))
    return pats


def added_lines(base, head):
    out = subprocess.run(["git", "diff", "-U0", "--no-color", base, head],
                         capture_output=True, text=True).stdout
    path = None
    for line in out.splitlines():
        if line.startswith("+++ "):
            path = line[6:] if line.startswith("+++ b/") else None
        elif path and line.startswith("+") and path.endswith(TEXT):
            if path == "scripts/personalcheck.py":
                continue
            yield path, line[1:]


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
    head = sys.argv[2] if len(sys.argv) > 2 else "HEAD"
    pats = patterns()
    hits = []
    for path, line in added_lines(base, head):
        for p in pats:
            if p.search(line):
                hits.append(f"{path}: {line.strip()[:140]}")
                break
    if hits:
        print("Personal circumstances in a public file (job, income, benefits,")
        print("employer). Keep them in memory or the private store instead:")
        for h in hits:
            print("  " + h)
        sys.exit(1)


if __name__ == "__main__":
    main()
