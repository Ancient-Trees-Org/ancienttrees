#!/usr/bin/env python3
"""One last sign-in link for the people who signed up by email on the
Guardian days and never got in (Hidde, 2026-11-20: "doe beide maar").

Who: accounts made with an email link from 15 to 18 November 2026 that never
confirmed or signed in, picked fresh from Supabase on the day it sends. Left
out: an address whose mail bounced or that the hook called undeliverable
(signin_watch's state and the inbox's bounce notices), and anybody whose name
before the @ already got in on another account (a typo they fixed themselves).

When: from SEND_FROM, a week after the sign-in watcher's last mail to them
(one week's rest across every route), until EXPIRES. One mail per person,
ever; who had it sits in data/signin-last-call.json under people.ref codes.
It goes only while APPROVED is True: the text below is the one Hidde said yes
to, and changing it needs his yes again. It replaces the Yahoo-only apology
drafted on 11-17 (drafts/signin-sorry-yahoo-2026-11-23.md): the Yahoo people
are in this list too, so nobody gets both.

Route: a first mail on its own, so kind FIRST: signed through Resend, Gmail
when Resend is full or down. Each mail carries a fresh magic link (24 hours,
the project's setting since 2026-11-16) back to /account.

Usage:
  python3 scripts/signin_last_call.py           dry run: who would get it, and the mail
  python3 scripts/signin_last_call.py --send    send (only between SEND_FROM and EXPIRES)
"""
import datetime
import json
import os
import sys
import urllib.request
from email.message import EmailMessage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mailer  # noqa: E402
import people  # noqa: E402
import signin_watch  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, "data", "signin-last-call.json")
SIGNED_UP = ("2026-11-15", "2026-11-19")          # created_at from, before
SEND_FROM = datetime.datetime(2026, 11, 27, 8, 0, tzinfo=datetime.timezone.utc)
EXPIRES = datetime.datetime(2026, 11, 30, 0, 0, tzinfo=datetime.timezone.utc)
APPROVED = True    # Hidde's yes to the text below, 2026-11-20: "Yes, send it then"
BATCH = "signin-last-call-2026-11-27"
REDIRECT = "https://ancienttrees.app/account"

SUBJECT = "Your Ancient Trees sign-in link"
BODY = """Sorry, your sign-in link may never have reached you.

You signed up for Ancient Trees in mid-November but never got in. Some mail providers turned our mails away or put them in spam, and that was on our side. This link signs you straight in, for the next 24 hours:

{link}

If you no longer want an account, just ignore this mail. This is the last one we send about it.

Ancient Trees"""


def load_state():
    try:
        with open(STATE, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return {"note": "Who got the one last sign-in link (scripts/signin_last_call.py). Codes, never addresses.",
                "sent": {}}


def chosen(users, watch_state, bounced, key):
    """[(code, user)] still stuck from the Guardian days, minus the ones we
    cannot or need not reach."""
    out = []
    for u in users:
        made = (u.get("created_at") or "")[:10]
        if not (SIGNED_UP[0] <= made < SIGNED_UP[1]) or not signin_watch.never_in(u):
            continue
        addr = (u.get("email") or "").strip()
        if not addr:
            continue
        code = people.ref(u["id"], key)
        if watch_state["retried"].get(code, {}).get("undeliverable") or addr.lower() in bounced:
            continue
        if signin_watch.in_elsewhere(addr, users):
            continue
        out.append((code, u))
    return out


def magic_link(addr, key):
    req = urllib.request.Request(people.BASE + "/auth/v1/admin/generate_link", method="POST",
                                 data=json.dumps({"type": "magiclink", "email": addr,
                                                  "options": {"redirect_to": REDIRECT}}).encode(),
                                 headers={"apikey": key, "Authorization": f"Bearer {key}",
                                          "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        got = json.loads(r.read())
    return got.get("action_link") or (got.get("properties") or {}).get("action_link")


def main():
    send = "--send" in sys.argv
    key = people.service_key()
    if not key:
        sys.exit("signin_last_call: needs SUPABASE_SERVICE_KEY")
    now = datetime.datetime.now(datetime.timezone.utc)
    if send and not (APPROVED and SEND_FROM <= now < EXPIRES):
        print("signin_last_call: not now (" + ("waiting for Hidde's yes" if not APPROVED else
              f"sends {SEND_FROM:%Y-%m-%d %H:%M} to {EXPIRES:%Y-%m-%d} UTC") + ")")
        return
    state = load_state()
    users = signin_watch.users(key)
    todo = [(c, u) for c, u in chosen(users, signin_watch.load_state(), signin_watch.bounced_addresses(days=14), key)
            if c not in state["sent"]]
    if not send:
        print(f"WOULD SEND {len(todo)}: " + ", ".join(
            f"{c} ({'signed' if mailer.wants_resend(u['email'], mailer.EXPECTED) else 'gmail'} address)" for c, u in todo))
        print("\nSubject: " + SUBJECT + "\n\n" + BODY.format(link="<a fresh sign-in link>"))
        return
    creds = {k: os.environ.get(f"OUTREACH_{k}") for k in ("SMTP_HOST", "SMTP_PORT", "SMTP_USER", "SMTP_PASS", "FROM")}
    if not all(creds.values()) or "burgmans.hidde" in creds["FROM"].lower():
        sys.exit("signin_last_call: no Ancient Trees mail credentials")
    try:
        with open(mailer.SENT_LOG, encoding="utf-8") as fh:
            log = json.load(fh)
    except FileNotFoundError:
        sys.exit("signin_last_call: no send log; private_store.py pull first")
    today = now.date().isoformat()
    n = 0
    with mailer.connect(creds, timeout=60, kind=mailer.FIRST) as server:
        for code, u in todo:
            try:
                link = magic_link(u["email"], key)
            except Exception as e:  # noqa: BLE001
                print("NO LINK", code, type(e).__name__)
                continue
            if not link:
                print("NO LINK", code)
                continue
            msg = EmailMessage()
            msg["From"], msg["To"], msg["Subject"] = creds["FROM"], u["email"], SUBJECT
            msg.set_content(BODY.format(link=link))
            try:
                route = server.send_message(msg)
            except mailer.RecentlyMailed:
                print("RESTING", code)
                continue
            except Exception as e:  # noqa: BLE001
                print("FAILED", code, type(e).__name__)
                continue
            state["sent"][code] = now.isoformat(timespec="minutes")
            log.setdefault("sent", []).append({"date": today, "to": u["email"], "outlet": "sign-in last call",
                                               "subject": SUBJECT, "batch": BATCH, "route": route})
            n += 1
            print("SENT", code, route)
    with open(mailer.SENT_LOG, "w", encoding="utf-8") as fh:
        json.dump(log, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    with open(STATE, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(f"signin_last_call: {n} sent")


if __name__ == "__main__":
    main()
