"""Tests for scripts/mail_brake.py with a fake Resend: no network, no waiting.
python3 scripts/test_mail_brake.py"""
import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mail_brake as mb

UTC = datetime.timezone.utc
NOW = datetime.datetime(2026, 11, 24, 12, 0, tzinfo=UTC)
fails = []


def expect(name, got, want):
    ok = (got is None) == (want is None) if want in (None, "stop") else got == want
    if want == "stop":
        ok = got is not None
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f": got {got!r}"))
    if not ok:
        fails.append(name)


def row(to, event, minutes_ago=5):
    return {"id": f"{to}-{minutes_ago}", "to": [to], "last_event": event,
            "created_at": (NOW - datetime.timedelta(minutes=minutes_ago)).strftime("%Y-%m-%d %H:%M:%S.000+00")}


class FakeResend:
    """Serves `rows` newest first, 100 a page, like GET /emails."""

    def __init__(self, rows):
        self.rows, self.calls = rows, 0

    def __call__(self, key, url):
        self.calls += 1
        after = url.split("after=")[1] if "after=" in url else None
        start = 0
        if after:
            start = next(i for i, r in enumerate(self.rows) if r["id"] == after) + 1
        page = self.rows[start:start + 100]
        return {"data": page, "has_more": start + 100 < len(self.rows)}


def brake(rows, key="k"):
    waits = []
    b = mb.Brake(key=key, get=FakeResend(rows), sleep=waits.append, now=lambda: NOW)
    return b, waits


# A quiet week: go.
week = [row(f"r{i}@x.org", "delivered", 60 * 24 + i) for i in range(300)]
b, _ = brake(week)
expect("a quiet week lets the batch start", b.check(), None)

# A bad week across the account stops before the first mail.
bad = [row(f"r{i}@x.org", "bounced" if i < 12 else "delivered", 60 + i) for i in range(300)]
b, _ = brake(bad)
expect("4% bounces in seven days stops the batch before it starts", b.check(), "stop")

# One spam complaint in 300 (0.33%) stops it too.
spam = [row(f"r{i}@x.org", "complained" if i == 7 else "delivered", 60 + i) for i in range(300)]
b, _ = brake(spam)
expect("a complaint share over 0.1% stops the batch", b.check(), "stop")

# Few mails in the week: a share says nothing yet.
few = [row("a@x.org", "bounced", 60), row("b@x.org", "delivered", 61)]
b, _ = brake(few)
expect("under fifty mails a week, one bounce is no share", b.check(), None)

# During the run: three of this batch's mails bounce -> the step check stops it.
rows = list(week)
b, waits = brake(rows)
expect("start", b.check(), None)
for i in range(mb.STEP):
    b.sent(f"new{i}@y.org")
    if i < mb.STEP - 1:
        expect(f"no check between steps ({i})", b.check(), None) if i == 0 else b.check()
rows[:0] = [row(f"new{i}@y.org", "bounced" if i < 3 else "delivered", -1) for i in range(mb.STEP)]
b._get = FakeResend(rows)
expect("three bounces in this batch stop it at the step", b.check(), "stop")
expect("the step waited for events first", waits, [mb.WAIT])
expect("once stopped it stays stopped", b.check(), "stop")

# Any complaint on this batch's mail stops it.
rows = list(week)
b, _ = brake(rows)
b.check()
for i in range(mb.STEP):
    b.sent(f"c{i}@y.org")
rows[:0] = [row("c3@y.org", "complained", -1)]
b._get = FakeResend(rows)
expect("one complaint on this batch stops it", b.check(), "stop")

# An old bounce of the same address before this run does not count for the run.
rows = [row("old@y.org", "bounced", 60 * 3)] + week
b, _ = brake(rows)
b.check()
b.sent("old@y.org")
for i in range(mb.STEP - 1):
    b.sent(f"z{i}@y.org")
expect("a bounce from before this run is not this run's", b.check(), None)

# Blind: no read key -> at most BLIND_CAP first mails, never a network call.
fake = FakeResend(week)
b = mb.Brake(key="", get=fake, sleep=lambda s: None, now=lambda: NOW)
for i in range(mb.BLIND_CAP):
    expect("blind lets the first mails go", b.check(), None) if i == 0 else b.check()
    b.sent(f"b{i}@y.org")
expect("blind holds after the cap", b.check(), "stop")
expect("blind never calls Resend", fake.calls, 0)

# Resend unreachable: hold, never send blind past the first look.
def down(key, url):
    raise OSError("down")
b = mb.Brake(key="k", get=down, sleep=lambda s: None, now=lambda: NOW)
expect("Resend unreadable holds the batch", b.check(), "stop")

# Pagination stops at the week's edge.
long = [row(f"p{i}@x.org", "delivered", i) for i in range(250)] + \
       [row(f"o{i}@x.org", "bounced", 60 * 24 * 8 + i) for i in range(100)]
got = mb.fetch("k", NOW - datetime.timedelta(days=7), FakeResend(long))
expect("fetch reads across pages and stops at seven days", len(got), 250)

print()
print("FAILED: " + ", ".join(fails) if fails else "all passed")
sys.exit(1 if fails else 0)
