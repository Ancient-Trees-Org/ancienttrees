#!/usr/bin/env python3
"""How many agent minutes the reader judge spent today, against its cap.

Found 2026-11-17: on its first day the reader judge ran its Opus agent 17
times for 79 minutes, and run_health.py, which the budget brake reads, counts
only the night run, so none of it was seen. This adds up the "Judge and
publish" step of every reader-judge.yml run since midnight UTC (the agent
itself; the ten-minute wait and the intake cost no tokens) and compares it
with JUDGE_DAY_MINUTES. Over it, the workflow starts no agent and the night
run, which reads readers' work first anyway, takes what waits.

The cap is a share of Hidde's DAY_BUDGET_MINUTES (200, CLAUDE.md "How runs
fire"); raising it is his call.

    python3 scripts/judge_budget.py          exit 0 under the cap, 1 over it
    python3 scripts/judge_budget.py --print  minutes today and this week
"""
import datetime
import json
import os
import subprocess
import sys

JUDGE_DAY_MINUTES = 120
REPO = "burgmanshidde-ancienttrees/ancienttrees"


def _api(path):
    out = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=60)
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip()[:200])
    return json.loads(out.stdout)


def minutes_since(since):
    """Agent minutes of reader-judge runs created on or after `since` (a date)."""
    total = 0.0
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
                    if s.get("name") != "Judge and publish" or s.get("conclusion") == "skipped":
                        continue
                    a, b = s.get("started_at"), s.get("completed_at") or datetime.datetime.now(
                        datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                    if a:
                        ta = datetime.datetime.fromisoformat(a.replace("Z", "+00:00"))
                        tb = datetime.datetime.fromisoformat(b.replace("Z", "+00:00"))
                        total += max(0.0, (tb - ta).total_seconds() / 60)
        if len(runs) < 100:
            return total
        page += 1


def main():
    today = datetime.datetime.now(datetime.timezone.utc).date()
    try:
        day = minutes_since(today)
    except Exception as e:  # noqa: BLE001
        # Unreadable is not a reason to keep readers waiting: start, and say so.
        print("judge_budget: could not count (%s); starting" % e)
        return 0
    if "--print" in sys.argv:
        week = minutes_since(today - datetime.timedelta(days=6))
        print("reader judge: %d agent minutes today (cap %d), %d in 7 days" % (round(day), JUDGE_DAY_MINUTES, round(week)))
        return 0
    print("reader judge: %d of %d agent minutes today" % (round(day), JUDGE_DAY_MINUTES))
    return 0 if day < JUDGE_DAY_MINUTES else 1


if __name__ == "__main__":
    sys.exit(main())
