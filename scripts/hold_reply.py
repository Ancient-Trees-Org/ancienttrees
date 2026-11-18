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
        # Hidde, 2026-11-18: "we think this is a photo made by somebody else and
        # can't put it live without their permission, a photo of your own".
        "Thank you for telling us about {name}. We think this photo was taken by "
        "someone else, and we can't put it live without their permission.\n\n"
        "If you are ever near it, a photo of your own puts it on the map.\n\n"
        "Ancient Trees\nhttps://ancienttrees.app\n"),
    # Hidde, 2026-11-18: every hold the reader can fix gets a friendly standard
    # mail ("for all the rightly held ... an automated system"); wording from
    # the bad-frame reply he approved that day (submission 858) and his line on
    # private property. Holds a reader cannot change (not_special, dead,
    # wrong_subject, inappropriate, doubt_info, doubt_photo) get no mail.
    "bad_frame": (
        # Hidde, 2026-11-18, on the flower close-up: never comment on what the
        # photo shows; say we know little about the tree from it and ask about it.
        "Thanks for your photo of {name}! From the photo alone we can't tell much "
        "about the tree yet, and we'd like to know a bit more before we put it on "
        "the map for everyone.\n\n"
        "Could you tell us more about it, by replying to this mail? What kind of tree "
        "it is, roughly how thick the trunk is, how old it might be, anything you know. "
        "And if you're ever passing by again, a photo of the whole tree helps too, with "
        "the camera button in the app or here:\n"
        "https://ancienttrees.app/contribute\n\n"
        "Thanks again,\nAncient Trees\n"),
    "no_location": (
        "Thanks for {name}! We couldn't work out exactly where it stands.\n\n"
        "Could you tell us, by replying to this mail? Then we can put it on the map.\n\n"
        "Thanks again,\nAncient Trees\n"),
    "not_public": (
        "Thanks for {name}! It looks like it stands on private property.\n\n"
        "Can it be seen from a street or path? Then we'll put it on the map with the "
        "pin at that spot.\n\n"
        "Thanks again,\nAncient Trees\n"),
    "wrong_tree": (
        "Thanks for your photo of {name}! We couldn't tell which tree it shows.\n\n"
        "Could you tell us which one it is, or where you stood when you took it?\n\n"
        "Thanks again,\nAncient Trees\n"),
}
REPLIES["doubt_location"] = REPLIES["no_location"]


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
