"""The brake on batch mail (Hidde, 2026-11-24, "ok bouw rem").

Google blocked his Gmail on 2026-11-23 after a week of machine mail, and since
2026-11-24 every script sends through Resend only. Resend suspends an account
whose mail bounces (about 4%) or is marked as spam (about 0.1%) too often, and
then the sign-in mail stops with it. So a batch (scripts/outreach_send.py)
sends first mails in steps of STEP, waits WAIT seconds after each step, reads
what Resend saw happen to them, and stops the rest of the batch when:

  - this run: BOUNCE_STOP bounces, or any spam complaint;
  - the last seven days, every mail on the account: a bounce share of
    WEEK_BOUNCE_STOP or a complaint share of WEEK_COMPLAINT_STOP.

It reads with RESEND_READ_KEY, a Resend API key that may read (the sending key
RESEND_SMTP_PASS is "restricted to only send emails"). Without one the brake
is blind and a run sends at most BLIND_CAP first mails. A reply in a thread is
never braked: it is mail somebody expects.

    python3 scripts/mail_brake.py        the seven-day numbers and the verdict

Addresses are never printed; only counts.
"""
import datetime
import json
import os
import sys
import time
import urllib.error
import urllib.request

STEP = 25
WAIT = 90
BLIND_CAP = 25
BOUNCE_STOP = 3
WEEK_BOUNCE_STOP = 0.03
WEEK_COMPLAINT_STOP = 0.001
WEEK_MIN = 50  # under this many mails a share says nothing yet

API = "https://api.resend.com/emails"


def read_key():
    return (os.environ.get("RESEND_READ_KEY") or "").strip() or None


def _when(s):
    """Resend's created_at ("2026-11-24 10:00:00.123+00") as an aware datetime."""
    s = (s or "").strip().replace(" ", "T", 1)
    if s.endswith("+00"):
        s += ":00"
    try:
        d = datetime.datetime.fromisoformat(s)
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=datetime.timezone.utc)


def _get(key, url):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {key}",
                                               "User-Agent": "ancienttrees-mail-brake"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def fetch(key, since, get=_get):
    """Every mail on the account created since `since`, newest first:
    [{"to": [...], "event": "...", "at": datetime}]."""
    rows, after = [], None
    for _ in range(200):  # 20,000 mails, far past a week of ours
        url = f"{API}?limit=100" + (f"&after={after}" if after else "")
        page = get(key, url)
        data = page.get("data") or []
        for e in data:
            at = _when(e.get("created_at"))
            if at and at < since:
                return rows
            to = e.get("to") or []
            rows.append({"to": [t.lower() for t in (to if isinstance(to, list) else [to])],
                         "event": e.get("last_event") or "", "at": at})
        if not data or not page.get("has_more"):
            return rows
        after = data[-1].get("id")
    return rows


def judge(rows, run_to=(), run_since=None):
    """The reason to stop, or None. `run_to` are the addresses this run sent
    to since `run_since`."""
    run_to = {a.lower() for a in run_to}
    if run_to:
        mine = [r for r in rows if set(r["to"]) & run_to
                and (run_since is None or (r["at"] and r["at"] >= run_since))]
        complained = sum(r["event"] == "complained" for r in mine)
        bounced = sum(r["event"] == "bounced" for r in mine)
        if complained:
            return f"{complained} spam complaint(s) on this batch's mail"
        if bounced >= BOUNCE_STOP:
            return f"{bounced} of {len(mine)} of this batch's mails bounced"
    n = len(rows)
    if n >= WEEK_MIN:
        bounced = sum(r["event"] == "bounced" for r in rows)
        complained = sum(r["event"] == "complained" for r in rows)
        if bounced / n >= WEEK_BOUNCE_STOP:
            return f"{bounced} of {n} mails bounced in seven days ({bounced / n:.1%})"
        if complained / n >= WEEK_COMPLAINT_STOP:
            return f"{complained} of {n} mails marked as spam in seven days ({complained / n:.2%})"
    return None


class Brake:
    """One per batch run. Call check() before each first mail and sent(to)
    after it; check() returns the reason to hold the rest, or None."""

    def __init__(self, key=None, get=_get, sleep=time.sleep, now=None):
        self.key = key if key is not None else read_key()
        self._get, self._sleep = get, sleep
        self._now = now or (lambda: datetime.datetime.now(datetime.timezone.utc))
        self.start = self._now()
        self.sent_to = []
        self._checked_at = None
        self.stopped = None

    def _look(self):
        since = self._now() - datetime.timedelta(days=7)
        try:
            rows = fetch(self.key, since, self._get)
        except (urllib.error.URLError, OSError, ValueError) as e:
            # Cannot see: hold rather than send blind past the first step.
            return f"could not read Resend's delivery events ({type(e).__name__})"
        return judge(rows, self.sent_to, self.start)

    def check(self):
        if self.stopped:
            return self.stopped
        n = len(self.sent_to)
        if not self.key:
            if n >= BLIND_CAP:
                self.stopped = (f"the brake is blind (no RESEND_READ_KEY), so a run sends "
                                f"at most {BLIND_CAP} first mails")
            return self.stopped
        if self._checked_at is None or (n and n % STEP == 0 and self._checked_at != n):
            if n:
                self._sleep(WAIT)  # bounces and complaints take a moment to come back
            self._checked_at = n
            self.stopped = self._look()
        return self.stopped

    def sent(self, to):
        self.sent_to.append((to or "").lower())

    def last_look(self):
        """After the batch: one more look at what this run sent."""
        if not self.key or not self.sent_to or self.stopped:
            return self.stopped
        self._sleep(WAIT)
        return self._look()


def main():
    key = read_key()
    if not key:
        print("mail brake: blind, no RESEND_READ_KEY (a batch run sends at most "
              f"{BLIND_CAP} first mails)")
        return 0
    rows = fetch(key, datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=7))
    count = {}
    for r in rows:
        count[r["event"]] = count.get(r["event"], 0) + 1
    print(f"mail brake: {len(rows)} mails in seven days: "
          + ", ".join(f"{k or '?'} {v}" for k, v in sorted(count.items())))
    reason = judge(rows)
    print("verdict: " + (f"STOP, {reason}" if reason else "go"))
    return 1 if reason else 0


if __name__ == "__main__":
    sys.exit(main())
