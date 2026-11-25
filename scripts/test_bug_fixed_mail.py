#!/usr/bin/env python3
"""Tests for bug_fixed_mail.py: who is told, when, and in which words.

    python3 scripts/test_bug_fixed_mail.py
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bug_fixed_mail as b  # noqa: E402


def always(ok, why="test"):
    return lambda row, store, live: (ok, why)


BUG = {"id": "ESC-x", "status": "fixed", "fixed_in": "abc", "file": "ios/A.swift",
       "reader_line": "the country you pick in Edit profile now stays"}


class Plan(unittest.TestCase):
    def test_a_shipped_fix_with_a_line_is_ready(self):
        ready, waiting = b.plan({"1491": {"status": "bug", "bug": "ESC-x"}}, {"ESC-x": BUG}, {}, {}, None, always(True))
        self.assertEqual([r[0] for r in ready], ["1491"])
        self.assertEqual(waiting, [])

    def test_not_shipped_waits(self):
        ready, waiting = b.plan({"1491": {"status": "bug", "bug": "ESC-x"}}, {"ESC-x": BUG}, {}, {}, None,
                                always(False, "waits for iPhone build 42 in the App Store"))
        self.assertEqual(ready, [])
        self.assertIn("build 42", waiting[0][1])

    def test_no_reader_line_waits(self):
        row = dict(BUG, reader_line="")
        ready, waiting = b.plan({"1": {"status": "bug", "bug": "ESC-x"}}, {"ESC-x": row}, {}, {}, None, always(True))
        self.assertEqual(ready, [])
        self.assertIn("reader_line", waiting[0][1])

    def test_mailed_once(self):
        ready, _ = b.plan({"1": {"status": "bug", "bug": "ESC-x"}}, {"ESC-x": BUG}, {"1": {"bug": "ESC-x"}}, {}, None,
                          always(True))
        self.assertEqual(ready, [])

    def test_only_bug_rows(self):
        ready, waiting = b.plan({"1": {"status": "handled"}}, {"ESC-x": BUG}, {}, {}, None, always(True))
        self.assertEqual((ready, waiting), ([], []))


class Shipped(unittest.TestCase):
    def test_unfixed_row_never_ships(self):
        self.assertFalse(b.shipped(dict(BUG, status="open"), {}, None)[0])
        self.assertFalse(b.shipped(dict(BUG, fixed_in=None), {}, None)[0])

    def test_web_needs_the_live_commit(self):
        self.assertFalse(b.shipped(dict(BUG, file="site/src/x.ts"), {}, None)[0])


class Words(unittest.TestCase):
    def test_platform(self):
        self.assertEqual(b.platform({"file": "ios/x.swift:12"}), "ios")
        self.assertEqual(b.platform({"file": "android/x.kt"}), "android")
        self.assertEqual(b.platform({"file": "site/src/x.ts"}), "web")
        self.assertEqual(b.platform({"file": "supabase/x.sql"}), "web")

    def test_dutch(self):
        self.assertTrue(b.is_dutch("Love de app! Kan alleen het land waar ik woon niet aanpassen"))
        self.assertFalse(b.is_dutch("I have added an ancient tree but it is listed in the wrong place"))

    def test_app_mail_asks_to_update_and_quotes_nothing(self):
        subject, body = b.compose("the country you pick now stays", "Anna", "ios", False)
        self.assertIn("Hi Anna,", body)
        self.assertIn("Update the app", body)
        self.assertTrue(body.endswith("Ancient Trees"))
        self.assertNotIn("—", body + subject)

    def test_web_mail_has_no_update_line(self):
        _, body = b.compose("the map opens at your tree", None, "web", False)
        self.assertTrue(body.startswith("Hi,"))
        self.assertNotIn("Update the app", body)

    def test_dutch_mail(self):
        subject, body = b.compose("je land blijft nu staan", None, "ios", True)
        self.assertIn("Opgelost", subject)
        self.assertIn("Werk de app bij", body)


if __name__ == "__main__":
    unittest.main()
