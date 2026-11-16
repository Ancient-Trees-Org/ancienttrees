"""Exercise mailer's route rule with two fake SMTP servers (Resend and Gmail),
no real mail. Cases: who goes where; Resend refusing; Gmail refusing; Gmail
unreachable; Resend not configured; check(); qa's rule check."""
import os
import smtplib
import sys
from email.message import EmailMessage
from unittest import mock

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
os.chdir(ROOT)
import mailer  # noqa: E402

sent = []


class Fake:
    behaviour = {}  # host -> "ok" | "refuse" | "down"

    def __init__(self, host, port, timeout=30):
        self.host = host
        if Fake.behaviour.get(host) == "down":
            raise OSError("connection refused")

    def starttls(self):
        pass

    def login(self, u, p):
        pass

    def send_message(self, msg):
        if Fake.behaviour.get(self.host) == "refuse":
            raise smtplib.SMTPDataError(550, b"daily limit")
        sent.append((self.host, msg["To"]))

    def quit(self):
        pass


# Fake test addresses at personal mail providers, built from parts so qa's
# check_no_reader_traces_in_the_repo() never mistakes them for a person's.
AT = "@"
X_GMAIL = "x" + AT + "gmail.com"
A_GMAIL = "a" + AT + "gmail.com"
B_YAHOO_UK = "b" + AT + "yahoo.co.uk"
B_YAHOO = "b" + AT + "yahoo.com"
C_AOL = "c" + AT + "aol.com"


CREDS = {"SMTP_HOST": "gmail", "SMTP_PORT": "587", "SMTP_USER": X_GMAIL, "SMTP_PASS": "p"}
ENV = {"RESEND_SMTP_HOST": "resend", "RESEND_SMTP_PASS": "k"}


def msg(to):
    m = EmailMessage()
    m["To"], m["From"], m["Subject"] = to, "Ancient Trees <info@ancienttrees.app>", "t"
    m.set_content("x")
    return m


def run(kind, tos, behaviour, env=ENV):
    sent.clear()
    Fake.behaviour = behaviour
    with mock.patch.object(smtplib, "SMTP", Fake), mock.patch.dict(os.environ, env, clear=False), \
         mock.patch.object(mailer, "keep_copy", lambda m: None), \
         mock.patch.object(mailer, "last_sent", lambda a: None):
        if not env:
            for k in ENV:
                os.environ.pop(k, None)
        s = mailer.connect(CREDS, kind=kind)
        for t in tos:
            s.send_message(msg(t))
        s.quit()
    return list(sent)


fails = 0


def expect(name, got, want):
    global fails
    ok = got == want
    fails += not ok
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else f": got {got}, want {want}"))


expect("expected mail: gmail, yahoo via resend",
       run(mailer.EXPECTED, [A_GMAIL, B_YAHOO_UK, C_AOL], {}),
       [("gmail", A_GMAIL), ("resend", B_YAHOO_UK), ("resend", C_AOL)])
expect("first mail: all via resend",
       run(mailer.FIRST, [A_GMAIL, B_YAHOO], {}),
       [("resend", A_GMAIL), ("resend", B_YAHOO)])
expect("resend full: first mail falls to gmail, and stays there",
       run(mailer.FIRST, ["a@x.org", "b@y.org"], {"resend": "refuse"}),
       [("gmail", "a@x.org"), ("gmail", "b@y.org")])
expect("gmail full: expected mail falls to resend",
       run(mailer.EXPECTED, [A_GMAIL], {"gmail": "refuse"}),
       [("resend", A_GMAIL)])
expect("gmail down: expected mail via resend",
       run(mailer.EXPECTED, [A_GMAIL], {"gmail": "down"}),
       [("resend", A_GMAIL)])
expect("no resend configured: yahoo via gmail",
       run(mailer.EXPECTED, [B_YAHOO], {}, env={}),
       [("gmail", B_YAHOO)])
try:
    run(mailer.FIRST, ["a@x.org"], {"resend": "refuse", "gmail": "refuse"})
    expect("both refuse: raises", "no error", "error")
except smtplib.SMTPResponseException:
    expect("both refuse: raises", "error", "error")

Fake.behaviour = {"gmail": "down"}
with mock.patch.object(smtplib, "SMTP", Fake), mock.patch.dict(os.environ, ENV):
    expect("check(): expected kind with gmail down reports resend",
           mailer.connect(CREDS, kind=mailer.EXPECTED).check(), "resend")

import qa  # noqa: E402
expect("qa rule check clean", qa.check_one_mail_route_rule(), [])
print("FAILS:", fails)
sys.exit(1 if fails else 0)
