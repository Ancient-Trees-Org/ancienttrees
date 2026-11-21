"""Merge the 2026-11-21 write pass into data/cities.

    python3 scripts/build_write_2026_11_21.py [--check]

Two Stuttgart trees from the pending shelf, written into
data/research/stuttgart-verified.json first (BRIEF_WRITING.md) and merged
here: stu_014 (the Pfaffeneiche) and stu_015 (the 16 Buchen), one walk
through the Rotwildpark about 1.1 km apart.

Not written, and why:
- York's two READY leads. The Minster Yard Beech's one source (Paul Wood,
  The Street Tree no. 12) is paywalled, so beyond species and site we hold
  no fact to write 150 words from. The Museum Gardens plane has no source at
  all and waits for the ambassador's photograph, as its lead says.
- Taiwan: lul_001 is already live; a28_001 is the same tree as live alh_002
  (0 m apart, passcheck --pending). The third entry is _notes, not a tree.

APP FIRST: both trees are new with no reader content, so findable.app_only()
keeps them off the web. --check prints word counts and bans only.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(ROOT, "data", "research")
C = os.path.join(ROOT, "data", "cities")
TREE_FIELDS = ["id", "name", "species", "age_estimate", "age_min", "age_max", "age_basis",
               "girth_cm", "height_m", "location", "location_site", "story", "how_to_recognise",
               "verified_sources", "official_register", "access", "paid_entry", "transport", "best_time",
               "photo", "location_precision", "pin_source", "curation_status"]
MISSING = {"url": None, "license": None, "attribution": None, "status": "missing"}
BANNED = ["hidden gem", "must-see", "breathtaking", "nestled", "majestic", "stunning", "iconic",
          "a testament to", "—", "–", "!"]

PLAN = [
    ("stuttgart", "stu_014", "stuttgart"),
    ("stuttgart", "stu_015", "stuttgart"),
]


def check(t):
    errs = []
    n = len(t["story"].split())
    if not 150 <= n <= 250:
        errs.append(f"story {n} words")
    blob = json.dumps(t, ensure_ascii=False)
    for b in BANNED:
        if b.lower() in blob.lower():
            errs.append("banned " + repr(b))
    rec = t.get("how_to_recognise", "")
    if not rec or len(rec) >= 240:
        errs.append("recognise missing or too long (%d)" % len(rec))
    return n, errs


def main():
    bad = False
    built = []
    for slug, tid, city in PLAN:
        src = json.load(open(os.path.join(R, slug + "-verified.json"), encoding="utf-8"))
        t = dict(next(x for x in src if isinstance(x, dict) and x.get("id") == tid))
        t = {k: t[k] for k in TREE_FIELDS if t.get(k) not in (None, "", [])}
        n, errs = check(t)
        print(city, tid, n, "words", len(t.get("how_to_recognise", "")), "chars", errs or "ok")
        bad = bad or bool(errs)
        built.append((city, t))
    if bad or "--check" in sys.argv:
        sys.exit(1 if bad else 0)
    for city, t in built:
        path = os.path.join(C, city + ".json")
        d = json.load(open(path, encoding="utf-8"))
        if t["id"] in {x["id"] for x in d["trees"]}:
            print(t["id"], "already live")
            continue
        t.setdefault("photo", dict(MISSING))
        t.setdefault("curation_status", "flagged")
        d["trees"].append(t)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(city, "added", t["id"], "now", len(d["trees"]))


if __name__ == "__main__":
    main()
