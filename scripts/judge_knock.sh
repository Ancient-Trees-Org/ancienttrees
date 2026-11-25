#!/usr/bin/env bash
# Start the reader judge when GitHub dropped its cron (2026-11-25).
#
# reader-judge.yml asks for a run every 15 minutes; on 2026-11-25 GitHub
# delivered about one an hour and none for three hours from 17:26 UTC, while
# readers' trees waited. A workflow_dispatch is never dropped, so knock.yml and
# uptime.yml, two more independent crons, each call this: when no judge run
# is in flight and none started in the last 20 minutes, dispatch one with
# poll=yes, which polls first exactly as the cron does (no agent unless a
# reader sent something). Needs GH_TOKEN with actions: write.
set -uo pipefail
REPO="${GITHUB_REPOSITORY:?}"
RUNS=$(gh api "repos/$REPO/actions/workflows/reader-judge.yml/runs?per_page=10" 2>/dev/null || echo "")
if [ -z "$RUNS" ]; then echo "judge history unreadable; nothing to do"; exit 0; fi
INFLIGHT=$(echo "$RUNS" | jq '[.workflow_runs[] | select(.status != "completed")] | length')
if [ "$INFLIGHT" -gt 0 ]; then echo "a judge run is in flight"; exit 0; fi
LAST=$(echo "$RUNS" | jq -r '.workflow_runs[0].created_at // empty')
if [ -n "$LAST" ]; then
  AGE=$(( $(date -u +%s) - $(date -u -d "$LAST" +%s) ))
  echo "last judge run started $(( AGE / 60 ))m ago"
  if [ "$AGE" -lt 1200 ]; then echo "recent enough"; exit 0; fi
fi
gh workflow run reader-judge.yml -R "$REPO" -f poll=yes && echo "judge dispatched" || echo "dispatch failed"
exit 0
