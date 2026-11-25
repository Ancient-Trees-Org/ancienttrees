#!/usr/bin/env python3
"""Tests for web_errors.py's grouping: one fault in three browsers' words is
one type, and a known type that jumps turns red (2026-11-25, the "el is null"
card error that sat orange as two types).

    python3 scripts/test_web_errors.py
"""
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import web_errors  # noqa: E402

NOW = datetime.datetime(2026, 11, 25, 9, 0, tzinfo=datetime.timezone.utc)


def row(message, path, hours_ago, source="inline"):
    when = (NOW - datetime.timedelta(hours=hours_ago)).isoformat()
    return {"message": message, "source": source, "path": path, "created_at": when}


def test_browsers_word_one_fault_alike():
    chrome = web_errors.normalise("TypeError: Cannot read properties of null (reading 'getBoundingClientRect')")
    safari = web_errors.normalise("TypeError: null is not an object (evaluating 'el.getBoundingClientRect')")
    firefox = web_errors.normalise('TypeError: can\'t access property "getBoundingClientRect", el is null')
    assert chrome == safari == firefox == "TypeError: null has no property 'getBoundingClientRect'", (chrome, safari, firefox)
    assert web_errors.normalise("Uncaught TypeError: t.getExtension is not a function") == \
        "TypeError: t.getExtension is not a function"
    assert web_errors.normalise("TypeError: undefined is not an object (evaluating 'n.standardSelectors')") == \
        "TypeError: undefined has no property 'standardSelectors'"


def test_the_card_error_of_2026_11_25_is_red():
    # The real rows: one Chrome report five days ago, then three in a day.
    rows = [
        row("TypeError: null is not an object (evaluating 'el.getBoundingClientRect')", "/venice", 1),
        row("TypeError: Cannot read properties of null (reading 'getBoundingClientRect')", "/milan", 10),
        row("TypeError: Cannot read properties of null (reading 'getBoundingClientRect')", "/pisa", 20),
        row("TypeError: Cannot read properties of null (reading 'getBoundingClientRect')", "/vancouver", 24 * 5),
    ]
    types = web_errors.group(rows, now=NOW)
    assert len(types) == 1, types
    t = types[0]
    assert t["day"] == 3 and t["before"] == 1 and t["spreading"], t


def test_steady_noise_stays_quiet():
    # ResizeObserver fires every day; four today against many before is not red.
    rows = [row("ResizeObserver loop completed with undelivered notifications.", "/p%d" % i, 2) for i in range(4)]
    rows += [row("ResizeObserver loop completed with undelivered notifications.", "/q%d" % i, 30 + i) for i in range(50)]
    t = web_errors.group(rows, now=NOW)[0]
    assert not t["spreading"], t


def test_one_report_stays_orange():
    t = web_errors.group([row("Error: Na", "/", 3)], now=NOW)[0]
    assert t["new"] and not t["spreading"], t


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
    print("%d tests passed" % len(tests))
