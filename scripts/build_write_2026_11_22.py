"""Merge the 2026-11-22 write pass into data/cities.

    python3 scripts/build_write_2026_11_22.py [--check]

The pending pool was nearly empty: every other unpublished entry in
passcheck.py --pending was either live under another id (Cardiff, Cyprus,
Split, Tenerife, Wolverhampton, Fort Greene, Saratoga Park, Paros stone pine
folded into pao_001) or claimed by the Birmingham verify pass in flight
(hwp_001, left for that pass's writer). Three trees flagged only for standing
near a live tree of a different species, checked by hand and kept:

- lvg_015 Mondell pine behind the Carlson Education Building, UNLV (Nevada
  Big Tree Register 2023 champion; 26 m from the Camperdown elm lvg_012).
- lvg_016 holm oak beside White Hall, UNLV (UNLV's champion list only; 25 m
  from the Buddhist pine lvg_013). Species canonicalised to Holm Oak.
- nyc_029 American hornbeam across from the Camperdown Elm, Prospect Park
  (NYC Parks Great Trees; 40 m from the pagoda tree nyc_144).

Written into data/research/*-verified.json first (BRIEF_WRITING.md). No
best_time: two evergreens and a hornbeam with no seasonal peak in its source.
APP FIRST: all three are new with no reader content, so findable.app_only()
keeps them off the web.
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
    ("las-vegas", "lvg_015", "las-vegas"),
    ("las-vegas", "lvg_016", "las-vegas"),
    ("new-york", "nyc_029", "new-york"),
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
