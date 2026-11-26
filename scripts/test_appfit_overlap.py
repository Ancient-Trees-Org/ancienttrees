#!/usr/bin/env python3
"""appfit's OVERLAP rule, on a hand-made dump (escaped bug of 2026-11-25: My
trees' follower count ran over the person's name at a large text size).

    python3 scripts/test_appfit_overlap.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import appfit  # noqa: E402


def dump(*rows):
    lines = ["<<<SWEEP mytrees 375x667",
             "Window, 0x1, {{0.0, 0.0}, {375.0, 667.0}}"]
    lines += ["  " + r for r in rows]
    lines.append("SWEEP>>>")
    return "\n".join(lines)


def findings(*rows, large=True):
    screen = appfit.parse(dump(*rows))[0]
    return [f for f in appfit.check(screen, large) if f[0] == "OVERLAP"]


def test_the_follower_count_over_the_name_is_found():
    got = findings(
        "StaticText, 0x2, {{20.0, 120.0}, {260.0, 44.0}}, label: 'Miguel P.'",
        "StaticText, 0x3, {{200.0, 130.0}, {150.0, 30.0}}, label: '12 followers'")
    assert len(got) == 1, got
    assert "12 followers" in got[0][2]


def test_the_count_on_its_own_line_is_fine():
    assert not findings(
        "StaticText, 0x2, {{20.0, 120.0}, {260.0, 44.0}}, label: 'Miguel P.'",
        "StaticText, 0x3, {{20.0, 168.0}, {150.0, 30.0}}, label: '12 followers'")


def test_a_brushing_descender_is_not_an_overlap():
    assert not findings(
        "StaticText, 0x2, {{20.0, 120.0}, {260.0, 44.0}}, label: 'Miguel P.'",
        "StaticText, 0x3, {{20.0, 162.0}, {150.0, 30.0}}, label: '12 followers'")


def test_the_same_words_twice_on_one_frame_are_one_text():
    assert not findings(
        "StaticText, 0x2, {{20.0, 120.0}, {260.0, 44.0}}, label: 'Miguel P.'",
        "StaticText, 0x3, {{20.0, 120.0}, {260.0, 44.0}}, label: 'Miguel P.'")


def test_a_list_under_a_fixed_bar_is_not_an_overlap():
    # The first large-text sweep's 40 false findings: a list scrolling under
    # the floating tab bar or a pinned button.
    assert not findings(
        "ScrollView, 0x2, {{0.0, 0.0}, {375.0, 667.0}}",
        "  StaticText, 0x3, {{20.0, 600.0}, {260.0, 44.0}}, label: 'The Van Loon Copper Beech'",
        "Button, 0x4, {{20.0, 610.0}, {200.0, 48.0}}, identifier: 'tree-take-me-there'",
        "  StaticText, 0x5, {{20.0, 610.0}, {200.0, 48.0}}, label: 'Take me there'")


def test_two_lines_in_one_list_that_collide_are_found():
    got = findings(
        "ScrollView, 0x2, {{0.0, 0.0}, {375.0, 667.0}}",
        "  StaticText, 0x3, {{20.0, 120.0}, {260.0, 44.0}}, label: 'Miguel P.'",
        "  StaticText, 0x4, {{200.0, 130.0}, {150.0, 30.0}}, label: '12 followers'")
    assert len(got) == 1, got


def test_a_page_under_a_full_screen_cover_is_not_an_overlap():
    assert not findings(
        "Other, 0x2, {{0.0, 0.0}, {375.0, 667.0}}",
        "  StaticText, 0x3, {{20.0, 609.0}, {211.0, 48.0}}, label: 'Take me there'",
        "Other, 0x4, {{0.0, 0.0}, {375.0, 667.0}}",
        "  StaticText, 0x5, {{32.0, 495.0}, {311.0, 140.0}}, label: 'You need an account'")


def test_overlap_is_judged_only_at_large_text():
    assert not findings(
        "StaticText, 0x2, {{20.0, 120.0}, {260.0, 44.0}}, label: 'Miguel P.'",
        "StaticText, 0x3, {{200.0, 130.0}, {150.0, 30.0}}, label: '12 followers'",
        large=False)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
