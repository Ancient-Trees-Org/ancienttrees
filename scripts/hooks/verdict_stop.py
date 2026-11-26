"""Stop hook: Hidde's word on a reader's tree is filed before the turn ends.

Hidde, 2026-11-26, after the Tsagarada plane came back on his list for the
third time: "maar je moet het onthouden als ik ooit reageer", and "je kunt er
niet vanuit gaan als ik nooit op een boom heb gereageerd dat het akkoord is".
The page remembers what it showed him (`shown` in data/judgements.json), but
only a session can hear his answer, and sessions forgot to file it. So in a
session that showed him the trees (its transcript ran inspect_readers.py or
show_digest.py), every time he has written something new and a tree shown to
him in the last three days still has no answer, the turn is held once with
the list: file what he said with judgement.py --feedback, or carry on when
he said nothing about them. Silence is never filed as agreement.

Once per message of his (the marker in out/tmp/), never twice in a row
(`stop_hook_active`), and silent when anything goes wrong."""
import datetime
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DAYS = 3


def human_messages(path):
    """(uuid, text) of every message he typed, oldest first."""
    out = []
    for line in open(path, encoding="utf-8"):
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("type") != "user" or e.get("isMeta"):
            continue
        c = (e.get("message") or {}).get("content")
        if isinstance(c, list):
            if any(isinstance(b, dict) and b.get("type") == "tool_result" for b in c):
                continue
            c = " ".join(b.get("text", "") for b in c if isinstance(b, dict))
        if isinstance(c, str) and c.strip():
            out.append((e.get("uuid") or str(len(out)), c))
    return out


def pending(today=None):
    today = today or datetime.date.today()
    since = (today - datetime.timedelta(days=DAYS)).isoformat()
    rows = json.load(open(os.path.join(ROOT, "data/judgements.json"), encoding="utf-8"))
    out = []
    for j in rows.get("judgements", []):
        if j.get("hidde"):
            continue
        if any(str(d) >= since for d in (j.get("shown") or [])):
            out.append(j)
    return out


def decide(event, transcript_text, msgs, rows, marker):
    """The reason to hold the turn, or None."""
    if event.get("stop_hook_active") or not rows or not msgs:
        return None
    if "inspect_readers.py" not in transcript_text and "show_digest.py" not in transcript_text:
        return None
    last = msgs[-1][0]
    if marker == last:
        return None
    lines = ["%s  %s (%s), our verdict %s" % (j.get("id"), j.get("tree"), j.get("city") or "?", j.get("verdict"))
             for j in rows]
    return ("Trees shown to Hidde in the last %d days with no answer filed:\n%s\n\n"
            "If anything he wrote in this conversation is his word on one of them, file it now, "
            "his own words: python3 scripts/judgement.py --feedback <id> \"<his words>\" agreed "
            "(leave off agreed when he overrules us). Never file silence as agreement. "
            "If he said nothing about them, just finish." % (DAYS, "\n".join(lines)))


def main():
    try:
        event = json.load(sys.stdin)
        path = event.get("transcript_path") or ""
        if not os.path.exists(path):
            return
        text = open(path, encoding="utf-8").read()
        msgs = human_messages(path)
        rows = pending()
        mpath = os.path.join(ROOT, "out/tmp", "verdict-stop-%s.txt" % (event.get("session_id") or "x"))
        marker = open(mpath).read().strip() if os.path.exists(mpath) else ""
        reason = decide(event, text, msgs, rows, marker)
        if not reason:
            return
        os.makedirs(os.path.dirname(mpath), exist_ok=True)
        open(mpath, "w").write(msgs[-1][0])
        print(json.dumps({"decision": "block", "reason": reason}))
    except Exception:
        return


if __name__ == "__main__":
    main()
