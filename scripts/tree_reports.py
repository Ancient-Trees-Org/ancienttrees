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
