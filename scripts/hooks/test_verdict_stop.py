"""python3 scripts/hooks/test_verdict_stop.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verdict_stop as v

ROW = {"id": "lead:tip-1", "tree": "A plane", "city": "X", "verdict": "hold", "shown": ["2026-11-26"]}
MSGS = [("u1", "dd"), ("u2", "deze is doorgestuurd")]
SHOWN = "ran python3 scripts/inspect_readers.py"

# He wrote something new after seeing the list: the turn is held, with the id.
r = v.decide({}, SHOWN, MSGS, [ROW], "")
assert r and "lead:tip-1" in r and "Never file silence" in r, r
# Same message already handled: no second hold.
assert v.decide({}, SHOWN, MSGS, [ROW], "u2") is None
# Already held once this stop: never loops.
assert v.decide({"stop_hook_active": True}, SHOWN, MSGS, [ROW], "") is None
# Nothing open, or a session that never showed him the trees: quiet.
assert v.decide({}, SHOWN, MSGS, [], "") is None
assert v.decide({}, "other work", MSGS, [ROW], "") is None
print("verdict_stop: 5 cases ok")
