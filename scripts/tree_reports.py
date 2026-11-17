#!/usr/bin/env python3
"""Reports on a tree and moved pins, read from their own table.

Step 2 of splitting submissions (Hidde, 2026-11-16: votes and tree submissions
are "hele andere dingen", the one catch-all table "een troep"; step 1 moved
votes to tree_votes). supabase/tree-reports.sql makes `tree_reports`: one row
per report (reason, the person's words filled in place, the coordinate for a
pin, and the verdict and reply fields), and a trigger moves every report still
posted to `submissions` across.

Every script that read these rows out of submissions reads them through here,
so the rest of each script keeps its old row shape:

  rows(get, since=None)    tree_reports rows in the submissions row shape
                           (kind, tree, why, location_hint, outcome, reply_text,
                           replied_at, thanked_at), each with `_table`
                           "tree_reports"; None when the table cannot answer
                           (the SQL not pasted yet), and the caller reads
                           submissions as before.
  merged(subs, reps)       submissions rows plus report rows, without the
                           submissions rows that were copied across (so a
                           report counts once) and, once the table answers,
                           without report-shaped rows still in submissions
                           that were copied. Rows with no account stay where
                           they are (the copy skips them) and are kept.
  path(row)                the REST path of a row, for a PATCH.
  is_report(row)           whether a submissions-shaped row is a report, by
                           the same rule as public.is_tree_report().

`get(path)` is any function that returns the parsed JSON of a GET with the
service key; it may raise urllib.error.HTTPError, which counts as "cannot
answer".
"""
SELECT = ("id,user_id,tree_id,tree,reason,detail,detail_at,lat,lng,location_hint,city,page,"
          "created_at,outcome,reply_text,replied_at,thanked_at,submission_id,detail_submission_id")

# Reasons that are not an answer to "Something's wrong" (WorthIt.swift notAChip).
NOT_A_CHIP = ("pin moved", "collected far", "merged", "correction")


def is_report(row):
    """public.is_tree_report(kind, why) in Python."""
    kind = row.get("kind") or ""
    w = (row.get("why") or "").strip().lower()
    return kind == "correction" or (kind == "feedback" and (
        w == "report" or w.startswith("report:") or w.startswith("report detail")))


def why_of(r):
    """The words a script used to read in `why`: "report: <chip>" with the
    follow-up after it, or the correction's own words."""
    reason = r.get("reason") or ""
    detail = (r.get("detail") or "").strip()
    if reason in NOT_A_CHIP:
        return detail or reason
    out = "report: %s" % reason
    if detail:
        out += "\nreport detail: %s" % detail
    return out


def shape(r):
    out = dict(r)
    out["_table"] = "tree_reports"
    out["kind"] = "correction" if (r.get("reason") in NOT_A_CHIP) else "feedback"
    out["why"] = why_of(r)
    out.setdefault("email", None)
    return out


class Reports(list):
    """The report rows asked for, and the ids of every submissions row ever
    copied across (from the whole table, so a follow-up copied into an older
    report is still known when only this week was asked for)."""
    copied = frozenset()


def rows(get, since=None):
    # The whole table: it is small (one row per report), and the copied ids
    # must come from all of it.
    try:
        got = get("/rest/v1/tree_reports?select=%s&order=created_at.asc" % SELECT)
    except Exception:
        return None
    if got is None or not isinstance(got, list):
        return None
    out = Reports(shape(r) for r in got
                  if not since or str(r.get("created_at") or "") >= since
                  or str(r.get("detail_at") or "") >= since)
    out.copied = frozenset(i for r in got for i in (r.get("submission_id"), r.get("detail_submission_id"))
                           if i is not None)
    return out


def copied(reps):
    return set(getattr(reps, "copied", ()) or ())


def merged(subs, reps):
    """Submissions rows and report rows as one list, oldest first; a report
    that was copied across appears once, from tree_reports."""
    if reps is None:
        return list(subs or [])
    gone = copied(reps)
    keep = [r for r in subs or [] if r.get("id") not in gone]
    out = keep + list(reps)
    out.sort(key=lambda r: str(r.get("created_at") or ""))
    return out


def path(row):
    return "/rest/v1/%s?id=eq.%s" % (row.get("_table") or "submissions", row["id"])


# ---------------------------------------------------------------------------
# The instant lane (Hidde, 2026-11-17: reports should be picked up "direct",
# like the readers' trees). The reader judge (reader-judge.yml) runs these:
#
#   python3 scripts/tree_reports.py --open        open reports from readers, words included
#   python3 scripts/tree_reports.py --count       how many are open (the workflow's gate)
#   python3 scripts/tree_reports.py --auto        close the bookkeeping rows nobody has to read
#   python3 scripts/tree_reports.py --close <id> changed|holds|open_question ["reply text"]
#
# Before 2026-11-17 nothing closed these rows: 51 sat open from 11-15 on,
# among them a Bristol grid reference for two pins and a Domesday age question.
# ---------------------------------------------------------------------------

import re as _re

SUPA = "https://caimvxiyrtifilimlkqw.supabase.co"

# A reader nudging a pin we already confirmed by a GPS fix by a few metres is
# a finger on a phone map, not a correction (CLAUDE.md: "a GPS fix at the tree
# is that evidence"). These close without a reply and wake nobody.
NUDGE_M = 30


def _key():
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import inbox
    return inbox.load_key()


def _req(p, key, method="GET", body=None):
    import json
    import urllib.request
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(SUPA + p, data=data, method=method, headers={
        "apikey": key, "Authorization": "Bearer " + key,
        "Content-Type": "application/json", "Prefer": "return=minimal"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
    return json.loads(raw) if raw else None


def open_rows(key):
    """Open reports from readers (our own accounts left out), oldest first."""
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ours
    got = rows(lambda p: _req(p, key))
    if got is None:
        return None
    return [r for r in got if not r.get("outcome") and not ours.is_ours(r.get("user_id"))]


def is_nudge(r):
    """A moved pin on a confirmed pin, under NUDGE_M metres."""
    if r.get("reason") != "pin moved":
        return False
    d = r.get("detail") or ""
    m = _re.search(r"(\d+) m from the published position", d)
    return bool(m and int(m.group(1)) <= NUDGE_M and "marked confirmed" in d)


def close(key, rid, outcome, reply=None):
    if outcome not in ("changed", "holds", "open_question"):
        raise SystemExit("outcome must be changed, holds or open_question")
    body = {"outcome": outcome}
    if reply:
        body["reply_text"] = reply.rstrip() + "\n"
    _req("/rest/v1/tree_reports?id=eq.%s" % int(rid), key, "PATCH", body)


def _main(argv):
    key = _key()
    if not key:
        print("tree_reports: no SUPABASE_SERVICE_KEY")
        return 1
    if "--close" in argv:
        i = argv.index("--close")
        rid, outcome = argv[i + 1], argv[i + 2]
        reply = argv[i + 3] if len(argv) > i + 3 else None
        if outcome == "changed" and not reply:
            # contributor_reply.py holds a changed report with no words; say
            # so here rather than leave a row that never mails.
            raise SystemExit("a changed report needs its reply text (CLAUDE.md 'Reader input')")
        close(key, rid, outcome, reply)
        print("tree_reports: %s closed as %s%s" % (rid, outcome, ", reply written" if reply else ""))
        return 0
    rs = open_rows(key)
    if rs is None:
        print("tree_reports: the table did not answer")
        return 0 if "--count" in argv else 1
    if "--auto" in argv:
        n = 0
        for r in rs:
            if is_nudge(r):
                close(key, r["id"], "holds")
                n += 1
        print("tree_reports: %d nudge(s) of a confirmed pin closed without a reply" % n)
        return 0
    if "--count" in argv:
        print(len(rs))
        return 0
    for r in rs:
        print("=" * 72)
        print("report %s   %s   reason %s" % (r["id"], str(r.get("created_at") or "")[:16], r.get("reason")))
        for f in ("city", "tree", "tree_id", "lat", "lng", "location_hint"):
            if r.get(f) not in (None, ""):
                print("  %-13s %s" % (f, r[f]))
        if (r.get("detail") or "").strip():
            print("  words:")
            for line in r["detail"].strip().splitlines():
                print("    " + line)
    print("%d open report(s) from readers" % len(rs))
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(_main(sys.argv[1:]))
