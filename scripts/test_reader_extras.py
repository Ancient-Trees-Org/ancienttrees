#!/usr/bin/env python3
"""Every photograph a reader sends with a tree reaches the page, or says why not.

    python3 scripts/test_reader_extras.py

The bug (2026-11-26, a tester): a tree sent with three photographs went live
with one, because no script published the further ones. Red before
reader_extras.py existed: nothing put extra 1 and 2 on the tree.
"""
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("SUPABASE_SERVICE_KEY", "test-service-key")
import reader_extras as rx  # noqa: E402
import sightings_publish as sp  # noqa: E402

SID = "11111111-2222-3333-4444-555555555555"


def jpeg(path, shade):
    from PIL import Image
    im = Image.new("RGB", (120, 90), (shade, 120, 255 - shade))
    for x in range(0, 120, 10):  # a pattern, so the hashes differ by shade and layout
        for y in range(90):
            im.putpixel((x, y), (255 - shade, shade, 0))
    if shade > 128:
        im = im.transpose(Image.FLIP_LEFT_RIGHT).rotate(90, expand=True)
    im.save(path, "JPEG")


class TestExtras(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.tmp, "data", "cities"))
        os.makedirs(os.path.join(self.tmp, "out", "sightings"))
        os.makedirs(os.path.join(self.tmp, "photos"))
        self.saved = (rx.ROOT, rx.LEDGER, rx.LEADS, rx.PROCESSED, rx.OUT, sp.PHOTOS)
        rx.ROOT = self.tmp
        rx.LEDGER = os.path.join(self.tmp, "data", "reader-extras.json")
        rx.LEADS = os.path.join(self.tmp, "data", "leads.json")
        rx.PROCESSED = os.path.join(self.tmp, "data", "processed.json")
        rx.OUT = os.path.join(self.tmp, "out", "sightings")
        sp.PHOTOS = os.path.join(self.tmp, "photos")
        lead_file = os.path.join(sp.PHOTOS, "tst_001-oak.jpg")
        jpeg(lead_file, 10)
        self.extras = []
        for n, shade in ((1, 90), (2, 200)):
            p = os.path.join(rx.OUT, f"{SID}-extra-{n}.jpg")
            jpeg(p, shade)
            self.extras.append(p)
        city = {"trees": [{"id": "tst_001", "name": "Oak", "photo": {
            "url": f"{sp.BASE_URL}/photos/tst_001-oak.jpg", "source": "contributor",
            "contributor_user_id": "p_aaaaaaaaaaaaaaaaaaaaaaaa", "sighting_id": SID}}]}
        json.dump(city, open(os.path.join(self.tmp, "data", "cities", "testville.json"), "w"))
        json.dump({"leads": [{"sighting_id": SID, "status": "published", "published_as": "testville/tst_001",
                              "user_id": "p_aaaaaaaaaaaaaaaaaaaaaaaa", "extra_files": self.extras}]},
                  open(rx.LEADS, "w"))

    def tearDown(self):
        rx.ROOT, rx.LEDGER, rx.LEADS, rx.PROCESSED, rx.OUT, sp.PHOTOS = self.saved
        shutil.rmtree(self.tmp)

    def tree(self):
        return json.load(open(os.path.join(self.tmp, "data", "cities", "testville.json")))["trees"][0]

    def test_a_published_tree_with_extras_is_flagged_until_each_has_a_verdict(self):
        self.assertEqual(len(rx.check()), 2)

    def test_every_extra_goes_in_the_gallery(self):
        led = rx.ledger()
        for n, p in enumerate(self.extras, 1):
            word = rx.publish_one(led, SID, n, p, 5, "testville", "tst_001", None, "2026-11-26")
            self.assertEqual(word, "published")
        rx.save_ledger(led)
        photos = self.tree().get("photos") or []
        self.assertEqual([x["sighting_id"] for x in photos], [f"{SID}-extra-1", f"{SID}-extra-2"])
        self.assertEqual(photos[0]["taken_month"], 5)
        self.assertEqual(rx.check(), [])

    def test_extras_survive_the_lead_being_judged_again(self):
        # The promotion branch clears the strip of the lead's own sighting id;
        # an extra's id is suffixed so it stays.
        led = rx.ledger()
        rx.publish_one(led, SID, 1, self.extras[0], None, "testville", "tst_001", None, "2026-11-26")
        sp_root = sp.ROOT
        sp.ROOT = self.tmp
        try:
            sp.apply_to_city({"city_slug": "testville", "tree_id": "tst_001", "sighting_id": SID},
                             {"url": f"{sp.BASE_URL}/photos/tst_001-oak.jpg", "sighting_id": SID})
        finally:
            sp.ROOT = sp_root
        self.assertEqual(len(self.tree().get("photos") or []), 1)

    def test_one_already_on_the_page_is_not_added_twice(self):
        shutil.copyfile(self.extras[0], os.path.join(sp.PHOTOS, "tst_001-oak-extra1.jpg"))
        path = os.path.join(self.tmp, "data", "cities", "testville.json")
        city = json.load(open(path))
        city["trees"][0]["photos"] = [{"url": f"{sp.BASE_URL}/photos/tst_001-oak-extra1.jpg", "sighting_id": SID}]
        json.dump(city, open(path, "w"))
        led = rx.ledger()
        self.assertEqual(rx.publish_one(led, SID, 1, self.extras[0], None, "testville", "tst_001", None, "x"),
                         "already_live")
        self.assertEqual(len(self.tree()["photos"]), 1)

    def test_no_extra_without_its_main_photo_on_the_page(self):
        path = os.path.join(self.tmp, "data", "cities", "testville.json")
        city = json.load(open(path))
        city["trees"][0]["photo"]["sighting_id"] = "someone-else"
        json.dump(city, open(path, "w"))
        led = rx.ledger()
        self.assertEqual(rx.publish_one(led, SID, 1, self.extras[0], None, "testville", "tst_001", None, "x"),
                         "main_off_page")

    def test_a_reason_must_come_from_the_closed_list(self):
        self.assertEqual(rx.main(["--leave", SID, "1", "weaker_than_the_lead"]), 2)
        self.assertEqual(rx.main(["--leave", SID, "1", "person", "a selfie"]), 0)
        self.assertEqual(rx.ledger()["sightings"][SID]["extras"]["1"]["reason"], "person")


if __name__ == "__main__":
    unittest.main()
