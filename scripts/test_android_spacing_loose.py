"""A spacing reason keeps covering its gap when a species row's tree count grows
(android_spacing.loose; the job went red on 2026-11-25 when Oriental Plane went
from 70 to 75 trees)."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import android_spacing as a  # noqa: E402


class LooseTest(unittest.TestCase):
    def test_a_count_does_not_change_the_key(self):
        self.assertEqual(a.loose("Growing near you first -> Oriental Plane, Platanus orientalis, 70"),
                         a.loose("Growing near you first -> Oriental Plane, Platanus orientalis, 1,075"))

    def test_other_numbers_stay(self):
        self.assertEqual(a.loose("116-136 years right"), "116-136 years right")
        self.assertEqual(a.loose("tab-discover left"), "tab-discover left")

    def test_the_judge_uses_it(self):
        allowed = [{"what": "x -> Oak, Quercus robur, 70", "why": "header frame"}]
        self.assertIn(a.loose("x -> Oak, Quercus robur, 75"), {a.loose(r["what"]) for r in allowed})


if __name__ == "__main__":
    unittest.main()
