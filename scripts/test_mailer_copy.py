#!/usr/bin/env python3
"""keep_copy logs in to the mailbox once per run, not once per mail
(2026-11-24: 367 logins on 2026-11-20 from GitHub's servers)."""
import os
import sys
import unittest
from email.message import EmailMessage
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mailer  # noqa: E402


class FakeBox:
    logins = 0

    def __init__(self, *a, **k):
        self.appended = 0

    def login(self, u, p):
        FakeBox.logins += 1

    def list(self):
        return ("OK", [b'(\\HasNoChildren \\Sent) "/" "[Gmail]/Sent Mail"'])

    def append(self, *a):
        self.appended += 1

    def logout(self):
        pass


class OneLogin(unittest.TestCase):
    def setUp(self):
        FakeBox.logins = 0
        mailer._close_copy_box()

    def tearDown(self):
        mailer._close_copy_box()

    def test_many_mails_one_login(self):
        env = {"OUTREACH_SMTP_USER": "x@ancienttrees.app", "OUTREACH_SMTP_PASS": "p"}
        with mock.patch.dict(os.environ, env), \
             mock.patch.object(mailer.imaplib, "IMAP4_SSL", FakeBox):
            for _ in range(25):
                mailer.keep_copy(EmailMessage())
        self.assertEqual(FakeBox.logins, 1)

    def test_refused_login_is_not_retried(self):
        class Refused(FakeBox):
            def login(self, u, p):
                FakeBox.logins += 1
                raise mailer.imaplib.IMAP4.error("AUTHENTICATIONFAILED")
        env = {"OUTREACH_SMTP_USER": "x@ancienttrees.app", "OUTREACH_SMTP_PASS": "p"}
        with mock.patch.dict(os.environ, env), \
             mock.patch.object(mailer.imaplib, "IMAP4_SSL", Refused):
            mailer.keep_copy(EmailMessage())
        self.assertEqual(FakeBox.logins, 1)


if __name__ == "__main__":
    unittest.main()
