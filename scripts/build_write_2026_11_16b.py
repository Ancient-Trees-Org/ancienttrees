"""Publish gui_010, the Camellia of Casa de Margaride, into data/cities/guimaraes.json.

    python3 scripts/build_write_2026_11_16b.py [--check]

Verified 2026-11-16 (data/research/guimaraes-verified.json): 2024 Portuguese
Tree of the Year, Despacho 837/2022, paid entry by appointment per the
Associacao Portuguesa dos Jardins Historicos inventory. Species renamed to the
canonical "Common Camellia" (BRIEF_WRITING.md "Species names"; five live
cities use it). The access line gains one sentence saying the booking is open
to anyone, which is what the verify pass settled (hard rule 10: paid entry and
bookable visits are a yes) and what preflight's BOOKING_OPEN_TO_ANYONE reads.
APP FIRST: the tree is new and has no reader content, so findable.app_only()
keeps it off the web; nothing here changes that.
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

STORY = (
    "Portugal's Tree of the Year for 2024 is a camellia barely more than six metres tall. It took "
    "3,900 votes, beating the Sobreiro do Rei on 3,075. In 2023 it was Guimaraes' own Tree "
    "of the Year, and in 2025 it carried Portugal into the European contest and finished fourth.\n\n"
    "It grows in the front courtyard of Casa de Margaride, a house documented since 1021 and held by the "
    "same family for 13 generations. The walled baroque garden behind it dates from around 1675 and runs "
    "through three spaces in turn. The state made house and garden a Monument of Public "
    "Interest in 2012, and in 2022 it classified the garden's trees as a group, this camellia among the "
    "three protected one by one.\n\n"
    "How old it is depends on who you ask. The nature magazine Wilder says about 300 years. The "
    "decree's wording and a Jornal de Noticias report say over a hundred, and the forest service's record "
    "gave 130 at its last measurement. Somewhere between one and three centuries is the honest answer. "
    "Camellias reached Portugal with the sailors of the Discoveries, Wilder notes, but no source says when "
    "this one went in.\n\n"
    "Do not confuse it with the garden's Casa de Fresco, camellia grown about 15 metres tall inside a "
    "circle of box hedge, which is a separate planting.\n\n"
    "The estate is private and cannot be seen from the road. Visits are booked with the owners and paid "
    "for, so confirm the price.")

RECOGNISE = ("You can recognise it by its bell-shaped crown, 6.3 metres across and about as tall. It "
             "stands in the front courtyard of the house, not in the box-hedge circle, whose much taller "
             "camellia is the Casa de Fresco.")

ACCESS_ADD = (" Anyone can book a visit through the association's published contact; the garden is not "
              "open without one.")

UPDATE = {
    "species": "Common Camellia (Camellia japonica)",
    "story": STORY,
    "how_to_recognise": RECOGNISE,
    "paid_entry": True,
    "best_time": {"months": [3], "kind": "flowers",
                  "label": "March, the height of a camellia's late-winter flowering, when spent blooms drop whole under the crown"},
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
        errs.append("recognise too long (%d)" % len(t["how_to_recognise"]))
    return n, errs


def main():
    src = json.load(open(os.path.join(R, "guimaraes-verified.json"), encoding="utf-8"))
    t = dict(next(x for x in src if isinstance(x, dict) and x.get("id") == "gui_010"))
    t.update(UPDATE)
    if "Anyone can book" not in t["access"]:
        t["access"] = t["access"] + ACCESS_ADD
    t = {k: t[k] for k in TREE_FIELDS if t.get(k) not in (None, "", [])}
    n, errs = check(t)
    print("guimaraes", t["id"], n, "words", len(t["how_to_recognise"]), "chars", errs or "ok")
    if errs or "--check" in sys.argv:
        sys.exit(1 if errs else 0)
    path = os.path.join(ROOT, "data", "cities", "guimaraes.json")
    d = json.load(open(path, encoding="utf-8"))
    if t["id"] in {x["id"] for x in d["trees"]}:
        print(t["id"], "already live")
        return
    t.setdefault("photo", dict(MISSING))
    t.setdefault("curation_status", "flagged")
    d["trees"].append(t)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("guimaraes added", t["id"], "now", len(d["trees"]))


if __name__ == "__main__":
    main()
