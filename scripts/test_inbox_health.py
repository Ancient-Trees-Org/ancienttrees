#!/usr/bin/env python3
"""Tests for inbox_health.py: the alarm when mail stops reaching us."""
import datetime
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inbox_health as ih  # noqa: E402

D = datetime.date(2026, 11, 24)


class FakeImap:
    def __init__(self, stamp):
        self.stamp = stamp

    def select(self, box, readonly=True):
        return ("OK", [b"1"])

    def search(self, *a):
        return ("OK", [b"1 2 3" if self.stamp else b""])

    def fetch(self, mid, what):
        return ("OK", [b'3 (INTERNALDATE "%s")' % self.stamp.encode()])


class Assess(unittest.TestCase):
    def test_fresh_mail_is_ok(self):
        ok, _ = ih.assess({"status": "ok", "checked_day": "2026-11-24", "newest_mail_day": "2026-11-23"}, D)
        self.assertTrue(ok)

    def test_two_quiet_days_is_red(self):
        ok, line = ih.assess({"status": "ok", "checked_day": "2026-11-24", "newest_mail_day": "2026-11-22"}, D)
        self.assertFalse(ok)
        self.assertIn("No mail", line)

    def test_no_mail_in_a_week_is_red(self):
        ok, _ = ih.assess({"status": "ok", "checked_day": "2026-11-24", "newest_mail_day": None}, D)
        self.assertFalse(ok)

    def test_failed_login_is_red(self):
        ok, line = ih.assess({"status": "failing", "checked_day": "2026-11-24", "failing_since": "2026-11-24",
                              "error": "AUTHENTICATIONFAILED"}, D)
        self.assertFalse(ok)
        self.assertIn("will not open", line)

    def test_a_check_that_stopped_is_red(self):
        ok, line = ih.assess({"status": "ok", "checked_day": "2026-11-20", "newest_mail_day": "2026-11-20"}, D)
        self.assertFalse(ok)
        self.assertIn("has not run", line)

    def test_nothing_recorded_is_unknown(self):
        self.assertIsNone(ih.assess({}, D)[0])


class Record(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(tempfile.mkdtemp(), "inbox-health.json")

    def test_reads_the_newest_arrival_day(self):
        ih.record(FakeImap("23-Nov-2026 22:15:00 +0100"), self.path, D)
        self.assertEqual(ih.load(self.path)["newest_mail_day"], "2026-11-23")

    def test_writes_only_on_change(self):
        self.assertTrue(ih.record(FakeImap("24-Nov-2026 08:00:00 +0000"), self.path, D))
        self.assertFalse(ih.record(FakeImap("24-Nov-2026 09:00:00 +0000"), self.path, D))

    def test_failure_keeps_its_first_day(self):
        ih.record_failure("x", self.path, D)
        ih.record_failure("x", self.path, D + datetime.timedelta(days=1))
        self.assertEqual(ih.load(self.path)["failing_since"], "2026-11-24")


if __name__ == "__main__":
    unittest.main()
