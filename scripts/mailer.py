"""One door for every mail we send, and one rule for which route it takes:
signed for ancienttrees.app (Resend) where it matters, Gmail for the rest.
The rule since 2026-11-16 is above wants_resend(); what follows is how it grew.

Why (2026-10-12): every mail went out through Hidde's Gmail wearing
info@ancienttrees.app, and Gmail signs such mail for gmail.com, never for our
domain. Yahoo refused it outright ("sender is unauthenticated ... DKIM"), and
other providers are free to file it as spam without saying so. Resend signs
with a DKIM key published under resend._domainkey.ancienttrees.app (set up at
TransIP the same day, with a DMARC record beside it).

So (until 2026-11-16): when RESEND_SMTP_* is set, mail left through Resend;
otherwise through OUTREACH_SMTP_* exactly as before, so a machine without the
new key keeps working. Today the rule picks per mail and either route stands
in for the other. Gmail is still the inbox (replies arrive through ImprovMX), and a
mail sent through Resend never lands in Gmail's Sent folder by itself, which
outreach_inbox.py reads to know what was answered. keep_copy() puts it there.

    server = mailer.connect(creds, kind=mailer.EXPECTED)  # or FIRST (default)
    server.send_message(msg)             # sends, then files a copy in Sent
    server.quit()

ONE REST PERIOD ACROSS EVERY ROUTE (Hidde, 2026-10-25: "we hebben die porto
dude nu in totaal 3 keer gemaild kun je in het vervolg altijd checken voor je
mailt of we niet iemand al eerder hebben gemaild"). Five scripts send mail
(outreach batches, ambassador invitation, editor mail and heads-up, reader
replies, photo-live and congratulation mails) and each guarded only its own
history, so one person could hear from three of them in a week. Every one of
them sends through this door, so the check lives here: an address that got any
mail logged in data/outreach-sent.json in the last RECENT_DAYS is refused with
RecentlyMailed. The automatic routes catch it and try again on a later knock.
Let through without the check: a reply in a thread (In-Reply-To set), and a
caller that passes recent_ok, a sentence saying why (an answer to a message
the person just sent us).
"""
import datetime
import imaplib
import json
import os
import smtplib
import time
from email.utils import formatdate, make_msgid, parseaddr

SENT_LOG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "outreach-sent.json")
RECENT_DAYS = 7


class RecentlyMailed(Exception):
    pass


def last_sent(addr, days=RECENT_DAYS):
    """The latest logged mail to this address within `days`, or None. A missing
    log answers None: the routes that send pull it first (nightly.yml)."""
    addr = (addr or "").strip().lower()
    try:
        sent = json.load(open(SENT_LOG, encoding="utf-8")).get("sent", [])
    except (OSError, ValueError):
        return None
    since = (datetime.date.today() - datetime.timedelta(days=days)).isoformat()
    hits = [s for s in sent if (s.get("to") or "").strip().lower() == addr and (s.get("date") or "") >= since]
    return max(hits, key=lambda s: s.get("date") or "") if hits else None


# SIGNED WHERE IT MATTERS, GMAIL FOR THE REST (Hidde, 2026-11-16, "ok how to
# set up this", after the Guardian day: 71 email sign-ups in four hours, and
# Resend's free plan stops at 100 a day and 3,000 a month). One rule for every
# mail we send, here and in the Supabase hook (supabase/functions/send-email):
#   - an address on Yahoo's servers: Resend, whatever the mail, because Yahoo
#     refuses mail not signed for our domain;
#   - a first mail to a stranger (outreach, press: kind FIRST): Resend, because
#     unsigned cold mail goes to spam without a bounce;
#   - mail somebody asked for or expects (sign-in, welcome, a reply to them, a
#     congratulation, an ambassador mail: kind EXPECTED): Gmail, so a press-day
#     peak never eats Resend's allowance.
# Either route full or down: the other one. The Yahoo list is written twice,
# here and in the hook; qa's check_one_mail_route_rule() keeps them equal.
FIRST, EXPECTED = "first", "expected"
YAHOO_FAMILY = ("yahoo", "ymail", "rocketmail", "aol", "aim", "verizon", "att",
                "sbcglobal", "bellsouth", "frontier")


def on_yahoo(addr):
    """True for an address whose mail Yahoo's servers receive."""
    domain = (addr or "").strip().lower().rpartition("@")[2]
    return domain.split(".")[0] in YAHOO_FAMILY


def wants_resend(addr, kind):
    return kind == FIRST or on_yahoo(addr)


def _resend_route():
    host = os.environ.get("RESEND_SMTP_HOST")
    if host and os.environ.get("RESEND_SMTP_PASS"):
        return (host, int(os.environ.get("RESEND_SMTP_PORT") or 587),
                os.environ.get("RESEND_SMTP_USER") or "resend", os.environ["RESEND_SMTP_PASS"])
    return None


def keep_copy(msg):
    """File a sent mail in Gmail's Sent folder, read with the same app password
    the inbox reader uses. Never raises: a missing copy costs a thread view,
    not the send."""
    user = os.environ.get("OUTREACH_SMTP_USER") or ""
    pw = os.environ.get("OUTREACH_SMTP_PASS")
    if not (user.endswith("@gmail.com") and pw):
        return
    try:
        box = imaplib.IMAP4_SSL(os.environ.get("OUTREACH_IMAP_HOST", "imap.gmail.com"), timeout=30)
        box.login(user, pw)
        box.append('"[Gmail]/Sent Mail"', "\\Seen",
                   imaplib.Time2Internaldate(time.time()), msg.as_bytes())
        box.logout()
    except Exception as e:  # noqa: BLE001
        print(f"mailer: sent, but no copy in Gmail's Sent folder ({type(e).__name__})")


def _gmail_route(creds):
    """The old route (OUTREACH_SMTP_*), or None when this machine has none."""
    if not creds or not creds.get("SMTP_HOST") or not creds.get("SMTP_PASS"):
        return None
    return (creds["SMTP_HOST"], int(creds.get("SMTP_PORT") or 587), creds["SMTP_USER"], creds["SMTP_PASS"])


def _open(host, port, user, pw, timeout):
    smtp = smtplib.SMTP(host, port, timeout=timeout)
    smtp.starttls()
    smtp.login(user, pw)
    return smtp


# What a server says when it will not take a mail (Resend's free plan stops at
# 100 a day; Gmail stops at about 500): an SMTP refusal. A dropped connection
# is not on the list, because the mail may have left and the other route would
# send it twice.
_REFUSED = (smtplib.SMTPResponseException, smtplib.SMTPRecipientsRefused)


class _Server:
    """Both routes, opened when first needed, each mail on the route the rule
    gives it (wants_resend), the other route when that one refuses or cannot be
    reached. GMAIL WHEN RESEND IS FULL (Hidde, 2026-11-16, "Yes, add fallback",
    after the Guardian wave took Resend to 80% of its 100 a day): once a route
    has refused, the rest of this connection skips it. Mail through Gmail is
    unsigned for our domain, so on a full day Yahoo bounces it; everyone else
    hears from us the same day."""

    def __init__(self, creds=None, timeout=30, kind=FIRST):
        self._creds, self._timeout, self._kind = creds, timeout, kind
        self._open_smtp = {}      # "resend" | "gmail" -> smtplib.SMTP
        self._dead = set()        # routes that refused or could not be reached

    def _route(self, name):
        return _resend_route() if name == "resend" else _gmail_route(self._creds)

    def _conn(self, name):
        if name in self._dead or not self._route(name):
            return None
        if name not in self._open_smtp:
            try:
                self._open_smtp[name] = _open(*self._route(name), self._timeout)
            except (smtplib.SMTPException, OSError) as e:
                print(f"mailer: {name} unreachable ({type(e).__name__}); trying the other route")
                self._dead.add(name)
                return None
        return self._open_smtp[name]

    def _send(self, name, msg):
        self._conn(name).send_message(msg)
        if name == "resend":
            keep_copy(msg)  # Gmail files its own mail in Sent

    def send_message(self, msg, recent_ok=None):
        to = parseaddr(msg["To"] or "")[1]
        if not recent_ok and not msg["In-Reply-To"]:
            prior = last_sent(to)
            if prior:
                raise RecentlyMailed(
                    f"{to} already had a mail on {prior.get('date')} "
                    f"({prior.get('batch') or prior.get('outlet') or '?'}: {(prior.get('subject') or '')[:60]}); "
                    f"{RECENT_DAYS}-day rest across every route")
        if not msg["Date"]:
            msg["Date"] = formatdate(localtime=True)
        if not msg["Message-ID"]:
            msg["Message-ID"] = make_msgid(domain="ancienttrees.app")
        order = ["resend", "gmail"] if wants_resend(to, self._kind) else ["gmail", "resend"]
        last_refusal = None
        for name in order:
            if self._conn(name) is None:
                continue
            try:
                self._send(name, msg)
                return name
            except _REFUSED as e:
                print(f"mailer: {name} refused ({type(e).__name__} {str(e)[:120]}); trying the other route")
                self._dead.add(name)
                last_refusal = e
        if last_refusal is not None:
            raise last_refusal
        raise smtplib.SMTPServerDisconnected("no mail route reachable on this machine")

    def check(self):
        """Log in on the route this kind of mail takes first (the other when
        that one is down) and say which, or raise: a transport probe that
        sends nothing."""
        order = ["resend", "gmail"] if self._kind == FIRST else ["gmail", "resend"]
        for name in order:
            if self._conn(name) is not None:
                return name
        raise smtplib.SMTPServerDisconnected("no mail route reachable on this machine")

    def quit(self):
        for smtp in self._open_smtp.values():
            try:
                smtp.quit()
            except Exception:  # noqa: BLE001
                pass

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.quit()


def connect(creds, timeout=30, kind=FIRST):
    """A sender for one batch. `kind` is FIRST for a first mail to a stranger
    (the default, signed) and EXPECTED for mail a person asked for or expects.
    Connections open on the first mail that needs them, so a machine without
    one of the two routes still sends through the other."""
    if not _resend_route() and not _gmail_route(creds):
        raise smtplib.SMTPServerDisconnected("no mail route configured on this machine")
    return _Server(creds, timeout, kind)
