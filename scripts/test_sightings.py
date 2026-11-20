#!/usr/bin/env python3
"""Unit tests for the reader-photograph loop: matching and the photo block.

    python3 scripts/test_sightings.py
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Codes need a key; a test key when the real one is not around (CI).
os.environ.setdefault("SUPABASE_SERVICE_KEY", "test-service-key")
import sightings_inbox as inbox  # noqa: E402
import sightings_publish as pub  # noqa: E402

INDEX = {
    "ams_001": {"slug": "amsterdam", "city": "Amsterdam", "name": "The Wertheimpark Wingnut",
                "lat": 52.3670, "lng": 4.9050, "photo_status": "none", "photo_source": None, "path": ""},
    "ams_002": {"slug": "amsterdam", "city": "Amsterdam", "name": "Another tree",
                "lat": 52.3700, "lng": 4.9100, "photo_status": "approved", "photo_source": None, "path": ""},
}


class TestMatch(unittest.TestCase):
    def test_app_tree_id_wins_even_when_gps_is_off(self):
        tid, how, d = inbox.match({"tree_id": "ams_002", "lat": 52.3670, "lng": 4.9050}, INDEX)
        self.assertEqual((tid, how), ("ams_002", "app"))
        self.assertGreater(d, 100)

    def test_unknown_tree_id_falls_through_to_distance(self):
        tid, how, d = inbox.match({"tree_id": "gone_999", "lat": 52.36701, "lng": 4.90501}, INDEX)
        self.assertEqual((tid, how), ("ams_001", "distance"))
        self.assertLessEqual(d, inbox.MATCH_M)

    def test_nearest_within_threshold(self):
        tid, how, d = inbox.match({"tree_id": None, "lat": 52.36715, "lng": 4.90510}, INDEX)
        self.assertEqual((tid, how), ("ams_001", "distance"))

    def test_too_far_is_a_lead_not_a_guess(self):
        tid, how, d = inbox.match({"tree_id": None, "lat": 52.3690, "lng": 4.9050}, INDEX)
        self.assertEqual((tid, how), (None, "none"))
        self.assertGreater(d, inbox.MATCH_M)

    def test_no_coordinates(self):
        self.assertEqual(inbox.match({"tree_id": None, "lat": None, "lng": None}, INDEX), (None, "none", None))


class TestPhotoBlock(unittest.TestCase):
    ENTRY = {"sighting_id": "abc-123", "user_id": "u-1", "display_name": "Katy",
             "tree_id": "ams_001", "tree_name": "The Wertheimpark Wingnut",
             "city_slug": "amsterdam", "city": "Amsterdam", "taken_at": "2026-09-03T10:00:00Z"}

    def test_block_carries_both_takedown_fields(self):
        b = pub.photo_block(self.ENTRY, 1200, 1600, "good frame", "2026-09-04")
        self.assertEqual(b["source"], "contributor")
        # The code, never the id: data/cities is public (people.py, 2026-10-19).
        self.assertEqual(b["contributor_user_id"], pub.people.ref("u-1"))
        self.assertEqual(b["status"], "approved")
        self.assertEqual((b["width"], b["height"]), (1200, 1600))

    def test_an_extras_url_follows_its_own_file(self):
        """An `add` verdict writes the file under a name carrying the sighting
        id so it cannot overwrite the lead; the url has to point at THAT file.
        It used to point at the lead's, apply_to_city's duplicate check dropped
        the extra, and the orphaned file failed QA and was deleted: the Paris
        Turkey Oak close-up a reader sent on 2026-10-01 was lost that way."""
        lead = pub.photo_block(self.ENTRY, 1, 1, "", "2026-10-02")
        extra = pub.photo_block(self.ENTRY, 1, 1, "", "2026-10-02",
                                fname="ams_001-the-wertheimpark-wingnut-abc-123.jpg")
        self.assertTrue(extra["url"].endswith("/photos/ams_001-the-wertheimpark-wingnut-abc-123.jpg"))
        self.assertNotEqual(extra["url"], lead["url"])

    def test_no_name_is_printed_beside_a_readers_photograph(self):
        """Hidde, 2026-09-04: "laten we niet mensen hun naam noemen, laten we
        alleen hun fotos gebruiken als ze goed zijn, het kan mensen afschrikken
        als hun naam erbij staat."

        These two tests asserted the OPPOSITE until 2026-09-08, because they
        were written the day before that ruling and nothing failed loudly
        enough to get them read: they had been red for four days. A red test
        nobody fixes is a gate nobody has, which is the same lesson this
        project already recorded about ios.yml.
        """
        b = pub.photo_block(self.ENTRY, 1, 1, "", "2026-09-04")
        self.assertIsNone(b["attribution"])
        self.assertTrue(b["license"].lower().startswith("provided by"))
        self.assertNotIn("Katy", json_dump(b))
        self.assertNotIn("@", json_dump(b))

    def test_the_account_id_travels_even_though_the_name_does_not(self):
        """The id is the whole of the deletion promise in /terms: a published
        photograph is a copy no database cascade reaches, so photo_takedown.py
        needs something to ask Supabase about. Preflight refuses one without
        the other in either direction."""
        b = pub.photo_block(dict(self.ENTRY, display_name=""), 1, 1, "", "2026-09-04")
        self.assertEqual(b["source"], "contributor")
        self.assertTrue(b["contributor_user_id"])
        self.assertIsNone(b["attribution"])

    def test_url_is_ours_and_named_after_the_tree(self):
        b = pub.photo_block(self.ENTRY, 1, 1, "", "2026-09-04")
        self.assertEqual(b["url"], "https://ancienttrees.app/photos/ams_001-the-wertheimpark-wingnut.jpg")


def json_dump(o):
    import json
    return json.dumps(o)


class TestReaderPin(unittest.TestCase):
    """A reader's accepted fix replaces an approximate pin, never a confirmed one."""

    def tree(self, precision="approximate", lat=64.1474, lon=-21.9418):
        return {"id": "rey_001", "location_precision": precision,
                "location": {"latitude": lat, "longitude": lon}}

    def test_approximate_moves_and_becomes_confirmed(self):
        t = self.tree()
        line = pub.move_pin(t, 64.1474222, -21.9420133, "sid", "2026-09-04T15:45:35Z", "2026-10-05")
        self.assertTrue(line.startswith("PIN "))
        self.assertEqual(t["location"]["latitude"], 64.147422)
        self.assertEqual(t["location_precision"], "confirmed")
        self.assertEqual(t["pin_source"]["sighting_id"], "sid")
        self.assertEqual(t["pin_source"]["moved_m"], 11)

    def test_confirmed_is_never_touched(self):
        t = self.tree("confirmed")
        self.assertIsNone(pub.move_pin(t, 64.1475, -21.9420, "sid", None, "2026-10-05"))
        self.assertEqual(t["location"]["latitude"], 64.1474)
        self.assertNotIn("pin_source", t)

    def test_too_far_is_reported_not_applied(self):
        t = self.tree()
        line = pub.move_pin(t, 64.1600, -21.9418, "sid", None, "2026-10-05")
        self.assertTrue(line.startswith("NOT MOVED"))
        self.assertEqual(t["location_precision"], "approximate")
        self.assertEqual(t["location"]["latitude"], 64.1474)

    def test_our_own_pin_echoed_back_is_not_a_fix(self):
        # Balete Park, 2026-11-16: the sighting carried our pin digit for digit.
        t = self.tree()
        line = pub.move_pin(t, 64.1474, -21.9418, "sid", None, "2026-11-16")
        self.assertTrue(line.startswith("NOT MOVED"))
        self.assertEqual(t["location_precision"], "approximate")
        self.assertNotIn("pin_source", t)

    def test_no_fix_no_change(self):
        t = self.tree()
        self.assertIsNone(pub.move_pin(t, None, None, "sid", None, "2026-10-05"))


class TestOneRoute(unittest.TestCase):
    """A photograph of another tree than the one it was sent for becomes a
    waiting lead, judged as a new tree (Hidde, 2026-11-17: "1 route")."""

    def test_other_tree_becomes_a_waiting_lead_once(self):
        import tempfile
        tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False)
        tmp.write(b'{"leads": []}')
        tmp.close()
        old = pub.LEADS
        pub.LEADS = tmp.name
        try:
            e = {"sighting_id": "s1", "user_id": "p_x", "tree_id": "dub_017", "city": "Dublin",
                 "latitude": 53.37, "longitude": -6.27, "photo_path": "p_x/S1.jpg", "distance_m": 12}
            self.assertTrue(pub.to_lead(e, "a weeping conifer", "2026-11-17"))
            self.assertFalse(pub.to_lead(e, "again", "2026-11-17"))
            leads = pub.load(tmp.name, {})["leads"]
            self.assertEqual(len(leads), 1)
            l = leads[0]
            self.assertEqual((l["status"], l.get("hold"), l["sent_for"]), ("lead", None, "dub_017"))
            self.assertIn("matches no tree we map", l["why"])
            # The photo path's first part is a code, never the account id.
            raw = {"sighting_id": "s2", "tree_id": "dub_017",
                   "photo_path": "12ea7b4f-1542-4216-b4af-909ffb0a4be8/S2.jpg"}
            pub.to_lead(raw, "x", "2026-11-17")
            l2 = [x for x in pub.load(tmp.name, {})["leads"] if x["sighting_id"] == "s2"][0]
            self.assertTrue(l2["photo"].startswith("p_"), l2["photo"])
        finally:
            pub.LEADS = old
            os.unlink(tmp.name)


class TestTrimBlack(unittest.TestCase):
    """A phone screenshot of a photograph loses its black bars; a dark
    photograph stays whole (Hidde, 2026-11-19: the Fortingall yew on /visitors,
    and the night-time Ashbrittle plaque that a looser rule cut)."""

    def test_screenshot_bars_go_and_the_home_indicator_does_not_stop_it(self):
        from PIL import Image, ImageDraw
        im = Image.new("RGB", (740, 1600), (0, 0, 0))
        d = ImageDraw.Draw(im)
        d.rectangle((0, 300, 739, 1240), fill=(90, 140, 70))      # the photograph
        d.rectangle((270, 1560, 470, 1565), fill=(255, 255, 255))  # home indicator
        out = pub.trim_black(im)
        self.assertEqual(out.size[0], 740)
        self.assertTrue(900 < out.size[1] <= 941, out.size)

    def test_a_dark_photograph_is_left_whole(self):
        from PIL import Image
        im = Image.new("RGB", (1600, 1200), (14, 16, 20))         # night, not black
        self.assertEqual(pub.trim_black(im).size, (1600, 1200))


class TestSamePicture(unittest.TestCase):
    """One photograph sent twice is never added twice (Hidde, 2026-11-19,
    "double?", the Finer Holm Oak of Edinburgh Gardens)."""

    def test_a_byte_identical_file_is_found(self):
        import tempfile
        d = tempfile.mkdtemp()
        old, pub.PHOTOS = pub.PHOTOS, d
        try:
            for name, body in [("a.jpg", b"one"), ("b.jpg", b"one"), ("c.jpg", b"two")]:
                open(os.path.join(d, name), "wb").write(body)
            u = lambda n: "https://ancienttrees.app/photos/" + n
            self.assertEqual(pub.same_picture({"url": u("b.jpg")}, [{"url": u("a.jpg")}]), u("a.jpg"))
            self.assertIsNone(pub.same_picture({"url": u("c.jpg")}, [{"url": u("a.jpg")}]))
        finally:
            pub.PHOTOS = old


class TestPhotoDate(unittest.TestCase):
    """Hidde, 2026-11-19: the photo's own month reaches the lead and the
    queue, an upload moment never does."""

    def test_app_row_keeps_its_month(self):
        row = {"taken_at": "2025-07-14T16:02:11+00:00", "note": "A big oak"}
        self.assertEqual(inbox.taken_month(row), 7)

    def test_old_website_row_is_an_upload_moment(self):
        row = {"taken_at": "2026-11-19T10:00:00+00:00",
               "note": "Photograph sent from this tree’s page on the website. The position ..."}
        self.assertIsNone(inbox.photo_taken_at(row))
        self.assertIsNone(inbox.taken_month(row))

    def test_website_row_with_the_files_date(self):
        row = {"taken_at": "2025-04-02T09:00:00+00:00",
               "note": "Photograph sent from this tree’s page on the website. "
                       "Its date is the photograph’s own date."}
        self.assertEqual(inbox.taken_month(row), 4)

    def test_no_date(self):
        self.assertIsNone(inbox.taken_month({"note": "x"}))

    def test_a_tips_send_moment_is_not_its_photos_date(self):
        row = {"taken_at": "2026-11-20T09:00:00+00:00", "from_tip": True, "note": "x"}
        self.assertIsNone(inbox.photo_taken_at(row))
        self.assertIsNone(inbox.taken_month(row))

    def test_a_tips_photo_month(self):
        row = {"taken_at": "2026-11-20T09:00:00+00:00", "from_tip": True, "photo_month": 6}
        self.assertEqual(inbox.taken_month(row), 6)


if __name__ == "__main__":
    unittest.main()
