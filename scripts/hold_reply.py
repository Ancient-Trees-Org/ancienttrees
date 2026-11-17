#!/usr/bin/env python3
"""The standard, friendly answer to a reader whose tree we held for a reason
they can fix themselves.

Hidde, 2026-11-17, on the Chêne de la Vierge (submission 1066), held as
`not_theirs` because the picture looked like Street View: "moeten we zo
iemand niet ook een auto mail sturen met de foto lijkt niet van jou? kunnen we
niet live zetten, doe zelf een foto maken? maar dan aardig". So a hold the
reader can lift gets a mail that says what would put the tree on the map,
written once here, never by a run.

    python3 scripts/hold_reply.py <submission id> not_theirs ["tree name"] [--dry]

It writes the text as the row's reply_text with outcome `open_question`;
contributor_reply.py mails it at the knock after mailcheck, like any answer.
"""
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SUPA = "https://caimvxiyrtifilimlkqw.supabase.co"

REPLIES = {
    "not_theirs": (
        "Thank you for telling us about {name}. We would love to have it on the map, "
        "but the photograph looks like it was taken by someone else, and we can only "
        "show pictures people took themselves.\n\n"
        "If you are ever near it, a photograph of your own from the spot is all it "
        "needs to go on the map.\n\n"
        "Ancient Trees\nhttps://ancienttrees.app\n"),
}


def text(reason, name):
    return REPLIES[reason].format(name=name or "your tree")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if len(args) < 2 or args[1] not in REPLIES:
        print(__doc__)
        return 1
    sid, reason = args[0], args[1]
    import inbox
    key = inbox.load_key()
    row = inbox.get("/rest/v1/submissions?select=id,tree,why,reply_text,replied_at&id=eq.%d" % int(sid), key)[0]
    name = args[2] if len(args) > 2 else None
    body = text(reason, name)
    if "--dry" in argv:
        print(body)
        return 0
    if row.get("replied_at"):
        print("hold_reply: %s already answered, nothing written" % sid)
        return 0
    req = urllib.request.Request(SUPA + "/rest/v1/submissions?id=eq.%d" % int(sid), method="PATCH",
                                 data=json.dumps({"reply_text": body, "outcome": "open_question"}).encode(),
                                 headers={"apikey": key, "Authorization": "Bearer " + key,
                                          "Content-Type": "application/json", "Prefer": "return=minimal"})
    urllib.request.urlopen(req, timeout=30).read()
    print("hold_reply: %s answered with the standard %s mail (goes at the next knock)" % (sid, reason))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
