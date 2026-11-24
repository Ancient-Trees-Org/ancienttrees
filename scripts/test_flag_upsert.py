#!/usr/bin/env python3
"""The country save of both apps upserts a profile row with no display_name,
which the table refused (reader report, 2026-11-22). The server-side fix is a
BEFORE INSERT trigger that keeps the existing name. This test refuses a change
that removes it; migrations.py (health.py's Migrations line) refuses a file
that was never pasted."""
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestFlagUpsertFix(unittest.TestCase):
    def test_trigger_keeps_the_existing_name(self):
        with open(os.path.join(ROOT, "supabase", "flag-upsert-fix.sql"), encoding="utf-8") as fh:
            sql = fh.read()
        self.assertIn("create trigger profile_keep_name before insert on public.profiles", sql)
        self.assertIn("if new.display_name is null then", sql)
        self.assertIn("select p.display_name from public.profiles p", sql)


if __name__ == "__main__":
    unittest.main()
