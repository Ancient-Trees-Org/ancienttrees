#!/usr/bin/env python3
"""Somebody signed up with their email address and never got in: send the
sign-in mail again.

Why (Hidde, 2026-11-19, "zien we als iemand het probeert en het lukt niet?"):
that morning a batch filled Resend's 100 a day. Yahoo, Apple-relay and BT
addresses accept only mail signed for our domain, which only Resend sends, so
until midnight UTC their sign-in mail had nowhere to go, and nothing told us.
Gmail-sent mail can go missing too. Now every knock looks for accounts made
with an email link that are more than an hour old and never confirmed or
signed in, and asks Supabase to send their sign-in mail again (the same mail,
through the same hook, so it takes the route the rule gives it):

  - an address that needs a signed mail: once after an hour, and once more
    after the next midnight UTC, when Resend's day starts over;
  - any other address: once, after an hour.

Never more, so a person who simply changed their mind hears from us at most
twice. Accounts older than three days are left alone. What was retried sits
in data/signin-watch.json under people.ref codes, never an address.

The other half of the gap is closed in mailer.py (RESEND_FOR_STRANGERS): first
mails to strangers may use 60 of Resend's 100, the rest is kept for this mail.
Not covered: somebody who already had an account and asked for a new link;
Supabase keeps that in its auth audit log, which the API does not serve.

Usage:
  python3 scripts/signin_watch.py           dry run: who would get a new mail
  python3 scripts/signin_watch.py --send    send them, record it
  python3 scripts/signin_watch.py --status  counts for the digest, one line
"""
import datetime
import json
import os
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mailer  # noqa: E402
import people  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, "data", "signin-watch.json")
WAIT = datetime.timedelta(hours=1)
GIVE_UP = datetime.timedelta(days=3)


def _ts(s):
    """Supabase's timestamps, which Python 3.9 cannot read whole (5-digit fractions)."""
    if not s:
        return None
    s = s.replace("Z", "+00:00")
    head, _, zone = s.partition("+")
    t = datetime.datetime.fromisoformat(head.split(".")[0])
    return t.replace(tzinfo=datetime.timezone.utc) if (zone in ("", "00:00")) else \
        datetime.datetime.fromisoformat(head.split(".")[0] + "+" + zone)


def _call(path, key, body=None):
    req = urllib.request.Request(people.BASE + path, method="POST" if body is not None else "GET",
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"apikey": key, "Authorization": f"Bearer {key}",
                                          "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read() or b"{}")


def users(key):
    out, page = [], 1
    while True:
        got = _call(f"/auth/v1/admin/users?page={page}&per_page=1000", key).get("users", [])
        if not got:
            return out
        out += got
        page += 1


def load_state():
    try:
        with open(STATE, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return {"note": "Accounts whose sign-in mail was sent again (scripts/signin_watch.py). Codes, never addresses.",
                "retried": {}}


def due(user, tries, now):
    """Whether this account gets its sign-in mail again now (pure, tested)."""
    if (user.get("app_metadata") or {}).get("provider") != "email":
        return False
    if user.get("email_confirmed_at") or user.get("last_sign_in_at"):
        return False
    made = _ts(user.get("created_at"))
    if not made or now - made < WAIT or now - made > GIVE_UP:
        return False
    signed = mailer.wants_resend(user.get("email") or "", mailer.EXPECTED)
    if not tries:
        return True
    if signed and len(tries) == 1:
        midnight = datetime.datetime.combine(_ts(tries[0]).date() + datetime.timedelta(days=1),
                                             datetime.time(0, 5), tzinfo=datetime.timezone.utc)
        return now >= midnight
    return False


def status_line(now=None):
    """One line for the digest, from the state file only (no network)."""
    state = load_state()
    now = now or datetime.datetime.now(datetime.timezone.utc)
    week = (now - datetime.timedelta(days=7)).isoformat(timespec="minutes")
    rows = [v for v in state["retried"].values() if any(t >= week for t in v.get("tries", []))]
    if not rows:
        return None
    got_in = sum(1 for v in rows if v.get("got_in"))
    return (f"**Sign-in mail sent again** (stuck an hour or more, `scripts/signin_watch.py`): "
            f"{len(rows)} people in 7 days, {got_in} of them got in afterwards.")


def main():
    send = "--send" in sys.argv
    key = people.service_key()
    if not key:
        sys.exit("signin_watch: needs SUPABASE_SERVICE_KEY")
    state = load_state()
    now = datetime.datetime.now(datetime.timezone.utc)
    if "--status" in sys.argv:
        print(status_line())
        return
    all_users = users(key)
    for u in all_users:  # who got in after a retry
        code = people.ref(u["id"], key)
        row = state["retried"].get(code)
        if row and not row.get("got_in") and (u.get("email_confirmed_at") or u.get("last_sign_in_at")):
            row["got_in"] = now.isoformat(timespec="minutes")
    todo = []
    for u in all_users:
        code = people.ref(u["id"], key)
        if state["retried"].get(code, {}).get("undeliverable"):
            continue
        if due(u, state["retried"].get(code, {}).get("tries", []), now):
            todo.append((code, u))
    for code, u in todo:
        signed = mailer.wants_resend(u.get("email") or "", mailer.EXPECTED)
        label = f"{code} ({'signed route' if signed else 'gmail route'}, made {u['created_at'][:16]})"
        if not send:
            print("WOULD SEND", label)
            continue
        try:
            _call("/auth/v1/otp", key, {"email": u["email"], "create_user": False})
            print("SENT AGAIN", label)
        except urllib.error.HTTPError as e:
            # Never print the body: the hook's refusal names the address, and
            # Actions logs of this repository are public.
            body = e.read().decode("utf-8", "replace")
            if "undeliverable" in body:
                # The address cannot receive mail (a typo in the domain, mostly);
                # the sign-in screen already told them. Recorded, never retried.
                print("UNDELIVERABLE", label)
                state["retried"].setdefault(code, {"tries": []}).update(
                    {"undeliverable": now.isoformat(timespec="minutes")})
                continue
            print("FAILED", label, e.code)
            continue
        state["retried"].setdefault(code, {"tries": []})["tries"].append(now.isoformat(timespec="minutes"))
    if send:
        with open(STATE, "w", encoding="utf-8") as fh:
            json.dump(state, fh, indent=1, ensure_ascii=False)
            fh.write("\n")
    print(f"signin_watch: {len(todo)} {'sent again' if send else 'due'}")


if __name__ == "__main__":
    main()
