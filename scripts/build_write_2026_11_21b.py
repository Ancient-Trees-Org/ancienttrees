"""Merge the second 2026-11-21 write pass into data/cities.

    python3 scripts/build_write_2026_11_21b.py [--check]

Four Ottawa trees from the NCC remarkable-trees register, all at the Central
Experimental Farm and within about 250 m of each other, so they join the
Arboretum walk already live (ott_015 to ott_019): ott_023 (the ginkgo),
ott_024 (the Duke of Connaught's red oak), ott_025 (the cucumber tree) and
ott_026 (the Macoun Garden sycamore). Written into
data/research/ottawa-verified.json first (BRIEF_WRITING.md) and merged here.
Two species names were set to the corpus's canonical ones: Northern Red Oak
and Cucumber Tree Magnolia.

Not written, and why:
- York's READY lead, the riverside London plane in Museum Gardens. It has a
  pin (the ambassador's what3words) and nothing else: no source, no photo,
  no measurement. 150 words would be invented. It waits for the
  ambassador's photograph, as its lead says.

APP FIRST: all four are new with no reader content, so findable.app_only()
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
    ("ottawa", "ott_023", "ottawa"),
    ("ottawa", "ott_024", "ottawa"),
    ("ottawa", "ott_025", "ottawa"),
    ("ottawa", "ott_026", "ottawa"),
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
