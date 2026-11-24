#!/usr/bin/env python3
"""test_emulator_lock.py - the emulator lock never hands a script Hidde's phone.

2026-11-24: with his Samsung on the cable and no emulator running, a ButtonWalk
uninstalled his Play copy of the app. These pin what `adb devices` may yield.

    python3 scripts/test_emulator_lock.py
"""
import os
import pathlib
import sys
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import emulator_lock  # noqa: E402

PHONE_ONLY = "List of devices attached\nR5CR61FY7EE            device usb:1048576X product:p3sxeea model:SM_G998B\n\n"
BOTH = ("List of devices attached\nR5CR61FY7EE            device usb:1048576X model:SM_G998B\n"
        "emulator-5554          device product:sdk_gphone64_arm64\n\n")
OFFLINE = "List of devices attached\nemulator-5554          offline\n\n"


class Listing(unittest.TestCase):
    def test_a_phone_on_the_cable_is_never_an_emulator(self):
        self.assertEqual(emulator_lock.emulators(PHONE_ONLY), [])

    def test_the_emulator_is_found_beside_the_phone(self):
        self.assertEqual(emulator_lock.emulators(BOTH), ["emulator-5554"])

    def test_an_offline_emulator_is_not_used(self):
        self.assertEqual(emulator_lock.emulators(OFFLINE), [])


class Pin(unittest.TestCase):
    def run_with(self, listing, env):
        done = mock.Mock(stdout=listing)
        with mock.patch.object(emulator_lock.subprocess, "run", return_value=done), \
                mock.patch.dict(os.environ, env, clear=True):
            return emulator_lock.pin_to_emulator(), os.environ.get("ANDROID_SERIAL")

    def test_refuses_with_only_the_phone(self):
        with self.assertRaises(SystemExit):
            self.run_with(PHONE_ONLY, {})

    def test_pins_the_emulator_when_both_are_there(self):
        self.assertEqual(self.run_with(BOTH, {}), ("emulator-5554", "emulator-5554"))

    def test_refuses_a_serial_that_names_the_phone(self):
        with self.assertRaises(SystemExit):
            self.run_with(BOTH, {"ANDROID_SERIAL": "R5CR61FY7EE"})


if __name__ == "__main__":
    unittest.main()
