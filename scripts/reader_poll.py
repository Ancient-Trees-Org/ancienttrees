#!/usr/bin/env python3
"""Did a reader send a tree, share a photograph or report on a tree in the
last few minutes?

The reader judge (reader-judge.yml) polls with this every 15 minutes, so a
reader's tree is judged soon after it arrives without anything set up in
Supabase or a token for Hidde to make (2026-11-17: "do i have to do all this
or can you do parts of it?"). It reads two tiny id lists, never a photograph,
so it costs almost no Supabase egress (the free plan's 5 GB matter, LOG
2026-11-16).

    python3 scripts/reader_poll.py            # exit 0 = something new, 1 = nothing
    python3 scripts/reader_poll.py --minutes 30

The window is a little longer than the poll interval, so a row is never
missed between two polls; a row seen twice only means the second run finds
it already judged and starts no agent.
"""
import datetime
import json
import os
import sys
import urllib.request

SUPA = "https://caimvxiyrtifilimlkqw.supabase.co"


def get(path, key):
    req = urllib.request.Request(SUPA + path, headers={"apikey": key, "Authorization": "Bearer " + key})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read() or b"[]")


def main():
    minutes = 25
    if "--minutes" in sys.argv:
        minutes = int(sys.argv[sys.argv.index("--minutes") + 1])
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    if not key:
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            import inbox
            key = inbox.load_key()
        except Exception:  # noqa: BLE001
            key = None
    if not key:
        print("reader_poll: no SUPABASE_SERVICE_KEY, nothing read")
        return 1
    since = (datetime.datetime.now(datetime.timezone.utc)
             - datetime.timedelta(minutes=minutes)).strftime("%Y-%m-%dT%H:%M:%S")
    n = 0
    try:
        # sightings has no created_at, and updated_at moves whenever our own
        # scripts touch a row, so a photograph counts as new only when its id
        # is not in data/sightings-processed.json yet.
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        try:
            done = json.load(open(os.path.join(root, "data", "sightings-processed.json"))).get("done", {})
        except Exception:  # noqa: BLE001
            done = {}
        rows = get("/rest/v1/sightings?select=id&shared=eq.true&photo=not.is.null&updated_at=gte." + since, key)
        n += len([r for r in rows if r["id"] not in done])
        n += len(get("/rest/v1/submissions?select=id&kind=in.(tree,city,ambassador)&created_at=gte." + since, key))
        # General feedback too (Hidde, 2026-11-17), but never a one-tap vote:
        # "worth it" arrives as feedback dozens of times a day and needs
        # nothing ("worth it hoeven we in principe niks mee").
        fb = get("/rest/v1/submissions?select=why&kind=eq.feedback&created_at=gte." + since, key)
        n += len([r for r in fb if not (r.get("why") or "").strip().lower().startswith(
            ("worth it", "not worth it", "vote undone", "report"))])
        # Reports on our trees (dead, wrong place, could not tell which, a
        # moved pin) wake the judge too, by when they were sent or when their
        # follow-up words came (Hidde, 2026-11-17: like the readers' trees).
        n += len(get("/rest/v1/tree_reports?select=id&outcome=is.null"
                     "&or=(created_at.gte.%s,detail_at.gte.%s)" % (since, since), key))
    except Exception as e:  # noqa: BLE001
        # Any doubt starts the run (claude_gate.py's rule): a quiet failure
        # here would leave readers waiting for the knock again.
        print("reader_poll: could not read (%s), starting anyway" % e.__class__.__name__)
        return 0
    print("reader_poll: %d new in the last %d minutes" % (n, minutes))
    return 0 if n else 1


if __name__ == "__main__":
    sys.exit(main())
