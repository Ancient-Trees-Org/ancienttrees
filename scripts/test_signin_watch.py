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


def ago(h):
    return NOW - dt.timedelta(hours=h)


def user(provider="email", confirmed=False, signed_in=False):
    return {"app_metadata": {"provider": provider},
            "email_confirmed_at": "x" if confirmed else None,
            "last_sign_in_at": "x" if signed_in else None}


def report(action, rcpt):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.message import Message
    m = MIMEMultipart("report")
    m.attach(MIMEText("Delivery report"))
    status = Message()
    status.set_type("message/delivery-status")
    per = Message()
    per["Final-Recipient"] = "rfc822; " + rcpt
    per["Action"] = action
    status.set_payload([Message(), per])
    m.attach(status)
    return m


TYPO = "pm" + AT + "tahoo.com"
FIXED = {"email": "pm" + AT + "yahoo.com", "email_confirmed_at": "x"}
STUCK = {"email": TYPO}
OTHER_IN = {"email": "pmx" + AT + "yahoo.com", "last_sign_in_at": "x"}

cases = [
    ("typo fixed on a second account: skipped", w.in_elsewhere(TYPO, [STUCK, FIXED]), True),
    ("only the stuck account itself: not skipped", w.in_elsewhere(TYPO, [STUCK]), False),
    ("a different name that is in: not skipped", w.in_elsewhere(TYPO, [STUCK, OTHER_IN]), False),
    ("second account also never in: not skipped",
     w.in_elsewhere(TYPO, [STUCK, {"email": "pm" + AT + "yahoo.com"}]), False),
    ("a failed bounce names the address", w.failed_recipients(report("failed", "Ista" + AT + "gmail.com")),
     {"ista" + AT + "gmail.com"}),
    ("a delay notice is not a bounce", w.failed_recipients(report("delayed", TYPO)), set()),
    ("no login: no inbox read, empty set",
     (os.environ.pop("OUTREACH_SMTP_USER", None), w.bounced_addresses())[1], set()),
    ("stuck an hour and more: first retry", w.due(ago(2), GMAIL, [], NOW), True),
    ("too fresh: waits", w.due(ago(0.5), GMAIL, [], NOW), False),
    ("older than three days: left alone", w.due(ago(80), GMAIL, [], NOW), False),
    ("gmail route retried once: never again", w.due(ago(30), GMAIL, ["2026-11-18T10:00+00:00"], NOW), False),
    ("signed route, retry today: waits for midnight",
     w.due(ago(5), YAHOO, ["2026-11-19T10:00+00:00"], NOW), False),
    ("signed route, retried yesterday: second try after midnight",
     w.due(ago(30), YAHOO, ["2026-11-18T10:00+00:00"], NOW), True),
    ("signed route, two tries: done",
     w.due(ago(30), YAHOO, ["2026-11-18T10:00+00:00", "2026-11-19T00:10+00:00"], NOW), False),
    ("the retry's own new link does not start a new round",
     w.due(ago(2), GMAIL, ["2026-11-19T11:59+00:00"], NOW), False),
    ("stuck again a week later: tries from last time do not count",
     w.due(ago(2), GMAIL, ["2026-11-10T10:00+00:00"], NOW), True),
    ("never in: email sign-up that never confirmed", w.never_in(user()), True),
    ("never in: confirmed is in", w.never_in(user(confirmed=True)), False),
    ("never in: apple sign-in is not ours to chase", w.never_in(user(provider="apple")), False),
]
fails = 0
for name, got, want in cases:
    ok = got == want
    fails += not ok
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else f": got {got}"))
print("FAILS:", fails)
sys.exit(1 if fails else 0)
