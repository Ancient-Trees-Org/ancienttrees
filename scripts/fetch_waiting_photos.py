#!/usr/bin/env python3
"""Put the photograph of every reader's tree still waiting for a verdict on
THIS machine, so the run that judges it can look at it.

Why (2026-11-17): sightings_inbox.py downloads a photograph once, when it
first files the tree as a lead, into out/sightings/ on whatever runner did
the intake. The next knock starts on a clean runner with an empty out/, so a
lead not judged in that same run could never be looked at again by a night
run ("their files are not on this runner"), and the rule says never judge a
stranger's photograph blind. 29 reader trees waited a weekend that way.

Waiting = a lead in data/leads/_sightings.json with status "lead", no `hold`
reason, and not ours. Files land at out/sightings/<sighting id>.jpg, the
inbox's own naming. Already on disk = skipped, so it costs nothing twice.

    python3 scripts/fetch_waiting_photos.py          # fetch, print the list
    python3 scripts/fetch_waiting_photos.py --count  # how many wait, no fetch
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
os.chdir(ROOT)
sys.path.insert(0, HERE)

LEADS = "data/leads/_sightings.json"
OUT = os.path.join("out", "sightings")


def waiting():
    with open(LEADS, encoding="utf-8") as fh:
        leads = json.load(fh).get("leads", [])
    return [l for l in leads
            if l.get("status") == "lead" and not l.get("hold") and not l.get("mine")
            and l.get("photo")]


def main():
    rows = waiting()
    if "--count" in sys.argv:
        print(len(rows))
        return 0
    if not rows:
        print("fetch_waiting_photos: no reader tree waits for a verdict")
        return 0
    if not os.environ.get("SUPABASE_SERVICE_KEY"):
        try:
            import inbox
            key = inbox.load_key()
            if key:
                os.environ["SUPABASE_SERVICE_KEY"] = key
        except Exception:  # noqa: BLE001
            pass
    if not os.environ.get("SUPABASE_SERVICE_KEY"):
        print("fetch_waiting_photos: SUPABASE_SERVICE_KEY absent, %d photograph(s) not fetched" % len(rows))
        return 0
    import sightings_inbox as si
    si.KEY = os.environ["SUPABASE_SERVICE_KEY"]
    os.makedirs(OUT, exist_ok=True)
    got = 0
    for l in rows:
        sid = (l.get("sighting_id") or "").lower()
        dest = os.path.join(OUT, sid + ".jpg")
        ok = si.fetch_photo(l["photo"], dest)
        got += 1 if ok else 0
        print("%s  %s  %s" % ("ok  " if ok else "MISS", dest, l.get("name")))
    print("fetch_waiting_photos: %d of %d waiting photograph(s) on disk" % (got, len(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
