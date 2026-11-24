#!/usr/bin/env python3
"""One crash on a store build with no answer on file is an act item
(Hidde, 2026-11-20: "one crash on a stranger's phone is enough"; the
MetricKit reader waited for a burst until 2026-11-24).

    python3 scripts/test_crash_single.py
"""
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import crashes  # noqa: E402

NOW = datetime.datetime(2026, 11, 24, 12, 0, tzinfo=datetime.timezone.utc)


def sig(hours_ago, fix=None):
    at = (NOW - datetime.timedelta(hours=hours_ago)).isoformat()
    return {"kind": "crash", "build": "41", "version": "1.0.4", "frame": "X", "symbol": "MapTab.body", "count": 1,
            "_phone_times": {"p1": [at]}, "fix": fix}


def run():
    stores = {"41": "READY_FOR_SALE"}
    orig = crashes.is_store
    crashes.is_store = lambda build, st: build in st
    try:
        found = crashes.assess([sig(30)], stores, now=NOW)
        assert [a["level"] for a in found] == ["act"], found
        line = crashes.message(found[0])
        assert "1 crash(es) on 1 phone(s) in 48h" in line, line
        assert crashes.assess([sig(60)], stores, now=NOW) == [], "older than 48h stays quiet"
        answered = {"signature": "X", "what": "looked into"}
        assert crashes.assess([sig(30, answered)], stores, now=NOW) == [], "an answer on file quiets it"
    finally:
        crashes.is_store = orig
    print("ok: one unanswered store crash acts; old or answered ones do not")


if __name__ == "__main__":
    run()
