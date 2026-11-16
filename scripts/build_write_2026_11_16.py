"""Publish the 2026-11-16 write pass into data/cities.

    python3 scripts/build_write_2026_11_16.py [--check]

phl_010 The Grumblethorpe Ginkgo: written 2026-11-15 and held under hard rule
10 because its access line came from search summaries and named tours by
appointment. The owner's visit page (philalandmarks.org/contact-visit, fetched
2026-11-16) gives public open hours and a ticket price, so the access line is
rewritten from that page and the closing paragraph follows it.

lpz_032 The Horse Chestnut of Papiermuehlstrasse: the READY Leipzig lead ND 34,
cadastre N79444 (read 2026-11-16 by baumnummer: girth 354 cm, 14 m, crown 12 m,
planting-year class 1876, not felled) plus the city's natural-monument list
(ND 34, Flurstueck 236/2, protected surround 17 m, resolution 601/96). At 354 cm
it is 96% of species_size.py's horse-chestnut reference (p90 369, n=260).
--check prints word counts and bans only.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(ROOT, "data", "research")
TREE_FIELDS = ["id", "name", "species", "age_estimate", "age_min", "age_max", "age_basis",
               "girth_cm", "height_m", "location", "location_site", "story", "how_to_recognise",
               "verified_sources", "official_register", "access", "paid_entry", "transport", "best_time",
               "photo", "location_precision", "pin_source", "curation_status"]
MISSING = {"url": None, "license": None, "attribution": None, "status": "missing"}
BANNED = ["hidden gem", "must-see", "breathtaking", "nestled", "majestic", "stunning", "iconic",
          "a testament to", "—", "–", "!"]

PHL_STORY = (
    "The people who run Grumblethorpe believe the ginkgo in its grounds is one of the oldest female "
    "ginkgoes in America.\n\n"
    "Ginkgoes come as separate male and female trees, and only the females fruit. Philadelphia's famous "
    "one, at Bartram's Garden, is a male planted in 1785. This is the other half of the story. The "
    "Philadelphia Society for the Preservation of Landmarks, which owns the house, calls it a massive "
    "fruiting ginkgo that towers over the property and dates it to around 1830. The Philadelphia Orchard "
    "Project names the man who planted it, Charles Wister Sr., and goes a step further, saying it may be "
    "the oldest known living female ginkgo in the country.\n\n"
    "Both accounts say circa 1830, and other dates circulate, so take roughly 190 years as an estimate "
    "rather than a record. Nobody has published its girth or height.\n\n"
    "The tree grew up with a family of gardeners. John Wister built the house in 1744, later Wisters were "
    "botanists, and by the owner's account the climbing wisteria is named for them. Grumblethorpe now sits "
    "inside the Colonial Germantown Historic District.\n\n"
    "Seeing it takes planning. The house opens to the public on the second Saturday of each month "
    "from May to October, noon to 4 pm, with garden mornings from August to October, and a ticket costs "
    "$10. Special events can cut hours, so email ahead. The pin marks the house, not the trunk, and it "
    "is not established whether the tree can be seen from Germantown Avenue.")

PHL_ACCESS = (
    "Paid entry, open to the public on set days. Grumblethorpe, run by the Philadelphia Society for the "
    "Preservation of Landmarks, opens every second Saturday of the month from May to October, 12 to 4 pm; "
    "garden hours August to October, 10 am to 12 pm (owner's visit page, philalandmarks.org/contact-visit). "
    "General admission $10, students and seniors $8, families $25, free under 6. Open hours may be limited "
    "by special events, so email the society to check. Other visits are arranged with the society. Whether "
    "the ginkgo can be seen from Germantown Avenue is not established.")

PHL = {
    "access": PHL_ACCESS,
    "paid_entry": True,
    "story": PHL_STORY,
    "best_time": {"months": [10], "kind": "autumn colour",
                  "label": "October, the last month the garden opens, as the fan-shaped leaves turn gold"},
    "verified_sources": ["https://www.philalandmarks.org/grumblethorpe",
                         "https://www.phillyorchards.org/2020/11/19/spotlight-on-ginkgo-pretty-edible-historic/",
                         "https://www.philalandmarks.org/contact-visit"],
}

CADASTRE = ("https://geodienste.leipzig.de/l3/OpenData/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature"
            "&typeNames=OpenData:Baeume&outputFormat=application/json&CQL_FILTER=baumnummer%3D%27N79444%27")

LPZ_STORY = (
    "This street-corner chestnut in Stötteritz sits close to the top tenth of the 260 horse chestnuts we "
    "hold a measured girth for, anywhere. Leipzig's tree cadastre puts its trunk at 3.54 metres round "
    "and 1.13 metres through.\n\n"
    "It is not a tall tree. The same record gives it 14 metres of height under a crown 12 metres wide, so "
    "it reads as broad and low rather than soaring. Leipzig protects it as natural monument number 34, "
    "under council resolution 601/96, together with a ring of 17 metres of ground around the trunk. It "
    "stands on a patch of public green where Papiermühlstrasse meets Oststrasse.\n\n"
    "Nobody has published when it was planted. The cadastre files it under the planting year 1876, a "
    "figure the city gives to a whole class of trees rather than a record of this one, so read it as "
    "roughly 150 years and no tighter.\n\n"
    "Horse chestnuts are not native here. They came to central Europe from the Balkans in the sixteenth "
    "century and were planted for shade and show, and this one should do what the species is known for: "
    "upright white candles of flowers in May, shiny brown conkers in the autumn.\n\n"
    "The latest word on it is the city's own tree register, which on 16 November 2026 still listed it as "
    "standing. If you pass the corner, tell us how it looks, and if you know who planted it, tell us that "
    "too.")

LPZ = {
    "id": "lpz_032",
    "name": "The Horse Chestnut of Papiermühlstrasse",
    "species": "Horse Chestnut (Aesculus hippocastanum)",
    "age_estimate": "about 150 years, by the city cadastre's planting-year class",
    "age_min": 130,
    "age_max": 170,
    "age_basis": "source",
    "girth_cm": 354,
    "height_m": 14,
    "location": {"address": "Papiermühlstrasse at the corner of Oststrasse, Leipzig",
                 "latitude": 51.32272, "longitude": 12.42119, "neighbourhood": "Stötteritz"},
    "story": LPZ_STORY,
    "how_to_recognise": ("You can recognise it by the trunk, 3.54 metres round, under a crown about 12 "
                         "metres wide and only 14 metres tall. It stands on the green at the corner of "
                         "Papiermühlstrasse and Oststrasse."),
    "verified_sources": [CADASTRE, "https://de.wikipedia.org/wiki/Liste_der_Naturdenkmale_in_Leipzig"],
    "official_register": {"name": "Stadt Leipzig Baumkataster (open data WFS), Naturdenkmal ND 34, tree N79444",
                          "url": CADASTRE},
    "access": ("Free, public city green at a street corner (cadastre area 'Grün- und Parkanlagen', "
               "Papiermühlstrasse/Oststrasse, Stötteritz)."),
    "best_time": {"months": [5], "kind": "flowers",
                  "label": "May, when the crown carries the upright white flower candles of a horse chestnut"},
    "location_precision": "approximate",
    "curation_status": "flagged",
}


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
    return n, errs


def main():
    src = json.load(open(os.path.join(R, "philadelphia-verified.json"), encoding="utf-8"))
    phl = dict(next(x for x in src if isinstance(x, dict) and x.get("id") == "phl_010"))
    phl.update(PHL)
    todo = [("philadelphia", phl), ("leipzig", dict(LPZ))]
    bad = False
    for slug, t in todo:
        t = {k: t[k] for k in TREE_FIELDS if t.get(k) not in (None, "", [])}
        n, errs = check(t)
        print(slug, t["id"], n, "words", errs or "ok")
        bad = bad or bool(errs)
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
