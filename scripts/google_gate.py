#!/usr/bin/env python3
"""One door to Hidde's Google account for every script, with a ceiling.

Hidde, 2026-11-24: "kunnen we ook iets inbouwen dat we niet ergens anders
enthousiast dingen met google doen die ons weer gebanned kan krijgen?"
Google disabled his Gmail on 2026-11-23 after weeks of machine traffic on it:
250 to 400 mails a day, ~125 mailbox logins a day from changing GitHub
servers in the US, and one more login for every mail filed in Sent. Each
script had added its own piece and nobody saw the sum.

So, three guards:
1. Every login to the Google mailbox goes through mailbox() here. It reuses
   one connection for the whole run, allows at most MAX_LOGINS_PER_RUN, and
   never tries again after Google refused a login (a refused login retried
   in a loop is the surest way to look like an attack).
2. data/google-touch.json lists every script that touches the Google account
   (mailbox logins and API calls), where it runs and how often a day. qa's
   check_google_is_touched_through_one_door() refuses a push where a script
   logs in to the mailbox outside this file, where a script that touches
   Google is not in the ledger, or where the ledger's logins a day add up to
   more than its budget.
3. Mail never goes through Google at all (mailer.GOOGLE_ROUTE = False,
   check_no_script_mails_through_google()).

Raising the budget, or a new kind of Google traffic, needs Hidde.

    python3 scripts/google_gate.py     # the ledger and its sum
"""
import atexit
import imaplib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "data", "google-touch.json")
MAX_LOGINS_PER_RUN = 2


class GoogleRefused(imaplib.IMAP4.error):
    """The gate said no: no login on this machine, refused earlier in this
    run, or the run's ceiling reached. An IMAP4.error, so every caller that
    already handles a failed login handles this too."""


_state = {"box": None, "logins": 0, "refused": None, "hook": False}


def _close():
    box = _state.get("box")
    _state["box"] = None
    if box is not None:
        try:
            box.logout()
        except Exception:  # noqa: BLE001
            pass


def reset():
    """For tests: forget this process's connection and counts."""
    _close()
    _state.update(logins=0, refused=None)


def mailbox(timeout=30):
    """The logged-in Google mailbox, one connection for the whole run.
    Callers do not log out: the gate closes it when the script ends."""
    if _state["refused"]:
        raise GoogleRefused("Google refused the login earlier in this run (%s); not trying again"
                            % _state["refused"])
    box = _state["box"]
    if box is not None and getattr(box, "state", "") != "LOGOUT":
        return box
    if _state["logins"] >= MAX_LOGINS_PER_RUN:
        raise GoogleRefused("this run already logged in to Google %d times (google_gate.py)"
                            % _state["logins"])
    user = os.environ.get("OUTREACH_SMTP_USER")
    pw = os.environ.get("OUTREACH_SMTP_PASS")
    if not (user and pw):
        raise GoogleRefused("no mailbox login on this machine (OUTREACH_SMTP_USER/PASS)")
    _state["logins"] += 1
    box = imaplib.IMAP4_SSL(os.environ.get("OUTREACH_IMAP_HOST", "imap.gmail.com"), timeout=timeout)
    try:
        box.login(user, pw)
    except imaplib.IMAP4.error as e:
        _state["refused"] = str(e)[:80]
        raise
    _state["box"] = box
    if not _state["hook"]:
        atexit.register(_close)
        _state["hook"] = True
    return box


def ledger():
    with open(LEDGER, encoding="utf-8") as fh:
        return json.load(fh)


def logins_a_day(led=None):
    led = led or ledger()
    return sum(int(r.get("logins_per_day", 0)) for r in led.get("touches", []))


if __name__ == "__main__":
    led = ledger()
    for r in led["touches"]:
        print("%-24s %-8s %3s/day  %s" % (r["script"], r["kind"], r.get("logins_per_day", 0), r["where"]))
    total = logins_a_day(led)
    print("\nmailbox logins a day: %d of a budget of %d" % (total, led["mailbox_logins_per_day_budget"]))
    sys.exit(1 if total > led["mailbox_logins_per_day_budget"] else 0)
