#!/usr/bin/env python3
"""An iPhone report on a build on sale rings until data/crash-fixes.json
answers it (Hidde, 2026-11-20: "one crash on a stranger's phone is enough";
2026-11-24: "is this a solid system without leaks?").

    python3 scripts/test_crash_single.py
"""
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import crashes  # noqa: E402

NOW = datetime.datetime(2026, 11, 24, 12, 0, tzinfo=datetime.timezone.utc)


def at(hours_ago):
    return (NOW - datetime.timedelta(hours=hours_ago)).isoformat()


def sig(times, fix=None, kind="crash", secs=0.0):
    times = [at(h) for h in times]
    return {"kind": kind, "build": "41", "version": "1.0.4", "frame": "X", "symbol": "MapTab.body",
            "count": len(times), "phones": 1, "_phone_times": {"p1": times},
            "_secs": [(t, secs) for t in times], "fix": fix}


def levels(s):
    return [a["level"] for a in crashes.assess([s], {"41": "READY_FOR_SALE"}, now=NOW)]


def run():
    orig = crashes.is_store
    crashes.is_store = lambda build, st: build in st
    try:
        found = crashes.assess([sig([30])], {"41": 1}, now=NOW)
        assert [a["level"] for a in found] == ["act"], found
        line = crashes.message(found[0])
        assert "1 crash(es) on 1 phone(s), not answered yet" in line, line

        # A crash nobody answered still rings a week later.
        assert levels(sig([24 * 7])) == ["act"], "an unanswered crash went quiet"

        # A fix build answers it; so does answered_at, but only for older reports.
        assert levels(sig([30], {"signature": "X", "first_fixed_build": "42"})) == []
        looked = {"signature": "X", "answered_at": at(10), "what": "no cause found"}
        assert levels(sig([30], looked)) == [], "a looked-into crash kept ringing"
        assert levels(sig([30, 2], looked)) == ["act"], "a crash after the answer stayed quiet"

        # Hangs: one short hang is the system; a repeat or a long one rings.
        assert levels(sig([30], kind="hang", secs=2)) == [], "one 2 s hang rang"
        assert levels(sig([30, 20], kind="hang", secs=2)) == ["act"], "a repeated hang stayed quiet"
        assert levels(sig([30], kind="hang", secs=8)) == ["act"], "an 8 s hang stayed quiet"
        assert "hang(s)" in crashes.message(
            crashes.assess([sig([30], kind="hang", secs=8)], {"41": 1}, now=NOW)[0])

        assert crashes._secs("2 sec") == 2.0 and crashes._secs("750 ms") == 0.75 and crashes._secs(None) == 0.0
    finally:
        crashes.is_store = orig
    print("ok: unanswered reports ring until answered; hangs ring when repeated or long")


if __name__ == "__main__":
    run()
