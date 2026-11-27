"""The photo_elsewhere question is the text Hidde approved for the Genoa cedar
(2026-11-27, "Send both", then "remember this response for this situation")."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hold_reply  # noqa: E402

SENT = (
    "Hi,\n\nThanks for your photo of the Cedar of Lebanon of Acquasanta in Genoa!\n\n"
    "On our map that cedar stands in the square in front of the Acquasanta church, and your "
    "photo shows one on a wooded slope. Is it the same tree, or another cedar nearby? Either "
    "way we'd love to have it.\n\nCould you tell us where you took it, by replying to this mail?"
    "\n\nThanks again,\nAncient Trees\nhttps://ancienttrees.app\n")


def test_matches_the_approved_mail():
    got = hold_reply.text("photo_elsewhere", "the Cedar of Lebanon of Acquasanta in Genoa",
                          "in the square in front of the Acquasanta church", "one on a wooded slope", "cedar")
    assert got == SENT, got


def test_needs_where_and_seen():
    try:
        hold_reply.text("photo_elsewhere", "x")
    except SystemExit:
        return
    raise AssertionError("photo_elsewhere without --where/--seen must refuse")


if __name__ == "__main__":
    test_matches_the_approved_mail()
    test_needs_where_and_seen()
    print("ok")
