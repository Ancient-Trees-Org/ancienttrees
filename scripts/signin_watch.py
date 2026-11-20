#!/usr/bin/env python3
"""Somebody asked for a sign-in mail and never got in: send it again.

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
twice. Never at all to an address whose earlier mail bounced (read from the
inbox), or when the same name before the @ already got in on another account
(a typo they fixed themselves: outlook.co, tahoo.com; Hidde, 2026-11-20). An ask older than three days is left alone (`--days N` reaches further
back, for a one-off catch-up a session runs on Hidde's word). What was retried sits
in data/signin-watch.json under people.ref codes, never an address.

The other half of the gap is closed in mailer.py (RESEND_FOR_STRANGERS): first
mails to strangers may use 60 of Resend's 100, the rest is kept for this mail.
Existing accounts too (Hidde, same day: "kunnen we dat nagaan?"): the audit log
is empty on this project, but a link or code stays in auth.one_time_tokens until
it is used, so supabase/stuck-signin-links.sql lists everybody holding one an
hour old without signing in since. The first count, 15 to 19 November: 15
existing accounts, 12 of them on Yahoo, Apple-relay or BT addresses, nearly all
on 16 November, the day after the Guardian piece. Same rules as above, counted
from when they asked.

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
if "--days" in sys.argv:  # a one-off catch-up further back, run by a session on Hidde's word
    GIVE_UP = datetime.timedelta(days=int(sys.argv[sys.argv.index("--days") + 1]))
# THE GUARDIAN-DAY CATCH-UP (Hidde, 2026-11-19, "waarom niet nu al?"): 31
# people asked to sign in from 15 November on and never got in. The ones on
# the Gmail route got their mail that evening (--days 6 --route gmail); the
# Yahoo, Apple-relay and BT ones need Resend, which was full until midnight
# UTC, so the knocks reach back six days between these two moments and send
# theirs. Expires by itself.
CATCH_UP = (datetime.datetime(2026, 11, 20, 0, 5, tzinfo=datetime.timezone.utc),
            datetime.datetime(2026, 11, 20, 18, 0, tzinfo=datetime.timezone.utc))
if CATCH_UP[0] <= datetime.datetime.now(datetime.timezone.utc) < CATCH_UP[1] and "--days" not in sys.argv:
    GIVE_UP = datetime.timedelta(days=6)
ROUTE = sys.argv[sys.argv.index("--route") + 1] if "--route" in sys.argv else None  # gmail | signed


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


def never_in(user):
    """An account made with an email link that never confirmed or signed in."""
    return ((user.get("app_metadata") or {}).get("provider") == "email"
            and not user.get("email_confirmed_at") and not user.get("last_sign_in_at"))


def stuck_links(key):
    """Accounts with a sign-in link or code they never used, old or new
    (supabase/stuck-signin-links.sql): {user_id: when they asked}."""
    try:
        rows = _call("/rest/v1/rpc/stuck_signin_links", key,
                     {"max_age": f"{GIVE_UP.days} days"})
    except urllib.error.HTTPError as e:
        print("signin_watch: stuck_signin_links unavailable", e.code)
        return {}
    out = {}
    for r in rows:
        t = _ts(r["asked_at"])
        out[r["user_id"]] = min(out.get(r["user_id"], t), t)
    return out


def in_elsewhere(email, all_users):
    """Whether the person behind `email` already got in on another account
    with the same name before the @ (pure, tested). Hidde, 2026-11-20, after
    bounces to outlook.co and tahoo.com reached his inbox: both people had
    signed up again a minute later with the right domain and were in, but the
    watcher kept mailing the typo."""
    local, _, domain = (email or "").lower().partition("@")
    if not local:
        return False
    for u in all_users:
        other = (u.get("email") or "").lower()
        if other == (email or "").lower() or other.partition("@")[0] != local:
            continue
        if u.get("email_confirmed_at") or u.get("last_sign_in_at"):
            return True
    return False


def bounced_addresses(days=7):
    """Addresses whose mail came back as failed (a 5xx bounce notice) in the
    Ancient Trees inbox, INBOX and Spam, read-only. Hidde, 2026-11-20: the
    watcher re-sent to ista@, an unknown Gmail mailbox, and he got the bounce
    again. A delay notice ("Gmail will retry") is not a failure. Without the
    mailbox login, or on any error, an empty set: the watcher then behaves as
    before, never worse."""
    import email as email_lib
    import imaplib
    user = os.environ.get("OUTREACH_SMTP_USER")
    pw = os.environ.get("OUTREACH_SMTP_PASS")
    if not (user and pw):
        return set()
    out = set()
    try:
        box = imaplib.IMAP4_SSL(os.environ.get("OUTREACH_IMAP_HOST", "imap.gmail.com"), timeout=30)
        box.login(user, pw)
        since = (datetime.date.today() - datetime.timedelta(days=days)).strftime("%d-%b-%Y")
        for folder in ("INBOX", "[Gmail]/Spam"):
            if box.select(f'"{folder}"', readonly=True)[0] != "OK":
                continue
            ok, data = box.search(None, f'(SINCE {since} OR FROM "mailer-daemon" FROM "postmaster")')
            for n in data[0].split():
                ok, full = box.fetch(n, "(BODY.PEEK[])")
                out |= failed_recipients(email_lib.message_from_bytes(full[0][1]))
        box.logout()
    except Exception as e:  # never let the inbox stop the watcher
        print("signin_watch: bounce check unavailable", type(e).__name__)
        return set()
    return out


def failed_recipients(msg):
    """The recipients a delivery report says failed for good (pure, tested)."""
    out = set()
    for part in msg.walk():
        if part.get_content_type() != "message/delivery-status":
            continue
        for sub in part.get_payload():
            rcpt = sub.get("Final-Recipient") or sub.get("Original-Recipient")
            action = (sub.get("Action") or "").strip().lower()
            if rcpt and action == "failed":
                out.add(rcpt.split(";")[-1].strip().strip("<>").lower())
    return out


def due(start, email, tries, now):
    """Whether somebody who asked to sign in at `start` and never got in gets
    the mail again now (pure, tested). `tries` older than GIVE_UP belong to an
    earlier time they were stuck and do not count."""
    if not start or now - start < WAIT or now - start > GIVE_UP:
        return False
    tries = [t for t in tries if _ts(t) > now - GIVE_UP]
    signed = mailer.wants_resend(email or "", mailer.EXPECTED)
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
    all_users = {u["id"]: u for u in users(key)}
    for u in all_users.values():  # who got in after a retry
        code = people.ref(u["id"], key)
        row = state["retried"].get(code)
        last_in = _ts(u.get("last_sign_in_at"))
        if row and row.get("tries") and not row.get("got_in") and last_in and last_in > _ts(row["tries"][-1]):
            row["got_in"] = now.isoformat(timespec="minutes")
    # Two kinds of stuck: a new account never in (its creation is the ask), and
    # anybody, new or existing, holding a link they never used.
    starts = {uid: _ts(u.get("created_at")) for uid, u in all_users.items() if never_in(u)}
    for uid, asked in stuck_links(key).items():
        if uid in all_users:
            starts[uid] = min(starts.get(uid, asked), asked)
    todo = []
    bounced = bounced_addresses() if starts else set()
    for uid, start in starts.items():
        u = all_users[uid]
        code = people.ref(uid, key)
        if not u.get("email") or state["retried"].get(code, {}).get("undeliverable"):
            continue
        if u["email"].lower() in bounced:
            # Their mail came back: the address does not exist or refuses us.
            # Recorded, never retried (the address itself is never written).
            state["retried"].setdefault(code, {"tries": []}).update(
                {"undeliverable": now.isoformat(timespec="minutes"), "why": "bounced"})
            print("BOUNCED, skipped", code)
            continue
        if in_elsewhere(u["email"], all_users.values()):
            print("IN ON ANOTHER ACCOUNT, skipped", code)
            continue
        if ROUTE and ROUTE != ("signed" if mailer.wants_resend(u["email"], mailer.EXPECTED) else "gmail"):
            continue
        if due(start, u["email"], state["retried"].get(code, {}).get("tries", []), now):
            todo.append((code, u, start))
    for code, u, start in todo:
        signed = mailer.wants_resend(u.get("email") or "", mailer.EXPECTED)
        kind = "new account" if never_in(u) else "existing account"
        label = f"{code} ({kind}, {'signed route' if signed else 'gmail route'}, asked {start.isoformat()[:16]})"
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
