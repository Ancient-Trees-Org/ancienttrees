#!/usr/bin/env python3
"""google_gate: one connection a run, a ceiling, no retry after a refusal."""
import imaplib
import os
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import google_gate as gg  # noqa: E402

ENV = {"OUTREACH_SMTP_USER": "x@ancienttrees.app", "OUTREACH_SMTP_PASS": "p"}


class Box:
    logins = 0
    refuse = False

    def __init__(self, *a, **k):
        self.state = "NONAUTH"

    def login(self, u, p):
        Box.logins += 1
        if Box.refuse:
            raise imaplib.IMAP4.error("AUTHENTICATIONFAILED")
        self.state = "AUTH"

    def logout(self):
        self.state = "LOGOUT"


class Gate(unittest.TestCase):
    def setUp(self):
        Box.logins, Box.refuse = 0, False
        gg.reset()
        self.p = [mock.patch.dict(os.environ, ENV), mock.patch.object(gg.imaplib, "IMAP4_SSL", Box)]
        for p in self.p:
            p.start()

    def tearDown(self):
        gg.reset()
        for p in self.p:
            p.stop()

    def test_one_login_for_many_callers(self):
        for _ in range(50):
            gg.mailbox()
        self.assertEqual(Box.logins, 1)

    def test_a_refusal_is_never_retried(self):
        Box.refuse = True
        with self.assertRaises(imaplib.IMAP4.error):
            gg.mailbox()
        for _ in range(5):
            with self.assertRaises(gg.GoogleRefused):
                gg.mailbox()
        self.assertEqual(Box.logins, 1)

    def test_the_ceiling_holds_after_logouts(self):
        for _ in range(gg.MAX_LOGINS_PER_RUN):
            gg.mailbox().logout()
        with self.assertRaises(gg.GoogleRefused):
            gg.mailbox()
        self.assertEqual(Box.logins, gg.MAX_LOGINS_PER_RUN)

    def test_no_login_without_credentials(self):
        with mock.patch.dict(os.environ, {"OUTREACH_SMTP_PASS": ""}):
            with self.assertRaises(gg.GoogleRefused):
                gg.mailbox()
        self.assertEqual(Box.logins, 0)

    def test_the_ledger_stays_within_budget(self):
        led = gg.ledger()
        self.assertLessEqual(gg.logins_a_day(led), led["mailbox_logins_per_day_budget"])


if __name__ == "__main__":
    unittest.main()
