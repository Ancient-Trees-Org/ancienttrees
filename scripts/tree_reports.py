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
#   python3 scripts/tree_reports.py --close <id> holds|open_question   (no reply: a run writes none)
#   python3 scripts/tree_reports.py --thank pin|dead <id> <tree id> ["name"]   standard mail, closed changed
#   python3 scripts/tree_reports.py --thank pin 0 <tree id> --dry              print it only
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


# The standard thank-you for the two reports we act on most (Hidde,
# 2026-11-17: a moved pin earns "bedankt, het is live, bekijk het hier, en we
# horen graag als je nog wat anders vindt"; "zelfde voor dood"). Written as the
# reply_text of a `changed` row, so contributor_reply.py mails it at the knock
# after mailcheck, like any other answer.
THANKS = {
    "pin": ("Thank you for showing us where {name} really stands. We checked "
            "it and moved the pin, so the next person finds it:\n\n{link}\n\n"
            "If you notice anything else that is off, or know a tree we are "
            "missing, we would love to hear it. Every correction like yours "
            "makes the map a little better.\n\n"
            "Ancient Trees\nhttps://ancienttrees.app\n"),
    "dead": ("Thank you for telling us about {name}. We checked, and we have "
             "taken it off the map, so nobody goes looking for a tree that "
             "is no longer there.\n\n"
             "If you notice anything else that is off, or know a tree we are "
             "missing, we would love to hear it. Every report like yours makes "
             "the map a little better.\n\n"
             "Ancient Trees\nhttps://ancienttrees.app\n"),
}


def tree_name_and_link(tree_id):
    """The tree's name from our data and its page from the site's own feed
    (contributor_reply.tree_pages, never a slug rule written twice)."""
    import glob
    import json
    import os
    import sys
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    name = None
    for f in glob.glob(os.path.join(root, "data", "cities", "*.json")):
        for t in json.load(open(f, encoding="utf-8")).get("trees") or []:
            if t.get("id") == tree_id:
                name = t.get("name")
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import contributor_reply
    url = contributor_reply.tree_pages()[0].get(tree_id)
    link = (contributor_reply.SITE + url) if url and url.startswith("/") else (url or contributor_reply.SITE)
    return name, link


_MACHINE = (
    _re.compile(r"^Moved the pin on the map, \d+ m from the published position\. "
                r"Our pin was marked (confirmed|approximate)\.$"),
    _re.compile(r"^Collected with a photograph .*$", _re.S),
    _re.compile(r"^could not tell which tree: .*$", _re.S),
    _re.compile(r"^[A-Z]{2}\s?\d{3,5}\s?\d{3,5}$"),                 # an OS grid reference
    _re.compile(r"^-?\d{1,3}\.\d+\s*,\s*-?\d{1,3}\.\d+$"),           # a coordinate
)


def own_words(row):
    """The reader's own written words on a report, or "" when it holds only
    the chip, our app's generated line, a coordinate or a grid reference.
    Their own words are general feedback, Hidde's to read (2026-11-17)."""
    d = (row.get("detail") or "").strip()
    if not d or d.lower() == (row.get("reason") or "").strip().lower():
        return ""
    return "" if any(p.match(d) for p in _MACHINE) else d


def thank(kind, tree_id, name=None):
    found, link = tree_name_and_link(tree_id)
    name = name or found
    if not name:
        raise SystemExit("no tree %s in data/cities and no name given" % tree_id)
    return THANKS[kind].format(name=name, link=link)


def _main(argv):
    if "--thank" in argv and "--dry" in argv:
        # Print the mail without touching Supabase.
        i = argv.index("--thank")
        print(thank(argv[i + 1], argv[i + 3], argv[i + 4] if len(argv) > i + 4 and argv[i + 4] != "--dry" else None))
        return 0
    key = _key()
    if not key:
        print("tree_reports: no SUPABASE_SERVICE_KEY")
        return 1
    if "--thank" in argv:
        # --thank pin|dead <report id> <tree id> ["name"]: the standard mail,
        # closed as changed. For a dead tree run it before retire.py's commit
        # reaches the feed, or give the name, since its page is gone.
        i = argv.index("--thank")
        kind, rid, tid = argv[i + 1], argv[i + 2], argv[i + 3]
        if kind not in THANKS:
            raise SystemExit("--thank pin|dead")
        name = argv[i + 4] if len(argv) > i + 4 else None
        got = _req("/rest/v1/tree_reports?select=reason,detail&id=eq.%s" % int(rid), key) or []
        if got and own_words(got[0]):
            raise SystemExit("report %s carries the reader's own words: general feedback, "
                             "Hidde's to read. Draft to drafts/reply-reader-%s-<date>.md and "
                             "--close %s holds (BRIEF_READER_JUDGE.md 'Who answers')" % (rid, rid, rid))
        close(key, rid, "changed", thank(kind, tid, name))
        print("tree_reports: %s closed as changed with the standard %s mail" % (rid, kind))
        return 0
    if "--close" in argv:
        i = argv.index("--close")
        rid, outcome = argv[i + 1], argv[i + 2]
        if len(argv) > i + 3:
            # A run writes no answer of its own on a report (Hidde,
            # 2026-11-17): the standard mails go through --thank, anything
            # else is a draft for him.
            raise SystemExit("--close takes no reply text; use --thank pin|dead, or a draft "
                             "for Hidde (BRIEF_READER_JUDGE.md 'Who answers')")
        if outcome == "changed":
            raise SystemExit("a changed report closes through --thank pin|dead")
        close(key, rid, outcome)
        print("tree_reports: %s closed as %s" % (rid, outcome))
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
