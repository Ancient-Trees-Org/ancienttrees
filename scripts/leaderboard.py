#!/usr/bin/env python3
"""Who is most active: a leaderboard of readers, for Hidde's eyes on his Mac.

Hidde, 2026-11-22: "can you make a leaderboard of the most active users".
Counts per account, our own accounts left out (ours.py):
  trees    tree or city submissions they sent
  photos   app photographs (sightings) they shared
  notes    notes they wrote on trees
  visits   trees they ticked off as visited
  saves    trees they saved to Want to go
  hearts   hearts they gave a visitor's photo
Score weighs what they give the map over what they keep for themselves:
trees 5, photos 3, notes 3, visits 1, saves 0.5, hearts 0.5.

Prints to the terminal only; names come from profiles and never go to a file
in the repository. Key as in scripts/inbox.py.

  python3 scripts/leaderboard.py            top 25
  python3 scripts/leaderboard.py --top 50
  python3 scripts/leaderboard.py --days 30  only activity in the last 30 days
"""
import argparse
import collections
import datetime
import os
import sys
import urllib.request
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inbox  # noqa: E402
import ours  # noqa: E402

WEIGHTS = {"trees": 5, "photos": 3, "notes": 3, "visits": 1, "saves": 0.5, "hearts": 0.5}
SOURCES = [
    ("trees", "submissions", "&kind=in.(tree,city)"),
    ("photos", "sightings", ""),
    ("notes", "tree_notes", ""),
    ("visits", "visited", ""),
    ("saves", "saves", ""),
    ("hearts", "photo_likes", ""),
]


def fetch_all(path, key):
    out, start, step = [], 0, 1000
    while True:
        req = urllib.request.Request(inbox.SUPA + path, headers={
            "apikey": key, "Authorization": "Bearer " + key,
            "Range": "%d-%d" % (start, start + step - 1)})
        with urllib.request.urlopen(req, timeout=30) as r:
            rows = json.load(r)
        out.extend(rows)
        if len(rows) < step:
            return out
        start += step


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--days", type=int, default=0)
    a = ap.parse_args()
    key = inbox.load_key()
    if not key:
        sys.exit("No SUPABASE_SERVICE_KEY (see scripts/inbox.py).")
    since = ""
    if a.days:
        d = (datetime.date.today() - datetime.timedelta(days=a.days)).isoformat()
        since = "&created_at=gte.%sT00:00:00" % d

    counts = collections.defaultdict(collections.Counter)
    for col, table, extra in SOURCES:
        try:
            rows = fetch_all("/rest/v1/%s?select=user_id%s%s" % (table, extra, since), key)
        except Exception as e:  # one table failing should not hide the rest
            print("  (could not read %s: %s)" % (table, e), file=sys.stderr)
            continue
        for r in rows:
            uid = r.get("user_id")
            if uid and not ours.is_ours(uid):
                counts[uid][col] += 1

    names = {p["user_id"]: p.get("display_name") or "?"
             for p in fetch_all("/rest/v1/profiles?select=user_id,display_name", key)}

    board = []
    for uid, c in counts.items():
        score = sum(WEIGHTS[k] * c[k] for k in WEIGHTS)
        board.append((score, uid, c))
    board.sort(key=lambda t: (-t[0], -t[2]["trees"], -t[2]["photos"]))

    span = "last %d days" % a.days if a.days else "all time"
    print("Most active readers, %s (%d active accounts)\n" % (span, len(board)))
    cols = list(WEIGHTS)
    print("%3s  %-24s %6s  " % ("#", "name", "score") + " ".join("%6s" % k for k in cols))
    for i, (score, uid, c) in enumerate(board[:a.top], 1):
        name = names.get(uid, "(no profile)")[:24]
        print("%3d  %-24s %6g  " % (i, name, score) + " ".join("%6d" % c[k] for k in cols))
    tot = collections.Counter()
    for _, _, c in board:
        tot.update(c)
    print("\n     %-24s %6s  " % ("all readers", "") + " ".join("%6d" % tot[k] for k in cols))


if __name__ == "__main__":
    main()
