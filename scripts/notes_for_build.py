#!/usr/bin/env python3
"""Readers' notes into the built pages (Hidde, 2026-11-27: "Ja, bouw 1 en 2").

Until today the "From people who stood here" block on a tree page was filled
in the browser by TREE_NOTES_JS, so the HTML every crawler received held only
the empty card ("Did you visit the tree?"), never the notes. The notes are the
one thing on those pages that exists nowhere else on the web, so the build
now writes them into the page and the script takes over from there.

Runs in deploy.yml before `astro build`. Reads the trees that carry a visible
note (data/tree-notes-live.json, ids only, kept by tree_notes.py --noted) and
asks Supabase's public tree_notes_for() for their notes with the publishable
key the website itself uses: the same rows any visitor's browser gets, hidden
notes left out by the function, a name only for a public profile.

Writes data/build/tree-notes.json, which is gitignored: readers' words never
live in the repository (CLAUDE.md, "Readers' words go on the page"; the ids
stay in Supabase). A failed fetch writes nothing new and never fails the
build: the pages then fall back to the empty card and the script, as before.

    python3 scripts/notes_for_build.py
"""
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIVE = os.path.join(ROOT, "data", "tree-notes-live.json")
OUT = os.path.join(ROOT, "data", "build", "tree-notes.json")
CONFIG = os.path.join(ROOT, "site", "src", "lib", "site-config.ts")
BATCH = 25


def site_config():
    text = open(CONFIG, encoding="utf-8").read()
    url = re.search(r'SUPABASE_URL\s*=\s*"([^"]+)"', text).group(1)
    key = re.search(r'SUPABASE_KEY\s*=\s*"([^"]+)"', text).group(1)
    return url, key


def fetch(url, key, ids):
    req = urllib.request.Request(
        url + "/rest/v1/rpc/tree_notes_for",
        data=json.dumps({"ids": ids}).encode(),
        headers={"apikey": key, "Authorization": "Bearer " + key,
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())


def main():
    try:
        ids = json.load(open(LIVE, encoding="utf-8")).get("trees") or []
    except (OSError, ValueError):
        print("notes for build: no data/tree-notes-live.json, nothing to do")
        return 0
    url, key = site_config()
    notes = {}
    try:
        for i in range(0, len(ids), BATCH):
            for row in fetch(url, key, ids[i:i + BATCH]) or []:
                body = (row.get("body") or "").strip()
                if not body or not row.get("tree_id"):
                    continue
                notes.setdefault(row["tree_id"], []).append({
                    "body": body,
                    "created_at": row.get("created_at"),
                    "author_name": row.get("author_name") or None,
                })
    except Exception as e:  # a build never depends on Supabase answering
        print("notes for build: Supabase did not answer (%s); pages keep the empty card" % e)
        return 0
    for rows in notes.values():
        rows.sort(key=lambda r: r.get("created_at") or "", reverse=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"notes": notes}, fh, ensure_ascii=False)
    print("notes for build: %d note(s) on %d tree(s) of %d listed"
          % (sum(len(v) for v in notes.values()), len(notes), len(ids)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
