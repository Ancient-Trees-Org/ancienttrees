#!/usr/bin/env python3
"""General feedback: what was handled, and what is open for Hidde.

Hidde, 2026-11-17: "Hou er ergens bij of feedback is behandeld of niet ...
wat ik moet zien, zijn de dingen die openstaan, waar je over twijfelt of waar
je mijn hulp bij nodig hebt ... de makkelijke gevallen moet jij gewoon
behandelen". And the same day: "lijkt me beter als ik dat zelf lees" about a
mail going out on its own, so handling never sends a reply: a reply is drafted
and the row is `needs_hidde` until he says yes.

What counts as feedback: a `submissions` row of kind `feedback` from a person
who is not us, that is not a one-tap vote ("worth it", "not worth it", "vote
undone": Hidde, 2026-11-17, "worth it hoeven we in principe niks mee") and
not a report already copied to `tree_reports` (those are the reader judge's,
scripts/tree_reports.py). Trees, ambassador requests and corrections have
their own ledgers (judgements.json, ambassadors.json, tree_reports).

The ledger, data/feedback-ledger.json, is public: it holds the row id, a
status and OUR one-line summary of what was done, never the person's words or
anything that names them (their words stay in Supabase and on the local
digest page).

    python3 scripts/feedback.py --open            unhandled feedback, words in full
    python3 scripts/feedback.py --count           how many wait (for the workflow gate)
    python3 scripts/feedback.py --close <id> handled|needs_hidde|doubt "what was done"
    python3 scripts/feedback.py --close <id> bug <code-audit BUG id> "what was done"
    python3 scripts/feedback.py --for-hidde       the rows that need him (digest)

Statuses: `handled` (done, nothing for him: a fix made, a lead recorded, an
idea filed, no answer needed), `bug` (something broken: the BUG row it names
in data/code-audit.json is rung-2 work until a test closes it, never his
call), `needs_hidde` (a reply drafted for his yes, or a decision that is
his), `doubt` (we could not settle it; say why).
"""
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
LEDGER = os.path.join(ROOT, "data", "feedback-ledger.json")
VOTES = ("worth it", "not worth it", "vote undone")
STATUSES = ("handled", "needs_hidde", "doubt", "bug")
AUDIT = os.path.join(ROOT, "data", "code-audit.json")


def bug_ids():
    """Every BUG row id in data/code-audit.json (escaped.py --add writes them)."""
    try:
        doc = json.load(open(AUDIT, encoding="utf-8"))
    except (OSError, ValueError):
        return set()
    return {f.get("id") for f in doc.get("findings", []) if f.get("kind") == "BUG"}


def ledger():
    try:
        return json.load(open(LEDGER, encoding="utf-8"))
    except (OSError, ValueError):
        return {"_note": "General feedback rows (submissions, kind feedback): id -> status, our "
                         "one-line summary, date. Never the person's words. scripts/feedback.py.",
                "rows": {}}


def save(doc):
    with open(LEDGER, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")


def _key():
    k = os.environ.get("SUPABASE_SERVICE_KEY")
    if k:
        return k
    try:
        import inbox
        return inbox.load_key()
    except Exception:  # noqa: BLE001
        return None


def unhandled():
    """Feedback rows with no ledger entry, newest last."""
    import inbox
    import ours
    key = _key()
    if not key:
        return None
    rows = inbox.get("/rest/v1/submissions?select=id,user_id,page,tree,city,why,outcome,created_at"
                     "&kind=eq.feedback&order=created_at.asc", key) or []
    try:
        import tree_reports
        copied = tree_reports.copied(tree_reports.rows(lambda p: inbox.get(p, key)))
    except Exception:  # noqa: BLE001
        copied = set()
    done = ledger()["rows"]
    out = []
    for r in rows:
        words = (r.get("why") or "").strip()
        if ours.is_ours(r.get("user_id")) or r["id"] in copied or str(r["id"]) in done:
            continue
        if words.lower().startswith(VOTES) or words.lower().startswith("report"):
            continue
        out.append(r)
    return out


def for_hidde():
    rows = ledger()["rows"]
    return sorted(((k, v) for k, v in rows.items() if v.get("status") in ("needs_hidde", "doubt")),
                  key=lambda kv: kv[1].get("date") or "")


def main():
    a = sys.argv[1:]
    if "--close" in a:
        i = a.index("--close")
        rid, status, what = a[i + 1], a[i + 2], " ".join(a[i + 3:])
        if status not in STATUSES:
            print("status must be one of " + ", ".join(STATUSES))
            return 2
        row = {"status": status, "what": what, "date": datetime.date.today().isoformat()}
        if status == "bug":
            # A READER'S BUG IS A BUG, NOT HIDDE'S CALL (2026-11-24: report
            # 1491, the country that would not stay, sat two days as
            # needs_hidde while a fix was the work). It names the BUG row in
            # data/code-audit.json, which makes it rung-2 work until a test
            # closes it; a reply drafted for his yes still shows in drafts/.
            bug, _, what = what.partition(" ")
            if bug not in bug_ids():
                print("bug needs the id of a BUG row in data/code-audit.json first "
                      "(python3 scripts/escaped.py --add ... --found-by reader), then: "
                      "--close <id> bug <bug-id> \"what was done\"")
                return 2
            row.update(bug=bug, what=what.strip())
        doc = ledger()
        doc["rows"][str(rid)] = row
        save(doc)
        print("%s: %s" % (rid, status))
        return 0
    if "--for-hidde" in a:
        for rid, v in for_hidde():
            print("%s  %-11s %s  %s" % (rid, v["status"], v.get("date"), v.get("what")))
        return 0
    rows = unhandled()
    if rows is None:
        print("feedback: no SUPABASE_SERVICE_KEY, nothing read")
        return 0
    if "--count" in a:
        print(len(rows))
        return 0
    for r in rows:
        print("=" * 60)
        print("%s  %s  %s  %s %s" % (r["id"], (r.get("created_at") or "")[:16], r.get("page") or "",
                                     r.get("tree") or "", r.get("city") or ""))
        print((r.get("why") or "").strip())
    print("=" * 60)
    print("%d feedback message(s) without a verdict; %d open for Hidde" % (len(rows), len(for_hidde())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
