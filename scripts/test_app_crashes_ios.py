#!/usr/bin/env python3
"""The iPhone's own exit reports reach health.py (2026-11-24): ExitWatch.swift
sends app_exit_abnormal with no reason, and every such row was dropped, so
the iPhone's own route could never ring. And a report rings until it is
answered, not for 48 hours.

    python3 scripts/test_app_crashes_ios.py
"""
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import app_crashes  # noqa: E402

NOW = datetime.datetime.now(datetime.timezone.utc)


def row(inst, days_ago, os_name="iOS 18.7", reason=None, last="tree_opened", build="42"):
    t = (NOW - datetime.timedelta(days=days_ago)).isoformat()
    # The columns load() selects, in order.
    return [t, inst, "app_exit_abnormal", reason, None, None, None, os_name, "43",
            "1.0.5", "[]", build, last]


def run():
    orig_q, orig_fixes = app_crashes._q, app_crashes.load_fixes
    app_crashes.load_fixes = lambda: []
    try:
        def rows_of(raw):
            app_crashes._q = lambda sql: raw
            return app_crashes.load(days=14, all_installs=True)

        one = rows_of([row("aaaaaaaa1", 1)])
        assert len(one) == 1, "the iPhone's exit report was dropped"
        r = one[0]
        assert r["reason"] == app_crashes.IOS_EXIT and r["build"] == "42", r
        assert r["signature"] == "exit on screen after tree_opened", r["signature"]
        assert app_crashes.health_line(one) is None, "one iPhone exit alone rang"

        two = rows_of([row("aaaaaaaa1", 1), row("bbbbbbbb2", 2)])
        line = app_crashes.health_line(two)
        assert line and "exit on screen after tree_opened" in line, line

        # An Android crash a week old still rings: until answered, not 48 hours.
        old = rows_of([row("cccccccc3", 7, os_name="Android 16", reason="crash", build="5")])
        assert app_crashes.health_line(old), "a week-old unanswered Android crash went quiet"

        # An Android memory kill in the background is still not ours.
        mem = rows_of([row("dddddddd4", 1, os_name="Android 16", reason="memory")])
        assert mem == [], mem
    finally:
        app_crashes._q, app_crashes.load_fixes = orig_q, orig_fixes
    print("ok: iPhone exits are kept and ring at two; unanswered crashes ring past 48 hours")


if __name__ == "__main__":
    run()
