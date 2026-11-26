"""Nothing a person does stays on the phone (Hidde, 2026-11-26: "NOOIT IETS
LOKAALS OPSLAAN ALTIJD AAN ACCOUNT", after account/DraftStore.kt kept a tree
being added on an Android phone and crossdevice.py never looked at Android)."""
import os
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import crossdevice as c  # noqa: E402


class ClosedListTest(unittest.TestCase):
    def test_a_new_device_store_is_refused(self):
        known = {"android-file:DraftStore.kt": {"verdict": "device", "why": "unsent draft"}}
        self.assertEqual(c.unasked_device_stores(known), ["android-file:DraftStore.kt"])

    def test_the_closed_list_passes(self):
        known = {"hero.index.v1": {"verdict": "device"}, "saves": {"verdict": "account"}}
        self.assertEqual(c.unasked_device_stores(known), [])

    def test_android_storage_is_seen(self):
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, "DraftStore.kt")
            open(f, "w").write('val dir = File(context.filesDir, "draft-tree")\n')
            old = c.ANDROID
            c.ANDROID = d
            try:
                self.assertIn("android-file:DraftStore.kt", c.found())
            finally:
                c.ANDROID = old


if __name__ == "__main__":
    unittest.main()
