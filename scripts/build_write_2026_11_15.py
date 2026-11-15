"""Publish the 2026-11-15 Chicago write pass into data/cities.

    python3 scripts/build_write_2026_11_15.py [--check]

chi_059 to chi_064 come from data/research/chicago-verified.json: Forest
Preserves of Cook County champion-register rows (GNSS fix at the tree, girth
converted from inches). chi_058 was folded away as a duplicate of chi_004.
The coffeetree's Latin name is set to the spelling the other cities use.
--check prints word counts and bans only.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(ROOT, "data", "research")
TREE_FIELDS = ["id", "name", "species", "age_estimate", "age_min", "age_max", "age_basis",
               "girth_cm", "height_m", "location", "location_site", "story", "how_to_recognise",
               "verified_sources", "official_register", "access", "paid_entry", "transport", "best_time",
               "photo", "location_precision", "pin_source", "curation_status", "verify_notes"]
MISSING = {"url": None, "license": None, "attribution": None, "status": "missing"}
BANNED = ["hidden gem", "must-see", "breathtaking", "nestled", "majestic", "stunning", "iconic",
          "a testament to", "—", "–", "!"]

PLAN = [("chicago", "chicago", f"chi_0{n}") for n in range(59, 65)]
OVERRIDE = {"chi_061": {"species": "Kentucky Coffeetree (Gymnocladus dioica)"}}


def check(t):
    errs = []
    n = len(t["story"].split())
    if not 150 <= n <= 250:
        errs.append(f"story {n} words")
    blob = json.dumps(t, ensure_ascii=False)
    for b in BANNED:
        if b.lower() in blob.lower():
            errs.append("banned " + repr(b))
    if len(t.get("how_to_recognise", "")) >= 240:
        errs.append("recognise too long")
    if t.get("hold"):
        errs.append("held: " + t["hold"][:60])
    return n, errs


def main():
    todo = []
    bad = False
    for slug, rfile, rid in PLAN:
        src = json.load(open(os.path.join(R, rfile + "-verified.json"), encoding="utf-8"))
        t = dict(next(x for x in src if isinstance(x, dict) and x.get("id") == rid))
        t.update(OVERRIDE.get(rid, {}))
        n, errs = check(t)
        print(slug, rid, n, "words", errs or "ok")
        bad = bad or bool(errs)
        todo.append((slug, t))
    if bad or "--check" in sys.argv:
        sys.exit(1 if bad else 0)
    for slug, t in todo:
        path = os.path.join(ROOT, "data", "cities", slug + ".json")
        d = json.load(open(path, encoding="utf-8"))
        if t["id"] in {x["id"] for x in d["trees"]}:
            print(t["id"], "already live")
            continue
        o = {k: t[k] for k in TREE_FIELDS if t.get(k) not in (None, "", [])}
        o.setdefault("photo", dict(MISSING))
        o.setdefault("curation_status", "flagged")
        d["trees"].append(o)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(slug, "added", t["id"], "now", len(d["trees"]))


if __name__ == "__main__":
    main()
