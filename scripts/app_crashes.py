#!/usr/bin/env python3
"""Crashes on strangers' phones as the app itself reports them to PostHog, and
whether each one has been looked into.

    python3 scripts/app_crashes.py              every crash of 14 days, with what
                                                that phone did just before it
    python3 scripts/app_crashes.py --days 3
    python3 scripts/app_crashes.py --open       only the ones nobody answered yet

WHY THIS EXISTS (Hidde, 2026-11-20: "we need a system in place where if you
find about crashes you dive into them i shouldnt have to ask you"). Five
crashes on three collectors' Android phones sat in PostHog for a day as
`app_exit_abnormal`, read by nobody: scripts/crashes.py reads only the
iPhone's MetricKit table in Supabase, so health.py never saw them and no run
took them up. This is the reader for the other route, both platforms:

  app_exit_abnormal   ExitWatch (iPhone and Android) at the next launch:
                      reason, on screen, and on Android 4+ `trace`, the
                      one-line crash note (account/ExitWatch.kt)
  app_crash_note      the note when no exit record sat beside it
  $exception          PostHog's own crash handler (CrashReporter), when it
                      delivers (it delivered none of build 3's)

A CRASH here: reason crash, crash_native or init_failure, or an ANR on
screen. A memory kill in the background is the system tidying up, not ours.

ANSWERED: an entry in data/crash-fixes.json with "platform", "signature" (the
signature this script prints) and "builds" (the build numbers it covers) or
"first_fixed_build" (every build below it). A run that dives into a crash
records what it found there in the same change, also when it found no cause
("no trace yet; build 4 carries the crash note"), so the same crash does not
ring twice. health.py rings for every open crash of the last 48 hours: rung 2.

PRIVACY: installs are printed as the first eight characters of their random
id, as scripts/posthog.py does; no account, no place beyond the tree ids the
events carry. Our own testing is cut the way the digest cuts it.
"""
import argparse
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import daily_digest as dd  # noqa: E402
import posthog as ph  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXES = os.path.join(ROOT, "data", "crash-fixes.json")
CRASH_REASONS = ("crash", "crash_native", "init_failure")


def _q(sql):
    key = ph.read_key()
    if not key:
        return None
    project, _ = dd._ph_project(key)
    if not project:
        return None
    return dd._posthog(sql, key, project)


def platform(os_name):
    return "android" if str(os_name or "").lower().startswith("android") else "ios"


def signature(row):
    """The trace's types and first line of our own code, or the bare reason."""
    trace = row.get("trace") or ""
    if not trace:
        return "no trace (%s)" % row["reason"]
    head, _, lines = trace.partition(" @ ")
    types = head.split(" (")[0]
    ours = [l for l in lines.split(" | ") if not l.startswith(("ActivityThread", "Handler", "Looper"))]
    return types + (" @ " + ours[0] if ours else "")


def load(days=14, all_installs=False):
    """Every crash of `days` days, newest first; None without a PostHog key."""
    ours = "" if all_installs else dd._ph_ours()[0]
    rows = _q("""
        SELECT timestamp, distinct_id, event, properties.reason, properties.on_screen,
               properties.trace, properties.detail, properties.os, properties.build_number,
               properties.app_version, toString(properties.$exception_list)
        FROM events
        WHERE event IN ('app_exit_abnormal', 'app_crash_note', '$exception')
              AND NOT startsWith(distinct_id, 'crash-probe')
              AND timestamp >= now() - INTERVAL %d DAY %s
        ORDER BY timestamp DESC""" % (int(days), ("AND " + ours) if ours else ""))
    if rows is None:
        return None
    out = []
    for t, inst, ev, reason, on_screen, trace, detail, os_name, build, version, exc in rows:
        if ev == "app_exit_abnormal":
            if not (reason in CRASH_REASONS or (reason == "anr" and on_screen == "yes")):
                continue
        elif ev == "app_crash_note":
            reason = "crash"
        else:
            reason = "exception"
            trace = trace or _exception_line(exc)
        r = {"at": str(t), "install": str(inst)[:8], "event": ev, "reason": reason,
             "on_screen": on_screen or "?", "trace": trace or "", "detail": detail or "",
             "os": os_name or "?", "platform": platform(os_name), "build": str(build or "?"),
             "version": version or "?"}
        r["signature"] = signature(r)
        out.append(r)
    return out


def _exception_line(raw):
    """PostHog's $exception_list as the same one line the crash note uses."""
    try:
        lst = json.loads(raw or "[]")
    except ValueError:
        return ""
    if not lst:
        return ""
    types = " < ".join(e.get("type", "?") for e in lst)
    frames = (lst[0].get("stacktrace") or {}).get("frames") or []
    ours = [f for f in reversed(frames) if f.get("in_app")][:5]
    lines = " | ".join("%s.%s:%s" % (str(f.get("module", "")).split(".")[-1], f.get("function"), f.get("lineno"))
                       for f in ours)
    return types + (" @ " + lines if lines else "")


def load_fixes():
    try:
        with open(FIXES, encoding="utf-8") as f:
            return json.load(f).get("fixes") or []
    except (OSError, ValueError):
        return []


def answer(row, fixes):
    for f in fixes:
        if f.get("platform") != row["platform"] or f.get("signature") != row["signature"]:
            continue
        if row["build"] in [str(b) for b in f.get("builds") or []]:
            return f
        first = f.get("first_fixed_build")
        if first and row["build"].isdigit() and int(row["build"]) < int(first):
            return f
    return None


def open_crashes(rows, hours=None):
    """Crashes with no answer, optionally only those of the last `hours`."""
    fixes = load_fixes()
    now = datetime.datetime.now(datetime.timezone.utc)
    out = []
    for r in rows:
        if answer(r, fixes):
            continue
        if hours is not None:
            when = datetime.datetime.fromisoformat(r["at"].replace("Z", "+00:00"))
            if when.tzinfo is None:
                when = when.replace(tzinfo=datetime.timezone.utc)
            if now - when > datetime.timedelta(hours=hours):
                continue
        out.append(r)
    return out


def health_line(rows):
    """What health.py says about open crashes of the last 48 hours, or None."""
    fresh = open_crashes(rows, hours=48)
    if not fresh:
        return None
    groups = {}
    for r in fresh:
        g = groups.setdefault((r["platform"], r["signature"]), {"n": 0, "phones": set(), "builds": set()})
        g["n"] += 1
        g["phones"].add(r["install"])
        g["builds"].add(r["build"])
    parts = ["%s build %s: %s (%d on %d phone%s)" % (
        p, "/".join(sorted(g["builds"])), sig, g["n"], len(g["phones"]), "" if len(g["phones"]) == 1 else "s")
        for (p, sig), g in sorted(groups.items(), key=lambda kv: -kv[1]["n"])]
    return ("; ".join(parts) + ". Dive in: python3 scripts/app_crashes.py --open, find the line, "
            "fix it with a test, record it in data/crash-fixes.json (CLAUDE.md rung 2)")


def before(install, at, n=8):
    """What that phone did in the ten minutes before the crash."""
    rows = _q("""
        SELECT timestamp, event, properties.tab, properties.tree
        FROM events
        WHERE startsWith(distinct_id, '%s')
              AND timestamp <= toDateTime('%s') AND timestamp >= toDateTime('%s') - INTERVAL 10 MINUTE
              AND event NOT IN ('app_exit_abnormal', 'app_crash_note', '$exception')
        ORDER BY timestamp DESC LIMIT %d""" % (install.replace("'", ""), at[:19].replace("T", " "),
                                                at[:19].replace("T", " "), n)) or []
    return list(reversed(rows))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--open", action="store_true", help="only crashes nobody answered")
    ap.add_argument("--all", action="store_true", help="keep our own testing in")
    a = ap.parse_args()
    rows = load(a.days, a.all)
    if rows is None:
        print("No PostHog key (see scripts/posthog.py).")
        return 1
    fixes = load_fixes()
    if a.open:
        rows = open_crashes(rows)
    if not rows:
        print("No crashes in %d days." % a.days)
        return 0
    for r in rows:
        f = answer(r, fixes)
        print("%s  %s  %s build %s  %s  %s  on screen %s" % (
            r["at"][:16].replace("T", " "), r["install"], r["os"], r["build"], r["event"], r["reason"], r["on_screen"]))
        print("    signature: %s" % r["signature"])
        if r["trace"]:
            print("    trace: %s" % r["trace"])
        if r["detail"]:
            print("    detail: %s" % r["detail"])
        print("    answered: %s" % ((f.get("what") or "yes") if f else "NO"))
        for t, ev, tab, tree in before(r["install"], r["at"]):
            print("      %s  %s%s%s" % (str(t)[11:19], ev, "  tab " + tab if tab else "", "  tree " + tree if tree else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
