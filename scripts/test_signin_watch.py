"""When signin_watch.py sends a sign-in mail again: pure cases, no network."""
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import signin_watch as w  # noqa: E402

AT = "@"
GMAIL = "a" + AT + "gmail.com"
YAHOO = "b" + AT + "yahoo.com"
UTC = dt.timezone.utc
NOW = dt.datetime(2026, 11, 19, 14, 0, tzinfo=UTC)


def u(email, made_hours_ago, provider="email", confirmed=False):
    return {"email": email, "app_metadata": {"provider": provider},
            "created_at": (NOW - dt.timedelta(hours=made_hours_ago)).isoformat(),
            "email_confirmed_at": "x" if confirmed else None, "last_sign_in_at": None}


cases = [
    ("stuck an hour and more: first retry", w.due(u(GMAIL, 2), [], NOW), True),
    ("too fresh: waits", w.due(u(GMAIL, 0.5), [], NOW), False),
    ("got in: nothing", w.due(u(GMAIL, 2, confirmed=True), [], NOW), False),
    ("apple or google sign-in: nothing", w.due(u(GMAIL, 2, provider="apple"), [], NOW), False),
    ("older than three days: left alone", w.due(u(GMAIL, 80), [], NOW), False),
    ("gmail route retried once: never again", w.due(u(GMAIL, 30), ["2026-11-18T10:00+00:00"], NOW), False),
    ("signed route, retry today: waits for midnight",
     w.due(u(YAHOO, 5), ["2026-11-19T10:00+00:00"], NOW), False),
    ("signed route, retried yesterday: second try after midnight",
     w.due(u(YAHOO, 30), ["2026-11-18T10:00+00:00"], NOW), True),
    ("signed route, two tries: done", w.due(u(YAHOO, 30), ["a", "b"], NOW), False),
]
fails = 0
for name, got, want in cases:
    ok = got == want
    fails += not ok
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else f": got {got}"))
print("FAILS:", fails)
sys.exit(1 if fails else 0)
