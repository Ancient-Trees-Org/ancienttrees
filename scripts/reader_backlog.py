#!/usr/bin/env python3
"""Anything a reader sent that has waited more than a day without a verdict.

Hidde, 2026-11-17, on whether the reader system is watertight: the one thing
missing was an alarm, so a tree, photo, report or message that slips through
is seen without anybody asking. health.py reads this (a red RUNG 2 line, so
the night run deals with it first and the digest's quality line goes red), and
the digest's "Open for you" names the rows.

Counted, each only when older than MAX_HOURS:
  - verdict stubs in data/judgements.json without a verdict (photos, leads,
    tips without a photograph);
  - readers' leads still `lead` without a hold (scripts/fetch_waiting_photos.py);
  - reports in tree_reports with no outcome;
  - feedback with no ledger row (scripts/feedback.py).
Items that wait on purpose are not counted: a `needs_hidde` or `doubt` row is
already in front of him.

    python3 scripts/reader_backlog.py          exit 1 when anything is late
"""
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
MAX_HOURS = 24


def late():
    now = datetime.datetime.now(datetime.timezone.utc)
    cut_day = (now - datetime.timedelta(hours=MAX_HOURS)).date().isoformat()
    cut_ts = (now - datetime.timedelta(hours=MAX_HOURS)).strftime("%Y-%m-%dT%H:%M:%S")
    out = []
    try:
        for j in json.load(open(os.path.join(ROOT, "data", "judgements.json")))["judgements"]:
            if not j.get("verdict") and (j.get("seen") or "9999") < cut_day:
                out.append("verdict missing: %s (%s, seen %s)" % (j["id"], j.get("kind"), j.get("seen")))
    except (OSError, ValueError):
        out.append("data/judgements.json unreadable")
    try:
        import fetch_waiting_photos
        for l in fetch_waiting_photos.waiting():
            if (l.get("seen") or "9999") < cut_day:
                out.append("reader lead waiting: %s (seen %s)" % ((l.get("sighting_id") or "?")[:12], l.get("seen")))
    except Exception as e:  # noqa: BLE001
        out.append("leads unreadable (%s)" % str(e)[:60])
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    if not key:
        try:
            import inbox
            key = inbox.load_key()
        except Exception:  # noqa: BLE001
            key = None
    if key:
        try:
            import inbox
            import ours
            import tree_reports
            for r in tree_reports.rows(lambda p: inbox.get(p, key)) or []:
                if not r.get("outcome") and not ours.is_ours(r.get("user_id")) and (r.get("created_at") or "9999") < cut_ts:
                    out.append("report open: %s (%s)" % (r.get("id"), r.get("reason") or r.get("kind")))
        except Exception as e:  # noqa: BLE001
            out.append("reports unreadable (%s)" % str(e)[:60])
        try:
            os.environ["SUPABASE_SERVICE_KEY"] = key
            import feedback
            for r in feedback.unhandled() or []:
                if (r.get("created_at") or "9999") < cut_ts:
                    out.append("feedback without a verdict: %s" % r["id"])
        except Exception as e:  # noqa: BLE001
            out.append("feedback unreadable (%s)" % str(e)[:60])
    return out


def main():
    rows = late()
    if not rows:
        print("reader backlog: nothing a reader sent has waited over %dh" % MAX_HOURS)
        return 0
    print("reader backlog: %d item(s) waited over %dh" % (len(rows), MAX_HOURS))
    for r in rows:
        print("  " + r)
    return 1


if __name__ == "__main__":
    sys.exit(main())
