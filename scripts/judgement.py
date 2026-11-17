#!/usr/bin/env python3
"""Every tree a reader sends gets a written verdict, and Hidde gets to disagree.

Hidde, 2026-09-23, right after settling the rule for which trees earn a page:
"kun je dit opslaan, en elke keer als er een boom wordt ingestuurd mij vertellen
wat je oordeel is en dat ik het kan inzien, zodat ik voorlopig feedback kan
geven zodat we het aanscherpen?"

The point is the LAST clause. The rule in DECISIONS.md 2026-09-23 is a first
draft of somebody's taste written down, and the only way it gets better is by
being applied out loud, one tree at a time, where he can say "no, that one".
A verdict that lives in a session's chat cannot be disagreed with a week later.
So each one is written down with the reasoning beside it, and his answer is
written down next to that.

Three states per entry:
  verdict   ours: publish | lead | hold, with the reason and the numbers
  hidde     his answer, when he gives one, in his own words
  agreed    true when they match, false when they do not

`--learn` prints only the ones where they did not match, which is the whole
value of the file: it is the list of places where the written rule and his
taste come apart, and every one of them is either a bug in the rule or a tree
we got wrong.

Usage:
  python3 scripts/judgement.py --scan                     # stub every unjudged submission
  python3 scripts/judgement.py --verdict <id> lead "..."  # the run's call
  python3 scripts/judgement.py --open                     # what he has not seen
  python3 scripts/judgement.py --feedback <id> "..."      # his answer
  python3 scripts/judgement.py --learn                    # where we disagreed
  python3 scripts/judgement.py --report                   # table for the digest
"""
import json
import os
import re
import sys
from datetime import date

FILE = "data/judgements.json"
QUEUE = "data/sighting-queue.json"
LEADS = "data/leads/_sightings.json"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def coded_photo(path):
    """A storage path whose first part is a reader's account id gets their
    code instead (people.ref). A lead written by hand on 2026-10-20 carried the
    raw id, this copied it on, and qa refused every deploy until both were
    fixed. Raises without the key rather than write the id (people.ref)."""
    if not path or "/" not in path:
        return path
    head, rest = path.split("/", 1)
    if len(head) == 36 and head.count("-") == 4:
        import people
        return people.ref(head) + "/" + rest
    return path


def load():
    if not os.path.exists(FILE):
        return {"_note": "One verdict per reader submission. See DECISIONS.md 2026-09-23.",
                "judgements": []}
    return json.load(open(FILE))


def save(doc):
    doc["judgements"].sort(key=lambda j: j.get("seen") or "", reverse=True)
    json.dump(doc, open(FILE, "w"), ensure_ascii=False, indent=1)


def city_slots(slug):
    """How much room the place has left, which is half of the rule."""
    try:
        q = json.load(open("data/city-queue.json"))
    except (OSError, ValueError):
        return None
    rows = q if isinstance(q, list) else q.get("cities", [])
    for r in rows:
        if isinstance(r, dict) and r.get("slug") == slug:
            return {"city": r.get("city"), "target": r.get("target"),
                    "live": r.get("trees"), "slots": (r.get("target") or 0) - (r.get("trees") or 0)}
    return None


def measure(species, girth_cm=None, years=None, age_basis=None):
    """Big or old for its species, the better of the two. An age we derived
    ourselves from a girth is not new evidence, so only age_basis 'source'
    counts on the age axis (DECISIONS.md 2026-09-23)."""
    try:
        from species_size import remarkable
    except ImportError:
        return None
    if age_basis != "source":
        years = None
    if not species:
        return None
    score, which, note = remarkable(species, girth_cm, years)
    if score is None:
        return {"score": None, "note": note}
    return {"score": round(score, 3), "via": which, "note": note}


TIPS_SINCE = "2026-11-10"  # the first tip without a photograph left unjudged was 11-16


def scan_tips(doc, known, today):
    """Stub every tree or place sent without a photograph: `tip:<submission id>`."""
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    if not key:
        try:
            import inbox
            key = inbox.load_key()
        except Exception:  # noqa: BLE001
            key = None
    if not key:
        print("tips without a photograph: no SUPABASE_SERVICE_KEY, not read")
        return 0
    import inbox
    import ours
    try:
        rows = inbox.get("/rest/v1/submissions?select=id,user_id,kind,tree,city,why,photo,girth_cm,outcome,created_at"
                         "&kind=in.(tree,city)&photo=is.null&outcome=is.null&created_at=gte.%s" % TIPS_SINCE, key) or []
    except Exception as e:  # noqa: BLE001
        print("tips without a photograph: database unreadable (%s)" % str(e)[:80])
        return 0
    uuid_re = r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}"
    # A SIGHTING THAT IS GONE (2026-11-17): eight app trees of 11-15 and 11-16
    # sat with no verdict because their row is named by a sighting that no
    # longer exists (the sender deleted it, or the app sent the tree again
    # under a new id). The photo route never sees them, so they are tips now.
    named = [(r.get("tree") or "").strip().lower() for r in rows
             if re.fullmatch(uuid_re, (r.get("tree") or "").strip())]
    alive = set()
    if named:
        try:
            got = inbox.get("/rest/v1/sightings?select=id&id=in.(%s)" % ",".join(named), key) or []
            alive = {g["id"].lower() for g in got}
        except Exception:  # noqa: BLE001
            alive = set(named)          # unsure: leave them to the photo route
    added = 0
    for r in rows:
        if ours.is_ours(r.get("user_id")):
            continue
        # The app writes a submissions row beside every tree it sends with a
        # photograph, named by the sighting's uuid: that tree is judged on the
        # photo route (sight:/lead:), so it is not a tip without a photograph,
        # unless that sighting no longer exists (above).
        if re.fullmatch(uuid_re, (r.get("tree") or "").strip()) and (r.get("tree") or "").strip().lower() in alive:
            continue
        jid = "tip:%s" % r["id"]
        if jid in known or ("lead:tip-%s" % r["id"]) in known:
            continue
        doc["judgements"].append({
            "id": jid, "seen": (r.get("created_at") or today)[:10], "kind": "a tip without a photograph",
            "tree": r.get("tree"), "city": r.get("city"), "species": None, "photo": None,
            "reader_note": "", "reader_girth_cm": r.get("girth_cm"),
            "verdict": None, "reason": None, "hidde": None, "agreed": None,
        })
        added += 1
    return added


def open_count():
    """Stubs with no verdict yet: the reader judge's gate reads this."""
    return sum(1 for j in load()["judgements"] if not j.get("verdict"))


def scan():
    doc = load()
    known = {j["id"] for j in doc["judgements"]}
    today = date.today().isoformat()
    added = 0

    if os.path.exists(QUEUE):
        for e in json.load(open(QUEUE)).get("queue", []):
            if e.get("mine"):
                continue                      # our own photographs are not contributions
            jid = "sight:" + str(e.get("sighting_id"))
            if jid in known:
                continue
            doc["judgements"].append({
                "id": jid, "seen": today, "kind": "photo of a tree we map",
                "tree": e.get("tree_name"), "city": e.get("city"),
                "species": e.get("tree_species"), "photo": f"out/sightings/{e.get('sighting_id')}.jpg",
                "reader_note": e.get("note") or "", "reader_girth_cm": e.get("girth_cm"),
                "match": e.get("match"), "distance_m": e.get("distance_m"),
                "current_photo": e.get("current_photo"),
                "measure": measure(e.get("tree_species"), e.get("girth_cm")),
                "verdict": None, "reason": None, "hidde": None, "agreed": None,
            })
            added += 1

    if os.path.exists(LEADS):
        d = json.load(open(LEADS))
        for e in (d.get("leads") if isinstance(d, dict) else d) or []:
            jid = "lead:" + str(e.get("id") or e.get("sighting_id") or e.get("name"))
            if jid in known:
                continue
            doc["judgements"].append({
                "id": jid, "seen": e.get("seen") or today, "kind": "a tree we do not map",
                "tree": e.get("name"), "city": e.get("city") or e.get("near"),
                "species": e.get("species"), "photo": coded_photo(e.get("photo")),
                "reader_note": e.get("note") or "", "reader_girth_cm": e.get("girth_cm"),
                "coords": [e.get("lat"), e.get("lng")], "register": e.get("register"),
                "measure": measure(e.get("species"), e.get("girth_cm")),
                "verdict": None, "reason": None, "hidde": None, "agreed": None,
            })
            added += 1

    # TIPS WITHOUT A PHOTOGRAPH (2026-11-17, escaped bug: submission 936, the
    # Ochi chestnut, and web submissions 937 and 939 sat unjudged). The queue
    # and the leads only ever hold rows that carry a photograph, so a tree sent
    # as words alone, from the app or the website's form, never got a stub and
    # nothing judged it. They are read from the database here; without a key
    # (a Mac without the env file) this part is skipped and says so.
    added += scan_tips(doc, known, today)

    save(doc)
    print(f"{added} new submission(s) to judge, {len(doc['judgements'])} on file")
    if added:
        print("Next: look at the photograph, then --verdict <id> publish|lead|hold \"why\"")
    return added


def show(j):
    slots = city_slots(j.get("city_slug") or "") or {}
    print(f"\n{j['id']}   seen {j['seen']}")
    print(f"  {j['kind']}: {j.get('tree') or '(unnamed)'}  in {j.get('city') or '?'}")
    if j.get("species"):
        print(f"  species: {j['species']}")
    m = j.get("measure") or {}
    if m.get("score") is not None:
        print(f"  size:    {m['score']:.0%} via {m.get('via')}  ({m.get('note')})")
    elif m.get("note"):
        print(f"  size:    {m['note']}")
    if j.get("reader_note"):
        print(f"  reader:  {j['reader_note'][:200]}")
    if j.get("photo"):
        print(f"  photo:   {j['photo']}")
    if slots:
        print(f"  city:    {slots['live']} live of target {slots['target']}, {slots['slots']} slots")
    print(f"  OURS:    {j.get('verdict') or 'not judged yet'}"
          + (f"  {j['reason']}" if j.get("reason") else ""))
    if j.get("hidde"):
        print(f"  HIDDE:   {j['hidde']}   {'agreed' if j.get('agreed') else 'DISAGREED'}")


def main():
    a = sys.argv[1:]
    doc = load()
    js = {j["id"]: j for j in doc["judgements"]}
    if not a or a[0] == "--scan":
        scan()
    elif a[0] == "--count":
        print(open_count())
    elif a[0] == "--unjudged":
        for j in doc["judgements"]:
            if not j.get("verdict"):
                show(j)
    elif a[0] == "--open":
        pend = [j for j in doc["judgements"] if not j.get("hidde")]
        print(f"{len(pend)} submission(s) Hidde has not answered")
        for j in pend:
            show(j)
    elif a[0] == "--verdict":
        j = js[a[1]]
        j["verdict"] = a[2]
        j["reason"] = a[3] if len(a) > 3 else None
        save(doc)
        show(j)
    elif a[0] == "--feedback":
        j = js[a[1]]
        j["hidde"] = a[2]
        j["agreed"] = (len(a) > 3 and a[3] == "agreed") or a[2].strip().lower() in ("ja", "eens", "goed")
        save(doc)
        show(j)
    elif a[0] == "--learn":
        bad = [j for j in doc["judgements"] if j.get("hidde") and j.get("agreed") is False]
        print(f"{len(bad)} verdict(s) he overruled. Each one is a bug in the rule or a tree we misread.")
        for j in bad:
            show(j)
    elif a[0] == "--report":
        rows = doc["judgements"][:20]
        print("| seen | what | where | size | ours | Hidde |")
        print("|---|---|---|---|---|---|")
        for j in rows:
            m = j.get("measure") or {}
            sz = f"{m['score']:.0%} {m.get('via')}" if m.get("score") is not None else "-"
            print(f"| {j['seen']} | {(j.get('tree') or j['kind'])[:34]} | {j.get('city') or '-'} | "
                  f"{sz} | {j.get('verdict') or 'open'} | {j.get('hidde') or '-'} |")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
