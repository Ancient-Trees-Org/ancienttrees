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
    python3 scripts/hold_reply.py <sighting id or lead:<id>> not_public ["tree name"]
    python3 scripts/hold_reply.py <id> doubt_photo_live ["tree name"] [--again]

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
    # wrong_subject, inappropriate, doubt_info) get no mail; doubt_photo is a
    # question they can answer (below, since 2026-11-26).
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
    # A SCREENSHOT IS ASKED ABOUT (Hidde, 2026-11-26: "screenshot zijn wel
    # gevaarlijk toch"): no camera data, so we cannot tell who took it, and a
    # photo goes up only with its maker's yes. Asked kindly, never accused.
    "doubt_photo": (
        "Thanks for your photo of {name}! It looks like a screenshot, so we can't tell "
        "who took it, and we only put a photo on the map with the photographer's "
        "permission.\n\n"
        "Did you take it yourself? Just reply to this mail and let us know. And if you're "
        "ever passing by, a photo of your own with the camera button in the app works too.\n\n"
        "Thanks again,\nAncient Trees\n"),
    # The tree went live on other sources and only the photo waits for the answer.
    "doubt_photo_live": (
        "Thanks for {name}! It's on the map now. We left your photo off for the moment: "
        "it looks like a screenshot, so we can't tell who took it, and we only put a photo "
        "on the map with the photographer's permission.\n\n"
        "Did you take it yourself? Just reply to this mail and let us know, and we'll add it.\n\n"
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
    if not sid.isdigit():
        # AN APP TREE IS ANSWERED THE SAME WAY (Hidde, 2026-11-23: "dit moet jij
        # automatisch doen", after two app trees held `not_public` sat without
        # the question because a run believed only website rows could be
        # mailed). A tree sent with "add" in the app writes a submissions row
        # with page app:collect and the sighting's id in `tree`; that row is the
        # reply channel. A sighting with no such row was only kept in the
        # reader's own collection, never sent to us: no mail.
        sight = sid.split(":", 1)[-1]
        rows = inbox.get("/rest/v1/submissions?select=id&tree=ilike.%s&order=id.desc&limit=1" % sight, key)
        if not rows:
            print("hold_reply: sighting %s was never sent to us as a tree (no submissions row), no mail" % sight)
            return 0
        sid = str(rows[0]["id"])
    row = inbox.get("/rest/v1/submissions?select=id,tree,why,reply_text,replied_at&id=eq.%d" % int(sid), key)[0]
    name = args[2] if len(args) > 2 else None
    body = text(reason, name)
    if "--dry" in argv:
        print(body)
        return 0
    patch = {"reply_text": body, "outcome": "open_question"}
    if row.get("replied_at"):
        # --again: a later question on a row we already answered (2026-11-26,
        # the Tsagarada plane: told "on the map", then asked about its photo).
        # The earlier text was a standard template; the new one replaces it
        # and goes at the next knock.
        if "--again" not in argv:
            print("hold_reply: %s already answered, nothing written (--again asks a new question)" % sid)
            return 0
        patch["replied_at"] = None
    req = urllib.request.Request(SUPA + "/rest/v1/submissions?id=eq.%d" % int(sid), method="PATCH",
                                 data=json.dumps(patch).encode(),
                                 headers={"apikey": key, "Authorization": "Bearer " + key,
                                          "Content-Type": "application/json", "Prefer": "return=minimal"})
    urllib.request.urlopen(req, timeout=30).read()
    print("hold_reply: %s answered with the standard %s mail (goes at the next knock)" % (sid, reason))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
