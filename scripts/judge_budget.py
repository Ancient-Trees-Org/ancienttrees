#!/usr/bin/env python3
"""How many agent minutes the reader judge spent, for the digest.

Found 2026-11-17: on its first day the reader judge ran its Opus agent 17
times for 79 minutes, and run_health.py counts only the night run, so none of
it was seen. This adds up the "Judge and publish" step of every
reader-judge.yml run (the agent itself; the ten-minute wait and the intake
cost no tokens). It never stops the judge (Hidde, same day: "ik heb liever
niet dat die stopt"); it only makes the cost visible, in the daily digest.

    python3 scripts/judge_budget.py            minutes yesterday, today and in 7 days
"""
import datetime
import json
import subprocess
import sys

REPO = "burgmanshidde-ancienttrees/ancienttrees"


def _api(path):
    out = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=60)
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip()[:200])
    return json.loads(out.stdout)


def minutes_by_day(since):
    """{date: agent minutes} for reader-judge runs created on or after `since`."""
    days = {}
    page = 1
    while True:
        doc = _api("repos/%s/actions/workflows/reader-judge.yml/runs?per_page=100&page=%d&created=%%3E%%3D%s"
                   % (REPO, page, since.isoformat()))
        runs = doc.get("workflow_runs") or []
        for r in runs:
            if r.get("conclusion") in ("cancelled", "skipped"):
                continue
            for job in _api("repos/%s/actions/runs/%s/jobs" % (REPO, r["id"])).get("jobs") or []:
                for s in job.get("steps") or []:
                    if s.get("name") != "Judge and publish" or s.get("conclusion") == "skipped" or not s.get("started_at"):
                        continue
                    end = s.get("completed_at") or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                    ta = datetime.datetime.fromisoformat(s["started_at"].replace("Z", "+00:00"))
                    tb = datetime.datetime.fromisoformat(end.replace("Z", "+00:00"))
                    d = ta.date().isoformat()
                    days[d] = days.get(d, 0.0) + max(0.0, (tb - ta).total_seconds() / 60)
        if len(runs) < 100:
            return days
        page += 1


def line(today=None):
    """One sentence for the digest, or None when it cannot be counted."""
    today = today or datetime.datetime.now(datetime.timezone.utc).date()
    try:
        days = minutes_by_day(today - datetime.timedelta(days=7))
    except Exception:  # noqa: BLE001
        return None
    y = days.get((today - datetime.timedelta(days=1)).isoformat(), 0)
    week = sum(v for k, v in days.items() if k < today.isoformat())
    return "Reader judge: %d agent minutes yesterday, %d in the last 7 days." % (round(y), round(week))


def main():
    today = datetime.datetime.now(datetime.timezone.utc).date()
    try:
        days = minutes_by_day(today - datetime.timedelta(days=7))
    except Exception as e:  # noqa: BLE001
        print("judge_budget: could not count (%s)" % e)
        return 0
    print("reader judge: %d agent minutes today, %d yesterday, %d in 7 days" % (
        round(days.get(today.isoformat(), 0)),
        round(days.get((today - datetime.timedelta(days=1)).isoformat(), 0)),
        round(sum(days.values()))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
