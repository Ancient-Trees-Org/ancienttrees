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
            for sid, when, what in trees_without_a_verdict(key, cut_ts):
                out.append("tree sent %s without a verdict: submission %s (%s)" % (when[:10], sid, what))
        except Exception as e:  # noqa: BLE001
            out.append("tree submissions unreadable (%s)" % str(e)[:60])
        try:
            os.environ["SUPABASE_SERVICE_KEY"] = key
            import feedback
            for r in feedback.unhandled() or []:
                if (r.get("created_at") or "9999") < cut_ts:
                    out.append("feedback without a verdict: %s" % r["id"])
        except Exception as e:  # noqa: BLE001
            out.append("feedback unreadable (%s)" % str(e)[:60])
    return out


def trees_without_a_verdict(key, cut_ts):
    """Every tree or city a stranger sent before cut_ts that has no verdict
    anywhere, counted from when THEY SENT it (Hidde, 2026-11-17: the stub
    check above counts from the day a stub was written, so a tip of 11-15
    stubbed on 11-17 looked new; 23 trees were late while the alarm said 3).

    A verdict is any of: the row's own outcome; a judgement with a verdict
    under tip:<id>, lead:<sighting> or sight:<sighting>; a lead or a processed
    photograph that is no longer waiting; or a published tree whose
    found_by_reader names the sighting or tip-<id>."""
    import glob
    import inbox
    import ours
    rows = inbox.get("/rest/v1/submissions?select=id,created_at,kind,tree,city,outcome,user_id"
                     "&kind=in.(tree,city)&outcome=is.null&created_at=lt.%s&order=created_at.asc" % cut_ts, key) or []
    verdicts = set()
    try:
        for j in json.load(open(os.path.join(ROOT, "data", "judgements.json")))["judgements"]:
            if j.get("verdict"):
                verdicts.add(str(j["id"]).lower())
    except (OSError, ValueError):
        pass
    decided = set()
    try:
        for l in json.load(open(os.path.join(ROOT, "data", "leads", "_sightings.json")))["leads"]:
            if l.get("status") != "lead" or l.get("hold"):
                decided.add((l.get("sighting_id") or "").lower())
    except (OSError, ValueError):
        pass
    try:
        for k, v in json.load(open(os.path.join(ROOT, "data", "sightings-processed.json")))["done"].items():
            if v.get("outcome") not in ("lead", None):
                decided.add(k.lower())
    except (OSError, ValueError):
        pass
    for f in glob.glob(os.path.join(ROOT, "data", "cities", "*.json")):
        try:
            for t in json.load(open(f, encoding="utf-8")).get("trees") or []:
                fbr = t.get("found_by_reader") or {}
                if fbr.get("sighting_id"):
                    decided.add(str(fbr["sighting_id"]).lower())
        except (OSError, ValueError):
            continue
    out = []
    for r in rows:
        if ours.is_ours(r.get("user_id")):
            continue
        sid = str(r["id"])
        tree = (r.get("tree") or "").strip().lower()
        keys = {"tip:" + sid, "lead:" + tree, "sight:" + tree, sid}
        if keys & verdicts or tree in decided or ("tip-" + sid) in decided:
            continue
        out.append((sid, r.get("created_at") or "", (r.get("city") or r.get("tree") or "")[:40]))
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
