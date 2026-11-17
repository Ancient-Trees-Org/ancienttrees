#!/usr/bin/env python3
"""A tree sent without a photograph gets a verdict stub (escaped bug 2026-11-17).

Submission 936 (the Ochi chestnut) and web submissions 937 and 939 sat
unjudged because judgement.py only stubbed rows that carried a photograph.
This feeds scan_tips() a fake database and checks that a words-only tip is
stubbed, that the app's uuid-named row beside a photographed tree is not, and
that a second scan adds nothing.

    python3 scripts/test_judgement_tips.py
"""
import os
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ["SUPABASE_SERVICE_KEY"] = "test"

fake_inbox = types.ModuleType("inbox")
fake_inbox.get = lambda path, key: [
    {"id": 936, "user_id": "u1", "kind": "tree", "tree": "Ochi chestnut", "city": "Karystos",
     "why": "huge chestnut", "photo": None, "girth_cm": None, "outcome": None, "created_at": "2026-11-16T10:00:00"},
    {"id": 1029, "user_id": "u2", "kind": "tree", "tree": "60878254-21F7-4E0D-8D06-91700DB3E06A", "city": "",
     "why": "", "photo": None, "girth_cm": None, "outcome": None, "created_at": "2026-11-16T11:00:00"},
]
fake_inbox.load_key = lambda: "test"
fake_ours = types.ModuleType("ours")
fake_ours.is_ours = lambda uid: False
sys.modules["inbox"] = fake_inbox
sys.modules["ours"] = fake_ours

import judgement  # noqa: E402

doc = {"judgements": []}
added = judgement.scan_tips(doc, set(), "2026-11-17")
ids = [j["id"] for j in doc["judgements"]]
assert added == 1, (added, ids)
assert ids == ["tip:936"], ids
assert doc["judgements"][0]["verdict"] is None
again = judgement.scan_tips(doc, set(ids), "2026-11-17")
assert again == 0, again
print("ok: a tip without a photograph is stubbed once; the app's photo row is not")
