#!/usr/bin/env python3
"""Is mail still reaching us? The alarm for a mailbox that went quiet.

Hidde, 2026-11-24 ("dit lijkt me slim"), the day after Google disabled his
Gmail: mail to @ancienttrees.app bounced for hours and nothing said so. Since
then every address lands in one Workspace mailbox; if Google blocks that one
too, readers, press and ambassadors bounce in silence. This file is the
silence's end.

It adds no login of its own. reader_mail_replies.py already opens the
mailbox; it calls record() with that connection (or record_failure() when
the login itself fails), and health.py calls assess(). Red when:
- the login failed (wrong password, account blocked or disabled);
- nothing arrived in INBOX for QUIET_DAYS days (mail is not reaching us);
- the check itself has not run for STALE_DAYS days (the step stopped).

data/inbox-health.json holds days, never times, so it changes at most a few
times a day and the reader judge commits it only then. No addresses, no
subjects: only dates and the error's first words.

    python3 scripts/inbox_health.py      # print the verdict
"""
import datetime
import email.utils
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "data", "inbox-health.json")
QUIET_DAYS = 2   # a day without mail happens; two in a row has not since the app launched
STALE_DAYS = 2


def _today():
    return datetime.datetime.now(datetime.timezone.utc).date()


def load(path=PATH):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def _write(state, path=PATH):
    """Write only when something changed, so the file is not a commit a run."""
    if load(path) == state:
        return False
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2, sort_keys=True)
        fh.write("\n")
    return True


def newest_inbox_day(imap, today=None):
    """The day the newest message in INBOX arrived (server time), or None
    when nothing came in the last week. Read-only."""
    today = today or _today()
    if imap.select("INBOX", readonly=True)[0] != "OK":
        return None
    since = (today - datetime.timedelta(days=7)).strftime("%d-%b-%Y")
    _, ids = imap.search(None, "SINCE", since)
    ids = (ids[0] or b"").split()
    if not ids:
        return None
    _, data = imap.fetch(ids[-1], "(INTERNALDATE)")
    raw = data[0] if data and isinstance(data[0], bytes) else (data[0][0] if data else b"")
    m = re.search(rb'INTERNALDATE "([^"]+)"', raw or b"")
    if not m:
        return None
    parsed = email.utils.parsedate_to_datetime(
        m.group(1).decode().replace("-", " ", 2))
    return parsed.astimezone(datetime.timezone.utc).date()


def record(imap, path=PATH, today=None):
    today = today or _today()
    newest = newest_inbox_day(imap, today)
    return _write({"status": "ok", "checked_day": today.isoformat(),
                   "newest_mail_day": newest.isoformat() if newest else None}, path)


def record_failure(err, path=PATH, today=None):
    today = today or _today()
    old = load(path)
    since = old.get("failing_since") if old.get("status") == "failing" else None
    return _write({"status": "failing", "checked_day": today.isoformat(),
                   "failing_since": since or today.isoformat(),
                   "newest_mail_day": old.get("newest_mail_day"),
                   "error": str(err)[:120]}, path)


def assess(state=None, today=None):
    """(ok, sentence). ok is None when there is no record yet."""
    state = load() if state is None else state
    today = today or _today()
    if not state:
        return None, "no inbox check recorded yet"

    def age(key):
        d = state.get(key)
        return (today - datetime.date.fromisoformat(d)).days if d else None

    if state.get("status") == "failing":
        return False, ("The mailbox will not open since %s (%s). Mail to "
                       "@ancienttrees.app may be bouncing: check the Workspace "
                       "account first, then the app password in OUTREACH_SMTP_PASS."
                       % (state.get("failing_since"), state.get("error", "")))
    checked = age("checked_day")
    if checked is None or checked > STALE_DAYS:
        return False, ("The inbox check has not run for %s days (reader-judge.yml, "
                       "step \"Readers' mail replies become rows\")." % checked)
    quiet = age("newest_mail_day")
    if quiet is None or quiet >= QUIET_DAYS:
        return False, ("No mail has arrived in the inbox for %s days. Check the MX "
                       "record of ancienttrees.app and the Workspace account: "
                       "readers' and press mail may be bouncing."
                       % ("7+" if quiet is None else quiet))
    return True, "newest mail %s, checked %s" % (state["newest_mail_day"], state["checked_day"])


if __name__ == "__main__":
    ok, line = assess()
    print(("ok   " if ok else "RED  " if ok is False else "?    ") + line)
    sys.exit(1 if ok is False else 0)
