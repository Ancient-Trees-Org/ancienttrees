#!/usr/bin/env python3
"""What a reader wrote about the tree they sent becomes their note on its page.

Hidde, 2026-11-15, after finding no reader's words under "From people who
stood here" on the trees readers had sent that day: "Ja, bouw het", and
"maar zeg dus ook dat het openbaar wordt". The convention (CONVENTIONS.md,
"The words somebody types with a photograph"): on Google Maps, komoot,
AllTrails and iNaturalist the words typed with a photo are public on the place,
under the person's name. Ours kept them in a field only we read.

What this does, at each knock: for every published tree a reader found
(`found_by_reader`), it takes the words that reader typed when sending it and
writes them as THEIR note on that tree (supabase/tree-notes.sql: one note per
person per tree, the name shown only when their profile is public, else
"A visitor"). A note they already wrote is never touched (ignore-duplicates on
the primary key), so this only fills an empty slot.

ONLY WORDS TYPED UNDER A FIELD THAT SAID SO. People who wrote before the field
told them it would show on the page wrote to us, not to the next visitor, so
their words stay where they were (quoted in the story, unnamed). The cut-off
per surface is a date below:
  WEB_SINCE  the deploy that put "Shows on the tree's page" under the website
             form's "Why is it remarkable?" (site/src/pages/contribute.astro).
  APP_SINCE  None until the app build that carries the same line under "What
             makes this tree special?" (TreeDetail.swift EditableField.hint) is
             live in the App Store; the session that releases it sets the date.
Our own accounts (scripts/ours.py) are left out. A text that is only a link is
left out: it is a pointer for us, not a word for a visitor.

    python3 scripts/reader_text_notes.py            dry run: prints what it would write
    python3 scripts/reader_text_notes.py --write    writes (needs SUPABASE_SERVICE_KEY)

Record: data/reader-text-notes.json, (code, tree_id) -> date. Codes, never ids,
and never the words (they live in Supabase).
"""
import datetime
import glob
import json
import os
import re
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import people  # noqa: E402
import ours  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUPA = "https://caimvxiyrtifilimlkqw.supabase.co"
KEY = os.environ.get("SUPABASE_SERVICE_KEY")
RECORD = os.path.join(ROOT, "data", "reader-text-notes.json")

WEB_SINCE = "2026-11-15T19:00:00+00:00"
APP_SINCE = None

ONLY_A_LINK = re.compile(r"^\s*(https?://)?[\w.-]+\.[a-z]{2,}(/\S*)?\s*$", re.I)


def eligible(text, sent_at, since):
    """The rule, pure: words typed after the field said they show, and more
    than a link. Returns the body to write, or None."""
    if not since or not sent_at or not text:
        return None
    if sent_at[:19] < since[:19]:
        return None
    body = text.strip()
    if not body or ONLY_A_LINK.match(body):
        return None
    return body[:1000]


def supa(path, method="GET", body=None, prefer="return=minimal"):
    h = {"apikey": KEY, "Authorization": "Bearer " + KEY}
    data = None
    if body is not None:
        h["Content-Type"] = "application/json"
        h["Prefer"] = prefer
        data = json.dumps(body).encode()
    req = urllib.request.Request(SUPA + path, data=data, method=method, headers=h)
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
        return json.loads(raw) if raw else None


def reader_trees():
    """(tree_id, sighting_id or None, tip submission id or None) per reader-found tree."""
    out = []
    for fp in glob.glob(os.path.join(ROOT, "data", "cities", "*.json")):
        try:
            c = json.load(open(fp, encoding="utf-8"))
        except Exception:
            continue
        for t in c.get("trees", []):
            f = t.get("found_by_reader") or {}
            sid = str(f.get("sighting_id") or "")
            if not sid:
                continue
            if sid.startswith("tip-"):
                out.append((t["id"], None, sid[4:]))
            else:
                out.append((t["id"], sid, None))
    return out


def candidates():
    found = []
    for tree_id, sid, tip in reader_trees():
        if sid and APP_SINCE:
            rows = supa(f"/rest/v1/sightings?id=eq.{sid}&select=user_id,note,created_at") or []
            for r in rows:
                body = eligible(r.get("note"), r.get("created_at"), APP_SINCE)
                if body:
                    found.append((tree_id, r["user_id"], body))
        if tip and WEB_SINCE:
            rows = supa(f"/rest/v1/submissions?id=eq.{tip}&select=user_id,why,created_at") or []
            for r in rows:
                body = eligible(r.get("why"), r.get("created_at"), WEB_SINCE)
                if body and r.get("user_id"):
                    found.append((tree_id, r["user_id"], body))
    return [(t, u, b) for t, u, b in found if not ours.is_ours(u)]


def main(argv):
    if not KEY:
        print("reader_text_notes: no SUPABASE_SERVICE_KEY, nothing done")
        return 0
    write = "--write" in argv
    try:
        rec = json.load(open(RECORD, encoding="utf-8"))
    except Exception:
        rec = {"_note": "Readers' own words written as their note on the tree they sent: "
                        "(code|tree_id) -> date. Codes, never ids; the words stay in Supabase.",
               "written": {}}
    n = 0
    for tree_id, uid, body in candidates():
        key = f"{people.ref(uid)}|{tree_id}"
        if key in rec["written"]:
            continue
        if not write:
            print(f"  would write {key}: {body[:80]}")
            continue
        supa("/rest/v1/tree_notes?on_conflict=user_id,tree_id", "POST",
             {"user_id": uid, "tree_id": tree_id, "body": body},
             prefer="resolution=ignore-duplicates,return=minimal")
        rec["written"][key] = datetime.date.today().isoformat()
        n += 1
    if write:
        with open(RECORD, "w", encoding="utf-8") as fh:
            json.dump(rec, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
    print(f"reader_text_notes: {n} written" if write else "reader_text_notes: dry run")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
