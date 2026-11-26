#!/usr/bin/env python3
"""What reaches the server feed (scripts/feed_publish.py, 2026-11-26): only
what the judge looked at, never our own accounts, a reader's tree once."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import feed_publish as fp  # noqa: E402


def photo(sid, who="p_reader", **kw):
    return dict(url=f"https://ancienttrees.app/photos/{sid}.jpg", source="contributor",
                sighting_id=sid, contributor_user_id=who, **kw)


def city(*trees):
    return [("somewhere", {"city": "Somewhere", "trees": list(trees)})]


def tree(tid, **kw):
    t = {"id": tid, "name": f"The Oak {tid}", "location": {"latitude": 1.0, "longitude": 2.0}}
    t.update(kw)
    return t


def test_a_readers_tree_is_one_tree_row():
    rows = fp.collect(city(tree("a_001", found_by_reader={"sighting_id": "s1", "date": "2026-11-25"},
                                photo=photo("s1"))), mine=set(), ok={})
    assert list(rows) == ["s1"] and rows["s1"]["kind"] == "tree"
    assert rows["s1"]["place"] == "Somewhere" and rows["s1"]["tree_name"] == "The Oak a_001"


def test_a_photo_on_our_tree_is_a_photo_row():
    rows = fp.collect(city(tree("a_002", photos=[photo("s2")])), mine=set(), ok={})
    assert rows["s2"]["kind"] == "photo"


def test_an_unjudged_strip_photo_waits_for_the_judge():
    t = tree("a_003", photos=[photo("s3", live_first_on="2026-11-26")])
    assert fp.collect(city(t), mine=set(), ok={}) == {}
    assert "s3" in fp.collect(city(t), mine=set(), ok={"s3": "2026-11-26"})


def test_never_our_own_accounts():
    t = tree("a_004", photos=[photo("s4", who="p_ours")])
    assert fp.collect(city(t), mine={"p_ours"}, ok={}) == {}


def test_a_commons_photo_is_not_a_readers():
    t = tree("a_005", photo={"url": "https://x/y.jpg", "source": "commons"})
    assert fp.collect(city(t), mine=set(), ok={}) == {}


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
