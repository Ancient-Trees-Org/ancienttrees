#!/usr/bin/env python3
"""Eleven readers' trees from the weekend of 2026-11-15/16, live under the
closed list (Hidde, 2026-11-17: "we need either a gps or photo and it needs
to be somewhat special"). Every photograph was viewed in the session that ran
this. Run once; it refuses to add a tree id that already exists.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
os.chdir(ROOT)
sys.path.insert(0, HERE)
from sightings_publish import write_image, slugify  # noqa: E402

TODAY = "2026-11-17"
BASE = "https://ancienttrees.app/photos/"


def photo(src, tree_id, name, user_code, sid, seen):
    fname = "%s-%s.jpg" % (tree_id, slugify(name.replace("The ", "", 1)))
    w, h = write_image(src, os.path.join("site", "public", "photos", fname))
    return {
        "url": BASE + fname,
        "license": "Provided by a reader through Ancient Trees, all rights reserved",
        "attribution": None,
        "status": "approved",
        "width": w,
        "height": h,
        "source": "contributor",
        "contributor_user_id": user_code,
        "sighting_id": sid,
        "note": ("Photographed by a reader and sent to Ancient Trees (%s); viewed and approved "
                 "on %s: %s Not an open licence: ask before reuse elsewhere. No name is printed "
                 "beside it (2026-09-04)." % (TREE_SENT[sid], TODAY, seen)),
    }


TREE_SENT = {}

TREES = [
 dict(city="cusop", sid="471cdeb1-6853-43a4-85a6-f926e83b532c", src="out/inspect/471cdeb1-6853-43a4-85a6-f926e83b532c.jpg",
  user="p_15642ad760ce3bac3f536318", sent="2026-11-17, through the app",
  seen="the whole yew from the churchyard grass, its fluted red trunk under a full crown, gravestones either side, daylight, colour.",
  tree=dict(id="cus_001", name="The Churchyard Yew of Cusop", species="European Yew (Taxus baccata)",
   age_estimate=None, age_min=None, age_max=None,
   location={"address": "Churchyard, Church Road, Cusop, Herefordshire", "latitude": 52.0669347677227, "longitude": -3.1099705959563, "neighbourhood": "Cusop"},
   how_to_recognise="The big yew at the end of a curving gravel path in the churchyard: a squat, deeply fluted red trunk under a dense dark crown, an old lichened gravestone standing in the grass in front of it.",
   access="Free. A village churchyard, open in daylight.",
   story=("Cusop sits on the English side of the Dulas Brook, a short walk from the bookshops of Hay-on-Wye, and in its churchyard a reader stopped at this yew and sent us a photograph.\n\n"
          "What the picture shows is the kind of yew that makes people slow down in a churchyard. The trunk is short and enormously thick, its red bark running in deep vertical folds and ridges, as if several stems had grown together and kept on growing. Above it the crown spreads wide and dark, low enough on one side to brush the grass. Someone keeps a path of bare earth worn round the foot of it, and old headstones lean in the grass on either side.\n\n"
          "We do not yet know its girth or its age, and churchyard yews are famously hard to date: a hollow trunk loses the rings that would tell. If you have measured it, or know what the parish says about it, tell us here and we will add it with your figures.\n\n"
          "Go when the church is open and walk the path all the way round the trunk."),
  )),
 dict(city="los-angeles", sid="dadb2ea4-792f-460d-b66d-d46f064f0a8a", src="out/inspect/dadb2ea4-792f-460d-b66d-d46f064f0a8a.jpg",
  user="p_a52c97c9ecd3468c7f9a998f", sent="2026-11-17, through the app",
  seen="the trunk and its buttress roots in ivy, the white house with the green tiled roof behind, daylight, colour.",
  tree=dict(id="lax_033", name="The Moreton Bay Fig by the White Mansion", species="Moreton Bay Fig (Ficus macrophylla)",
   age_estimate=None, age_min=None, age_max=None,
   location={"address": "Near Lockehaven Street, west Pasadena", "latitude": 34.1386861166667, "longitude": -118.15981945, "neighbourhood": "Pasadena"},
   how_to_recognise="A pale grey fig on a bed of ivy, its roots pouring out in fat ribs around the base, with a white mansion under a green tiled roof and a row of flagpoles just beyond it.",
   access="The reader photographed it from the lawn beside the house. We have not confirmed whether these grounds are open at all hours; check before you go.",
   story=("A reader walking in west Pasadena sent us this photograph from the foot of the tree: a Moreton Bay fig, the Australian giant that Southern California planted in the late nineteenth century and has been living in the shade of ever since.\n\n"
          "This one is all trunk and root. The smooth grey bole rises out of a bed of ivy and splits into great limbs that reach far out over the lawn, while at the bottom the roots run out in thick ribbed buttresses, the way a Moreton Bay fig props itself up as it ages. Behind it stands a white mansion with a green tiled roof and a row of flagpoles, the tree easily as wide as the front of the house is tall.\n\n"
          "We do not know the house's name for certain, who planted the fig, or when. If you know this tree, or the grounds it stands in, tell us here and we will put your words on the page.\n\n"
          "Stand back on the lawn to take in the whole spread of the crown, then walk in close to see the roots."),
  )),
 dict(city="tilaran", sid="00fd8d2f-72a7-44c8-9d4a-7f1eb5380462", src="out/inspect/00fd8d2f-72a7-44c8-9d4a-7f1eb5380462.jpg",
  user="p_e6628375ba1aea1573317fad", sent="2026-11-16, through the app",
  seen="the whole lower trunk from below, a lattice of roots and an arch at the left, forest around it, daylight, colour.",
  tree=dict(id="tlr_001", name="The Elephant-Trunk Fig of Tilarán", species="Fig (Ficus sp.)",
   age_estimate="300 to 400 years, by a reader's estimate", age_min=None, age_max=None,
   location={"address": "Forest beside Vía 927, Sabalito, Tilarán, Guanacaste", "latitude": 10.5645460347411, "longitude": -85.0081071938515, "neighbourhood": "Sabalito"},
   how_to_recognise="In the forest: a trunk made of many fused roots climbing together, with one root peeling away on the left to leave a tall open arch.",
   access="The reader reached it on foot through forest near Vía 927. We have not confirmed who owns the land; ask locally before you go.",
   story=("\"It looks like an elephant's trunk,\" wrote the reader who sent this tree from the hills above Lake Arenal, near Tilarán in Costa Rica.\n\n"
          "Look at the left side of the photograph and you can see what they mean. The trunk is not one trunk at all but a column of roots that have climbed together and fused, and one of them curls away from the rest and down to the ground, leaving a tall arch you could look through. That latticed, poured look is the mark of a strangler fig, which starts high in another tree and sends its roots down until they become a trunk of their own. The reader knows it as a kapok; tell us which you think it is.\n\n"
          "They put it at 300 to 400 years old and its girth at about twenty metres. Those are their figures, not a measurement we have seen, and a fig's fused trunk is hard to measure.\n\n"
          "If you go, walk round to the arch and stand inside it."),
  )),
 dict(city="tilaran", sid="df10cd8a-f0f4-4911-a37f-b5b4e85b7425", src="out/inspect/df10cd8a.jpg",
  user="p_e6628375ba1aea1573317fad", sent="2026-11-16, through the app",
  seen="a mass of fused pale fig trunks and roots on a raised bank above stone steps and a wall, daylight, colour.",
  tree=dict(id="tlr_002", name="The Figs Saved by a Wall", species="Fig (Ficus sp.)",
   age_estimate="300 to 400 years, by a reader's estimate", age_min=None, age_max=None,
   location={"address": "Above a stone wall and steps, Santa Rosa, Tilarán, Guanacaste", "latitude": 10.52263, "longitude": -84.966295, "neighbourhood": "Santa Rosa"},
   how_to_recognise="Three great pale figs grown into one mass of roots on a raised bank, held in by a low stone wall with steps running up beside it.",
   access="Seen from the steps beside the wall, where the reader stood. We have not confirmed who owns the land behind it.",
   story=("\"3 trees in close proximity, saved from destruction by building a wall in front of them,\" wrote the reader who sent us this photograph from Santa Rosa, near Tilarán in Costa Rica.\n\n"
          "The wall is in the picture, a low run of grey stone with steps climbing beside it, and above it the three trees have grown into one another until it is hard to say where one ends. Pale roots hang from the branches, drop to the bank and thicken into new trunks, wrapping round the old ones in ropes and plates. That is how a fig behaves once it has room, and the reader's three look like it, although they know them as kapoks. Tell us which you think they are.\n\n"
          "The reader puts them at 300 to 400 years old and one trunk at about fifteen metres round. Those figures are theirs; we have not seen a measurement. Who built the wall, and when, we would love to know too.\n\n"
          "Stand on the steps and look up into the roots."),
  )),
 dict(city="lisbon", sid="4cec5259-ac92-4a7a-9c4c-9f6ddd1acd1a", src="out/inspect/4cec5259-ac92-4a7a-9c4c-9f6ddd1acd1a.jpg",
  user="p_c516cec5b9e607f5340d3a45", sent="2026-11-17, through the app",
  seen="the whole oak and its broad round crown in the arcaded courtyard of a yellow building, hedge in front, overcast daylight, colour.",
  tree=dict(id="lis_039", name="The Portuguese Oak of the Agronomy Cloister", species="Portuguese Oak (Quercus faginea)",
   age_estimate="about 96 years, by a reader's estimate", age_min=None, age_max=None,
   location={"address": "Courtyard of the Instituto Superior de Agronomia, Tapada da Ajuda, Lisbon", "latitude": 38.7077237792144, "longitude": -9.18254545517746, "neighbourhood": "Ajuda"},
   how_to_recognise="The single big oak filling the arcaded courtyard of the yellow agronomy building, its trunk behind a low box hedge and its crown as wide as the courtyard.",
   access="On the Instituto Superior de Agronomia campus in the Tapada da Ajuda; the reader walked into the courtyard. Visit in campus hours.",
   story=("Lisbon's agronomy school has been teaching people about plants inside the walled Tapada da Ajuda for well over a century, and at the heart of its main building, in a courtyard ringed by yellow arcades, stands this oak. A reader sent us its photograph from the courtyard.\n\n"
          "It is a Portuguese oak, Quercus faginea, the semi-evergreen oak of Iberia's hills, and it has had the courtyard to itself long enough to grow into the shape oaks take when nothing crowds them. A short thick trunk stands behind a low box hedge and opens almost at once into a dome of crooked limbs, as wide as the courtyard and nearly as tall as the building's roof. In the reader's picture the leaves are turning, brown and bronze against the grey sky.\n\n"
          "The reader gives it 96 years. We have no girth or record of its planting yet; if you know the campus's own story of this tree, tell us here.\n\n"
          "Walk the arcade all the way round and watch the crown change shape against the roofs."),
  )),
 dict(city="melbourne", sid="665082d2-815b-4630-883a-5f619725cdb9", src="out/inspect/665082d2-815b-4630-883a-5f619725cdb9.jpg",
  user="p_68e3fe2f2c08d678d123d61f", sent="2026-11-16, through the app",
  seen="the whole tree beside a garden path, its low limbs sweeping out in every direction over a roped bed, overcast daylight, colour.",
  tree=dict(id="mel_017", name="The Water Gum that Reaches Out", species="Water Gum (Tristaniopsis laurina)",
   age_estimate=None, age_min=None, age_max=None,
   location={"address": "Royal Botanic Gardens Victoria, Melbourne Gardens, South Yarra", "latitude": -37.8328053558392, "longitude": 144.982058420709, "neighbourhood": "South Yarra"},
   how_to_recognise="Beside a garden road: a low tree whose pale, peeling limbs spread from one base in every direction like the spokes of a wheel, one of them reaching almost to the path, behind a low rope.",
   access="Free, in the Royal Botanic Gardens; open daily.",
   story=("\"It seems to reach out to say hello in all directions,\" wrote the reader who sent us this tree from Melbourne's Royal Botanic Gardens.\n\n"
          "It is a water gum, Tristaniopsis laurina, a tree of the creek banks of eastern Australia, usually neat and modest in a street. This one has been left to do as it likes. From a single base its limbs splay out like the spokes of a wheel, pale and smooth and peeling in patches, and the longest of them runs almost flat along the ground for metres before turning up towards the light, as if offering a hand to whoever walks along the road. A low rope keeps feet off its roots, and a garden label stands among the limbs.\n\n"
          "We do not know when it was planted or how wide it spreads. The gardens may; if you find out, tell us here.\n\n"
          "Walk round it on the grass side, where you can see every limb leave the base at once."),
  )),
 dict(city="melbourne", sid="993d2833-d88b-43cc-a6e2-804c1e2c6921", src="out/inspect/993d2833-d88b-43cc-a6e2-804c1e2c6921.jpg",
  user="p_68e3fe2f2c08d678d123d61f", sent="2026-11-16, through the app",
  seen="the leaning grey trunk from its flaring roots to the crown, a steel boardwalk passing beneath it among tree ferns and palms, daylight, colour.",
  tree=dict(id="mel_018", name="The Leaning Fig over the Boardwalk", species="Fig (Ficus sp.)",
   age_estimate=None, age_min=None, age_max=None,
   location={"address": "Royal Botanic Gardens Victoria, Melbourne Gardens, South Yarra", "latitude": -37.8314956491425, "longitude": 144.980384196569, "neighbourhood": "South Yarra"},
   how_to_recognise="Among tree ferns and tall palms: a smooth grey fig trunk leaning hard over a rusted steel boardwalk, its roots gripping the bank on the right.",
   access="Free, in the Royal Botanic Gardens; open daily.",
   story=("A reader sent us this fig from the Royal Botanic Gardens in Melbourne, taken on the boardwalk beneath it, and the photograph explains why they stopped.\n\n"
          "The tree leans. From a bank of roots on the right it sets off at a steep angle, smooth and grey, crosses over the walkway and only then bends upright, so that anyone on the boardwalk passes under the trunk itself. Around it the gardens have made a small rainforest: tree ferns unrolling at head height, bird's nest ferns in the roots, and fan palms rising straight past the fig into the canopy. Its roots spread in thick flanges over the bank, the way big figs hold themselves up.\n\n"
          "It is a fig, but which one we would like a reader to confirm: the flared roots and the broad leaves look like a Moreton Bay fig. We have no age or size for it yet; tell us here if you know.\n\n"
          "Walk the boardwalk slowly, and look up as you pass beneath the lean."),
  )),
 dict(city="buenos-aires", sid="b451d1e8-4b8b-4bb0-9680-01874b41c26b", src="out/inspect/b451d1e8-4b8b-4bb0-9680-01874b41c26b.jpg",
  user="p_c2012de5624108c0f0e2806e", sent="2026-11-17, through the app",
  seen="the whole tree at dusk from its sprawling buttress roots up into the crown, the plaza's railings and lamps behind, colour.",
  tree=dict(id="bai_005", name="The Gomero of Plaza San Martín", species="Moreton Bay Fig (Ficus macrophylla)",
   age_estimate="250 to 300 years, by a reader's estimate", age_min=None, age_max=None,
   location={"address": "Plaza San Martín, Retiro, Buenos Aires", "latitude": -34.5955810487646, "longitude": -58.3765121594678, "neighbourhood": "Retiro"},
   how_to_recognise="In the middle of the plaza: a fig whose roots run out over bare earth like a frozen river delta, under a crown that covers the lawns around it, inside a low iron railing.",
   access="Free, in a public plaza, open at all hours.",
   verified_sources=["https://buenosaires.gob.ar/sites/default/files/2024-04/Listado%20de%20%C3%81rboles%20Hist%C3%B3ricos%20y%20Notables%20-%20GCBA.pdf (Buenos Aires city government, list of historic and notable trees: Gomero de Plaza San Martín, Ficus macrophylla, notable)"],
   story=("\"One of the oldest inhabitants of Buenos Aires,\" wrote the reader who sent us this tree from Plaza San Martín in Retiro. \"Possibly the second or third oldest tree after the Gomero de la Recoleta. This one is called Gomero de Plaza San Martín.\"\n\n"
          "The city knows it by that name too: its own list of historic and notable trees includes the Gomero de Plaza San Martín, a Moreton Bay fig, among the notable ones. Porteños call these Australian figs gomeros, and the plaza's is a giant. Its roots run out over the bare earth in every direction like the channels of a river delta, ribbed and grey and higher than a person's knee, and from them a short trunk breaks into limbs that carry the crown far out over the lawns.\n\n"
          "The reader puts it at 250 to 300 years and its girth at about twelve metres. Those figures are theirs; the city's list gives neither.\n\n"
          "Come at dusk, as the reader did, when the lamps come on under the crown."),
  )),
 dict(city="ferrara", sid="tip-990", src="out/inspect/tip-990.jpg",
  user="p_64aded5e0bdd8d60b3e78790", sent="2026-11-16, through the website",
  seen="the whole tall oak from the foot of its trunk inside a rope fence up into the crown, park lawn around, daylight, colour.",
  tree=dict(id="fer_006", name="The Oak of Parco Massari", species="Pedunculate Oak (Quercus robur)",
   age_estimate="about 150 years, by a reader's estimate", age_min=None, age_max=None,
   location={"address": "Parco Massari, Corso Porta Mare, Ferrara", "latitude": 44.8435561, "longitude": 11.6237259, "neighbourhood": "Addizione Erculea"},
   how_to_recognise="A very tall straight oak in the park, its trunk ringed by a low rope fence on wooden posts, ivy climbing the lower trunk.",
   access="Free, in a public park, open in daytime.",
   verified_sources=["https://www.facebook.com/ilregistrodeglialberi/posts/una-bella-farnia-quercus-robur-al-parco-massari-a-ferrara/1076894882919340/ (Il Registro degli Alberi: a pedunculate oak, Quercus robur, in Parco Massari, Ferrara; cited by the reader)"],
   story=("\"Albero monumentale protetto dalla Regione Emilia-Romagna,\" begins the note of the reader who sent us this oak from Parco Massari in Ferrara: a monumental tree protected by the Emilia-Romagna region, about 150 years old by their estimate, its trunk 480 centimetres round.\n\n"
          "Parco Massari is the big green behind the Renaissance palaces of Corso Porta Mare, and this pedunculate oak is one of its tallest trees. The photograph is taken from its foot looking up: a dark, deeply furrowed trunk with ivy climbing it, rising straight for a long way before the first great limbs spread into a high, airy crown. A low rope fence on wooden posts keeps a circle of ground clear around it.\n\n"
          "The reader also wrote down what it is like to stand there: \"E' maestosa e forte, ma stare sotto le sue fronde dà anche un senso di ospitalità e protezione.\" It is majestic and strong, but standing under its branches also gives a sense of welcome and protection.\n\n"
          "Our pin marks the park, not the tree; if you find it, send us a photograph with your location and we will move it."),
  )),
 dict(city="balmerino", sid="tip-993", src="out/inspect/tip-993.jpg",
  user="p_689c4e2ff0c620317107e194", sent="2026-11-16, through the website",
  seen="the low, twisted, lichen-grey trunk with its leaning limb on green props, autumn leaves, a timber rail around it, daylight, colour.",
  tree=dict(id="blm_001", name="The Balmerino Abbey Chestnut", species="Sweet Chestnut (Castanea sativa)",
   age_estimate="400 to 450 years; 500 by a reader's estimate", age_min=400, age_max=500,
   location={"address": "Balmerino Abbey, Balmerino, Fife", "latitude": 56.4098940, "longitude": -3.0412895, "neighbourhood": "Balmerino"},
   how_to_recognise="Beside the abbey ruins: a short, twisted, lichen-grey chestnut trunk with great swollen burrs at its foot, its long leaning limbs held up on green metal props inside a timber rail.",
   access="Free. In the grounds of the ruined abbey, open in daylight.",
   verified_sources=[
    "https://gazetteer.org.uk/place/Balmerino_Abbey,_Fife_299726 (Gazetteer for Great Britain and Northern Ireland: a Spanish chestnut about 400 years old in the grounds, alleged to be the oldest tree in Fife)",
    "https://hridigital.shef.ac.uk/cistercians/abbeys/balmerino.php (University of Sheffield, Cistercian abbeys: the chestnut believed to have been planted by the monks)",
    "https://EN.wikipedia.com/wiki/Balmerino (Balmerino: a chestnut tree about 450 years old at the abbey)"],
   story=("Balmerino Abbey was founded on the south shore of the Firth of Tay in the thirteenth century, and among its broken red walls grows a sweet chestnut that local accounts call the oldest tree in Fife. A Gazetteer of Great Britain puts it at about 400 years; other accounts say 450, and a University of Sheffield survey of Cistercian houses notes the belief that the monks planted it.\n\n"
          "The reader who sent us this photograph puts it at 500 years, its girth at five metres, and adds a story of their own: that it \"may mark the remains of Queen Ermengarde of Scotland\". We have no source for that, so take it as theirs.\n\n"
          "What the photograph shows is a tree that has spent centuries falling over slowly. The trunk is short, twisted and grey with lichen, swollen at the base into great burrs, and its long limbs lean so far that green metal props now carry them. A timber rail keeps visitors a step away, and in autumn the leaves go copper over the grass.\n\n"
          "Walk round to the side of the props to see how far the old limbs reach."),
  )),
 dict(city="bologna", sid="tip-995", src="out/inspect/tip-995.jpg",
  user="p_64aded5e0bdd8d60b3e78790", sent="2026-11-16, through the website",
  seen="looking up a thick white poplar trunk that splits into several stems, pale upper bark, fresh green leaves, daylight, colour.",
  tree=dict(id="bol_014", name="The Three-Hundred-Year Poplar of Lagoverde", species="White Poplar (Populus alba)",
   age_estimate="about 300 years, by a reader's estimate", age_min=None, age_max=None,
   location={"address": "Oasi del Lagoverde, Via Cristoforo Colombo 77, Corticella, Bologna", "latitude": 44.5447999, "longitude": 11.3483213, "neighbourhood": "Navile"},
   how_to_recognise="On the path into the oasis, on the left from the entrance: a white poplar whose thick dark trunk splits into four pale stems climbing together.",
   access="Inside the Oasi del Lagoverde, on a path the reader describes as open for walks and activities. Check opening times before you go.",
   story=("\"Pioppo trecentenario,\" the three-hundred-year poplar, is what people call this tree, says the reader who sent it to us from the Oasi del Lagoverde, a pocket of nature on the northern edge of Bologna at Corticella.\n\n"
          "It is a white poplar, and the reader explains why the people of the Po plain admire them. \"Il pioppo bianco viene comunemente chiamato 'Sequoia della Pianura Padana' da chi vive in questi territori,\" they write: the white poplar is commonly called the sequoia of the Po Valley by those who live here, because of the size it can reach. This one stands on a nature path inside the oasis, where, they say, the walks include hugging the tree to bring adults and children closer to its energy.\n\n"
          "The photograph looks straight up the trunk. Low down it is dark and furrowed, about three metres round by the reader's measure, and then it splits into four stems that climb together, their bark turning the chalky white that gives the tree its name, into a crown of fresh green.\n\n"
          "Our pin marks the oasis gate. The reader says the tree is on the left as you walk in."),
  )),
]

NEW_PLACES = {
 "cusop": dict(city="Cusop", country="United Kingdom",
  intro="Cusop is a small parish on the English side of the Dulas Brook, a short walk from the bookshops of Hay-on-Wye on the Welsh border. In its churchyard grows a big yew with a deeply fluted red trunk, which a reader photographed and sent to us. We do not yet know its girth or age, and we would like to.",
  meta="The churchyard yew at Cusop, by Hay-on-Wye: a fluted old trunk a reader photographed, where it stands and what we know so far."),
 "tilaran": dict(city="Tilarán", country="Costa Rica",
  intro="Tilarán is a small town in the hills of Guanacaste above Lake Arenal, in northern Costa Rica. A reader sent us two of its trees: a fig whose fused roots leave an open arch in the forest, and three figs grown into one mass above a stone wall built to save them. They know them as kapoks, so we ask readers which they are.",
  meta="Two giant figs near Tilarán in Guanacaste, Costa Rica, sent by a reader: a forest trunk with an open arch and three figs saved by a wall."),
 "balmerino": dict(city="Balmerino", country="United Kingdom",
  intro="Balmerino is a hamlet on the south shore of the Firth of Tay in Fife, around the red ruins of a thirteenth-century Cistercian abbey. In the abbey grounds grows a sweet chestnut often called the oldest tree in Fife, its long limbs now resting on props. A reader sent us its photograph.",
  meta="The sweet chestnut at Balmerino Abbey in Fife, often called the oldest tree in Fife: its age, its props, and how to find it."),
}


def main():
    leads = json.load(open("data/leads/_sightings.json"))
    by_sid = {l.get("sighting_id"): l for l in leads["leads"]}
    for spec in TREES:
        TREE_SENT[spec["sid"]] = spec["sent"]
        t = dict(spec["tree"])
        words = len(t["story"].split())
        assert 150 <= words <= 250, (t["id"], words)
        assert "—" not in t["story"], t["id"]
        path = "data/cities/%s.json" % spec["city"]
        if os.path.exists(path):
            city = json.load(open(path))
        else:
            p = NEW_PLACES[spec["city"]]
            city = {"city": p["city"], "country": p["country"], "status": "needs_curation",
                    "intro": p["intro"], "meta_description": p["meta"],
                    "hero_tree_id": t["id"], "oldest_tree_id": t["id"], "trees": []}
        if any(x["id"] == t["id"] for x in city["trees"]):
            print("skip", t["id"], "already there")
            continue
        t.setdefault("verified_sources", [])
        t["age_basis"] = "source" if t.get("age_estimate") else None
        if t["age_basis"] is None:
            del t["age_basis"]
        lead = by_sid[spec["sid"]]
        t["found_by_reader"] = {"sighting_id": spec["sid"], "date": TODAY}
        # Stories never say how a pin was obtained (no "with a GPS fix": Hidde,
        # 2026-11-20, qa check_no_gps_in_public_copy()).
        # A FIX, NOT A FINGER (Hidde, 2026-11-20): only a device fix or the
        # photograph's own location is GPS. A pin the reader dragged by hand
        # ("placed") or of unknown origin stays approximate; 31 live trees had
        # been called a confirmed GPS fix this way.
        gps = lead.get("latitude") is not None and lead.get("location_kind") in ("device", "photo")
        t["location_precision"] = "confirmed" if gps else "approximate"
        if lead.get("latitude") is not None and not gps:
            t["pin_source"] = {"kind": "reader's hand-placed pin", "sighting_id": spec["sid"], "date": TODAY,
                               "note": "The reader placed this pin on the map in the app; not a GPS fix."}
        if gps:
            t["pin_source"] = {"kind": "reader GPS fix", "sighting_id": spec["sid"], "moved_m": 0, "date": TODAY,
                               "note": "The pin marks where a reader stood to photograph this tree; the photograph was checked to show it."}
        t["curation_status"] = "flagged"
        t["verify_notes"] = ("%s session: sent by a reader (%s, %s). Photograph viewed: %s Published under the closed list "
                             "for a reader's tree (Hidde, 2026-11-17: \"we need either a gps or photo and it needs to be somewhat special\"). "
                             "The reader's own figures: name '%s', species '%s', age '%s', girth %s cm. Every figure on the page that is not "
                             "in verified_sources is stated as theirs." % (TODAY, spec["sid"], spec["sent"], spec["seen"], lead.get("name"),
                                                                         lead.get("species"), lead.get("age"), lead.get("girth_cm")))
        t["photo"] = photo(spec["src"], t["id"], t["name"], spec["user"], spec["sid"], spec["seen"])
        city["trees"].append(t)
        json.dump(city, open(path, "w"), ensure_ascii=False, indent=2)
        open(path, "a").write("\n")
        lead["status"] = "published"
        lead["judged"] = TODAY
        lead["published_as"] = "%s/%s" % (spec["city"], t["id"])
        lead["why"] = "Photograph viewed %s: %s Live as %s under the closed list (Hidde, 2026-11-17)." % (TODAY, spec["seen"], lead["published_as"])
        print("added", spec["city"], t["id"], words, "words")
    json.dump(leads, open("data/leads/_sightings.json", "w"), ensure_ascii=False, indent=1)
    open("data/leads/_sightings.json", "a").write("\n")


if __name__ == "__main__":
    main()
