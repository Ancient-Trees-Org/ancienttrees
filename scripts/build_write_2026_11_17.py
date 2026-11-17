"""Merge the 2026-11-17 write pass into data/cities.

    python3 scripts/build_write_2026_11_17.py [--check]

Ten trees from the pending shelf, written into their research files first
(BRIEF_WRITING.md) and merged here: all_001, asp_001, asp_002, cbu_001,
dmr_002, sgz_005, tmt_001, not_003, ssb_002, ssb_003. Each had a writing-pass
hold that was a judgement (thin life evidence, register point only, which tree
in a wood), not a hard rule; CLAUDE.md "Verify": a judgement never blocks, thin
confirmation is said on the page. Every story says its gap plainly and every
tree carries a recognition line.

Still held, not merged: det_001 and det_002 (no coordinate at all), brd_001,
frk_027, inn_007, not_002 (access not shown public, hard rule 10), sfo_012
(the same tree as live sfo_004).

cbu_001's species is renamed to the canonical "Sycamore (Acer pseudoplatanus)"
(BRIEF_WRITING.md "Species names"). APP FIRST: every tree here is new with no
reader content, so findable.app_only() keeps it off the web.
--check prints word counts and bans only.
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

# (research file, id, city file)
PLAN = [
    ("allentown", "all_001", "allentown"),
    ("aspromonte", "asp_001", "aspromonte"),
    ("aspromonte", "asp_002", "aspromonte"),
    ("castelbuono", "cbu_001", "castelbuono"),
    ("dartmoor", "dmr_002", "dartmoor"),
    ("grazalema-rediam", "sgz_005", "grazalema"),
    ("isole-tremiti", "tmt_001", "isole-tremiti"),
    ("noto", "not_003", "noto"),
    ("serra-san-bruno", "ssb_002", "serra-san-bruno"),
    ("serra-san-bruno", "ssb_003", "serra-san-bruno"),
]
SPECIES = {"cbu_001": "Sycamore (Acer pseudoplatanus)"}

NEW_PLACES = {
    "allentown": {
        "city": "Allentown", "country": "United States", "status": "needs_curation",
        "intro": ("Allentown's biggest recorded cottonwood grows in Lehigh Parkway, the 629-acre city park "
                  "along Little Lehigh Creek, downstream of the Overhill Road interchange. The Pennsylvania "
                  "Big Trees register measured it in 2009 at 5.46 metres round and 40.5 metres tall, about "
                  "133 feet, and scored it at 378 points. Nobody has reported on it since, and the register's "
                  "point does not pick out one crown, so it waits for a visitor to say it still stands."),
        "meta_description": ("An eastern cottonwood 5.46 metres round and 40.5 metres tall in Allentown's "
                             "Lehigh Parkway, on the Pennsylvania Big Trees register since 2009."),
        "question_meta": ("No tree we map in Allentown has a published age. The biggest is a Lehigh Parkway "
                          "cottonwood 5.46 metres round."),
        "question_answer": ("No tree we map in Allentown has a published age. The biggest is an eastern "
                            "cottonwood in Lehigh Parkway beside Little Lehigh Creek, measured in 2009 at "
                            "5.46 metres round and 40.5 metres tall by the Pennsylvania Big Trees register."),
        "question_context": ("Eastern cottonwoods grow fast in wet ground and are short-lived as big trees go, so "
                             "a trunk this size does not date the tree, and the register gives no age. What the "
                             "Pennsylvania Big Trees register does give is the size, 215 inches round, which is "
                             "5.46 metres, and 133 feet tall, which is 40.5 metres, for a score of 378 points. "
                             "That is big, but the register does not list it as a state or national champion. "
                             "The measurement is from 2009, and we have found no later report of the tree and no "
                             "iNaturalist record of a cottonwood within 150 metres of the register's point, so "
                             "whether it still stands is an open question. The register places it on the "
                             "Lehigh Parkway strip beside Little Lehigh Creek, downstream of the Overhill Road "
                             "interchange, without picking out one crown, which makes our pin approximate. "
                             "Lehigh Parkway is a free public park of 629 acres, open daily. If you find a "
                             "cottonwood this size by the creek, tell us it still stands and where."),
        "faq": [
            {"q": "Where is the big cottonwood in Lehigh Parkway?",
             "a": "On the parkway strip beside Little Lehigh Creek, downstream of the Overhill Road interchange. The register's point is approximate, so look for a cottonwood about 5.5 metres round."},
            {"q": "Is it a state champion?",
             "a": "No. The Pennsylvania Big Trees register lists it at 378 points, but not as a state or national champion."},
            {"q": "Is Lehigh Parkway free?",
             "a": "Yes. It is a public city park of Allentown, open every day."},
        ],
        "hero_tree_id": "all_001", "oldest_tree_id": "all_001",
    },
    "aspromonte": {
        "city": "Aspromonte", "country": "Italy", "status": "needs_curation",
        "intro": ("Two of Italy's registered monumental beeches grow on the Sentiero Calabria where it climbs "
                  "from Reggio di Calabria to Gambarie in the Aspromonte national park. One stands at Gornelle, "
                  "near the trail's crossing of the SS 183, 5.36 metres round and 25 metres tall. The other "
                  "stands by the old fountain of Tre Aie, 5.60 metres round and 20 metres tall. One walk through "
                  "the beech wood passes both places."),
        "meta_description": ("Two monumental beeches on the Sentiero Calabria in the Aspromonte, at Gornelle "
                             "and the Tre Aie fountain, 5.36 and 5.60 metres round."),
        "question_meta": ("The Aspromonte's registered beeches stand at Gornelle and Tre Aie on the Sentiero "
                          "Calabria. Nobody has dated them."),
        "question_answer": ("No beech we map in the Aspromonte has a published age. Italy's national register "
                            "lists two big ones on the Sentiero Calabria below Gambarie, at Gornelle and by the "
                            "Tre Aie fountain, 5.36 and 5.60 metres round."),
        "question_context": ("The register gives each tree a girth, a height and a point, but no age and no "
                             "description of the trunk. The beech at Gornelle, sheet 02/H224/RC/18, is 5.36 "
                             "metres round and 25 metres tall. The beech at Tre Aie, sheet 03/H224/RC/18, is "
                             "5.60 metres round and 20 metres tall, the wider and the shorter of the two. The "
                             "same register also lists a stand of silver firs at Tre Aie and a Corsican pine at "
                             "Fragolara, about a hundred metres from the Tre Aie beech. The park's trail page "
                             "names the fountain and the road crossing but not the trees, so the link between "
                             "path and trunk rests on the place names, and we have found no dated sighting of "
                             "either beech. The walk from Piazza Mangeruca in Gambarie to the Tre Aie fountain "
                             "and back takes about an hour and a half to two hours, through beech wood on the "
                             "Sentiero Calabria. Nobody has published an age for these trees, and a girth "
                             "alone does not give one. If you find either beech, tell us which trunk it is."),
        "faq": [
            {"q": "Where are the Aspromonte's monumental beeches?",
             "a": "On the Sentiero Calabria between Gornelle, where the trail crosses the SS 183, and the Tre Aie fountain on the way into Gambarie."},
            {"q": "How long is the walk?",
             "a": "From Gambarie to the Tre Aie fountain and back is about an hour and a half to two hours. Gornelle lies further along the same trail."},
            {"q": "When are the beech woods at their best?",
             "a": "October, when the beeches turn copper and russet."},
        ],
        "hero_tree_id": "asp_002", "oldest_tree_id": "asp_002",
    },
    "castelbuono": {
        "city": "Castelbuono", "country": "Italy", "status": "needs_curation",
        "intro": ("Above Castelbuono, at about 1,600 metres in the Madonie mountains of Sicily, grows the "
                  "Acerone, a sycamore 9.5 metres round and 20 metres tall that Italy's national register lists "
                  "as monumental. It stands in a doline above Serra Circio, has lost its two biggest limbs, and "
                  "was still alive at the last register update in December 2024. Estimates of its age run from "
                  "several centuries to about 900 years. Reaching it is a mountain walk with no signed route."),
        "meta_description": ("The Acerone of the Madonie above Castelbuono: a sycamore 9.5 metres round at "
                             "1,600 metres, put at up to about 900 years old."),
        "question_meta": ("The oldest tree above Castelbuono is the Acerone, a sycamore in the Madonie put at "
                          "up to about 900 years. How sure that is."),
        "question_answer": ("The oldest tree we map near Castelbuono is the Acerone, a sycamore 9.5 metres round "
                            "at about 1,600 metres in the Madonie. The Registro degli Alberi estimates about "
                            "905 years, and a park route page says about 900."),
        "question_context": ("Neither figure comes from a measurement or a ring count. A smaller maple on the "
                             "same walk, the Ciminnita maple, is put at about 450 years, so somewhere between "
                             "the two is the honest range. The national register lists a sycamore of the same "
                             "girth at Piano Ciminnita and Serra Circio, very probably the same tree, though no "
                             "source ties the sheet to the name. A published loop, the Via dei Giganti, about "
                             "9.4 kilometres from Piano Sempria, passes the Catagiddebbe and Ciminnita maples; "
                             "the park signs no route to the Acerone itself. The people who recorded it describe "
                             "a very wide base where the roots have fused, in a hollow with a view to the "
                             "Aeolian Islands. It has lost its two biggest limbs, one at least fourteen years "
                             "ago and the other after 2014, and the register still counted it alive at its "
                             "December 2024 update. If you walk up and stand under it, tell us how it looks."),
        "faq": [
            {"q": "How do I reach the Acerone?",
             "a": "On foot only. The Via dei Giganti loop, about 9.4 kilometres with 617 metres of climbing, starts at Piano Sempria; the last stretch to the Acerone is not signed."},
            {"q": "How big is it?",
             "a": "Italy's national register gives 9.5 metres round and 20 metres tall."},
            {"q": "Can I go in winter?",
             "a": "It stands at about 1,600 metres and snow is possible in winter, so plan it as a mountain walk."},
        ],
        "hero_tree_id": "cbu_001", "oldest_tree_id": "cbu_001",
    },
    "isole-tremiti": {
        "city": "Isole Tremiti", "country": "Italy", "status": "needs_curation",
        "intro": ("On Isola San Nicola, the island of the Tremiti that carries the abbey and fortress, Puglia's "
                  "register of monumental trees protects a small group of ombu, an evergreen tree from the "
                  "South American pampas with a swollen, buttressed base. Two visitors recorded them there in "
                  "August 2025, their GPS points about 18 metres apart. Ferries and hydrofoils reach the island "
                  "in summer from Termoli, Vieste, Peschici and Rodi Garganico."),
        "meta_description": ("The ombu of Isola San Nicola in the Tremiti islands, a South American tree "
                             "on Puglia's register of monumental trees."),
        "question_meta": ("The Tremiti's registered trees are a group of ombu on Isola San Nicola. Nobody has "
                          "dated them."),
        "question_answer": ("No tree we map on the Tremiti has a published age. Puglia's register lists a group "
                            "of ombu, Phytolacca dioica, on Isola San Nicola, and two visitors recorded them "
                            "there in August 2025."),
        "question_context": ("The register calls them a homogeneous group and gives no girth, height or age. "
                             "Two iNaturalist records from August 2025, each confirmed by a second person, fall "
                             "within about 30 metres of the register's point. Whether that spot is on a public "
                             "path or inside a closed part of the abbey and fortress we have not established. "
                             "The ombu is native to the South American pampas, an evergreen with a swollen, "
                             "buttressed base that stands up well to sea wind, which makes a group of them on an "
                             "Adriatic island an oddity worth the register's protection. The two observers' "
                             "GPS points lie about 18 metres apart, so the trees most likely form one small "
                             "cluster rather than being scattered over the island. Ferries and hydrofoils run "
                             "to San Nicola from Termoli, Vieste, Peschici and Rodi Garganico, taking about 45 "
                             "to 90 minutes, and boats run mainly from May to September. If you go, tell us "
                             "which trunk is biggest and how you reached it."),
        "faq": [
            {"q": "What is an ombu?",
             "a": "Phytolacca dioica, an evergreen tree native to South America, known for its swollen, buttressed base and its tolerance of sea wind."},
            {"q": "How do I get to Isola San Nicola?",
             "a": "By ferry or hydrofoil in summer from Termoli, Vieste, Peschici or Rodi Garganico, about 45 to 90 minutes depending on the port. Services thin out outside May to September."},
            {"q": "Can I walk right up to the trees?",
             "a": "We have not established whether they stand on a public path or inside a closed part of the abbey and fortress."},
        ],
        "hero_tree_id": "tmt_001", "oldest_tree_id": "tmt_001",
    },
}
PLACE_KEYS = ["intro", "meta_description", "question_meta", "question_answer", "question_context",
              "faq", "hero_tree_id", "oldest_tree_id"]


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
        if tid in SPECIES:
            t["species"] = SPECIES[tid]
        t = {k: t[k] for k in TREE_FIELDS if t.get(k) not in (None, "", [])}
        n, errs = check(t)
        print(city, tid, n, "words", len(t.get("how_to_recognise", "")), "chars", errs or "ok")
        bad = bad or bool(errs)
        built.append((city, t))
    for city, d in NEW_PLACES.items():
        blob = json.dumps(d, ensure_ascii=False).lower()
        for b in BANNED:
            if b.lower() in blob:
                print(city, "place text banned", repr(b))
                bad = True
        print(city, "intro", len(d["intro"].split()), "words")
    if bad or "--check" in sys.argv:
        sys.exit(1 if bad else 0)
    for city, t in built:
        path = os.path.join(C, city + ".json")
        if os.path.exists(path):
            d = json.load(open(path, encoding="utf-8"))
        else:
            d = dict(NEW_PLACES[city])
            d["trees"] = []
        if city in NEW_PLACES:
            for k in PLACE_KEYS:
                d[k] = NEW_PLACES[city][k]
        if t["id"] in {x["id"] for x in d["trees"]}:
            print(t["id"], "already live")
            if city in NEW_PLACES:
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(d, f, ensure_ascii=False, indent=2)
                    f.write("\n")
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
