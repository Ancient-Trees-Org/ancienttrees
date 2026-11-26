#!/usr/bin/env python3
"""Tests for bug_fixed_mail.py: who is told, when, in which order and words.

    python3 scripts/test_bug_fixed_mail.py
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bug_fixed_mail as b  # noqa: E402


def st(stage, app=True, why="test"):
    return lambda row, store, live: (stage, app, why)


BUG = {"id": "ESC-x", "status": "fixed", "fixed_in": "abc", "file": "ios/A.swift",
       "reader_line": "the country you pick in Edit profile now stays"}
LEDGER = {"1491": {"status": "bug", "bug": "ESC-x"}}


class Order(unittest.TestCase):
    """Hidde, 2026-11-26: first "fixed, comes with the next update", then "out"."""

    def test_an_app_fix_not_out_yet_is_told_at_once(self):
        ready, _ = b.plan(LEDGER, {"ESC-x": BUG}, {}, {}, None, st("coming"))
        self.assertEqual([(r[0], r[2], r[4]) for r in ready], [("1491", "coming", False)])

    def test_coming_is_told_once(self):
        ready, waiting = b.plan(LEDGER, {"ESC-x": BUG}, {"1491": {"coming": "2026-11-26"}}, {}, None, st("coming"))
        self.assertEqual(ready, [])
        self.assertIn("told it is fixed", waiting[0][1])

    def test_out_after_coming_is_the_short_mail(self):
        ready, _ = b.plan(LEDGER, {"ESC-x": BUG}, {"1491": {"coming": "2026-11-26"}}, {}, None, st("live"))
        self.assertEqual([(r[2], r[4]) for r in ready], [("live", True)])

    def test_out_is_told_once(self):
        ready, waiting = b.plan(LEDGER, {"ESC-x": BUG}, {"1491": {"coming": "x", "date": "y"}}, {}, None, st("live"))
        self.assertEqual((ready, waiting), ([], []))

    def test_unfixed_waits(self):
        ready, waiting = b.plan(LEDGER, {"ESC-x": dict(BUG, status="open")}, {}, {}, None,
                                st("unfixed", why="not fixed yet"))
        self.assertEqual(ready, [])
        self.assertIn("not fixed", waiting[0][1])

    def test_no_reader_line_waits(self):
        ready, waiting = b.plan(LEDGER, {"ESC-x": dict(BUG, reader_line="")}, {}, {}, None, st("coming"))
        self.assertEqual(ready, [])
        self.assertIn("reader_line", waiting[0][1])

    def test_only_bug_rows(self):
        ready, waiting = b.plan({"1": {"status": "handled"}}, {"ESC-x": BUG}, {}, {}, None, st("live"))
        self.assertEqual((ready, waiting), ([], []))

    def test_unfixed_row_state(self):
        self.assertEqual(b.state(dict(BUG, status="open"), {}, None)[0], "unfixed")
        self.assertEqual(b.state(dict(BUG, fixed_in=None), {}, None)[0], "unfixed")


class Words(unittest.TestCase):
    def test_platform(self):
        self.assertEqual(b.platform({"file": "ios/x.swift:12"}), "ios")
        self.assertEqual(b.platform({"file": "android/x.kt"}), "android")
        self.assertEqual(b.platform({"file": "site/src/x.ts"}), "web")

    def test_dutch(self):
        self.assertTrue(b.is_dutch("Love de app! Kan alleen het land waar ik woon niet aanpassen"))
        self.assertFalse(b.is_dutch("I have added an ancient tree but it is listed in the wrong place"))

    def test_coming_says_next_update_and_quotes_nothing(self):
        subject, body = b.compose("A tree you added now shows where it stands", "Anna", True, False, "coming")
        self.assertIn("Hi Anna,", body)
        self.assertIn("We fixed it: a tree you added", body)
        self.assertIn("next app update", body)
        self.assertNotIn("Update the app", body)
        self.assertTrue(body.endswith("Ancient Trees"))
        self.assertNotIn("—", body + subject)

    def test_out_after_coming(self):
        subject, body = b.compose("the country you pick now stays", None, True, False, "live", told=True)
        self.assertIn("is out", body)
        self.assertIn("Update the app", body)

    def test_web_fix_one_mail_no_update_line(self):
        _, body = b.compose("the map opens at your tree", None, False, False, "live")
        self.assertTrue(body.startswith("Hi,"))
        self.assertNotIn("Update the app", body)

    def test_dutch_mails(self):
        subject, body = b.compose("je land blijft nu staan", None, True, True, "coming")
        self.assertIn("volgende update", body)
        subject, body = b.compose("je land blijft nu staan", None, True, True, "live", told=True)
        self.assertIn("Werk de app bij", body)


if __name__ == "__main__":
    unittest.main()
