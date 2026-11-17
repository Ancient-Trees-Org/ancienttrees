#!/usr/bin/env python3
""""walks" as a verb is fine in a mail; walks as a feature still fails.

Hidde, 2026-11-17: the Blaise reply ("so the next person walks straight to
them") was held as an unshipped feature: "we mogen best walks zeggen wtf".
Exit 1 when either half breaks.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mailcheck

verb = "We moved the pins, so the next person walks straight to them."
feature = "Try our guided walks past the oldest oaks."
bad = []
if mailcheck.check_no_unshipped_feature("verb.md", verb):
    bad.append("the verb 'walks' is refused")
if not mailcheck.check_no_unshipped_feature("feature.md", feature):
    bad.append("'guided walks' as a feature passes")
for b in bad:
    print("FAIL", b)
if not bad:
    print("ok  walks: verb passes, feature refused")
sys.exit(1 if bad else 0)
