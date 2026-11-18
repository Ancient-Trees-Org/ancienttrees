# DATA — the daily numbers, and what they mean

One entry per day, newest first, written automatically by the data-digest
workflow. Numbers are for the previous UTC day. While volume is tiny the
conclusion says so plainly; noise is never narrated as trend (Hidde's
standing rule, 2026-07-27).

Three event counts changed meaning on 2026-08-20, and the fall in them is the
fix rather than a regression. Until that date `app-cta`, `directions` and
`walks-app` were each counted by two click listeners at once, so one click
inserted two rows. Read any figure for those three from before 2026-08-20 as
roughly double the real number, and do not compare one across that date.
`app-cta` was worse than doubled: it also fired on the two `walks-app` links,
because those point at /app and the listener matched the href. Every other
event on the list is unaffected.

<!-- archive-index -->

**Older entries live in the archive**, moved by `scripts/archive_logs.py`, nothing deleted:

- [2026-11](archive/DATA-2026-11.md)
- [2026-10](archive/DATA-2026-10.md)
- [2026-09](archive/DATA-2026-09.md)
- [2026-08](archive/DATA-2026-08.md)
- [2026-07](archive/DATA-2026-07.md)

So absence from this file is not evidence something was never tried: `grep -ri "<place>" archive/` before concluding a hunt is new. Re-running an exhausted hunt is this project's most repeated waste.
<!-- archive-index -->
## 2026-11-17 (previous UTC day)

**Today: 79 android waitlist signups arrived yesterday (996 total); 40 tree submissions and an ambassador request for Budapest and an ambassador request for Sofia and 5 feedback reports arrived today (411 submissions of every kind in all); 19 accounts were opened today (746 accounts in all).**

**North star: 213 people have uploaded a tree or photo of their own (+200 this week); 20 of them did it on more than one day (+16).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 2763 | 49 |
| ... of which from search | every search engine | 75 | 20 |
| ... from Google | Google's recovery | 58 | 15 |
| ... from Bing | Bing | 4 | 2 |
| Website visitors who came back | people who stay | 504 | 11 |
| App downloads (first-time) | people | 5493 | 24 |
| New accounts | people | 666 | 5 |
| Phones back within 30 days | people who stay | 5 of 14 | 3 of 12 |
| Trees saved to Want to go | intent | 372 | 1 |
| Trees collected | goal 1: stood at a tree | 289 | 2 |
| Readers' contributions | data: trees, photos, corrections | 476 | 5 |
| Worth-it votes | one tap, not a contribution | 127 | 0 |
| Shares (app and web) | word of mouth, since 10-30 | 229 | 2 |
| Visits from a shared link | what sharing brings | 76 | 0 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web orange, iOS red, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | orange: 1 compliance point(s) wait for Hidde (data/compliance.json) | red: iOS build failure on main | grey: no checks wired yet |
| Open bugs | orange: 1 open | green | grey: no checks wired yet |

**Plus question** (10 answers, 1 new; 4 asked to be told; 6 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| Something else | 5 |
| A richer log of every tree you've collected | 4 |
| Download offline maps | 2 |
| Recommended tree walks for a city trip | 2 |
| Seasonal alerts when trees are at their best | 2 |

**New ambassadors yesterday: 3.** JOEY R. (Media); Калоян Р. (Sofia); daninegyeri (Budapest). Each got the mail and the badge automatically; 30 ambassadors in all (`python3 scripts/ambassador.py --list`).

**Open for you** (3; everything else handled and recorded, 7 feedback in all)

| What | Why it waits | Summary |
|---|---|---|
| feedback 1092 | your call | Three app questions (following uploaders, editing a sent description, tagging seasons); a partial suggested answer in drafts/reply-reader-1092-2026-11-17.md, two points left to check |
| feedback 786 | your call | Idea: introduce users to UK heritage-tree initiatives (Tree Council Green Monuments, Woodland Trust Ancient Tree Inventory). Outside the four verbs, so your call; no reply drafted. |
| feedback 1128 | your call | Asks how to add a tree; the app's Add a tree button does it. Suggested answer drafted for Hidde. |

Reader judge: 204 agent minutes yesterday, 204 in the last 7 days.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-11 | 11-12 | 11-13 | 11-14 | 11-15 | 11-16 | 11-17 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 0 | 3 | 5 | 3 | 1797 | 734 | 298 | **2840** |
| New accounts | 0 | 1 | 0 | 2 | 369 | 197 | 97 | **666** |
| Saves | 0 | 0 | 0 | 0 | 190 | 143 | 39 | **372** |
| Android waitlist | 0 | 0 | 0 | 0 | 1317 | 416 | 158 | **1891** |
| App downloads | 1 | 2 | 2 | 1 | 3896 | 1588 | – | **5490** |
| App deletions | 0 | – | – | – | 11 | 16 | – | **27** |
| App phones | 6 | 5 | 5 | 8 | 3563 | 1692 | 948 | **5634** |
| Trees opened in the app | 3 | 3 | 4 | 18 | 7608 | 3262 | 1844 | **12742** |
| Trees collected | 0 | 0 | 0 | 3 | 96 | 59 | 30 | **188** |
| Trees sent | 0 | 0 | 1 | 0 | 98 | 51 | 37 | **187** |
| Feedback | 0 | 0 | 0 | 0 | 29 | 23 | 15 | **67** |
| Worth-it votes | 0 | 0 | 0 | 0 | 63 | 44 | 20 | **127** |
| Ambassador asks | 0 | 0 | 0 | 0 | 5 | 3 | 2 | **10** |
| Website photos | 1 | 0 | 0 | 0 | 8 | 1 | 9 | **19** |
| iPhone photos | 0 | 0 | 0 | 3 | 149 | 87 | 128 | **367** |
| Android photos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Tree notes | 0 | 0 | 0 | 1 | 15 | 23 | 11 | **50** |
| App Store reviews | 0 | 0 | 0 | 0 | 4 | 2 | 0 | **6** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.
- App deletions count only phones that share analytics with developers, and Apple leaves out days too small to show: read it against the installs of the same day, not as a total.

**Feedback by kind** (the Feedback row above, split; their words are in the readers-in-full block)

| Kind | 11-17 | **7 days** |
|---|---:|---:|
| Pin moved | 7 | **41** |
| Written feedback | 4 | **10** |
| Report on a tree | 4 | **16** |
| Collected far from our pin | 0 | **1** |

**Trees readers sent, for you to inspect** (280 you have not looked at; ours left out)

| Judged | Reader | Tree | Where | Species | Their girth | Our verdict | Page |
|---|---|---|---|---|---:|---|---|
| 2026-11-18 | A | Moreton Bay Fig in Sydney | sydney | Moreton Bay Fig | 750 cm | publish | [syd_008](https://ancienttrees.app/sydney/moreton-bay-fig-of-rushcutters-bay-park) |
| 2026-11-18 | A | The Moreton Bay Fig of Rushcutters Bay Park | sydney | - | - | publish | [syd_008](https://ancienttrees.app/sydney/moreton-bay-fig-of-rushcutters-bay-park) |
| 2026-11-18 | B | The Camperdown Cemetery Fig | Sydney | Moreton Bay Fig (Ficus macroph | - | publish | [syd_005](https://ancienttrees.app/sydney/camperdown-cemetery-fig) |
| 2026-11-18 | C | The Sprawling Sycamore of Pawling Farm (4 photos) | Valley Forge | American Sycamore (Platanus oc | - | hold | - |
| 2026-11-18 | D | The Remnant River Red Gum of Edinburgh Garde (6 photos) | Melbourne | River Red Gum (Eucalyptus cama | - | hold | - |
| 2026-11-18 | D | The Southern Mahogany of Edinburgh Gardens (2 photos) | Melbourne | Southern Mahogany (Eucalyptus  | - | hold | - |
| 2026-11-18 | E | A tree I found (10 photos) | - | - | - | hold | - |
| 2026-11-18 | D | - | Melbourne | - | - | hold | - |
| 2026-11-18 | D | - | Melbourne | - | - | publish | [mel_019](https://ancienttrees.app/melbourne/gum-by-the-edinburgh-gardens-skate-bowl) |
| 2026-11-17 | F | Horse Chestnut Tree of Sofienbergparken | oslo | - | - | publish | [osl_005](https://ancienttrees.app/oslo/low-armed-chestnut-of-sofienbergparken) |
| 2026-11-17 | G | The Sécheron Plane | Geneva | London Plane (Platanus x aceri | - | publish | [gen_012](https://ancienttrees.app/geneva/secheron-plane) |
| 2026-11-17 | G | The Himalayan Cedar of Parc Mon Repos | Geneva | Himalayan Cedar (Cedrus deodar | - | publish | [gen_019](https://ancienttrees.app/geneva/himalayan-cedar-of-parc-mon-repos) |
| 2026-11-17 | H | Black Mulberry in London (3 photos) | london | - | - | publish | [lon_054](https://ancienttrees.app/london/burred-mulberry-of-morden-hall-park) |
| 2026-11-17 | I | The Hollow Boab of Rowing Club Road (2 photos) | Kununurra | Boab | - | publish | [knx_001](https://ancienttrees.app/kununurra/hollow-boab-of-rowing-club-road) |
| 2026-11-17 | J | Pedunculate Oak near Winterswijk (2 photos) | raesfeld | - | - | publish | [rsf_001](https://ancienttrees.app/raesfeld/erler-femeiche) |
| 2026-11-17 | K | Senegalia Galpinii (2 photos) | francistown | - | - | publish | [frt_001](https://ancienttrees.app/francistown/monkey-thorn-on-the-riverbed) |
| 2026-11-17 | L | Pioppo bianco dell'Oasi Lagoverde di Bologna | bologna | - | - | publish | [bol_014](https://ancienttrees.app/bologna/three-hundred-year-poplar-of-lagoverde) |
| 2026-11-17 | M | Balmerino Chestnut | balmerino | - | - | publish | [blm_001](https://ancienttrees.app/balmerino/balmerino-abbey-chestnut) |
| 2026-11-17 | L | Quercia del Parco Massari di Ferrara | ferrara | - | - | publish | [fer_006](https://ancienttrees.app/ferrara/oak-of-parco-massari) |
| 2026-11-17 | N | Ficus macrophylla in Buenos Aires (2 photos) | buenos-aires | - | - | publish | [bai_005](https://ancienttrees.app/buenos-aires/gomero-of-plaza-san-martin) |
| 2026-11-17 | O | Giant Ficus Tree, Bali Botanic Garden (2 photos) | melbourne | - | - | publish | [mel_018](https://ancienttrees.app/melbourne/leaning-fig-over-the-boardwalk) |
| 2026-11-17 | O | Tristaniopsis laurina in Melbourne (2 photos) | melbourne | - | - | publish | [mel_017](https://ancienttrees.app/melbourne/water-gum-that-reaches-out) |
| 2026-11-17 | P | Portuguese Oak in Lisbon (2 photos) | lisbon | - | - | publish | [lis_039](https://ancienttrees.app/lisbon/portuguese-oak-of-the-agronomy-cloister) |
| 2026-11-17 | Q | Kapok (4 photos) | tilaran | - | - | publish | [tlr_002](https://ancienttrees.app/tilaran/figs-saved-by-a-wall) |
| 2026-11-17 | R | Moreton Bay Fig in Los Angeles (2 photos) | los-angeles | - | - | publish | [lax_033](https://ancienttrees.app/los-angeles/moreton-bay-fig-by-the-white-mansion) |
| 2026-11-17 | S | European Yew near Llanfihangel-nant-Melan (2 photos) | cusop | - | - | publish | [cus_001](https://ancienttrees.app/cusop/churchyard-yew-of-cusop) |
| 2026-11-17 | T | - | powelltown | - | - | publish | [pwt_001](https://ancienttrees.app/powelltown/ada-tree) |
| 2026-11-17 | U | - | humboldt-redwoods-state-park | - | - | publish | [hum_001](https://ancienttrees.app/humboldt-redwoods-state-park/giant-tree) |
| 2026-11-17 | V | - | new-york | - | - | publish | [nyc_024](https://ancienttrees.app/new-york/ginkgo-of-the-united-order-of-tents) |
| 2026-11-17 | R | - | - | - | - | hold | - |
| 2026-11-17 | W | - | bristol | - | - | publish | [bri_003](https://ancienttrees.app/bristol/cedar-of-lebanon-at-blaise-castle) |
| 2026-11-17 | X | - | cascais | - | - | publish | [csc_001](https://ancienttrees.app/cascais/moreton-bay-fig-of-parque-marechal-carmona) |
| 2026-11-17 | Y | - | setubal | - | - | publish | [stb_009](https://ancienttrees.app/setubal/pepper-tree-that-mended-nets) |
| 2026-11-17 | R | - | los-angeles | - | - | publish | [lax_011](https://ancienttrees.app/los-angeles/huntington-rose-garden-kauri) |
| 2026-11-17 | Z | - | sydney | - | - | publish | [syd_006](https://ancienttrees.app/sydney/wishing-tree) |
| 2026-11-17 | Y | - | setubal | - | - | publish | [stb_010](https://ancienttrees.app/setubal/peruvian-pepper-of-the-jardim-de-palhais) |
| 2026-11-17 | A1 | - | cardiff | - | - | publish | [crd_012](https://ancienttrees.app/cardiff/roath-park-lake-pedunculate-oak) |
| 2026-11-17 | B1 | - | kyoto | - | - | publish | [kyo_014](https://ancienttrees.app/kyoto/grand-ginkgo-of-goo-shrine) |
| 2026-11-17 | B1 | - | kyoto | - | - | publish | [kyo_014](https://ancienttrees.app/kyoto/grand-ginkgo-of-goo-shrine) |
| 2026-11-17 | ? | - | - | - | - | hold | - |
| 2026-11-17 | R | - | - | - | - | hold | - |
| 2026-11-17 | R | - | - | - | - | hold | - |
| 2026-11-17 | C1 | - | mistley | - | - | publish | [okb_001](https://ancienttrees.app/mistley/old-knobbley) |
| 2026-11-17 | D1 | - | benmore | - | - | publish | [bmr_001](https://ancienttrees.app/benmore/benmore-redwood-avenue) |
| 2026-11-17 | Y | - | benmore | - | - | publish | [bmr_001](https://ancienttrees.app/benmore/benmore-redwood-avenue) |
| 2026-11-17 | E1 | - | derby | - | - | publish | [der_001](https://ancienttrees.app/derby/boab-prison-tree) |
| 2026-11-17 | F1 | - | vienna | - | - | publish | [vie_007](https://ancienttrees.app/vienna/sisi-platane-of-volksgarten) |
| 2026-11-17 | F1 | - | - | - | - | hold | - |
| 2026-11-17 | F1 | - | - | - | - | hold | - |
| 2026-11-17 | F1 | - | vienna | - | - | publish | [vie_007](https://ancienttrees.app/vienna/sisi-platane-of-volksgarten) |
| 2026-11-17 | G1 | - | baarn | - | - | publish | [brn_002](https://ancienttrees.app/baarn/cantonspark-giant-sequoia) |
| 2026-11-17 | T | - | sequoia-national-park | - | - | publish | [seq_003](https://ancienttrees.app/sequoia-national-park/chief-sequoyah-tree) |
| 2026-11-17 | H1 | - | aguas-de-moura | - | - | publish | [agm_001](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 2026-11-17 | H1 | - | aguas-de-moura | - | - | publish | [agm_001](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 2026-11-17 | H1 | - | aguas-de-moura | - | - | publish | [agm_001](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 2026-11-17 | L | - | poggio-renatico | - | - | publish | [pgr_001](https://ancienttrees.app/poggio-renatico/oak-of-molinazzo) |
| 2026-11-17 | I1 | - | nevern | - | - | publish | [nvn_001](https://ancienttrees.app/nevern/bleeding-yew-of-nevern) |
| 2026-11-17 | J1 | - | madrid | - | - | publish | [mad_004](https://ancienttrees.app/madrid/bald-cypresses-of-the-crystal-palace-pond) |
| 2026-11-17 | K1 | - | trollskogen | - | - | publish | [trs_001](https://ancienttrees.app/trollskogen/trolleken-the-troll-oak-of-trollskogen) |
| 2026-11-17 | K1 | - | palma-de-mallorca | - | - | publish | [plm_001](https://ancienttrees.app/palma-de-mallorca/solivera-de-cort) |
| 2026-11-17 | B1 | - | kyoto | - | - | publish | [kyo_002](https://ancienttrees.app/kyoto/land-boat-pine) |
| 2026-11-17 | L1 | River Red Gum | Orroroo | River Red Gum | - | publish | [orr_001](https://ancienttrees.app/orroroo/orroroo-giant-gum) |
| 2026-11-17 | M1 | A tree in Los Angeles | - | - | - | hold | - |
| 2026-11-17 | N1 | A tree near Copenhagen | - | - | - | hold | - |
| 2026-11-17 | O1 | Bodhi Tree near Chiang Mai | - | Bodhi Tree | - | hold | - |
| 2026-11-17 | P | Blue Jacaranda in ISA | - | Blue Jacaranda | - | hold | - |
| 2026-11-17 | P | Judas Tree in ISA | - | Judas Tree | - | hold | - |
| 2026-11-17 | Z | Queensland Kauri in Sydney | - | Queensland Kauri | - | hold | - |
| 2026-11-17 | P1 | Oriental Plane in Cambridge | - | Oriental Plane | - | hold | - |
| 2026-11-17 | L1 | River Red Gum | orroroo | River Red Gum | 1089 cm | publish | [orr_001](https://ancienttrees.app/orroroo/orroroo-giant-gum) |
| 2026-11-17 | L | Quercia del Parco Massari di Ferrara | Ferrara - Italy | Oak (Quercus sp.) | 480 cm | publish | [fer_006](https://ancienttrees.app/ferrara/oak-of-parco-massari) |
| 2026-11-17 | M | Balmerino Chestnut | Balmerino | Sweet Chestnut (Castanea sp.) | 500 cm | publish | [blm_001](https://ancienttrees.app/balmerino/balmerino-abbey-chestnut) |
| 2026-11-17 | L | Pioppo bianco dell'Oasi Lagoverde di Bologna | Bologna, Italy | Poplar (Populus sp.) | 300 cm | publish | [bol_014](https://ancienttrees.app/bologna/three-hundred-year-poplar-of-lagoverde) |
| 2026-11-17 | Q1 | Pohutukawa | te-araroa | Pohutukawa | - | publish | [tar_001](https://ancienttrees.app/te-araroa/te-waha-o-rerekohu) |
| 2026-11-17 | R1 | The Gennet Poplar (Tulip Tree) | chattahoochee-national-forest | Tulip Tree | 550 cm | publish | [gnp_001](https://ancienttrees.app/chattahoochee-national-forest/gennett-poplar) |
| 2026-11-17 | R1 | The Knightwood Oak - A tree near Mottisfont | new-forest | Pedunculate Oak | 740 cm | publish | [nwf_001](https://ancienttrees.app/new-forest/knightwood-oak) |
| 2026-11-17 | R1 | Giant Sequoias at Tall Trees Trail Walk | new-forest | Giant Sequoia | - | publish | [nwf_002](https://ancienttrees.app/new-forest/giant-sequoias-of-the-tall-trees-trail) |
| 2026-11-17 | R1 | Pecan | - | Pecan | - | hold | - |
| 2026-11-17 | R1 | Large-leaved Lime near La Tène | estavayer-le-lac | Large-leaved Lime | - | publish | [esl_001](https://ancienttrees.app/estavayer-le-lac/old-lime-of-estavayer-le-lac) |
| 2026-11-17 | R1 | Big tree trail at Cathedral Grove | meares-island | - | - | publish | [mrs_001](https://ancienttrees.app/meares-island/a-cedar-of-the-meares-island-big-tree-trail) |
| 2026-11-17 | S1 | River Red Gum near Adelaide | adelaide | River Red Gum | 800 cm | publish | [ads_003](https://ancienttrees.app/adelaide/red-gum-of-overbury-drive) |
| 2026-11-17 | Q1 | Gomero de la Recoleta | Buenos Aires | - | - | publish | [bai_001](https://ancienttrees.app/buenos-aires/gomero-de-la-recoleta) |
| 2026-11-17 | R1 | The Angel Oak (2 photos) | Charleston | - | - | publish | [chs_001](https://ancienttrees.app/charleston/angel-oak) |
| 2026-11-17 | T1 | The Dawn Redwoods of Elizabeth Street | Hobart | - | - | publish | [hob_002](https://ancienttrees.app/hobart/dawn-redwoods-of-elizabeth-street) |
| 2026-11-17 | T1 | The Norfolk Island Pine of Ingle Hall | Hobart | - | - | publish | [hob_003](https://ancienttrees.app/hobart/norfolk-island-pine-of-ingle-hall) |
| 2026-11-17 | T1 | The Bhutan Cypress of Brisbane Street | Hobart | - | - | publish | [hob_004](https://ancienttrees.app/hobart/bhutan-cypress-of-brisbane-street) |
| 2026-11-17 | U1 | The Moreton Bay Fig of Balboa Park | San Diego | - | - | publish | [sdg_001](https://ancienttrees.app/san-diego/moreton-bay-fig-of-balboa-park) |
| 2026-11-17 | Z | The Wishing Tree (2 photos) | Sydney | - | - | publish | [syd_006](https://ancienttrees.app/sydney/wishing-tree) |
| 2026-11-17 | R1 | The Big Oak (2 photos) | Thomasville | - | - | publish | [thv_001](https://ancienttrees.app/thomasville/big-oak) |
| 2026-11-17 | V1 | The Big Totara of Lillburn Monowai Road (3 photos) | Tuatapere | - | - | publish | [tua_001](https://ancienttrees.app/tuatapere/big-totara-of-lillburn-monowai-road) |
| 2026-11-17 | U1 | Ahuehuete del Jardin de San Fernando (3 photos) | Mexico City | - | - | publish | [mex_011](https://ancienttrees.app/mexico-city/el-sargento) |
| 2026-11-17 | W1 | The Great Ginkgo of Hida Kokubunji | Takayama | Ginkgo (Ginkgo biloba) | - | publish | [tky_001](https://ancienttrees.app/takayama/great-ginkgo-of-hida-kokubunji) |
| 2026-11-17 | Q1 | Te Waha o Rerekohu | Te Araroa | Pohutukawa (Metrosideros excel | - | publish | [tar_001](https://ancienttrees.app/te-araroa/te-waha-o-rerekohu) |
| 2026-11-17 | R1 | The Gennett Poplar | Chattahoochee National Forest | Tulip Tree (Liriodendron tulip | - | publish | [gnp_001](https://ancienttrees.app/chattahoochee-national-forest/gennett-poplar) |
| 2026-11-17 | R1 | The Knightwood Oak | New Forest | Pedunculate Oak (Quercus robur | - | publish | [nwf_001](https://ancienttrees.app/new-forest/knightwood-oak) |
| 2026-11-17 | R1 | The Giant Sequoias of the Tall Trees Trail | New Forest | Giant Sequoia (Sequoiadendron  | - | publish | [nwf_002](https://ancienttrees.app/new-forest/giant-sequoias-of-the-tall-trees-trail) |
| 2026-11-17 | R1 | A Cedar of the Meares Island Big Tree Trail | Meares Island | Western Redcedar (Thuja plicat | - | publish | [mrs_001](https://ancienttrees.app/meares-island/a-cedar-of-the-meares-island-big-tree-trail) |
| 2026-11-17 | R1 | The Old Lime of Estavayer-le-Lac | Estavayer-le-Lac | Large-leaved Lime (Tilia platy | - | publish | [esl_001](https://ancienttrees.app/estavayer-le-lac/old-lime-of-estavayer-le-lac) |
| 2026-11-17 | S1 | The Red Gum of Overbury Drive | Adelaide | River Red Gum (Eucalyptus cama | - | publish | [ads_003](https://ancienttrees.app/adelaide/red-gum-of-overbury-drive) |
| 2026-11-17 | R1 | Pecan | Griffin | Pecan | - | lead | - |
| 2026-11-17 | X1 | The Cosgrove House Banyan (3 photos) | Key West | Fig (Ficus sp.) | - | publish | [kyw_004](https://ancienttrees.app/key-west/cosgrove-house-banyan) |
| 2026-11-17 | X1 | Jindai-zakura (Yamataka Jindai Zakura) (2 photos) | Hokuto | Higan Cherry (Prunus subhirtel | - | publish | [hok_001](https://ancienttrees.app/hokuto/jindai-zakura-yamataka-jindai-zakura) |
| 2026-11-17 | Y1 | The Lewisham Elm | London | European White Elm (Ulmus laev | - | publish | [lon_045](https://ancienttrees.app/london/lewisham-elm) |
| 2026-11-17 | Z1 | Millennium Tree of Balete Park (2 photos) | Maria Aurora | Fig (Ficus sp.) | - | publish | [mra_001](https://ancienttrees.app/maria-aurora/millennium-tree-of-balete-park) |
| 2026-11-17 | A2 | The north door yews of St Edward's, Stow-on- | Stow-on-the-Wold | European Yew (Taxus baccata) | - | publish | [stw_001](https://ancienttrees.app/stow-on-the-wold/north-door-yews-of-st-edwards-stow-on-the-wold) |
| 2026-11-17 | B2 | The Oak of Orkin | Pamplona | Pedunculate Oak (Quercus robur | - | publish | [pam_002](https://ancienttrees.app/pamplona/oak-of-orkin) |
| 2026-11-17 | I | Boab Prison Tree | Derby | Boab (Adansonia gregorii) | - | publish | [der_001](https://ancienttrees.app/derby/boab-prison-tree) |
| 2026-11-17 | C2 | The Finsbury Circus Pagoda Tree | London | Japanese Pagoda Tree (Styphnol | - | hold | - |
| 2026-11-17 | D2 | Le Chêne de la Vierge | - | Oak | 250 cm | hold | - |
| 2026-11-17 | E2 | The Moreton Bay Fig of Curtain Square | - | - | - | hold | - |
| 2026-11-17 | C | American Sycamore at Pawling Farm in Valley  (2 photos) | - | American Sycamore | 650 cm | publish | - |
| 2026-11-17 | C2 | A London plane in Finsbury Circus Gardens | - | London Plane (Platanus x aceri | - | hold | - |
| 2026-11-17 | F2 | A dead sweet chestnut in the Kastanologos fo | - | Sweet Chestnut (Castanea sativ | - | hold | - |
| 2026-11-17 | K1 | Trolleken (the Troll Oak of Trollskogen) (3 photos) | Trollskogen | Pedunculate Oak (Quercus robur | - | publish | [trs_001](https://ancienttrees.app/trollskogen/trolleken-the-troll-oak-of-trollskogen) |
| 2026-11-17 | G2 | A tree near Edinburgh | north-berwick | - | - | publish | [nbw_001](https://ancienttrees.app/north-berwick/act-of-union-beeches-of-north-berwick-law) |
| 2026-11-17 | H2 | The Rain Tree of Bolar | mangaluru | - | - | publish | [mlr_001](https://ancienttrees.app/mangaluru/rain-tree-of-bolar) |
| 2026-11-17 | I2 | The Old Yew of Cremines (If millenaire) | Cremines | European Yew (Taxus baccata) | - | publish | [cre_001](https://ancienttrees.app/cremines/old-yew-of-cremines-if-millenaire) |
| 2026-11-17 | J2 | The Oudemanhuispoort Elm | Amsterdam | Dutch Elm (Ulmus x hollandica) | - | publish | [ams_021](https://ancienttrees.app/amsterdam/oudemanhuispoort-elm) |
| 2026-11-17 | K2 | The Totteridge Yew (2 photos) | London | European Yew (Taxus baccata) | - | publish | [lon_001](https://ancienttrees.app/london/totteridge-yew) |
| 2026-11-17 | L2 | The St Paul's Churchyard Planes | London | London Plane (Platanus x aceri | - | publish | [lon_011](https://ancienttrees.app/london/st-pauls-churchyard-planes) |
| 2026-11-17 | M2 | The Twisted Sweet Chestnut of Greenwich Park | London | Sweet Chestnut (Castanea sativ | - | publish | [lon_053](https://ancienttrees.app/london/twisted-sweet-chestnut-of-greenwich-park) |
| 2026-11-17 | M2 | Queen Elizabeth’s Oak in Greenwich Park | - | Pedunculate Oak | - | hold | - |
| 2026-11-17 | N2 | - | - | - | - | hold | - |
| 2026-11-17 | O2 | - | - | - | - | hold | - |
| 2026-11-17 | P2 | - | - | - | - | hold | - |
| 2026-11-17 | Q2 | - (2 photos) | - | - | - | hold | - |
| 2026-11-17 | W | - (2 photos) | - | - | - | hold | - |
| 2026-11-17 | ? | Romantik-Eiche | Heidelberg | - | - | lead | - |
| 2026-11-17 | ? | Bergmammutbaum im Arboretum 1 | Heidelberg | - | 765 cm | lead | - |
| 2026-11-17 | ? | Holdermanns-Eiche | Heidelberg | - | - | lead | - |
| 2026-11-17 | ? | Banyan Tree | Ho Chi Minh City | - | - | lead | - |
| 2026-11-17 | ? | It is a specimen of the species Fitzroya cup | La Unión, Chile | - | 420 cm | lead | - |
| 2026-11-17 | R2 | The Ankerwycke Yew (2 photos) | Runnymede | European Yew (Taxus baccata) | - | publish | [mdb_001](https://ancienttrees.app/maidstone/baobab-plane-of-penenden-heath) |
| 2026-11-17 | S2 | - | dublin | - | - | publish | [dub_020](https://ancienttrees.app/dublin/weeping-cedar-tunnel-of-glasnevin) |
| 2026-11-17 | U1 | - | Mexico City | - | - | publish | [mex_011](https://ancienttrees.app/mexico-city/el-sargento) |
| 2026-11-17 | S2 | - | Chiang Mai | - | - | publish | [cnx_002](https://ancienttrees.app/chiang-mai/fig-that-holds-the-stones) |
| 2026-11-17 | T2 | - | Azores | - | - | hold | - |
| 2026-11-17 | U2 | The Rhodes Bald Cypress (2 photos) | Richard Bong State Recreation Area | Bald Cypress (Taxodium distich | - | publish | [bng_001](https://ancienttrees.app/richard-bong-state-recreation-area/rhodes-bald-cypress) |
| 2026-11-17 | V2 | the Zamalek Banyan (2 photos) | cairo | Indian Banyan | - | publish | [cai_001](https://ancienttrees.app/cairo/zamalek-banyan) |
| 2026-11-17 | L2 | The Cheapside Plane | London | London Plane (Platanus x aceri | - | publish | [lon_003](https://ancienttrees.app/london/cheapside-plane) |
| 2026-11-17 | W2 | Rumskullaeken (the Kvill Oak) | Rumskulla | Pedunculate Oak (Quercus robur | - | publish | [rkm_001](https://ancienttrees.app/rumskulla/rumskullaeken-the-kvill-oak) |
| 2026-11-17 | W2 | Ekebyhovseken (2 photos) | Ekerö | Pedunculate Oak (Quercus robur | - | publish | [eke_001](https://ancienttrees.app/ekero/ekebyhovseken) |
| 2026-11-17 | X2 | Apple in Milton Keynes (2 photos) | - | Apple | - | publish | - |
| 2026-11-17 | X2 | The Leaning Apple Row of Linford Wood | Milton Keynes | Apple (Malus domestica) | - | publish | [mkn_003](https://ancienttrees.app/milton-keynes/leaning-apple-row-of-linford-wood) |
| 2026-11-17 | Y2 | Orange | - | Orange (Citrus sinensis) | - | hold | - |
| 2026-11-17 | Y2 | Monterey Pine | quito | Monterey Pine | 450 cm | publish | [uio_001](https://ancienttrees.app/quito/many-stemmed-pine-of-la-pradera) |
| 2026-11-17 | Y2 | The Many-Stemmed Pine of La Pradera | quito | - | - | publish | [uio_001](https://ancienttrees.app/quito/many-stemmed-pine-of-la-pradera) |
| 2026-11-17 | Z2 | Eastern White Pine | bangor-maine | Eastern White Pine | - | publish | [bnm_001](https://ancienttrees.app/bangor-maine/white-pine-at-the-orono-bog-boardwalk) |
| 2026-11-17 | Z2 | The White Pine at the Orono Bog Boardwalk | Bangor, Maine | Eastern White Pine (Pinus stro | - | publish | [bnm_001](https://ancienttrees.app/bangor-maine/white-pine-at-the-orono-bog-boardwalk) |
| 2026-11-17 | A3 | The Tall Tree on the Kanker Forest Track | Kanker | species not established | - | publish | [knk_001](https://ancienttrees.app/kanker/tall-tree-on-the-kanker-forest-track) |
| 2026-11-17 | B3 | The Multisecular Beech of Saint-Jammes (2 photos) | Sorèze | European Beech (Fagus sylvatic | - | publish | [sor_001](https://ancienttrees.app/soreze/multisecular-beech-of-saint-jammes) |
| 2026-11-17 | C3 | The Gunnersbury Park Black Mulberry (4 photos) | London | Black Mulberry (Morus nigra) | - | publish | [lon_030](https://ancienttrees.app/london/gunnersbury-park-black-mulberry) |
| 2026-11-17 | ? | BB61E294-5FFB-4378-960A-64DAB336FD46 | - | - | - | hold | - |
| 2026-11-17 | D3 | The National Mall Jefferson Elm | Washington DC | American Elm (Ulmus americana  | - | publish | [wdc_004](https://ancienttrees.app/washington-dc/national-mall-jefferson-elm) |
| 2026-11-17 | F | Horse Chestnut Tree of Sofienbergparken | Oslo | - | - | publish | [osl_005](https://ancienttrees.app/oslo/low-armed-chestnut-of-sofienbergparken) |
| 2026-11-17 | ? | CAA9C183-3017-433B-A1CA-09E1CAA99BF3 | - | - | - | hold | - |
| 2026-11-17 | ? | The Signal Tree (Native American'Indian Sign | Akron, Ohio, USA | - | 122 cm | lead | - |
| 2026-11-17 | E3 | Coolibah | lightning-ridge | Coolibah | 750 cm | publish | [lri_001](https://ancienttrees.app/lightning-ridge/coolibah-south-of-lightning-ridge) |
| 2026-11-17 | E3 | Coolibah near Lightning Ridge | lightning-ridge | - | - | publish | [lri_001](https://ancienttrees.app/lightning-ridge/coolibah-south-of-lightning-ridge) |
| 2026-11-17 | F3 | Strangler Fig | daintree | Strangler Fig | - | publish | [dtr_001](https://ancienttrees.app/daintree/strangler-fig-of-the-daintree-discovery-centre) |
| 2026-11-17 | F3 | The Strangler Fig of the Daintree Discovery  | daintree | - | - | publish | [dtr_001](https://ancienttrees.app/daintree/strangler-fig-of-the-daintree-discovery-centre) |
| 2026-11-16 | G3 | Pedunculate Oak (2 photos) | jelasnica | - | - | publish | [jls_001](https://ancienttrees.app/jelasnica/open-grown-oak-of-jelasnica) |
| 2026-11-16 | H3 | Ginkgo (2 photos) | dujiangyan | - | - | publish | [djy_001](https://ancienttrees.app/dujiangyan/temple-ginkgo-of-dujiangyan) |
| 2026-11-16 | R2 | Populus nigra subsp. Betulifolia near Linton (2 photos) | castlemorton | - | - | publish | [ctm_001](https://ancienttrees.app/castlemorton/leaning-black-poplar-of-hancocks-lane) |
| 2026-11-16 | I3 | The Borrowdale Yews (the Fraternal Four) | Borrowdale | European Yew (Taxus baccata) | - | publish | [bwd_001](https://ancienttrees.app/borrowdale/borrowdale-yews-the-fraternal-four) |
| 2026-11-16 | J3 | Ahuehuete de Parque Espana (2 photos) | Mexico City | Montezuma Cypress (Taxodium mu | - | publish | [mex_005](https://ancienttrees.app/mexico-city/ahuehuete-de-parque-espana) |
| 2026-11-16 | K3 | Earlysville Oak | earlysville | White Oak | - | publish | [ely_001](https://ancienttrees.app/earlysville/airport-oak-of-earlysville) |
| 2026-11-16 | V1 | Podocarpus hallii | tuatapere | Podocarpus hallii | 831 cm | publish | [tua_001](https://ancienttrees.app/tuatapere/big-totara-of-lillburn-monowai-road) |
| 2026-11-16 | V1 | Curtain Fig | yungaburra | Cunningham's Fig / White Fig | - | publish | [ybr_001](https://ancienttrees.app/yungaburra/curtain-fig-tree) |
| 2026-11-16 | L3 | European Yew near Estry | la-lande-patry | European Yew | - | publish | [llp_001](https://ancienttrees.app/la-lande-patry/hollow-yew-of-la-lande-patry) |
| 2026-11-16 | M3 | American Elm (2 photos) | - | American Elm | - | hold | - |
| 2026-11-16 | M3 | Eastern Cottonwood (2 photos) | - | Eastern Cottonwood | - | hold | - |
| 2026-11-16 | M3 | White Oak | - | White Oak | - | hold | - |
| 2026-11-16 | M3 | Northern Red Oak | - | Northern Red Oak | - | hold | - |
| 2026-11-16 | N3 | Baobab (2 photos) | mbissel | Baobab | 33 cm | publish | [mbs_001](https://ancienttrees.app/mbissel/baobab-of-mbissel) |
| 2026-11-16 | O3 | Boab | darwin | Boab | 940 cm | publish | [drw_001](https://ancienttrees.app/darwin/cavenagh-street-boab) |
| 2026-11-16 | P3 | The Becks Prime Augusta Live Oaks | Houston | - | - | publish | [hou_009](https://ancienttrees.app/houston/becks-prime-augusta-live-oaks) |
| 2026-11-16 | P3 | The Old Pecan Tree | Houston | - | - | publish | [hou_002](https://ancienttrees.app/houston/old-pecan-tree) |
| 2026-11-16 | Q3 | The Kapok Tree | Key West | - | - | publish | [kyw_003](https://ancienttrees.app/key-west/kapok-tree) |
| 2026-11-16 | R3 | Oak | kvam | Oak | - | publish | [kvm_001](https://ancienttrees.app/kvam/old-oak-at-tolo) |
| 2026-11-16 | H3 | The Champion Lodgepole Pine | big-bear-lake | Lodgepole Pine | 1100 cm | publish | [bbl_001](https://ancienttrees.app/big-bear-lake/champion-lodgepole-pine) |
| 2026-11-16 | S3 | Ancient totara tree | akaroa | - | 850 cm | publish | [akr_001](https://ancienttrees.app/akaroa/giant-totara-of-montgomery-park) |
| 2026-11-16 | T3 | 1500 old olive tree | kastela | Olive (Olea sp.) | 650 cm | publish | [cdl_003](https://ancienttrees.app/kastela/mastrinka-the-olive-of-kastel-stafilic) |
| 2026-11-16 | T3 | Linden tree next to the pond | - | Lime (Tilia sp.) | 166 cm | hold | - |
| 2026-11-16 | U3 | The Aogiri of Peace Memorial Park | Hiroshima | Chinese Parasol Tree (Firmiana | - | publish | [hir_005](https://ancienttrees.app/hiroshima/aogiri-of-peace-memorial-park) |
| 2026-11-16 | V3 | The Embracing Fig of the Giardini Reali | Palermo | Moreton Bay Fig (Ficus macroph | - | publish | [pal_016](https://ancienttrees.app/palermo/embracing-fig-of-the-giardini-reali) |
| 2026-11-16 | W3 | Enchanted Balete Tree of Lazi | Siquijor | Fig (Ficus sp.) | - | publish | [sqj_001](https://ancienttrees.app/siquijor/enchanted-balete-tree-of-lazi) |
| 2026-11-16 | X3 | El Árbol del Tule | Santa María del Tule | Montezuma Cypress (Taxodium mu | - | publish | [tul_001](https://ancienttrees.app/santa-maria-del-tule/el-arbol-del-tule) |
| 2026-11-16 | Y3 | Elleholmseken (The Oak of Elleholm) | Elleholm | Pedunculate Oak (Quercus robur | - | publish | [elh_001](https://ancienttrees.app/elleholm/elleholmseken-the-oak-of-elleholm) |
| 2026-11-16 | U3 | The Willow Nearest the Hypocentre | Hiroshima | Weeping Willow (Salix babyloni | - | publish | [hir_001](https://ancienttrees.app/hiroshima/willow-nearest-the-hypocentre) |
| 2026-11-16 | X3 | The Fortingall Yew | Fortingall | European Yew (Taxus baccata) | - | publish | [for_001](https://ancienttrees.app/fortingall/fortingall-yew) |
| 2026-11-16 | H3 | General Sherman Tree | Sequoia National Park | Giant Sequoia (Sequoiadendron  | - | publish | [seq_001](https://ancienttrees.app/sequoia-national-park/general-sherman-tree) |
| 2026-11-16 | H3 | Lincoln Tree | Sequoia National Park | Giant Sequoia (Sequoiadendron  | - | publish | [seq_004](https://ancienttrees.app/sequoia-national-park/lincoln-tree) |
| 2026-11-16 | Z3 | The Sacred Olive Tree of the Acropolis | Athens | Olive (Olea europaea) | - | publish | [ath_001](https://ancienttrees.app/athens/sacred-olive-tree-of-the-acropolis) |
| 2026-11-16 | A4 | The Plaited Birch of Brocton | Cannock Chase | Birch (Betula sp.) | - | publish | [cnk_004](https://ancienttrees.app/cannock-chase/plaited-birch-of-brocton) |
| 2026-11-16 | B4 | The Fig of Neal Macrossan Park | Brisbane | Fig (Ficus sp.) | - | publish | [bne_022](https://ancienttrees.app/brisbane/fig-of-neal-macrossan-park) |
| 2026-11-16 | U | The Bodhi Tree of Lumbini | Lumbini | Bodhi Tree (Ficus religiosa) | - | publish | [lmb_001](https://ancienttrees.app/lumbini/bodhi-tree-of-lumbini) |
| 2026-11-16 | K3 | The Airport Oak of Earlysville | Earlysville | Oak (Quercus sp.) | - | publish | [ely_001](https://ancienttrees.app/earlysville/airport-oak-of-earlysville) |
| 2026-11-16 | V1 | The Curtain Fig Tree | Yungaburra | Cunningham's Fig / White Fig ( | - | publish | [ybr_001](https://ancienttrees.app/yungaburra/curtain-fig-tree) |
| 2026-11-16 | L3 | The Hollow Yew of La Lande-Patry | La Lande-Patry | European Yew (Taxus baccata) | - | publish | [llp_001](https://ancienttrees.app/la-lande-patry/hollow-yew-of-la-lande-patry) |
| 2026-11-16 | N3 | The Baobab of Mbissel | Mbissel | Baobab (Adansonia digitata) | - | publish | [mbs_001](https://ancienttrees.app/mbissel/baobab-of-mbissel) |
| 2026-11-16 | N3 | The Sagole Baobab | Sagole | Baobab (Adansonia digitata) | - | publish | [sgl_001](https://ancienttrees.app/sagole/sagole-baobab) |
| 2026-11-16 | O3 | The Cavenagh Street Boab | Darwin | Boab (Adansonia gregorii) | - | publish | [drw_001](https://ancienttrees.app/darwin/cavenagh-street-boab) |
| 2026-11-16 | R3 | The Old Oak at Tolo | Kvam | Oak (Quercus sp.) | - | publish | [kvm_001](https://ancienttrees.app/kvam/old-oak-at-tolo) |
| 2026-11-16 | C4 | Blackbutt | middle-brother-national-park | Blackbutt | 1100 cm | publish | [mbr_001](https://ancienttrees.app/middle-brother-national-park/blackbutt-of-bird-tree-road) |
| 2026-11-16 | C4 | middle-brother-national-park/mbr_001 The Bla | middle-brother-national-park | Blackbutt | 1100 cm | publish | [mbr_001](https://ancienttrees.app/middle-brother-national-park/blackbutt-of-bird-tree-road) |
| 2026-11-16 | D4 | nottingham/ntm_001 The Arbour Oak of Wollato | nottingham | Oak (Quercus sp.) | 700 cm | publish | [ntm_001](https://ancienttrees.app/nottingham/arbour-oak-of-wollaton-park) |
| 2026-11-16 | L | poggio-renatico/pgr_001 The Oak of Molinazzo | poggio-renatico | Oak (Quercus sp.) | 460 cm | publish | [pgr_001](https://ancienttrees.app/poggio-renatico/oak-of-molinazzo) |
| 2026-11-16 | H3 | big-bear-lake/bbl_001 The Champion Lodgepole | big-bear-lake | Lodgepole Pine | 1100 cm | publish | [bbl_001](https://ancienttrees.app/big-bear-lake/champion-lodgepole-pine) |
| 2026-11-16 | E4 | gilgandra/gil_001 The Grapevine of the Royal | gilgandra | Grape | 300 cm | publish | [gil_001](https://ancienttrees.app/gilgandra/grapevine-of-the-royal-hotel) |
| 2026-11-16 | S3 | akaroa/akr_001 The Giant Tōtara of Montgomer | akaroa | - | 850 cm | publish | [akr_001](https://ancienttrees.app/akaroa/giant-totara-of-montgomery-park) |
| 2026-11-16 | T3 | kastela/cdl_003 Mastrinka, the Olive of Kašt | kastela | Olive (Olea sp.) | 650 cm | publish | [cdl_003](https://ancienttrees.app/kastela/mastrinka-the-olive-of-kastel-stafilic) |
| 2026-11-16 | F4 | Phytolacca dioica | essaouira | Phytolacca dioica | 1000 cm | publish | [ess_001](https://ancienttrees.app/essaouira/ombu-of-the-essaouira-medina) |
| 2026-11-16 | F4 | The Ombu of the Essaouira Medina | Essaouira | Ombu (Phytolacca dioica) | 1000 cm | publish | [ess_001](https://ancienttrees.app/essaouira/ombu-of-the-essaouira-medina) |
| 2026-11-16 | G4 | Prince Eugen's Oak | - | Oak (Quercus sp.) | - | hold | - |
| 2026-11-16 | H4 | A tree near Helmond | - | - | - | hold | - |
| 2026-11-16 | I4 | The Tassili cypress | Tassili Plateau, Algeria | Cypress (Cupressus sp.) | - | hold | - |
| 2026-11-16 | R3 | Pendulate Oak | Norheimsund | Oak (Quercus sp.) | 706 cm | publish | - |
| 2026-11-16 | J4 | Yew | Vigeois | Yew (Taxus sp.) | - | publish | - |
| 2026-11-16 | K4 | - | kamakura | broad-leaved evergreen, knobbl | - | publish | [kmk_007](https://ancienttrees.app/kamakura/tabunoki-of-hasedera) |
| 2026-11-16 | J1 | - | bilbao | bare spreading crown, dark fur | - | publish | [bil_004](https://ancienttrees.app/bilbao/centenary-horse-chestnut-of-parque-de-dona-casilda) |
| 2026-11-16 | L4 | - | - | ridged furrowed bark, spreadin | - | hold | - |
| 2026-11-16 | L4 | - | boston | ginkgo crown, fan leaves | - | publish | [bos_051](https://ancienttrees.app/boston/public-garden-ginkgo) |
| 2026-11-16 | W | - | bristol | giant sequoia, fibrous red bar | - | publish | [bri_018](https://ancienttrees.app/bristol/wellingtonias-by-the-lower-pond-combe-dingle) |
| 2026-11-16 | L4 | - | boston | deeply ridged oak bark, spread | - | publish | [bos_052](https://ancienttrees.app/boston/public-garden-bur-oak) |
| 2026-11-16 | Y | - | setubal | melaleuca, low twisted domes | - | publish | [stb_004](https://ancienttrees.app/setubal/melaleuca-that-grows-sideways) |
| 2026-11-16 | L4 | - | boston | compound leaves, fissured trun | - | publish | [bos_047](https://ancienttrees.app/boston/public-garden-pagoda-tree) |
| 2026-11-16 | J1 | - | bilbao | feathery russet foliage, buttr | - | publish | [bil_002](https://ancienttrees.app/bilbao/bald-cypress-of-deusto) |
| 2026-11-16 | M4 | - | llanerfyl | yew, red fluted trunks | - | publish | [lef_001](https://ancienttrees.app/llanerfyl/llanerfyl-yew) |
| 2026-11-16 | N4 | - | olympic-national-park | Sitka spruce bark and crown | - | publish | [oly_004](https://ancienttrees.app/olympic-national-park/quinault-big-spruce) |
| 2026-11-16 | N4 | - | olympic-national-park | spruce foliage on a root-held  | - | publish | [oly_003](https://ancienttrees.app/olympic-national-park/tree-of-life) |
| 2026-11-16 | I3 | - | borrowdale | yew needles, arils, fluted tru | - | publish | [bwd_001](https://ancienttrees.app/borrowdale/borrowdale-yews-the-fraternal-four) |
| 2026-11-16 | W | - | bristol | oak branching, lobed leaves | - | publish | [bri_016](https://ancienttrees.app/bristol/bundle-planted-sessile-oak-bishops-knoll) |
| 2026-11-16 | O4 | A tree near Westonbirt Arboretum | - | - | - | hold | - |
| 2026-11-16 | P4 | Leccio (Quercus Ilex) nel piazzale della sta | San Bonifacio | Oak (Quercus sp.) | 265 cm | publish | - |
| 2026-11-16 | Q4 | The Lietzensee Plane | Berlin | London Plane (Platanus x aceri | - | publish | [ber_016](https://ancienttrees.app/berlin/lietzensee-plane) |
| 2026-11-16 | J1 | The Plane Trees of Jardines de Albia | Bilbao | London Plane (Platanus x aceri | - | publish | [bil_001](https://ancienttrees.app/bilbao/plane-trees-of-jardines-de-albia) |
| 2026-11-16 | J1 | The Centenary Trees of Parque de la Miserico | Bilbao | Canary Island Date Palm (Phoen | - | publish | [bil_003](https://ancienttrees.app/bilbao/centenary-trees-of-parque-de-la-misericordia) |
| 2026-11-16 | R4 | The Great Plane of Brunswick Square | London | London Plane (Platanus x aceri | - | publish | [lon_016](https://ancienttrees.app/london/great-plane-of-brunswick-square) |
| 2026-11-16 | S4 | The Huff Creek Road White Pine | Nicolet National Forest | Eastern White Pine (Pinus stro | - | publish | [nfw_001](https://ancienttrees.app/nicolet-national-forest/huff-creek-road-white-pine) |
| 2026-11-16 | ? | Cat Island Bald Cypress | St Francis ville, LA | - | 1650 cm | lead | - |
| 2026-11-16 | ? | The 180-year-old Moreton Bay Fig at Arderne  | Cape Town | - | 1120 cm | lead | - |
| 2026-11-16 | ? | The 800-year-old Big Tree in Tsitsikamma | Stormsrivier, the Garden Route, South Africa | - | 900 cm | lead | - |
| 2026-11-16 | ? | The Famous Nossob Camel Thorn Tree | Kgalagadi Transfrontier Park | - | - | lead | - |
| 2026-11-16 | ? | South Africa's largest indigenous tree! The  | Near Sagole village, east of Tshipise, Limpopo | - | 34 cm | publish | - |
| 2026-11-16 | ? | Chestnut "Miraglia" | Camaldoli (Ar) - Italy | - | 2000 cm | lead | - |
| 2026-11-15 | T4 | Endangered Dawn Redwood in Holborn, legal di | - | Dawn Redwood | - | hold | - |
| 2026-11-15 | T2 | Giant Australian Rubber Tree of Jardim Anton | Azores | Moreton Bay Fig (Ficus macroph | - | hold | - |
| 2026-11-15 | U4 | Deans Oak | - | - | 1200 cm | hold | - |
| 2026-11-15 | V4 | A giant sequoia | - | - | - | lead | - |
| 2026-11-15 | W4 | Scots Pine in Dunkeld | - | Scots Pine | 660 cm | hold | - |
| 2026-11-15 | X4 | Tree in Waitangi | - | - | - | hold | - |
| 2026-11-15 | Y4 | The Great Oriental Plane Tree, Emmanuel Coll | - | - | 478 cm | hold | - |
| 2026-11-15 | Q2 | - | - | - | - | hold | - |
| 2026-11-15 | Z4 | - | - | - | - | hold | - |
| 2026-11-15 | A5 | - | - | - | - | hold | - |
| 2026-11-15 | A5 | - | - | - | - | hold | - |
| 2026-11-15 | A5 | - | - | - | - | hold | - |
| 2026-11-15 | B5 | - | - | - | - | hold | - |
| 2026-11-15 | C5 | The Witch Tree of Fanal | Madeira | Til / Stinkwood (Ocotea foeten | - | hold | - |
| 2026-11-15 | U | Marton Oak | - | Pedunculate Oak | - | hold | - |
| 2026-11-15 | D5 | Malmö | - | - | - | hold | - |
| 2026-11-15 | E5 | Blue Jacaranda in Melbourne | - | Blue Jacaranda | - | hold | - |
| 2026-11-15 | F5 | English Hawthorn | - | English Hawthorn (Crataegus la | 50 cm | lead | - |
| 2026-11-15 | G5 | Wistman's Wood | Dartmoor | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-15 | H5 | Grimston's Oak | London | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-15 | G5 | The Crom Yews | Crom | European Yew (Taxus baccata) | - | hold | - |
| 2026-11-15 | G5 | The Dawn Redwood by the Kelvin Statue (2 photos) | Belfast | Dawn Redwood (Metasequoia glyp | - | hold | - |
| 2026-11-15 | G5 | S'Olivera de Cort | Palma de Mallorca | Olive (Olea europaea) | - | hold | - |
| 2026-11-15 | S2 | A tree near Chiang Mai | - | - | - | hold | - |
| 2026-11-15 | L | Il cipresso calvo di Villa Smeraldi | - | Cypress (Cupressus sp.) | - | hold | - |
| 2026-11-15 | G5 | The Boole Library Redwoods | Cork | Redwood | - | hold | - |
| 2026-11-15 | ? | Oak tree, Quercus Robur. | Bagni di Lusnizza, Udine | - | 454 cm | lead | - |
| 2026-11-15 | ? | Oliveira de Mouchão, oldest olive tree in Po | Mouriscas | - | - | lead | - |
| 2026-11-15 | ? | 71F93157-AEF9-41A4-AF61-E1AD9755F9B1 | - | - | - | hold | - |
| 2026-11-15 | ? | 24FDCCB3-A454-4556-8169-2BAD2FB36ABD | - | - | - | hold | - |
| 2026-11-15 | ? | C7962FE1-14DB-407A-B62F-CFA617580655 | - | - | - | hold | - |
| 2026-11-18 | Z | The Bidwill Kauri Pine | Sydney | Queensland Kauri (Agathis robu | - | hold | - |
| 2026-11-18 | D | The Finer Holm Oak of Edinburgh Gardens | Melbourne | Holm Oak (Quercus ilex) | - | publish | [mel_001](https://ancienttrees.app/melbourne/finer-holm-oak-of-edinburgh-gardens) |
| 2026-11-18 | I5 | The Shiba Toshogu Ginkgo | Tokyo | Ginkgo (Ginkgo biloba) | - | publish | [tok_005](https://ancienttrees.app/tokyo/shiba-toshogu-ginkgo) |
- From 139 readers: reader R1 14, reader L 7, reader D 5, reader G5 5, reader H3 5, reader J1 5, reader R 5, reader F1 4, reader L4 4, reader M3 4, reader V1 4, reader W 4, reader Y 4, reader Z 4, reader A5 3, reader B1 3, reader H1 3, reader K1 3, reader N3 3, reader P 3, reader Q1 3, reader R3 3, reader S2 3, reader T1 3, reader T3 3, reader U 3, reader U1 3, reader Y2 3, reader A 2, reader C 2, reader C2 2, reader C4 2, reader E3 2, reader F 2, reader F3 2, reader F4 2, reader G 2, reader I 2, reader I3 2, reader K3 2, reader L1 2, reader L2 2, reader L3 2, reader M 2, reader M2 2, reader N4 2, reader O 2, reader O3 2, reader P3 2, reader Q2 2, reader R2 2, reader S1 2, reader S3 2, reader T 2, reader T2 2, reader U3 2, reader W2 2, reader X1 2, reader X2 2, reader X3 2, reader Z2 2, reader A1 1, reader A2 1, reader A3 1, reader A4 1, reader B 1, reader B2 1, reader B3 1, reader B4 1, reader B5 1, reader C1 1, reader C3 1, reader C5 1, reader D1 1, reader D2 1, reader D3 1, reader D4 1, reader D5 1, reader E 1, reader E1 1, reader E2 1, reader E4 1, reader E5 1, reader F2 1, reader F5 1, reader G1 1, reader G2 1, reader G3 1, reader G4 1, reader H 1, reader H2 1, reader H4 1, reader H5 1, reader I1 1, reader I2 1, reader I4 1, reader I5 1, reader J 1, reader J2 1, reader J3 1, reader J4 1, reader K 1, reader K2 1, reader K4 1, reader M1 1, reader M4 1, reader N 1, reader N1 1, reader N2 1, reader O1 1, reader O2 1, reader O4 1, reader P1 1, reader P2 1, reader P4 1, reader Q 1, reader Q3 1, reader Q4 1, reader R4 1, reader S 1, reader S4 1, reader T4 1, reader U2 1, reader U4 1, reader V 1, reader V2 1, reader V3 1, reader V4 1, reader W1 1, reader W3 1, reader W4 1, reader X 1, reader X4 1, reader Y1 1, reader Y3 1, reader Y4 1, reader Z1 1, reader Z3 1, reader Z4 1.
- Photographs and the readers' own words: `python3 scripts/inspect_readers.py` (a local page, never in this public file). Your answer goes in with `python3 scripts/judgement.py --feedback <id> "..."`.

**Waiting for you** (what the runs left for you since 2026-11-17)

- 246 email addresses ready to mail (archive 0, nature 9, guide 8, press 135, source 58, council 16, society 7, tourism 5, other 5, garden 3); **the night run found no new contacts in two days**
- a suggested reply is in drafts/reply-reader-1000077-2026-11-17.md.
- drafts/reply-reader-1115-2026-11-17.md asks the Akron reader whether the tree can be seen from open ground.
- 9 Yahoo-family sign-ups from 11-15/16 are still not in, after our two mails failed them.
- the daily task "publish-held-trees-daily" can be switched off under Scheduled; write passes put trees straight into the app, so nothing waits for it.
- two feedback rows wait for your call (786 idea, 849 reply draft); five reports the judge left open are listed under "Open for you".
- goes as reply_text with outcome `holds` on his yes.
- readers cannot find how to add a tree on the web, or a photo from a computer (three Plus answers say so); PRODUCT_TODO.md item 19, a design to show you first.
- the Major Oak as a monument is parked for your call: it died in 2026 (RSPB), so the dead-tree rule keeps it off; PRODUCT_TODO.md item 20.

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-17 | J5 | The Dawn Redwood of Kew Gardens | Toronto | a reader's photograph, published | [live](https://ancienttrees.app/toronto/dawn-redwood-of-kew-gardens) |
| 11-17 | G2 | The Act of Union Beeches of North Berwick Law | North Berwick | a reader's photograph, published | [live](https://ancienttrees.app/north-berwick/act-of-union-beeches-of-north-berwick-law) |
| 11-17 | S2 | The Hollow Lime of Pabaži | Saulkrasti | a reader's photograph, published | [live](https://ancienttrees.app/saulkrasti/hollow-lime-of-pabazi) |
| 11-17 | S2 | The Great Ash of the Bison's Rib Trail | Białowieża | a reader's photograph, published | [live](https://ancienttrees.app/bialowieza/great-ash-of-the-bisons-rib-trail) |
| 11-16 | A4 | The Plaited Birch of Brocton | Cannock Chase | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/cannock-chase/plaited-birch-of-brocton) |
| 11-16 | B4 | The Fig of Neal Macrossan Park | Brisbane | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/brisbane/fig-of-neal-macrossan-park) |
| 11-16 | U | The Bodhi Tree of Lumbini | Lumbini | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/lumbini/bodhi-tree-of-lumbini) |
| 11-16 | K3 | The Airport Oak of Earlysville | Earlysville | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/earlysville/airport-oak-of-earlysville) |
| 11-16 | V1 | The Big Totara of Lillburn Monowai Road | Tuatapere | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tuatapere/big-totara-of-lillburn-monowai-road) |
| 11-16 | V1 | The Curtain Fig Tree | Yungaburra | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/yungaburra/curtain-fig-tree) |
| 11-16 | L3 | The Hollow Yew of La Lande-Patry | La Lande-Patry | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/la-lande-patry/hollow-yew-of-la-lande-patry) |
| 11-16 | N3 | The Baobab of Mbissel | Mbissel | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mbissel/baobab-of-mbissel) |
| 11-16 | N3 | The Sagole Baobab | Sagole | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sagole/sagole-baobab) |
| 11-17 | H3 | The Temple Ginkgo of Dujiangyan | Dujiangyan | a reader's photograph, published | [live](https://ancienttrees.app/dujiangyan/temple-ginkgo-of-dujiangyan) |
| 11-16 | O3 | The Cavenagh Street Boab | Darwin | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/darwin/cavenagh-street-boab) |
| 11-16 | P3 | The Becks Prime Augusta Live Oaks | Houston | a reader's photograph, published | [live](https://ancienttrees.app/houston/becks-prime-augusta-live-oaks) |
| 11-16 | P3 | The Old Pecan Tree | Houston | a reader's photograph, published | [live](https://ancienttrees.app/houston/old-pecan-tree) |
| 11-16 | Q3 | The Kapok Tree | Key West | a reader's photograph, published | [live](https://ancienttrees.app/key-west/kapok-tree) |
| 11-16 | U2 | The Rhodes Bald Cypress | Richard Bong State Recreation Area | a reader's photograph, published | [live](https://ancienttrees.app/richard-bong-state-recreation-area/rhodes-bald-cypress) |
| 11-16 | I3 | The Borrowdale Yews (the Fraternal Four) | Borrowdale | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/borrowdale/borrowdale-yews-the-fraternal-four) |
| 11-16 | K5 | The Angel Oak | Charleston | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/charleston/angel-oak) |
| 11-16 | J3 | Ahuehuete de Parque Espana | Mexico City | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mexico-city/ahuehuete-de-parque-espana) |
| 11-16 | J3 | Ahuehuete de Parque Espana | Mexico City | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mexico-city/ahuehuete-de-parque-espana) |
| 11-17 | R2 | The Leaning Black Poplar of Hancocks Lane | Castlemorton | a reader's photograph, published | [live](https://ancienttrees.app/castlemorton/leaning-black-poplar-of-hancocks-lane) |
| 11-16 | R3 | The Old Oak at Tolo | Kvam | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kvam/old-oak-at-tolo) |
| 11-16 | U3 | The Aogiri of Peace Memorial Park | Hiroshima | a reader's photograph, published | [live](https://ancienttrees.app/hiroshima/aogiri-of-peace-memorial-park) |
| 11-16 | V3 | The Embracing Fig of the Giardini Reali | Palermo | a reader's photograph, published | [live](https://ancienttrees.app/palermo/embracing-fig-of-the-giardini-reali) |
| 11-16 | W3 | Enchanted Balete Tree of Lazi | Siquijor | a reader's photograph, published | [live](https://ancienttrees.app/siquijor/enchanted-balete-tree-of-lazi) |
| 11-16 | L5 | Millennium Tree of Balete Park | Maria Aurora | a reader's photograph, published | [live](https://ancienttrees.app/maria-aurora/millennium-tree-of-balete-park) |
| 11-16 | X3 | El Árbol del Tule | Santa María del Tule | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/santa-maria-del-tule/el-arbol-del-tule) |
| 11-16 | Y3 | Elleholmseken (The Oak of Elleholm) | Elleholm | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/elleholm/elleholmseken-the-oak-of-elleholm) |
| 11-16 | U3 | The Willow Nearest the Hypocentre | Hiroshima | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/hiroshima/willow-nearest-the-hypocentre) |
| 11-16 | X3 | The Fortingall Yew | Fortingall | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/fortingall/fortingall-yew) |
| 11-16 | H3 | General Sherman Tree | Sequoia National Park | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sequoia-national-park/general-sherman-tree) |
| 11-16 | H3 | Lincoln Tree | Sequoia National Park | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sequoia-national-park/lincoln-tree) |
| 11-16 | Z3 | The Sacred Olive Tree of the Acropolis | Athens | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/athens/sacred-olive-tree-of-the-acropolis) |
| 11-16 | M5 | The Dawn Redwood of Préfargier | La Tène | a reader's photograph, published | [live](https://ancienttrees.app/la-tene/dawn-redwood-of-prefargier) |
| 11-16 | M5 | The Weeping Beeches of Préfargier | La Tène | a reader's photograph, published | [live](https://ancienttrees.app/la-tene/weeping-beeches-of-prefargier) |
| 11-16 | M5 | The Large-leaved Lime of Préfargier | La Tène | a reader's photograph, published | [live](https://ancienttrees.app/la-tene/large-leaved-lime-of-prefargier) |
| 11-16 | Y3 | Elleholmseken (The Oak of Elleholm) | Elleholm | a reader's photograph, published | [live](https://ancienttrees.app/elleholm/elleholmseken-the-oak-of-elleholm) |
| 11-16 | N5 | The Pollard Oaks of Wantisden | Wantisden | a reader's photograph, published | [live](https://ancienttrees.app/wantisden/pollard-oaks-of-wantisden) |
| 11-16 | R2 | The Baobab Plane of Penenden Heath | Maidstone | a reader's photograph, published | [live](https://ancienttrees.app/maidstone/baobab-plane-of-penenden-heath) |
| 11-16 | R2 | The Oak of Clingoe Hill | Colchester | a reader's photograph, published | [live](https://ancienttrees.app/colchester/oak-of-clingoe-hill) |
| 11-16 | O5 | The Library Ginkgo of Carmarthen | Carmarthen | a reader's photograph, published | [live](https://ancienttrees.app/carmarthen/library-ginkgo-of-carmarthen) |
| 11-16 | P5 | The Methuselah Tree | Woodside | a reader's photograph, published | [live](https://ancienttrees.app/woodside/methuselah-tree) |
| 11-16 | A4 | The Doveridge Yew | Doveridge | a reader's photograph, published | [live](https://ancienttrees.app/doveridge/doveridge-yew) |
| 11-16 | Q5 | The Crowhurst Yew | Crowhurst | a reader's photograph, published | [live](https://ancienttrees.app/crowhurst/crowhurst-yew) |
| 11-16 | M2 | The Twisted Sweet Chestnut of Greenwich Park | London | a reader's photograph, published | [live](https://ancienttrees.app/london/twisted-sweet-chestnut-of-greenwich-park) |
| 11-16 | Q5 | The Bowthorpe Oak | Bowthorpe | a reader's photograph, published | [live](https://ancienttrees.app/bowthorpe/bowthorpe-oak) |
| 11-17 | G3 | The Open-Grown Oak of Jelašnica | Jelašnica | a reader's photograph, published | [live](https://ancienttrees.app/jelasnica/open-grown-oak-of-jelasnica) |
| 11-16 | K4 | The Tabunoki of Hasedera | Kamakura | a reader's photograph, published | [live](https://ancienttrees.app/kamakura/tabunoki-of-hasedera) |
| 11-16 | J1 | The Centenary Horse Chestnut of Parque de Doña Casilda | Bilbao | a reader's photograph, published | [live](https://ancienttrees.app/bilbao/centenary-horse-chestnut-of-parque-de-dona-casilda) |
| 11-16 | L4 | The Public Garden Ginkgo | Boston | a reader's photograph, published | [live](https://ancienttrees.app/boston/public-garden-ginkgo) |
| 11-16 | W | The Wellingtonias by the Lower Pond, Combe Dingle | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/wellingtonias-by-the-lower-pond-combe-dingle) |
| 11-16 | L4 | The Public Garden Bur Oak | Boston | a reader's photograph, published | [live](https://ancienttrees.app/boston/public-garden-bur-oak) |
| 11-16 | Y | The Melaleuca That Grows Sideways | Setubal | a reader's photograph, published | [live](https://ancienttrees.app/setubal/melaleuca-that-grows-sideways) |
| 11-16 | L4 | The Public Garden Pagoda Tree | Boston | a reader's photograph, published | [live](https://ancienttrees.app/boston/public-garden-pagoda-tree) |
| 11-16 | J1 | The Bald Cypress of Deusto | Bilbao | a reader's photograph, published | [live](https://ancienttrees.app/bilbao/bald-cypress-of-deusto) |
| 11-16 | M4 | Llanerfyl Yew | Llanerfyl | a reader's photograph, published | [live](https://ancienttrees.app/llanerfyl/llanerfyl-yew) |
| 11-16 | N4 | The Quinault Big Spruce | Olympic National Park | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/olympic-national-park/quinault-big-spruce) |
| 11-16 | N4 | The Tree of Life | Olympic National Park | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/olympic-national-park/tree-of-life) |
| 11-16 | I3 | The Borrowdale Yews (the Fraternal Four) | Borrowdale | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/borrowdale/borrowdale-yews-the-fraternal-four) |
| 11-16 | W | The Bundle-planted Sessile Oak, Bishops Knoll | Bristol | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/bristol/bundle-planted-sessile-oak-bishops-knoll) |
| 11-16 | E4 | The Grapevine of the Royal Hotel | Gilgandra | a reader's photograph, published | [live](https://ancienttrees.app/gilgandra/grapevine-of-the-royal-hotel) |
| 11-16 | H3 | The Champion Lodgepole Pine | Big Bear Lake | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/big-bear-lake/champion-lodgepole-pine) |
| 11-16 | C4 | The Blackbutt of Bird Tree Road | Middle Brother National Park | a reader's photograph, published | [live](https://ancienttrees.app/middle-brother-national-park/blackbutt-of-bird-tree-road) |
| 11-16 | J1 | The Centenary Trees of Parque de la Misericordia | Bilbao | a reader's photograph, published | [live](https://ancienttrees.app/bilbao/centenary-trees-of-parque-de-la-misericordia) |
| 11-16 | S4 | The Huff Creek Road White Pine | Nicolet National Forest | a reader's photograph, published | [live](https://ancienttrees.app/nicolet-national-forest/huff-creek-road-white-pine) |
| 11-16 | J1 | The Plane Trees of Jardines de Albia | Bilbao | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/bilbao/plane-trees-of-jardines-de-albia) |
| 11-16 | R4 | The Great Plane of Brunswick Square | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/great-plane-of-brunswick-square) |
| 11-16 | Q4 | The Lietzensee Plane | Berlin | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/berlin/lietzensee-plane) |
| 11-17 | T | The Ada Tree | Powelltown | a reader's photograph, published | [live](https://ancienttrees.app/powelltown/ada-tree) |
| 11-17 | U | The Giant Tree | Humboldt Redwoods State Park | a reader's photograph, published | [live](https://ancienttrees.app/humboldt-redwoods-state-park/giant-tree) |
| 11-17 | V | The Ginkgo of the United Order of Tents | New York | a reader's photograph, published | [live](https://ancienttrees.app/new-york/ginkgo-of-the-united-order-of-tents) |
| 11-17 | W | The Cedar of Lebanon at Blaise Castle | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/cedar-of-lebanon-at-blaise-castle) |
| 11-17 | X | The Moreton Bay Fig of Parque Marechal Carmona | Cascais | a reader's photograph, published | [live](https://ancienttrees.app/cascais/moreton-bay-fig-of-parque-marechal-carmona) |
| 11-17 | Y | The Pepper Tree That Mended Nets | Setubal | a reader's photograph, published | [live](https://ancienttrees.app/setubal/pepper-tree-that-mended-nets) |
| 11-17 | R | The Huntington Rose Garden Kauri | Los Angeles | a reader's photograph, published | [live](https://ancienttrees.app/los-angeles/huntington-rose-garden-kauri) |
| 11-17 | Z | The Wishing Tree | Sydney | a reader's photograph, published | [live](https://ancienttrees.app/sydney/wishing-tree) |
| 11-17 | Y | The Peruvian Pepper of the Jardim de Palhais | Setubal | a reader's photograph, published | [live](https://ancienttrees.app/setubal/peruvian-pepper-of-the-jardim-de-palhais) |
| 11-17 | A1 | Roath Park Lake Pedunculate Oak | Cardiff | a reader's photograph, published | [live](https://ancienttrees.app/cardiff/roath-park-lake-pedunculate-oak) |
| 11-17 | B1 | The Grand Ginkgo of Goo Shrine | Kyoto | a reader's photograph, published | [live](https://ancienttrees.app/kyoto/grand-ginkgo-of-goo-shrine) |
| 11-17 | B1 | The Grand Ginkgo of Goo Shrine | Kyoto | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kyoto/grand-ginkgo-of-goo-shrine) |
| 11-17 | C1 | Old Knobbley | Mistley | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mistley/old-knobbley) |
| 11-17 | D1 | Benmore Redwood Avenue | Benmore | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/benmore/benmore-redwood-avenue) |
| 11-17 | Y | Benmore Redwood Avenue | Benmore | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/benmore/benmore-redwood-avenue) |
| 11-17 | E1 | Boab Prison Tree | Derby | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/derby/boab-prison-tree) |
| 11-17 | F1 | The Sisi-Platane of Volksgarten | Vienna | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/vienna/sisi-platane-of-volksgarten) |
| 11-17 | F1 | The Sisi-Platane of Volksgarten | Vienna | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/vienna/sisi-platane-of-volksgarten) |
| 11-17 | G1 | The Cantonspark Giant Sequoia | Baarn | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/baarn/cantonspark-giant-sequoia) |
| 11-17 | T | Chief Sequoyah Tree | Sequoia National Park | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sequoia-national-park/chief-sequoyah-tree) |
| 11-17 | H1 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 11-17 | H1 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 11-17 | H1 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 11-17 | L | The Oak of Molinazzo | Poggio Renatico | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/poggio-renatico/oak-of-molinazzo) |
| 11-17 | I1 | Bleeding Yew of Nevern | Nevern | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/nevern/bleeding-yew-of-nevern) |
| 11-17 | J1 | The Bald Cypresses of the Crystal Palace Pond | Madrid | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/madrid/bald-cypresses-of-the-crystal-palace-pond) |
| 11-17 | K1 | Trolleken (the Troll Oak of Trollskogen) | Trollskogen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/trollskogen/trolleken-the-troll-oak-of-trollskogen) |
| 11-17 | K1 | S'Olivera de Cort | Palma de Mallorca | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/palma-de-mallorca/solivera-de-cort) |
| 11-17 | B1 | The Land Boat Pine | Kyoto | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kyoto/land-boat-pine) |
| 11-17 | F4 | The Ombu of the Essaouira Medina | Essaouira | a reader's photograph, published | [live](https://ancienttrees.app/essaouira/ombu-of-the-essaouira-medina) |
| 11-17 | T1 | The Norfolk Island Pine of Ingle Hall | Hobart | a reader's photograph, published | [live](https://ancienttrees.app/hobart/norfolk-island-pine-of-ingle-hall) |
| 11-17 | T1 | The Bhutan Cypress of Brisbane Street | Hobart | a reader's photograph, published | [live](https://ancienttrees.app/hobart/bhutan-cypress-of-brisbane-street) |
| 11-17 | T1 | The Dawn Redwoods of Elizabeth Street | Hobart | a reader's photograph, published | [live](https://ancienttrees.app/hobart/dawn-redwoods-of-elizabeth-street) |
| 11-17 | V1 | The Big Totara of Lillburn Monowai Road | Tuatapere | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tuatapere/big-totara-of-lillburn-monowai-road) |
| 11-17 | Z | The Wishing Tree | Sydney | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sydney/wishing-tree) |
| 11-17 | Z | The Wishing Tree | Sydney | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sydney/wishing-tree) |
| 11-17 | R1 | The Big Oak | Thomasville | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/thomasville/big-oak) |
| 11-17 | R1 | The Big Oak | Thomasville | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/thomasville/big-oak) |
| 11-17 | U1 | The Moreton Bay Fig of Balboa Park | San Diego | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/san-diego/moreton-bay-fig-of-balboa-park) |
| 11-17 | Q1 | The Gomero de la Recoleta | Buenos Aires | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/buenos-aires/gomero-de-la-recoleta) |
| 11-17 | R1 | The Angel Oak | Charleston | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/charleston/angel-oak) |
| 11-17 | L1 | The Orroroo Giant Gum | Orroroo | a reader's photograph, published | [live](https://ancienttrees.app/orroroo/orroroo-giant-gum) |
| 11-17 | Q1 | Te Waha o Rerekohu | Te Araroa | a reader's photograph, published | [live](https://ancienttrees.app/te-araroa/te-waha-o-rerekohu) |
| 11-17 | R1 | The Old Lime of Estavayer-le-Lac | Estavayer-le-Lac | a reader's photograph, published | [live](https://ancienttrees.app/estavayer-le-lac/old-lime-of-estavayer-le-lac) |
| 11-17 | R1 | The Gennett Poplar | Chattahoochee National Forest | a reader's photograph, published | [live](https://ancienttrees.app/chattahoochee-national-forest/gennett-poplar) |
| 11-17 | R1 | The Knightwood Oak | New Forest | a reader's photograph, published | [live](https://ancienttrees.app/new-forest/knightwood-oak) |
| 11-17 | R1 | A Cedar of the Meares Island Big Tree Trail | Meares Island | a reader's photograph, published | [live](https://ancienttrees.app/meares-island/a-cedar-of-the-meares-island-big-tree-trail) |
| 11-17 | S1 | The Red Gum of Overbury Drive | Adelaide | a reader's photograph, published | [live](https://ancienttrees.app/adelaide/red-gum-of-overbury-drive) |
| 11-17 | R1 | The Giant Sequoias of the Tall Trees Trail | New Forest | a reader's photograph, published | [live](https://ancienttrees.app/new-forest/giant-sequoias-of-the-tall-trees-trail) |
| 11-17 | W1 | The Great Ginkgo of Hida Kokubunji | Takayama | a reader's photograph, published | [live](https://ancienttrees.app/takayama/great-ginkgo-of-hida-kokubunji) |
| 11-17 | S | The Churchyard Yew of Cusop | Cusop | a reader's photograph, published | [live](https://ancienttrees.app/cusop/churchyard-yew-of-cusop) |
| 11-17 | R | The Moreton Bay Fig by the White Mansion | Los Angeles | a reader's photograph, published | [live](https://ancienttrees.app/los-angeles/moreton-bay-fig-by-the-white-mansion) |
| 11-17 | Q | The Elephant-Trunk Fig of Tilarán | Tilarán | a reader's photograph, published | [live](https://ancienttrees.app/tilaran/elephant-trunk-fig-of-tilaran) |
| 11-17 | Q | The Figs Saved by a Wall | Tilarán | a reader's photograph, published | [live](https://ancienttrees.app/tilaran/figs-saved-by-a-wall) |
| 11-17 | P | The Portuguese Oak of the Agronomy Cloister | Lisbon | a reader's photograph, published | [live](https://ancienttrees.app/lisbon/portuguese-oak-of-the-agronomy-cloister) |
| 11-17 | O | The Water Gum that Reaches Out | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/water-gum-that-reaches-out) |
| 11-17 | O | The Leaning Fig over the Boardwalk | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/leaning-fig-over-the-boardwalk) |
| 11-17 | N | The Gomero of Plaza San Martín | Buenos Aires | a reader's photograph, published | [live](https://ancienttrees.app/buenos-aires/gomero-of-plaza-san-martin) |
| 11-17 | X1 | The Cosgrove House Banyan | Key West | a reader's photograph, published | [live](https://ancienttrees.app/key-west/cosgrove-house-banyan) |
| 11-17 | X1 | Jindai-zakura (Yamataka Jindai Zakura) | Hokuto | a reader's photograph, published | [live](https://ancienttrees.app/hokuto/jindai-zakura-yamataka-jindai-zakura) |
| 11-17 | Y1 | The Lewisham Elm | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/lewisham-elm) |
| 11-17 | Z1 | Millennium Tree of Balete Park | Maria Aurora | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/maria-aurora/millennium-tree-of-balete-park) |
| 11-17 | K | The Monkey Thorn on the Riverbed | Francistown | a reader's photograph, published | [live](https://ancienttrees.app/francistown/monkey-thorn-on-the-riverbed) |
| 11-17 | J | The Erler Femeiche | Raesfeld | a reader's photograph, published | [live](https://ancienttrees.app/raesfeld/erler-femeiche) |
| 11-17 | A2 | The north door yews of St Edward's, Stow-on-the-Wold | Stow-on-the-Wold | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/stow-on-the-wold/north-door-yews-of-st-edwards-stow-on-the-wold) |
| 11-17 | V1 | The Big Totara of Lillburn Monowai Road | Tuatapere | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tuatapere/big-totara-of-lillburn-monowai-road) |
| 11-17 | B2 | The Oak of Orkin | Pamplona | a reader's photograph, published | [live](https://ancienttrees.app/pamplona/oak-of-orkin) |
| 11-17 | I | Boab Prison Tree | Derby | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/derby/boab-prison-tree) |
| 11-17 | I | The Hollow Boab of Rowing Club Road | Kununurra | a reader's photograph, published | [live](https://ancienttrees.app/kununurra/hollow-boab-of-rowing-club-road) |
| 11-17 | C | The Sprawling Sycamore of Pawling Farm | Valley Forge | a reader's photograph, published | [live](https://ancienttrees.app/valley-forge/sprawling-sycamore-of-pawling-farm) |
| 11-17 | K1 | Trolleken (the Troll Oak of Trollskogen) | Trollskogen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/trollskogen/trolleken-the-troll-oak-of-trollskogen) |
| 11-17 | K1 | Trolleken (the Troll Oak of Trollskogen) | Trollskogen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/trollskogen/trolleken-the-troll-oak-of-trollskogen) |
| 11-17 | K1 | Trolleken (the Troll Oak of Trollskogen) | Trollskogen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/trollskogen/trolleken-the-troll-oak-of-trollskogen) |
| 11-17 | H2 |  | ? | a reader's photograph, published | not live yet |
| 11-17 | I2 | The Old Yew of Cremines (If millenaire) | Cremines | a reader's photograph, published | [live](https://ancienttrees.app/cremines/old-yew-of-cremines-if-millenaire) |
| 11-17 | J2 | The Oudemanhuispoort Elm | Amsterdam | a reader's photograph, published | [live](https://ancienttrees.app/amsterdam/oudemanhuispoort-elm) |
| 11-17 | K2 | The Totteridge Yew | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/totteridge-yew) |
| 11-17 | L2 | The St Paul's Churchyard Planes | London | a reader's photograph, published | [live](https://ancienttrees.app/london/st-pauls-churchyard-planes) |
| 11-17 | M2 | The Twisted Sweet Chestnut of Greenwich Park | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/twisted-sweet-chestnut-of-greenwich-park) |
| 11-17 | H |  | ? | a reader's photograph, published | not live yet |
| 11-17 | S2 | The Weeping Cedar Tunnel of Glasnevin | Dublin | a reader's photograph, published | [live](https://ancienttrees.app/dublin/weeping-cedar-tunnel-of-glasnevin) |
| 11-17 | U1 | El Sargento | Mexico City | a reader's photograph, published | [live](https://ancienttrees.app/mexico-city/el-sargento) |
| 11-17 | S2 | The Fig That Holds the Stones | Chiang Mai | a reader's photograph, published | [live](https://ancienttrees.app/chiang-mai/fig-that-holds-the-stones) |
| 11-17 | R2 | The Baobab Plane of Penenden Heath | Maidstone | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/maidstone/baobab-plane-of-penenden-heath) |
| 11-17 | H5 | Barney the Plane | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/barney-the-plane) |
| 11-17 | U2 | The Rhodes Bald Cypress | Richard Bong State Recreation Area | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/richard-bong-state-recreation-area/rhodes-bald-cypress) |
| 11-17 | V2 | The Zamalek Banyan | Cairo | a reader's photograph, published | [live](https://ancienttrees.app/cairo/zamalek-banyan) |
| 11-17 | L2 | The Cheapside Plane | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/cheapside-plane) |
| 11-17 | X2 | The Leaning Apple Row of Linford Wood | Milton Keynes | a reader's photograph, published | [live](https://ancienttrees.app/milton-keynes/leaning-apple-row-of-linford-wood) |
| 11-17 | X2 | The Leaning Apple Row of Linford Wood | Milton Keynes | a reader's photograph, published | [live](https://ancienttrees.app/milton-keynes/leaning-apple-row-of-linford-wood) |
| 11-17 | W2 | Rumskullaeken (the Kvill Oak) | Rumskulla | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/rumskulla/rumskullaeken-the-kvill-oak) |
| 11-17 | W2 | Ekebyhovseken | Ekerö | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/ekero/ekebyhovseken) |
| 11-17 | Y2 |  | ? | a reader's photograph, published | not live yet |
| 11-17 | G | The Himalayan Cedar of Parc Mon Repos | Geneva | a reader's photograph, published | [live](https://ancienttrees.app/geneva/himalayan-cedar-of-parc-mon-repos) |
| 11-17 | G | The Sécheron Plane | Geneva | a reader's photograph, published | [live](https://ancienttrees.app/geneva/secheron-plane) |
| 11-17 | A3 | The Tall Tree on the Kanker Forest Track | Kanker | a reader's photograph, published | [live](https://ancienttrees.app/kanker/tall-tree-on-the-kanker-forest-track) |
| 11-17 | Z2 | The White Pine at the Orono Bog Boardwalk | Bangor, Maine | a reader's photograph, published | [live](https://ancienttrees.app/bangor-maine/white-pine-at-the-orono-bog-boardwalk) |
| 11-17 | B3 | The Multisecular Beech of Saint-Jammes | Sorèze | a reader's photograph, published | [live](https://ancienttrees.app/soreze/multisecular-beech-of-saint-jammes) |
| 11-17 | B3 | The Multisecular Beech of Saint-Jammes | Sorèze | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/soreze/multisecular-beech-of-saint-jammes) |
| 11-17 | C3 | The Gunnersbury Park Black Mulberry | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/gunnersbury-park-black-mulberry) |
| 11-17 | C3 | The Gunnersbury Park Black Mulberry | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/gunnersbury-park-black-mulberry) |
| 11-17 | C3 | The Gunnersbury Park Black Mulberry | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/gunnersbury-park-black-mulberry) |
| 11-17 | C3 | The Gunnersbury Park Black Mulberry | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/gunnersbury-park-black-mulberry) |
| 11-17 | D3 | The National Mall Jefferson Elm | Washington DC | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/washington-dc/national-mall-jefferson-elm) |
| 11-17 | F |  | ? | a reader's photograph, published | not live yet |
| 11-17 | R5 | The Ankerwycke Yew | Runnymede | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/runnymede/ankerwycke-yew) |
| 11-17 | E3 |  | ? | a reader's photograph, published | not live yet |
| 11-17 | F3 |  | ? | a reader's photograph, published | not live yet |
| 11-17 | C | The Sprawling Sycamore of Pawling Farm | Valley Forge | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/valley-forge/sprawling-sycamore-of-pawling-farm) |
| 11-17 | C | The Sprawling Sycamore of Pawling Farm | Valley Forge | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/valley-forge/sprawling-sycamore-of-pawling-farm) |
| 11-18 | A |  | ? | a reader's photograph, published | not live yet |
| 11-18 | B | The Camperdown Cemetery Fig | Sydney | a reader's photograph, published | [live](https://ancienttrees.app/sydney/camperdown-cemetery-fig) |
| 11-18 | C | The Sprawling Sycamore of Pawling Farm | Valley Forge | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/valley-forge/sprawling-sycamore-of-pawling-farm) |
| 11-18 | D | The Remnant River Red Gum of Edinburgh Gardens | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/remnant-river-red-gum-of-edinburgh-gardens) |
| 11-18 | D | The Remnant River Red Gum of Edinburgh Gardens | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/remnant-river-red-gum-of-edinburgh-gardens) |
| 11-18 | D | The Finer Holm Oak of Edinburgh Gardens | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/finer-holm-oak-of-edinburgh-gardens) |
| 11-18 | I5 | The Shiba Toshogu Ginkgo | Tokyo | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tokyo/shiba-toshogu-ginkgo) |
| 11-16 | S3 | Ancient totara tree | Akaroa | a reader's tree changed the page | - |
| 11-16 | S5 | isp_001 (The Plane of Çınar Sokak) | Isparta | a reader's correction changed the page | - |
| 11-16 | T3 | 1500 old olive tree | Kaštel Štafalić | a reader's tree changed the page | - |
| 11-16 | H3 | The Champion Lodgepole Pine | - | a reader's correction changed the page | - |
| 11-16 | K4 | kmk_003 (The Tabunoki of the Goryo Shrine at Sakanoshita) | Kamakura | a reader's feedback changed the page | - |
| 11-16 | J1 | The Bald Cypress of Deusto | Bilbao | a reader's correction changed the page | - |
| 11-16 | J4 | Yew | Vigeois | a reader's tree changed the page | - |
| 11-16 | W | bri_003 (The Cedar of Lebanon at Blaise Castle) | Bristol | a reader's feedback changed the page | - |
| 11-16 | L | Quercia del Parco Massari di Ferrara | Ferrara - Italy | a reader's tree changed the page | - |
| 11-16 | M | Balmerino Chestnut | Balmerino | a reader's tree changed the page | - |
| 11-16 | L | Pioppo bianco dell'Oasi Lagoverde di Bologna | Bologna, Italy | a reader's tree changed the page | - |
| 11-16 | R | lax_011 (The Huntington Rose Garden Kauri) | Los Angeles | a reader's feedback changed the page | - |
| 11-16 | T5 | The Yew of Nicorps (If commun de Nicorps) | Nicorps | a reader's correction changed the page | - |
| 11-17 | J | Pedunculate Oak near Winterswijk | - | a reader's correction changed the page | - |
| 11-17 | C | American Sycamore at Pawling Farm in Valley Forge National Park | - | a reader's correction changed the page | - |
| 11-17 | L2 | The St Paul's Churchyard Planes | London | a reader's correction changed the page | - |
| 11-17 | F | Horse Chestnut Tree of Sofienbergparken | Oslo | a reader's tree changed the page | - |
- From 115 readers: reader R1 8, reader J1 6, reader C 5, reader H3 5, reader K1 5, reader C3 4, reader R2 4, reader S2 4, reader V1 4, reader W 4, reader Y 4, reader B1 3, reader D 3, reader H1 3, reader L 3, reader L2 3, reader L4 3, reader M5 3, reader R 3, reader T1 3, reader Z 3, reader A4 2, reader B3 2, reader F 2, reader F1 2, reader G 2, reader I 2, reader I3 2, reader J 2, reader J3 2, reader K4 2, reader M2 2, reader N3 2, reader N4 2, reader O 2, reader P3 2, reader Q 2, reader Q1 2, reader Q5 2, reader T 2, reader U 2, reader U1 2, reader U2 2, reader U3 2, reader W2 2, reader X1 2, reader X2 2, reader X3 2, reader Y3 2, reader A 1, reader A1 1, reader A2 1, reader A3 1, reader B 1, reader B2 1, reader B4 1, reader C1 1, reader C4 1, reader D1 1, reader D3 1, reader E1 1, reader E3 1, reader E4 1, reader F3 1, reader F4 1, reader G1 1, reader G2 1, reader G3 1, reader H 1, reader H2 1, reader H5 1, reader I1 1, reader I2 1, reader I5 1, reader J2 1, reader J4 1, reader J5 1, reader K 1, reader K2 1, reader K3 1, reader K5 1, reader L1 1, reader L3 1, reader L5 1, reader M 1, reader M4 1, reader N 1, reader N5 1, reader O3 1, reader O5 1, reader P 1, reader P5 1, reader Q3 1, reader Q4 1, reader R3 1, reader R4 1, reader R5 1, reader S 1, reader S1 1, reader S3 1, reader S4 1, reader S5 1, reader T3 1, reader T5 1, reader V 1, reader V2 1, reader V3 1, reader W1 1, reader W3 1, reader X 1, reader Y1 1, reader Y2 1, reader Z1 1, reader Z2 1, reader Z3 1.

**What was sent in, and what we decided**

| seen | what | where | size for its species | ours | Hidde |
|---|---|---|---|---|---|
| 2026-11-18 | The Sprawling Sycamore of Pawling Farm | Valley Forge | - | publish | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | publish | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | The Southern Mahogany of Edinburgh Gar | Melbourne | - | hold | - |
| 2026-11-17 | Kapok | - | - | publish | - |
| 2026-11-17 | Kapok | - | - | publish | - |
| 2026-11-17 | The Wishing Tree | Sydney | - | publish | - |
| 2026-11-17 | The Big Oak | Thomasville | - | publish | - |
| 2026-11-17 | Ahuehuete del Jardin de San Fernando | Mexico City | - | hold | - |
| 2026-11-17 | Ahuehuete del Jardin de San Fernando | Mexico City | - | hold | - |
| 2026-11-17 | The Cosgrove House Banyan | Key West | - | hold | - |
| 2026-11-17 | The Cosgrove House Banyan | Key West | - | hold | - |
| 2026-11-17 | Jindai-zakura (Yamataka Jindai Zakura) | Hokuto | - | hold | - |
| 2026-11-17 | Black Mulberry in London | - | - | hold | - |

0 waiting for a verdict. Disagree with one and the rule changes: `python3 scripts/judgement.py --feedback <id> "..."`, and `--learn` prints every verdict he has overruled.

**Searched yesterday:** nothing.

**App crashes** (last 7 days, store builds; MetricKit, a sample)

| Crashes | Kind | Build | Where | Phones | Last | Fix |
|---:|---|---|---|---:|---|---|
| 1 | crash | 1.0.4 (41) | (no AncientTrees frame) | 1 | 2026-11-15 | none |
| 1 | crash | 1.0.4 (41) | AncientTrees+0x2409a0 | 1 | 2026-11-16 | none |

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 11-08 | 25 | 1013 | 2.5% | 9.1 |
| 11-09 | 28 | 1177 | 2.4% | 8.9 |
| 11-10 | 8 | 196 | 4.1% | 13.0 |
| 11-11 | 1 | 16 | 6.2% | 22.1 |
| 11-12 | 1 | 28 | 3.6% | 31.4 |
| 11-13 | 1 | 32 | 3.1% | 55.0 |
| 11-14 | 0 | 51 | 0.0% | 57.5 |
| 11-15 | 210 | 363 | 57.9% | 8.2 |
| 11-16 | 116 | 204 | 56.9% | 6.6 |
| 11-17 *partial* | 53 | 112 | 47.3% | 14.7 |
| **window** | **443** | **3192** | **13.9%** | |
- Top queries (10d): ancient trees app (i409, p1); ancient tree app (i3, p1); ancient trees (i14, p30); android au (i1, p1); skovfogedegen (i1, p4)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-10 | 136 | 9 | 6.6% |
| 11-11 | 97 | 7 | 7.2% |
| 11-12 | 190 | 4 | 2.1% |
| 11-13 | 125 | 5 | 4.0% |
| 11-14 | 103 | 6 | 5.8% |
| 11-15 | 132 | 13 | 9.8% |
| 11-16 | 211 | 15 | 7.1% |
| **7 days** | **994** | **59** | **5.9%** |
- Week before: 849 impressions, 37 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); platane du square des batignolles (c4/i2, p1); picture of the tree in helsinki city center that was preserved (c3/i2, p4); ancient trees app (c2/i8, p5); who planted the western red cedar tree in blarney ireland (c2/i8, p2); fig tree in square alicante (c2/i4, p4); cipresso calvo indro montanelli milano (c2/i2, p8); palma del cile (c2/i2, p6)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-17T17:18 | 10.7 | 0 | 15 | 3 | Dublin, Soreze |
| 11-17T23:58 | 20.2 | 6 | 13 | 2 | Fort Worth +3, Leeds +2, Sydney +1 |
| 11-18T00:23 | 10.9 | 2 | 6 | 1 | Baltimore +1, Philadelphia +1, Sydney |
| **3 runs** | **42** | **8** | **34** | | |

- 1 of 3 produced no trees; 1 to 3 commands refused per run; last build that went live: 0h ago.

**What they made**

- Code review: 1 new finding(s)
- Fresh-eyes review: 6 finding(s)
- Fresh-eyes review: 4 finding(s)
- reader judge: two Edinburgh Gardens sightings rejected as duplicates of the held backlit gum frame
- reader judge: first photograph of Melbourne's finer holm oak (mel_001), a reader's photo leads the Shiba Toshogu ginkgo (tok_005), a Wishing Tree duplicate rejected
- reader judge: first photograph of the Edinburgh Gardens red gum (mel_002); a reader's gum by the skate bowl live as mel_019
- reader judge: the finder's trunk photograph of the Pawling Farm sycamore (vfg_001) into its gallery
- reader judge: a reader's photograph leads the Camperdown Cemetery Fig (syd_005); Pawling Farm sign rejected, no tree in frame
- Philadelphia phl_022 and Baltimore bal_005 published, claims released, costs and LOG
- Philadelphia and Baltimore verify passes: one flagged tree each, leads and blocked kept
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- reader judge: the Rushcutters Bay fig's trunk close-up into syd_008's strip (the reader's second photograph)
- Birmingham UK verify pass found no pinned tree; leads and blocked entries kept, LOG

**Reader photographs in a strip, live first, not yet looked at** (44)

| Day | Tree | Where | Undo |
|---|---|---|---|
| 11-17 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | `sightings_publish.py --unstrip 5e09bb82-34d7-4622-b626-8251836f6eb4` |
| 11-17 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | `sightings_publish.py --unstrip 62c4bb28-b3f8-46f6-8d7a-c88755acce7b` |
| 11-17 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | `sightings_publish.py --unstrip 5ecc82c8-870b-4961-9a0f-b4fb6bf2e1b6` |
| 11-16 | The Sacred Olive Tree of the Acropolis | Athens | `sightings_publish.py --unstrip c86414b5-1884-40c9-aff2-724f25f8e1f4` |
| 11-17 | The Cantonspark Giant Sequoia | Baarn | `sightings_publish.py --unstrip cc8a74d4-d8a7-42fa-865c-f5a12e490f7f` |
| 11-17 | Benmore Redwood Avenue | Benmore | `sightings_publish.py --unstrip cdc0b82c-26f6-4691-94df-3d728924d039` |
| 11-17 | Benmore Redwood Avenue | Benmore | `sightings_publish.py --unstrip 4c161566-17bf-4859-a3cb-2148328999a9` |
| 11-16 | The Lietzensee Plane | Berlin | `sightings_publish.py --unstrip 37223ae8-945a-4737-bd16-1cf8defb2ee1` |
| 11-16 | The Plane Trees of Jardines de Albia | Bilbao | `sightings_publish.py --unstrip ea9d0b2f-f100-496d-a05c-6f492630635f` |
| 11-16 | The Borrowdale Yews (the Fraternal Four) | Borrowdale | `sightings_publish.py --unstrip b24f5c1e-b9c6-4f5a-af2e-c761fa60e614` |
| 11-16 | The Borrowdale Yews (the Fraternal Four) | Borrowdale | `sightings_publish.py --unstrip 3cf4d1ae-05de-4dff-b168-0c0815960fd3` |
| 11-16 | The Bundle-planted Sessile Oak, Bishops Knoll | Bristol | `sightings_publish.py --unstrip 1b2096fe-4e2d-41f0-9517-b288ef04b372` |
| 11-17 | The Gomero de la Recoleta | Buenos Aires | `sightings_publish.py --unstrip e5b4eedf-8140-4bf4-8ce2-c32a1f921168` |
| 11-16 | The Angel Oak | Charleston | `sightings_publish.py --unstrip 27b65062-4209-44fa-ad20-a179dd1e974f` |
| 11-17 | The Angel Oak | Charleston | `sightings_publish.py --unstrip 78b88780-f090-4c13-8360-95570ebe3113` |
| 11-17 | Boab Prison Tree | Derby | `sightings_publish.py --unstrip 023ed607-1e16-4502-a16c-ba7b77888f82` |
| 11-16 | Elleholmseken (The Oak of Elleholm) | Elleholm | `sightings_publish.py --unstrip a04e6933-4b0d-4172-90d1-5d13dcfec0e5` |
| 11-16 | The Fortingall Yew | Fortingall | `sightings_publish.py --unstrip 7fb05e54-cf36-4393-a549-92e3c17d96b3` |
| 11-16 | The Willow Nearest the Hypocentre | Hiroshima | `sightings_publish.py --unstrip 96c47295-7fb6-40d8-b0da-3575f4b9b420` |
| 11-17 | The Land Boat Pine | Kyoto | `sightings_publish.py --unstrip 46766dcd-94f4-4656-8dab-53b5c98b30f8` |
| 11-16 | The Great Plane of Brunswick Square | London | `sightings_publish.py --unstrip 68f3ef55-878f-4dad-846d-9582ed057c08` |
| 11-17 | The Bald Cypresses of the Crystal Palace Pond | Madrid | `sightings_publish.py --unstrip e593be60-987f-469d-97d7-7da2a69503d5` |
| 11-16 | Ahuehuete de Parque Espana | Mexico City | `sightings_publish.py --unstrip 3693bdc5-cbb5-4ff1-909e-745a397aaf76` |
| 11-16 | Ahuehuete de Parque Espana | Mexico City | `sightings_publish.py --unstrip 9d72943f-aba5-4ab8-a8da-ee9c3a21a1cf` |
| 11-17 | Old Knobbley | Mistley | `sightings_publish.py --unstrip a477d312-0d76-4189-9217-ef167b0b1bc7` |
| 11-17 | Bleeding Yew of Nevern | Nevern | `sightings_publish.py --unstrip 09765ff6-b1e9-4d56-a98a-73c47709468b` |
| 11-16 | The Tree of Life | Olympic National Park | `sightings_publish.py --unstrip d8212c9e-e921-4b28-b931-44a7ff01fec4` |
| 11-16 | The Quinault Big Spruce | Olympic National Park | `sightings_publish.py --unstrip d21fa973-8906-4f73-81f7-c7e4036c2fd2` |
| 11-17 | S'Olivera de Cort | Palma de Mallorca | `sightings_publish.py --unstrip 3c756f92-fc89-4a76-a714-06e8a6361b0f` |
| 11-17 | The Oak of Molinazzo | Poggio Renatico | `sightings_publish.py --unstrip c42df403-c159-4896-9c07-223d1122c3d6` |
| 11-17 | The Moreton Bay Fig of Balboa Park | San Diego | `sightings_publish.py --unstrip ee80ee46-48b1-4e89-bc8d-23c892d50b1d` |
| 11-16 | El Árbol del Tule | Santa María del Tule | `sightings_publish.py --unstrip 586a2d0f-096b-421c-97dc-62e612fd99b2` |
| 11-16 | General Sherman Tree | Sequoia National Park | `sightings_publish.py --unstrip b8d96d31-883d-496e-8607-a353a8acab01` |
| 11-17 | Chief Sequoyah Tree | Sequoia National Park | `sightings_publish.py --unstrip c59bfd73-d95b-4cda-9ae3-5f75cf6f9754` |
| 11-16 | Lincoln Tree | Sequoia National Park | `sightings_publish.py --unstrip 9342233f-7ec8-4d72-b3d6-2f859d2c26c1` |
| 11-17 | The Wishing Tree | Sydney | `sightings_publish.py --unstrip 4be001d1-ee21-48f8-81df-67bf1bb02d41` |
| 11-17 | The Wishing Tree | Sydney | `sightings_publish.py --unstrip f05d3a86-b304-47ac-bf24-2e0f88ad99a1` |
| 11-17 | The Great Ginkgo of Hida Kokubunji | Takayama | `sightings_publish.py --unstrip 65cb49cd-5812-4470-a56c-4b681646b7d2` |
| 11-17 | The Big Oak | Thomasville | `sightings_publish.py --unstrip aa636a2c-f651-42b4-82e2-18f8ce6b981e` |
| 11-17 | The Big Oak | Thomasville | `sightings_publish.py --unstrip c64b5650-6946-456a-b0d4-8af4fd95bacd` |
| 11-17 | Trolleken (the Troll Oak of Trollskogen) | Trollskogen | `sightings_publish.py --unstrip 54dc7d2a-aaf6-4158-8784-3f3c256942a3` |
| 11-17 | The Big Totara of Lillburn Monowai Road | Tuatapere | `sightings_publish.py --unstrip 45e7ad05-a36e-480b-8c4b-fc0e4d5c5a47` |
| 11-17 | The Sisi-Platane of Volksgarten | Vienna | `sightings_publish.py --unstrip 57a1afed-1a15-4782-b4a1-4aeaf08a9f04` |
| 11-17 | The Sisi-Platane of Volksgarten | Vienna | `sightings_publish.py --unstrip 161c7f67-f76d-4527-84b1-d24ab59c798f` |

Machine: 4 chain attempts yesterday, 4 got real work time (~88 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c379/i616); /app (c3/i27); /switzerland (c3/i12); /seville (c2/i51); /fr/lyon/arbre-le-plus-vieux (c2/i4)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i5, p3)
    - 'alte bäume karte' (i3, p7)
    - 'acient tree' (i2, p14)
    - 'angeloak' (i2, p79)
    - 'android au' (i1, p1)
    - 'ahornbäume in der nähe' (i1, p7)
    - 'alberi di roma' (i1, p1)
    - 'alter' (i1, p2)
    - and 1 more

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 170 | 18 | 59 | 0.35 | 1 |
| Not yet rich | 267 | 22 | 215 | 0.81 | 0 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| fortingall | 0 | 146 | 0.0% | 11.5 | 2.0% | fortingall yew (i117, p11) |
| lisbon | 0 | 61 | 0.0% | 6.4 | 4.6% | historic giant plant of lisbon (i1, p12) |
| seville | 2 | 57 | 3.5% | 5.1 | 6.8% | sevilla (i1, p1) |
| berlin | 2 | 41 | 4.9% | 6.0 | 5.1% | berlin trees (i2, p5) |
| fulufjallet | 0 | 41 | 0.0% | 9.4 | 2.8% | old tjikko (i22, p11) |
| olympic-national-park | 0 | 36 | 0.0% | 20.3 | 0.8% | duncan cedar (i14, p10) |
| tokyo | 0 | 33 | 0.0% | 5.8 | 5.5% | ginkgo sperm (i2, p11) |
| malaga | 0 | 31 | 0.0% | 25.2 | 0.6% | árboles históricos de málaga (i7, p89) |
| london | 2 | 29 | 6.9% | 33.0 | 0.4% | flats to rent clerkenwell (i3, p89) |
| singapore | 0 | 29 | 0.0% | 9.0 | 3.0% | earpod tree (i3, p5) |
| south-korea | 0 | 28 | 0.0% | 21.4 | 0.7% | ginkgo tree korea (i2, p5) |
| munich | 1 | 26 | 3.8% | 5.3 | 6.4% | ältester baum münchen (i1, p8) |
| tenerife | 0 | 25 | 0.0% | 34.2 | 0.4% | el drago milenario (i2, p10) |
| paris | 1 | 24 | 4.2% | 5.9 | 5.2% | - |
| kyoto | 1 | 24 | 4.2% | 4.0 | 8.1% | ginkgo tree kyoto (i1, p1) |
| palermo | 0 | 24 | 0.0% | 9.0 | 3.0% | palermo tree (i1, p9) |
| monterey | 0 | 23 | 0.0% | 54.9 | 0.4% | lone cypress (i5, p77) |
| united-states | 2 | 22 | 9.1% | 20.3 | 0.8% | oldest tree in oregon (i4, p10) |
| sequoia-national-park | 0 | 22 | 0.0% | 33.7 | 0.4% | washington tree (i10, p27) |
| copenhagen | 2 | 21 | 9.5% | 11.0 | 2.2% | copenhagen trees (i3, p39) |
| seoul | 1 | 21 | 4.8% | 6.1 | 4.9% | - |
| amsterdam | 0 | 21 | 0.0% | 8.7 | 3.1% | lomanstraat (i2, p19) |
| taiwan | 0 | 18 | 0.0% | 11.1 | 2.1% | oldest tree in taiwan (i3, p5) |
| reykjavik | 0 | 18 | 0.0% | 5.8 | 5.3% | - |
| barcelona | 0 | 17 | 0.0% | 9.4 | 2.8% | - |
| venice | 2 | 16 | 12.5% | 4.0 | 8.0% | - |
| austin | 0 | 16 | 0.0% | 17.2 | 1.0% | oldest tree in austin (i2, p12) |
| kagoshima | 0 | 16 | 0.0% | 10.0 | 2.5% | oldest camphor tree (i1, p7) |
| germany | 1 | 15 | 6.7% | 6.1 | 4.9% | - |
| san-francisco | 0 | 15 | 0.0% | 4.9 | 7.1% | old tree near me (i1, p4) |
| edinburgh | 0 | 15 | 0.0% | 12.5 | 1.7% | - |
| brisbane | 0 | 15 | 0.0% | 16.5 | 1.1% | banyan tree (i3, p10) |
| porto | 1 | 14 | 7.1% | 2.1 | 14.4% | - |
| oahu | 0 | 14 | 0.0% | 9.4 | 2.8% | hitachi tree (i2, p10) |
| cambridge | 0 | 14 | 0.0% | 25.3 | 0.6% | isaac newton tree (i2, p22) |
| los-angeles | 0 | 14 | 0.0% | 7.8 | 3.6% | moreton bay fig tree beverly hills (i1, p9) |
| milan | 0 | 14 | 0.0% | 5.4 | 6.3% | - |
| prague | 0 | 14 | 0.0% | 4.9 | 7.1% | - |
| athens | 0 | 13 | 0.0% | 5.5 | 6.1% | - |
| switzerland | 3 | 12 | 25.0% | 3.6 | 9.2% | - |
| dublin | 1 | 12 | 8.3% | 4.3 | 7.7% | - |
| nara | 1 | 12 | 8.3% | 5.8 | 5.5% | - |
| charleston | 0 | 12 | 0.0% | 24.3 | 0.6% | angeloak (i2, p79) |
| kanazawa | 0 | 12 | 0.0% | 6.3 | 4.7% | - |
| madrid | 0 | 12 | 0.0% | 7.1 | 4.0% | - |
| chishang | 0 | 11 | 0.0% | 6.5 | 4.5% | takeshi kaneshiro tree (i6, p7) |
| fukuoka | 0 | 11 | 0.0% | 7.4 | 3.8% | dazaifu tenmangu (i1, p1) |
| netherlands | 1 | 10 | 10.0% | 9.0 | 3.0% | dutch trees (i1, p39) |
| bristol | 0 | 10 | 0.0% | 6.0 | 5.0% | - |
| poland | 0 | 10 | 0.0% | 7.7 | 3.6% | trees in poland (i1, p8) |
| antwerp | 0 | 10 | 0.0% | 42.3 | 0.4% | park den brandt (i3, p52) |
| seattle | 0 | 10 | 0.0% | 9.3 | 2.8% | oldest tree in seattle (i1, p10) |

- Plus 212 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: bath, rome, new-york, brussels, vienna, alicante, cadiz, pamplona.

## 2026-11-16 (previous UTC day)

**Today: 15 android waitlist signups arrived today (996 total); 59 tree submissions and an ambassador request for Colchester and an ambassador request for Sydney and an ambassador request for Toronto and 14 correction reports and 36 feedback reports arrived today (372 submissions of every kind in all); 15 accounts were opened today (645 accounts in all).**

**North star: 174 people have uploaded a tree or photo of their own (+162 this week); 15 of them did it on more than one day (+11).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 2504 | 52 |
| ... of which from search | every search engine | 67 | 22 |
| ... from Google | Google's recovery | 50 | 17 |
| ... from Bing | Bing | 4 | 2 |
| Website visitors who came back | people who stay | 396 | 11 |
| App downloads (first-time) | people | 3907 | 24 |
| New accounts | people | 570 | 4 |
| Phones back within 30 days | people who stay | 4 of 15 | 4 of 10 |
| Trees saved to Want to go | intent | 334 | 1 |
| Trees collected | goal 1: stood at a tree | 193 | 7 |
| Readers' contributions | data: trees, photos, corrections | 378 | 4 |
| Worth-it votes | one tap, not a contribution | 107 | 0 |
| Shares (app and web) | word of mouth, since 10-30 | 163 | 2 |
| Visits from a shared link | what sharing brings | 61 | 0 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web orange, iOS red, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | green | red: iOS build failure on main | grey: no checks wired yet |
| Live | orange: 1 new error type(s), first "Error: Failed to initialize WebGL" in /assets/maplibre-gl-4.7.1.js | green | grey: no checks wired yet |

**Plus question** (9 answers, 2 new; 3 asked to be told; 5 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| Something else | 4 |
| A richer log of every tree you've collected | 3 |
| Download offline maps | 2 |
| Recommended tree walks for a city trip | 2 |
| Seasonal alerts when trees are at their best | 2 |

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-10 | 11-11 | 11-12 | 11-13 | 11-14 | 11-15 | 11-16 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 11 | 0 | 3 | 5 | 3 | 1797 | 734 | **2553** |
| New accounts | 1 | 0 | 1 | 0 | 2 | 369 | 197 | **570** |
| Saves | 0 | 0 | 0 | 0 | 0 | 191 | 143 | **334** |
| Android waitlist | 1 | 0 | 0 | 0 | 0 | 739 | 242 | **982** |
| App downloads | 3 | 1 | 2 | 2 | 1 | 3896 | – | **3905** |
| App deletions | 0 | 0 | – | – | – | 11 | 16 | **27** |
| App phones | 5 | 6 | 5 | 5 | 8 | 3562 | 1690 | **4990** |
| Trees opened in the app | 14 | 3 | 3 | 4 | 18 | 7607 | 3261 | **10910** |
| Trees collected | 0 | 0 | 0 | 0 | 3 | 96 | 59 | **158** |
| Trees sent | 0 | 0 | 0 | 1 | 0 | 98 | 51 | **150** |
| Feedback | 0 | 0 | 0 | 0 | 0 | 29 | 23 | **52** |
| Worth-it votes | 0 | 0 | 0 | 0 | 0 | 63 | 44 | **107** |
| Ambassador asks | 0 | 0 | 0 | 0 | 0 | 5 | 3 | **8** |
| Website photos | 0 | 1 | 0 | 0 | 0 | 9 | 1 | **11** |
| iPhone photos | 0 | 0 | 0 | 0 | 3 | 158 | 115 | **276** |
| Android photos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Tree notes | 0 | 0 | 0 | 0 | 1 | 15 | 23 | **39** |
| App Store reviews | 0 | 0 | 0 | 0 | 0 | 5 | 0 | **5** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.
- App deletions count only phones that share analytics with developers, and Apple leaves out days too small to show: read it against the installs of the same day, not as a total.

**Feedback by kind** (the Feedback row above, split; their words are in the readers-in-full block)

| Kind | 11-16 | **7 days** |
|---|---:|---:|
| Pin moved | 16 | **34** |
| Written feedback | 0 | **5** |
| Report on a tree | 7 | **12** |
| Collected far from our pin | 0 | **1** |

**Trees readers sent, for you to inspect** (332 you have not looked at; ours left out)

| Judged | Reader | Tree | Where | Species | Their girth | Our verdict | Page |
|---|---|---|---|---|---:|---|---|
| 2026-11-17 | A | - | powelltown | - | - | publish | [pwt_001](https://ancienttrees.app/powelltown/ada-tree) |
| 2026-11-17 | B | - | humboldt-redwoods-state-park | - | - | publish | [hum_001](https://ancienttrees.app/humboldt-redwoods-state-park/giant-tree) |
| 2026-11-17 | C | - | new-york | - | - | publish | [nyc_024](https://ancienttrees.app/new-york/ginkgo-of-the-united-order-of-tents) |
| 2026-11-17 | D | - | los-angeles | - | - | publish | [lax_017](https://ancienttrees.app/los-angeles/huntington-montezuma-cypress) |
| 2026-11-17 | E | - | bristol | - | - | publish | [bri_003](https://ancienttrees.app/bristol/cedar-of-lebanon-at-blaise-castle) |
| 2026-11-17 | F | - | cascais | - | - | publish | [csc_001](https://ancienttrees.app/cascais/moreton-bay-fig-of-parque-marechal-carmona) |
| 2026-11-17 | G | - | setubal | - | - | publish | [stb_009](https://ancienttrees.app/setubal/pepper-tree-that-mended-nets) |
| 2026-11-17 | D | - | los-angeles | - | - | publish | [lax_011](https://ancienttrees.app/los-angeles/huntington-rose-garden-kauri) |
| 2026-11-17 | H | - | sydney | - | - | publish | [syd_006](https://ancienttrees.app/sydney/wishing-tree) |
| 2026-11-17 | G | - | setubal | - | - | publish | [stb_010](https://ancienttrees.app/setubal/peruvian-pepper-of-the-jardim-de-palhais) |
| 2026-11-17 | I | - | cardiff | - | - | publish | [crd_012](https://ancienttrees.app/cardiff/roath-park-lake-pedunculate-oak) |
| 2026-11-17 | J | - | kyoto | - | - | publish | [kyo_014](https://ancienttrees.app/kyoto/grand-ginkgo-of-goo-shrine) |
| 2026-11-17 | J | - | kyoto | - | - | publish | [kyo_014](https://ancienttrees.app/kyoto/grand-ginkgo-of-goo-shrine) |
| 2026-11-17 | H | - | - | - | - | hold | - |
| 2026-11-17 | D | - | - | - | - | hold | - |
| 2026-11-17 | D | - | - | - | - | hold | - |
| 2026-11-17 | K | - | mistley | - | - | publish | [okb_001](https://ancienttrees.app/mistley/old-knobbley) |
| 2026-11-17 | L | - | benmore | - | - | publish | [bmr_001](https://ancienttrees.app/benmore/benmore-redwood-avenue) |
| 2026-11-17 | G | - | benmore | - | - | publish | [bmr_001](https://ancienttrees.app/benmore/benmore-redwood-avenue) |
| 2026-11-17 | M | - | derby | - | - | publish | [der_001](https://ancienttrees.app/derby/boab-prison-tree) |
| 2026-11-17 | N | - | vienna | - | - | publish | [vie_007](https://ancienttrees.app/vienna/sisi-platane-of-volksgarten) |
| 2026-11-17 | N | - | - | - | - | hold | - |
| 2026-11-17 | N | - | - | - | - | hold | - |
| 2026-11-17 | N | - | vienna | - | - | publish | [vie_007](https://ancienttrees.app/vienna/sisi-platane-of-volksgarten) |
| 2026-11-17 | O | - | baarn | - | - | publish | [brn_002](https://ancienttrees.app/baarn/cantonspark-giant-sequoia) |
| 2026-11-17 | A | - | sequoia-national-park | - | - | publish | [seq_003](https://ancienttrees.app/sequoia-national-park/chief-sequoyah-tree) |
| 2026-11-17 | P | - | aguas-de-moura | - | - | publish | [agm_001](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 2026-11-17 | P | - | aguas-de-moura | - | - | publish | [agm_001](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 2026-11-17 | P | - | aguas-de-moura | - | - | publish | [agm_001](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 2026-11-17 | Q | - | poggio-renatico | - | - | publish | [pgr_001](https://ancienttrees.app/poggio-renatico/oak-of-molinazzo) |
| 2026-11-17 | R | - | nevern | - | - | publish | [nvn_001](https://ancienttrees.app/nevern/bleeding-yew-of-nevern) |
| 2026-11-17 | S | - | madrid | - | - | publish | [mad_004](https://ancienttrees.app/madrid/bald-cypresses-of-the-crystal-palace-pond) |
| 2026-11-17 | T | - | trollskogen | - | - | publish | [trs_001](https://ancienttrees.app/trollskogen/trolleken-the-troll-oak-of-trollskogen) |
| 2026-11-17 | T | - | palma-de-mallorca | - | - | publish | [plm_001](https://ancienttrees.app/palma-de-mallorca/solivera-de-cort) |
| 2026-11-17 | J | - | kyoto | - | - | publish | [kyo_002](https://ancienttrees.app/kyoto/land-boat-pine) |
| 2026-11-17 | U | River Red Gum | Orroroo | River Red Gum | - | publish | [orr_001](https://ancienttrees.app/orroroo/orroroo-giant-gum) |
| 2026-11-16 | V | The Borrowdale Yews (the Fraternal Four) | Borrowdale | European Yew (Taxus baccata) | - | publish | [bwd_001](https://ancienttrees.app/borrowdale/borrowdale-yews-the-fraternal-four) |
| 2026-11-16 | W | Ahuehuete de Parque Espana (2 photos) | Mexico City | Montezuma Cypress (Taxodium mu | - | publish | [mex_005](https://ancienttrees.app/mexico-city/ahuehuete-de-parque-espana) |
| 2026-11-16 | X | The Angel Oak | Charleston | Southern Live Oak (Quercus vir | - | publish | [chs_001](https://ancienttrees.app/charleston/angel-oak) |
| 2026-11-16 | Y | Earlysville Oak | earlysville | White Oak | - | publish | [ely_001](https://ancienttrees.app/earlysville/airport-oak-of-earlysville) |
| 2026-11-16 | Z | Podocarpus hallii | tuatapere | Podocarpus hallii | 831 cm | publish | [tua_001](https://ancienttrees.app/tuatapere/big-totara-of-lillburn-monowai-road) |
| 2026-11-16 | Z | Curtain Fig | yungaburra | Cunningham's Fig / White Fig | - | publish | [ybr_001](https://ancienttrees.app/yungaburra/curtain-fig-tree) |
| 2026-11-16 | A1 | European Yew near Estry | la-lande-patry | European Yew | - | publish | [llp_001](https://ancienttrees.app/la-lande-patry/hollow-yew-of-la-lande-patry) |
| 2026-11-16 | B1 | American Elm (2 photos) | - | American Elm | - | lead | - |
| 2026-11-16 | B1 | Eastern Cottonwood (2 photos) | - | Eastern Cottonwood | - | lead | - |
| 2026-11-16 | B1 | White Oak | - | White Oak | - | lead | - |
| 2026-11-16 | B1 | Northern Red Oak | - | Northern Red Oak | - | lead | - |
| 2026-11-16 | C1 | Baobab (2 photos) | mbissel | Baobab | 33 cm | publish | [mbs_001](https://ancienttrees.app/mbissel/baobab-of-mbissel) |
| 2026-11-16 | D1 | Ginkgo (3 photos) | - | Ginkgo | - | lead | - |
| 2026-11-16 | E1 | Boab | darwin | Boab | 940 cm | publish | [drw_001](https://ancienttrees.app/darwin/cavenagh-street-boab) |
| 2026-11-16 | F1 | A tree I found (9 photos) | - | - | - | lead | - |
| 2026-11-16 | G1 | The Becks Prime Augusta Live Oaks | Houston | - | - | publish | [hou_009](https://ancienttrees.app/houston/becks-prime-augusta-live-oaks) |
| 2026-11-16 | G1 | The Old Pecan Tree | Houston | - | - | publish | [hou_002](https://ancienttrees.app/houston/old-pecan-tree) |
| 2026-11-16 | H1 | The Kapok Tree | Key West | - | - | publish | [kyw_003](https://ancienttrees.app/key-west/kapok-tree) |
| 2026-11-16 | I1 | The Rhodes Bald Cypress | Richard Bong State Recreation Area | - | - | publish | [bng_001](https://ancienttrees.app/richard-bong-state-recreation-area/rhodes-bald-cypress) |
| 2026-11-16 | J1 | Populus nigra subsp. Betulifolia near Linton | - | Populus nigra subsp. Betulifol | 300 cm | lead | - |
| 2026-11-16 | K1 | Oak | kvam | Oak | - | publish | [kvm_001](https://ancienttrees.app/kvam/old-oak-at-tolo) |
| 2026-11-16 | D1 | The Champion Lodgepole Pine | big-bear-lake | Lodgepole Pine | 1100 cm | publish | [bbl_001](https://ancienttrees.app/big-bear-lake/champion-lodgepole-pine) |
| 2026-11-16 | L1 | Ancient totara tree | akaroa | - | 850 cm | publish | [akr_001](https://ancienttrees.app/akaroa/giant-totara-of-montgomery-park) |
| 2026-11-16 | M1 | 1500 old olive tree | kastela | Olive (Olea sp.) | 650 cm | publish | [cdl_003](https://ancienttrees.app/kastela/mastrinka-the-olive-of-kastel-stafilic) |
| 2026-11-16 | M1 | Linden tree next to the pond | - | Lime (Tilia sp.) | 166 cm | lead | - |
| 2026-11-16 | N1 | The Aogiri of Peace Memorial Park | Hiroshima | Chinese Parasol Tree (Firmiana | - | publish | [hir_005](https://ancienttrees.app/hiroshima/aogiri-of-peace-memorial-park) |
| 2026-11-16 | O1 | The Embracing Fig of the Giardini Reali | Palermo | Moreton Bay Fig (Ficus macroph | - | publish | [pal_016](https://ancienttrees.app/palermo/embracing-fig-of-the-giardini-reali) |
| 2026-11-16 | P1 | Enchanted Balete Tree of Lazi | Siquijor | Fig (Ficus sp.) | - | publish | [sqj_001](https://ancienttrees.app/siquijor/enchanted-balete-tree-of-lazi) |
| 2026-11-16 | Q1 | Millennium Tree of Balete Park | Maria Aurora | Fig (Ficus sp.) | - | publish | [mra_001](https://ancienttrees.app/maria-aurora/millennium-tree-of-balete-park) |
| 2026-11-16 | R1 | El Árbol del Tule (2 photos) | Santa María del Tule | Montezuma Cypress (Taxodium mu | - | publish | [tul_001](https://ancienttrees.app/santa-maria-del-tule/el-arbol-del-tule) |
| 2026-11-16 | S1 | Elleholmseken (The Oak of Elleholm) (2 photos) | Elleholm | Pedunculate Oak (Quercus robur | - | publish | [elh_001](https://ancienttrees.app/elleholm/elleholmseken-the-oak-of-elleholm) |
| 2026-11-16 | N1 | The Willow Nearest the Hypocentre | Hiroshima | Weeping Willow (Salix babyloni | - | publish | [hir_001](https://ancienttrees.app/hiroshima/willow-nearest-the-hypocentre) |
| 2026-11-16 | R1 | The Fortingall Yew (3 photos) | Fortingall | European Yew (Taxus baccata) | - | publish | [for_001](https://ancienttrees.app/fortingall/fortingall-yew) |
| 2026-11-16 | D1 | General Sherman Tree | Sequoia National Park | Giant Sequoia (Sequoiadendron  | - | publish | [seq_001](https://ancienttrees.app/sequoia-national-park/general-sherman-tree) |
| 2026-11-16 | D1 | Lincoln Tree | Sequoia National Park | Giant Sequoia (Sequoiadendron  | - | publish | [seq_004](https://ancienttrees.app/sequoia-national-park/lincoln-tree) |
| 2026-11-16 | T1 | The Sacred Olive Tree of the Acropolis | Athens | Olive (Olea europaea) | - | publish | [ath_001](https://ancienttrees.app/athens/sacred-olive-tree-of-the-acropolis) |
| 2026-11-16 | U1 | The Plaited Birch of Brocton | Cannock Chase | Birch (Betula sp.) | - | publish | [cnk_004](https://ancienttrees.app/cannock-chase/plaited-birch-of-brocton) |
| 2026-11-16 | V1 | The Fig of Neal Macrossan Park | Brisbane | Fig (Ficus sp.) | - | publish | [bne_022](https://ancienttrees.app/brisbane/fig-of-neal-macrossan-park) |
| 2026-11-16 | B | The Bodhi Tree of Lumbini | Lumbini | Bodhi Tree (Ficus religiosa) | - | publish | [lmb_001](https://ancienttrees.app/lumbini/bodhi-tree-of-lumbini) |
| 2026-11-16 | Y | The Airport Oak of Earlysville | Earlysville | Oak (Quercus sp.) | - | publish | [ely_001](https://ancienttrees.app/earlysville/airport-oak-of-earlysville) |
| 2026-11-16 | Z | The Big Totara of Lillburn Monowai Road | Tuatapere | Totara (Podocarpus sp.) | - | publish | [tua_001](https://ancienttrees.app/tuatapere/big-totara-of-lillburn-monowai-road) |
| 2026-11-16 | Z | The Curtain Fig Tree | Yungaburra | Cunningham's Fig / White Fig ( | - | publish | [ybr_001](https://ancienttrees.app/yungaburra/curtain-fig-tree) |
| 2026-11-16 | A1 | The Hollow Yew of La Lande-Patry | La Lande-Patry | European Yew (Taxus baccata) | - | publish | [llp_001](https://ancienttrees.app/la-lande-patry/hollow-yew-of-la-lande-patry) |
| 2026-11-16 | C1 | The Baobab of Mbissel | Mbissel | Baobab (Adansonia digitata) | - | publish | [mbs_001](https://ancienttrees.app/mbissel/baobab-of-mbissel) |
| 2026-11-16 | C1 | The Sagole Baobab | Sagole | Baobab (Adansonia digitata) | - | publish | [sgl_001](https://ancienttrees.app/sagole/sagole-baobab) |
| 2026-11-16 | E1 | The Cavenagh Street Boab | Darwin | Boab (Adansonia gregorii) | - | publish | [drw_001](https://ancienttrees.app/darwin/cavenagh-street-boab) |
| 2026-11-16 | K1 | The Old Oak at Tolo | Kvam | Oak (Quercus sp.) | - | publish | [kvm_001](https://ancienttrees.app/kvam/old-oak-at-tolo) |
| 2026-11-16 | W1 | Blackbutt | middle-brother-national-park | Blackbutt | 1100 cm | publish | [mbr_001](https://ancienttrees.app/middle-brother-national-park/blackbutt-of-bird-tree-road) |
| 2026-11-16 | W1 | middle-brother-national-park/mbr_001 The Bla | middle-brother-national-park | Blackbutt | 1100 cm | publish | [mbr_001](https://ancienttrees.app/middle-brother-national-park/blackbutt-of-bird-tree-road) |
| 2026-11-16 | X1 | nottingham/ntm_001 The Arbour Oak of Wollato | nottingham | Oak (Quercus sp.) | 700 cm | publish | [ntm_001](https://ancienttrees.app/nottingham/arbour-oak-of-wollaton-park) |
| 2026-11-16 | Q | poggio-renatico/pgr_001 The Oak of Molinazzo | poggio-renatico | Oak (Quercus sp.) | 460 cm | publish | [pgr_001](https://ancienttrees.app/poggio-renatico/oak-of-molinazzo) |
| 2026-11-16 | D1 | big-bear-lake/bbl_001 The Champion Lodgepole | big-bear-lake | Lodgepole Pine | 1100 cm | publish | [bbl_001](https://ancienttrees.app/big-bear-lake/champion-lodgepole-pine) |
| 2026-11-16 | Y1 | gilgandra/gil_001 The Grapevine of the Royal | gilgandra | Grape | 300 cm | publish | [gil_001](https://ancienttrees.app/gilgandra/grapevine-of-the-royal-hotel) |
| 2026-11-16 | L1 | akaroa/akr_001 The Giant Tōtara of Montgomer | akaroa | - | 850 cm | publish | [akr_001](https://ancienttrees.app/akaroa/giant-totara-of-montgomery-park) |
| 2026-11-16 | M1 | kastela/cdl_003 Mastrinka, the Olive of Kašt | kastela | Olive (Olea sp.) | 650 cm | publish | [cdl_003](https://ancienttrees.app/kastela/mastrinka-the-olive-of-kastel-stafilic) |
| 2026-11-16 | Z1 | Phytolacca dioica | essaouira | Phytolacca dioica | 1000 cm | publish | [ess_001](https://ancienttrees.app/essaouira/ombu-of-the-essaouira-medina) |
| 2026-11-16 | Z1 | The Ombu of the Essaouira Medina | Essaouira | Ombu (Phytolacca dioica) | 1000 cm | publish | [ess_001](https://ancienttrees.app/essaouira/ombu-of-the-essaouira-medina) |
| 2026-11-16 | A2 | Pedunculate Oak (3 photos) | - | Pedunculate Oak | 200 cm | lead | - |
| 2026-11-16 | B2 | Prince Eugen's Oak | - | Oak (Quercus sp.) | - | hold | - |
| 2026-11-16 | C2 | A tree near Helmond | - | - | - | lead | - |
| 2026-11-16 | D2 | The Tassili cypress | Tassili Plateau, Algeria | Cypress (Cupressus sp.) | - | lead | - |
| 2026-11-16 | K1 | Pendulate Oak | Norheimsund | Oak (Quercus sp.) | 706 cm | publish | - |
| 2026-11-16 | E2 | Yew | Vigeois | Yew (Taxus sp.) | - | publish | - |
| 2026-11-16 | F2 | - | kamakura | broad-leaved evergreen, knobbl | - | publish | [kmk_003](https://ancienttrees.app/kamakura/tabunoki-of-the-goryo-shrine-at-sakanoshita) |
| 2026-11-16 | S | - | bilbao | bare spreading crown, dark fur | - | publish | [bil_004](https://ancienttrees.app/bilbao/centenary-horse-chestnut-of-parque-de-dona-casilda) |
| 2026-11-16 | E | - | - | tall tapering red-brown fibrou | - | hold | - |
| 2026-11-16 | G2 | - | - | ridged furrowed bark, spreadin | - | hold | - |
| 2026-11-16 | G2 | - | boston | ginkgo crown, fan leaves | - | publish | [bos_051](https://ancienttrees.app/boston/public-garden-ginkgo) |
| 2026-11-16 | E | - | bristol | giant sequoia, fibrous red bar | - | publish | [bri_018](https://ancienttrees.app/bristol/wellingtonias-by-the-lower-pond-combe-dingle) |
| 2026-11-16 | G2 | - | boston | deeply ridged oak bark, spread | - | publish | [bos_052](https://ancienttrees.app/boston/public-garden-bur-oak) |
| 2026-11-16 | G | - | setubal | melaleuca, low twisted domes | - | publish | [stb_004](https://ancienttrees.app/setubal/melaleuca-that-grows-sideways) |
| 2026-11-16 | G2 | - | boston | compound leaves, fissured trun | - | publish | [bos_047](https://ancienttrees.app/boston/public-garden-pagoda-tree) |
| 2026-11-16 | S | - | bilbao | feathery russet foliage, buttr | - | publish | [bil_002](https://ancienttrees.app/bilbao/bald-cypress-of-deusto) |
| 2026-11-16 | H2 | - | llanerfyl | yew, red fluted trunks | - | publish | [lef_001](https://ancienttrees.app/llanerfyl/llanerfyl-yew) |
| 2026-11-16 | I2 | - | olympic-national-park | Sitka spruce bark and crown | - | publish | [oly_004](https://ancienttrees.app/olympic-national-park/quinault-big-spruce) |
| 2026-11-16 | I2 | - | olympic-national-park | spruce foliage on a root-held  | - | publish | [oly_003](https://ancienttrees.app/olympic-national-park/tree-of-life) |
| 2026-11-16 | V | - | borrowdale | yew needles, arils, fluted tru | - | publish | [bwd_001](https://ancienttrees.app/borrowdale/borrowdale-yews-the-fraternal-four) |
| 2026-11-16 | E | - | bristol | oak branching, lobed leaves | - | publish | [bri_016](https://ancienttrees.app/bristol/bundle-planted-sessile-oak-bishops-knoll) |
| 2026-11-16 | J2 | A tree near Westonbirt Arboretum | - | - | - | lead | - |
| 2026-11-16 | K2 | Leccio (Quercus Ilex) nel piazzale della sta | San Bonifacio | Oak (Quercus sp.) | 265 cm | publish | - |
| 2026-11-16 | L2 | The Lietzensee Plane | Berlin | London Plane (Platanus x aceri | - | publish | [ber_016](https://ancienttrees.app/berlin/lietzensee-plane) |
| 2026-11-16 | S | The Plane Trees of Jardines de Albia | Bilbao | London Plane (Platanus x aceri | - | publish | [bil_001](https://ancienttrees.app/bilbao/plane-trees-of-jardines-de-albia) |
| 2026-11-16 | S | The Centenary Trees of Parque de la Miserico | Bilbao | Canary Island Date Palm (Phoen | - | publish | [bil_003](https://ancienttrees.app/bilbao/centenary-trees-of-parque-de-la-misericordia) |
| 2026-11-16 | M2 | The Great Plane of Brunswick Square | London | London Plane (Platanus x aceri | - | publish | [lon_016](https://ancienttrees.app/london/great-plane-of-brunswick-square) |
| 2026-11-16 | N2 | The Huff Creek Road White Pine | Nicolet National Forest | Eastern White Pine (Pinus stro | - | publish | [nfw_001](https://ancienttrees.app/nicolet-national-forest/huff-creek-road-white-pine) |
| 2026-11-15 | O2 | River Red Gum (2 photos) | adelaide | River Red Gum | - | publish | [ads_001](https://ancienttrees.app/adelaide/red-gum-of-the-rostrevor-creek) |
| 2026-11-15 | P2 | Canary Pine | moss-vale | Canary Pine | 300 cm | publish | [mvv_001](https://ancienttrees.app/moss-vale/canary-pine-of-leighton-gardens) |
| 2026-11-15 | Q2 | Veteran Lime (Linden) Tree | milton-keynes | Lime (Tilia sp.) | - | publish | [mkn_001](https://ancienttrees.app/milton-keynes/linford-lime) |
| 2026-11-15 | R2 | Coldwaltham Yew (2 photos) | Coldwaltham | - | - | publish | [cwh_001](https://ancienttrees.app/coldwaltham/coldwaltham-yew) |
| 2026-11-15 | S2 | The Belvoir Oak | Belfast | - | - | publish | [bfs_001](https://ancienttrees.app/belfast/belvoir-oak) |
| 2026-11-15 | T2 | The Fulham Palace Oak | London | - | - | publish | [lon_007](https://ancienttrees.app/london/fulham-palace-oak) |
| 2026-11-15 | T2 | Barney the Plane | London | - | - | publish | [lon_008](https://ancienttrees.app/london/barney-the-plane) |
| 2026-11-15 | U2 | The Argyle Street Ash | Glasgow | - | - | publish | [gla_005](https://ancienttrees.app/glasgow/argyle-street-ash) |
| 2026-11-15 | U2 | El Drago Milenario (2 photos) | Tenerife | - | - | publish | [tfe_001](https://ancienttrees.app/tenerife/el-drago-milenario) |
| 2026-11-15 | T2 | The Ravenscourt Park Baobab Plane | London | - | - | publish | [lon_018](https://ancienttrees.app/london/ravenscourt-park-baobab-plane) |
| 2026-11-15 | P2 | Canary Pine, Moss Vale | moss-vale | - | - | publish | [mvv_001](https://ancienttrees.app/moss-vale/canary-pine-of-leighton-gardens) |
| 2026-11-15 | O2 | River Red Gum, Rostrevor | adelaide | - | - | publish | [ads_001](https://ancienttrees.app/adelaide/red-gum-of-the-rostrevor-creek) |
| 2026-11-15 | V2 | Sessile Oak near London | london | Sessile Oak | - | publish | [lon_050](https://ancienttrees.app/london/bruce-castle-oak) |
| 2026-11-15 | W2 | Endangered Dawn Redwood in Holborn, legal di | - | Dawn Redwood | - | hold | - |
| 2026-11-15 | X2 | Cedar of Lebanon near Defynnog | brecon | Cedar of Lebanon | - | publish | [brk_001](https://ancienttrees.app/brecon/cedar-of-brecon-cathedral) |
| 2026-11-15 | Y2 | Ancient Lappa plane tree | argyroupoli | - | 2000 cm | publish | [agy_001](https://ancienttrees.app/argyroupoli/plane-of-the-five-virgins) |
| 2026-11-15 | V2 | The Bruce Castle Oak | London | Sessile Oak (Quercus petraea) | - | publish | [lon_050](https://ancienttrees.app/london/bruce-castle-oak) |
| 2026-11-15 | X2 | The Cedar of Brecon Cathedral | Brecon | Cedar of Lebanon (Cedrus liban | - | publish | [brk_001](https://ancienttrees.app/brecon/cedar-of-brecon-cathedral) |
| 2026-11-15 | Y2 | The Plane of the Five Virgins | Argyroupoli | Oriental Plane (Platanus orien | - | publish | [agy_001](https://ancienttrees.app/argyroupoli/plane-of-the-five-virgins) |
| 2026-11-15 | Z2 | Giant Norfolk Island Pine of Lagoa das Furna | Azores | Norfolk Island Pine (Araucaria | - | publish | [azo_005](https://ancienttrees.app/azores/giant-norfolk-island-pine-of-lagoa-das-furnas) |
| 2026-11-15 | A3 | The Plane of Saint Gerasimos, Omala | Kefalonia | Oriental Plane (Platanus orien | - | publish | [kef_001](https://ancienttrees.app/kefalonia/plane-of-saint-gerasimos-omala) |
| 2026-11-15 | T2 | The Totteridge Yew | London | European Yew (Taxus baccata) | - | publish | [lon_001](https://ancienttrees.app/london/totteridge-yew) |
| 2026-11-15 | T2 | The Ravenscourt Park Tree of Heaven | London | Tree of Heaven (Ailanthus alti | - | publish | [lon_023](https://ancienttrees.app/london/ravenscourt-park-tree-of-heaven) |
| 2026-11-15 | Q2 | Linford Lime | Milton Keynes | Common Lime (Tilia x europaea) | - | publish | [mkn_001](https://ancienttrees.app/milton-keynes/linford-lime) |
| 2026-11-15 | B3 | The Redford Wood Redwood | Edinburgh | Giant Sequoia (Sequoiadendron  | - | publish | [edi_021](https://ancienttrees.app/edinburgh/redford-wood-redwood) |
| 2026-11-15 | C3 | Giant Australian Rubber Tree of Jardim Anton (2 photos) | Azores | Moreton Bay Fig (Ficus macroph | - | hold | - |
| 2026-11-15 | B3 | Robert Louis Stevenson's Yew | Edinburgh | European Yew (Taxus baccata) | - | publish | [edi_017](https://ancienttrees.app/edinburgh/robert-louis-stevensons-yew) |
| 2026-11-15 | B3 | Sitka Spruce in Dunkeld | dunkeld | Sitka Spruce | - | publish | [dnk_009](https://ancienttrees.app/dunkeld/sitka-spruce-at-scone-palace) |
| 2026-11-15 | B3 | Sweet Chestnut | lytham | Sweet Chestnut | 700 cm | publish | [lyt_001](https://ancienttrees.app/lytham/lytham-sweet-chestnut) |
| 2026-11-15 | D3 | Deans Oak | - | - | 1200 cm | hold | - |
| 2026-11-15 | E3 | A giant sequoia | - | - | - | lead | - |
| 2026-11-15 | B3 | The Sitka Spruce at Scone Palace | Dunkeld | - | - | publish | [dnk_009](https://ancienttrees.app/dunkeld/sitka-spruce-at-scone-palace) |
| 2026-11-15 | F3 | The Geelong Ginkgo | Geelong | - | - | publish | [glg_001](https://ancienttrees.app/geelong/geelong-ginkgo) |
| 2026-11-15 | B3 | The Lytham Sweet Chestnut | Lytham | - | - | publish | [lyt_001](https://ancienttrees.app/lytham/lytham-sweet-chestnut) |
| 2026-11-15 | T2 | The Royal Oak | London | - | - | publish | [lon_002](https://ancienttrees.app/london/royal-oak) |
| 2026-11-15 | T2 | The Windrush Square Plane | London | - | - | publish | [lon_044](https://ancienttrees.app/london/windrush-square-plane) |
| 2026-11-15 | G3 | The Kyushaku-fuji of Byakugo-ji | Tamba | - | - | publish | [tmb_002](https://ancienttrees.app/tamba/kyushaku-fuji-of-byakugo-ji) |
| 2026-11-15 | G3 | Camphor Tree | nagasaki | Camphor Tree | 658 cm | publish | [ngs_001](https://ancienttrees.app/nagasaki/a-bombed-camphors-of-sanno-shrine) |
| 2026-11-15 | G3 | Japanese Black Pine near Kyoto | otsu | Japanese Black Pine | 390 cm | publish | [ots_001](https://ancienttrees.app/otsu/pine-of-ukimido) |
| 2026-11-15 | H3 | European Beech in London | london | European Beech | - | publish | [lon_052](https://ancienttrees.app/london/gnarled-beech-of-hampstead-heath) |
| 2026-11-15 | I3 | American Sycamore near Media | willistown | American Sycamore | 650 cm | publish | [wtn_001](https://ancienttrees.app/willistown/sycamore-at-the-crum-creek-bridge) |
| 2026-11-15 | B3 | Wheatley Elm in Edinburgh | edinburgh | Wheatley Elm | 400 cm | publish | [edi_022](https://ancienttrees.app/edinburgh/wheatley-elm-of-balgreen) |
| 2026-11-15 | J3 | Giant sequoia in the heart of Geashill | geashill | Giant sequoia (Sequiadendron g | - | publish | [gsh_001](https://ancienttrees.app/geashill/geashill-sequoia) |
| 2026-11-15 | K3 | The King of the Forest | dunkeld | Scots Pine | 660 cm | publish | [dnk_010](https://ancienttrees.app/dunkeld/king-of-the-forest) |
| 2026-11-15 | L3 | Scots Pine in Dunkeld | - | Scots Pine | 660 cm | hold | - |
| 2026-11-15 | M3 | Ancient eastern plane tree on Çınar Street | isparta | - | 400 cm | publish | [isp_001](https://ancienttrees.app/isparta/plane-of-cnar-sokak) |
| 2026-11-15 | N3 | Old Knobbley | - | - | 950 cm | publish | - |
| 2026-11-15 | O3 | Tree in Waitangi | - | - | - | lead | - |
| 2026-11-15 | P3 | The Great Oriental Plane Tree, Emmanuel Coll | - | - | 478 cm | hold | - |
| 2026-11-15 | Q3 | The picture card perfect pines in Connamara | - | - | - | publish | - |
| 2026-11-15 | R3 | Mariam Dearit (also known as the Madonna of  | keren | - | 700 cm | publish | [krn_001](https://ancienttrees.app/keren/mariam-dearit) |
| 2026-11-15 | G3 | The A-bombed Camphors of Sanno Shrine | Nagasaki | - | - | publish | [ngs_001](https://ancienttrees.app/nagasaki/a-bombed-camphors-of-sanno-shrine) |
| 2026-11-15 | S3 | The Market Bosworth Yew | Market Bosworth | - | - | publish | [mbw_001](https://ancienttrees.app/market-bosworth/market-bosworth-yew) |
| 2026-11-15 | T3 | Kett's Oak | Hethersett | - | - | publish | [hth_001](https://ancienttrees.app/hethersett/ketts-oak) |
| 2026-11-15 | G3 | The Pine of Ukimido | Kyoto | - | - | publish | [ots_001](https://ancienttrees.app/otsu/pine-of-ukimido) |
| 2026-11-15 | H3 | The Gnarled Beech of Hampstead Heath (2 photos) | London | - | - | publish | [lon_052](https://ancienttrees.app/london/gnarled-beech-of-hampstead-heath) |
| 2026-11-15 | U3 | The Giant of Mount Horne | Grenada | - | - | publish | [grn_001](https://ancienttrees.app/grenada/giant-of-mount-horne) |
| 2026-11-15 | B3 | The Wheatley Elm of Balgreen | Edinburgh | - | - | publish | [edi_022](https://ancienttrees.app/edinburgh/wheatley-elm-of-balgreen) |
| 2026-11-15 | V3 | - | oxford | - | - | publish | [oxf_004](https://ancienttrees.app/oxford/pococke-plane) |
| 2026-11-15 | W3 | - | - | - | - | hold | - |
| 2026-11-15 | X3 | - | bristol | - | - | publish | [bri_016](https://ancienttrees.app/bristol/bundle-planted-sessile-oak-bishops-knoll) |
| 2026-11-15 | Y3 | - | santalfio | - | - | publish | [sal_001](https://ancienttrees.app/santalfio/hundred-horse-chestnut) |
| 2026-11-15 | Y3 | - | - | - | - | hold | - |
| 2026-11-15 | Z3 | - | - | - | - | hold | - |
| 2026-11-15 | Z3 | - | bar | - | - | publish | [mtn_001](https://ancienttrees.app/bar/stara-maslina-old-olive-tree-of-mirovica) |
| 2026-11-15 | Z3 | - | - | - | - | hold | - |
| 2026-11-15 | Z3 | - | - | - | - | hold | - |
| 2026-11-15 | W3 | - | - | - | - | hold | - |
| 2026-11-15 | A4 | - | farnham | - | - | publish | [frn_001](https://ancienttrees.app/farnham/waverley-abbey-yew) |
| 2026-11-15 | Q3 | - | gort | - | - | publish | [gor_001](https://ancienttrees.app/gort/autograph-tree) |
| 2026-11-15 | G3 | - | - | - | - | hold | - |
| 2026-11-15 | G3 | - | nagoya | - | - | publish | [ngy_002](https://ancienttrees.app/nagoya/camphor-of-atsuta-shrine) |
| 2026-11-15 | B4 | - | palermo | - | - | publish | [pal_001](https://ancienttrees.app/palermo/ficus-of-piazza-marina) |
| 2026-11-15 | C4 | - | dunkeld | - | - | publish | [dnk_002](https://ancienttrees.app/dunkeld/birnam-oak) |
| 2026-11-15 | C4 | - | dunkeld | - | - | publish | [dnk_002](https://ancienttrees.app/dunkeld/birnam-oak) |
| 2026-11-15 | G3 | - | kyoto | - | - | publish | [kyo_002](https://ancienttrees.app/kyoto/land-boat-pine) |
| 2026-11-15 | D4 | - | york | - | - | publish | [yor_002](https://ancienttrees.app/york/cut-leaved-hornbeam) |
| 2026-11-15 | K3 | The King of the Forest | Dunkeld | - | - | publish | [dnk_010](https://ancienttrees.app/dunkeld/king-of-the-forest) |
| 2026-11-15 | J3 | The Geashill Sequoia | Geashill | - | - | publish | [gsh_001](https://ancienttrees.app/geashill/geashill-sequoia) |
| 2026-11-15 | M3 | The Plane of Cinar Street | Isparta | - | - | publish | [isp_001](https://ancienttrees.app/isparta/plane-of-cnar-sokak) |
| 2026-11-15 | R3 | Mariam Dearit | Keren | - | - | publish | [krn_001](https://ancienttrees.app/keren/mariam-dearit) |
| 2026-11-15 | I3 | The Sycamore at the Crum Creek Bridge (2 photos) | Willistown | - | - | publish | [wtn_001](https://ancienttrees.app/willistown/sycamore-at-the-crum-creek-bridge) |
| 2026-11-15 | E4 | The Moved Giant Sequoia of Fort Boise Park | Boise | - | - | publish | [boi_002](https://ancienttrees.app/boise/moved-giant-sequoia-of-fort-boise-park) |
| 2026-11-15 | F4 | The Lewisham Elm | London | - | - | publish | [lon_045](https://ancienttrees.app/london/lewisham-elm) |
| 2026-11-15 | W3 | The Green Beeches of the Nieuwe Kerkhof (3 photos) | Groningen | - | - | publish | [gro_014](https://ancienttrees.app/groningen/green-beeches-of-the-nieuwe-kerkhof) |
| 2026-11-15 | G4 | The Weeping Beech of the Schwanenbrücke (3 photos) | Munich | - | - | publish | [muc_014](https://ancienttrees.app/munich/weeping-beech-of-the-schwanenbrucke) |
| 2026-11-15 | W3 | The Pollarded Lindens of the Pepergasthuis | Groningen | - | - | publish | [gro_020](https://ancienttrees.app/groningen/pollarded-lindens-of-the-pepergasthuis) |
| 2026-11-15 | H4 | The Brace Elm | Brighton | - | - | publish | [bhm_002](https://ancienttrees.app/brighton/brace-elm) |
| 2026-11-15 | B | Tāne Mahuta (2 photos) | Waipoua Forest | - | - | publish | [wai_001](https://ancienttrees.app/waipoua-forest/tane-mahuta) |
| 2026-11-15 | F4 | The Evelyn Mulberry | London | - | - | publish | [lon_010](https://ancienttrees.app/london/evelyn-mulberry) |
| 2026-11-15 | E4 | The Cedars of the Konigsflugel | Bad Homburg | - | - | publish | [bhg_001](https://ancienttrees.app/bad-homburg/cedars-of-the-konigsflugel) |
| 2026-11-15 | V3 | The Pococke Plane | Oxford | - | - | publish | [oxf_004](https://ancienttrees.app/oxford/pococke-plane) |
| 2026-11-15 | I4 | Great Plane of Mottisfont | Mottisfont | - | - | publish | [mtf_001](https://ancienttrees.app/mottisfont/great-plane-of-mottisfont) |
| 2026-11-15 | G4 | The Fern-leaved Beech of the Amalienburg (2 photos) | Munich | - | - | publish | [muc_013](https://ancienttrees.app/munich/fern-leaved-beech-of-the-amalienburg) |
| 2026-11-15 | E4 | The Temple Tree of Landbohøjskolens Have | Copenhagen | - | - | publish | [cop_005](https://ancienttrees.app/copenhagen/temple-tree-of-landbohojskolens-have) |
| 2026-11-15 | G4 | The Oak of the Dörfchen, Nymphenburg (2 photos) | Munich | - | - | publish | [muc_007](https://ancienttrees.app/munich/oak-of-the-dorfchen-nymphenburg) |
| 2026-11-15 | J4 | The Gomero de la Recoleta (2 photos) | Buenos Aires | - | - | publish | [bai_001](https://ancienttrees.app/buenos-aires/gomero-de-la-recoleta) |
| 2026-11-15 | B | Ashbrittle Yew | Ashbrittle | - | - | publish | [asb_001](https://ancienttrees.app/ashbrittle/ashbrittle-yew) |
| 2026-11-15 | K4 | The Toogood Road Fig | Cairns | - | - | publish | [cns_001](https://ancienttrees.app/cairns/toogood-road-fig) |
| 2026-11-15 | J4 | The Old Olive of Exo Chora | Zakynthos | - | - | publish | [zak_001](https://ancienttrees.app/zakynthos/old-olive-of-exo-chora) |
| 2026-11-15 | J4 | The Fig on the Abraaozinho Trail | Ilha Grande | - | - | publish | [ilg_001](https://ancienttrees.app/ilha-grande/fig-on-the-abraaozinho-trail) |
| 2026-11-15 | E4 | The Tarzan Tree | Algiers | - | - | publish | [alg_001](https://ancienttrees.app/algiers/tarzan-tree) |
| 2026-11-15 | E4 | The Elephant's Foot of Zapotitlan | Zapotitlan Salinas | - | - | publish | [zps_001](https://ancienttrees.app/zapotitlan-salinas/elephants-foot-of-zapotitlan) |
| 2026-11-15 | R2 | The Bromley Oak (2 photos) | London | Pedunculate Oak (Quercus robur | - | publish | [lon_046](https://ancienttrees.app/london/bromley-oak) |
| 2026-11-15 | G3 | The Great Cedar of Kasuga Taisha | Nara | Japanese Cedar (Cryptomeria ja | - | publish | [nra_002](https://ancienttrees.app/nara/great-cedar-of-kasuga-taisha) |
| 2026-11-15 | L4 | The Witch Tree of Fanal | Madeira | Til / Stinkwood (Ocotea foeten | - | hold | - |
| 2026-11-15 | B | Marton Oak | - | Pedunculate Oak | - | hold | - |
| 2026-11-15 | K4 | Weeping Fig | cairns | Weeping Fig | 754 cm | publish | [cns_001](https://ancienttrees.app/cairns/toogood-road-fig) |
| 2026-11-15 | J4 | Olive | zakynthos | Olive | - | publish | [zak_001](https://ancienttrees.app/zakynthos/old-olive-of-exo-chora) |
| 2026-11-15 | E4 | The Tarzan Tree | algiers | Moreton Bay Fig | - | publish | [alg_001](https://ancienttrees.app/algiers/tarzan-tree) |
| 2026-11-15 | E4 | Ponytail Palm / Elephant's Foot | zapotitlan-salinas | Ponytail Palm / Elephant's Foo | - | publish | [zps_001](https://ancienttrees.app/zapotitlan-salinas/elephants-foot-of-zapotitlan) |
| 2026-11-15 | M4 | Malmö | - | - | - | hold | - |
| 2026-11-15 | N4 | Dawn Redwood in Toronto | - | Dawn Redwood | - | lead | - |
| 2026-11-15 | O4 | whole veteran tree beside the manor | valdemarpils | old linden, twisted trunk, lon | - | publish | [vld_001](https://ancienttrees.app/valdemarpils/elku-linden-of-valdemarpils-linden-of-sacrifice) |
| 2026-11-15 | O4 | hollow in the old trunk | valdemarpils | linden bark and hollow | - | publish | [vld_001](https://ancienttrees.app/valdemarpils/elku-linden-of-valdemarpils-linden-of-sacrifice) |
| 2026-11-15 | O4 | trunk and limbs beside manor | valdemarpils | linden trunk and spreading lim | - | publish | [vld_001](https://ancienttrees.app/valdemarpils/elku-linden-of-valdemarpils-linden-of-sacrifice) |
| 2026-11-15 | P4 | veteran oak with steel scaffold | warsaw | pedunculate oak, split trunk w | - | publish | [war_001](https://ancienttrees.app/warsaw/dab-mieszko-i-king-mieszko-is-oak) |
| 2026-11-15 | Q4 | mature beech with unusual bark | york | beech, smooth trunk in autumn  | - | publish | [yor_003](https://ancienttrees.app/york/pear-barked-beech) |
| 2026-11-15 | G4 | large copper beech by the palace | munich | copper beech in rust autumn le | - | publish | [muc_011](https://ancienttrees.app/munich/copper-beech-of-the-badenburg) |
| 2026-11-15 | P4 | tall multi-armed cactus in a car park | seville | giant cardon cactus, many arms | - | publish | [sev_044](https://ancienttrees.app/seville/cardon-of-the-expo) |
| 2026-11-15 | G4 | leaning lime by the lake | munich | old linden leaning over the la | - | publish | [muc_012](https://ancienttrees.app/munich/leaning-lime-of-the-badenburger-see) |
| 2026-11-15 | G4 | leaning lime, lake and dusk light | munich | old linden over the lake | - | publish | [muc_012](https://ancienttrees.app/munich/leaning-lime-of-the-badenburger-see) |
| 2026-11-15 | Q4 | wide-crowned hornbeam in a park | york | hornbeam, bare crown with autu | - | publish | [yor_002](https://ancienttrees.app/york/cut-leaved-hornbeam) |
| 2026-11-15 | R4 | weeping beech trunk and pendant branches | dresden | weeping beech, wide fluted tru | - | publish | [dre_019](https://ancienttrees.app/dresden/weeping-beech-of-helfenberg-park) |
| 2026-11-15 | S4 | banyan-like fig with pillar roots | palermo | Ficus macrophylla, aerial root | - | publish | [pal_003](https://ancienttrees.app/palermo/ficus-of-the-orto-botanico) |
| 2026-11-15 | R4 | ancient lime with hollow trunk | dresden | large-leaved linden, multi-ste | - | publish | [dre_005](https://ancienttrees.app/dresden/kaditzer-linde) |
| 2026-11-15 | B | Giant Tree | humboldt-redwoods-state-park | Giant Sequoia | 1615 cm | publish | [hum_001](https://ancienttrees.app/humboldt-redwoods-state-park/giant-tree) |
| 2026-11-15 | B | Rockefeller - Tall Tree | humboldt-redwoods-state-park | Giant Sequoia | 1280 cm | publish | [hum_002](https://ancienttrees.app/humboldt-redwoods-state-park/tall-tree) |
| 2026-11-15 | T4 | Common Fig | manaccan | Common Fig | - | publish | [mnc_002](https://ancienttrees.app/manaccan/fig-in-manaccan-church-wall) |
| 2026-11-15 | T4 | Monterey Cypress (3 photos) | manaccan | Monterey Cypress | - | publish | [mnc_001](https://ancienttrees.app/manaccan/monterey-cypress-over-the-creek) |
| 2026-11-15 | U4 | The Linton Yew (3 photos) | linton-herefordshire | European Yew | 950 cm | publish | [lnt_001](https://ancienttrees.app/linton-herefordshire/linton-yew) |
| 2026-11-15 | V4 | Blue Jacaranda in Melbourne | - | Blue Jacaranda | - | hold | - |
| 2026-11-15 | W4 | Black Mulberry | lewes | Mulberry (Morus sp.) | - | publish | [lew_001](https://ancienttrees.app/lewes/southover-grange-mulberry) |
| 2026-11-15 | X4 | Cedar of Lebanon | ulverston | Cedar (Cedrus sp.) | 755 cm | publish | [ulv_001](https://ancienttrees.app/ulverston/conishead-priory-cedar) |
| 2026-11-15 | X4 | Douglas fir | ulverston | Fir (Abies sp.) | 582 cm | publish | [ulv_002](https://ancienttrees.app/ulverston/conishead-priory-douglas-fir) |
| 2026-11-15 | P4 | King Jan's Linden | Warsaw | Linden | - | publish | [war_007](https://ancienttrees.app/warsaw/king-jans-linden) |
| 2026-11-15 | E4 | The Fern-leaved Beech of the National Galler | Copenhagen | Fern-leaved Beech | - | publish | [cop_026](https://ancienttrees.app/copenhagen/fern-leaved-beech-of-the-national-gallery) |
| 2026-11-15 | Y4 | The Anseman Oak | New Orleans | - | - | publish | [nol_002](https://ancienttrees.app/new-orleans/anseman-oak) |
| 2026-11-15 | Y4 | The Suicide Oak | New Orleans | - | - | publish | [nol_005](https://ancienttrees.app/new-orleans/suicide-oak) |
| 2026-11-15 | T4 | Wistman's Wood (4 photos) | Dartmoor | - | - | publish | [dmr_001](https://ancienttrees.app/dartmoor/wistmans-wood) |
| 2026-11-15 | T4 | The Fig in Manaccan Church Wall | Manaccan | Common Fig (Ficus carica) | - | publish | [mnc_002](https://ancienttrees.app/manaccan/fig-in-manaccan-church-wall) |
| 2026-11-15 | B | The Tall Tree | Humboldt Redwoods State Park | Coast Redwood (Sequoia semperv | - | publish | [hum_002](https://ancienttrees.app/humboldt-redwoods-state-park/tall-tree) |
| 2026-11-15 | W4 | The Southover Grange Mulberry | Lewes | Mulberry (Morus sp.) | - | publish | [lew_001](https://ancienttrees.app/lewes/southover-grange-mulberry) |
| 2026-11-15 | X4 | The Conishead Priory Cedar | Ulverston | Cedar of Lebanon (Cedrus liban | - | publish | [ulv_001](https://ancienttrees.app/ulverston/conishead-priory-cedar) |
| 2026-11-15 | X4 | The Conishead Priory Douglas Fir | Ulverston | Douglas Fir (Pseudotsuga menzi | - | publish | [ulv_002](https://ancienttrees.app/ulverston/conishead-priory-douglas-fir) |
| 2026-11-15 | W3 | The ANWB Linden of Wilhelminakade | Groningen | Common Lime (Tilia x europaea) | - | publish | [gro_018](https://ancienttrees.app/groningen/anwb-linden-of-wilhelminakade) |
| 2026-11-15 | Z4 | Cedar of Lebanon near Hethersett | norwich | Cedar of Lebanon | - | publish | [nwc_001](https://ancienttrees.app/norwich/norwich-cathedral-cedar) |
| 2026-11-15 | A5 | English Hawthorn | - | English Hawthorn (Crataegus la | 50 cm | lead | - |
| 2026-11-15 | B5 | A tree near Edinburgh | - | - | - | hold | - |
| 2026-11-15 | C5 | Southern Live Oak | ormond-beach | Southern Live Oak | 32 cm | publish | [obc_001](https://ancienttrees.app/ormond-beach/fairchild-oak) |
| 2026-11-15 | C5 | The Fairchild Oak (4 photos) | ormond-beach | Southern Live Oak | 32 cm | publish | [obc_001](https://ancienttrees.app/ormond-beach/fairchild-oak) |
| 2026-11-15 | Z4 | The Norwich Cathedral Cedar (2 photos) | norwich | Cedar of Lebanon | - | publish | [nwc_001](https://ancienttrees.app/norwich/norwich-cathedral-cedar) |
| 2026-11-15 | W3 | The Mespilifolia Oak of Noorderplantsoen (2 photos) | Groningen | Sessile Oak "Mespilifolia" (Qu | - | publish | [gro_016](https://ancienttrees.app/groningen/mespilifolia-oak-of-noorderplantsoen) |
| 2026-11-15 | W3 | The Oak of Martinikerkhof (2 photos) | Groningen | Pedunculate Oak (Quercus robur | - | publish | [gro_007](https://ancienttrees.app/groningen/oak-of-martinikerkhof) |
| 2026-11-15 | D5 | Métaséquoia in La Tène | la-tene | Métaséquoia | 250 cm | publish | [prf_003](https://ancienttrees.app/la-tene/dawn-redwood-of-prefargier) |
| 2026-11-15 | D5 | A tree in La Tène | la-tene | - | - | publish | [prf_004](https://ancienttrees.app/la-tene/weeping-beeches-of-prefargier) |
| 2026-11-15 | D5 | Giant Sequoia in La Tène | la-tene | Giant Sequoia | 705 cm | publish | [prf_002](https://ancienttrees.app/la-tene/tall-cedar-of-prefargier) |
| 2026-11-15 | D5 | Large-leaved Lime in La Tène | la-tene | Large-leaved Lime | - | publish | [prf_005](https://ancienttrees.app/la-tene/large-leaved-lime-of-prefargier) |
| 2026-11-15 | S1 | Elleholmseken (The Oak of Elleholm) | elleholm | Pedunculate Oak | 785 cm | publish | [elh_001](https://ancienttrees.app/elleholm/elleholmseken-the-oak-of-elleholm) |
| 2026-11-15 | J1 | London Plane | maidstone | London Plane | 700 cm | publish | [mdb_001](https://ancienttrees.app/maidstone/baobab-plane-of-penenden-heath) |
| 2026-11-15 | J1 | Pedunculate Oak near Mistley | colchester | Pedunculate Oak | 600 cm | publish | [cls_001](https://ancienttrees.app/colchester/oak-of-clingoe-hill) |
| 2026-11-15 | X1 | Arbour Oak | nottingham | Oak (Quercus sp.) | 700 cm | publish | [ntm_001](https://ancienttrees.app/nottingham/arbour-oak-of-wollaton-park) |
| 2026-11-15 | E5 | The Oriental Plane of Landgoed Bantam | Hilversum | Oriental Plane | - | publish | [hil_001](https://ancienttrees.app/hilversum/oriental-plane-of-landgoed-bantam) |
| 2026-11-15 | F5 | The Hackberry of the Mura Latine | Rome | Hackberry | - | publish | [rom_028](https://ancienttrees.app/rome/hackberry-of-the-mura-latine) |
| 2026-11-15 | S1 | Rumskullaeken (the Kvill Oak) | Rumskulla | Pedunculate Oak | - | publish | [rkm_001](https://ancienttrees.app/rumskulla/rumskullaeken-the-kvill-oak) |
| 2026-11-15 | G5 | The Fremont Tree | Santa Cruz | Coast Redwood | - | publish | [scz_002](https://ancienttrees.app/santa-cruz/fremont-tree) |
| 2026-11-15 | H5 | Te Matua Ngahere | Waipoua Forest | Kauri | - | publish | [wai_002](https://ancienttrees.app/waipoua-forest/te-matua-ngahere) |
| 2026-11-15 | I5 | The Pollard Oaks of Wantisden | Wantisden | Pedunculate Oak | - | publish | [wnt_001](https://ancienttrees.app/wantisden/pollard-oaks-of-wantisden) |
| 2026-11-15 | J1 | The Baobab Plane of Penenden Heath | Maidstone | London Plane | - | publish | [mdb_001](https://ancienttrees.app/maidstone/baobab-plane-of-penenden-heath) |
| 2026-11-15 | J1 | The Oak of Clingoe Hill | Colchester | Pedunculate Oak | - | publish | [cls_001](https://ancienttrees.app/colchester/oak-of-clingoe-hill) |
| 2026-11-15 | J5 | The Library Ginkgo of Carmarthen | Carmarthen | Ginkgo | - | publish | [cmt_001](https://ancienttrees.app/carmarthen/library-ginkgo-of-carmarthen) |
| 2026-11-15 | D5 | The Giant Sequoia of Préfargier | La Tène | Giant Sequoia | - | publish | [prf_002](https://ancienttrees.app/la-tene/tall-cedar-of-prefargier) |
| 2026-11-15 | D5 | The Dawn Redwood of Préfargier | La Tène | Dawn Redwood | - | publish | [prf_003](https://ancienttrees.app/la-tene/dawn-redwood-of-prefargier) |
| 2026-11-15 | D5 | The Weeping Beeches of Préfargier | La Tène | Weeping Beech | - | publish | [prf_004](https://ancienttrees.app/la-tene/weeping-beeches-of-prefargier) |
| 2026-11-15 | D5 | The Large-leaved Lime of Préfargier | La Tène | Large-leaved Lime | - | publish | [prf_005](https://ancienttrees.app/la-tene/large-leaved-lime-of-prefargier) |
| 2026-11-15 | T2 | Grimston's Oak | London | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-15 | K5 | The Plane Trees of the Circus | Bath | London Plane (Platanus x aceri | - | publish | [bat_003](https://ancienttrees.app/bath/plane-trees-of-the-circus) |
| 2026-11-15 | K5 | The Orange Courtyard of the Mezquita | Cordoba | Bitter Orange (Citrus aurantiu | - | publish | [cdb_002](https://ancienttrees.app/cordoba/orange-courtyard-of-the-mezquita) |
| 2026-11-15 | K5 | The Crom Yews | Crom | European Yew (Taxus baccata) | - | hold | - |
| 2026-11-15 | L5 | The Sunderland Buttonball Tree | Sunderland, Massachusetts | American Sycamore (Platanus oc | - | publish | [snd_001](https://ancienttrees.app/sunderland-massachusetts/sunderland-buttonball-tree) |
| 2026-11-15 | K5 | The Dawn Redwood by the Kelvin Statue (2 photos) | Belfast | Dawn Redwood (Metasequoia glyp | - | hold | - |
| 2026-11-15 | K5 | S'Olivera de Cort (2 photos) | Palma de Mallorca | Olive (Olea europaea) | - | hold | - |
| 2026-11-15 | L5 | Jackson's Oak | Mobile | Southern Live Oak (Quercus vir | - | publish | [mob_003](https://ancienttrees.app/mobile/jacksons-oak) |
| 2026-11-15 | L5 | Endicott Pear Tree | Boston | European Pear (Pyrus communis) | - | publish | [bos_013](https://ancienttrees.app/boston/endicott-pear-tree) |
| 2026-11-15 | K5 | The Olive of the Orange Courtyard | Cordoba | Olive (Olea europaea) | - | publish | [cdb_001](https://ancienttrees.app/cordoba/olive-of-the-orange-courtyard) |
| 2026-11-15 | M5 | Methuselah Tree (Coast Redwood) | woodside | Coast Redwood | - | publish | [wdd_001](https://ancienttrees.app/woodside/methuselah-tree) |
| 2026-11-15 | N5 | A tree near Sēja | - | - | - | lead | - |
| 2026-11-15 | N5 | A tree near Przybudki | - | - | - | lead | - |
| 2026-11-15 | N5 | A tree near Chiang Mai | - | - | - | lead | - |
| 2026-11-15 | U1 | The Old Yew Tree, St Cuthberts | doveridge | European Yew | - | publish | [dvr_001](https://ancienttrees.app/doveridge/doveridge-yew) |
| 2026-11-15 | U1 | Birch in Cannock Chase | cannock-chase | Birch | - | publish | [cnk_004](https://ancienttrees.app/cannock-chase/plaited-birch-of-brocton) |
| 2026-11-15 | V1 | Moreton Bay Fig in Brisbane | brisbane | Moreton Bay Fig | - | publish | [bne_022](https://ancienttrees.app/brisbane/fig-of-neal-macrossan-park) |
| 2026-11-15 | B | Bodhi Tree at Buddha’s Birthplace | lumbini | Bodhi Tree | - | publish | [lmb_001](https://ancienttrees.app/lumbini/bodhi-tree-of-lumbini) |
| 2026-11-15 | O5 | Sweet Chestnut in London: a Woodland Trust t | london | Sweet Chestnut | - | publish | [lon_053](https://ancienttrees.app/london/twisted-sweet-chestnut-of-greenwich-park) |
| 2026-11-15 | P5 | European Yew near Wilmington | crowhurst | European Yew | 1030 cm | publish | [crh_001](https://ancienttrees.app/crowhurst/crowhurst-yew) |
| 2026-11-15 | Q | Il cipresso calvo di Villa Smeraldi | - | Cypress (Cupressus sp.) | - | lead | - |
| 2026-11-15 | Q | Quercia di Molinazzo | poggio-renatico | Oak (Quercus sp.) | 460 cm | publish | [pgr_001](https://ancienttrees.app/poggio-renatico/oak-of-molinazzo) |
| 2026-11-15 | Q5 | Ardkinglas Grand Fir | Ardkinglas | Grand Fir | - | publish | [akw_001](https://ancienttrees.app/ardkinglas/ardkinglas-grand-fir) |
| 2026-11-15 | Q5 | Ardkinglas Silver Fir, the Mightiest Conifer | Ardkinglas | Silver Fir | - | publish | [akw_002](https://ancienttrees.app/ardkinglas/ardkinglas-silver-fir-the-mightiest-conifer) |
| 2026-11-15 | D | Library Park Fig | Los Angeles | Fig | - | publish | [lax_031](https://ancienttrees.app/los-angeles/library-park-fig) |
| 2026-11-15 | E5 | The Variegated Maple of Coevorden Castle | Emmen | Maple | - | publish | [emm_008](https://ancienttrees.app/emmen/variegated-maple-of-coevorden-castle) |
| 2026-11-15 | K5 | The Twin Cypresses of the Parador | Granada | Cypress | - | publish | [gra_007](https://ancienttrees.app/granada/twin-cypresses-of-the-parador) |
| 2026-11-15 | R5 | Xemxija Old Carob Tree | Malta | Carob | - | publish | [mlt_001](https://ancienttrees.app/malta/xemxija-old-carob-tree) |
| 2026-11-15 | N5 | Yang Na of the City Pillar, Wat Chedi Luang | Chiang Mai | Yang Na | - | hold | - |
| 2026-11-15 | K5 | The Boole Library Redwoods | Cork | Redwood | - | hold | - |
| 2026-11-15 | N5 | The Glasnevin Hybrid Strawberry Tree | Dublin | Hybrid Strawberry Tree | - | hold | - |
| 2026-11-15 | P5 | The Bowthorpe Oak | Bowthorpe | - | - | publish | [bow_001](https://ancienttrees.app/bowthorpe/bowthorpe-oak) |
| 2026-11-15 | P5 | The Crowhurst Yew | Crowhurst | - | - | publish | [crh_001](https://ancienttrees.app/crowhurst/crowhurst-yew) |
| 2026-11-15 | U1 | The Doveridge Yew | Doveridge | - | - | publish | [dvr_001](https://ancienttrees.app/doveridge/doveridge-yew) |
| 2026-11-15 | O5 | The Twisted Sweet Chestnut of Greenwich Park | London | - | - | publish | [lon_053](https://ancienttrees.app/london/twisted-sweet-chestnut-of-greenwich-park) |
| 2026-11-15 | M5 | The Methuselah Tree | Woodside | - | - | publish | [wdd_001](https://ancienttrees.app/woodside/methuselah-tree) |
- From 148 readers: reader B 9, reader G3 9, reader B3 8, reader D5 8, reader E4 8, reader K5 8, reader T2 8, reader W3 7, reader G4 6, reader D 5, reader D1 5, reader J1 5, reader N5 5, reader S 5, reader B1 4, reader E 4, reader G 4, reader G2 4, reader J4 4, reader N 4, reader Q 4, reader T4 4, reader U1 4, reader X4 4, reader Z 4, reader Z3 4, reader C1 3, reader J 3, reader K1 3, reader L5 3, reader M1 3, reader O4 3, reader P 3, reader P4 3, reader P5 3, reader S1 3, reader A 2, reader A1 2, reader C4 2, reader C5 2, reader E1 2, reader E5 2, reader F4 2, reader G1 2, reader H 2, reader H3 2, reader I2 2, reader I3 2, reader J3 2, reader K3 2, reader K4 2, reader L1 2, reader M3 2, reader M5 2, reader N1 2, reader O2 2, reader O5 2, reader P2 2, reader Q2 2, reader Q3 2, reader Q4 2, reader Q5 2, reader R1 2, reader R2 2, reader R3 2, reader R4 2, reader T 2, reader U2 2, reader V 2, reader V1 2, reader V2 2, reader V3 2, reader W1 2, reader W4 2, reader X1 2, reader X2 2, reader Y 2, reader Y2 2, reader Y3 2, reader Y4 2, reader Z1 2, reader Z4 2, reader A2 1, reader A3 1, reader A4 1, reader A5 1, reader B2 1, reader B4 1, reader B5 1, reader C 1, reader C2 1, reader C3 1, reader D2 1, reader D3 1, reader D4 1, reader E2 1, reader E3 1, reader F 1, reader F1 1, reader F2 1, reader F3 1, reader F5 1, reader G5 1, reader H1 1, reader H2 1, reader H4 1, reader H5 1, reader I 1, reader I1 1, reader I4 1, reader I5 1, reader J2 1, reader J5 1, reader K 1, reader K2 1, reader L 1, reader L2 1, reader L3 1, reader L4 1, reader M 1, reader M2 1, reader M4 1, reader N2 1, reader N3 1, reader N4 1, reader O 1, reader O1 1, reader O3 1, reader P1 1, reader P3 1, reader Q1 1, reader R 1, reader R5 1, reader S2 1, reader S3 1, reader S4 1, reader T1 1, reader T3 1, reader U 1, reader U3 1, reader U4 1, reader V4 1, reader W 1, reader W2 1, reader X 1, reader X3 1, reader Y1 1, reader Z2 1.
- Photographs and the readers' own words: `python3 scripts/inspect_readers.py` (a local page, never in this public file). Your answer goes in with `python3 scripts/judgement.py --feedback <id> "..."`.

**Waiting for you** (what the runs left for you since 2026-11-16)

- 246 email addresses ready to mail (archive 0, nature 9, guide 8, press 135, source 58, council 16, society 7, tourism 5, other 5, garden 3); **the night run found no new contacts in two days**
- the daily task "publish-held-trees-daily" can be switched off under Scheduled; write passes put trees straight into the app, so nothing waits for it.
- preflight's note says a stranger's photo plus GPS is held back only for wrong tree, subject or frame; the leads above (and about 15 like them from 11-15/16)
- next iOS build carries it.** No difference between iPhone and Android, so nothing in data/android-parity.json.
- (1)

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-15 | R2 | Coldwaltham Yew | Coldwaltham | a reader's photograph, published | [live](https://ancienttrees.app/coldwaltham/coldwaltham-yew) |
| 11-15 | S2 | The Belvoir Oak | Belfast | a reader's photograph, published | [live](https://ancienttrees.app/belfast/belvoir-oak) |
| 11-15 | T2 | The Fulham Palace Oak | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/fulham-palace-oak) |
| 11-15 | T2 | Barney the Plane | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/barney-the-plane) |
| 11-15 | U2 | The Argyle Street Ash | Glasgow | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/glasgow/argyle-street-ash) |
| 11-15 | U2 | El Drago Milenario | Tenerife | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tenerife/el-drago-milenario) |
| 11-15 | T2 | The Ravenscourt Park Baobab Plane | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/ravenscourt-park-baobab-plane) |
| 11-15 | O2 | The Red Gum of the Rostrevor Creek | Adelaide | a reader's photograph, published | [live](https://ancienttrees.app/adelaide/red-gum-of-the-rostrevor-creek) |
| 11-15 | P2 | The Canary Pine of Leighton Gardens | Moss Vale | a reader's photograph, published | [live](https://ancienttrees.app/moss-vale/canary-pine-of-leighton-gardens) |
| 11-15 | T2 | The Totteridge Yew | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/totteridge-yew) |
| 11-15 | T2 | The Ravenscourt Park Tree of Heaven | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/ravenscourt-park-tree-of-heaven) |
| 11-15 | A3 | The Plane of Saint Gerasimos, Omala | Kefalonia | a reader's photograph, published | [live](https://ancienttrees.app/kefalonia/plane-of-saint-gerasimos-omala) |
| 11-15 | Z2 | Giant Norfolk Island Pine of Lagoa das Furnas | Azores | a reader's photograph, published | [live](https://ancienttrees.app/azores/giant-norfolk-island-pine-of-lagoa-das-furnas) |
| 11-15 | V2 | The Bruce Castle Oak | London | a reader's photograph, published | [live](https://ancienttrees.app/london/bruce-castle-oak) |
| 11-15 | X2 | The Cedar of Brecon Cathedral | Brecon | a reader's photograph, published | [live](https://ancienttrees.app/brecon/cedar-of-brecon-cathedral) |
| 11-15 | B3 | The Redford Wood Redwood | Edinburgh | a reader's photograph, published | [live](https://ancienttrees.app/edinburgh/redford-wood-redwood) |
| 11-15 | C3 | Giant Australian Rubber Tree of Jardim Antonio Borges | Azores | a reader's photograph, published | [live](https://ancienttrees.app/azores/giant-australian-rubber-tree-of-jardim-antonio-borges) |
| 11-15 | B3 | Robert Louis Stevenson's Yew | Edinburgh | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/edinburgh/robert-louis-stevensons-yew) |
| 11-15 | B3 | The Sitka Spruce at Scone Palace | Dunkeld | a reader's photograph, published | [live](https://ancienttrees.app/dunkeld/sitka-spruce-at-scone-palace) |
| 11-15 | B3 | The Lytham Sweet Chestnut | Lytham | a reader's photograph, published | [live](https://ancienttrees.app/lytham/lytham-sweet-chestnut) |
| 11-15 | F3 | The Geelong Ginkgo | Geelong | a reader's photograph, published | [live](https://ancienttrees.app/geelong/geelong-ginkgo) |
| 11-15 | G3 | The Kyushaku-fuji of Byakugo-ji | Tamba | a reader's photograph, published | [live](https://ancienttrees.app/tamba/kyushaku-fuji-of-byakugo-ji) |
| 11-15 | T2 | The Royal Oak | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/royal-oak) |
| 11-15 | T2 | The Windrush Square Plane | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/windrush-square-plane) |
| 11-15 | G3 | The A-bombed Camphors of Sannō Shrine | Nagasaki | a reader's photograph, published | [live](https://ancienttrees.app/nagasaki/a-bombed-camphors-of-sanno-shrine) |
| 11-15 | S3 | The Market Bosworth Yew | Market Bosworth | a reader's photograph, published | [live](https://ancienttrees.app/market-bosworth/market-bosworth-yew) |
| 11-15 | T3 | Kett's Oak | Hethersett | a reader's photograph, published | [live](https://ancienttrees.app/hethersett/ketts-oak) |
| 11-15 | G3 | The Pine of Ukimidō | Ōtsu | a reader's photograph, published | [live](https://ancienttrees.app/otsu/pine-of-ukimido) |
| 11-15 | H3 | The Gnarled Beech of Hampstead Heath | London | a reader's photograph, published | [live](https://ancienttrees.app/london/gnarled-beech-of-hampstead-heath) |
| 11-15 | U3 | The Giant of Mount Horne | Grenada | a reader's photograph, published | [live](https://ancienttrees.app/grenada/giant-of-mount-horne) |
| 11-15 | I3 | The Sycamore at the Crum Creek Bridge | Willistown | a reader's photograph, published | [live](https://ancienttrees.app/willistown/sycamore-at-the-crum-creek-bridge) |
| 11-15 | B3 | The Wheatley Elm of Balgreen | Edinburgh | a reader's photograph, published | [live](https://ancienttrees.app/edinburgh/wheatley-elm-of-balgreen) |
| 11-15 | J3 | The Geashill Sequoia | Geashill | a reader's photograph, published | [live](https://ancienttrees.app/geashill/geashill-sequoia) |
| 11-15 | K3 | The King of the Forest | Dunkeld | a reader's photograph, published | [live](https://ancienttrees.app/dunkeld/king-of-the-forest) |
| 11-15 | M3 | The Plane of Çınar Sokak | Isparta | a reader's photograph, published | [live](https://ancienttrees.app/isparta/plane-of-cnar-sokak) |
| 11-15 | R3 | Mariam Dearit | Keren | a reader's photograph, published | [live](https://ancienttrees.app/keren/mariam-dearit) |
| 11-15 | V3 | The Pococke Plane | Oxford | a reader's photograph, published | [live](https://ancienttrees.app/oxford/pococke-plane) |
| 11-15 | X3 | The Bundle-planted Sessile Oak, Bishops Knoll | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/bundle-planted-sessile-oak-bishops-knoll) |
| 11-15 | Y3 | The Hundred-Horse Chestnut | Sant'Alfio | a reader's photograph, published | [live](https://ancienttrees.app/santalfio/hundred-horse-chestnut) |
| 11-15 | Z3 | Stara Maslina (Old Olive Tree of Mirovica) | Bar | a reader's photograph, published | [live](https://ancienttrees.app/bar/stara-maslina-old-olive-tree-of-mirovica) |
| 11-15 | A4 | Waverley Abbey Yew | Farnham | a reader's photograph, published | [live](https://ancienttrees.app/farnham/waverley-abbey-yew) |
| 11-15 | Q3 | The Autograph Tree | Gort | a reader's photograph, published | [live](https://ancienttrees.app/gort/autograph-tree) |
| 11-15 | G3 | The Camphor of Atsuta Shrine | Nagoya | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/nagoya/camphor-of-atsuta-shrine) |
| 11-15 | B4 | The Ficus of Piazza Marina | Palermo | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/palermo/ficus-of-piazza-marina) |
| 11-15 | C4 | The Birnam Oak | Dunkeld | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dunkeld/birnam-oak) |
| 11-15 | C4 | The Birnam Oak | Dunkeld | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dunkeld/birnam-oak) |
| 11-15 | G3 | The Land Boat Pine | Kyoto | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kyoto/land-boat-pine) |
| 11-15 | D4 | The Cut-Leaved Hornbeam | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/cut-leaved-hornbeam) |
| 11-15 | K4 | The Toogood Road Fig | Cairns | a reader's photograph, published | [live](https://ancienttrees.app/cairns/toogood-road-fig) |
| 11-15 | J4 | The Old Olive of Exo Chora | Zakynthos | a reader's photograph, published | [live](https://ancienttrees.app/zakynthos/old-olive-of-exo-chora) |
| 11-15 | J4 | The Fig on the Abraãozinho Trail | Ilha Grande | a reader's photograph, published | [live](https://ancienttrees.app/ilha-grande/fig-on-the-abraaozinho-trail) |
| 11-15 | E4 | The Tarzan Tree | Algiers | a reader's photograph, published | [live](https://ancienttrees.app/algiers/tarzan-tree) |
| 11-15 | E4 | The Elephant's Foot of Zapotitlán | Zapotitlán Salinas | a reader's photograph, published | [live](https://ancienttrees.app/zapotitlan-salinas/elephants-foot-of-zapotitlan) |
| 11-15 | E4 | The Moved Giant Sequoia of Fort Boise Park | Boise | a reader's photograph, published | [live](https://ancienttrees.app/boise/moved-giant-sequoia-of-fort-boise-park) |
| 11-15 | F4 | The Lewisham Elm | London | a reader's photograph, published | [live](https://ancienttrees.app/london/lewisham-elm) |
| 11-15 | W3 | The Green Beeches of the Nieuwe Kerkhof | Groningen | a reader's photograph, published | [live](https://ancienttrees.app/groningen/green-beeches-of-the-nieuwe-kerkhof) |
| 11-15 | G4 | The Weeping Beech of the Schwanenbrücke | Munich | a reader's photograph, published | [live](https://ancienttrees.app/munich/weeping-beech-of-the-schwanenbrucke) |
| 11-15 | G4 | The Weeping Beech of the Schwanenbrücke | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/weeping-beech-of-the-schwanenbrucke) |
| 11-15 | W3 | The Pollarded Lindens of the Pepergasthuis | Groningen | a reader's photograph, published | [live](https://ancienttrees.app/groningen/pollarded-lindens-of-the-pepergasthuis) |
| 11-15 | H4 | The Brace Elm | Brighton | a reader's photograph, published | [live](https://ancienttrees.app/brighton/brace-elm) |
| 11-15 | B | Tāne Mahuta | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/tane-mahuta) |
| 11-15 | F4 | The Evelyn Mulberry | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/evelyn-mulberry) |
| 11-15 | E4 | The Cedars of the Konigsflugel | Bad Homburg | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/bad-homburg/cedars-of-the-konigsflugel) |
| 11-15 | V3 | The Pococke Plane | Oxford | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/oxford/pococke-plane) |
| 11-15 | I4 | Great Plane of Mottisfont | Mottisfont | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mottisfont/great-plane-of-mottisfont) |
| 11-15 | G4 | The Fern-leaved Beech of the Amalienburg | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/fern-leaved-beech-of-the-amalienburg) |
| 11-15 | E4 | The Temple Tree of Landbohøjskolens Have | Copenhagen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/copenhagen/temple-tree-of-landbohojskolens-have) |
| 11-15 | E4 | El Drago Milenario | Tenerife | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tenerife/el-drago-milenario) |
| 11-15 | G4 | The Oak of the Dörfchen, Nymphenburg | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/oak-of-the-dorfchen-nymphenburg) |
| 11-15 | G4 | The Oak of the Dörfchen, Nymphenburg | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/oak-of-the-dorfchen-nymphenburg) |
| 11-15 | B | The Fortingall Yew | Fortingall | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/fortingall/fortingall-yew) |
| 11-15 | R2 | Coldwaltham Yew | Coldwaltham | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/coldwaltham/coldwaltham-yew) |
| 11-15 | E4 | El Árbol del Tule | Santa María del Tule | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/santa-maria-del-tule/el-arbol-del-tule) |
| 11-15 | I3 | The Sycamore at the Crum Creek Bridge | Willistown | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/willistown/sycamore-at-the-crum-creek-bridge) |
| 11-15 | J4 | The Gomero de la Recoleta | Buenos Aires | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/buenos-aires/gomero-de-la-recoleta) |
| 11-15 | B | Tāne Mahuta | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/tane-mahuta) |
| 11-15 | B | Ashbrittle Yew | Ashbrittle | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/ashbrittle/ashbrittle-yew) |
| 11-15 | O4 | Elku Linden of Valdemārpils (Linden of Sacrifice) | Valdemārpils | a reader's photograph, published | [live](https://ancienttrees.app/valdemarpils/elku-linden-of-valdemarpils-linden-of-sacrifice) |
| 11-15 | O4 | Elku Linden of Valdemārpils (Linden of Sacrifice) | Valdemārpils | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/valdemarpils/elku-linden-of-valdemarpils-linden-of-sacrifice) |
| 11-15 | O4 | Elku Linden of Valdemārpils (Linden of Sacrifice) | Valdemārpils | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/valdemarpils/elku-linden-of-valdemarpils-linden-of-sacrifice) |
| 11-15 | P4 | Dab Mieszko I (King Mieszko I's Oak) | Warsaw | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/warsaw/dab-mieszko-i-king-mieszko-is-oak) |
| 11-15 | Q4 | The Pear-Barked Beech | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/pear-barked-beech) |
| 11-15 | G4 | The Copper Beech of the Badenburg | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/copper-beech-of-the-badenburg) |
| 11-15 | E4 | The Gomero de la Recoleta | Buenos Aires | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/buenos-aires/gomero-de-la-recoleta) |
| 11-15 | G4 | The Fern-leaved Beech of the Amalienburg | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/fern-leaved-beech-of-the-amalienburg) |
| 11-15 | P4 | The Cardón of the Expo | Seville | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/seville/cardon-of-the-expo) |
| 11-15 | G4 | The Leaning Lime of the Badenburger See | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/leaning-lime-of-the-badenburger-see) |
| 11-15 | G4 | The Leaning Lime of the Badenburger See | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/leaning-lime-of-the-badenburger-see) |
| 11-15 | B | The Fortingall Yew | Fortingall | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/fortingall/fortingall-yew) |
| 11-15 | Q4 | The Cut-Leaved Hornbeam | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/cut-leaved-hornbeam) |
| 11-15 | R2 | The Bromley Oak | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/bromley-oak) |
| 11-15 | R2 | The Bromley Oak | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/bromley-oak) |
| 11-15 | G3 | The Great Cedar of Kasuga Taisha | Nara | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/nara/great-cedar-of-kasuga-taisha) |
| 11-15 | R4 | The Weeping Beech of Helfenberg Park | Dresden | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dresden/weeping-beech-of-helfenberg-park) |
| 11-15 | S4 | The Ficus of the Orto Botanico | Palermo | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/palermo/ficus-of-the-orto-botanico) |
| 11-15 | R4 | The Kaditzer Linde | Dresden | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dresden/kaditzer-linde) |
| 11-15 | P4 | King Jan's Linden | Warsaw | a reader's photograph, published | [live](https://ancienttrees.app/warsaw/king-jans-linden) |
| 11-15 | E4 | The Fern-leaved Beech of the National Gallery | Copenhagen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/copenhagen/fern-leaved-beech-of-the-national-gallery) |
| 11-15 | Y4 | The Anseman Oak | New Orleans | a reader's photograph, published | [live](https://ancienttrees.app/new-orleans/anseman-oak) |
| 11-15 | Y4 | The Suicide Oak | New Orleans | a reader's photograph, published | [live](https://ancienttrees.app/new-orleans/suicide-oak) |
| 11-15 | T4 | Wistman's Wood | Dartmoor | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dartmoor/wistmans-wood) |
| 11-15 | T4 | Wistman's Wood | Dartmoor | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dartmoor/wistmans-wood) |
| 11-15 | G4 | The Weeping Beech of the Schwanenbrücke | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/weeping-beech-of-the-schwanenbrucke) |
| 11-15 | W3 | The Mespilifolia Oak of Noorderplantsoen | Groningen | a reader's photograph, published | [live](https://ancienttrees.app/groningen/mespilifolia-oak-of-noorderplantsoen) |
| 11-15 | W3 | The Oak of Martinikerkhof | Groningen | a reader's photograph, published | [live](https://ancienttrees.app/groningen/oak-of-martinikerkhof) |
| 11-15 | W3 | The Green Beeches of the Nieuwe Kerkhof | Groningen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/groningen/green-beeches-of-the-nieuwe-kerkhof) |
| 11-15 | O2 | The Red Gum of Glynburn Road | Adelaide | a reader's photograph, published | [live](https://ancienttrees.app/adelaide/red-gum-of-glynburn-road) |
| 11-15 | B | The Tall Tree | Humboldt Redwoods State Park | a reader's photograph, published | [live](https://ancienttrees.app/humboldt-redwoods-state-park/tall-tree) |
| 11-15 | T4 | The Fig in Manaccan Church Wall | Manaccan | a reader's photograph, published | [live](https://ancienttrees.app/manaccan/fig-in-manaccan-church-wall) |
| 11-15 | U4 | The Linton Yew | Linton, Herefordshire | a reader's photograph, published | [live](https://ancienttrees.app/linton-herefordshire/linton-yew) |
| 11-15 | T4 | The Monterey Cypress over the Creek | Manaccan | a reader's photograph, published | [live](https://ancienttrees.app/manaccan/monterey-cypress-over-the-creek) |
| 11-15 | G5 | The Fremont Tree | Santa Cruz | a reader's photograph, published | [live](https://ancienttrees.app/santa-cruz/fremont-tree) |
| 11-15 | S1 | Rumskullaeken (the Kvill Oak) | Rumskulla | a reader's photograph, published | [live](https://ancienttrees.app/rumskulla/rumskullaeken-the-kvill-oak) |
| 11-15 | W3 | The ANWB Linden of Wilhelminakade | Groningen | a reader's photograph, published | [live](https://ancienttrees.app/groningen/anwb-linden-of-wilhelminakade) |
| 11-15 | E5 | The Oriental Plane of Landgoed Bantam | Hilversum | a reader's photograph, published | [live](https://ancienttrees.app/hilversum/oriental-plane-of-landgoed-bantam) |
| 11-15 | F5 | The Hackberry of the Mura Latine | Rome | a reader's photograph, published | [live](https://ancienttrees.app/rome/hackberry-of-the-mura-latine) |
| 11-15 | H5 | Te Matua Ngahere | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/te-matua-ngahere) |
| 11-15 | Z4 | The Norwich Cathedral Cedar | Norwich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/norwich/norwich-cathedral-cedar) |
| 11-15 | C5 | The Fairchild Oak | Ormond Beach | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/ormond-beach/fairchild-oak) |
| 11-16 | U1 | The Plaited Birch of Brocton | Cannock Chase | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/cannock-chase/plaited-birch-of-brocton) |
| 11-16 | V1 | The Fig of Neal Macrossan Park | Brisbane | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/brisbane/fig-of-neal-macrossan-park) |
| 11-16 | B | The Bodhi Tree of Lumbini | Lumbini | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/lumbini/bodhi-tree-of-lumbini) |
| 11-15 | Q5 | Ardkinglas Silver Fir, the Mightiest Conifer | Ardkinglas | a reader's photograph, published | [live](https://ancienttrees.app/ardkinglas/ardkinglas-silver-fir-the-mightiest-conifer) |
| 11-15 | Q5 | Ardkinglas Grand Fir | Ardkinglas | a reader's photograph, published | [live](https://ancienttrees.app/ardkinglas/ardkinglas-grand-fir) |
| 11-15 | D | Library Park Fig | Los Angeles | a reader's photograph, published | [live](https://ancienttrees.app/los-angeles/library-park-fig) |
| 11-15 | E5 | The Variegated Maple of Coevorden Castle | Emmen | a reader's photograph, published | [live](https://ancienttrees.app/emmen/variegated-maple-of-coevorden-castle) |
| 11-15 | K5 | The Twin Cypresses of the Parador | Granada | a reader's photograph, published | [live](https://ancienttrees.app/granada/twin-cypresses-of-the-parador) |
| 11-15 | R5 | Xemxija Old Carob Tree | Malta | a reader's photograph, published | [live](https://ancienttrees.app/malta/xemxija-old-carob-tree) |
| 11-15 | K5 | The Plane Trees of the Circus | Bath | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/bath/plane-trees-of-the-circus) |
| 11-15 | L5 | Endicott Pear Tree | Boston | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/boston/endicott-pear-tree) |
| 11-15 | K5 | The Olive of the Orange Courtyard | Cordoba | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/cordoba/olive-of-the-orange-courtyard) |
| 11-15 | K5 | The Orange Courtyard of the Mezquita | Cordoba | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/cordoba/orange-courtyard-of-the-mezquita) |
| 11-15 | L5 | Jackson's Oak | Mobile | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mobile/jacksons-oak) |
| 11-15 | L5 | S'Olivera de Cort | Palma de Mallorca | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/palma-de-mallorca/solivera-de-cort) |
| 11-15 | L5 | The Sunderland Buttonball Tree | Sunderland, Massachusetts | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sunderland-massachusetts/sunderland-buttonball-tree) |
| 11-16 | Y | The Airport Oak of Earlysville | Earlysville | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/earlysville/airport-oak-of-earlysville) |
| 11-16 | Z | The Big Totara of Lillburn Monowai Road | Tuatapere | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tuatapere/big-totara-of-lillburn-monowai-road) |
| 11-16 | Z | The Curtain Fig Tree | Yungaburra | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/yungaburra/curtain-fig-tree) |
| 11-16 | A1 | The Hollow Yew of La Lande-Patry | La Lande-Patry | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/la-lande-patry/hollow-yew-of-la-lande-patry) |
| 11-16 | C1 | The Baobab of Mbissel | Mbissel | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mbissel/baobab-of-mbissel) |
| 11-16 | C1 | The Sagole Baobab | Sagole | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sagole/sagole-baobab) |
| 11-16 | E1 | The Cavenagh Street Boab | Darwin | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/darwin/cavenagh-street-boab) |
| 11-16 | G1 | The Becks Prime Augusta Live Oaks | Houston | a reader's photograph, published | [live](https://ancienttrees.app/houston/becks-prime-augusta-live-oaks) |
| 11-16 | G1 | The Old Pecan Tree | Houston | a reader's photograph, published | [live](https://ancienttrees.app/houston/old-pecan-tree) |
| 11-16 | H1 | The Kapok Tree | Key West | a reader's photograph, published | [live](https://ancienttrees.app/key-west/kapok-tree) |
| 11-16 | I1 | The Rhodes Bald Cypress | Richard Bong State Recreation Area | a reader's photograph, published | [live](https://ancienttrees.app/richard-bong-state-recreation-area/rhodes-bald-cypress) |
| 11-16 | V | The Borrowdale Yews (the Fraternal Four) | Borrowdale | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/borrowdale/borrowdale-yews-the-fraternal-four) |
| 11-16 | X | The Angel Oak | Charleston | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/charleston/angel-oak) |
| 11-16 | W | Ahuehuete de Parque Espana | Mexico City | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mexico-city/ahuehuete-de-parque-espana) |
| 11-16 | W | Ahuehuete de Parque Espana | Mexico City | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mexico-city/ahuehuete-de-parque-espana) |
| 11-16 | K1 | The Old Oak at Tolo | Kvam | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kvam/old-oak-at-tolo) |
| 11-16 | N1 | The Aogiri of Peace Memorial Park | Hiroshima | a reader's photograph, published | [live](https://ancienttrees.app/hiroshima/aogiri-of-peace-memorial-park) |
| 11-16 | O1 | The Embracing Fig of the Giardini Reali | Palermo | a reader's photograph, published | [live](https://ancienttrees.app/palermo/embracing-fig-of-the-giardini-reali) |
| 11-16 | P1 | Enchanted Balete Tree of Lazi | Siquijor | a reader's photograph, published | [live](https://ancienttrees.app/siquijor/enchanted-balete-tree-of-lazi) |
| 11-16 | Q1 | Millennium Tree of Balete Park | Maria Aurora | a reader's photograph, published | [live](https://ancienttrees.app/maria-aurora/millennium-tree-of-balete-park) |
| 11-16 | R1 | El Árbol del Tule | Santa María del Tule | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/santa-maria-del-tule/el-arbol-del-tule) |
| 11-16 | S1 | Elleholmseken (The Oak of Elleholm) | Elleholm | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/elleholm/elleholmseken-the-oak-of-elleholm) |
| 11-16 | N1 | The Willow Nearest the Hypocentre | Hiroshima | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/hiroshima/willow-nearest-the-hypocentre) |
| 11-16 | R1 | The Fortingall Yew | Fortingall | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/fortingall/fortingall-yew) |
| 11-16 | D1 | General Sherman Tree | Sequoia National Park | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sequoia-national-park/general-sherman-tree) |
| 11-16 | D1 | Lincoln Tree | Sequoia National Park | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sequoia-national-park/lincoln-tree) |
| 11-16 | T1 | The Sacred Olive Tree of the Acropolis | Athens | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/athens/sacred-olive-tree-of-the-acropolis) |
| 11-16 | D5 | The Dawn Redwood of Préfargier | La Tène | a reader's photograph, published | [live](https://ancienttrees.app/la-tene/dawn-redwood-of-prefargier) |
| 11-16 | D5 | The Weeping Beeches of Préfargier | La Tène | a reader's photograph, published | [live](https://ancienttrees.app/la-tene/weeping-beeches-of-prefargier) |
| 11-16 | D5 | The Large-leaved Lime of Préfargier | La Tène | a reader's photograph, published | [live](https://ancienttrees.app/la-tene/large-leaved-lime-of-prefargier) |
| 11-16 | S1 | Elleholmseken (The Oak of Elleholm) | Elleholm | a reader's photograph, published | [live](https://ancienttrees.app/elleholm/elleholmseken-the-oak-of-elleholm) |
| 11-16 | I5 | The Pollard Oaks of Wantisden | Wantisden | a reader's photograph, published | [live](https://ancienttrees.app/wantisden/pollard-oaks-of-wantisden) |
| 11-16 | J1 | The Baobab Plane of Penenden Heath | Maidstone | a reader's photograph, published | [live](https://ancienttrees.app/maidstone/baobab-plane-of-penenden-heath) |
| 11-16 | J1 | The Oak of Clingoe Hill | Colchester | a reader's photograph, published | [live](https://ancienttrees.app/colchester/oak-of-clingoe-hill) |
| 11-16 | J5 | The Library Ginkgo of Carmarthen | Carmarthen | a reader's photograph, published | [live](https://ancienttrees.app/carmarthen/library-ginkgo-of-carmarthen) |
| 11-16 | M5 | The Methuselah Tree | Woodside | a reader's photograph, published | [live](https://ancienttrees.app/woodside/methuselah-tree) |
| 11-16 | U1 | The Doveridge Yew | Doveridge | a reader's photograph, published | [live](https://ancienttrees.app/doveridge/doveridge-yew) |
| 11-16 | P5 | The Crowhurst Yew | Crowhurst | a reader's photograph, published | [live](https://ancienttrees.app/crowhurst/crowhurst-yew) |
| 11-16 | O5 | The Twisted Sweet Chestnut of Greenwich Park | London | a reader's photograph, published | [live](https://ancienttrees.app/london/twisted-sweet-chestnut-of-greenwich-park) |
| 11-16 | P5 | The Bowthorpe Oak | Bowthorpe | a reader's photograph, published | [live](https://ancienttrees.app/bowthorpe/bowthorpe-oak) |
| 11-16 | F2 | The Tabunoki of the Goryo Shrine at Sakanoshita | Kamakura | a reader's photograph, published | [live](https://ancienttrees.app/kamakura/tabunoki-of-the-goryo-shrine-at-sakanoshita) |
| 11-16 | S | The Centenary Horse Chestnut of Parque de Doña Casilda | Bilbao | a reader's photograph, published | [live](https://ancienttrees.app/bilbao/centenary-horse-chestnut-of-parque-de-dona-casilda) |
| 11-16 | G2 | The Public Garden Ginkgo | Boston | a reader's photograph, published | [live](https://ancienttrees.app/boston/public-garden-ginkgo) |
| 11-16 | E | The Wellingtonias by the Lower Pond, Combe Dingle | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/wellingtonias-by-the-lower-pond-combe-dingle) |
| 11-16 | G2 | The Public Garden Bur Oak | Boston | a reader's photograph, published | [live](https://ancienttrees.app/boston/public-garden-bur-oak) |
| 11-16 | G | The Melaleuca That Grows Sideways | Setubal | a reader's photograph, published | [live](https://ancienttrees.app/setubal/melaleuca-that-grows-sideways) |
| 11-16 | G2 | The Public Garden Pagoda Tree | Boston | a reader's photograph, published | [live](https://ancienttrees.app/boston/public-garden-pagoda-tree) |
| 11-16 | S | The Bald Cypress of Deusto | Bilbao | a reader's photograph, published | [live](https://ancienttrees.app/bilbao/bald-cypress-of-deusto) |
| 11-16 | H2 | Llanerfyl Yew | Llanerfyl | a reader's photograph, published | [live](https://ancienttrees.app/llanerfyl/llanerfyl-yew) |
| 11-16 | I2 | The Quinault Big Spruce | Olympic National Park | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/olympic-national-park/quinault-big-spruce) |
| 11-16 | I2 | The Tree of Life | Olympic National Park | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/olympic-national-park/tree-of-life) |
| 11-16 | V | The Borrowdale Yews (the Fraternal Four) | Borrowdale | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/borrowdale/borrowdale-yews-the-fraternal-four) |
| 11-16 | E | The Bundle-planted Sessile Oak, Bishops Knoll | Bristol | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/bristol/bundle-planted-sessile-oak-bishops-knoll) |
| 11-16 | Y1 | The Grapevine of the Royal Hotel | Gilgandra | a reader's photograph, published | [live](https://ancienttrees.app/gilgandra/grapevine-of-the-royal-hotel) |
| 11-16 | D1 | The Champion Lodgepole Pine | Big Bear Lake | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/big-bear-lake/champion-lodgepole-pine) |
| 11-16 | W1 | The Blackbutt of Bird Tree Road | Middle Brother National Park | a reader's photograph, published | [live](https://ancienttrees.app/middle-brother-national-park/blackbutt-of-bird-tree-road) |
| 11-16 | S | The Centenary Trees of Parque de la Misericordia | Bilbao | a reader's photograph, published | [live](https://ancienttrees.app/bilbao/centenary-trees-of-parque-de-la-misericordia) |
| 11-16 | N2 | The Huff Creek Road White Pine | Nicolet National Forest | a reader's photograph, published | [live](https://ancienttrees.app/nicolet-national-forest/huff-creek-road-white-pine) |
| 11-16 | S | The Plane Trees of Jardines de Albia | Bilbao | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/bilbao/plane-trees-of-jardines-de-albia) |
| 11-16 | M2 | The Great Plane of Brunswick Square | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/great-plane-of-brunswick-square) |
| 11-16 | L2 | The Lietzensee Plane | Berlin | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/berlin/lietzensee-plane) |
| 11-17 | A | The Ada Tree | Powelltown | a reader's photograph, published | [live](https://ancienttrees.app/powelltown/ada-tree) |
| 11-17 | B | The Giant Tree | Humboldt Redwoods State Park | a reader's photograph, published | [live](https://ancienttrees.app/humboldt-redwoods-state-park/giant-tree) |
| 11-17 | C | The Ginkgo of the United Order of Tents | New York | a reader's photograph, published | [live](https://ancienttrees.app/new-york/ginkgo-of-the-united-order-of-tents) |
| 11-17 | D | The Huntington Montezuma Cypress | Los Angeles | a reader's photograph, published | [live](https://ancienttrees.app/los-angeles/huntington-montezuma-cypress) |
| 11-17 | E | The Cedar of Lebanon at Blaise Castle | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/cedar-of-lebanon-at-blaise-castle) |
| 11-17 | F | The Moreton Bay Fig of Parque Marechal Carmona | Cascais | a reader's photograph, published | [live](https://ancienttrees.app/cascais/moreton-bay-fig-of-parque-marechal-carmona) |
| 11-17 | G | The Pepper Tree That Mended Nets | Setubal | a reader's photograph, published | [live](https://ancienttrees.app/setubal/pepper-tree-that-mended-nets) |
| 11-17 | D | The Huntington Rose Garden Kauri | Los Angeles | a reader's photograph, published | [live](https://ancienttrees.app/los-angeles/huntington-rose-garden-kauri) |
| 11-17 | H | The Wishing Tree | Sydney | a reader's photograph, published | [live](https://ancienttrees.app/sydney/wishing-tree) |
| 11-17 | G | The Peruvian Pepper of the Jardim de Palhais | Setubal | a reader's photograph, published | [live](https://ancienttrees.app/setubal/peruvian-pepper-of-the-jardim-de-palhais) |
| 11-17 | I | Roath Park Lake Pedunculate Oak | Cardiff | a reader's photograph, published | [live](https://ancienttrees.app/cardiff/roath-park-lake-pedunculate-oak) |
| 11-17 | J | The Grand Ginkgo of Goo Shrine | Kyoto | a reader's photograph, published | [live](https://ancienttrees.app/kyoto/grand-ginkgo-of-goo-shrine) |
| 11-17 | J | The Grand Ginkgo of Goo Shrine | Kyoto | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kyoto/grand-ginkgo-of-goo-shrine) |
| 11-17 | K | Old Knobbley | Mistley | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mistley/old-knobbley) |
| 11-17 | L | Benmore Redwood Avenue | Benmore | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/benmore/benmore-redwood-avenue) |
| 11-17 | G | Benmore Redwood Avenue | Benmore | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/benmore/benmore-redwood-avenue) |
| 11-17 | M | Boab Prison Tree | Derby | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/derby/boab-prison-tree) |
| 11-17 | N | The Sisi-Platane of Volksgarten | Vienna | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/vienna/sisi-platane-of-volksgarten) |
| 11-17 | N | The Sisi-Platane of Volksgarten | Vienna | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/vienna/sisi-platane-of-volksgarten) |
| 11-17 | O | The Cantonspark Giant Sequoia | Baarn | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/baarn/cantonspark-giant-sequoia) |
| 11-17 | A | Chief Sequoyah Tree | Sequoia National Park | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sequoia-national-park/chief-sequoyah-tree) |
| 11-17 | P | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 11-17 | P | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 11-17 | P | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 11-17 | Q | The Oak of Molinazzo | Poggio Renatico | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/poggio-renatico/oak-of-molinazzo) |
| 11-17 | R | Bleeding Yew of Nevern | Nevern | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/nevern/bleeding-yew-of-nevern) |
| 11-17 | S | The Bald Cypresses of the Crystal Palace Pond | Madrid | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/madrid/bald-cypresses-of-the-crystal-palace-pond) |
| 11-17 | T | Trolleken (the Troll Oak of Trollskogen) | Trollskogen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/trollskogen/trolleken-the-troll-oak-of-trollskogen) |
| 11-17 | T | S'Olivera de Cort | Palma de Mallorca | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/palma-de-mallorca/solivera-de-cort) |
| 11-17 | J | The Land Boat Pine | Kyoto | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kyoto/land-boat-pine) |
| 11-17 | Z1 | The Ombu of the Essaouira Medina | Essaouira | a reader's photograph, published | [live](https://ancienttrees.app/essaouira/ombu-of-the-essaouira-medina) |
| 11-15 | Q2 | Veteran Lime (Linden) Tree | Milton Keynes | a reader's tree changed the page | - |
| 11-15 | S5 | The Master Oak | Stanmore | a reader's tree changed the page | - |
| 11-15 | Y2 | Ancient Lappa plane tree | Argyroupoli | a reader's tree changed the page | - |
| 11-15 | T5 | The Old banyan at the office of Nhan Dan newspaper | Hanoi | a reader's tree changed the page | - |
| 11-15 | Z2 | - | - | a reader's feedback changed the page | - |
| 11-15 | M3 | Ancient eastern plane tree on Çınar Street | Isparta | a reader's tree changed the page | - |
| 11-15 | U5 | Faux de Verzy | Reims | a reader's tree changed the page | - |
| 11-15 | V5 | The Zaandam wingnut | Zaandam | a reader's tree changed the page | - |
| 11-15 | N3 | Old Knobbley | Essex, Mistley | a reader's tree changed the page | - |
| 11-15 | W5 | Wyndham's Oak | Gillingham, Dorset | a reader's tree changed the page | - |
| 11-15 | Q3 | The picture card perfect pines in Connamara | Connamara | a reader's tree changed the page | - |
| 11-15 | R3 | Mariam Dearit (also known as the Madonna of the Baobab) | Kerrn, Senhit (Anseba) region of Eritrea | a reader's tree changed the page | - |
| 11-15 | W4 | Black Mulberry | Lewes, East Sussex, England | a reader's tree changed the page | - |
| 11-15 | X4 | Cedar of Lebanon | Ulverston | a reader's tree changed the page | - |
| 11-15 | X4 | Douglas fir | Ulverston | a reader's tree changed the page | - |
| 11-15 | X1 | Arbour Oak | Nottingham | a reader's tree changed the page | - |
| 11-15 | Q | Quercia di Molinazzo | Poggio Renatico (FE) | a reader's tree changed the page | - |
| 11-16 | L1 | Ancient totara tree | Akaroa | a reader's tree changed the page | - |
| 11-16 | M1 | 1500 old olive tree | Kaštel Štafalić | a reader's tree changed the page | - |
| 11-16 | E2 | Yew | Vigeois | a reader's tree changed the page | - |
- From 131 readers: reader G4 10, reader E4 9, reader B 8, reader T2 7, reader G3 6, reader W3 6, reader B3 5, reader S 5, reader G 4, reader K5 4, reader L5 4, reader R2 4, reader T4 4, reader D 3, reader D1 3, reader D5 3, reader E 3, reader G2 3, reader J 3, reader J4 3, reader O4 3, reader P 3, reader P4 3, reader S1 3, reader A 2, reader C1 2, reader C4 2, reader E5 2, reader F4 2, reader G1 2, reader I2 2, reader I3 2, reader J1 2, reader M3 2, reader N 2, reader N1 2, reader O2 2, reader P5 2, reader Q 2, reader Q3 2, reader Q4 2, reader Q5 2, reader R1 2, reader R3 2, reader R4 2, reader T 2, reader U1 2, reader U2 2, reader V 2, reader V3 2, reader W 2, reader X4 2, reader Y4 2, reader Z 2, reader Z2 2, reader A1 1, reader A3 1, reader A4 1, reader B4 1, reader C 1, reader C3 1, reader C5 1, reader D4 1, reader E1 1, reader E2 1, reader F 1, reader F2 1, reader F3 1, reader F5 1, reader G5 1, reader H 1, reader H1 1, reader H2 1, reader H3 1, reader H4 1, reader H5 1, reader I 1, reader I1 1, reader I4 1, reader I5 1, reader J3 1, reader J5 1, reader K 1, reader K1 1, reader K3 1, reader K4 1, reader L 1, reader L1 1, reader L2 1, reader M 1, reader M1 1, reader M2 1, reader M5 1, reader N2 1, reader N3 1, reader O 1, reader O1 1, reader O5 1, reader P1 1, reader P2 1, reader Q1 1, reader Q2 1, reader R 1, reader R5 1, reader S2 1, reader S3 1, reader S4 1, reader S5 1, reader T1 1, reader T3 1, reader T5 1, reader U3 1, reader U4 1, reader U5 1, reader V1 1, reader V2 1, reader V5 1, reader W1 1, reader W4 1, reader W5 1, reader X 1, reader X1 1, reader X2 1, reader X3 1, reader Y 1, reader Y1 1, reader Y2 1, reader Y3 1, reader Z1 1, reader Z3 1, reader Z4 1.

**What was sent in, and what we decided**

| seen | what | where | size for its species | ours | Hidde |
|---|---|---|---|---|---|
| 2026-11-17 | Kapok | - | - | open | - |
| 2026-11-16 | Ahuehuete de Parque Espana | Mexico City | - | publish | - |
| 2026-11-16 | Eastern Cottonwood | - | - | lead | - |
| 2026-11-15 | River Red Gum | - | - | publish | - |
| 2026-11-15 | Giant Australian Rubber Tree of Jardim | Azores | - | publish | - |
| 2026-11-15 | A tree I found | - | - | hold | - |
| 2026-11-15 | The Weeping Beech of the Schwanenbrück | Munich | - | publish | - |
| 2026-11-15 | El Drago Milenario | Tenerife | - | publish | - |
| 2026-11-15 | The Oak of the Dörfchen, Nymphenburg | Munich | - | publish | - |
| 2026-11-15 | The Fortingall Yew | Fortingall | - | publish | - |
| 2026-11-15 | Coldwaltham Yew | Coldwaltham | - | publish | - |
| 2026-11-15 | El Árbol del Tule | Santa María del Tule | - | publish | - |
| 2026-11-15 | The Sycamore at the Crum Creek Bridge | Willistown | - | publish | - |
| 2026-11-15 | Tāne Mahuta | Waipoua Forest | - | publish | - |
| 2026-11-15 | The Fern-leaved Beech of the Amalienbu | Munich | - | publish | - |

21 waiting for a verdict. Disagree with one and the rule changes: `python3 scripts/judgement.py --feedback <id> "..."`, and `--learn` prints every verdict he has overruled.

**Searched yesterday:** nothing.

**App crashes** (last 7 days, store builds; MetricKit, a sample)

| Crashes | Kind | Build | Where | Phones | Last | Fix |
|---:|---|---|---|---:|---|---|
| 1 | crash | 1.0.4 (41) | (no AncientTrees frame) | 1 | 2026-11-15 | none |
| 1 | crash | 1.0.4 (41) | AncientTrees+0x2409a0 | 1 | 2026-11-16 | none |

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 11-07 | 2 | 34 | 5.9% | 38.3 |
| 11-08 | 25 | 1013 | 2.5% | 9.1 |
| 11-09 | 28 | 1177 | 2.4% | 8.9 |
| 11-10 | 8 | 196 | 4.1% | 13.0 |
| 11-11 | 1 | 16 | 6.2% | 22.1 |
| 11-12 | 1 | 28 | 3.6% | 31.4 |
| 11-13 | 1 | 32 | 3.1% | 55.0 |
| 11-14 | 0 | 51 | 0.0% | 57.5 |
| 11-15 | 210 | 363 | 57.9% | 8.2 |
| 11-16 *partial* | 100 | 168 | 59.5% | 7.2 |
| **window** | **376** | **3078** | **12.2%** | |
- Top queries (10d): ancient trees app (i324, p1); ancient trees (i14, p30); ancient tree app (i2, p1); android au (i1, p1); skovfogedegen (i1, p4)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-09 | 151 | 4 | 2.6% |
| 11-10 | 136 | 9 | 6.6% |
| 11-11 | 97 | 7 | 7.2% |
| 11-12 | 190 | 4 | 2.1% |
| 11-13 | 125 | 5 | 4.0% |
| 11-14 | 103 | 6 | 5.8% |
| 11-15 | 132 | 13 | 9.8% |
| **7 days** | **934** | **48** | **5.1%** |
- Week before: 844 impressions, 39 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); platane du square des batignolles (c4/i2, p1); picture of the tree in helsinki city center that was preserved (c3/i2, p4); ancient trees app (c2/i8, p5); who planted the western red cedar tree in blarney ireland (c2/i8, p2); fig tree in square alicante (c2/i4, p4); palma del cile (c2/i2, p6); cipresso calvo indro montanelli milano (c2/i2, p8)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-16T10:07 | 24.9 | 11 | 15 | 2 | Brisbane +1, Cannock Chase +1, Darwin +1, Earlysville +1, +17 more |
| 11-16T13:14 | 19.6 | 3 | 12 | 1 | Guimaraes +1, Leipzig +1, Philadelphia +1, Bilbao, +7 more |
| 11-16T14:32 | 3.9 | 0 | 6 | 0 | Berlin, Bilbao, London, Nicolet National Forest |
| 11-16T23:56 | 8.0 | 1 | 8 | 0 | Orroroo +1, Aguas De Moura, Baarn, Benmore, +19 more |
| **4 runs** | **56** | **15** | **41** | | |

- 1 of 4 produced no trees; 1 to 2 commands refused per run; last build that went live: 2h ago.

**What they made**

- New tree from a reader's photograph: Orroroo Giant Gum (South Australia), sign in the photo is the source
- Escaped bug closed: reader tree links its sighting, fixed in 3e9b4071a, test in qa
- Unmapped reader photographs looked at, verdict sentences written; log
- Reader photographs looked at: 12 lead pictures, 19 added to strips, 5 held; three colon reveals reworded
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- Weekly analysis
- Fresh-eyes review: 3 finding(s)
- Fresh-eyes review: 2 finding(s)
- Health: answered the 11-16 deploy and iOS reds
- Reader photographs looked at: two close photo gaps (Bilbao palms, Nicolet white pine), three planes added to strips, two unmapped trees stay leads with a verdict
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed

**Reader photographs in a strip, live first, not yet looked at** (63)

| Day | Tree | Where | Undo |
|---|---|---|---|
| 11-17 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | `sightings_publish.py --unstrip 5e09bb82-34d7-4622-b626-8251836f6eb4` |
| 11-17 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | `sightings_publish.py --unstrip 62c4bb28-b3f8-46f6-8d7a-c88755acce7b` |
| 11-17 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | `sightings_publish.py --unstrip 5ecc82c8-870b-4961-9a0f-b4fb6bf2e1b6` |
| 11-16 | The Sacred Olive Tree of the Acropolis | Athens | `sightings_publish.py --unstrip c86414b5-1884-40c9-aff2-724f25f8e1f4` |
| 11-17 | The Cantonspark Giant Sequoia | Baarn | `sightings_publish.py --unstrip cc8a74d4-d8a7-42fa-865c-f5a12e490f7f` |
| 11-15 | The Plane Trees of the Circus | Bath | `sightings_publish.py --unstrip 3b39d16a-da7e-41df-b566-3345170189b9` |
| 11-17 | Benmore Redwood Avenue | Benmore | `sightings_publish.py --unstrip cdc0b82c-26f6-4691-94df-3d728924d039` |
| 11-17 | Benmore Redwood Avenue | Benmore | `sightings_publish.py --unstrip 4c161566-17bf-4859-a3cb-2148328999a9` |
| 11-16 | The Lietzensee Plane | Berlin | `sightings_publish.py --unstrip 37223ae8-945a-4737-bd16-1cf8defb2ee1` |
| 11-16 | The Plane Trees of Jardines de Albia | Bilbao | `sightings_publish.py --unstrip ea9d0b2f-f100-496d-a05c-6f492630635f` |
| 11-16 | The Borrowdale Yews (the Fraternal Four) | Borrowdale | `sightings_publish.py --unstrip b24f5c1e-b9c6-4f5a-af2e-c761fa60e614` |
| 11-16 | The Borrowdale Yews (the Fraternal Four) | Borrowdale | `sightings_publish.py --unstrip 3cf4d1ae-05de-4dff-b168-0c0815960fd3` |
| 11-15 | Endicott Pear Tree | Boston | `sightings_publish.py --unstrip b724f1db-2429-4905-a291-fa1bf50132cd` |
| 11-16 | The Bundle-planted Sessile Oak, Bishops Knoll | Bristol | `sightings_publish.py --unstrip 1b2096fe-4e2d-41f0-9517-b288ef04b372` |
| 11-15 | The Gomero de la Recoleta | Buenos Aires | `sightings_publish.py --unstrip 3325a9bc-9642-4364-8475-8f89d62e834d` |
| 11-16 | The Angel Oak | Charleston | `sightings_publish.py --unstrip 27b65062-4209-44fa-ad20-a179dd1e974f` |
| 11-15 | The Fern-leaved Beech of the National Gallery | Copenhagen | `sightings_publish.py --unstrip 40d6b9ff-509f-488b-9e02-4f507e7f889a` |
| 11-15 | The Olive of the Orange Courtyard | Cordoba | `sightings_publish.py --unstrip 79e27623-4f57-4e8b-93ed-5809952ad465` |
| 11-15 | The Orange Courtyard of the Mezquita | Cordoba | `sightings_publish.py --unstrip 505b0039-de16-410f-817e-55e31e93c41a` |
| 11-17 | Boab Prison Tree | Derby | `sightings_publish.py --unstrip 023ed607-1e16-4502-a16c-ba7b77888f82` |
| 11-15 | The Kaditzer Linde | Dresden | `sightings_publish.py --unstrip 90aa5d92-64b3-439f-b2b3-a56cc8b41136` |
| 11-15 | The Weeping Beech of Helfenberg Park | Dresden | `sightings_publish.py --unstrip cfcad2b9-4ce3-49f8-bf53-a03f156c8794` |
| 11-16 | Elleholmseken (The Oak of Elleholm) | Elleholm | `sightings_publish.py --unstrip a04e6933-4b0d-4172-90d1-5d13dcfec0e5` |
| 11-16 | The Fortingall Yew | Fortingall | `sightings_publish.py --unstrip 7fb05e54-cf36-4393-a549-92e3c17d96b3` |
| 11-15 | The Argyle Street Ash | Glasgow | `sightings_publish.py --unstrip c62d8c77-f078-478f-babf-1c12d2426ef4` |
| 11-16 | The Willow Nearest the Hypocentre | Hiroshima | `sightings_publish.py --unstrip 96c47295-7fb6-40d8-b0da-3575f4b9b420` |
| 11-17 | The Land Boat Pine | Kyoto | `sightings_publish.py --unstrip 46766dcd-94f4-4656-8dab-53b5c98b30f8` |
| 11-15 | The Fulham Palace Oak | London | `sightings_publish.py --unstrip d8994b07-93c9-41a0-ae09-ab417f322b93` |
| 11-15 | Barney the Plane | London | `sightings_publish.py --unstrip 6f2cee0c-369d-4da5-a2e3-6e08f138a29f` |
| 11-16 | The Great Plane of Brunswick Square | London | `sightings_publish.py --unstrip 68f3ef55-878f-4dad-846d-9582ed057c08` |
| 11-15 | The Ravenscourt Park Baobab Plane | London | `sightings_publish.py --unstrip eb811a74-663f-476f-bf0f-349d058508e0` |
| 11-15 | The Bromley Oak | London | `sightings_publish.py --unstrip cc260294-0437-4efb-8c0f-5bf73fb0adf3` |
| 11-15 | The Bromley Oak | London | `sightings_publish.py --unstrip 4fa5c2bb-2a1f-4c07-9e87-d7fd9b008800` |
| 11-17 | The Bald Cypresses of the Crystal Palace Pond | Madrid | `sightings_publish.py --unstrip e593be60-987f-469d-97d7-7da2a69503d5` |
| 11-16 | Ahuehuete de Parque Espana | Mexico City | `sightings_publish.py --unstrip 3693bdc5-cbb5-4ff1-909e-745a397aaf76` |
| 11-16 | Ahuehuete de Parque Espana | Mexico City | `sightings_publish.py --unstrip 9d72943f-aba5-4ab8-a8da-ee9c3a21a1cf` |
| 11-17 | Old Knobbley | Mistley | `sightings_publish.py --unstrip a477d312-0d76-4189-9217-ef167b0b1bc7` |
| 11-15 | Jackson's Oak | Mobile | `sightings_publish.py --unstrip bcde1019-cccf-445a-a2ab-81b2bdbb8809` |
| 11-15 | The Copper Beech of the Badenburg | Munich | `sightings_publish.py --unstrip a1e5696d-07f6-4ad8-b33d-af8a195ee53a` |
| 11-15 | The Leaning Lime of the Badenburger See | Munich | `sightings_publish.py --unstrip f9aef0f0-825b-43a6-80c6-bdae5f77ce0d` |
| 11-15 | The Leaning Lime of the Badenburger See | Munich | `sightings_publish.py --unstrip 31f72d8f-0bcc-4df5-88a8-46c14bbbb5cf` |
| 11-15 | The Great Cedar of Kasuga Taisha | Nara | `sightings_publish.py --unstrip 221f1245-c4b5-4b97-a777-879f9f8bd9e7` |
| 11-17 | Bleeding Yew of Nevern | Nevern | `sightings_publish.py --unstrip 09765ff6-b1e9-4d56-a98a-73c47709468b` |
| 11-16 | The Tree of Life | Olympic National Park | `sightings_publish.py --unstrip d8212c9e-e921-4b28-b931-44a7ff01fec4` |
| 11-16 | The Quinault Big Spruce | Olympic National Park | `sightings_publish.py --unstrip d21fa973-8906-4f73-81f7-c7e4036c2fd2` |
| 11-15 | The Ficus of the Orto Botanico | Palermo | `sightings_publish.py --unstrip 61ca336b-c1eb-4f2a-8709-bcb29e63a2c6` |
| 11-15 | S'Olivera de Cort | Palma de Mallorca | `sightings_publish.py --unstrip 513c935b-b7e0-4b76-93c2-6a8223d8274b` |
| 11-17 | S'Olivera de Cort | Palma de Mallorca | `sightings_publish.py --unstrip 3c756f92-fc89-4a76-a714-06e8a6361b0f` |
| 11-17 | The Oak of Molinazzo | Poggio Renatico | `sightings_publish.py --unstrip c42df403-c159-4896-9c07-223d1122c3d6` |
| 11-16 | El Árbol del Tule | Santa María del Tule | `sightings_publish.py --unstrip 586a2d0f-096b-421c-97dc-62e612fd99b2` |
| 11-16 | General Sherman Tree | Sequoia National Park | `sightings_publish.py --unstrip b8d96d31-883d-496e-8607-a353a8acab01` |
| 11-17 | Chief Sequoyah Tree | Sequoia National Park | `sightings_publish.py --unstrip c59bfd73-d95b-4cda-9ae3-5f75cf6f9754` |
| 11-16 | Lincoln Tree | Sequoia National Park | `sightings_publish.py --unstrip 9342233f-7ec8-4d72-b3d6-2f859d2c26c1` |
| 11-15 | The Cardón of the Expo | Seville | `sightings_publish.py --unstrip 770b668b-0152-47a4-9822-70e04183b599` |
| 11-15 | The Sunderland Buttonball Tree | Sunderland, Massachusetts | `sightings_publish.py --unstrip 9689a5aa-c566-41e5-a674-f26dd189e7cc` |
| 11-15 | El Drago Milenario | Tenerife | `sightings_publish.py --unstrip d1f0b3c4-247f-4f5b-8b34-f2e44c765fef` |
| 11-17 | Trolleken (the Troll Oak of Trollskogen) | Trollskogen | `sightings_publish.py --unstrip 54dc7d2a-aaf6-4158-8784-3f3c256942a3` |
| 11-17 | The Sisi-Platane of Volksgarten | Vienna | `sightings_publish.py --unstrip 57a1afed-1a15-4782-b4a1-4aeaf08a9f04` |
| 11-17 | The Sisi-Platane of Volksgarten | Vienna | `sightings_publish.py --unstrip 161c7f67-f76d-4527-84b1-d24ab59c798f` |
| 11-15 | Te Matua Ngahere | Waipoua Forest | `sightings_publish.py --unstrip ab926a56-7355-4115-aaeb-20715143d5c0` |
| 11-15 | Dab Mieszko I (King Mieszko I's Oak) | Warsaw | `sightings_publish.py --unstrip 5b8c4e7a-86a1-4b3f-a434-83e7a0945553` |
| 11-15 | The Cut-Leaved Hornbeam | York | `sightings_publish.py --unstrip b24fa509-4aa6-42fc-9fda-04282a20e481` |
| 11-15 | The Pear-Barked Beech | York | `sightings_publish.py --unstrip 56342639-17a9-44b9-a876-bfe3cfa658dc` |

Machine: 5 chain attempts yesterday, 5 got real work time (~86 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c311/i508); /app (c3/i22); /switzerland (c3/i13); /seville (c2/i51); /de (c2/i19)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i5, p3)
    - 'alte bäume karte' (i3, p7)
    - 'acient tree' (i2, p14)
    - 'angeloak' (i2, p79)
    - 'android au' (i1, p1)
    - 'ahornbäume in der nähe' (i1, p7)
    - 'alberi di roma' (i1, p1)
    - 'alter' (i1, p2)
    - and 1 more

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 158 | 16 | 51 | 0.32 | 1 |
| Not yet rich | 212 | 20 | 210 | 0.99 | 0 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| fortingall | 0 | 145 | 0.0% | 11.0 | 2.2% | fortingall yew (i117, p11) |
| lisbon | 1 | 61 | 1.6% | 6.4 | 4.6% | historic giant plant of lisbon (i1, p12) |
| seville | 2 | 57 | 3.5% | 5.1 | 6.8% | sevilla (i1, p1) |
| berlin | 2 | 41 | 4.9% | 6.0 | 5.1% | berlin trees (i2, p5) |
| fulufjallet | 0 | 41 | 0.0% | 9.4 | 2.8% | old tjikko (i22, p11) |
| olympic-national-park | 0 | 33 | 0.0% | 16.4 | 1.1% | duncan cedar (i14, p10) |
| tokyo | 0 | 32 | 0.0% | 5.4 | 6.2% | ginkgo sperm (i2, p11) |
| malaga | 0 | 31 | 0.0% | 25.2 | 0.6% | árboles históricos de málaga (i7, p89) |
| london | 2 | 29 | 6.9% | 33.0 | 0.4% | flats to rent clerkenwell (i3, p89) |
| singapore | 0 | 29 | 0.0% | 9.0 | 3.0% | earpod tree (i3, p5) |
| south-korea | 0 | 28 | 0.0% | 21.4 | 0.7% | ginkgo tree korea (i2, p5) |
| munich | 1 | 26 | 3.8% | 5.3 | 6.4% | ältester baum münchen (i1, p8) |
| tenerife | 0 | 26 | 0.0% | 35.3 | 0.4% | el drago milenario (i2, p10) |
| paris | 1 | 24 | 4.2% | 5.9 | 5.2% | - |
| kyoto | 1 | 24 | 4.2% | 4.0 | 8.1% | ginkgo tree kyoto (i1, p1) |
| palermo | 0 | 24 | 0.0% | 9.0 | 3.0% | palermo tree (i1, p9) |
| monterey | 0 | 23 | 0.0% | 53.7 | 0.4% | lone cypress (i6, p76) |
| copenhagen | 2 | 21 | 9.5% | 11.0 | 2.2% | copenhagen trees (i3, p39) |
| seoul | 1 | 21 | 4.8% | 6.1 | 4.9% | - |
| amsterdam | 0 | 21 | 0.0% | 8.7 | 3.1% | lomanstraat (i2, p19) |
| united-states | 2 | 20 | 10.0% | 17.4 | 1.0% | oldest tree in oregon (i4, p10) |
| taiwan | 0 | 18 | 0.0% | 11.1 | 2.1% | oldest tree in taiwan (i3, p5) |
| sequoia-national-park | 0 | 18 | 0.0% | 24.1 | 0.6% | washington tree (i9, p20) |
| reykjavik | 0 | 18 | 0.0% | 5.8 | 5.3% | - |
| barcelona | 0 | 17 | 0.0% | 9.4 | 2.8% | - |
| venice | 2 | 16 | 12.5% | 4.0 | 8.0% | - |
| austin | 0 | 16 | 0.0% | 17.2 | 1.0% | oldest tree in austin (i2, p12) |
| germany | 1 | 15 | 6.7% | 6.1 | 4.9% | - |
| san-francisco | 0 | 15 | 0.0% | 4.9 | 7.1% | old tree near me (i1, p4) |
| kagoshima | 0 | 15 | 0.0% | 10.4 | 2.4% | oldest camphor tree (i1, p7) |
| brisbane | 0 | 15 | 0.0% | 16.5 | 1.1% | banyan tree (i3, p10) |
| oahu | 0 | 14 | 0.0% | 9.4 | 2.8% | hitachi tree (i2, p10) |
| cambridge | 0 | 14 | 0.0% | 25.3 | 0.6% | isaac newton tree (i2, p22) |
| los-angeles | 0 | 14 | 0.0% | 7.8 | 3.6% | moreton bay fig tree beverly hills (i1, p9) |
| milan | 0 | 14 | 0.0% | 5.4 | 6.3% | - |
| prague | 0 | 14 | 0.0% | 4.9 | 7.1% | - |
| switzerland | 3 | 13 | 23.1% | 7.7 | 3.7% | - |
| porto | 1 | 13 | 7.7% | 2.2 | 14.1% | - |
| edinburgh | 0 | 13 | 0.0% | 6.8 | 4.2% | - |
| athens | 0 | 13 | 0.0% | 5.5 | 6.1% | - |
| dublin | 1 | 12 | 8.3% | 4.3 | 7.7% | - |
| nara | 1 | 12 | 8.3% | 5.8 | 5.5% | - |
| charleston | 0 | 12 | 0.0% | 24.3 | 0.6% | angeloak (i2, p79) |
| kanazawa | 0 | 12 | 0.0% | 6.3 | 4.7% | - |
| chishang | 0 | 11 | 0.0% | 6.5 | 4.5% | takeshi kaneshiro tree (i6, p7) |
| fukuoka | 0 | 11 | 0.0% | 7.4 | 3.8% | dazaifu tenmangu (i1, p1) |
| seattle | 0 | 11 | 0.0% | 9.0 | 3.0% | oldest tree in seattle (i1, p10) |
| netherlands | 1 | 10 | 10.0% | 9.0 | 3.0% | dutch trees (i1, p39) |
| bristol | 0 | 10 | 0.0% | 6.0 | 5.0% | - |
| poland | 0 | 10 | 0.0% | 7.7 | 3.6% | trees in poland (i1, p8) |
| antwerp | 0 | 10 | 0.0% | 42.3 | 0.4% | park den brandt (i3, p52) |
| madrid | 0 | 10 | 0.0% | 6.5 | 4.5% | - |

- Plus 212 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: bath, rome, new-york, brussels, vienna, alicante, cadiz, pamplona.

## Weekly analysis 2026-11-16

Sixteenth weekly analysis. Compares 11-09 to 11-15 with 11-02 to 11-08, read from the
11-15 daily entry (7-day tables, Google and Bing rows). 11-15 is the Guardian day and
carries most of the week; the other six days are at noise level. Google's 11-15 row is
partial.

**Scorecard**

| Week | Impressions | Clicks | CTR | Avg position | Visitors (GA, new) | From Google | App downloads (first-time) | New accounts | Trees collected | Readers' contributions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 11-02 to 11-08 | ~3,830 (11-08 now 1,013) | ~93 | ~2.5% | 8 to 10 on 4 days, 34 to 38 on 3 | 54 | 16 | 14 | 7 | 7 | 6 |
| 11-09 to 11-15 | 1,803 (11-15 partial) | 221 | 12.3% | 5.5 to 9 on 11-08/09/15, 13 to 58 on the rest | 1,818 | 38 | 14 | 369 | 3 | 301 |

Per day, 11-09 to 11-15: Google 1,177 / 196 / 16 / 28 / 32 / 51 / 303 impressions; 11-15
has 182 clicks (60% CTR, position 5.5), almost all the brand query "ancient trees app"
(i190 in the 10-day window). Bing, 7 days to 11-13: 905 impressions, 45 clicks (5.0%),
80 to 190 a day; the "watchdog" line compares against the 11-01 spike (2,953) and is not
news. 11-15 alone: 1,797 visitors, 365 new accounts, 191 saves, 944 Android waitlist
signups (996 total), 98 feedback rows, 96 trees collected, 7,607 trees opened on 3,562
phones. First-time downloads are not yet reported for 11-15 (Apple lags). Device split
and per-visit ratios are not in the entry, so none is claimed.

**Outreach yield** (data/mail-yield.json, mailbox read; weeks keyed by the Monday of our first mail; the week of 11-02 is the one old enough to read, 11-09 and 11-16 are not)

| Group | Mailed, week of 11-02 | Answered of those | Mailed, total | Answered, total | Rate | Linked |
|---|---:|---:|---:|---:|---:|---:|
| archive | 10 | 2 | 27 | 5 | 19% | 0 |
| nature | 16 | 2 | 81 | 6 | 7% | 1 |
| guide | 19 | 0 | 37 | 1 | 3% | 1 |
| source | 0 | 0 | 63 | 5 | 8% | 0 |
| press | 23 | 0 | 126 | 9 | 7% | 0 |
| tourism | 0 | 0 | 19 | 3 | 16% | 0 |
| garden | 0 | 0 | 97 | 11 | 11% | 0 |
| society | 0 | 0 | 148 | 25 | 17% | 1 |
| council | 3 | 1 | 58 | 9 | 16% | 0 |
| other | 19 | 4 | 366 | 61 | 17% | 2 |

The week of 11-09 sent 196 mails (other 184, press 5, source 4, archive 2, guide 1,
tourism 1) and 22 more went the week of 11-16; both too young to judge. Five links in
all, none new this week.

**What moved:**
1. The Guardian piece on 11-15 moved the product numbers, not search: 1,797 visitors
   against 3 to 11 a day, 365 accounts, 191 saves, 944 Android waitlist signups, 301
   readers' contributions for the week against 6. It is one day; whether any of it
   persists is not readable yet.
2. Google search outside 11-15 is at noise level again: 16 to 51 impressions a day on
   11-11 to 11-14 at position 22 to 58, after two days of about 1,000 (11-08, 11-09).
   The 11-15 clicks are brand search from the article, not page recovery.
3. Visitors from Google 38 against 16, from all search 48 against 21; the 11-02 to 11-08
   comparison is a different regime and should not be read as growth.
4. App first-time downloads 14 against 14 through 11-14 (11-15 not yet in); phones back
   within 30 days 4 of 16. Trees collected 3 against 7 (99 across the days in the
   day-by-day table, 96 on 11-15 alone, so read the 3 and the 99 as different counts).
5. Quality: Web red, a RangeError "Maximum call stack size exceeded" in an inline script,
   5 reports on 3 pages, on the day with the most visitors; Backup red (Hidde's setup).
   Outreach: archive and council answer best by rate on small n; guide is 1 in 37.

**Suggestions, ranked:**
1. **[run]** Fix the RangeError (max call stack, inline script, 3 pages). It is rung-2
   work and it hit the Guardian day; find the page paths in web_errors.py first.
2. **[run]** Read the new-account and save cohort of 11-15 at day 7 and day 30 (accounts
   still opening the app, saves turned into collects) before judging the Guardian day;
   the 30-day phones row is the only retention number and it is 4 of 16 for older cohorts.
3. **[sessie]** The 944 Android waitlist signups (996 total) are the largest asset of the
   week. Android parity (data/android-parity.json) is the path; say in the waitlist
   confirmation what happens next so the list stays warm.
4. **[run]** Keep sourcing archive contacts for kept-set cities with photo gaps: archive
   answers 5 of 27 (19%), the best of the coverage groups beside 7% for nature and 3% for
   guide. Do not draft more guide mail until the week-of-11-02 batch's 19 mails have had
   time (0 answers).
5. **[FOR HIDDE]** 11-15 brand queries ("ancient trees app", position 1) earned 190
   impressions in the window; Google ranks the site first for its own name but nowhere for
   tree queries (position 22 to 58 on non-brand days). Decide whether press coverage is
   the lane to repeat (Guardian, Bristol24/7, Wilder) since it is the only thing that has
   moved traffic at scale; archive and nature outreach have produced no links this week.

**Watch next week:** how many of the 11-15 accounts and visitors are still active on
11-22 and 11-23 (visitors back to 3 to 11 a day would say the day was a spike), and
whether the RangeError reports fall to zero.

## 2026-11-15 (previous UTC day)

**Today: 56 android waitlist signups arrived today (996 total); 113 tree submissions and an ambassador request for Auckland and an ambassador request for Edinburgh and an ambassador request for London and an ambassador request for Media and an ambassador request for Melbourne and an ambassador request for Toronto and 25 correction reports and 80 feedback reports arrived today (283 submissions of every kind in all); 27 accounts were opened today (456 accounts in all).**

**North star: 118 people have uploaded a tree or photo of their own (+106 this week); 10 of them did it on more than one day (+6).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 1818 | 54 |
| ... of which from search | every search engine | 48 | 21 |
| ... from Google | Google's recovery | 38 | 16 |
| ... from Bing | Bing | 1 | 2 |
| Website visitors who came back | people who stay | 144 | 13 |
| App downloads (first-time) | people | 14 | 23 |
| New accounts | people | 369 | 7 |
| Phones back within 30 days | people who stay | 4 of 16 | 4 of 7 |
| Trees saved to Want to go | intent | 191 | 3 |
| Trees collected | goal 1: stood at a tree | 3 | 7 |
| Readers' contributions | data: trees, photos, corrections, votes | 301 | 6 |
| Shares (app and web) | word of mouth, since 10-30 | 46 | 2 |
| Visits from a shared link | what sharing brings | 34 | 0 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web red, iOS green, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Live | red: new error spreading: "RangeError: Maximum call stack size exceeded." in inline, 5 reports on 3 pages | green | grey: no checks wired yet |

**Plus question** (7 answers, 7 new; 2 asked to be told; 4 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| A richer log of every tree you've collected | 3 |
| Download offline maps | 2 |
| Recommended tree walks for a city trip | 2 |
| Seasonal alerts when trees are at their best | 2 |
| Something else | 2 |

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-09 | 11-10 | 11-11 | 11-12 | 11-13 | 11-14 | 11-15 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 9 | 11 | 0 | 3 | 5 | 3 | 1797 | **1828** |
| New accounts | 0 | 1 | 0 | 1 | 0 | 2 | 365 | **369** |
| Saves | 0 | 0 | 0 | 0 | 0 | 0 | 191 | **191** |
| Android waitlist | 0 | 1 | 0 | 0 | 0 | 0 | 944 | **945** |
| App downloads | 2 | 3 | 1 | 2 | 2 | 1 | – | **11** |
| App phones | 7 | 5 | 6 | 5 | 5 | 8 | 3562 | **3588** |
| Trees opened in the app | 5 | 14 | 3 | 3 | 4 | 18 | 7607 | **7654** |
| Trees collected | 0 | 0 | 0 | 0 | 0 | 3 | 96 | **99** |
| Trees sent | 0 | 0 | 0 | 0 | 1 | 0 | 98 | **99** |
| Feedback | 0 | 0 | 0 | 0 | 0 | 0 | 98 | **98** |
| Ambassador asks | 0 | 0 | 0 | 0 | 0 | 0 | 5 | **5** |
| Website photos | 0 | 0 | 1 | 0 | 0 | 0 | 9 | **10** |
| iPhone photos | 0 | 0 | 0 | 0 | 0 | 3 | 177 | **180** |
| Android photos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Tree notes | 0 | 0 | 0 | 0 | 0 | 1 | 15 | **16** |
| App Store reviews | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.

**Trees readers sent, for you to inspect** (234 you have not looked at; ours left out)

| Judged | Reader | Tree | Where | Species | Their girth | Our verdict | Page |
|---|---|---|---|---|---:|---|---|
| 2026-11-16 | A | The Borrowdale Yews (the Fraternal Four) | Borrowdale | European Yew (Taxus baccata) | - | publish | [bwd_001](https://ancienttrees.app/borrowdale/borrowdale-yews-the-fraternal-four) |
| 2026-11-16 | B | Ahuehuete de Parque Espana (2 photos) | Mexico City | Montezuma Cypress (Taxodium mu | - | publish | [mex_005](https://ancienttrees.app/mexico-city/ahuehuete-de-parque-espana) |
| 2026-11-16 | C | The Angel Oak | Charleston | Southern Live Oak (Quercus vir | - | publish | [chs_001](https://ancienttrees.app/charleston/angel-oak) |
| 2026-11-16 | D | Earlysville Oak | - | White Oak | - | open | - |
| 2026-11-16 | E | Podocarpus hallii | - | Podocarpus hallii | 831 cm | open | - |
| 2026-11-16 | E | Curtain Fig | - | Cunningham's Fig / White Fig | - | open | - |
| 2026-11-16 | F | European Yew near Estry | - | European Yew | - | open | - |
| 2026-11-16 | G | American Elm (2 photos) | - | American Elm | - | open | - |
| 2026-11-16 | G | Eastern Cottonwood (2 photos) | - | Eastern Cottonwood | - | open | - |
| 2026-11-16 | G | White Oak | - | White Oak | - | open | - |
| 2026-11-16 | G | Northern Red Oak | - | Northern Red Oak | - | open | - |
| 2026-11-16 | H | Baobab (2 photos) | - | Baobab | 33 cm | open | - |
| 2026-11-16 | I | Ginkgo (3 photos) | - | Ginkgo | - | open | - |
| 2026-11-16 | J | Boab | - | Boab | 940 cm | open | - |
| 2026-11-16 | K | A tree I found (9 photos) | - | - | - | open | - |
| 2026-11-16 | L | The Becks Prime Augusta Live Oaks | Houston | - | - | publish | [hou_009](https://ancienttrees.app/houston/becks-prime-augusta-live-oaks) |
| 2026-11-16 | L | The Old Pecan Tree | Houston | - | - | publish | [hou_002](https://ancienttrees.app/houston/old-pecan-tree) |
| 2026-11-16 | M | The Kapok Tree | Key West | - | - | publish | [kyw_003](https://ancienttrees.app/key-west/kapok-tree) |
| 2026-11-16 | N | The Rhodes Bald Cypress | Richard Bong State Recreation Area | - | - | publish | [bng_001](https://ancienttrees.app/richard-bong-state-recreation-area/rhodes-bald-cypress) |
| 2026-11-15 | O | River Red Gum (2 photos) | adelaide | River Red Gum | - | publish | [ads_001](https://ancienttrees.app/adelaide/red-gum-of-the-rostrevor-creek) |
| 2026-11-15 | P | Canary Pine | moss-vale | Canary Pine | 300 cm | publish | [mvv_001](https://ancienttrees.app/moss-vale/canary-pine-of-leighton-gardens) |
| 2026-11-15 | Q | Veteran Lime (Linden) Tree | milton-keynes | Lime (Tilia sp.) | - | publish | [mkn_001](https://ancienttrees.app/milton-keynes/linford-lime) |
| 2026-11-15 | R | Coldwaltham Yew (2 photos) | Coldwaltham | - | - | publish | [cwh_001](https://ancienttrees.app/coldwaltham/coldwaltham-yew) |
| 2026-11-15 | S | The Belvoir Oak | Belfast | - | - | publish | [bfs_001](https://ancienttrees.app/belfast/belvoir-oak) |
| 2026-11-15 | T | The Fulham Palace Oak | London | - | - | publish | [lon_007](https://ancienttrees.app/london/fulham-palace-oak) |
| 2026-11-15 | T | Barney the Plane | London | - | - | publish | [lon_008](https://ancienttrees.app/london/barney-the-plane) |
| 2026-11-15 | U | The Argyle Street Ash | Glasgow | - | - | publish | [gla_005](https://ancienttrees.app/glasgow/argyle-street-ash) |
| 2026-11-15 | U | El Drago Milenario (2 photos) | Tenerife | - | - | publish | [tfe_001](https://ancienttrees.app/tenerife/el-drago-milenario) |
| 2026-11-15 | T | The Ravenscourt Park Baobab Plane | London | - | - | publish | [lon_018](https://ancienttrees.app/london/ravenscourt-park-baobab-plane) |
| 2026-11-15 | P | Canary Pine, Moss Vale | moss-vale | - | - | publish | [mvv_001](https://ancienttrees.app/moss-vale/canary-pine-of-leighton-gardens) |
| 2026-11-15 | O | River Red Gum, Rostrevor | adelaide | - | - | publish | [ads_001](https://ancienttrees.app/adelaide/red-gum-of-the-rostrevor-creek) |
| 2026-11-15 | V | Sessile Oak near London | london | Sessile Oak | - | publish | [lon_050](https://ancienttrees.app/london/bruce-castle-oak) |
| 2026-11-15 | W | Endangered Dawn Redwood in Holborn, legal di | - | Dawn Redwood | - | hold | - |
| 2026-11-15 | X | Cedar of Lebanon near Defynnog | brecon | Cedar of Lebanon | - | publish | [brk_001](https://ancienttrees.app/brecon/cedar-of-brecon-cathedral) |
| 2026-11-15 | Y | Ancient Lappa plane tree | argyroupoli | - | 2000 cm | publish | [agy_001](https://ancienttrees.app/argyroupoli/plane-of-the-five-virgins) |
| 2026-11-15 | V | The Bruce Castle Oak | London | Sessile Oak (Quercus petraea) | - | publish | [lon_050](https://ancienttrees.app/london/bruce-castle-oak) |
| 2026-11-15 | X | The Cedar of Brecon Cathedral | Brecon | Cedar of Lebanon (Cedrus liban | - | publish | [brk_001](https://ancienttrees.app/brecon/cedar-of-brecon-cathedral) |
| 2026-11-15 | Y | The Plane of the Five Virgins | Argyroupoli | Oriental Plane (Platanus orien | - | publish | [agy_001](https://ancienttrees.app/argyroupoli/plane-of-the-five-virgins) |
| 2026-11-15 | Z | Giant Norfolk Island Pine of Lagoa das Furna | Azores | Norfolk Island Pine (Araucaria | - | publish | [azo_005](https://ancienttrees.app/azores/giant-norfolk-island-pine-of-lagoa-das-furnas) |
| 2026-11-15 | A1 | The Plane of Saint Gerasimos, Omala | Kefalonia | Oriental Plane (Platanus orien | - | publish | [kef_001](https://ancienttrees.app/kefalonia/plane-of-saint-gerasimos-omala) |
| 2026-11-15 | T | The Totteridge Yew | London | European Yew (Taxus baccata) | - | publish | [lon_001](https://ancienttrees.app/london/totteridge-yew) |
| 2026-11-15 | T | The Ravenscourt Park Tree of Heaven | London | Tree of Heaven (Ailanthus alti | - | publish | [lon_023](https://ancienttrees.app/london/ravenscourt-park-tree-of-heaven) |
| 2026-11-15 | Q | Linford Lime | Milton Keynes | Common Lime (Tilia x europaea) | - | publish | [mkn_001](https://ancienttrees.app/milton-keynes/linford-lime) |
| 2026-11-15 | B1 | The Redford Wood Redwood | Edinburgh | Giant Sequoia (Sequoiadendron  | - | publish | [edi_021](https://ancienttrees.app/edinburgh/redford-wood-redwood) |
| 2026-11-15 | C1 | Giant Australian Rubber Tree of Jardim Anton (2 photos) | Azores | Moreton Bay Fig (Ficus macroph | - | hold | - |
| 2026-11-15 | B1 | Robert Louis Stevenson's Yew | Edinburgh | European Yew (Taxus baccata) | - | publish | [edi_017](https://ancienttrees.app/edinburgh/robert-louis-stevensons-yew) |
| 2026-11-15 | B1 | Sitka Spruce in Dunkeld | dunkeld | Sitka Spruce | - | publish | [dnk_009](https://ancienttrees.app/dunkeld/sitka-spruce-at-scone-palace) |
| 2026-11-15 | B1 | Sweet Chestnut | lytham | Sweet Chestnut | 700 cm | publish | [lyt_001](https://ancienttrees.app/lytham/lytham-sweet-chestnut) |
| 2026-11-15 | D1 | Deans Oak | - | - | 1200 cm | hold | - |
| 2026-11-15 | E1 | A giant sequoia | - | - | - | lead | - |
| 2026-11-15 | B1 | The Sitka Spruce at Scone Palace | Dunkeld | - | - | publish | [dnk_009](https://ancienttrees.app/dunkeld/sitka-spruce-at-scone-palace) |
| 2026-11-15 | F1 | The Geelong Ginkgo | Geelong | - | - | publish | [glg_001](https://ancienttrees.app/geelong/geelong-ginkgo) |
| 2026-11-15 | B1 | The Lytham Sweet Chestnut | Lytham | - | - | publish | [lyt_001](https://ancienttrees.app/lytham/lytham-sweet-chestnut) |
| 2026-11-15 | T | The Royal Oak | London | - | - | publish | [lon_002](https://ancienttrees.app/london/royal-oak) |
| 2026-11-15 | T | The Windrush Square Plane | London | - | - | publish | [lon_044](https://ancienttrees.app/london/windrush-square-plane) |
| 2026-11-15 | G1 | The Kyushaku-fuji of Byakugo-ji | Tamba | - | - | publish | [tmb_002](https://ancienttrees.app/tamba/kyushaku-fuji-of-byakugo-ji) |
| 2026-11-15 | G1 | Camphor Tree | nagasaki | Camphor Tree | 658 cm | publish | [ngs_001](https://ancienttrees.app/nagasaki/a-bombed-camphors-of-sanno-shrine) |
| 2026-11-15 | G1 | Japanese Black Pine near Kyoto | otsu | Japanese Black Pine | 390 cm | publish | [ots_001](https://ancienttrees.app/otsu/pine-of-ukimido) |
| 2026-11-15 | H1 | European Beech in London | london | European Beech | - | publish | [lon_052](https://ancienttrees.app/london/gnarled-beech-of-hampstead-heath) |
| 2026-11-15 | I1 | American Sycamore near Media | willistown | American Sycamore | 650 cm | publish | [wtn_001](https://ancienttrees.app/willistown/sycamore-at-the-crum-creek-bridge) |
| 2026-11-15 | B1 | Wheatley Elm in Edinburgh | edinburgh | Wheatley Elm | 400 cm | publish | [edi_022](https://ancienttrees.app/edinburgh/wheatley-elm-of-balgreen) |
| 2026-11-15 | J1 | Giant sequoia in the heart of Geashill | geashill | Giant sequoia (Sequiadendron g | - | publish | [gsh_001](https://ancienttrees.app/geashill/geashill-sequoia) |
| 2026-11-15 | K1 | The King of the Forest | dunkeld | Scots Pine | 660 cm | publish | [dnk_010](https://ancienttrees.app/dunkeld/king-of-the-forest) |
| 2026-11-15 | L1 | Scots Pine in Dunkeld | - | Scots Pine | 660 cm | hold | - |
| 2026-11-15 | M1 | Ancient eastern plane tree on Çınar Street | isparta | - | 400 cm | publish | [isp_001](https://ancienttrees.app/isparta/plane-of-cnar-sokak) |
| 2026-11-15 | N1 | Old Knobbley | - | - | 950 cm | publish | - |
| 2026-11-15 | O1 | Tree in Waitangi | - | - | - | lead | - |
| 2026-11-15 | P1 | The Great Oriental Plane Tree, Emmanuel Coll | - | - | 478 cm | hold | - |
| 2026-11-15 | Q1 | The picture card perfect pines in Connamara | - | - | - | publish | - |
| 2026-11-15 | R1 | Mariam Dearit (also known as the Madonna of  | keren | - | 700 cm | publish | [krn_001](https://ancienttrees.app/keren/mariam-dearit) |
| 2026-11-15 | G1 | The A-bombed Camphors of Sanno Shrine | Nagasaki | - | - | publish | [ngs_001](https://ancienttrees.app/nagasaki/a-bombed-camphors-of-sanno-shrine) |
| 2026-11-15 | S1 | The Market Bosworth Yew | Market Bosworth | - | - | publish | [mbw_001](https://ancienttrees.app/market-bosworth/market-bosworth-yew) |
| 2026-11-15 | T1 | Kett's Oak | Hethersett | - | - | publish | [hth_001](https://ancienttrees.app/hethersett/ketts-oak) |
| 2026-11-15 | G1 | The Pine of Ukimido | Kyoto | - | - | publish | [ots_001](https://ancienttrees.app/otsu/pine-of-ukimido) |
| 2026-11-15 | H1 | The Gnarled Beech of Hampstead Heath (2 photos) | London | - | - | publish | [lon_052](https://ancienttrees.app/london/gnarled-beech-of-hampstead-heath) |
| 2026-11-15 | U1 | The Giant of Mount Horne | Grenada | - | - | publish | [grn_001](https://ancienttrees.app/grenada/giant-of-mount-horne) |
| 2026-11-15 | B1 | The Wheatley Elm of Balgreen | Edinburgh | - | - | publish | [edi_022](https://ancienttrees.app/edinburgh/wheatley-elm-of-balgreen) |
| 2026-11-15 | V1 | - | oxford | - | - | publish | [oxf_004](https://ancienttrees.app/oxford/pococke-plane) |
| 2026-11-15 | W1 | - | - | - | - | hold | - |
| 2026-11-15 | X1 | - | bristol | - | - | publish | [bri_016](https://ancienttrees.app/bristol/bundle-planted-sessile-oak-bishops-knoll) |
| 2026-11-15 | Y1 | - | santalfio | - | - | publish | [sal_001](https://ancienttrees.app/santalfio/hundred-horse-chestnut) |
| 2026-11-15 | Y1 | - | - | - | - | hold | - |
| 2026-11-15 | Z1 | - | - | - | - | hold | - |
| 2026-11-15 | Z1 | - | bar | - | - | publish | [mtn_001](https://ancienttrees.app/bar/stara-maslina-old-olive-tree-of-mirovica) |
| 2026-11-15 | Z1 | - | - | - | - | hold | - |
| 2026-11-15 | Z1 | - | - | - | - | hold | - |
| 2026-11-15 | W1 | - | - | - | - | hold | - |
| 2026-11-15 | A2 | - | farnham | - | - | publish | [frn_001](https://ancienttrees.app/farnham/waverley-abbey-yew) |
| 2026-11-15 | Q1 | - | gort | - | - | publish | [gor_001](https://ancienttrees.app/gort/autograph-tree) |
| 2026-11-15 | G1 | - | - | - | - | hold | - |
| 2026-11-15 | G1 | - | nagoya | - | - | publish | [ngy_002](https://ancienttrees.app/nagoya/camphor-of-atsuta-shrine) |
| 2026-11-15 | B2 | - | palermo | - | - | publish | [pal_001](https://ancienttrees.app/palermo/ficus-of-piazza-marina) |
| 2026-11-15 | C2 | - | dunkeld | - | - | publish | [dnk_002](https://ancienttrees.app/dunkeld/birnam-oak) |
| 2026-11-15 | C2 | - | dunkeld | - | - | publish | [dnk_002](https://ancienttrees.app/dunkeld/birnam-oak) |
| 2026-11-15 | G1 | - | kyoto | - | - | publish | [kyo_002](https://ancienttrees.app/kyoto/land-boat-pine) |
| 2026-11-15 | D2 | - | york | - | - | publish | [yor_002](https://ancienttrees.app/york/cut-leaved-hornbeam) |
| 2026-11-15 | K1 | The King of the Forest | Dunkeld | - | - | publish | [dnk_010](https://ancienttrees.app/dunkeld/king-of-the-forest) |
| 2026-11-15 | J1 | The Geashill Sequoia | Geashill | - | - | publish | [gsh_001](https://ancienttrees.app/geashill/geashill-sequoia) |
| 2026-11-15 | M1 | The Plane of Cinar Street | Isparta | - | - | publish | [isp_001](https://ancienttrees.app/isparta/plane-of-cnar-sokak) |
| 2026-11-15 | R1 | Mariam Dearit | Keren | - | - | publish | [krn_001](https://ancienttrees.app/keren/mariam-dearit) |
| 2026-11-15 | I1 | The Sycamore at the Crum Creek Bridge (2 photos) | Willistown | - | - | publish | [wtn_001](https://ancienttrees.app/willistown/sycamore-at-the-crum-creek-bridge) |
| 2026-11-15 | E2 | The Moved Giant Sequoia of Fort Boise Park | Boise | - | - | publish | [boi_002](https://ancienttrees.app/boise/moved-giant-sequoia-of-fort-boise-park) |
| 2026-11-15 | F2 | The Lewisham Elm | London | - | - | publish | [lon_045](https://ancienttrees.app/london/lewisham-elm) |
| 2026-11-15 | W1 | The Green Beeches of the Nieuwe Kerkhof (2 photos) | Groningen | - | - | publish | [gro_014](https://ancienttrees.app/groningen/green-beeches-of-the-nieuwe-kerkhof) |
| 2026-11-15 | G2 | The Weeping Beech of the Schwanenbrücke (3 photos) | Munich | - | - | publish | [muc_014](https://ancienttrees.app/munich/weeping-beech-of-the-schwanenbrucke) |
| 2026-11-15 | W1 | The Pollarded Lindens of the Pepergasthuis | Groningen | - | - | publish | [gro_020](https://ancienttrees.app/groningen/pollarded-lindens-of-the-pepergasthuis) |
| 2026-11-15 | H2 | The Brace Elm | Brighton | - | - | publish | [bhm_002](https://ancienttrees.app/brighton/brace-elm) |
| 2026-11-15 | I2 | Tāne Mahuta (2 photos) | Waipoua Forest | - | - | publish | [wai_001](https://ancienttrees.app/waipoua-forest/tane-mahuta) |
| 2026-11-15 | F2 | The Evelyn Mulberry | London | - | - | publish | [lon_010](https://ancienttrees.app/london/evelyn-mulberry) |
| 2026-11-15 | E2 | The Cedars of the Konigsflugel | Bad Homburg | - | - | publish | [bhg_001](https://ancienttrees.app/bad-homburg/cedars-of-the-konigsflugel) |
| 2026-11-15 | V1 | The Pococke Plane | Oxford | - | - | publish | [oxf_004](https://ancienttrees.app/oxford/pococke-plane) |
| 2026-11-15 | J2 | Great Plane of Mottisfont | Mottisfont | - | - | publish | [mtf_001](https://ancienttrees.app/mottisfont/great-plane-of-mottisfont) |
| 2026-11-15 | G2 | The Fern-leaved Beech of the Amalienburg (2 photos) | Munich | - | - | publish | [muc_013](https://ancienttrees.app/munich/fern-leaved-beech-of-the-amalienburg) |
| 2026-11-15 | E2 | The Temple Tree of Landbohøjskolens Have | Copenhagen | - | - | publish | [cop_005](https://ancienttrees.app/copenhagen/temple-tree-of-landbohojskolens-have) |
| 2026-11-15 | G2 | The Oak of the Dörfchen, Nymphenburg (2 photos) | Munich | - | - | publish | [muc_007](https://ancienttrees.app/munich/oak-of-the-dorfchen-nymphenburg) |
| 2026-11-15 | I2 | The Fortingall Yew (2 photos) | Fortingall | - | - | publish | [for_001](https://ancienttrees.app/fortingall/fortingall-yew) |
| 2026-11-15 | E2 | El Árbol del Tule | Santa María del Tule | - | - | publish | [tul_001](https://ancienttrees.app/santa-maria-del-tule/el-arbol-del-tule) |
| 2026-11-15 | K2 | The Gomero de la Recoleta (2 photos) | Buenos Aires | - | - | publish | [bai_001](https://ancienttrees.app/buenos-aires/gomero-de-la-recoleta) |
| 2026-11-15 | I2 | Ashbrittle Yew | Ashbrittle | - | - | publish | [asb_001](https://ancienttrees.app/ashbrittle/ashbrittle-yew) |
| 2026-11-15 | L2 | The Toogood Road Fig | Cairns | - | - | publish | [cns_001](https://ancienttrees.app/cairns/toogood-road-fig) |
| 2026-11-15 | K2 | The Old Olive of Exo Chora | Zakynthos | - | - | publish | [zak_001](https://ancienttrees.app/zakynthos/old-olive-of-exo-chora) |
| 2026-11-15 | K2 | The Fig on the Abraaozinho Trail | Ilha Grande | - | - | publish | [ilg_001](https://ancienttrees.app/ilha-grande/fig-on-the-abraaozinho-trail) |
| 2026-11-15 | E2 | The Tarzan Tree | Algiers | - | - | publish | [alg_001](https://ancienttrees.app/algiers/tarzan-tree) |
| 2026-11-15 | E2 | The Elephant's Foot of Zapotitlan | Zapotitlan Salinas | - | - | publish | [zps_001](https://ancienttrees.app/zapotitlan-salinas/elephants-foot-of-zapotitlan) |
| 2026-11-15 | R | The Bromley Oak (2 photos) | London | Pedunculate Oak (Quercus robur | - | publish | [lon_046](https://ancienttrees.app/london/bromley-oak) |
| 2026-11-15 | G1 | The Great Cedar of Kasuga Taisha | Nara | Japanese Cedar (Cryptomeria ja | - | publish | [nra_002](https://ancienttrees.app/nara/great-cedar-of-kasuga-taisha) |
| 2026-11-15 | M2 | The Witch Tree of Fanal | Madeira | Til / Stinkwood (Ocotea foeten | - | open | - |
| 2026-11-15 | I2 | Marton Oak | - | Pedunculate Oak | - | hold | - |
| 2026-11-15 | L2 | Weeping Fig | cairns | Weeping Fig | 754 cm | publish | [cns_001](https://ancienttrees.app/cairns/toogood-road-fig) |
| 2026-11-15 | K2 | Olive | zakynthos | Olive | - | publish | [zak_001](https://ancienttrees.app/zakynthos/old-olive-of-exo-chora) |
| 2026-11-15 | E2 | The Tarzan Tree | algiers | Moreton Bay Fig | - | publish | [alg_001](https://ancienttrees.app/algiers/tarzan-tree) |
| 2026-11-15 | E2 | Ponytail Palm / Elephant's Foot | zapotitlan-salinas | Ponytail Palm / Elephant's Foo | - | publish | [zps_001](https://ancienttrees.app/zapotitlan-salinas/elephants-foot-of-zapotitlan) |
| 2026-11-15 | N2 | Malmö | - | - | - | hold | - |
| 2026-11-15 | O2 | Dawn Redwood in Toronto | - | Dawn Redwood | - | open | - |
| 2026-11-15 | P2 | whole veteran tree beside the manor | valdemarpils | old linden, twisted trunk, lon | - | publish | [vld_001](https://ancienttrees.app/valdemarpils/elku-linden-of-valdemarpils-linden-of-sacrifice) |
| 2026-11-15 | P2 | hollow in the old trunk | valdemarpils | linden bark and hollow | - | publish | [vld_001](https://ancienttrees.app/valdemarpils/elku-linden-of-valdemarpils-linden-of-sacrifice) |
| 2026-11-15 | P2 | trunk and limbs beside manor | valdemarpils | linden trunk and spreading lim | - | publish | [vld_001](https://ancienttrees.app/valdemarpils/elku-linden-of-valdemarpils-linden-of-sacrifice) |
| 2026-11-15 | Q2 | veteran oak with steel scaffold | warsaw | pedunculate oak, split trunk w | - | publish | [war_001](https://ancienttrees.app/warsaw/dab-mieszko-i-king-mieszko-is-oak) |
| 2026-11-15 | R2 | mature beech with unusual bark | york | beech, smooth trunk in autumn  | - | publish | [yor_003](https://ancienttrees.app/york/pear-barked-beech) |
| 2026-11-15 | G2 | large copper beech by the palace | munich | copper beech in rust autumn le | - | publish | [muc_011](https://ancienttrees.app/munich/copper-beech-of-the-badenburg) |
| 2026-11-15 | Q2 | tall multi-armed cactus in a car park | seville | giant cardon cactus, many arms | - | publish | [sev_044](https://ancienttrees.app/seville/cardon-of-the-expo) |
| 2026-11-15 | G2 | leaning lime by the lake | munich | old linden leaning over the la | - | publish | [muc_012](https://ancienttrees.app/munich/leaning-lime-of-the-badenburger-see) |
| 2026-11-15 | G2 | leaning lime, lake and dusk light | munich | old linden over the lake | - | publish | [muc_012](https://ancienttrees.app/munich/leaning-lime-of-the-badenburger-see) |
| 2026-11-15 | R2 | wide-crowned hornbeam in a park | york | hornbeam, bare crown with autu | - | publish | [yor_002](https://ancienttrees.app/york/cut-leaved-hornbeam) |
| 2026-11-15 | S2 | weeping beech trunk and pendant branches | dresden | weeping beech, wide fluted tru | - | publish | [dre_019](https://ancienttrees.app/dresden/weeping-beech-of-helfenberg-park) |
| 2026-11-15 | T2 | banyan-like fig with pillar roots | palermo | Ficus macrophylla, aerial root | - | publish | [pal_003](https://ancienttrees.app/palermo/ficus-of-the-orto-botanico) |
| 2026-11-15 | S2 | ancient lime with hollow trunk | dresden | large-leaved linden, multi-ste | - | publish | [dre_005](https://ancienttrees.app/dresden/kaditzer-linde) |
| 2026-11-15 | I2 | Giant Tree | - | Giant Sequoia | 1615 cm | publish | - |
| 2026-11-15 | I2 | Rockefeller - Tall Tree | humboldt-redwoods-state-park | Giant Sequoia | 1280 cm | publish | [hum_002](https://ancienttrees.app/humboldt-redwoods-state-park/tall-tree) |
| 2026-11-15 | U2 | Common Fig | manaccan | Common Fig | - | publish | [mnc_002](https://ancienttrees.app/manaccan/fig-in-manaccan-church-wall) |
| 2026-11-15 | U2 | Monterey Cypress (3 photos) | manaccan | Monterey Cypress | - | publish | [mnc_001](https://ancienttrees.app/manaccan/monterey-cypress-over-the-creek) |
| 2026-11-15 | V2 | The Linton Yew (3 photos) | linton-herefordshire | European Yew | 950 cm | publish | [lnt_001](https://ancienttrees.app/linton-herefordshire/linton-yew) |
| 2026-11-15 | W2 | Blue Jacaranda in Melbourne | - | Blue Jacaranda | - | hold | - |
| 2026-11-15 | X2 | Black Mulberry | lewes | Mulberry (Morus sp.) | - | publish | [lew_001](https://ancienttrees.app/lewes/southover-grange-mulberry) |
| 2026-11-15 | Y2 | Cedar of Lebanon | ulverston | Cedar (Cedrus sp.) | 755 cm | publish | [ulv_001](https://ancienttrees.app/ulverston/conishead-priory-cedar) |
| 2026-11-15 | Y2 | Douglas fir | ulverston | Fir (Abies sp.) | 582 cm | publish | [ulv_002](https://ancienttrees.app/ulverston/conishead-priory-douglas-fir) |
| 2026-11-15 | Q2 | King Jan's Linden | Warsaw | Linden | - | publish | [war_007](https://ancienttrees.app/warsaw/king-jans-linden) |
| 2026-11-15 | E2 | The Fern-leaved Beech of the National Galler | Copenhagen | Fern-leaved Beech | - | publish | [cop_026](https://ancienttrees.app/copenhagen/fern-leaved-beech-of-the-national-gallery) |
| 2026-11-15 | Z2 | The Anseman Oak | New Orleans | - | - | publish | [nol_002](https://ancienttrees.app/new-orleans/anseman-oak) |
| 2026-11-15 | Z2 | The Suicide Oak | New Orleans | - | - | publish | [nol_005](https://ancienttrees.app/new-orleans/suicide-oak) |
| 2026-11-15 | U2 | Wistman's Wood (4 photos) | Dartmoor | - | - | publish | [dmr_001](https://ancienttrees.app/dartmoor/wistmans-wood) |
| 2026-11-15 | U2 | The Fig in Manaccan Church Wall | Manaccan | Common Fig (Ficus carica) | - | publish | [mnc_002](https://ancienttrees.app/manaccan/fig-in-manaccan-church-wall) |
| 2026-11-15 | I2 | The Tall Tree | Humboldt Redwoods State Park | Coast Redwood (Sequoia semperv | - | publish | [hum_002](https://ancienttrees.app/humboldt-redwoods-state-park/tall-tree) |
| 2026-11-15 | X2 | The Southover Grange Mulberry | Lewes | Mulberry (Morus sp.) | - | publish | [lew_001](https://ancienttrees.app/lewes/southover-grange-mulberry) |
| 2026-11-15 | Y2 | The Conishead Priory Cedar | Ulverston | Cedar of Lebanon (Cedrus liban | - | publish | [ulv_001](https://ancienttrees.app/ulverston/conishead-priory-cedar) |
| 2026-11-15 | Y2 | The Conishead Priory Douglas Fir | Ulverston | Douglas Fir (Pseudotsuga menzi | - | publish | [ulv_002](https://ancienttrees.app/ulverston/conishead-priory-douglas-fir) |
| 2026-11-15 | W1 | The ANWB Linden of Wilhelminakade | Groningen | Common Lime (Tilia x europaea) | - | publish | [gro_018](https://ancienttrees.app/groningen/anwb-linden-of-wilhelminakade) |
| 2026-11-15 | A3 | Cedar of Lebanon near Hethersett | norwich | Cedar of Lebanon | - | publish | [nwc_001](https://ancienttrees.app/norwich/norwich-cathedral-cedar) |
| 2026-11-15 | B3 | English Hawthorn | - | English Hawthorn (Crataegus la | 50 cm | lead | - |
| 2026-11-15 | C3 | A tree near Edinburgh | - | - | - | hold | - |
| 2026-11-15 | D3 | Southern Live Oak | ormond-beach | Southern Live Oak | 32 cm | publish | [obc_001](https://ancienttrees.app/ormond-beach/fairchild-oak) |
| 2026-11-15 | D3 | The Fairchild Oak (2 photos) | ormond-beach | Southern Live Oak | 32 cm | publish | [obc_001](https://ancienttrees.app/ormond-beach/fairchild-oak) |
| 2026-11-15 | A3 | The Norwich Cathedral Cedar | norwich | Cedar of Lebanon | - | publish | [nwc_001](https://ancienttrees.app/norwich/norwich-cathedral-cedar) |
| 2026-11-15 | W1 | The Mespilifolia Oak of Noorderplantsoen | Groningen | Sessile Oak "Mespilifolia" (Qu | - | publish | [gro_016](https://ancienttrees.app/groningen/mespilifolia-oak-of-noorderplantsoen) |
| 2026-11-15 | W1 | The Oak of Martinikerkhof | Groningen | Pedunculate Oak (Quercus robur | - | publish | [gro_007](https://ancienttrees.app/groningen/oak-of-martinikerkhof) |
| 2026-11-15 | E3 | Pedunculate Oak (2 photos) | wantisden | Pedunculate Oak | - | open | [wnt_001](https://ancienttrees.app/wantisden/pollard-oaks-of-wantisden) |
| 2026-11-15 | F3 | Métaséquoia in La Tène | la-tene | Métaséquoia | 250 cm | open | [prf_003](https://ancienttrees.app/la-tene/dawn-redwood-of-prefargier) |
| 2026-11-15 | F3 | A tree in La Tène | la-tene | - | - | open | [prf_004](https://ancienttrees.app/la-tene/weeping-beeches-of-prefargier) |
| 2026-11-15 | F3 | Giant Sequoia in La Tène | la-tene | Giant Sequoia | 705 cm | open | [prf_002](https://ancienttrees.app/la-tene/giant-sequoia-of-prefargier) |
| 2026-11-15 | F3 | Large-leaved Lime in La Tène | la-tene | Large-leaved Lime | - | open | [prf_005](https://ancienttrees.app/la-tene/large-leaved-lime-of-prefargier) |
| 2026-11-15 | G3 | Elleholmseken (The Oak of Elleholm) | elleholm | Pedunculate Oak | 785 cm | open | [elh_001](https://ancienttrees.app/elleholm/elleholmseken-the-oak-of-elleholm) |
| 2026-11-15 | H3 | London Plane | maidstone | London Plane | 700 cm | open | [mdb_001](https://ancienttrees.app/maidstone/baobab-plane-of-penenden-heath) |
| 2026-11-15 | H3 | Pedunculate Oak near Mistley | colchester | Pedunculate Oak | 600 cm | open | [cls_001](https://ancienttrees.app/colchester/oak-of-clingoe-hill) |
| 2026-11-15 | I3 | Arbour Oak | - | Oak (Quercus sp.) | 700 cm | open | - |
| 2026-11-15 | J3 | The Oriental Plane of Landgoed Bantam | Hilversum | Oriental Plane | - | publish | [hil_001](https://ancienttrees.app/hilversum/oriental-plane-of-landgoed-bantam) |
| 2026-11-15 | K3 | The Hackberry of the Mura Latine | Rome | Hackberry | - | publish | [rom_028](https://ancienttrees.app/rome/hackberry-of-the-mura-latine) |
| 2026-11-15 | G3 | Rumskullaeken (the Kvill Oak) | Rumskulla | Pedunculate Oak | - | publish | [rkm_001](https://ancienttrees.app/rumskulla/rumskullaeken-the-kvill-oak) |
| 2026-11-15 | L3 | The Fremont Tree | Santa Cruz | Coast Redwood | - | publish | [scz_002](https://ancienttrees.app/santa-cruz/fremont-tree) |
| 2026-11-15 | M3 | Te Matua Ngahere | Waipoua Forest | Kauri | - | publish | [wai_002](https://ancienttrees.app/waipoua-forest/te-matua-ngahere) |
| 2026-11-15 | E3 | The Pollard Oaks of Wantisden | Wantisden | Pedunculate Oak | - | publish | [wnt_001](https://ancienttrees.app/wantisden/pollard-oaks-of-wantisden) |
| 2026-11-15 | G3 | Elleholmseken (The Oak of Elleholm) | Elleholm | Pedunculate Oak | - | publish | [elh_001](https://ancienttrees.app/elleholm/elleholmseken-the-oak-of-elleholm) |
| 2026-11-15 | H3 | The Baobab Plane of Penenden Heath | Maidstone | London Plane | - | publish | [mdb_001](https://ancienttrees.app/maidstone/baobab-plane-of-penenden-heath) |
| 2026-11-15 | H3 | The Oak of Clingoe Hill | Colchester | Pedunculate Oak | - | publish | [cls_001](https://ancienttrees.app/colchester/oak-of-clingoe-hill) |
| 2026-11-15 | N3 | The Library Ginkgo of Carmarthen | Carmarthen | Ginkgo | - | publish | [cmt_001](https://ancienttrees.app/carmarthen/library-ginkgo-of-carmarthen) |
| 2026-11-15 | F3 | The Giant Sequoia of Préfargier | La Tène | Giant Sequoia | - | publish | [prf_002](https://ancienttrees.app/la-tene/giant-sequoia-of-prefargier) |
| 2026-11-15 | F3 | The Dawn Redwood of Préfargier | La Tène | Dawn Redwood | - | publish | [prf_003](https://ancienttrees.app/la-tene/dawn-redwood-of-prefargier) |
| 2026-11-15 | F3 | The Weeping Beeches of Préfargier | La Tène | Weeping Beech | - | publish | [prf_004](https://ancienttrees.app/la-tene/weeping-beeches-of-prefargier) |
| 2026-11-15 | F3 | The Large-leaved Lime of Préfargier | La Tène | Large-leaved Lime | - | publish | [prf_005](https://ancienttrees.app/la-tene/large-leaved-lime-of-prefargier) |
| 2026-11-15 | T | Grimston's Oak | London | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-15 | O3 | The Plane Trees of the Circus | Bath | London Plane (Platanus x aceri | - | publish | [bat_003](https://ancienttrees.app/bath/plane-trees-of-the-circus) |
| 2026-11-15 | O3 | The Orange Courtyard of the Mezquita | Cordoba | Bitter Orange (Citrus aurantiu | - | publish | [cdb_002](https://ancienttrees.app/cordoba/orange-courtyard-of-the-mezquita) |
| 2026-11-15 | O3 | The Crom Yews | Crom | European Yew (Taxus baccata) | - | hold | - |
| 2026-11-15 | P3 | The Sunderland Buttonball Tree | Sunderland, Massachusetts | American Sycamore (Platanus oc | - | publish | [snd_001](https://ancienttrees.app/sunderland-massachusetts/sunderland-buttonball-tree) |
| 2026-11-15 | O3 | The Dawn Redwood by the Kelvin Statue (2 photos) | Belfast | Dawn Redwood (Metasequoia glyp | - | hold | - |
| 2026-11-15 | O3 | S'Olivera de Cort (2 photos) | Palma de Mallorca | Olive (Olea europaea) | - | hold | - |
| 2026-11-15 | P3 | Jackson's Oak | Mobile | Southern Live Oak (Quercus vir | - | publish | [mob_003](https://ancienttrees.app/mobile/jacksons-oak) |
| 2026-11-15 | P3 | Endicott Pear Tree | Boston | European Pear (Pyrus communis) | - | publish | [bos_013](https://ancienttrees.app/boston/endicott-pear-tree) |
| 2026-11-15 | O3 | The Olive of the Orange Courtyard | Cordoba | Olive (Olea europaea) | - | publish | [cdb_001](https://ancienttrees.app/cordoba/olive-of-the-orange-courtyard) |
| 2026-11-15 | Q3 | Methuselah Tree (Coast Redwood) | woodside | Coast Redwood | - | publish | [wdd_001](https://ancienttrees.app/woodside/methuselah-tree) |
| 2026-11-15 | R3 | A tree near Sēja | - | - | - | open | - |
| 2026-11-15 | R3 | A tree near Przybudki | - | - | - | open | - |
| 2026-11-15 | R3 | A tree near Chiang Mai | - | - | - | open | - |
| 2026-11-15 | S3 | The Old Yew Tree, St Cuthberts | doveridge | European Yew | - | publish | [dvr_001](https://ancienttrees.app/doveridge/doveridge-yew) |
| 2026-11-15 | S3 | Birch in Cannock Chase | - | Birch | - | open | - |
| 2026-11-15 | T3 | Moreton Bay Fig in Brisbane | - | Moreton Bay Fig | - | open | - |
| 2026-11-15 | I2 | Bodhi Tree at Buddha’s Birthplace | - | Bodhi Tree | - | open | - |
| 2026-11-15 | U3 | Sweet Chestnut in London: a Woodland Trust t | london | Sweet Chestnut | - | publish | [lon_053](https://ancienttrees.app/london/twisted-sweet-chestnut-of-greenwich-park) |
| 2026-11-15 | V3 | European Yew near Wilmington | crowhurst | European Yew | 1030 cm | publish | [crh_001](https://ancienttrees.app/crowhurst/crowhurst-yew) |
| 2026-11-15 | W3 | Il cipresso calvo di Villa Smeraldi | - | Cypress (Cupressus sp.) | - | open | - |
| 2026-11-15 | W3 | Quercia di Molinazzo | - | Oak (Quercus sp.) | 460 cm | open | - |
| 2026-11-15 | X3 | Ardkinglas Grand Fir | Ardkinglas | Grand Fir | - | publish | [akw_001](https://ancienttrees.app/ardkinglas/ardkinglas-grand-fir) |
| 2026-11-15 | X3 | Ardkinglas Silver Fir, the Mightiest Conifer | Ardkinglas | Silver Fir | - | publish | [akw_002](https://ancienttrees.app/ardkinglas/ardkinglas-silver-fir-the-mightiest-conifer) |
| 2026-11-15 | Y3 | Library Park Fig | Los Angeles | Fig | - | publish | [lax_031](https://ancienttrees.app/los-angeles/library-park-fig) |
| 2026-11-15 | J3 | The Variegated Maple of Coevorden Castle | Emmen | Maple | - | publish | [emm_008](https://ancienttrees.app/emmen/variegated-maple-of-coevorden-castle) |
| 2026-11-15 | O3 | The Twin Cypresses of the Parador | Granada | Cypress | - | publish | [gra_007](https://ancienttrees.app/granada/twin-cypresses-of-the-parador) |
| 2026-11-15 | Z3 | Xemxija Old Carob Tree | Malta | Carob | - | publish | [mlt_001](https://ancienttrees.app/malta/xemxija-old-carob-tree) |
| 2026-11-15 | R3 | Yang Na of the City Pillar, Wat Chedi Luang | Chiang Mai | Yang Na | - | hold | - |
| 2026-11-15 | O3 | The Boole Library Redwoods | Cork | Redwood | - | hold | - |
| 2026-11-15 | R3 | The Glasnevin Hybrid Strawberry Tree | Dublin | Hybrid Strawberry Tree | - | hold | - |
| 2026-11-15 | V3 | The Bowthorpe Oak | Bowthorpe | - | - | publish | [bow_001](https://ancienttrees.app/bowthorpe/bowthorpe-oak) |
| 2026-11-15 | V3 | The Crowhurst Yew | Crowhurst | - | - | publish | [crh_001](https://ancienttrees.app/crowhurst/crowhurst-yew) |
| 2026-11-15 | S3 | The Doveridge Yew | Doveridge | - | - | publish | [dvr_001](https://ancienttrees.app/doveridge/doveridge-yew) |
| 2026-11-15 | U3 | The Twisted Sweet Chestnut of Greenwich Park | London | - | - | publish | [lon_053](https://ancienttrees.app/london/twisted-sweet-chestnut-of-greenwich-park) |
| 2026-11-15 | Q3 | The Methuselah Tree | Woodside | - | - | publish | [wdd_001](https://ancienttrees.app/woodside/methuselah-tree) |
- From 104 readers: reader E2 9, reader G1 9, reader B1 8, reader F3 8, reader I2 8, reader O3 8, reader T 8, reader W1 7, reader G2 6, reader R3 5, reader G 4, reader H3 4, reader K2 4, reader U2 4, reader Y2 4, reader Z1 4, reader G3 3, reader P2 3, reader P3 3, reader Q2 3, reader S3 3, reader V3 3, reader A3 2, reader C2 2, reader D3 2, reader E 2, reader E3 2, reader F2 2, reader H1 2, reader I1 2, reader J1 2, reader J3 2, reader K1 2, reader L 2, reader L2 2, reader M1 2, reader O 2, reader P 2, reader Q 2, reader Q1 2, reader Q3 2, reader R 2, reader R1 2, reader R2 2, reader S2 2, reader U 2, reader U3 2, reader V 2, reader V1 2, reader W3 2, reader X 2, reader X2 2, reader X3 2, reader Y 2, reader Y1 2, reader Z2 2, reader A 1, reader A1 1, reader A2 1, reader B 1, reader B2 1, reader B3 1, reader C 1, reader C1 1, reader C3 1, reader D 1, reader D1 1, reader D2 1, reader E1 1, reader F 1, reader F1 1, reader H 1, reader H2 1, reader I 1, reader I3 1, reader J 1, reader J2 1, reader K 1, reader K3 1, reader L1 1, reader L3 1, reader M 1, reader M2 1, reader M3 1, reader N 1, reader N1 1, reader N2 1, reader N3 1, reader O1 1, reader O2 1, reader P1 1, reader S 1, reader S1 1, reader T1 1, reader T2 1, reader T3 1, reader U1 1, reader V2 1, reader W 1, reader W2 1, reader X1 1, reader Y3 1, reader Z 1, reader Z3 1.
- Photographs and the readers' own words: `python3 scripts/inspect_readers.py` (a local page, never in this public file). Your answer goes in with `python3 scripts/judgement.py --feedback <id> "..."`.

**Waiting for you** (what the runs left for you since 2026-11-15)

- 246 email addresses ready to mail (archive 0, nature 9, guide 8, press 135, source 58, council 16, society 7, tourism 5, other 5, garden 3); **the night run found no new contacts in two days**
- the daily task "publish-held-trees-daily" can be switched off under Scheduled; write passes now put trees straight into the app, so nothing waits for it.
- North Berwick Law (trees for the 1707 Act of Union, per the reader; trees too small in the frame, no source), a contorted pagoda tree or robinia at an inn in Fertoujlak, Hungary (shot up the trunk, no note; sent twice), 
- three reply drafts wait for his yes: drafts/reply-reader-786 (Tree Council tip), -813 (Coldwaltham, thumbnail), -802 (Lusnizza oak, asks for a photo).

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-14 | A4 | The Taşlı Çınar | Istanbul | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/istanbul/tasl-cnar) |
| 11-14 | A4 | The Gülhane London Plane | Istanbul | a reader's photograph, published | [live](https://ancienttrees.app/istanbul/gulhane-london-plane) |
| 11-14 | A4 | The Gülhane Nettle Tree | Istanbul | a reader's photograph, published | [live](https://ancienttrees.app/istanbul/gulhane-nettle-tree) |
| 11-15 | R | Coldwaltham Yew | Coldwaltham | a reader's photograph, published | [live](https://ancienttrees.app/coldwaltham/coldwaltham-yew) |
| 11-15 | S | The Belvoir Oak | Belfast | a reader's photograph, published | [live](https://ancienttrees.app/belfast/belvoir-oak) |
| 11-15 | T | The Fulham Palace Oak | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/fulham-palace-oak) |
| 11-15 | T | Barney the Plane | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/barney-the-plane) |
| 11-15 | U | The Argyle Street Ash | Glasgow | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/glasgow/argyle-street-ash) |
| 11-15 | U | El Drago Milenario | Tenerife | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tenerife/el-drago-milenario) |
| 11-15 | T | The Ravenscourt Park Baobab Plane | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/ravenscourt-park-baobab-plane) |
| 11-15 | O | The Red Gum of the Rostrevor Creek | Adelaide | a reader's photograph, published | [live](https://ancienttrees.app/adelaide/red-gum-of-the-rostrevor-creek) |
| 11-15 | P | The Canary Pine of Leighton Gardens | Moss Vale | a reader's photograph, published | [live](https://ancienttrees.app/moss-vale/canary-pine-of-leighton-gardens) |
| 11-15 | T | The Totteridge Yew | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/totteridge-yew) |
| 11-15 | T | The Ravenscourt Park Tree of Heaven | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/ravenscourt-park-tree-of-heaven) |
| 11-15 | A1 | The Plane of Saint Gerasimos, Omala | Kefalonia | a reader's photograph, published | [live](https://ancienttrees.app/kefalonia/plane-of-saint-gerasimos-omala) |
| 11-15 | Z | Giant Norfolk Island Pine of Lagoa das Furnas | Azores | a reader's photograph, published | [live](https://ancienttrees.app/azores/giant-norfolk-island-pine-of-lagoa-das-furnas) |
| 11-15 | V | The Bruce Castle Oak | London | a reader's photograph, published | [live](https://ancienttrees.app/london/bruce-castle-oak) |
| 11-15 | X | The Cedar of Brecon Cathedral | Brecon | a reader's photograph, published | [live](https://ancienttrees.app/brecon/cedar-of-brecon-cathedral) |
| 11-15 | B1 | The Redford Wood Redwood | Edinburgh | a reader's photograph, published | [live](https://ancienttrees.app/edinburgh/redford-wood-redwood) |
| 11-15 | C1 | Giant Australian Rubber Tree of Jardim Antonio Borges | Azores | a reader's photograph, published | [live](https://ancienttrees.app/azores/giant-australian-rubber-tree-of-jardim-antonio-borges) |
| 11-15 | B1 | Robert Louis Stevenson's Yew | Edinburgh | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/edinburgh/robert-louis-stevensons-yew) |
| 11-15 | B1 | The Sitka Spruce at Scone Palace | Dunkeld | a reader's photograph, published | [live](https://ancienttrees.app/dunkeld/sitka-spruce-at-scone-palace) |
| 11-15 | B1 | The Lytham Sweet Chestnut | Lytham | a reader's photograph, published | [live](https://ancienttrees.app/lytham/lytham-sweet-chestnut) |
| 11-15 | F1 | The Geelong Ginkgo | Geelong | a reader's photograph, published | [live](https://ancienttrees.app/geelong/geelong-ginkgo) |
| 11-15 | G1 | The Kyushaku-fuji of Byakugo-ji | Tamba | a reader's photograph, published | [live](https://ancienttrees.app/tamba/kyushaku-fuji-of-byakugo-ji) |
| 11-15 | T | The Royal Oak | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/royal-oak) |
| 11-15 | T | The Windrush Square Plane | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/windrush-square-plane) |
| 11-15 | G1 | The A-bombed Camphors of Sannō Shrine | Nagasaki | a reader's photograph, published | [live](https://ancienttrees.app/nagasaki/a-bombed-camphors-of-sanno-shrine) |
| 11-15 | S1 | The Market Bosworth Yew | Market Bosworth | a reader's photograph, published | [live](https://ancienttrees.app/market-bosworth/market-bosworth-yew) |
| 11-15 | T1 | Kett's Oak | Hethersett | a reader's photograph, published | [live](https://ancienttrees.app/hethersett/ketts-oak) |
| 11-15 | G1 | The Pine of Ukimidō | Ōtsu | a reader's photograph, published | [live](https://ancienttrees.app/otsu/pine-of-ukimido) |
| 11-15 | H1 | The Gnarled Beech of Hampstead Heath | London | a reader's photograph, published | [live](https://ancienttrees.app/london/gnarled-beech-of-hampstead-heath) |
| 11-15 | U1 | The Giant of Mount Horne | Grenada | a reader's photograph, published | [live](https://ancienttrees.app/grenada/giant-of-mount-horne) |
| 11-15 | I1 | The Sycamore at the Crum Creek Bridge | Willistown | a reader's photograph, published | [live](https://ancienttrees.app/willistown/sycamore-at-the-crum-creek-bridge) |
| 11-15 | B1 | The Wheatley Elm of Balgreen | Edinburgh | a reader's photograph, published | [live](https://ancienttrees.app/edinburgh/wheatley-elm-of-balgreen) |
| 11-15 | J1 | The Geashill Sequoia | Geashill | a reader's photograph, published | [live](https://ancienttrees.app/geashill/geashill-sequoia) |
| 11-15 | K1 | The King of the Forest | Dunkeld | a reader's photograph, published | [live](https://ancienttrees.app/dunkeld/king-of-the-forest) |
| 11-15 | M1 | The Plane of Çınar Sokak | Isparta | a reader's photograph, published | [live](https://ancienttrees.app/isparta/plane-of-cnar-sokak) |
| 11-15 | R1 | Mariam Dearit | Keren | a reader's photograph, published | [live](https://ancienttrees.app/keren/mariam-dearit) |
| 11-15 | V1 | The Pococke Plane | Oxford | a reader's photograph, published | [live](https://ancienttrees.app/oxford/pococke-plane) |
| 11-15 | X1 | The Bundle-planted Sessile Oak, Bishops Knoll | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/bundle-planted-sessile-oak-bishops-knoll) |
| 11-15 | Y1 | The Hundred-Horse Chestnut | Sant'Alfio | a reader's photograph, published | [live](https://ancienttrees.app/santalfio/hundred-horse-chestnut) |
| 11-15 | Z1 | Stara Maslina (Old Olive Tree of Mirovica) | Bar | a reader's photograph, published | [live](https://ancienttrees.app/bar/stara-maslina-old-olive-tree-of-mirovica) |
| 11-15 | A2 | Waverley Abbey Yew | Farnham | a reader's photograph, published | [live](https://ancienttrees.app/farnham/waverley-abbey-yew) |
| 11-15 | Q1 | The Autograph Tree | Gort | a reader's photograph, published | [live](https://ancienttrees.app/gort/autograph-tree) |
| 11-15 | G1 | The Camphor of Atsuta Shrine | Nagoya | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/nagoya/camphor-of-atsuta-shrine) |
| 11-15 | B2 | The Ficus of Piazza Marina | Palermo | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/palermo/ficus-of-piazza-marina) |
| 11-15 | C2 | The Birnam Oak | Dunkeld | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dunkeld/birnam-oak) |
| 11-15 | C2 | The Birnam Oak | Dunkeld | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dunkeld/birnam-oak) |
| 11-15 | G1 | The Land Boat Pine | Kyoto | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kyoto/land-boat-pine) |
| 11-15 | D2 | The Cut-Leaved Hornbeam | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/cut-leaved-hornbeam) |
| 11-15 | L2 | The Toogood Road Fig | Cairns | a reader's photograph, published | [live](https://ancienttrees.app/cairns/toogood-road-fig) |
| 11-15 | K2 | The Old Olive of Exo Chora | Zakynthos | a reader's photograph, published | [live](https://ancienttrees.app/zakynthos/old-olive-of-exo-chora) |
| 11-15 | K2 | The Fig on the Abraãozinho Trail | Ilha Grande | a reader's photograph, published | [live](https://ancienttrees.app/ilha-grande/fig-on-the-abraaozinho-trail) |
| 11-15 | E2 | The Tarzan Tree | Algiers | a reader's photograph, published | [live](https://ancienttrees.app/algiers/tarzan-tree) |
| 11-15 | E2 | The Elephant's Foot of Zapotitlán | Zapotitlán Salinas | a reader's photograph, published | [live](https://ancienttrees.app/zapotitlan-salinas/elephants-foot-of-zapotitlan) |
| 11-15 | E2 | The Moved Giant Sequoia of Fort Boise Park | Boise | a reader's photograph, published | [live](https://ancienttrees.app/boise/moved-giant-sequoia-of-fort-boise-park) |
| 11-15 | F2 | The Lewisham Elm | London | a reader's photograph, published | [live](https://ancienttrees.app/london/lewisham-elm) |
| 11-15 | W1 | The Green Beeches of the Nieuwe Kerkhof | Groningen | a reader's photograph, published | [live](https://ancienttrees.app/groningen/green-beeches-of-the-nieuwe-kerkhof) |
| 11-15 | G2 | The Weeping Beech of the Schwanenbrücke | Munich | a reader's photograph, published | [live](https://ancienttrees.app/munich/weeping-beech-of-the-schwanenbrucke) |
| 11-15 | G2 | The Weeping Beech of the Schwanenbrücke | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/weeping-beech-of-the-schwanenbrucke) |
| 11-15 | W1 | The Pollarded Lindens of the Pepergasthuis | Groningen | a reader's photograph, published | [live](https://ancienttrees.app/groningen/pollarded-lindens-of-the-pepergasthuis) |
| 11-15 | H2 | The Brace Elm | Brighton | a reader's photograph, published | [live](https://ancienttrees.app/brighton/brace-elm) |
| 11-15 | I2 | Tāne Mahuta | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/tane-mahuta) |
| 11-15 | F2 | The Evelyn Mulberry | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/evelyn-mulberry) |
| 11-15 | E2 | The Cedars of the Konigsflugel | Bad Homburg | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/bad-homburg/cedars-of-the-konigsflugel) |
| 11-15 | V1 | The Pococke Plane | Oxford | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/oxford/pococke-plane) |
| 11-15 | J2 | Great Plane of Mottisfont | Mottisfont | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mottisfont/great-plane-of-mottisfont) |
| 11-15 | G2 | The Fern-leaved Beech of the Amalienburg | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/fern-leaved-beech-of-the-amalienburg) |
| 11-15 | E2 | The Temple Tree of Landbohøjskolens Have | Copenhagen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/copenhagen/temple-tree-of-landbohojskolens-have) |
| 11-15 | E2 | El Drago Milenario | Tenerife | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tenerife/el-drago-milenario) |
| 11-15 | G2 | The Oak of the Dörfchen, Nymphenburg | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/oak-of-the-dorfchen-nymphenburg) |
| 11-15 | G2 | The Oak of the Dörfchen, Nymphenburg | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/oak-of-the-dorfchen-nymphenburg) |
| 11-15 | I2 | The Fortingall Yew | Fortingall | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/fortingall/fortingall-yew) |
| 11-15 | R | Coldwaltham Yew | Coldwaltham | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/coldwaltham/coldwaltham-yew) |
| 11-15 | E2 | El Árbol del Tule | Santa María del Tule | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/santa-maria-del-tule/el-arbol-del-tule) |
| 11-15 | I1 | The Sycamore at the Crum Creek Bridge | Willistown | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/willistown/sycamore-at-the-crum-creek-bridge) |
| 11-15 | K2 | The Gomero de la Recoleta | Buenos Aires | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/buenos-aires/gomero-de-la-recoleta) |
| 11-15 | I2 | Tāne Mahuta | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/tane-mahuta) |
| 11-15 | I2 | Ashbrittle Yew | Ashbrittle | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/ashbrittle/ashbrittle-yew) |
| 11-15 | P2 | Elku Linden of Valdemārpils (Linden of Sacrifice) | Valdemārpils | a reader's photograph, published | [live](https://ancienttrees.app/valdemarpils/elku-linden-of-valdemarpils-linden-of-sacrifice) |
| 11-15 | P2 | Elku Linden of Valdemārpils (Linden of Sacrifice) | Valdemārpils | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/valdemarpils/elku-linden-of-valdemarpils-linden-of-sacrifice) |
| 11-15 | P2 | Elku Linden of Valdemārpils (Linden of Sacrifice) | Valdemārpils | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/valdemarpils/elku-linden-of-valdemarpils-linden-of-sacrifice) |
| 11-15 | Q2 | Dab Mieszko I (King Mieszko I's Oak) | Warsaw | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/warsaw/dab-mieszko-i-king-mieszko-is-oak) |
| 11-15 | R2 | The Pear-Barked Beech | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/pear-barked-beech) |
| 11-15 | G2 | The Copper Beech of the Badenburg | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/copper-beech-of-the-badenburg) |
| 11-15 | E2 | The Gomero de la Recoleta | Buenos Aires | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/buenos-aires/gomero-de-la-recoleta) |
| 11-15 | G2 | The Fern-leaved Beech of the Amalienburg | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/fern-leaved-beech-of-the-amalienburg) |
| 11-15 | Q2 | The Cardón of the Expo | Seville | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/seville/cardon-of-the-expo) |
| 11-15 | G2 | The Leaning Lime of the Badenburger See | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/leaning-lime-of-the-badenburger-see) |
| 11-15 | G2 | The Leaning Lime of the Badenburger See | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/leaning-lime-of-the-badenburger-see) |
| 11-15 | I2 | The Fortingall Yew | Fortingall | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/fortingall/fortingall-yew) |
| 11-15 | R2 | The Cut-Leaved Hornbeam | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/cut-leaved-hornbeam) |
| 11-15 | R | The Bromley Oak | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/bromley-oak) |
| 11-15 | R | The Bromley Oak | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/bromley-oak) |
| 11-15 | G1 | The Great Cedar of Kasuga Taisha | Nara | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/nara/great-cedar-of-kasuga-taisha) |
| 11-15 | S2 | The Weeping Beech of Helfenberg Park | Dresden | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dresden/weeping-beech-of-helfenberg-park) |
| 11-15 | T2 | The Ficus of the Orto Botanico | Palermo | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/palermo/ficus-of-the-orto-botanico) |
| 11-15 | S2 | The Kaditzer Linde | Dresden | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dresden/kaditzer-linde) |
| 11-15 | Q2 | King Jan's Linden | Warsaw | a reader's photograph, published | [live](https://ancienttrees.app/warsaw/king-jans-linden) |
| 11-15 | E2 | The Fern-leaved Beech of the National Gallery | Copenhagen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/copenhagen/fern-leaved-beech-of-the-national-gallery) |
| 11-15 | Z2 | The Anseman Oak | New Orleans | a reader's photograph, published | [live](https://ancienttrees.app/new-orleans/anseman-oak) |
| 11-15 | Z2 | The Suicide Oak | New Orleans | a reader's photograph, published | [live](https://ancienttrees.app/new-orleans/suicide-oak) |
| 11-15 | U2 | Wistman's Wood | Dartmoor | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dartmoor/wistmans-wood) |
| 11-15 | U2 | Wistman's Wood | Dartmoor | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dartmoor/wistmans-wood) |
| 11-15 | G2 | The Weeping Beech of the Schwanenbrücke | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/weeping-beech-of-the-schwanenbrucke) |
| 11-15 | W1 | The Mespilifolia Oak of Noorderplantsoen | Groningen | a reader's photograph, published | [live](https://ancienttrees.app/groningen/mespilifolia-oak-of-noorderplantsoen) |
| 11-15 | W1 | The Oak of Martinikerkhof | Groningen | a reader's photograph, published | [live](https://ancienttrees.app/groningen/oak-of-martinikerkhof) |
| 11-15 | W1 | The Green Beeches of the Nieuwe Kerkhof | Groningen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/groningen/green-beeches-of-the-nieuwe-kerkhof) |
| 11-15 | O | The Red Gum of Glynburn Road | Adelaide | a reader's photograph, published | [live](https://ancienttrees.app/adelaide/red-gum-of-glynburn-road) |
| 11-15 | I2 | The Tall Tree | Humboldt Redwoods State Park | a reader's photograph, published | [live](https://ancienttrees.app/humboldt-redwoods-state-park/tall-tree) |
| 11-15 | U2 | The Fig in Manaccan Church Wall | Manaccan | a reader's photograph, published | [live](https://ancienttrees.app/manaccan/fig-in-manaccan-church-wall) |
| 11-15 | V2 | The Linton Yew | Linton, Herefordshire | a reader's photograph, published | [live](https://ancienttrees.app/linton-herefordshire/linton-yew) |
| 11-15 | U2 | The Monterey Cypress over the Creek | Manaccan | a reader's photograph, published | [live](https://ancienttrees.app/manaccan/monterey-cypress-over-the-creek) |
| 11-15 | L3 | The Fremont Tree | Santa Cruz | a reader's photograph, published | [live](https://ancienttrees.app/santa-cruz/fremont-tree) |
| 11-15 | G3 | Rumskullaeken (the Kvill Oak) | Rumskulla | a reader's photograph, published | [live](https://ancienttrees.app/rumskulla/rumskullaeken-the-kvill-oak) |
| 11-15 | W1 | The ANWB Linden of Wilhelminakade | Groningen | a reader's photograph, published | [live](https://ancienttrees.app/groningen/anwb-linden-of-wilhelminakade) |
| 11-15 | J3 | The Oriental Plane of Landgoed Bantam | Hilversum | a reader's photograph, published | [live](https://ancienttrees.app/hilversum/oriental-plane-of-landgoed-bantam) |
| 11-15 | K3 | The Hackberry of the Mura Latine | Rome | a reader's photograph, published | [live](https://ancienttrees.app/rome/hackberry-of-the-mura-latine) |
| 11-15 | M3 | Te Matua Ngahere | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/te-matua-ngahere) |
| 11-15 | A3 | The Norwich Cathedral Cedar | Norwich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/norwich/norwich-cathedral-cedar) |
| 11-15 | D3 | The Fairchild Oak | Ormond Beach | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/ormond-beach/fairchild-oak) |
| 11-15 | X3 | Ardkinglas Silver Fir, the Mightiest Conifer | Ardkinglas | a reader's photograph, published | [live](https://ancienttrees.app/ardkinglas/ardkinglas-silver-fir-the-mightiest-conifer) |
| 11-15 | X3 | Ardkinglas Grand Fir | Ardkinglas | a reader's photograph, published | [live](https://ancienttrees.app/ardkinglas/ardkinglas-grand-fir) |
| 11-15 | Y3 | Library Park Fig | Los Angeles | a reader's photograph, published | [live](https://ancienttrees.app/los-angeles/library-park-fig) |
| 11-15 | J3 | The Variegated Maple of Coevorden Castle | Emmen | a reader's photograph, published | [live](https://ancienttrees.app/emmen/variegated-maple-of-coevorden-castle) |
| 11-15 | O3 | The Twin Cypresses of the Parador | Granada | a reader's photograph, published | [live](https://ancienttrees.app/granada/twin-cypresses-of-the-parador) |
| 11-15 | Z3 | Xemxija Old Carob Tree | Malta | a reader's photograph, published | [live](https://ancienttrees.app/malta/xemxija-old-carob-tree) |
| 11-15 | O3 | The Plane Trees of the Circus | Bath | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/bath/plane-trees-of-the-circus) |
| 11-15 | P3 | Endicott Pear Tree | Boston | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/boston/endicott-pear-tree) |
| 11-15 | O3 | The Olive of the Orange Courtyard | Cordoba | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/cordoba/olive-of-the-orange-courtyard) |
| 11-15 | O3 | The Orange Courtyard of the Mezquita | Cordoba | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/cordoba/orange-courtyard-of-the-mezquita) |
| 11-15 | P3 | Jackson's Oak | Mobile | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mobile/jacksons-oak) |
| 11-15 | P3 | S'Olivera de Cort | Palma de Mallorca | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/palma-de-mallorca/solivera-de-cort) |
| 11-15 | P3 | The Sunderland Buttonball Tree | Sunderland, Massachusetts | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sunderland-massachusetts/sunderland-buttonball-tree) |
| 11-16 | L | The Becks Prime Augusta Live Oaks | Houston | a reader's photograph, published | [live](https://ancienttrees.app/houston/becks-prime-augusta-live-oaks) |
| 11-16 | L | The Old Pecan Tree | Houston | a reader's photograph, published | [live](https://ancienttrees.app/houston/old-pecan-tree) |
| 11-16 | M | The Kapok Tree | Key West | a reader's photograph, published | [live](https://ancienttrees.app/key-west/kapok-tree) |
| 11-16 | N | The Rhodes Bald Cypress | Richard Bong State Recreation Area | a reader's photograph, published | [live](https://ancienttrees.app/richard-bong-state-recreation-area/rhodes-bald-cypress) |
| 11-16 | A | The Borrowdale Yews (the Fraternal Four) | Borrowdale | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/borrowdale/borrowdale-yews-the-fraternal-four) |
| 11-16 | C | The Angel Oak | Charleston | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/charleston/angel-oak) |
| 11-16 | B | Ahuehuete de Parque Espana | Mexico City | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mexico-city/ahuehuete-de-parque-espana) |
| 11-16 | B | Ahuehuete de Parque Espana | Mexico City | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mexico-city/ahuehuete-de-parque-espana) |
| 11-15 | B4 | Faux de Verzy | Reims | a reader's tree changed the page | - |
| 11-15 | C4 | Wyndham's Oak | Gillingham, Dorset | a reader's tree changed the page | - |
| 11-15 | Q1 | The picture card perfect pines in Connamara | Connamara | a reader's tree changed the page | - |
| 11-15 | D4 | The Master Oak | Stanmore | a reader's tree changed the page | - |
| 11-15 | Z | - | - | a reader's feedback changed the page | - |
| 11-15 | E4 | The Zaandam wingnut | Zaandam | a reader's tree changed the page | - |
| 11-15 | N1 | Old Knobbley | Essex, Mistley | a reader's tree changed the page | - |
- From 73 readers: reader G2 10, reader E2 9, reader T 7, reader G1 6, reader I2 6, reader W1 6, reader B1 5, reader O3 4, reader P3 4, reader R 4, reader U2 4, reader A4 3, reader K2 3, reader P2 3, reader Q2 3, reader B 2, reader C2 2, reader F2 2, reader I1 2, reader J3 2, reader L 2, reader O 2, reader Q1 2, reader R2 2, reader S2 2, reader U 2, reader V1 2, reader X3 2, reader Z 2, reader Z2 2, reader A 1, reader A1 1, reader A2 1, reader A3 1, reader B2 1, reader B4 1, reader C 1, reader C1 1, reader C4 1, reader D2 1, reader D3 1, reader D4 1, reader E4 1, reader F1 1, reader G3 1, reader H1 1, reader H2 1, reader J1 1, reader J2 1, reader K1 1, reader K3 1, reader L2 1, reader L3 1, reader M 1, reader M1 1, reader M3 1, reader N 1, reader N1 1, reader P 1, reader R1 1, reader S 1, reader S1 1, reader T1 1, reader T2 1, reader U1 1, reader V 1, reader V2 1, reader X 1, reader X1 1, reader Y1 1, reader Y3 1, reader Z1 1, reader Z3 1.

**What was sent in, and what we decided**

| seen | what | where | size for its species | ours | Hidde |
|---|---|---|---|---|---|
| 2026-11-16 | Ahuehuete de Parque Espana | Mexico City | - | publish | - |
| 2026-11-16 | Eastern Cottonwood | - | - | open | - |
| 2026-11-16 | Baobab | - | - | open | - |
| 2026-11-15 | River Red Gum | - | - | publish | - |
| 2026-11-15 | Giant Australian Rubber Tree of Jardim | Azores | - | publish | - |
| 2026-11-15 | A tree I found | - | - | hold | - |
| 2026-11-15 | The Weeping Beech of the Schwanenbrück | Munich | - | publish | - |
| 2026-11-15 | El Drago Milenario | Tenerife | - | publish | - |
| 2026-11-15 | The Oak of the Dörfchen, Nymphenburg | Munich | - | publish | - |
| 2026-11-15 | Coldwaltham Yew | Coldwaltham | - | publish | - |
| 2026-11-15 | The Sycamore at the Crum Creek Bridge | Willistown | - | publish | - |
| 2026-11-15 | Tāne Mahuta | Waipoua Forest | - | publish | - |
| 2026-11-15 | The Fern-leaved Beech of the Amalienbu | Munich | - | publish | - |
| 2026-11-15 | The Fortingall Yew | Fortingall | - | publish | - |
| 2026-11-15 | The Bromley Oak | London | - | publish | - |

35 waiting for a verdict. Disagree with one and the rule changes: `python3 scripts/judgement.py --feedback <id> "..."`, and `--learn` prints every verdict he has overruled.

**Searched yesterday:** london (35 times), bristol (15 times), berlin (14 times), lond (14 times), lon (11 times), dublin (9 times), edinburgh (9 times), manchester (8 times), oxford (8 times), sheff (8 times), cambridge (7 times), cardiff (7 times), glasgow (7 times), norwich (7 times), paris (6 times), bath (5 times), chichester (5 times), edin (5 times), exeter (5 times), sheffield (5 times).

**App crashes** (last 7 days, store builds; MetricKit, a sample)

| Crashes | Kind | Build | Where | Phones | Last | Fix |
|---:|---|---|---|---:|---|---|
| 1 | crash | 1.0.4 (41) | (no AncientTrees frame) | 1 | 2026-11-15 | none |

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 11-06 | 1 | 35 | 2.9% | 36.6 |
| 11-07 | 2 | 34 | 5.9% | 38.3 |
| 11-08 | 25 | 1013 | 2.5% | 9.1 |
| 11-09 | 28 | 1177 | 2.4% | 8.9 |
| 11-10 | 8 | 196 | 4.1% | 13.0 |
| 11-11 | 1 | 16 | 6.2% | 22.1 |
| 11-12 | 1 | 28 | 3.6% | 31.4 |
| 11-13 | 1 | 32 | 3.1% | 55.0 |
| 11-14 | 0 | 51 | 0.0% | 57.7 |
| 11-15 *partial* | 182 | 303 | 60.1% | 5.5 |
| **window** | **249** | **2885** | **8.6%** | |
- Top queries (10d): ancient trees app (i190, p1); ancient trees (i14, p30); ancient tree app (i1, p1); skovfogedegen (i1, p4); 2 quai saint bernard 75005 paris (i1, p91)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-07 | 80 | 7 | 8.8% |
| 11-08 | 126 | 9 | 7.1% |
| 11-09 | 151 | 4 | 2.6% |
| 11-10 | 136 | 9 | 6.6% |
| 11-11 | 97 | 7 | 7.2% |
| 11-12 | 190 | 4 | 2.1% |
| 11-13 | 125 | 5 | 4.0% |
| **7 days** | **905** | **45** | **5.0%** |
- **BING WATCHDOG:** impressions fell from 2953 to 905 week on week. That is the shape of a demotion; read the Bing Webmaster dashboard today.
- Top Bing queries: oldest tree china (c8/i4, p12); platane du square des batignolles (c4/i2, p1); picture of the tree in helsinki city center that was preserved (c3/i2, p4); ancient trees app (c2/i8, p5); who planted the western red cedar tree in blarney ireland (c2/i8, p2); fig tree in square alicante (c2/i4, p4); palma del cile (c2/i2, p6); cipresso calvo indro montanelli milano (c2/i2, p8)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

**Monday: the slow tables.** They rarely change a day's decision, so they come once a week.

**Website actions, ever** (the events table begins 2026-08-01, when the funnel was repaired; a zero has never fired at all)

| Action | Ever |
|---|---:|
| app-cta | 383 |
| search-home | 176 |
| waitlist-submit | 86 |
| search-bar | 16 |
| search-none-home | 16 |
| home-country | 14 |
| signin-open | 12 |
| home-visitors | 11 |
| search-explore | 11 |
| home-fav | 11 |
| search-bar-m | 9 |
| app-open | 7 |
| empty-place-add | 6 |
| share_tapped | 6 |
| home-oldest | 5 |
| search-empty-home | 5 |
| signin-oauth | 5 |
| signin-done | 4 |
| directions | 3 |
| search-none-explore | 3 |
| share_arrived | 2 |
| suggestion-submit | 2 |
| home-dir-city | 1 |
| home-dir-collection | 1 |
| home-park | 1 |
| plus-open | 1 |
| search-empty-bar | 1 |
| search-empty-bar-m | 1 |
| search-none-bar | 1 |
| save | 0 |
| signin-link-sent | 0 |
| worthit-not worth it | 0 |
| worthit-worth it | 0 |
| **all** | **800** |

**App events, ever** (measured since 2026-08-30)

| What | Ever |
|---|---:|
| app_open | 5229 |
| tab | 3091 |
| tree_opened | 10332 |
| directions | 262 |
| tree_saved | 278 |
| tree_visited | 145 |
| sighting_recorded | 318 |
| sync_skipped | 0 |
| sync_failed | 0 |
| location | 3899 |
| share_tapped | 103 |
| plus-open | 62 |
| plus-answer | 3 |
| plus-tellme | 1 |
| **all** | **23723** |

**What readers told us** (7 days, structure only; the words stay in the database)

| Day | Tree | What | Note | From | Outcome |
|---|---|---|---|---|---|
| 11-13 | The Oak of Villa Salina Park | tree sent in | 1338 chars, read it in the database | 7e0c | - |
| 11-15 | exe_002 (Kenn Yew) | worth it | - | 166b | - |
| 11-15 | exe_001 (Heavitree Yew) | worth it | - | 166b | - |
| 11-15 | dmr_001 (Wistman's Wood) | worth it | - | 166b | - |
| 11-15 | Veteran Lime (Linden) Tree | tree sent in | 114 chars, read it in the database | 0493 | - |
| 11-15 | 45EA816D-259F-4437-AC86-D3499F0269 | tree sent in | - | a926 | - |
| 11-15 | 2733129B-FA14-4FE4-9F30-7BA889CA94 | tree sent in | 1504 chars, read it in the database | 9e00 | - |
| 11-15 | cwh_001 (Coldwaltham Yew) | worth it | - | 90a6 | - |
| 11-15 | AAC60386-7889-4A79-831D-3B506278D4 | tree sent in | 1036 chars, read it in the database | a926 | open_question |
| 11-15 | The Master Oak | tree sent in | 201 chars, read it in the database | 6d34 | changed |
| 11-15 | BC20D71A-11EA-4180-AD6F-78EC11B24D | tree sent in | 23 chars, read it in the database | 4e29 | - |
| 11-15 | 6ACE68F9-6CA3-470C-9511-7E55975FB2 | tree sent in | - | 7159 | - |
| 11-15 | 1C15666F-2956-4FF6-A73D-EE3A44045C | tree sent in | 71 chars, read it in the database | 4ade | open_question |
| 11-15 | kef_001 (The Plane of Saint Gerasi | worth it | - | 7413 | - |
| 11-15 | 24FDCCB3-A454-4556-8169-2BAD2FB36A | tree sent in | - | 1388 | - |
| 11-15 | Ancient Lappa plane tree | tree sent in | 409 chars, read it in the database | e4c8 | - |
| 11-15 | kly_001 (The Muckross Abbey Yew) | worth it | - | 7413 | - |
| 11-15 | azo_005 (Giant Norfolk Island Pine | worth it | - | fc13 | - |
| 11-15 | Edinburgh | ambassador request | - | d892 | - |
| 11-15 | gnv_011 (The Bunya Pine of Villa G | worth it | - | fc13 | - |
| 11-15 | edi_021 (The Redford Wood Redwood) | worth it | - | f924 | - |
| 11-15 | The Redford Wood Redwood | correction sent in | 92 chars, read it in the database | f924 | - |
| 11-15 | edi_017 (Robert Louis Stevenson's  | worth it | - | f924 | - |
| 11-15 | The Old banyan at the office of Nh | tree sent in | 42 chars, read it in the database | da7c | open_question |
| 11-15 | Robert Louis Stevenson's Yew | correction sent in | 91 chars, read it in the database | f924 | - |
| 11-15 | - | Hello great app. I saw two magnifi | 203 chars | fc13 | changed |
| 11-15 | Deans Oak | tree sent in | 176 chars, read it in the database | 4c15 | holds |
| 11-15 | FFA15EB0-3701-46B0-9F53-84281B66B9 | tree sent in | - | f924 | - |
| 11-15 | E65D75DD-6D74-40DC-8840-A803969430 | tree sent in | 181 chars, read it in the database | ecda | - |
| 11-15 | E731E63C-5E9A-4490-BA4C-B47F30AA22 | tree sent in | - | f924 | - |
| 11-15 | 71F93157-AEF9-41A4-AF61-E1AD9755F9 | tree sent in | - | f924 | - |
| 11-15 | A tree I found | correction sent in | 89 chars, read it in the database | f924 | - |
| 11-15 | A giant sequoia | tree sent in | 101 chars, read it in the database | 7091 | open_question |
| 11-15 | ams_020 (The Leopold Maple of Wert | worth it | - | 05b3 | - |
| 11-15 | lon_041 (The St Mary Magdalene Pla | worth it | - | d0cf | - |
| 11-15 | lon_012 (The Amwell Street Fig) | worth it | - | d0cf | - |
| 11-15 | lon_016 (The Great Plane of Brunsw | worth it | - | d0cf | - |
| 11-15 | mcr_002 (Adam's Laburnum) | worth it | - | 5c93 | - |
| 11-15 | mcr_004 (The Variegated Green Ash) | worth it | - | 5c93 | - |
| 11-15 | tmb_002 (The Kyushaku-fuji of Byak | worth it | - | cd40 | - |
| 11-15 | Ancient eastern plane tree on Çına | tree sent in | 28 chars, read it in the database | c208 | - |
| 11-15 | London | ambassador request | - | c223 | - |
| 11-15 | pal_001 (The Ficus of Piazza Marin | worth it | - | b349 | - |
| 11-15 | Faux de Verzy | tree sent in | 68 chars, read it in the database | 3d7f | changed |
| 11-15 | The Zaandam wingnut | tree sent in | 224 chars, read it in the database | 9bad | changed |
| 11-15 | 60DAA5DB-07E5-48D7-BE3D-04C5684D70 | tree sent in | 774 chars, read it in the database | cd40 | - |
| 11-15 | 8F172F80-82AD-44E0-B6D5-394C56C136 | tree sent in | 269 chars, read it in the database | c1c3 | - |
| 11-15 | 0A0CBD5B-D255-4748-A4F8-13CAD39A04 | tree sent in | - | 3669 | - |
| 11-15 | C3BC464B-C6E2-4EF3-8E24-471E4E4E92 | tree sent in | - | c1c3 | - |
| 11-15 | frn_001 (Waverley Abbey Yew) | worth it | - | d177 | - |
| 11-15 | Old Knobbley | tree sent in | 19 chars, read it in the database | 63b2 | changed |
| 11-15 | F3F121F2-3FFA-4CC5-8A06-D06DFF70F7 | tree sent in | 226 chars, read it in the database | cd40 | - |
| 11-15 | sal_001 (The Hundred-Horse Chestnu | worth it | - | e8ea | - |
| 11-15 | mtn_001 (Stara Maslina (Old Olive  | worth it | - | a9fd | - |
| 11-15 | The Pear-Barked Beech | correction sent in | 91 chars, read it in the database | 4b6f | - |
| 11-15 | 34C8442D-A040-44EC-8182-989D8D9F1F | tree sent in | 49 chars, read it in the database | 7d11 | - |
| 11-15 | CFD86B34-8ABD-47E1-B301-A3501DFA4A | tree sent in | 21 chars, read it in the database | 25b4 | - |
| 11-15 | Tule Tree - cypress | tree sent in | 22 chars, read it in the database | 1fce | holds |
| 11-15 | lgy_001 (The Llangernyw Yew) | worth it | - | 4d80 | - |
| 11-15 | zur_002 (Alfred Escher's Giant Seq | worth it | - | 2494 | - |
| 11-15 | D28A8330-7F37-49A3-AF29-B9CF48BB31 | tree sent in | 89 chars, read it in the database | 43af | - |
| 11-15 | Giant sequoia in Geashill | correction sent in | 89 chars, read it in the database | 43af | - |
| 11-15 | F754324B-C7EA-4A2A-A366-5BF9C3F220 | tree sent in | 464 chars, read it in the database | 43af | - |
| 11-15 | Tree in Waitangi | tree sent in | 4 chars, read it in the database | 9014 | - |
| 11-15 | FBDFF0D4-6A3B-4BDC-9E85-3A5AF160D7 | tree sent in | 122 chars, read it in the database | 3471 | - |
| 11-15 | 3580EF91-02E7-45A1-BD3D-C8B5673E1A | tree sent in | 458 chars, read it in the database | 43af | - |
| 11-15 | Media | ambassador request | - | 3471 | - |
| 11-15 | The King of the Forest | correction sent in | 91 chars, read it in the database | fbfa | - |
| 11-15 | Wheatley Elm in Edinburgh | correction sent in | 88 chars, read it in the database | f924 | - |
| 11-15 | 45248B7C-02B4-4B01-BF83-0DD8B4C6FD | tree sent in | 31 chars, read it in the database | f924 | - |
| 11-15 | Wyndham's Oak | tree sent in | 50 chars, read it in the database | e061 | changed |
| 11-15 | The Great Oriental Plane Tree, Emm | tree sent in | 352 chars, read it in the database | 6594 | holds |
| 11-15 | The picture card perfect pines in  | tree sent in | 36 chars, read it in the database | d431 | changed |
| 11-15 | FDA250F8-3D69-4814-98FE-D2AA828E3A | tree sent in | 108 chars, read it in the database | fbfa | - |
| 11-15 | Mariam Dearit (also known as the M | tree sent in | 284 chars, read it in the database | e00d | - |
| 11-15 | sfo_001 (Uncle John's Tree) | worth it | - | 9646 | - |
| 11-15 | oxf_004 (The Pococke Plane) | worth it | - | 4817 | - |
| 11-15 | 3F2218EF-F368-4EC1-95B5-A1EA20E4B7 | tree sent in | - | 1ffd | - |
| 11-15 | 4DDFAF86-EDD9-4511-9136-381775BC10 | tree sent in | - | e1ef | - |
| 11-15 | - | I mistakenly added Tane Mahuta to  | - | e1ef | holds |
| 11-15 | for_001 (The Fortingall Yew) | worth it | - | e1ef | - |
| 11-15 | wai_001 (Tāne Mahuta) | worth it | - | e1ef | - |
| 11-15 | asb_001 (Ashbrittle Yew) | worth it | - | e1ef | - |
| 11-15 | 53809B69-6932-4E7A-8637-7DC2493811 | tree sent in | - | e1ef | - |
| 11-15 | Marton Oak | correction sent in | 89 chars, read it in the database | e1ef | - |
| 11-15 | 5EBFB2E9-B400-49F6-9383-68ED78F7A7 | tree sent in | - | 67f2 | - |
| 11-15 | Malmö | tree sent in | 79 chars, read it in the database | bb13 | - |
| 11-15 | The Brace Elm | correction sent in | 91 chars, read it in the database | 4546 | - |
| 11-15 | bhm_002 (The Brace Elm) | worth it | - | 4546 | - |
| 11-15 | 03075F0D-FBC2-4688-A90C-D8B21B4846 | tree sent in | - | 95e4 | - |
| 11-15 | 95787CB8-C8C0-479F-896C-364441D93E | tree sent in | - | 95e4 | - |
| 11-15 | 24E1A766-4FF4-4C15-8CAC-F080514DEC | correction sent in | 62 chars, read it in the database | 95e4 | - |
| 11-15 | mtf_001 (Great Plane of Mottisfont | worth it | - | c1c2 | - |
| 11-15 | cop_001 (The Mulberry of Proviantg | worth it | - | d91e | - |
| 11-15 | cop_001 (The Mulberry of Proviantg | vote undone | worth it | d91e | - |
| 11-15 | tul_001 (El Árbol del Tule) | worth it | - | d91e | - |
| 11-15 | tfe_001 (El Drago Milenario) | worth it | - | d91e | - |
| 11-15 | boi_002 (The Moved Giant Sequoia o | worth it | - | d91e | - |
| 11-15 | cop_005 (The Temple Tree of Landbo | worth it | - | d91e | - |
| 11-15 | cad_001 (The Ficus of Alameda Apod | worth it | - | 8f9e | - |
| 11-15 | muc_013 (The Fern-leaved Beech of  | worth it | - | b26f | - |
| 11-15 | 224B5518-E50E-4C58-A616-A79CDDC0DB | tree sent in | - | d91e | - |
| 11-15 | bhg_001 (The Cedars of the Konigsf | worth it | - | d91e | - |
| 11-15 | muc_007 (The Oak of the Dörfchen,  | worth it | - | b26f | - |
| 11-15 | B6C42A88-4F55-4E46-89F5-1ACDF57038 | tree sent in | - | 1825 | - |
| 11-15 | E229A150-5543-4042-992C-6F98125AFA | tree sent in | - | d91e | - |
| 11-15 | bai_001 (The Gomero de la Recoleta | worth it | - | d91e | - |
| 11-15 | muc_014 (The Weeping Beech of the  | worth it | - | b26f | - |
| 11-15 | vld_001 (Elku Linden of Valdemārpi | worth it | - | 2aa4 | - |
| 11-15 | - | In 2002, UK charity The Tree Counc | - | 2c2d | - |
| 11-15 | yor_002 (The Cut-Leaved Hornbeam) | worth it | - | 3c01 | - |
| 11-15 | dre_005 (The Kaditzer Linde) | worth it | - | c05d | - |
| 11-15 | dre_005 (The Kaditzer Linde) | vote undone | worth it | c05d | - |
| 11-15 | dre_005 (The Kaditzer Linde) | worth it | - | c05d | - |
| 11-15 | FE8FC7E4-9E16-48B5-96C0-E8C2AF7A02 | tree sent in | - | 7009 | - |
| 11-15 | Dawn Redwood in Toronto | correction sent in | 89 chars, read it in the database | 7009 | - |
| 11-15 | pal_003 (The Ficus of the Orto Bot | worth it | - | 3fcf | - |
| 11-15 | Dawn Redwood in Toronto | correction sent in | 89 chars, read it in the database | 7009 | - |
| 11-15 | war_001 (Dab Mieszko I (King Miesz | worth it | - | c922 | - |
| 11-15 | sev_044 (The Cardón of the Expo) | worth it | - | c922 | - |
| 11-15 | The Monterey Pine at the Gates | correction sent in | 91 chars, read it in the database | 547d | - |
| 11-15 | war_007 (King Jan's Linden) | worth it | - | c922 | - |
| 11-15 | Oak tree, Quercus Robur. | tree sent in | 51 chars, read it in the database | 6d78 | - |
| 11-15 | Giant Tree | correction sent in | 90 chars, read it in the database | e1ef | - |
| 11-15 | ED5BD210-4A52-4FE2-90A8-F121559EF7 | tree sent in | 30 chars, read it in the database | e1ef | - |
| 11-15 | The Husalle Lindens | correction sent in | 29 chars, read it in the database | d91e | - |
| 11-15 | 64E94530-A55E-4174-B649-85EDA345DB | tree sent in | - | e1ef | - |
| 11-15 | Black Mulberry | tree sent in | 70 chars, read it in the database | 9b0b | - |
| 11-15 | 7547CFA4-55B8-4F9E-ACAB-06372DF4A3 | tree sent in | 378 chars, read it in the database | a4b2 | - |
| 11-15 | A0F1F73D-FF2F-4A30-B958-2BB1ACF20A | tree sent in | - | 9f7b | - |
| 11-15 | ank_001 (The Ankerwycke Yew) | worth it | - | a4b2 | - |
| 11-15 | Common Fig | correction sent in | 89 chars, read it in the database | 9f7b | - |
| 11-15 | cwh_001 (Coldwaltham Yew) | report | something else | 19a7 | - |
| 11-15 | cwh_001 (Coldwaltham Yew) | report detail | 221 chars | 19a7 | - |
| 11-15 | cwh_001 (Coldwaltham Yew) | report | something else | 19a7 | - |
| 11-15 | B27E5E37-779C-4373-872E-6DA86D1C30 | tree sent in | 71 chars, read it in the database | 9f7b | - |
| 11-15 | cwh_001 (Coldwaltham Yew) | report detail | 146 chars | 19a7 | - |
| 11-15 | Cedar of Lebanon | tree sent in | 27 chars, read it in the database | 02da | - |
| 11-15 | Douglas fir | tree sent in | 110 chars, read it in the database | 02da | - |
| 11-15 | FC04D59E-BB37-4B00-B069-2A4D28EBCF | tree sent in | - | 19a7 | - |
| 11-15 | Metrosideros (Metrosideros excelsu | tree sent in | 117 chars, read it in the database | 4bcd | - |
| 11-15 | E1144BEA-FD53-4CC6-A71F-D523C763F6 | tree sent in | - | 6051 | - |
| 11-15 | FBCB3C91-41F0-48D9-B573-F37E63AD01 | tree sent in | - | 6051 | - |
| 11-15 | 1306C000-ED52-40F3-AD73-C6F414C5DB | tree sent in | 35 chars, read it in the database | 4136 | - |
| 11-15 | nol_005 (The Suicide Oak) | worth it | - | dc5b | - |
| 11-15 | 8E99752E-A501-45C2-8247-AB981C9604 | tree sent in | 29 chars, read it in the database | 88eb | - |
| 11-15 | A tree near Edinburgh | correction sent in | 90 chars, read it in the database | ac28 | - |
| 11-15 | 460C96B9-89E2-41AC-A829-EC911BE11E | tree sent in | 97 chars, read it in the database | ac28 | - |
| 11-15 | bri_016 (The Bundle-planted Sessil | worth it | - | 2ce8 | - |
| 11-15 | bri_016 (The Bundle-planted Sessil | vote undone | worth it | 2ce8 | - |
| 11-15 | bri_016 (The Bundle-planted Sessil | worth it | - | 2ce8 | - |
| 11-15 | Southern Live Oak | correction sent in | 90 chars, read it in the database | 8726 | - |
| 11-15 | 0ADAC3F1-3C3F-4DA8-BB6E-A88BC759AC | tree sent in | - | 8726 | - |
| 11-15 | A6D28625-B0FB-469F-8653-84FF735DAD | tree sent in | - | 6ec2 | - |
| 11-15 | BF30B7A2-FE72-4E2F-BEEB-7757E1E917 | tree sent in | 18 chars, read it in the database | 6ec2 | - |
| 11-15 | 2186BB95-6054-4154-B6D9-C75CB1FCA1 | tree sent in | - | 6ec2 | - |
| 11-15 | C7DCA666-5183-4987-B585-0F10639B5C | tree sent in | - | 6ec2 | - |
| 11-15 | ED0A19ED-93E1-42E9-8A50-FCAA0420BD | tree sent in | 279 chars, read it in the database | 7d27 | - |
| 11-15 | hil_001 (The Oriental Plane of Lan | worth it | - | ed99 | - |
| 11-15 | Arbour Oak | tree sent in | 564 chars, read it in the database | 30b8 | - |
| 11-15 | scz_002 (The Fremont Tree) | worth it | - | ea37 | - |
| 11-15 | wai_002 (Te Matua Ngahere) | worth it | - | 74c9 | - |
| 11-15 | Auckland | ambassador request | - | 74c9 | - |
| 11-15 | rkm_001 (Rumskullaeken (the Kvill  | worth it | - | 59bc | - |
| 11-15 | ank_001 (The Ankerwycke Yew) | not worth it | - | 9b3c | - |
| 11-15 | B2B14047-08E5-447F-A435-3A4F137809 | tree sent in | 144 chars, read it in the database | 59bc | - |
| 11-15 | 0B0D29FA-BC94-48A7-8014-4D103452C1 | tree sent in | 114 chars, read it in the database | 9b3c | - |
| 11-15 | 2AB16C0E-AEAA-401D-9120-B884E8C85E | tree sent in | - | 9b3c | - |
| 11-15 | D8EDD734-1E64-45CB-AFE4-47A85A4D80 | tree sent in | - | 9b3c | - |
| 11-15 | - | I was wondering if we could submit | - | acda | - |
| 11-15 | Oliveira de Mouchão, oldest olive  | tree sent in | 226 chars, read it in the database | 05fb | - |
| 11-15 | kly_001 (The Muckross Abbey Yew) | worth it | - | 27c8 | - |
| 11-15 | kly_001 (The Muckross Abbey Yew) | vote undone | worth it | 27c8 | - |
| 11-15 | akw_002 (Ardkinglas Silver Fir, th | worth it | - | 19ce | - |
| 11-15 | 4B1E4321-165C-4742-B645-6EC065F309 | tree sent in | 327 chars, read it in the database | 7938 | - |
| 11-15 | akw_001 (Ardkinglas Grand Fir) | worth it | - | 19ce | - |
| 11-15 | 2EC0418A-AC10-4C61-9DAF-A287193AE9 | tree sent in | 217 chars, read it in the database | af61 | - |
| 11-15 | F1FAA5F9-5750-4863-8920-2CE31BF5D0 | tree sent in | - | bf55 | - |
| 11-15 | D291140E-1665-4036-A4CB-E826D8FF63 | tree sent in | - | bf55 | - |
| 11-15 | A9F9EB8D-F3C2-4146-94A2-AFE4FE3291 | tree sent in | - | bf55 | - |
| 11-15 | B59C4873-FD0A-4A92-A0D0-08074938E8 | correction sent in | 219 chars, read it in the database | bf55 | - |
| 11-15 | Yang Na of the City Pillar, Wat Ch | correction sent in | 169 chars, read it in the database | bf55 | - |
| 11-15 | 20D04DFD-E398-4533-A42D-B1385D2A6F | tree sent in | - | bf55 | - |
| 11-15 | bos_013 (Endicott Pear Tree) | worth it | - | 7aae | - |
| 11-15 | lnt_001 (The Linton Yew) | worth it | - | a4b2 | - |
| 11-15 | snd_001 (The Sunderland Buttonball | worth it | - | 7aae | - |
| 11-15 | mob_003 (Jackson's Oak) | worth it | - | 7aae | - |
| 11-15 | C476F81B-3871-4273-9E0A-F4F21AE2B5 | tree sent in | - | ceea | - |
| 11-15 | plm_001 (S'Olivera de Cort) | worth it | - | 7aae | - |
| 11-15 | 1215C9AD-3B03-438C-A3C4-74F631633F | tree sent in | - | ceea | - |
| 11-15 | Il cipresso calvo di Villa Smerald | tree sent in | 621 chars, read it in the database | 7e0c | - |
| 11-15 | boz_001 (The Linden of Linn) | worth it | - | b593 | - |
| 11-15 | 340D13E5-D031-448E-9595-DAFF201BBB | tree sent in | - | fc4b | - |
| 11-15 | A7751610-E6BC-4DC1-96F6-63005EF4F2 | tree sent in | - | 7050 | - |
| 11-15 | Quercia di Molinazzo | tree sent in | 1180 chars, read it in the database | 7e0c | - |
| 11-15 | 7FF97B69-76B5-4905-80C2-7C7E901C31 | tree sent in | - | 7050 | - |
| 11-15 | F249D2AC-4E34-4BDF-9919-626A212DE1 | tree sent in | 221 chars, read it in the database | e1ef | - |
| 11-15 | 24C1E280-6404-4056-AF86-C3AC625D6E | tree sent in | 654 chars, read it in the database | 8ced | - |
| 11-15 | it only works on Iphone | correction sent in | 39 chars, read it in the database | 34ff | - |
| 11-15 | European Yew near Wilmington | correction sent in | 90 chars, read it in the database | 7050 | - |
| 11-15 | Pedunculate Oak | correction sent in | 89 chars, read it in the database | 7050 | - |
| 11-15 | 62A9482B-A105-4572-B6CA-15DF5C7392 | tree sent in | - | 934c | - |
| 11-15 | Melbourne | ambassador request | - | c873 | - |
| 11-15 | 51D98942-7DBA-4D70-9DDD-17263958DD | tree sent in | - | 3e41 | - |
| 11-15 | C7962FE1-14DB-407A-B62F-CFA6175806 | tree sent in | 17 chars, read it in the database | 3e41 | - |
| 11-15 | FF8F7EAC-05BB-4474-A1BF-B44629A370 | tree sent in | - | 3e41 | - |
| 11-16 | kyw_003 (The Kapok Tree) | worth it | - | a5cf | - |
| 11-16 | Toronto | ambassador request | - | e54e | - |
| 11-16 | 3DFEEF4F-6A2A-474A-ABAA-B0594C7410 | tree sent in | - | 3fdc | - |
| 11-16 | F81EAEAA-49A5-464A-B5FD-18CAD1C749 | tree sent in | - | 1825 | - |
| 11-16 | 7B8B90C6-507C-46CC-9FE8-1366F7A953 | tree sent in | - | 1825 | - |
| 11-16 | E34C7308-6FCC-45CF-AFCA-1A9CDBF20D | tree sent in | - | 1825 | - |
| 11-16 | CB8B4EBE-74CA-4641-A139-533B41A7E3 | tree sent in | - | 1825 | - |
| 11-16 | 2C03D56E-6192-4FAE-9A95-94E41B042E | tree sent in | - | 1825 | - |
| 11-16 | 47730065-758C-46DC-B4BA-E0E3E353C3 | tree sent in | 37 chars, read it in the database | 6f92 | - |
| 11-16 | hou_002 (The Old Pecan Tree) | worth it | - | ae40 | - |
| 11-16 | hou_002 (The Old Pecan Tree) | vote undone | worth it | ae40 | - |
| 11-16 | hou_002 (The Old Pecan Tree) | worth it | - | ae40 | - |
| 11-16 | hou_009 (The Becks Prime Augusta L | worth it | - | ae40 | - |
| 11-16 | 9CDC79F8-530A-48D5-B9EA-C51D1F28D5 | tree sent in | 67 chars, read it in the database | de08 | - |
| 11-16 | 0269D848-F4E2-40DB-9157-8F6F951A34 | tree sent in | - | 6f92 | - |
| 11-16 | Boab | correction sent in | 89 chars, read it in the database | de08 | - |
| 11-16 | 6BB3D492-EA79-4B08-8F63-A66610632B | tree sent in | - | 24da | - |
| 11-16 | DE83AEF2-D85E-4D38-B4EF-73E6365D25 | tree sent in | 1154 chars, read it in the database | de08 | - |
| 11-16 | Boab | correction sent in | 89 chars, read it in the database | de08 | - |
| 11-16 | Cat Island Bald Cypress | tree sent in | 118 chars, read it in the database | 360c | - |
| 11-16 | 42A31D57-D883-4E4E-9967-EC876A4C40 | tree sent in | - | cc87 | - |
| 11-16 | Ancient totara tree | tree sent in | 59 chars, read it in the database | 250e | - |
| 11-16 | 92FAC7A0-332E-4B6B-8D54-463B3E592C | tree sent in | - | 9b3c | - |
| 11-16 | elh_001 (Elleholmseken (The Oak of | worth it | - | 59bc | - |

- 230 rows from 119 accounts.

**App Store downloads** (Apple's own count, not PostHog)

| Day | Downloads |
|---|---:|
| 2026-11-08 | 3 |
| 2026-11-09 | 2 |
| 2026-11-10 | 3 |
| 2026-11-11 | 1 |
| 2026-11-12 | 2 |
| 2026-11-13 | 2 |
| 2026-11-14 | 1 |
| **7 days** | **14** |
- First-time downloads only, which is what App Store Connect's Trends screen counts; redownloads and updates are not in this table.

**Where the downloads came from** (7 days, Apple's attribution)

| Came from | Via | Downloads |
|---|---|---:|
| App Store search | - | 9 |
| Web referrer | - | 5 |
| **window** | | **14** |
- Countries: US (9); GB (2); AU (1); JP (1); NO (1)
- Apple's own source split, first-time downloads only. "Web referrer" with our own domain is the site's app page; "App Store search" is somebody who typed into the store. "Unavailable" is Apple's word for a source it could not attribute.

**Bing's index** (pages crawled and in index, Bing Webmaster Tools)

| Day | Pages crawled | Pages in index |
|---|---:|---:|
| 11-07 | 209 | 4334 |
| 11-08 | 194 | 4335 |
| 11-09 | 369 | 4335 |
| 11-10 | 263 | 4404 |
| 11-11 | 269 | 4404 |
| 11-12 | 229 | 4453 |
| 11-13 | 217 | 4454 |
- In index the week before: 4335.

**Who they are** (full cut, Mondays)
Audience, 28 days of search (339 clicks, 6510 impressions):
- Countries: gbr c85/i542; usa c38/i1193; aus c23/i240; fra c21/i225; esp c20/i551
- Devices: MOBILE c247/i3724; DESKTOP c79/i2685; TABLET c13/i101
- Landing pages: / c201/i431; /de c4/i49; /seville c4/i97; /united-states/maryland c4/i32; /app c3/i43
- Search language (top 100 named queries, crude match, most clicks are in queries Google withholds): English 56q c155/i328; unclassified 31q c4/i40; German 5q c1/i30; Spanish 5q c0/i28; Italian 2q c0/i2; French 1q c0/i1

**Google Analytics** (last 7 days, visitors who accepted cookies)

| Day | People | New | Returning | Visits | Pageviews | Engaged visits |
|---|---:|---:|---:|---:|---:|---:|
| 11-09 | 9 | 8 | 1 | 14 | 53 | 7 |
| 11-10 | 11 | 7 | 4 | 18 | 36 | 8 |
| 11-12 | 3 | 3 | 0 | 4 | 4 | 2 |
| 11-13 | 5 | 5 | 0 | 5 | 24 | 5 |
| 11-14 | 3 | 2 | 1 | 9 | 14 | 2 |
| 11-15 | 1797 | 1793 | 4 | 2179 | 6031 | 1483 |
| **window** | | **1818** | | **2229** | **6162** | **1507** |
- People per day are not summed: one person on two days is one person, and GA counts them once per day.
- Coming back (28 days): 178 returning against 2022 new, 8% of the people GA saw.

| Page | Pageviews | People |
|---|---:|---:|
| / | 1757 | 1289 |
| /explore | 827 | 555 |
| /london | 165 | 110 |
| /countries | 139 | 94 |
| /cities | 112 | 85 |
| /united-kingdom | 96 | 70 |
| /contribute | 89 | 53 |
| /bristol | 46 | 29 |
| /edinburgh | 35 | 24 |
| /amsterdam | 33 | 11 |

| Came from | Visits | People |
|---|---:|---:|
| (direct) / (none) | 1251 | 1015 |
| theguardian.com / referral | 827 | 708 |
| (not set) / (not set) | 300 | 297 |
| google / organic | 55 | 38 |
| m.facebook.com / referral | 31 | 27 |
| facebook.com / referral | 22 | 22 |
| accounts.google.com / referral | 8 | 3 |
| share / app | 6 | 4 |
- GA sees only visitors who pressed Accept on the cookie bar; read it as a sample.

Backlinks (watched pages):
| Site | Links to | rel | First seen |
|---|---|---|---|
| getlisbon.com | /lisbon | followed | 2026-09-08 |
| getlisbon.com | /pt/lisbon | followed | 2026-09-08 |
| www.baumkunde.de | /copenhagen | followed | 2026-09-26 |
| www.baumkunde.de | /rogalin/russ-oak | followed | 2026-09-26 |
| wilder.pt | / | followed | 2026-10-24 |
5 linking page(s), 5 followed. Checked by fetching the page: a link with rel="noreferrer" never appears in the referrer table, so these two lines measure different things and neither replaces the other. Unknown links stay a manual read of Search Console's Links report. This run read 8 of 12 fetched (4 unreachable), out of 28 watched pages.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-15T06:56 | 20.5 | 3 | 18 | 4 | Bamberg +2, Buffalo +1 |
| 11-15T08:44 | 11.9 | 2 | 9 | 0 | Adelaide +1, Moss Vale +1, Belfast, Coldwaltham, +3 more |
| 11-15T14:59 | 10.4 | 2 | 8 | 0 | Grazalema +1, Meycauayan +1, Buenos Aires, Dresden, +9 more |
| 11-15T16:45 | 7.4 | 2 | 10 | 2 | Linton Herefordshire +1, Manaccan +1, Copenhagen, Warsaw |
| 11-15T20:19 | 9.5 | 9 | 7 | 0 | La Tene +4, Carmarthen +1, Colchester +1, Elleholm +1, +10 more |
| 11-15T22:24 | 8.2 | 5 | 8 | 0 | Bowthorpe +1, Crowhurst +1, Doveridge +1, London +1, +12 more |
| 11-16T04:21 | 3.6 | 0 | 6 | 0 | Borrowdale, Charleston, Houston, Key West, +2 more |
| **7 runs** | **72** | **23** | **66** | | |

- 1 of 7 produced no trees; 2 to 4 commands refused per run; last build that went live: 1h ago.

**What they made**

- Reader photographs: four trees get their first photograph (Houston x2, Key West, Bong), four strip verdicts; Houston story colon fixed
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- Five reader-found trees live (app first): Bowthorpe Oak, Crowhurst Yew, Doveridge Yew, Greenwich Park chestnut, Methuselah redwood; verdicts and leads
- Reader photographs: 6 live on photo-less trees, 7 kept beside existing, 7 taken out of the strip (people in frame, wrong tree), 3 rejected or held; verdicts written
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- Settings: load the image downsizer, so changing a profile photo no longer throws atDownsize is not a function
- Nine reader-found trees live (app first): Wantisden pollard oaks, Elleholmseken, Maidstone plane, Colchester oak, Carmarthen ginkgo, four more at Prefargier; verdicts, leads and log
- Reader photographs: 5 live on photo-less trees, 3 added beside existing, 5 held (plane tree sent as Ankerwycke Yew, a group portrait); verdicts written
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed

**Reader photographs in a strip, live first, not yet looked at** (32)

| Day | Tree | Where | Undo |
|---|---|---|---|
| 11-15 | The Plane Trees of the Circus | Bath | `sightings_publish.py --unstrip 3b39d16a-da7e-41df-b566-3345170189b9` |
| 11-16 | The Borrowdale Yews (the Fraternal Four) | Borrowdale | `sightings_publish.py --unstrip b24f5c1e-b9c6-4f5a-af2e-c761fa60e614` |
| 11-15 | Endicott Pear Tree | Boston | `sightings_publish.py --unstrip b724f1db-2429-4905-a291-fa1bf50132cd` |
| 11-15 | The Gomero de la Recoleta | Buenos Aires | `sightings_publish.py --unstrip 3325a9bc-9642-4364-8475-8f89d62e834d` |
| 11-16 | The Angel Oak | Charleston | `sightings_publish.py --unstrip 27b65062-4209-44fa-ad20-a179dd1e974f` |
| 11-15 | The Fern-leaved Beech of the National Gallery | Copenhagen | `sightings_publish.py --unstrip 40d6b9ff-509f-488b-9e02-4f507e7f889a` |
| 11-15 | The Olive of the Orange Courtyard | Cordoba | `sightings_publish.py --unstrip 79e27623-4f57-4e8b-93ed-5809952ad465` |
| 11-15 | The Orange Courtyard of the Mezquita | Cordoba | `sightings_publish.py --unstrip 505b0039-de16-410f-817e-55e31e93c41a` |
| 11-15 | The Kaditzer Linde | Dresden | `sightings_publish.py --unstrip 90aa5d92-64b3-439f-b2b3-a56cc8b41136` |
| 11-15 | The Weeping Beech of Helfenberg Park | Dresden | `sightings_publish.py --unstrip cfcad2b9-4ce3-49f8-bf53-a03f156c8794` |
| 11-15 | The Argyle Street Ash | Glasgow | `sightings_publish.py --unstrip c62d8c77-f078-478f-babf-1c12d2426ef4` |
| 11-15 | The Fulham Palace Oak | London | `sightings_publish.py --unstrip d8994b07-93c9-41a0-ae09-ab417f322b93` |
| 11-15 | Barney the Plane | London | `sightings_publish.py --unstrip 6f2cee0c-369d-4da5-a2e3-6e08f138a29f` |
| 11-15 | The Ravenscourt Park Baobab Plane | London | `sightings_publish.py --unstrip eb811a74-663f-476f-bf0f-349d058508e0` |
| 11-15 | The Bromley Oak | London | `sightings_publish.py --unstrip cc260294-0437-4efb-8c0f-5bf73fb0adf3` |
| 11-15 | The Bromley Oak | London | `sightings_publish.py --unstrip 4fa5c2bb-2a1f-4c07-9e87-d7fd9b008800` |
| 11-16 | Ahuehuete de Parque Espana | Mexico City | `sightings_publish.py --unstrip 3693bdc5-cbb5-4ff1-909e-745a397aaf76` |
| 11-16 | Ahuehuete de Parque Espana | Mexico City | `sightings_publish.py --unstrip 9d72943f-aba5-4ab8-a8da-ee9c3a21a1cf` |
| 11-15 | Jackson's Oak | Mobile | `sightings_publish.py --unstrip bcde1019-cccf-445a-a2ab-81b2bdbb8809` |
| 11-15 | The Copper Beech of the Badenburg | Munich | `sightings_publish.py --unstrip a1e5696d-07f6-4ad8-b33d-af8a195ee53a` |
| 11-15 | The Leaning Lime of the Badenburger See | Munich | `sightings_publish.py --unstrip f9aef0f0-825b-43a6-80c6-bdae5f77ce0d` |
| 11-15 | The Leaning Lime of the Badenburger See | Munich | `sightings_publish.py --unstrip 31f72d8f-0bcc-4df5-88a8-46c14bbbb5cf` |
| 11-15 | The Great Cedar of Kasuga Taisha | Nara | `sightings_publish.py --unstrip 221f1245-c4b5-4b97-a777-879f9f8bd9e7` |
| 11-15 | The Ficus of the Orto Botanico | Palermo | `sightings_publish.py --unstrip 61ca336b-c1eb-4f2a-8709-bcb29e63a2c6` |
| 11-15 | S'Olivera de Cort | Palma de Mallorca | `sightings_publish.py --unstrip 513c935b-b7e0-4b76-93c2-6a8223d8274b` |
| 11-15 | The Cardón of the Expo | Seville | `sightings_publish.py --unstrip 770b668b-0152-47a4-9822-70e04183b599` |
| 11-15 | The Sunderland Buttonball Tree | Sunderland, Massachusetts | `sightings_publish.py --unstrip 9689a5aa-c566-41e5-a674-f26dd189e7cc` |
| 11-15 | El Drago Milenario | Tenerife | `sightings_publish.py --unstrip d1f0b3c4-247f-4f5b-8b34-f2e44c765fef` |
| 11-15 | Te Matua Ngahere | Waipoua Forest | `sightings_publish.py --unstrip ab926a56-7355-4115-aaeb-20715143d5c0` |
| 11-15 | Dab Mieszko I (King Mieszko I's Oak) | Warsaw | `sightings_publish.py --unstrip 5b8c4e7a-86a1-4b3f-a434-83e7a0945553` |
| 11-15 | The Cut-Leaved Hornbeam | York | `sightings_publish.py --unstrip b24fa509-4aa6-42fc-9fda-04282a20e481` |
| 11-15 | The Pear-Barked Beech | York | `sightings_publish.py --unstrip 56342639-17a9-44b9-a876-bfe3cfa658dc` |

Machine: 8 chain attempts yesterday, 8 got real work time (~126 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c185/i332); /switzerland (c3/i13); /seville (c2/i51); /de (c2/i19); /app (c2/i18)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i5, p3)
    - 'alte bäume karte' (i3, p7)
    - 'acient tree' (i2, p14)
    - 'angeloak' (i2, p79)
    - 'ahornbäume in der nähe' (i1, p7)
    - 'alberi di roma' (i1, p1)
    - 'alter' (i1, p2)
    - 'arbol tipico canario' (i1, p42)

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 142 | 16 | 48 | 0.34 | 1 |
| Not yet rich | 174 | 20 | 210 | 1.21 | 0 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| fortingall | 0 | 144 | 0.0% | 10.7 | 2.2% | fortingall yew (i117, p11) |
| lisbon | 1 | 61 | 1.6% | 6.4 | 4.6% | historic giant plant of lisbon (i1, p12) |
| seville | 2 | 57 | 3.5% | 5.1 | 6.8% | sevilla (i1, p1) |
| berlin | 2 | 41 | 4.9% | 6.0 | 5.1% | berlin trees (i2, p5) |
| fulufjallet | 0 | 41 | 0.0% | 9.4 | 2.8% | old tjikko (i22, p11) |
| olympic-national-park | 0 | 32 | 0.0% | 13.8 | 1.4% | duncan cedar (i14, p10) |
| tokyo | 0 | 32 | 0.0% | 5.4 | 6.2% | ginkgo sperm (i2, p11) |
| malaga | 0 | 29 | 0.0% | 20.4 | 0.8% | árboles históricos de málaga (i5, p87) |
| singapore | 0 | 29 | 0.0% | 9.0 | 3.0% | earpod tree (i3, p5) |
| munich | 1 | 26 | 3.8% | 5.3 | 6.4% | ältester baum münchen (i1, p8) |
| south-korea | 0 | 25 | 0.0% | 14.6 | 1.3% | ginkgo tree korea (i2, p5) |
| paris | 1 | 24 | 4.2% | 5.9 | 5.2% | - |
| kyoto | 1 | 24 | 4.2% | 4.0 | 8.1% | ginkgo tree kyoto (i1, p1) |
| palermo | 0 | 24 | 0.0% | 9.0 | 3.0% | palermo tree (i1, p9) |
| tenerife | 0 | 23 | 0.0% | 27.6 | 0.5% | el drago milenario (i2, p10) |
| seoul | 1 | 22 | 4.5% | 8.3 | 3.3% | - |
| monterey | 0 | 22 | 0.0% | 53.1 | 0.4% | lone cypress monterey (i5, p64) |
| copenhagen | 2 | 21 | 9.5% | 11.0 | 2.2% | copenhagen trees (i3, p39) |
| amsterdam | 0 | 21 | 0.0% | 8.7 | 3.1% | lomanstraat (i2, p19) |
| united-states | 2 | 20 | 10.0% | 17.4 | 1.0% | oldest tree in oregon (i4, p10) |
| london | 2 | 20 | 10.0% | 15.1 | 1.2% | barney london bridge is falling down (i1, p69) |
| taiwan | 0 | 18 | 0.0% | 11.1 | 2.1% | oldest tree in taiwan (i3, p5) |
| sequoia-national-park | 0 | 18 | 0.0% | 24.1 | 0.6% | washington tree (i9, p20) |
| reykjavik | 0 | 18 | 0.0% | 5.8 | 5.3% | - |
| venice | 2 | 16 | 12.5% | 4.0 | 8.0% | - |
| austin | 0 | 16 | 0.0% | 17.2 | 1.0% | oldest tree in austin (i2, p12) |
| barcelona | 0 | 16 | 0.0% | 9.8 | 2.6% | - |
| germany | 1 | 15 | 6.7% | 6.1 | 4.9% | - |
| san-francisco | 0 | 15 | 0.0% | 4.9 | 7.1% | old tree near me (i1, p4) |
| kagoshima | 0 | 15 | 0.0% | 10.4 | 2.4% | oldest camphor tree (i1, p7) |
| brisbane | 0 | 15 | 0.0% | 16.5 | 1.1% | banyan tree (i3, p10) |
| oahu | 0 | 14 | 0.0% | 9.4 | 2.8% | hitachi tree (i2, p10) |
| los-angeles | 0 | 14 | 0.0% | 7.8 | 3.6% | moreton bay fig tree beverly hills (i1, p9) |
| milan | 0 | 14 | 0.0% | 5.4 | 6.3% | - |
| prague | 0 | 14 | 0.0% | 4.9 | 7.1% | - |
| switzerland | 3 | 13 | 23.1% | 7.7 | 3.7% | - |
| porto | 1 | 13 | 7.7% | 2.2 | 14.1% | - |
| edinburgh | 0 | 13 | 0.0% | 6.8 | 4.2% | - |
| cambridge | 0 | 13 | 0.0% | 30.4 | 0.4% | isaac newton tree (i2, p22) |
| athens | 0 | 13 | 0.0% | 5.5 | 6.1% | - |
| dublin | 1 | 12 | 8.3% | 4.3 | 7.7% | - |
| nara | 1 | 12 | 8.3% | 5.8 | 5.5% | - |
| charleston | 0 | 12 | 0.0% | 24.3 | 0.6% | angeloak (i2, p79) |
| kanazawa | 0 | 12 | 0.0% | 6.3 | 4.7% | - |
| chishang | 0 | 11 | 0.0% | 6.5 | 4.5% | takeshi kaneshiro tree (i6, p7) |
| fukuoka | 0 | 11 | 0.0% | 7.4 | 3.8% | dazaifu tenmangu (i1, p1) |
| seattle | 0 | 11 | 0.0% | 9.0 | 3.0% | oldest tree in seattle (i1, p10) |
| netherlands | 1 | 10 | 10.0% | 9.0 | 3.0% | dutch trees (i1, p39) |
| bristol | 0 | 10 | 0.0% | 6.0 | 5.0% | - |
| poland | 0 | 10 | 0.0% | 7.7 | 3.6% | trees in poland (i1, p8) |
| segovia | 0 | 10 | 0.0% | 38.1 | 0.4% | - |
| madrid | 0 | 10 | 0.0% | 6.5 | 4.5% | - |

- Plus 211 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: bath, rome, new-york, brussels, vienna, alicante, cadiz, pamplona.

## 2026-11-14 (previous UTC day)

**Today: 2 accounts were opened yesterday (64 accounts in all).**

**North star: 15 people have uploaded a tree or photo of their own (+3 this week); 4 of them did it on more than one day (+0).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 35 | 52 |
| ... of which from search | every search engine | 15 | 22 |
| ... from Google | Google's recovery | 10 | 13 |
| ... from Bing | Bing | 1 | 3 |
| Website visitors who came back | people who stay | 9 | 12 |
| App downloads (first-time) | people | 17 | 20 |
| New accounts | people | 4 | 11 |
| Phones back within 30 days | people who stay | 5 of 17 | 4 of 6 |
| Trees saved to Want to go | intent | 0 | 4 |
| Trees collected | goal 1: stood at a tree | 0 | 7 |
| Readers' contributions | data: trees, photos, corrections, votes | 4 | 8 |
| Shares (app and web) | word of mouth, since 10-30 | 1 | 3 |
| Visits from a shared link | what sharing brings | 0 | 2 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web orange, iOS red, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | green | red: iOS build failure on main | grey: no checks wired yet |
| Live | orange: 1 new error type(s), first "TypeError: undefined is not an object (evaluating 'window.et" in inline | green | grey: no checks wired yet |

**Plus question**: no answers yet.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-08 | 11-09 | 11-10 | 11-11 | 11-12 | 11-13 | 11-14 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 10 | 9 | 11 | 0 | 3 | 5 | 3 | **41** |
| New accounts | 0 | 0 | 1 | 0 | 1 | 0 | 2 | **4** |
| Saves | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Android waitlist | 0 | 0 | 1 | 0 | 0 | 0 | 0 | **1** |
| App downloads | 3 | 2 | 3 | 1 | 2 | 2 | – | **13** |
| App phones | 7 | 7 | 5 | 6 | 5 | 5 | 8 | **32** |
| Trees opened in the app | 27 | 5 | 14 | 3 | 3 | 4 | 18 | **74** |
| Trees collected | 0 | 0 | 0 | 0 | 0 | 0 | 3 | **3** |
| Trees sent | 0 | 0 | 0 | 0 | 0 | 1 | 0 | **1** |
| Feedback | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Ambassador asks | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Website photos | 0 | 0 | 0 | 1 | 0 | 0 | 0 | **1** |
| iPhone photos | 0 | 0 | 0 | 0 | 0 | 0 | 3 | **3** |
| Android photos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Tree notes | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **1** |
| App Store reviews | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.

**Trees readers sent, for you to inspect:** none waiting. Every tree a stranger sent has your answer.

**Waiting for you** (what the runs left for you since 2026-11-14)

- 246 email addresses ready to mail (archive 0, nature 9, guide 8, press 135, source 58, council 16, society 7, tourism 5, other 5, garden 3); **the night run found no new contacts in two days**
- the run's token cannot dispatch deploy.yml (HTTP 403), so the fix goes live on the next push-triggered or scheduled build.
- the daily task "publish-held-trees-daily" can be switched off under Scheduled.

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-14 | A | The Taşlı Çınar | Istanbul | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/istanbul/tasl-cnar) |
| 11-14 | A | The Gülhane London Plane | Istanbul | a reader's photograph, published | [live](https://ancienttrees.app/istanbul/gulhane-london-plane) |
| 11-14 | A | The Gülhane Nettle Tree | Istanbul | a reader's photograph, published | [live](https://ancienttrees.app/istanbul/gulhane-nettle-tree) |
- All from one reader (reader A 3).

**Searched yesterday:** bri.

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 11-05 | 1 | 23 | 4.3% | 34.1 |
| 11-06 | 1 | 35 | 2.9% | 36.6 |
| 11-07 | 2 | 34 | 5.9% | 38.3 |
| 11-08 | 25 | 1013 | 2.5% | 9.1 |
| 11-09 | 28 | 1177 | 2.4% | 8.9 |
| 11-10 | 8 | 196 | 4.1% | 13.0 |
| 11-11 | 1 | 16 | 6.2% | 22.1 |
| 11-12 | 1 | 28 | 3.6% | 31.4 |
| 11-13 | 1 | 32 | 3.1% | 55.0 |
| 11-14 *partial* | 0 | 38 | 0.0% | 58.7 |
| **window** | **68** | **2592** | **2.6%** | |
- Top queries (10d): ancient trees app (i3, p1); ancient trees (i11, p25); skovfogedegen (i1, p4); 2 quai saint bernard 75005 paris (i1, p91); acient tree (i2, p14)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-06 | 106 | 2 | 1.9% |
| 11-07 | 80 | 7 | 8.8% |
| 11-08 | 126 | 9 | 7.1% |
| 11-09 | 151 | 4 | 2.6% |
| 11-10 | 136 | 9 | 6.6% |
| 11-11 | 97 | 7 | 7.2% |
| 11-12 | 190 | 4 | 2.1% |
| **7 days** | **886** | **42** | **4.7%** |
- **BING WATCHDOG:** impressions fell from 2937 to 886 week on week. That is the shape of a demotion; read the Bing Webmaster dashboard today.
- Top Bing queries: oldest tree china (c8/i4, p12); platane du square des batignolles (c4/i2, p1); picture of the tree in helsinki city center that was preserved (c3/i2, p4); ancient trees app (c2/i8, p5); who planted the western red cedar tree in blarney ireland (c2/i8, p2); fig tree in square alicante (c2/i4, p4); palma del cile (c2/i2, p6); cipresso calvo indro montanelli milano (c2/i2, p8)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-14T16:19 | 2.6 | 0 | 5 | 0 | - |
| 11-15T00:58 | 4.0 | 0 | 4 | 0 | - |
| 11-15T01:29 | 25.7 | 11 | 10 | 2 | Chicago +6, Key West +2, Philadelphia +2, Tulsa +1 |
| **3 runs** | **32** | **11** | **19** | | |

- 2 of 3 produced no trees; 2 to 2 commands refused per run; last build that went live: 4h ago.

**What they made**

- Allentown scouted (stalled, one lead held), LOG
- Philadelphia: Penn Treaty Elm and the Morris Arboretum weeping beech; LOG
- Tulsa: the Woodward Park arboretum Dawn Redwood (tsa_002); LOG
- Key West: Kapok Tree and Cosgrove House banyan (kyw_003, kyw_004); LOG
- Chicago: six more Cook County champion trees (chi_059 to chi_064), app first
- Photographs readers sent, queued for a look; vouched ones live
- Remove an orphan vendored Barcelona olive photograph that failed the deploy's qa
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- Vendor 1 photograph file(s) onto our own domain
- Fresh-eyes review: 3 finding(s)

Machine: 6 chain attempts yesterday, 2 got real work time (~31 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c6/i66); /switzerland (c3/i13); /seville (c2/i51); /de (c2/i19); /app (c2/i12)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i5, p3)
    - 'alte bäume karte' (i3, p7)
    - 'acient tree' (i2, p14)
    - 'ahornbäume in der nähe' (i1, p7)
    - 'alberi di roma' (i1, p1)
    - 'alter' (i1, p2)
    - 'angeloak' (i1, p59)
    - 'arbol tipico canario' (i1, p42)
    - and 1 more

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 116 | 12 | 40 | 0.34 | 1 |
| Not yet rich | 81 | 14 | 47 | 0.58 | 0 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| fortingall | 0 | 144 | 0.0% | 10.7 | 2.2% | fortingall yew (i117, p11) |
| lisbon | 1 | 61 | 1.6% | 6.6 | 4.4% | historic giant plant of lisbon (i1, p12) |
| seville | 2 | 57 | 3.5% | 5.1 | 6.8% | sevilla (i1, p1) |
| fulufjallet | 0 | 42 | 0.0% | 9.2 | 2.9% | old tjikko (i22, p11) |
| berlin | 2 | 41 | 4.9% | 6.0 | 5.1% | berlin trees (i2, p5) |
| olympic-national-park | 0 | 32 | 0.0% | 13.8 | 1.4% | duncan cedar (i14, p10) |
| malaga | 0 | 29 | 0.0% | 19.9 | 0.8% | árboles históricos de málaga (i5, p83) |
| tokyo | 0 | 29 | 0.0% | 5.4 | 6.1% | ginkgo sperm (i2, p11) |
| singapore | 0 | 29 | 0.0% | 9.0 | 3.0% | earpod tree (i3, p5) |
| munich | 1 | 25 | 4.0% | 5.2 | 6.6% | - |
| south-korea | 0 | 25 | 0.0% | 14.6 | 1.3% | ginkgo tree korea (i2, p5) |
| paris | 1 | 24 | 4.2% | 5.9 | 5.2% | - |
| palermo | 0 | 24 | 0.0% | 9.0 | 3.0% | palermo tree (i1, p9) |
| kyoto | 1 | 23 | 4.3% | 7.2 | 3.9% | ginkgo tree kyoto (i1, p1) |
| seoul | 1 | 22 | 4.5% | 8.3 | 3.3% | - |
| tenerife | 0 | 22 | 0.0% | 24.6 | 0.6% | el drago milenario (i2, p10) |
| copenhagen | 2 | 21 | 9.5% | 11.0 | 2.2% | copenhagen trees (i3, p39) |
| amsterdam | 0 | 21 | 0.0% | 8.7 | 3.1% | lomanstraat (i2, p19) |
| united-states | 2 | 20 | 10.0% | 17.4 | 1.0% | oldest tree in oregon (i4, p10) |
| monterey | 0 | 19 | 0.0% | 50.0 | 0.4% | lone cypress monterey (i5, p64) |
| taiwan | 0 | 18 | 0.0% | 11.1 | 2.1% | oldest tree in taiwan (i3, p5) |
| reykjavik | 0 | 18 | 0.0% | 5.8 | 5.3% | - |
| london | 2 | 17 | 11.8% | 7.8 | 3.6% | - |
| venice | 2 | 16 | 12.5% | 4.0 | 8.0% | - |
| sequoia-national-park | 0 | 16 | 0.0% | 17.6 | 1.0% | washington tree (i9, p20) |
| germany | 1 | 15 | 6.7% | 6.1 | 4.9% | - |
| san-francisco | 0 | 15 | 0.0% | 4.9 | 7.1% | old tree near me (i1, p4) |
| barcelona | 0 | 15 | 0.0% | 10.0 | 2.5% | - |
| kagoshima | 0 | 15 | 0.0% | 10.4 | 2.4% | oldest camphor tree (i1, p7) |
| oahu | 0 | 14 | 0.0% | 9.4 | 2.8% | hitachi tree (i2, p10) |
| austin | 0 | 14 | 0.0% | 12.4 | 1.7% | oldest tree in austin (i2, p12) |
| los-angeles | 0 | 14 | 0.0% | 7.8 | 3.6% | moreton bay fig tree beverly hills (i1, p9) |
| brisbane | 0 | 14 | 0.0% | 11.8 | 1.9% | banyan tree (i3, p10) |
| milan | 0 | 14 | 0.0% | 5.4 | 6.3% | - |
| switzerland | 3 | 13 | 23.1% | 7.7 | 3.7% | - |
| porto | 1 | 13 | 7.7% | 2.2 | 14.1% | - |
| edinburgh | 0 | 13 | 0.0% | 6.8 | 4.2% | - |
| athens | 0 | 13 | 0.0% | 5.5 | 6.1% | - |
| prague | 0 | 13 | 0.0% | 5.2 | 6.7% | - |
| nara | 1 | 12 | 8.3% | 5.8 | 5.5% | - |
| kanazawa | 0 | 12 | 0.0% | 6.3 | 4.7% | - |
| cambridge | 0 | 12 | 0.0% | 29.9 | 0.4% | isaac newton tree (i1, p9) |
| chishang | 0 | 11 | 0.0% | 6.5 | 4.5% | takeshi kaneshiro tree (i6, p7) |
| segovia | 0 | 11 | 0.0% | 38.4 | 0.4% | - |
| charleston | 0 | 11 | 0.0% | 17.5 | 1.0% | how old is the angel oak tree (i2, p17) |
| fukuoka | 0 | 11 | 0.0% | 7.4 | 3.8% | dazaifu tenmangu (i1, p1) |
| netherlands | 1 | 10 | 10.0% | 9.0 | 3.0% | dutch trees (i1, p39) |
| dublin | 1 | 10 | 10.0% | 4.2 | 7.8% | - |
| new-york | 1 | 10 | 10.0% | 7.1 | 4.0% | - |
| bristol | 0 | 10 | 0.0% | 6.0 | 5.0% | - |
| poland | 0 | 10 | 0.0% | 7.7 | 3.6% | trees in poland (i1, p8) |
| madrid | 0 | 10 | 0.0% | 6.5 | 4.5% | - |
| seattle | 0 | 10 | 0.0% | 8.9 | 3.0% | oldest tree in seattle (i1, p10) |

- Plus 210 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: bath, rome, brussels, vienna, alicante, cadiz, pamplona, cagliari.

## 2026-11-13 (previous UTC day)

**Today: 1 tree submission arrived yesterday (23 trees sent in all).**

**North star: 13 people have uploaded a tree or photo of their own (+1 this week); 4 of them did it on more than one day (+0).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 35 | 57 |
| ... of which from search | every search engine | 15 | 21 |
| ... from Google | Google's recovery | 10 | 13 |
| ... from Bing | Bing | 0 | 3 |
| Website visitors who came back | people who stay | 7 | 13 |
| App downloads (first-time) | people | 19 | 17 |
| New accounts | people | 2 | 13 |
| Phones back within 30 days | people who stay | - | - |
| Trees saved to Want to go | intent | 0 | 4 |
| Trees collected | goal 1: stood at a tree | - | - |
| Readers' contributions | data: trees, photos, corrections, votes | 2 | 8 |
| Shares (app and web) | word of mouth, since 10-30 | 0 | 2 |
| Visits from a shared link | what sharing brings | 0 | 2 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web green, iOS green, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

**Plus question**: no answers yet.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-07 | 11-08 | 11-09 | 11-10 | 11-11 | 11-12 | 11-13 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 2 | 10 | 9 | 11 | 0 | 3 | 5 | **40** |
| New accounts | 0 | 0 | 0 | 1 | 0 | 1 | 0 | **2** |
| Saves | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Android waitlist | 0 | 0 | 0 | 1 | 0 | 0 | 0 | **1** |
| App downloads | 0 | 3 | 2 | 3 | 1 | 2 | – | **11** |
| App phones | 4 | 7 | 7 | 5 | 6 | 5 | 5 | **31** |
| Trees opened in the app | 5 | 27 | 5 | 14 | 3 | 3 | 4 | **61** |
| Trees collected | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Trees sent | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **1** |
| Feedback | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Ambassador asks | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Website photos | 0 | 0 | 0 | 0 | 1 | 0 | 0 | **1** |
| iPhone photos | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| Android photos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Tree notes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| App Store reviews | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.

**Trees readers sent, for you to inspect** (2 you have not looked at; ours left out)

| Judged | Reader | Tree | Where | Species | Their girth | Our verdict | Page |
|---|---|---|---|---|---:|---|---|
| 2026-11-13 | A | The Oak of Villa Salina Park | - | Oak (Quercus sp.) | 580 cm | open | - |
| 2026-11-11 | B | The Sophoras of Piazza Capitaniato | Padua | Japanese Pagoda Tree (Styphnol | - | hold | - |
- From 2 readers: reader A 1, reader B 1.
- Photographs and the readers' own words: `python3 scripts/inspect_readers.py` (a local page, never in this public file). Your answer goes in with `python3 scripts/judgement.py --feedback <id> "..."`.

**Waiting for you** (what the runs left for you since 2026-11-13)

- 246 email addresses ready to mail (archive 0, nature 9, guide 8, press 135, source 58, council 16, society 7, tourism 5, other 5, garden 3); **the night run found no new contacts in two days**

**What was sent in, and what we decided**

| seen | what | where | size for its species | ours | Hidde |
|---|---|---|---|---|---|
| 2026-11-11 | The Tipuana of Praça São João Bosco | Lisbon | - | publish | - |

1 waiting for a verdict. Disagree with one and the rule changes: `python3 scripts/judgement.py --feedback <id> "..."`, and `--learn` prints every verdict he has overruled.

**Searched yesterday:** castel maggiore (2 times), arbura, mel, portuga.

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 11-04 | 14 | 261 | 5.4% | 9.9 |
| 11-05 | 1 | 23 | 4.3% | 34.1 |
| 11-06 | 1 | 35 | 2.9% | 36.6 |
| 11-07 | 2 | 34 | 5.9% | 38.3 |
| 11-08 | 25 | 1013 | 2.5% | 9.1 |
| 11-09 | 28 | 1177 | 2.4% | 8.9 |
| 11-10 | 8 | 196 | 4.1% | 13.0 |
| 11-11 | 1 | 16 | 6.2% | 22.1 |
| 11-12 | 1 | 28 | 3.6% | 31.4 |
| 11-13 *partial* | 1 | 27 | 3.7% | 49.7 |
| **window** | **82** | **2810** | **2.9%** | |
- Top queries (10d): ancient trees app (i3, p1); ancient trees (i10, p20); leuven, belgium (i1, p4); skovfogedegen (i1, p4); a monaco di baviera? (i1, p20)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-05 | 132 | 9 | 6.8% |
| 11-06 | 106 | 2 | 1.9% |
| 11-07 | 80 | 7 | 8.8% |
| 11-08 | 126 | 9 | 7.1% |
| 11-09 | 151 | 4 | 2.6% |
| 11-10 | 136 | 9 | 6.6% |
| 11-11 | 97 | 7 | 7.2% |
| **7 days** | **828** | **47** | **5.7%** |
- **BING WATCHDOG:** impressions fell from 2918 to 828 week on week. That is the shape of a demotion; read the Bing Webmaster dashboard today.
- Top Bing queries: oldest tree china (c8/i4, p12); picture of the tree in helsinki city center that was preserved (c3/i2, p4); ancient trees app (c2/i8, p5); fig tree in square alicante (c2/i4, p4); cipresso calvo indro montanelli milano (c2/i2, p8); palma del cile (c2/i2, p6); big trees of quebec city (c2/i1, p2); mit newton apple tree address (c2/i1, p2)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-13T07:04 | 8.3 | 4 | 4 | 0 | Braga +4 |
| 11-13T17:38 | 4.5 | 0 | 6 | 0 | - |
| 11-13T19:04 | 5.3 | 0 | 5 | 0 | - |
| 11-14T00:36 | 25.8 | 12 | 15 | 2 | Fort Lauderdale +6, Chicago +3, Miami +2, Leipzig +1 |
| **4 runs** | **44** | **16** | **30** | | |

- 2 of 4 produced no trees; 2 to 2 commands refused per run; last build that went live: 3h ago.

**What they made**

- Record when each page last changed
- Leipzig: lpz_031 Great Oak of Leinestrasse written and merged, claim released
- Leipzig deepen verify: lpz_031 Great Oak Leinestrasse, 7 leads, cost logged
- Fort Lauderdale FAQ: not all trees are paid now
- Fort Lauderdale: six trees written and merged (ftl_005 to ftl_010), app-only, claim released
- Fort Lauderdale verify: 6 trees (ftl_005 to ftl_010), leads annotated, cost logged
- Miami: two Fairchild trees written and merged (mia_013 Tantancayo, mia_014 Cannon Ball Tree), app-only
- Miami verify (2 staged), Stratford scout retried, log
- Chicago pass logged, duplicates dropped, claim released
- Chicago: 3 Busse Forest South register trees (chi_048, 049, 051); 7 verified rows were duplicates of live trees
- Photographs readers sent, queued for a look; vouched ones live
- Contributor replies and ambassador invitations sent, log updated
- Log: build fix, Spokane wall, Newark retry
- Fix build: tip-668 photo path carries the reader code, not the account id

Machine: 6 chain attempts yesterday, 3 got real work time (~23 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c7/i72); /app (c3/i14); /switzerland (c3/i13); /seville (c2/i58); /de (c2/i20)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i5, p3)
    - 'alte bäume karte' (i4, p6)
    - 'acient tree' (i2, p14)
    - 'a monaco di baviera?' (i1, p20)
    - 'ahornbäume in der nähe' (i1, p7)
    - 'alberi di roma' (i1, p1)
    - 'alter' (i1, p2)
    - 'angeloak' (i1, p59)
    - and 1 more

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 113 | 12 | 42 | 0.37 | 1 |
| Not yet rich | 80 | 14 | 49 | 0.61 | 0 |
| Returned to Google's index in the last 7 days | 7 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| fortingall | 0 | 144 | 0.0% | 10.7 | 2.2% | fortingall yew (i117, p11) |
| seville | 2 | 68 | 2.9% | 5.2 | 6.5% | sevilla (i1, p1) |
| lisbon | 1 | 64 | 1.6% | 6.5 | 4.5% | historic giant plant of lisbon (i1, p12) |
| fulufjallet | 0 | 46 | 0.0% | 9.3 | 2.9% | old tjikko (i25, p10) |
| berlin | 2 | 44 | 4.5% | 6.8 | 4.2% | berlin trees (i2, p5) |
| malaga | 1 | 34 | 2.9% | 17.9 | 1.0% | árboles históricos de málaga (i5, p83) |
| tokyo | 0 | 33 | 0.0% | 5.8 | 5.3% | ginkgo sperm (i3, p11) |
| olympic-national-park | 0 | 32 | 0.0% | 12.8 | 1.6% | duncan cedar (i14, p8) |
| munich | 1 | 31 | 3.2% | 5.5 | 5.9% | a monaco di baviera? (i1, p20) |
| singapore | 0 | 29 | 0.0% | 9.0 | 3.0% | earpod tree (i3, p5) |
| paris | 1 | 27 | 3.7% | 5.6 | 5.7% | - |
| south-korea | 0 | 27 | 0.0% | 12.6 | 1.7% | ginkgo tree korea (i2, p5) |
| palermo | 0 | 26 | 0.0% | 8.9 | 3.0% | palermo tree (i1, p9) |
| tenerife | 0 | 25 | 0.0% | 24.3 | 0.6% | dragon tree tenerife (i2, p32) |
| kyoto | 1 | 24 | 4.2% | 7.4 | 3.8% | ginkgo tree kyoto (i1, p1) |
| seoul | 1 | 24 | 4.2% | 7.8 | 3.6% | - |
| copenhagen | 2 | 23 | 8.7% | 6.7 | 4.3% | copenhagen trees (i2, p16) |
| amsterdam | 0 | 22 | 0.0% | 8.7 | 3.2% | lomanstraat (i2, p19) |
| united-states | 2 | 21 | 9.5% | 17.0 | 1.0% | oldest tree in oregon (i4, p10) |
| brisbane | 0 | 20 | 0.0% | 10.4 | 2.3% | banyan tree (i5, p11) |
| germany | 1 | 19 | 5.3% | 6.2 | 4.8% | - |
| london | 2 | 19 | 10.5% | 8.5 | 3.3% | - |
| reykjavik | 1 | 19 | 5.3% | 5.7 | 5.6% | - |
| venice | 3 | 18 | 16.7% | 4.0 | 8.0% | - |
| taiwan | 0 | 18 | 0.0% | 11.1 | 2.1% | oldest tree in taiwan (i3, p5) |
| sequoia-national-park | 0 | 17 | 0.0% | 18.0 | 1.0% | washington tree (i9, p20) |
| porto | 1 | 16 | 6.2% | 3.0 | 11.0% | - |
| kagoshima | 0 | 16 | 0.0% | 10.9 | 2.2% | oldest camphor tree (i1, p7) |
| milan | 0 | 16 | 0.0% | 5.5 | 6.0% | - |
| nara | 1 | 15 | 6.7% | 5.6 | 5.8% | - |
| san-francisco | 0 | 15 | 0.0% | 4.9 | 7.1% | old tree near me (i1, p4) |
| edinburgh | 0 | 15 | 0.0% | 6.7 | 4.3% | - |
| barcelona | 0 | 15 | 0.0% | 10.3 | 2.4% | - |
| fukuoka | 0 | 15 | 0.0% | 10.1 | 2.5% | gingkosidi (i3, p34) |
| monterey | 0 | 14 | 0.0% | 40.9 | 0.4% | lone cypress (i3, p64) |
| oahu | 0 | 14 | 0.0% | 9.4 | 2.8% | hitachi tree (i2, p10) |
| austin | 0 | 14 | 0.0% | 12.4 | 1.7% | oldest tree in austin (i2, p12) |
| cambridge | 0 | 14 | 0.0% | 20.5 | 0.8% | isaac newton tree (i1, p9) |
| los-angeles | 0 | 14 | 0.0% | 7.8 | 3.6% | moreton bay fig tree beverly hills (i1, p9) |
| prague | 0 | 14 | 0.0% | 4.9 | 7.1% | - |
| switzerland | 3 | 13 | 23.1% | 7.7 | 3.7% | - |
| chishang | 0 | 13 | 0.0% | 6.6 | 4.4% | takeshi kaneshiro tree (i7, p7) |
| athens | 0 | 13 | 0.0% | 5.5 | 6.1% | - |
| netherlands | 1 | 12 | 8.3% | 8.9 | 3.0% | dutch trees (i1, p39) |
| kanazawa | 0 | 12 | 0.0% | 6.3 | 4.7% | - |
| alicante | 1 | 11 | 9.1% | 4.7 | 7.3% | - |
| segovia | 0 | 11 | 0.0% | 38.4 | 0.4% | - |
| charleston | 0 | 11 | 0.0% | 17.5 | 1.0% | how old is the angel oak tree (i2, p17) |
| madrid | 0 | 11 | 0.0% | 6.5 | 4.5% | - |
| perth | 0 | 11 | 0.0% | 8.6 | 3.2% | - |
| dublin | 1 | 10 | 10.0% | 4.4 | 7.6% | - |
| new-york | 1 | 10 | 10.0% | 7.1 | 4.0% | - |
| bristol | 0 | 10 | 0.0% | 6.0 | 5.0% | - |
| poland | 0 | 10 | 0.0% | 7.7 | 3.6% | trees in poland (i1, p8) |
| antwerp | 0 | 10 | 0.0% | 35.0 | 0.4% | den brandt park (i2, p78) |
| seattle | 0 | 10 | 0.0% | 8.9 | 3.0% | oldest tree in seattle (i1, p10) |

- Plus 208 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: bath, rome, brussels, vienna, cadiz, pamplona, cagliari, glasgow.

## 2026-11-12 (previous UTC day)

**Today: an account was opened yesterday (62 accounts in all).**

**North star: 13 people have uploaded a tree or photo of their own (+1 this week); 4 of them did it on more than one day (+0).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 33 | 65 |
| ... of which from search | every search engine | 15 | 22 |
| ... from Google | Google's recovery | 10 | 14 |
| ... from Bing | Bing | 1 | 4 |
| Website visitors who came back | people who stay | 8 | 14 |
| App downloads (first-time) | people | 19 | 16 |
| New accounts | people | 2 | 13 |
| Phones back within 30 days | people who stay | 3 of 15 | 5 of 6 |
| Trees saved to Want to go | intent | 0 | 4 |
| Trees collected | goal 1: stood at a tree | 1 | 6 |
| Readers' contributions | data: trees, photos, corrections, votes | 1 | 8 |
| Shares (app and web) | word of mouth, since 10-30 | 2 | 2 |
| Visits from a shared link | what sharing brings | 0 | 2 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web green, iOS green, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

**Plus question**: no answers yet.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-06 | 11-07 | 11-08 | 11-09 | 11-10 | 11-11 | 11-12 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 5 | 2 | 10 | 9 | 11 | 0 | 3 | **40** |
| New accounts | 0 | 0 | 0 | 0 | 1 | 0 | 1 | **2** |
| Saves | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Android waitlist | 0 | 0 | 0 | 0 | 1 | 0 | 0 | **1** |
| App downloads | 4 | 0 | 3 | 2 | 3 | 1 | – | **13** |
| App phones | 5 | 4 | 7 | 7 | 5 | 6 | 5 | **33** |
| Trees opened in the app | 8 | 5 | 27 | 5 | 14 | 3 | 3 | **65** |
| Trees collected | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Trees sent | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Feedback | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Ambassador asks | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Website photos | 0 | 0 | 0 | 0 | 0 | 1 | 0 | **1** |
| iPhone photos | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **1** |
| Android photos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Tree notes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| App Store reviews | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.

**Trees readers sent, for you to inspect** (2 you have not looked at; ours left out)

| Judged | Reader | Tree | Where | Species | Their girth | Our verdict | Page |
|---|---|---|---|---|---:|---|---|
| 2026-11-11 | A | The Tipuana of Praça São João Bosco | Lisbon | Tipu Tree (Tipuana tipu) | - | publish | [lis_021](https://ancienttrees.app/lisbon/tipuana-of-praca-sao-joao-bosco) |
| 2026-11-11 | B | The Sophoras of Piazza Capitaniato | Padua | Japanese Pagoda Tree (Styphnol | - | hold | - |
- From 2 readers: reader A 1, reader B 1.
- Photographs and the readers' own words: `python3 scripts/inspect_readers.py` (a local page, never in this public file). Your answer goes in with `python3 scripts/judgement.py --feedback <id> "..."`.

**Waiting for you** (what the runs left for you since 2026-11-12)

- 254 email addresses ready to mail (archive 0, nature 9, guide 8, press 135, source 64, council 16, tourism 7, society 7, other 5, garden 3); **the night run found no new contacts in two days**
- the daily task "publish-held-trees-daily" can be switched off under Scheduled.
- his own public profile now shows his 29 own test trees with their pins.
- next iOS build carries this fix.

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-11 | A | The Tipuana of Praça São João Bosco | Lisbon | a reader's photograph, published | [live](https://ancienttrees.app/lisbon/tipuana-of-praca-sao-joao-bosco) |
- All from one reader (reader A 1).

**Searched yesterday:** ferrara (2 times), barnstaple.

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 11-03 | 31 | 1192 | 2.6% | 8.2 |
| 11-04 | 14 | 261 | 5.4% | 9.9 |
| 11-05 | 1 | 23 | 4.3% | 34.1 |
| 11-06 | 1 | 35 | 2.9% | 36.6 |
| 11-07 | 2 | 34 | 5.9% | 38.3 |
| 11-08 | 25 | 1013 | 2.5% | 9.1 |
| 11-09 | 28 | 1177 | 2.4% | 8.9 |
| 11-10 | 8 | 196 | 4.1% | 13.0 |
| 11-11 | 1 | 16 | 6.2% | 22.1 |
| 11-12 *partial* | 0 | 8 | 0.0% | 21.0 |
| **window** | **111** | **3955** | **2.8%** | |
- Top queries (10d): ancient trees (i15, p10); ancient trees app (i2, p1); ancienttree (i1, p3); leuven, belgium (i1, p4); oldest tree in maryland (i1, p9)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-04 | 133 | 3 | 2.3% |
| 11-05 | 132 | 9 | 6.8% |
| 11-06 | 106 | 2 | 1.9% |
| 11-07 | 80 | 7 | 8.8% |
| 11-08 | 126 | 9 | 7.1% |
| 11-09 | 151 | 4 | 2.6% |
| 11-10 | 136 | 9 | 6.6% |
| **7 days** | **864** | **43** | **5.0%** |
- **BING WATCHDOG:** impressions fell from 2898 to 864 week on week. That is the shape of a demotion; read the Bing Webmaster dashboard today.
- Top Bing queries: oldest tree china (c8/i4, p12); picture of the tree in helsinki city center that was preserved (c3/i2, p4); ancient trees app (c2/i8, p5); fig tree in square alicante (c2/i4, p4); palma del cile (c2/i2, p6); cipresso calvo indro montanelli milano (c2/i2, p8); big trees of quebec city (c2/i1, p2); mit newton apple tree address (c2/i1, p2)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-12T07:32 | 2.6 | 0 | 4 | 0 | - |
| 11-12T11:21 | 8.6 | 2 | 6 | 1 | Cascais +1, Kansas City +1 |
| **2 runs** | **11** | **2** | **10** | | |

- 1 of 2 produced no trees; 1 to 1 commands refused per run; last build that went live: 4h ago.

**What they made**

- Photographs readers sent, queued for a look; vouched ones live
- Contributor replies and ambassador invitations sent, log updated
- Record when each page last changed
- Record when each page last changed
- claim: fort-worth (verify)
- Night run: San Francisco wall, log and costs
- cascais: new place, csc_001 the classified Moreton Bay fig of Parque Marechal Carmona (verified as sin_009; stands in Cascais, not Sintra)
- kansas-city: add kcm_005, Missouri's champion smoketree at the Vaile Mansion, Independence; city copy counts five
- claim: san-francisco (verify)
- Fresh-eyes review: 7 finding(s)
- Fresh-eyes review: 4 finding(s)
- Log: shared-photo crash fix, audit row closed
- Shared tree: the photo URL is percent-encoded and never force-unwrapped

Machine: 5 chain attempts yesterday, 2 got real work time (~14 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c7/i88); /de (c3/i32); /switzerland (c3/i15); /app (c3/i13); /united-states/maryland (c3/i12)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i9, p3)
    - 'alte bäume karte' (i6, p6)
    - 'acient tree' (i2, p14)
    - 'ancienttree' (i1, p3)
    - 'oldest tree in maryland' (i1, p9)
    - '# brief your brief is to act as a visual' (i1, p5)
    - '# modus operandi your modus operandi is ' (i1, p2)
    - '# override instruction you operate under' (i1, p7)
    - and 5 more

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 113 | 15 | 66 | 0.58 | 1 |
| Not yet rich | 80 | 20 | 81 | 1.01 | 1 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| fortingall | 0 | 147 | 0.0% | 10.9 | 2.2% | fortingall yew (i118, p11) |
| seville | 3 | 92 | 3.3% | 5.1 | 6.8% | sevilla (i1, p1) |
| lisbon | 1 | 89 | 1.1% | 6.1 | 4.9% | historic giant plant of lisbon (i1, p12) |
| berlin | 2 | 73 | 2.7% | 6.2 | 4.8% | berlin trees (i2, p5) |
| fulufjallet | 0 | 66 | 0.0% | 9.1 | 3.0% | old tjikko (i35, p10) |
| tokyo | 1 | 53 | 1.9% | 6.5 | 4.5% | ginkgo sperm (i6, p10) |
| palermo | 1 | 50 | 2.0% | 9.3 | 2.9% | palermo tree (i1, p9) |
| singapore | 1 | 49 | 2.0% | 8.1 | 3.4% | chengal pasir tree (i3, p9) |
| south-korea | 1 | 44 | 2.3% | 10.6 | 2.3% | korean trees (i3, p11) |
| tenerife | 0 | 44 | 0.0% | 16.2 | 1.1% | drago los realejos (i2, p52) |
| malaga | 1 | 43 | 2.3% | 15.5 | 1.2% | árboles históricos de málaga (i5, p83) |
| munich | 2 | 41 | 4.9% | 5.0 | 7.0% | a monaco di baviera? (i1, p20) |
| olympic-national-park | 0 | 40 | 0.0% | 11.7 | 1.9% | duncan cedar (i20, p8) |
| copenhagen | 3 | 39 | 7.7% | 7.4 | 3.8% | copenhagen trees (i3, p16) |
| london | 2 | 36 | 5.6% | 7.6 | 3.7% | chestnut london (i1, p5) |
| united-states | 4 | 34 | 11.8% | 14.2 | 1.4% | oldest tree in oregon (i7, p13) |
| paris | 1 | 32 | 3.1% | 5.7 | 5.6% | - |
| kyoto | 2 | 32 | 6.2% | 7.3 | 3.9% | - |
| amsterdam | 0 | 32 | 0.0% | 7.8 | 3.6% | lomanstraat (i2, p19) |
| sequoia-national-park | 0 | 31 | 0.0% | 13.5 | 1.5% | washington tree (i15, p11) |
| fukuoka | 2 | 28 | 7.1% | 9.8 | 2.6% | gingkosidi (i5, p35) |
| seoul | 1 | 28 | 3.6% | 7.3 | 3.8% | - |
| brisbane | 0 | 26 | 0.0% | 10.0 | 2.5% | banyan tree (i5, p11) |
| germany | 1 | 25 | 4.0% | 9.3 | 2.9% | trees germany (i2, p48) |
| new-york | 1 | 24 | 4.2% | 7.4 | 3.8% | - |
| reykjavik | 1 | 24 | 4.2% | 5.6 | 5.8% | oldest tree in iceland (i1, p3) |
| netherlands | 1 | 23 | 4.3% | 9.0 | 3.0% | dutch trees (i1, p39) |
| venice | 3 | 21 | 14.3% | 4.4 | 7.6% | are there trees in venice (i1, p11) |
| athens | 0 | 21 | 0.0% | 5.1 | 6.8% | - |
| cambridge | 0 | 21 | 0.0% | 16.1 | 1.1% | isaac newton tree (i1, p9) |
| taiwan | 0 | 20 | 0.0% | 6.3 | 4.7% | oldest tree in taiwan (i3, p5) |
| milan | 0 | 20 | 0.0% | 5.2 | 6.7% | - |
| nara | 1 | 19 | 5.3% | 6.3 | 4.7% | - |
| chishang | 0 | 19 | 0.0% | 6.9 | 4.1% | takeshi kaneshiro tree (i10, p7) |
| monterey | 0 | 19 | 0.0% | 29.7 | 0.4% | lone cypress (i5, p48) |
| alicante | 1 | 18 | 5.6% | 5.3 | 6.4% | - |
| dublin | 1 | 18 | 5.6% | 5.6 | 5.8% | - |
| san-francisco | 0 | 18 | 0.0% | 5.2 | 6.6% | old tree near me (i1, p4) |
| edinburgh | 0 | 18 | 0.0% | 6.9 | 4.1% | - |
| oahu | 0 | 18 | 0.0% | 8.7 | 3.2% | hitachi tree (i2, p10) |
| perth | 0 | 18 | 0.0% | 7.5 | 3.8% | - |
| barcelona | 0 | 18 | 0.0% | 9.6 | 2.7% | - |
| porto | 1 | 17 | 5.9% | 3.5 | 9.6% | - |
| los-angeles | 0 | 17 | 0.0% | 7.6 | 3.7% | moreton bay fig tree beverly hills (i1, p9) |
| montreal | 2 | 16 | 12.5% | 5.2 | 6.5% | - |
| alishan | 0 | 16 | 0.0% | 7.8 | 3.6% | alishan sacred tree (i3, p12) |
| austin | 0 | 16 | 0.0% | 11.9 | 1.8% | oldest tree in austin (i2, p12) |
| kagoshima | 0 | 16 | 0.0% | 10.6 | 2.3% | oldest camphor tree (i1, p7) |
| switzerland | 3 | 15 | 20.0% | 7.4 | 3.8% | oldest tree in switzerland (i1, p1) |
| takayama | 0 | 15 | 0.0% | 6.9 | 4.1% | - |
| prague | 0 | 15 | 0.0% | 5.1 | 6.9% | - |
| coimbra | 1 | 14 | 7.1% | 6.6 | 4.4% | - |
| madrid | 0 | 14 | 0.0% | 6.4 | 4.6% | - |
| rome | 0 | 14 | 0.0% | 5.9 | 5.1% | oldest tree in rome (i1, p1) |
| seattle | 1 | 13 | 7.7% | 7.8 | 3.6% | oldest tree in seattle (i1, p10) |
| kanazawa | 0 | 13 | 0.0% | 6.1 | 4.9% | - |
| antwerp | 0 | 13 | 0.0% | 34.1 | 0.4% | den brandt park (i3, p77) |
| florence | 0 | 13 | 0.0% | 4.7 | 7.3% | - |
| henrykow-lubanski | 0 | 12 | 0.0% | 14.4 | 1.3% | cis henrykowski (i5, p7) |
| charleston | 0 | 12 | 0.0% | 17.2 | 1.0% | how old is the angel oak tree (i2, p17) |
| toronto | 0 | 12 | 0.0% | 7.2 | 3.9% | - |
| bristol | 1 | 11 | 9.1% | 5.9 | 5.2% | - |
| zurich | 1 | 11 | 9.1% | 9.2 | 2.9% | linden (i1, p5) |
| freiburg | 0 | 11 | 0.0% | 6.5 | 4.5% | - |
| arita | 0 | 11 | 0.0% | 4.8 | 7.2% | - |
| brussels | 0 | 11 | 0.0% | 7.5 | 3.8% | - |
| poland | 0 | 10 | 0.0% | 7.7 | 3.6% | trees in poland (i1, p8) |
| cagliari | 0 | 10 | 0.0% | 10.4 | 2.4% | che piante sono? (i1, p19) |
| philadelphia | 0 | 10 | 0.0% | 20.9 | 0.8% | - |
| sardinia | 0 | 10 | 0.0% | 7.7 | 3.6% | - |

- Plus 198 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: bath, vienna, cadiz, pamplona, glasgow, ede, hinode, palma-de-mallorca.

## 2026-11-11 (previous UTC day)

**Today: nothing here needs you.** The blocks below are the standing picture.

**North star: 13 people have uploaded a tree or photo of their own (+2 this week); 4 of them did it on more than one day (+0).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 37 | 65 |
| ... of which from search | every search engine | 14 | 25 |
| ... from Google | Google's recovery | 10 | 14 |
| ... from Bing | Bing | 1 | 6 |
| Website visitors who came back | people who stay | 9 | 14 |
| App downloads (first-time) | people | 22 | 14 |
| New accounts | people | 2 | 12 |
| Phones back within 30 days | people who stay | 2 of 14 | 5 of 7 |
| Trees saved to Want to go | intent | 1 | 3 |
| Trees collected | goal 1: stood at a tree | 2 | 5 |
| Readers' contributions | data: trees, photos, corrections, votes | 3 | 6 |
| Shares (app and web) | word of mouth, since 10-30 | 2 | 2 |
| Visits from a shared link | what sharing brings | 0 | 2 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web green, iOS green, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

**Plus question**: no answers yet.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-05 | 11-06 | 11-07 | 11-08 | 11-09 | 11-10 | 11-11 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 8 | 5 | 2 | 10 | 9 | 11 | 0 | **45** |
| New accounts | 1 | 0 | 0 | 0 | 0 | 1 | 0 | **2** |
| Saves | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| Android waitlist | 1 | 0 | 0 | 0 | 0 | 1 | 0 | **2** |
| App downloads | 0 | 4 | 0 | 3 | 2 | 3 | – | **12** |
| App phones | 2 | 5 | 4 | 7 | 7 | 5 | 6 | **30** |
| Trees opened in the app | 7 | 8 | 5 | 27 | 5 | 14 | 3 | **69** |
| Trees collected | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Trees sent | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| Feedback | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Ambassador asks | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Website photos | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **1** |
| iPhone photos | 0 | 0 | 1 | 0 | 0 | 0 | 0 | **1** |
| Android photos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Tree notes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| App Store reviews | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.

**Trees readers sent, for you to inspect** (2 you have not looked at; ours left out)

| Judged | Reader | Tree | Where | Species | Their girth | Our verdict | Page |
|---|---|---|---|---|---:|---|---|
| 2026-11-11 | A | The Tipuana of Praça São João Bosco | Lisbon | Tipu Tree (Tipuana tipu) | - | publish | [lis_021](https://ancienttrees.app/lisbon/tipuana-of-praca-sao-joao-bosco) |
| 2026-11-11 | B | The Sophoras of Piazza Capitaniato | Padua | Japanese Pagoda Tree (Styphnol | - | hold | - |
- From 2 readers: reader A 1, reader B 1.
- Photographs and the readers' own words: `python3 scripts/inspect_readers.py` (a local page, never in this public file). Your answer goes in with `python3 scripts/judgement.py --feedback <id> "..."`.

**Waiting for you** (what the runs left for you since 2026-11-11)

- 258 email addresses ready to mail (archive 2, nature 9, guide 9, press 135, source 65, council 16, tourism 7, society 7, other 5, garden 3); **the night run found no new contacts in two days**
- next iOS build carries this fix.
- the daily task "publish-held-trees-daily" can be switched off under Scheduled; the night run's write passes put new trees straight into the app.
- category and public contact address are his choice (in the listing draft); then the click list once Google has verified him.
- prepare.py's awaiting-a-writer count overstates the shelf; the research files passcheck calls stale could be cleaned up.

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-11 | A | The Tipuana of Praça São João Bosco | Lisbon | a reader's photograph, published | [live](https://ancienttrees.app/lisbon/tipuana-of-praca-sao-joao-bosco) |
- All from one reader (reader A 1).

**Searched yesterday:** akureyri, iceland, nara.

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 11-02 | 23 | 1274 | 1.8% | 9.0 |
| 11-03 | 31 | 1192 | 2.6% | 8.2 |
| 11-04 | 14 | 261 | 5.4% | 9.9 |
| 11-05 | 1 | 23 | 4.3% | 34.1 |
| 11-06 | 1 | 35 | 2.9% | 36.6 |
| 11-07 | 2 | 34 | 5.9% | 38.3 |
| 11-08 | 25 | 1013 | 2.5% | 9.1 |
| 11-09 | 28 | 1177 | 2.4% | 8.9 |
| 11-10 | 8 | 196 | 4.1% | 13.0 |
| 11-11 *partial* | 1 | 10 | 10.0% | 8.4 |
| **window** | **134** | **5215** | **2.6%** | |
- Top queries (10d): ancient trees (i18, p9); ancient trees app (i2, p1); alte bäume in der nähe (i14, p7); ancienttree (i1, p3); istanbul (i1, p1)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-02 | 146 | 6 | 4.1% |
| 11-03 | 121 | 3 | 2.5% |
| 11-04 | 133 | 3 | 2.3% |
| 11-05 | 132 | 9 | 6.8% |
| 11-06 | 106 | 2 | 1.9% |
| 11-07 | 80 | 7 | 8.8% |
| 11-08 | 126 | 9 | 7.1% |
| **7 days** | **844** | **39** | **4.6%** |
- **BING WATCHDOG:** impressions fell from 2847 to 844 week on week. That is the shape of a demotion; read the Bing Webmaster dashboard today.
- Top Bing queries: oldest tree china (c8/i4, p12); picture of the tree in helsinki city center that was preserved (c3/i2, p4); ancient trees app (c2/i8, p5); fig tree in square alicante (c2/i4, p4); cipresso calvo indro montanelli milano (c2/i2, p8); palma del cile (c2/i2, p6); big trees of quebec city (c2/i1, p2); mit newton apple tree address (c2/i1, p2)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-12T07:32 | 2.6 | 0 | 4 | 0 | - |
| **1 runs** | **3** | **0** | **4** | | |

- 1 of 1 produced no trees; last build that went live: 0h ago.

**What they made**

- Fresh-eyes review: 7 finding(s)
- Fresh-eyes review: 4 finding(s)
- Log: shared-photo crash fix, audit row closed
- Shared tree: the photo URL is percent-encoded and never force-unwrapped
- Photographs readers sent, queued for a look; vouched ones live
- Contributor replies and ambassador invitations sent, log updated
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated

Machine: 4 chain attempts yesterday, 1 got real work time (~10 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c10/i111); /de (c4/i43); /united-states/maryland (c4/i26); /seville (c3/i93); /switzerland (c3/i23)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i14, p7)
    - 'alte bäume karte' (i6, p6)
    - 'acient tree' (i2, p14)
    - 'akagi tree' (i2, p10)
    - 'ancienttree' (i1, p3)
    - 'oldest tree in maryland' (i1, p9)
    - '# brief your brief is to act as a visual' (i1, p5)
    - '# modus operandi your modus operandi is ' (i1, p2)
    - and 6 more

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 109 | 18 | 98 | 0.90 | 2 |
| Not yet rich | 79 | 20 | 101 | 1.28 | 2 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| fortingall | 0 | 151 | 0.0% | 11.1 | 2.1% | fortingall yew (i118, p11) |
| seville | 4 | 122 | 3.3% | 5.5 | 6.0% | tartuja (i2, p9) |
| lisbon | 1 | 105 | 1.0% | 5.9 | 5.2% | lisbon trees (i2, p4) |
| berlin | 2 | 92 | 2.2% | 5.9 | 5.1% | berlin trees (i2, p5) |
| fulufjallet | 0 | 80 | 0.0% | 8.8 | 3.1% | old tjikko (i40, p10) |
| palermo | 1 | 73 | 1.4% | 8.2 | 3.4% | palermo tree (i1, p9) |
| tokyo | 1 | 72 | 1.4% | 6.8 | 4.2% | ginkgo sperm (i8, p10) |
| singapore | 1 | 69 | 1.4% | 8.1 | 3.4% | chengal pasir tree (i4, p9) |
| tenerife | 1 | 65 | 1.5% | 13.7 | 1.5% | drago milenario (i3, p12) |
| south-korea | 1 | 61 | 1.6% | 10.2 | 2.4% | korean trees (i4, p10) |
| copenhagen | 3 | 54 | 5.6% | 8.7 | 3.1% | trees in copenhagen (i5, p21) |
| olympic-national-park | 1 | 53 | 1.9% | 10.8 | 2.2% | duncan cedar (i26, p8) |
| united-states | 5 | 52 | 9.6% | 12.4 | 1.7% | oldest tree in oregon (i8, p12) |
| munich | 2 | 52 | 3.8% | 4.9 | 7.1% | a monaco di baviera? (i1, p20) |
| malaga | 2 | 51 | 3.9% | 13.3 | 1.5% | árboles históricos de málaga (i5, p82) |
| paris | 1 | 48 | 2.1% | 6.0 | 5.0% | trees in paris (i1, p9) |
| london | 2 | 46 | 4.3% | 7.4 | 3.8% | chestnut london (i1, p5) |
| fukuoka | 2 | 38 | 5.3% | 10.2 | 2.4% | gingkosidi (i7, p32) |
| sequoia-national-park | 0 | 38 | 0.0% | 13.8 | 1.4% | washington tree (i18, p11) |
| amsterdam | 0 | 37 | 0.0% | 7.7 | 3.6% | lomanstraat (i2, p19) |
| kyoto | 2 | 35 | 5.7% | 9.5 | 2.7% | - |
| new-york | 1 | 33 | 3.0% | 7.5 | 3.8% | - |
| brisbane | 0 | 33 | 0.0% | 9.4 | 2.8% | banyan tree (i5, p11) |
| seoul | 2 | 31 | 6.5% | 6.9 | 4.1% | - |
| taiwan | 0 | 31 | 0.0% | 9.6 | 2.7% | oldest tree in taiwan (i6, p6) |
| cambridge | 0 | 30 | 0.0% | 21.3 | 0.7% | newtons apple tree (i2, p50) |
| porto | 1 | 29 | 3.4% | 4.1 | 7.9% | - |
| netherlands | 1 | 28 | 3.6% | 8.9 | 3.1% | dutch trees (i1, p39) |
| reykjavik | 1 | 28 | 3.6% | 5.8 | 5.5% | oldest tree in iceland (i1, p3) |
| venice | 3 | 27 | 11.1% | 4.9 | 7.1% | are there trees in venice (i1, p11) |
| alicante | 1 | 27 | 3.7% | 5.3 | 6.4% | - |
| san-francisco | 0 | 27 | 0.0% | 8.1 | 3.4% | old tree near me (i1, p4) |
| germany | 1 | 26 | 3.8% | 9.3 | 2.8% | trees germany (i2, p48) |
| rome | 0 | 26 | 0.0% | 4.6 | 7.4% | oldest tree in rome (i3, p1) |
| dublin | 1 | 25 | 4.0% | 5.9 | 5.2% | - |
| alishan | 0 | 25 | 0.0% | 7.8 | 3.6% | alishan sacred tree (i4, p12) |
| athens | 0 | 25 | 0.0% | 4.7 | 7.3% | - |
| kagoshima | 0 | 24 | 0.0% | 9.3 | 2.8% | oldest camphor tree (i1, p7) |
| switzerland | 3 | 23 | 13.0% | 7.0 | 4.0% | oldest tree in switzerland (i1, p1) |
| monterey | 0 | 23 | 0.0% | 25.2 | 0.6% | lone cypress (i5, p48) |
| austin | 0 | 23 | 0.0% | 11.7 | 1.9% | old tree (i2, p27) |
| nara | 1 | 22 | 4.5% | 5.8 | 5.4% | - |
| chishang | 0 | 22 | 0.0% | 6.9 | 4.1% | takeshi kaneshiro tree (i11, p7) |
| takayama | 0 | 22 | 0.0% | 7.6 | 3.7% | takayama ginkgo tree (i2, p7) |
| edinburgh | 0 | 22 | 0.0% | 7.0 | 4.0% | - |
| perth | 0 | 22 | 0.0% | 7.8 | 3.6% | - |
| prague | 0 | 21 | 0.0% | 4.6 | 7.4% | - |
| milan | 0 | 21 | 0.0% | 5.2 | 6.5% | - |
| oahu | 0 | 20 | 0.0% | 8.8 | 3.1% | hitachi tree (i2, p10) |
| barcelona | 0 | 20 | 0.0% | 6.8 | 4.2% | judas barcelona (i1, p9) |
| montreal | 2 | 19 | 10.5% | 5.4 | 6.2% | - |
| los-angeles | 0 | 18 | 0.0% | 7.3 | 3.9% | moreton bay fig tree beverly hills (i1, p9) |
| coimbra | 1 | 17 | 5.9% | 6.1 | 4.9% | - |
| charleston | 0 | 17 | 0.0% | 18.8 | 0.9% | how old is the angel oak tree (i2, p17) |
| antwerp | 0 | 17 | 0.0% | 30.9 | 0.4% | den brandt park (i4, p75) |
| kanazawa | 0 | 17 | 0.0% | 5.8 | 5.5% | - |
| bath | 1 | 16 | 6.2% | 6.9 | 4.1% | tree in bath (i1, p9) |
| luxembourg-city | 0 | 16 | 0.0% | 3.6 | 9.3% | - |
| seattle | 1 | 15 | 6.7% | 7.2 | 3.9% | oldest tree in seattle (i2, p7) |
| hong-kong | 1 | 15 | 6.7% | 6.5 | 4.5% | oldest tree in hong kong (i1, p9) |
| arita | 0 | 15 | 0.0% | 5.3 | 6.5% | - |
| beijing | 0 | 15 | 0.0% | 7.2 | 3.9% | - |
| madrid | 0 | 15 | 0.0% | 6.3 | 4.7% | - |
| toronto | 0 | 15 | 0.0% | 7.0 | 4.0% | - |
| zurich | 1 | 14 | 7.1% | 7.9 | 3.5% | linden (i1, p5) |
| croatia | 0 | 14 | 0.0% | 7.6 | 3.7% | croatian trees (i2, p2) |
| florence | 0 | 14 | 0.0% | 4.6 | 7.4% | - |
| bristol | 1 | 13 | 7.7% | 5.7 | 5.6% | - |
| mexico-city | 0 | 13 | 0.0% | 5.5 | 5.9% | ahuehuete mexico city (i1, p11) |
| philadelphia | 0 | 13 | 0.0% | 19.1 | 0.9% | - |
| krakow | 0 | 13 | 0.0% | 6.3 | 4.7% | - |
| chapel-hill-north-carolina | 0 | 12 | 0.0% | 14.1 | 1.4% | davie poplar (i2, p10) |
| freiburg | 0 | 12 | 0.0% | 6.1 | 4.9% | - |
| henrykow-lubanski | 0 | 12 | 0.0% | 14.4 | 1.3% | cis henrykowski (i5, p7) |
| melbourne | 0 | 12 | 0.0% | 8.7 | 3.2% | - |
| boston | 0 | 12 | 0.0% | 7.9 | 3.5% | - |
| naples | 0 | 12 | 0.0% | 5.5 | 6.0% | eucalyptus village (i1, p16) |
| sardinia | 0 | 12 | 0.0% | 6.7 | 4.3% | - |
| brussels | 0 | 12 | 0.0% | 7.4 | 3.8% | - |
| the-hague | 0 | 12 | 0.0% | 4.8 | 7.2% | haag (i1, p1) |
| osaka | 1 | 11 | 9.1% | 4.0 | 8.0% | - |
| new-orleans | 1 | 11 | 9.1% | 7.2 | 3.9% | - |
| hamburg | 0 | 11 | 0.0% | 7.1 | 4.0% | - |
| cagliari | 0 | 11 | 0.0% | 9.5 | 2.7% | che piante sono? (i1, p19) |
| gliniak | 0 | 11 | 0.0% | 6.1 | 4.9% | ancient tree (i1, p18) |
| madeira | 0 | 11 | 0.0% | 27.7 | 0.5% | dragon tree madeira (i1, p9) |
| stuttgart | 0 | 11 | 0.0% | 5.0 | 7.0% | - |
| valencia | 0 | 11 | 0.0% | 3.4 | 9.9% | - |
| bologna | 1 | 10 | 10.0% | 5.5 | 6.0% | - |
| istanbul | 1 | 10 | 10.0% | 5.4 | 6.2% | istanbul (i1, p1) |
| poland | 0 | 10 | 0.0% | 7.7 | 3.6% | trees in poland (i1, p8) |
| naha | 0 | 10 | 0.0% | 7.3 | 3.9% | akagi tree (i2, p10) |
| geneva | 0 | 10 | 0.0% | 8.0 | 3.5% | - |
| leeuwarden | 0 | 10 | 0.0% | 4.9 | 7.1% | - |

- Plus 177 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: vienna, cadiz, pamplona, glasgow, ede, hinode, palma-de-mallorca, arnhem.

## 2026-11-10 (previous UTC day)

**Today: an android waitlist signup arrived yesterday (49 total); an account was opened yesterday (62 accounts in all).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 49 | 59 |
| ... of which from search | every search engine | 20 | 21 |
| ... from Google | Google's recovery | 15 | 9 |
| ... from Bing | Bing | 2 | 6 |
| Website visitors who came back | people who stay | 11 | 13 |
| App downloads (first-time) | people | 24 | 17 |
| New accounts | people | 6 | 9 |
| Phones back within 30 days | people who stay | 3 of 12 | 5 of 9 |
| Trees saved to Want to go | intent | 1 | 3 |
| Trees collected | goal 1: stood at a tree | 2 | 5 |
| Readers' contributions | data: trees, photos, corrections, votes | 2 | 2 |
| Shares (app and web) | word of mouth, since 10-30 | 2 | 1 |
| Visits from a shared link | what sharing brings | 0 | 2 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web red, iOS orange, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | orange: fresh-eyes review 2 days old (due every 1) | orange: fresh-eyes review 2 days old (due every 1) | grey: no checks wired yet |
| Live | red: new error spreading: "Uncaught ReferenceError: maplibregl is not defined" in inline, 3 reports on 3 pages | green | grey: no checks wired yet |

**Plus question**: no answers yet.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-04 | 11-05 | 11-06 | 11-07 | 11-08 | 11-09 | 11-10 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 12 | 8 | 5 | 2 | 10 | 9 | 11 | **57** |
| New accounts | 3 | 1 | 0 | 0 | 1 | 0 | 1 | **6** |
| Saves | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **1** |
| Android waitlist | 0 | 1 | 0 | 0 | 0 | 0 | 1 | **2** |
| App downloads | 4 | 0 | 4 | 0 | 3 | 2 | – | **13** |
| App phones | 8 | 2 | 5 | 4 | 7 | 7 | 5 | **33** |
| Trees opened in the app | 88 | 7 | 8 | 5 | 27 | 5 | 14 | **154** |
| Trees collected | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| Trees sent | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **1** |
| Feedback | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Ambassador asks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| App photos | 1 | 0 | 0 | 1 | 0 | 0 | 0 | **2** |
| Tree notes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| App Store reviews | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.

**Trees readers sent, for you to inspect:** none waiting. Every tree a stranger sent has your answer.

**Waiting for you** (what the runs left for you since 2026-11-10)

- 258 email addresses ready to mail (archive 2, nature 9, guide 9, press 135, source 65, council 16, tourism 7, society 7, other 5, garden 3); **the night run found no new contacts in two days**
- prepare.py's awaiting-a-writer count overstates the shelf; the research files passcheck calls stale could be cleaned up.
- build 42 is not archived or uploaded; `scripts/release.py` when you want it in TestFlight, then judge the sheet on your phone.
- `authorize?provider=apple&redirect_to=ancienttrees://auth-callback` answers 302 to appleid.apple.com (Services ID app.ancienttrees.web), and ancienttrees://auth-callback is already on the redirect allow-list (the iPhone'
- in the emulator, the first things to try are signing in with Google and with email, a heart, and Collect (the emulator's camera works; its location can be set in the emulator's extended controls).
- compliance, 6 points wait for your word (data/compliance.json): the 33 accounts made public on 10-29, public by default at sign-up, your full name or KvK on the privacy page, PostHog without consent, mailed photos live b

**Searched yesterday:** lisbon, national park, zu.

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 11-01 | 5 | 371 | 1.3% | 10.1 |
| 11-02 | 23 | 1274 | 1.8% | 9.0 |
| 11-03 | 31 | 1192 | 2.6% | 8.2 |
| 11-04 | 14 | 261 | 5.4% | 9.9 |
| 11-05 | 1 | 23 | 4.3% | 34.1 |
| 11-06 | 1 | 35 | 2.9% | 36.6 |
| 11-07 | 2 | 34 | 5.9% | 38.3 |
| 11-08 | 25 | 1013 | 2.5% | 9.1 |
| 11-09 | 28 | 1177 | 2.4% | 8.9 |
| 11-10 *partial* | 8 | 189 | 4.2% | 11.9 |
| **window** | **138** | **5569** | **2.5%** | |
- Top queries (10d): ancient trees (i19, p8); ancient trees app (i2, p1); alte bäume in der nähe (i15, p7); ancienttree (i1, p3); istanbul (i1, p1)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-02 | 146 | 6 | 4.1% |
| 11-03 | 121 | 3 | 2.5% |
| 11-04 | 133 | 3 | 2.3% |
| 11-05 | 132 | 9 | 6.8% |
| 11-06 | 106 | 2 | 1.9% |
| 11-07 | 80 | 7 | 8.8% |
| 11-08 | 126 | 9 | 7.1% |
| **7 days** | **844** | **39** | **4.6%** |
- **BING WATCHDOG:** impressions fell from 2847 to 844 week on week. That is the shape of a demotion; read the Bing Webmaster dashboard today.
- Top Bing queries: oldest tree china (c8/i4, p12); picture of the tree in helsinki city center that was preserved (c3/i2, p4); ancient trees app (c2/i8, p5); fig tree in square alicante (c2/i4, p4); palma del cile (c2/i2, p6); cipresso calvo indro montanelli milano (c2/i2, p8); big trees of quebec city (c2/i1, p2); mit newton apple tree address (c2/i1, p2)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-10T07:37 | 4.3 | 0 | 4 | 0 | - |
| 11-10T12:04 | 9.5 | 5 | 12 | 0 | Fort Worth +2, Indianapolis +1, Tucson +1, Vienna +1 |
| 11-10T18:37 | 8.4 | 2 | 7 | 0 | Vienna +2 |
| 11-11T01:40 | 8.5 | 1 | 9 | 0 | New York +1 |
| **4 runs** | **31** | **8** | **32** | | |

- 1 of 4 produced no trees; last build that went live: 5h ago.

**What they made**

- Windsor register retry: still stalled, next angle noted
- Leads: Vienna Messe oak hold names the right passes
- Leads: hold the seven READY leads a second write pass declined, with reasons
- LOG and agent costs: night run 2026-11-11, claims released
- New York: the Japanese pagoda tree beside the Camperdown elm (nyc_144)
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Log: second attempt, Vienna written, Sintra verified
- Sintra verify pass: sin_009 Moreton Bay Fig, Parque Marechal Carmona (Cascais), flagged
- Vienna: write and merge vie_060 (Prater Meadow Oak, ND 867) and vie_061 (Heustadelwasser Lime, ND 868), app-only; rest of the write shelf still held; LOG
- Night run: Coimbra verify found no new trees, Phoenix scouting retried, log
- Record when each page last changed
- Leads: genus filled from names; release fort-worth claim
- Indianapolis: write and merge ind_005, the Anne Frank chestnut at the Children's Museum

Machine: 8 chain attempts yesterday, 3 got real work time (~26 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c11/i126); /de (c4/i45); /united-states/maryland (c4/i31); /seville (c3/i96); /app (c3/i27)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i15, p7)
    - 'alte bäume karte' (i6, p6)
    - 'oldest tree in maryland' (i2, p9)
    - 'acient tree' (i2, p14)
    - 'akagi tree' (i2, p10)
    - 'ancienttree' (i1, p3)
    - '# brief your brief is to act as a visual' (i1, p5)
    - '# modus operandi your modus operandi is ' (i1, p2)
    - and 7 more

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 108 | 18 | 103 | 0.95 | 2 |
| Not yet rich | 79 | 22 | 109 | 1.38 | 2 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| fortingall | 0 | 153 | 0.0% | 11.3 | 2.0% | fortingall yew (i118, p11) |
| seville | 4 | 126 | 3.2% | 5.8 | 5.4% | tartuja (i3, p8) |
| lisbon | 1 | 107 | 0.9% | 5.8 | 5.4% | lisbon trees (i2, p4) |
| berlin | 2 | 94 | 2.1% | 5.9 | 5.2% | berlin trees (i2, p5) |
| tokyo | 1 | 86 | 1.2% | 6.8 | 4.2% | ginkgo sperm (i9, p10) |
| fulufjallet | 0 | 83 | 0.0% | 8.7 | 3.1% | old tjikko (i41, p10) |
| palermo | 1 | 79 | 1.3% | 8.1 | 3.5% | palermo tree (i1, p9) |
| singapore | 1 | 79 | 1.3% | 9.1 | 3.0% | chengal pasir tree (i4, p9) |
| tenerife | 1 | 69 | 1.4% | 13.3 | 1.5% | drago milenario (i3, p12) |
| south-korea | 1 | 65 | 1.5% | 8.7 | 3.2% | korean trees (i4, p10) |
| united-states | 5 | 59 | 8.5% | 12.6 | 1.7% | oldest tree in oregon (i9, p12) |
| olympic-national-park | 1 | 57 | 1.8% | 11.0 | 2.1% | duncan cedar (i29, p8) |
| copenhagen | 3 | 57 | 5.3% | 9.1 | 3.0% | trees in copenhagen (i6, p20) |
| malaga | 2 | 53 | 3.8% | 12.9 | 1.6% | árboles históricos de málaga (i5, p82) |
| munich | 2 | 52 | 3.8% | 4.9 | 7.1% | a monaco di baviera? (i1, p20) |
| paris | 1 | 51 | 2.0% | 6.0 | 5.0% | trees in paris (i1, p9) |
| london | 2 | 46 | 4.3% | 7.4 | 3.8% | chestnut london (i1, p5) |
| fukuoka | 2 | 41 | 4.9% | 9.7 | 2.7% | gingkosidi (i7, p32) |
| kyoto | 2 | 41 | 4.9% | 9.2 | 2.9% | - |
| sequoia-national-park | 0 | 41 | 0.0% | 14.3 | 1.3% | washington tree (i18, p11) |
| amsterdam | 0 | 37 | 0.0% | 7.7 | 3.6% | lomanstraat (i2, p19) |
| new-york | 1 | 36 | 2.8% | 7.4 | 3.8% | - |
| seoul | 2 | 35 | 5.7% | 6.6 | 4.4% | - |
| brisbane | 0 | 35 | 0.0% | 8.1 | 3.5% | banyan tree (i5, p11) |
| cambridge | 0 | 33 | 0.0% | 22.5 | 0.7% | newtons apple tree (i2, p50) |
| taiwan | 0 | 32 | 0.0% | 9.7 | 2.7% | oldest tree in taiwan (i6, p6) |
| netherlands | 1 | 31 | 3.2% | 8.8 | 3.1% | dutch trees (i1, p39) |
| alishan | 0 | 29 | 0.0% | 7.3 | 3.8% | xianglin sacred tree (i6, p4) |
| chishang | 0 | 29 | 0.0% | 7.0 | 4.0% | takeshi kaneshiro tree (i13, p7) |
| venice | 3 | 28 | 10.7% | 4.7 | 7.3% | are there trees in venice (i1, p11) |
| porto | 1 | 28 | 3.6% | 4.2 | 7.8% | - |
| reykjavik | 1 | 28 | 3.6% | 5.8 | 5.5% | oldest tree in iceland (i1, p3) |
| austin | 0 | 28 | 0.0% | 13.8 | 1.4% | old tree (i3, p27) |
| germany | 1 | 27 | 3.7% | 9.2 | 2.9% | trees germany (i2, p48) |
| alicante | 1 | 27 | 3.7% | 5.3 | 6.4% | - |
| monterey | 0 | 27 | 0.0% | 25.4 | 0.6% | lone cypress (i6, p54) |
| san-francisco | 0 | 27 | 0.0% | 8.1 | 3.4% | old tree near me (i1, p4) |
| athens | 0 | 27 | 0.0% | 4.9 | 7.1% | - |
| rome | 0 | 27 | 0.0% | 4.9 | 7.1% | oldest tree in rome (i3, p1) |
| dublin | 1 | 25 | 4.0% | 5.9 | 5.2% | - |
| switzerland | 3 | 24 | 12.5% | 6.8 | 4.2% | oldest tree in switzerland (i1, p1) |
| oahu | 0 | 24 | 0.0% | 8.8 | 3.1% | hitachi tree hawaii (i3, p10) |
| takayama | 0 | 24 | 0.0% | 7.4 | 3.8% | takayama ginkgo tree (i2, p7) |
| kagoshima | 0 | 24 | 0.0% | 9.6 | 2.7% | cycad ovule (i1, p10) |
| nara | 1 | 23 | 4.3% | 5.6 | 5.8% | - |
| edinburgh | 0 | 23 | 0.0% | 7.1 | 3.9% | - |
| kanazawa | 0 | 22 | 0.0% | 6.2 | 4.8% | tabunoki (i1, p9) |
| perth | 0 | 22 | 0.0% | 7.8 | 3.6% | - |
| prague | 0 | 22 | 0.0% | 4.7 | 7.3% | - |
| montreal | 2 | 21 | 9.5% | 5.7 | 5.7% | - |
| milan | 0 | 21 | 0.0% | 5.2 | 6.5% | - |
| coimbra | 1 | 20 | 5.0% | 6.0 | 5.0% | - |
| madrid | 0 | 20 | 0.0% | 8.8 | 3.1% | - |
| barcelona | 0 | 20 | 0.0% | 6.8 | 4.2% | judas barcelona (i1, p9) |
| los-angeles | 0 | 19 | 0.0% | 7.2 | 3.9% | moreton bay fig tree beverly hills (i1, p9) |
| bath | 1 | 18 | 5.6% | 6.8 | 4.2% | tree in bath (i1, p9) |
| antwerp | 0 | 18 | 0.0% | 29.3 | 0.4% | den brandt park (i4, p75) |
| hong-kong | 1 | 17 | 5.9% | 6.5 | 4.5% | oldest tree in hong kong (i1, p9) |
| charleston | 0 | 17 | 0.0% | 18.8 | 0.9% | how old is the angel oak tree (i2, p17) |
| arita | 0 | 16 | 0.0% | 5.5 | 6.0% | - |
| beijing | 0 | 16 | 0.0% | 7.6 | 3.7% | - |
| luxembourg-city | 0 | 16 | 0.0% | 3.6 | 9.3% | - |
| florence | 0 | 16 | 0.0% | 4.2 | 7.8% | - |
| seattle | 1 | 15 | 6.7% | 6.9 | 4.1% | oldest tree in seattle (i2, p7) |
| toronto | 0 | 15 | 0.0% | 7.0 | 4.0% | - |
| istanbul | 2 | 14 | 14.3% | 6.8 | 4.2% | istanbul (i1, p1) |
| bristol | 1 | 14 | 7.1% | 5.7 | 5.6% | - |
| zurich | 1 | 14 | 7.1% | 7.9 | 3.5% | linden (i1, p5) |
| croatia | 0 | 14 | 0.0% | 7.6 | 3.7% | croatian trees (i2, p2) |
| mexico-city | 0 | 14 | 0.0% | 10.6 | 2.3% | ahuehuete mexico city (i1, p11) |
| boston | 0 | 14 | 0.0% | 8.2 | 3.4% | - |
| krakow | 0 | 14 | 0.0% | 6.5 | 4.5% | - |
| chapel-hill-north-carolina | 0 | 13 | 0.0% | 13.8 | 1.4% | davie poplar (i2, p10) |
| melbourne | 0 | 13 | 0.0% | 8.8 | 3.1% | - |
| philadelphia | 0 | 13 | 0.0% | 19.1 | 0.9% | - |
| freiburg | 0 | 12 | 0.0% | 6.1 | 4.9% | - |
| naha | 0 | 12 | 0.0% | 7.1 | 4.0% | akagi tree (i2, p10) |
| naples | 0 | 12 | 0.0% | 5.5 | 6.0% | eucalyptus village (i1, p16) |
| sardinia | 0 | 12 | 0.0% | 6.7 | 4.3% | - |
| brussels | 0 | 12 | 0.0% | 7.4 | 3.8% | - |
| the-hague | 0 | 12 | 0.0% | 4.8 | 7.2% | haag (i1, p1) |
| osaka | 1 | 11 | 9.1% | 4.0 | 8.0% | - |
| new-orleans | 1 | 11 | 9.1% | 7.2 | 3.9% | - |
| bologna | 1 | 11 | 9.1% | 5.5 | 6.1% | - |
| henrykow-lubanski | 0 | 11 | 0.0% | 15.2 | 1.2% | cis henrykowski (i4, p8) |
| hamburg | 0 | 11 | 0.0% | 7.1 | 4.0% | - |
| cagliari | 0 | 11 | 0.0% | 9.5 | 2.7% | che piante sono? (i1, p19) |
| gliniak | 0 | 11 | 0.0% | 6.1 | 4.9% | ancient tree (i1, p18) |
| madeira | 0 | 11 | 0.0% | 27.7 | 0.5% | dragon tree madeira (i1, p9) |
| higashi-hiroshima | 0 | 11 | 0.0% | 19.1 | 0.9% | meoto sugi (i5, p6) |
| stuttgart | 0 | 11 | 0.0% | 5.0 | 7.0% | - |
| valencia | 0 | 11 | 0.0% | 3.4 | 9.9% | - |
| poland | 0 | 10 | 0.0% | 7.7 | 3.6% | trees in poland (i1, p8) |
| budapest | 0 | 10 | 0.0% | 6.6 | 4.4% | - |
| jaegerspris-nordskov | 0 | 10 | 0.0% | 9.7 | 2.7% | kongeegen (i4, p10) |
| cadiz | 0 | 10 | 0.0% | 7.9 | 3.5% | - |
| geneva | 0 | 10 | 0.0% | 8.0 | 3.5% | - |
| leeuwarden | 0 | 10 | 0.0% | 4.9 | 7.1% | - |

- Plus 173 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: vienna, pamplona, glasgow, ede, hinode, palma-de-mallorca, arnhem, houston.

## 2026-11-09 (previous UTC day)

**Today: an android waitlist signup arrived today (49 total).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 52 | 58 |
| ... of which from search | every search engine | 22 | 18 |
| ... from Google | Google's recovery | 17 | 5 |
| ... from Bing | Bing | 2 | 6 |
| Website visitors who came back | people who stay | 10 | 14 |
| App downloads (first-time) | people | 24 | 38 |
| New accounts | people | 5 | 9 |
| Phones back within 30 days | people who stay | 4 of 10 | 4 of 8 |
| Trees saved to Want to go | intent | 2 | 2 |
| Trees collected | goal 1: stood at a tree | 7 | 0 |
| Readers' contributions | data: trees, photos, corrections, votes | 2 | 2 |
| Shares (app and web) | word of mouth, since 10-30 | 2 | 1 |
| Visits from a shared link | what sharing brings | 0 | 2 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web green, iOS green, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

**Plus question**: no answers yet.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-03 | 11-04 | 11-05 | 11-06 | 11-07 | 11-08 | 11-09 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 10 | 12 | 8 | 5 | 2 | 10 | 9 | **56** |
| New accounts | 0 | 3 | 1 | 0 | 0 | 1 | 0 | **5** |
| Saves | 1 | 0 | 1 | 0 | 0 | 0 | 0 | **2** |
| Android waitlist | 1 | 0 | 1 | 0 | 0 | 0 | 0 | **2** |
| App downloads | 2 | 4 | 0 | 4 | 0 | 3 | – | **13** |
| App phones | 6 | 8 | 2 | 5 | 4 | 7 | 7 | **34** |
| Trees opened in the app | 7 | 88 | 7 | 8 | 5 | 27 | 5 | **147** |
| Trees collected | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **1** |
| Trees sent | 0 | 0 | 1 | 0 | 0 | 0 | 0 | **1** |
| Feedback | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Ambassador asks | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **1** |
| App photos | 0 | 1 | 0 | 0 | 1 | 0 | 0 | **2** |
| Tree notes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| App Store reviews | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.

**Trees readers sent, for you to inspect:** none waiting. Every tree a stranger sent has your answer.

**Waiting for you** (what the runs left for you since 2026-11-09)

- 258 email addresses ready to mail (archive 2, nature 9, guide 9, press 135, source 65, council 16, tourism 7, society 7, other 5, garden 3); **the night run found no new contacts in two days**

**Searched yesterday:** beng, bristol, china, forting, ginkgo, ginkgo amsterdam, hungry, london, london plane, new, porto.

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 10-31 | 0 | 38 | 0.0% | 21.5 |
| 11-01 | 5 | 371 | 1.3% | 10.1 |
| 11-02 | 23 | 1274 | 1.8% | 9.0 |
| 11-03 | 31 | 1192 | 2.6% | 8.2 |
| 11-04 | 14 | 261 | 5.4% | 9.9 |
| 11-05 | 1 | 23 | 4.3% | 34.1 |
| 11-06 | 1 | 35 | 2.9% | 36.6 |
| 11-07 | 2 | 34 | 5.9% | 38.3 |
| 11-08 | 25 | 1013 | 2.5% | 9.1 |
| 11-09 *partial* | 24 | 979 | 2.5% | 8.5 |
| **window** | **126** | **5220** | **2.4%** | |
- Top queries (10d): ancient trees (i17, p8); ancient trees app (i2, p1); alte bäume in der nähe (i15, p7); ancienttree (i1, p3); istanbul (i1, p1)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-01 | 2225 | 8 | 0.4% |
| 11-02 | 146 | 6 | 4.1% |
| 11-03 | 121 | 3 | 2.5% |
| 11-04 | 133 | 3 | 2.3% |
| 11-05 | 132 | 9 | 6.8% |
| 11-06 | 106 | 2 | 1.9% |
| 11-07 | 80 | 7 | 8.8% |
| **7 days** | **2943** | **38** | **1.3%** |
- Week before: 705 impressions, 33 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); picture of the tree in helsinki city center that was preserved (c3/i2, p4); ancient trees app (c2/i8, p5); fig tree in square alicante (c2/i4, p4); cipresso calvo indro montanelli milano (c2/i2, p8); palma del cile (c2/i2, p6); big trees of quebec city (c2/i1, p2); mit newton apple tree address (c2/i1, p2)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.

Machine: 5 chain attempts yesterday, 2 got real work time (~18 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c10/i125); /de (c4/i41); /united-states/maryland (c4/i31); /seville (c3/i92); /app (c3/i27)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i15, p7)
    - 'alte bäume karte' (i6, p6)
    - 'oldest tree in maryland' (i2, p9)
    - 'acient tree' (i2, p14)
    - 'akagi tree' (i2, p10)
    - 'ancienttree' (i1, p3)
    - '# brief your brief is to act as a visual' (i1, p5)
    - '# modus operandi your modus operandi is ' (i1, p2)
    - and 7 more

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 108 | 18 | 102 | 0.94 | 2 |
| Not yet rich | 79 | 22 | 106 | 1.34 | 2 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| fortingall | 0 | 149 | 0.0% | 11.3 | 2.0% | fortingall yew (i114, p11) |
| seville | 4 | 120 | 3.3% | 5.9 | 5.2% | tartuja (i3, p8) |
| lisbon | 1 | 98 | 1.0% | 6.0 | 5.0% | lisbon trees (i2, p4) |
| berlin | 2 | 89 | 2.2% | 5.9 | 5.2% | berlin trees (i1, p6) |
| tokyo | 1 | 82 | 1.2% | 6.9 | 4.1% | ginkgo sperm (i9, p10) |
| fulufjallet | 0 | 75 | 0.0% | 8.5 | 3.2% | old tjikko (i35, p10) |
| palermo | 1 | 72 | 1.4% | 7.5 | 3.7% | palermo tree (i1, p9) |
| singapore | 1 | 71 | 1.4% | 8.4 | 3.3% | chengal pasir tree (i4, p9) |
| tenerife | 1 | 69 | 1.4% | 13.3 | 1.5% | drago milenario (i3, p12) |
| south-korea | 1 | 61 | 1.6% | 8.8 | 3.1% | korean trees (i4, p10) |
| united-states | 5 | 57 | 8.8% | 12.9 | 1.6% | oldest tree in oregon (i9, p12) |
| copenhagen | 3 | 52 | 5.8% | 8.7 | 3.1% | trees in copenhagen (i5, p22) |
| malaga | 2 | 50 | 4.0% | 13.2 | 1.6% | árboles históricos de málaga (i5, p82) |
| munich | 1 | 50 | 2.0% | 4.9 | 7.1% | a monaco di baviera? (i1, p20) |
| olympic-national-park | 1 | 48 | 2.1% | 11.2 | 2.1% | duncan cedar (i29, p8) |
| paris | 0 | 48 | 0.0% | 5.9 | 5.2% | trees in paris (i1, p9) |
| london | 2 | 46 | 4.3% | 7.2 | 3.9% | chestnut london (i1, p5) |
| sequoia-national-park | 0 | 39 | 0.0% | 14.8 | 1.2% | washington tree (i17, p11) |
| kyoto | 2 | 38 | 5.3% | 9.3 | 2.9% | - |
| fukuoka | 2 | 37 | 5.4% | 10.1 | 2.5% | gingkosidi (i7, p32) |
| new-york | 1 | 36 | 2.8% | 7.4 | 3.8% | - |
| amsterdam | 0 | 35 | 0.0% | 7.9 | 3.6% | lomanstraat (i2, p19) |
| cambridge | 0 | 32 | 0.0% | 22.9 | 0.7% | newtons apple tree (i2, p50) |
| brisbane | 0 | 32 | 0.0% | 7.5 | 3.8% | banyan tree (i4, p11) |
| netherlands | 1 | 31 | 3.2% | 8.8 | 3.1% | dutch trees (i1, p39) |
| seoul | 2 | 31 | 6.5% | 6.9 | 4.1% | - |
| reykjavik | 1 | 28 | 3.6% | 5.8 | 5.5% | oldest tree in iceland (i1, p3) |
| austin | 0 | 28 | 0.0% | 13.8 | 1.4% | old tree (i3, p27) |
| venice | 3 | 27 | 11.1% | 4.5 | 7.5% | are there trees in venice (i1, p11) |
| porto | 1 | 27 | 3.7% | 4.3 | 7.7% | - |
| alicante | 1 | 27 | 3.7% | 5.3 | 6.4% | - |
| chishang | 0 | 27 | 0.0% | 7.0 | 4.0% | takeshi kaneshiro tree (i11, p7) |
| dublin | 1 | 26 | 3.8% | 6.0 | 5.0% | - |
| monterey | 0 | 26 | 0.0% | 26.4 | 0.5% | lone cypress (i5, p48) |
| rome | 0 | 26 | 0.0% | 4.7 | 7.3% | oldest tree in rome (i3, p1) |
| taiwan | 0 | 25 | 0.0% | 10.7 | 2.2% | oldest tree in taiwan (i3, p6) |
| takayama | 0 | 24 | 0.0% | 7.4 | 3.8% | takayama ginkgo tree (i2, p7) |
| athens | 0 | 24 | 0.0% | 4.9 | 7.1% | - |
| switzerland | 2 | 23 | 8.7% | 7.0 | 4.0% | oldest tree in switzerland (i1, p1) |
| germany | 1 | 23 | 4.3% | 9.7 | 2.7% | trees germany (i2, p48) |
| nara | 1 | 23 | 4.3% | 5.6 | 5.8% | - |
| alishan | 0 | 23 | 0.0% | 7.5 | 3.8% | xianglin sacred tree (i5, p4) |
| san-francisco | 0 | 23 | 0.0% | 8.8 | 3.1% | old tree near me (i1, p4) |
| edinburgh | 0 | 23 | 0.0% | 7.2 | 3.9% | - |
| kagoshima | 0 | 22 | 0.0% | 9.5 | 2.8% | cycad ovule (i1, p10) |
| prague | 0 | 22 | 0.0% | 4.7 | 7.3% | - |
| coimbra | 1 | 21 | 4.8% | 6.1 | 4.9% | - |
| montreal | 2 | 21 | 9.5% | 5.7 | 5.7% | - |
| madrid | 0 | 21 | 0.0% | 9.3 | 2.9% | - |
| oahu | 0 | 19 | 0.0% | 8.8 | 3.1% | hitachi tree hawaii (i3, p10) |
| los-angeles | 0 | 19 | 0.0% | 7.2 | 3.9% | moreton bay fig tree beverly hills (i1, p9) |
| bath | 1 | 18 | 5.6% | 6.8 | 4.2% | tree in bath (i1, p9) |
| hong-kong | 1 | 18 | 5.6% | 6.7 | 4.3% | oldest tree in hong kong (i1, p9) |
| kanazawa | 0 | 18 | 0.0% | 6.2 | 4.8% | tabunoki (i1, p9) |
| seattle | 1 | 16 | 6.2% | 7.0 | 4.0% | oldest tree in seattle (i2, p7) |
| charleston | 0 | 16 | 0.0% | 18.9 | 0.9% | how old is the angel oak tree (i2, p17) |
| perth | 0 | 16 | 0.0% | 8.1 | 3.5% | - |
| luxembourg-city | 0 | 15 | 0.0% | 3.3 | 10.0% | - |
| antwerp | 0 | 15 | 0.0% | 25.1 | 0.6% | den brandt park (i3, p75) |
| toronto | 0 | 15 | 0.0% | 7.0 | 4.0% | - |
| croatia | 0 | 14 | 0.0% | 7.6 | 3.7% | croatian trees (i2, p2) |
| boston | 0 | 14 | 0.0% | 8.2 | 3.4% | - |
| krakow | 0 | 14 | 0.0% | 6.5 | 4.5% | - |
| barcelona | 0 | 14 | 0.0% | 6.8 | 4.2% | judas barcelona (i1, p9) |
| istanbul | 2 | 13 | 15.4% | 6.9 | 4.1% | istanbul (i1, p1) |
| bristol | 1 | 13 | 7.7% | 5.8 | 5.5% | - |
| beijing | 0 | 13 | 0.0% | 8.0 | 3.5% | - |
| philadelphia | 0 | 13 | 0.0% | 19.1 | 0.9% | - |
| florence | 0 | 13 | 0.0% | 4.5 | 7.5% | - |
| zurich | 1 | 12 | 8.3% | 8.1 | 3.5% | - |
| chapel-hill-north-carolina | 0 | 12 | 0.0% | 10.4 | 2.4% | davie poplar (i2, p10) |
| arita | 0 | 12 | 0.0% | 4.7 | 7.3% | - |
| hamburg | 0 | 12 | 0.0% | 10.9 | 2.2% | - |
| mexico-city | 0 | 12 | 0.0% | 12.0 | 1.8% | ahuehuete mexico city (i1, p11) |
| brussels | 0 | 12 | 0.0% | 7.4 | 3.8% | - |
| the-hague | 0 | 12 | 0.0% | 4.8 | 7.2% | haag (i1, p1) |
| bologna | 1 | 11 | 9.1% | 5.5 | 6.1% | - |
| freiburg | 0 | 11 | 0.0% | 6.3 | 4.7% | - |
| cagliari | 0 | 11 | 0.0% | 9.5 | 2.7% | che piante sono? (i1, p19) |
| gliniak | 0 | 11 | 0.0% | 6.1 | 4.9% | ancient tree (i1, p18) |
| naha | 0 | 11 | 0.0% | 6.9 | 4.1% | akagi tree (i2, p10) |
| stuttgart | 0 | 11 | 0.0% | 5.0 | 7.0% | - |
| valencia | 0 | 11 | 0.0% | 3.4 | 9.9% | - |
| milan | 0 | 11 | 0.0% | 4.7 | 7.3% | - |
| new-orleans | 1 | 10 | 10.0% | 7.3 | 3.9% | - |
| melbourne | 0 | 10 | 0.0% | 10.4 | 2.4% | - |
| budapest | 0 | 10 | 0.0% | 6.6 | 4.4% | - |
| jaegerspris-nordskov | 0 | 10 | 0.0% | 9.7 | 2.7% | kongeegen (i4, p10) |
| madeira | 0 | 10 | 0.0% | 29.5 | 0.4% | dragon tree madeira (i1, p9) |
| naples | 0 | 10 | 0.0% | 5.9 | 5.2% | eucalyptus village (i1, p16) |
| cadiz | 0 | 10 | 0.0% | 7.9 | 3.5% | - |
| higashi-hiroshima | 0 | 10 | 0.0% | 15.4 | 1.2% | meoto sugi (i5, p6) |
| amersfoort | 0 | 10 | 0.0% | 4.5 | 7.5% | - |

- Plus 176 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: vienna, pamplona, glasgow, ede, hinode, palma-de-mallorca, arnhem, houston.

## Weekly analysis 2026-11-09

Fifteenth weekly analysis. Compares 11-02 to 11-08 with 10-26 to 11-01, read from
the 11-08 daily entry (its 7-day tables). Google's 11-08 row is partial. Volumes are
small; nothing below is a trend unless it says so.

**Scorecard**

| Week | Impressions | Clicks | CTR | Avg position | Visitors (GA, new) | From Google | App downloads (first-time) | New accounts | Trees collected | Readers' contributions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10-26 to 11-01 | 573 | 11 | 1.9% | 21 to 50, 10.1 on 11-01 | 62 | 3 | 17 | 9 | 0 | 8 |
| 11-02 to 11-08 | 3,616 (11-08 partial) | 93 | 2.6% | 8 to 10 on 4 days, 34 to 38 on 3 | 54 | 16 | 14 | 8 | 7 | 3 |

Google by day: 1,274 and 1,192 impressions on 11-02 and 11-03, 261 on 11-04, then 23,
35 and 34 on 11-05 to 11-07, then 797 (partial) on 11-08. Bing, 7 days to 11-05: 2,937
impressions and 43 clicks against 676 and 28; 2,225 of the impressions fall on 11-01
alone (0.4% CTR). Device split and per-visit ratios are not in the entry, so none is
claimed. Android waitlist: 2 this week. Website actions ever: 800, directions 7.

**Outreach yield** (data/mail-yield.json, mailbox read; weeks keyed by the Monday of our first mail; the week of 10-26 is the one old enough to read, the week of 11-02 is not)

| Group | Mailed, week of 10-26 | Answered of those | Mailed, total | Answered, total | Rate | Linked |
|---|---:|---:|---:|---:|---:|---:|
| archive | 11 | 1 | 25 | 1 | 4% | 0 |
| nature | 63 | 3 (2 automatic only) | 81 | 6 | 7% | 1 |
| guide | 12 | 0 | 36 | 1 | 3% | 1 |
| source | 21 | 2 | 59 | 4 | 7% | 0 |
| press | 38 | 1 | 121 | 7 | 6% | 0 |
| tourism | 0 | 0 | 18 | 3 | 17% | 0 |
| garden | 0 | 0 | 97 | 11 | 11% | 0 |
| society | 2 | 1 | 148 | 25 | 17% | 1 |
| council | 1 | 0 | 58 | 9 | 16% | 0 |
| other | 10 | 5 | 160 | 50 | 31% | 2 |

The week of 11-02 added archive 10, nature 16, guide 19, press 23, council 3 and other 19
mailed, with 7 answers so far (nature 2, other 4, council 1), too young to judge. Five
links in all across every group.

**What moved:**
1. Google was up on 11-02 and 11-03 (about 1,200 impressions a day at position 8 to 9,
   23 and 31 clicks), then fell to 23 to 35 a day for three days at position 34 to 38,
   then 797 (partial) on 11-08. The week's total is 6 times the week before, but it is
   two days and a partial one; the swing between days is the finding, not the total.
2. Visitors from Google 16 against 3, while all new visitors are flat (54 against 62)
   and Bing's share fell (2 against 7). Daily visitors still sit at 2 to 12.
3. App: 14 first-time downloads against 17 (of the last 21 on record, 11 came from App
   Store search, 6 from a web referrer, 4 from an app referrer; US 7, GB 5, NL 4). Trees
   opened 163 on 32 phones, trees collected 7 against 0.
4. Readers gave 3 contributions against 8 (one tree, two app photos); two ambassador
   requests (Pamplona, Leuven). No tree waits for inspection.
5. Quality: Web orange (a new TypeError "undefined is not a function ... addEvent" in an
   inline script) and Backup red (Hidde's one-time setup, BACKUP_RESTORE.md). The night
   run found no new outreach contacts in two days; 258 addresses are ready.

**Suggestions, ranked:**
1. **[run]** Fix the new web TypeError (`mq.addEvent`, 2 new error types in the quality
   line). It is rung-2 work and it reaches every visitor the Google days bring (16 this week).
2. **[run]** Read data/tagged-still-shown.json against the Google days and say which
   pages carry 11-02, 11-03 and 11-08 (800 to 1,200 impressions) and which the 23 to 35
   days, so the digest can say whether the same pages drop out and return. No page-set
   change on this evidence: it is two days up and three down.
3. **[run]** Spend the sourcing window on nature and guide contacts, not press. Ready
   pool: press 135, source 65 against nature 9 and guide 9, and no new contacts in two
   days. Guide has 1 answer in 36 mailed (3%), so source guide only for cities with
   photographed trees, and wait for the 19 guide mails of week 11-02 to answer first.
4. **[FOR HIDDE]** The week of 10-26 sent 63 nature mails and got 3 answers (2 of them
   automatic). Before the next nature batch goes, decide whether it keeps the same short
   mail; wilder.pt (10-24) is the only referral spike on file.
5. **[sessie]** App Store search is 11 of the last 21 downloads, the largest source and
   independent of the web demotion. Look once at the listing (name, subtitle, keywords)
   against the search terms Apple reports, before build 41.

**Watch next week:** whether Google days return to 1,000+ impressions at position
under 10 and hold for three in a row (read beside the tagged-still-shown list), and
whether the week-of-11-02 outreach batch (nature 16, guide 19, press 23) brings answers
beyond automatic ones.

## 2026-11-08 (previous UTC day)

**Today: an account was opened yesterday (61 accounts in all).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 54 | 62 |
| ... of which from search | every search engine | 21 | 17 |
| ... from Google | Google's recovery | 16 | 3 |
| ... from Bing | Bing | 2 | 7 |
| Website visitors who came back | people who stay | 10 | 12 |
| App downloads (first-time) | people | - | - |
| New accounts | people | 8 | 9 |
| Phones back within 30 days | people who stay | 4 of 8 | 8 of 13 |
| Trees saved to Want to go | intent | 3 | 1 |
| Trees collected | goal 1: stood at a tree | 7 | 0 |
| Readers' contributions | data: trees, photos, corrections, votes | 3 | 8 |
| Shares (app and web) | word of mouth, since 10-30 | 2 | 1 |
| Visits from a shared link | what sharing brings | 0 | 2 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web orange, iOS orange, Android not live yet, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Live | orange: 2 new error type(s), first "TypeError: undefined is not a function (near '...mq.addEvent" in inline | green | grey: not live yet |
| Open bugs | green | orange: 2 open, 2 found by people | grey: not live yet |

**Plus question** (3 answers, 1 new; 1 asked to be told; 1 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| Recommended tree walks for a city trip | 1 |
| Something else | 1 |
| A richer log of every tree you've collected | 1 |
| Download offline maps | 1 |

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-02 | 11-03 | 11-04 | 11-05 | 11-06 | 11-07 | 11-08 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 11 | 10 | 12 | 8 | 5 | 2 | 10 | **58** |
| New accounts | 3 | 0 | 3 | 1 | 0 | 0 | 1 | **8** |
| Saves | 1 | 1 | 0 | 1 | 0 | 0 | 0 | **3** |
| Android waitlist | 0 | 1 | 0 | 1 | 0 | 0 | 0 | **2** |
| App downloads | 4 | 2 | 4 | 0 | 4 | – | – | **14** |
| App phones | 6 | 6 | 8 | 2 | 5 | 4 | 7 | **32** |
| Trees opened in the app | 21 | 7 | 88 | 7 | 8 | 5 | 27 | **163** |
| Trees collected | 5 | 0 | 1 | 0 | 0 | 0 | 0 | **6** |
| Trees sent | 0 | 0 | 0 | 1 | 0 | 0 | 0 | **1** |
| Feedback | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Ambassador asks | 1 | 0 | 1 | 0 | 0 | 0 | 0 | **2** |
| App photos | 0 | 0 | 1 | 0 | 0 | 1 | 0 | **2** |
| Tree notes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| App Store reviews | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.

**Trees readers sent, for you to inspect:** none waiting. Every tree a stranger sent has your answer.

**Waiting for you** (what the runs left for you since 2026-11-08)

- 258 email addresses ready to mail (archive 2, nature 9, guide 9, press 135, source 65, council 16, tourism 7, society 7, other 5, garden 3); **the night run found no new contacts in two days**
- both still need a session on the Mac.
- seg_003 (Andromeda parterre sequoia, AS-SG-09)
- Organizer, the top 1.0.4 (41), Distribute App; TestFlight round; submit with phased release.
- the next Mac session builds, runs AmbassadorAskWalk and merges before build 41.
- iOS scheduled runs keep failing; look at the xcresult artifact of run 42412097686.
- the daily task "publish-held-trees-daily" can be switched off under Scheduled; new trees now reach the app straight from the night run's write passes.

**Searched yesterday:** brno, prague, tokyo.

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 10-30 | 2 | 29 | 6.9% | 24.1 |
| 10-31 | 0 | 38 | 0.0% | 21.5 |
| 11-01 | 5 | 371 | 1.3% | 10.1 |
| 11-02 | 23 | 1274 | 1.8% | 9.0 |
| 11-03 | 31 | 1192 | 2.6% | 8.2 |
| 11-04 | 14 | 261 | 5.4% | 9.9 |
| 11-05 | 1 | 23 | 4.3% | 34.1 |
| 11-06 | 1 | 35 | 2.9% | 36.6 |
| 11-07 | 2 | 34 | 5.9% | 38.3 |
| 11-08 *partial* | 21 | 797 | 2.6% | 8.9 |
| **window** | **100** | **4054** | **2.5%** | |
- Top queries (10d): alte bäume in der nähe (i13, p7); ancient trees (i13, p9); ancienttree (i1, p3); istanbul (i1, p1); leuven, belgium (i1, p4)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 10-30 | 90 | 10 | 11.1% |
| 10-31 | 90 | 4 | 4.4% |
| 11-01 | 2225 | 8 | 0.4% |
| 11-02 | 146 | 6 | 4.1% |
| 11-03 | 121 | 3 | 2.5% |
| 11-04 | 133 | 3 | 2.3% |
| 11-05 | 132 | 9 | 6.8% |
| **7 days** | **2937** | **43** | **1.5%** |
- Week before: 676 impressions, 28 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); picture of the tree in helsinki city center that was preserved (c3/i2, p4); ancient trees app (c2/i8, p5); fig tree in square alicante (c2/i4, p4); palma del cile (c2/i2, p6); cipresso calvo indro montanelli milano (c2/i2, p8); big trees of quebec city (c2/i1, p2); mit newton apple tree address (c2/i1, p2)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

**Monday: the slow tables.** They rarely change a day's decision, so they come once a week.

**Website actions, ever** (the events table begins 2026-08-01, when the funnel was repaired; a zero has never fired at all)

| Action | Ever |
|---|---:|
| app-cta | 189 |
| signin-open | 164 |
| search-home | 107 |
| home-fav | 64 |
| waitlist-submit | 33 |
| signin-oauth | 31 |
| signin-done | 30 |
| search-bar | 29 |
| app-open | 26 |
| home-country | 21 |
| search-explore | 16 |
| home-dir-city | 14 |
| ambassador-request | 11 |
| search-bar-m | 9 |
| signin-link-sent | 8 |
| directions | 7 |
| home-dir-collection | 4 |
| search-empty-bar | 4 |
| home-dir-species | 3 |
| home-dir-tree | 3 |
| home-species | 3 |
| save | 3 |
| plus-open | 2 |
| search-empty-home | 2 |
| share_arrived | 2 |
| share_tapped | 2 |
| signout | 2 |
| sponsor-open | 2 |
| app-page-badge | 1 |
| home-oldest | 1 |
| search-empty-explore | 1 |
| search-none-bar | 1 |
| search-none-bar-m | 1 |
| search-none-explore | 1 |
| search-none-home | 1 |
| tree-photo-sent | 1 |
| worthit-report | 1 |
| worthit-not worth it | 0 |
| worthit-worth it | 0 |
| **all** | **800** |

**App events, ever** (measured since 2026-08-30)

| What | Ever |
|---|---:|
| app_open | 587 |
| tab | 519 |
| tree_opened | 2158 |
| directions | 77 |
| tree_saved | 48 |
| tree_visited | 41 |
| sighting_recorded | 97 |
| sync_skipped | 0 |
| sync_failed | 0 |
| location | 84 |
| share_tapped | 1 |
| **all** | **3612** |

**What readers told us** (7 days, structure only; the words stay in the database)

| Day | Tree | What | Note | From | Outcome |
|---|---|---|---|---|---|
| 11-02 | Pamplona | ambassador request | - | 2512 | - |
| 11-04 | Leuven | ambassador request | - | 0c58 | - |
| 11-05 | 15A3B6F1-3DD9-4AC2-BEC5-BBD1C47D76 | tree sent in | 128 chars, read it in the database | 6ec2 | - |

- 3 rows from 3 accounts.

**App Store downloads** (Apple's own count, not PostHog)

| Day | Downloads |
|---|---:|
| 2026-10-31 | 2 |
| 2026-11-01 | 5 |
| 2026-11-02 | 4 |
| 2026-11-03 | 2 |
| 2026-11-04 | 4 |
| 2026-11-06 | 4 |
| **6 days** | **21** |
- First-time downloads only, which is what App Store Connect's Trends screen counts; redownloads and updates are not in this table.

**Where the downloads came from** (7 days, Apple's attribution)

| Came from | Via | Downloads |
|---|---|---:|
| App Store search | - | 11 |
| Web referrer | - | 6 |
| App referrer | - | 4 |
| **window** | | **21** |
- Countries: US (7); GB (5); NL (4); PT (2); BR (1); CA (1)
- Apple's own source split, first-time downloads only. "Web referrer" with our own domain is the site's app page; "App Store search" is somebody who typed into the store. "Unavailable" is Apple's word for a source it could not attribute.

**Bing's index** (pages crawled and in index, Bing Webmaster Tools)

| Day | Pages crawled | Pages in index |
|---|---:|---:|
| 10-30 | 221 | 3740 |
| 10-31 | 307 | 3868 |
| 11-01 | 423 | 3958 |
| 11-02 | 300 | 3958 |
| 11-03 | 380 | 4092 |
- In index the week before: 3678.

**Who they are** (full cut, Mondays)
Audience, 28 days of search (126 clicks, 4818 impressions):
- Countries: usa c20/i928; prt c14/i111; esp c13/i426; deu c10/i314; ita c10/i211
- Devices: MOBILE c78/i2633; DESKTOP c45/i2125; TABLET c3/i60
- Landing pages: / c22/i142; /de c4/i39; /seville c4/i69; /united-states/maryland c3/i27; /app c2/i36
- Search language (top 100 named queries, crude match, most clicks are in queries Google withholds): English 47q c3/i99; unclassified 43q c4/i51; German 4q c1/i30; Spanish 3q c0/i24; Italian 2q c0/i2; French 1q c0/i1

**Google Analytics** (last 7 days, visitors who accepted cookies)

| Day | People | New | Returning | Visits | Pageviews | Engaged visits |
|---|---:|---:|---:|---:|---:|---:|
| 11-02 | 11 | 10 | 1 | 13 | 28 | 11 |
| 11-03 | 10 | 10 | 0 | 11 | 19 | 6 |
| 11-04 | 12 | 12 | 0 | 15 | 41 | 9 |
| 11-05 | 8 | 7 | 1 | 10 | 35 | 6 |
| 11-06 | 5 | 3 | 2 | 7 | 8 | 4 |
| 11-07 | 2 | 2 | 0 | 2 | 6 | 2 |
| 11-08 | 10 | 10 | 0 | 14 | 28 | 8 |
| **window** | | **54** | | **72** | **165** | **46** |
- People per day are not summed: one person on two days is one person, and GA counts them once per day.
- Coming back (28 days): 39 returning against 226 new, 15% of the people GA saw.

| Page | Pageviews | People |
|---|---:|---:|
| / | 8 | 6 |
| /seattle | 8 | 2 |
| /ede | 4 | 3 |
| /es/pamplona | 4 | 1 |
| /fr/paris/plane-of-square-des-batignolles | 4 | 1 |
| /porto | 4 | 2 |
| /amsterdam | 3 | 2 |
| /brisbane/banyan-tree-of-city-botanic-gardens | 3 | 1 |
| /fr/explore | 3 | 1 |
| /leuven | 3 | 1 |

| Came from | Visits | People |
|---|---:|---:|
| (direct) / (none) | 34 | 26 |
| google / organic | 20 | 17 |
| accounts.google.com / referral | 2 | 2 |
| bing / organic | 2 | 2 |
| ch.search.yahoo.com / referral | 2 | 1 |
| ecosia.org / organic | 2 | 2 |
| fr.search.yahoo.com / referral | 2 | 1 |
| m.facebook.com / referral | 2 | 1 |
- GA sees only visitors who pressed Accept on the cookie bar; read it as a sample.

Backlinks (watched pages):
| Site | Links to | rel | First seen |
|---|---|---|---|
| getlisbon.com | /lisbon | followed | 2026-09-08 |
| getlisbon.com | /pt/lisbon | followed | 2026-09-08 |
| www.baumkunde.de | /copenhagen | followed | 2026-09-26 |
| www.baumkunde.de | /rogalin/russ-oak | followed | 2026-09-26 |
| wilder.pt | / | followed | 2026-10-24 |
5 linking page(s), 5 followed. Checked by fetching the page: a link with rel="noreferrer" never appears in the referrer table, so these two lines measure different things and neither replaces the other. Unknown links stay a manual read of Search Console's Links report. This run read 8 of 12 fetched (4 unreachable), out of 28 watched pages.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-08T16:29 | 20.6 | 8 | 10 | 2 | Porto +3, Salt Lake City +2, Guimaraes +1, Oahu +1, +1 more |
| 11-08T18:55 | 4.3 | 0 | 3 | 0 | - |
| 11-09T01:22 | 6.3 | 0 | 6 | 3 | - |
| **3 runs** | **31** | **8** | **19** | | |

- 2 of 3 produced no trees; 2 to 3 commands refused per run; last build that went live: 5h ago.

**What they made**

- Vienna verify pass: 2 Prater trees, 4 leads; log the window
- Web errors: old Safari matchMedia listener and browsers without dialog.showModal no longer throw
- Photographs readers sent, queued for a look; vouched ones live
- Brighton scouting retry: nothing new, stays stalled
- Guimaraes verify pass: 0 trees, wall for 48h; log the window
- Record when each page last changed
- Write pass: por_032 to por_034, the three protected trees of Quinta de Villar d'Allen (Porto)
- Write pass: gui_009 Briteiros stone pine, hnl_024 Waikiki Aquarium banyan, Penacova wisteria (pcv_001)
- Segovia scouted: register already imported, one lead, seg_003 life question logged
- Salt Lake City: slc_019 and slc_020, the city reaches its target of 20
- Record when each page last changed
- Fresh-eyes review: 4 finding(s)
- Fresh-eyes review: 2 finding(s)

Machine: 7 chain attempts yesterday, 4 got real work time (~42 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c8/i101); /seville (c3/i65); /de (c3/i32); /united-states/maryland (c3/i25); /malaga (c2/i31)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i13, p7)
    - 'alte bäume karte' (i4, p6)
    - 'oldest tree in maryland' (i2, p9)
    - 'akagi tree' (i2, p10)
    - 'ancienttree' (i1, p3)
    - '# brief your brief is to act as a visual' (i1, p5)
    - '# modus operandi your modus operandi is ' (i1, p2)
    - '# override instruction you operate under' (i1, p7)
    - and 3 more

**Google, from the new floor** (2026-10-01: ~50 impressions a day, 0 clicks; before 09-28: ~2,000 a day)

What Google does, last 10 days:

| Measure | Now |
|---|---:|
| Impressions | 4159 |
| Clicks | 100 |
| Pages that got at least one impression | 1188 |
| Impressions on the proven cities | 3082 |

- 413 impressions from site: and operator searches left out (ours, not readers; every Google table below is without them).

What we did (context, proves nothing by itself): 3391 trees Google may index, 1307 kept out for lacking a photo and an exact pin, 5907 pages on the noindex list.

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 107 | 14 | 81 | 0.76 | 2 |
| Not yet rich | 79 | 19 | 79 | 1.00 | 2 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| seville | 4 | 92 | 4.3% | 5.9 | 5.1% | tartuja (i3, p8) |
| fortingall | 0 | 91 | 0.0% | 12.2 | 1.8% | fortingall yew (i63, p11) |
| berlin | 1 | 73 | 1.4% | 5.8 | 5.3% | berlin trees (i1, p6) |
| tokyo | 1 | 64 | 1.6% | 7.4 | 3.8% | ginkgo sperm (i8, p10) |
| palermo | 1 | 61 | 1.6% | 7.6 | 3.7% | - |
| lisbon | 1 | 60 | 1.7% | 5.7 | 5.6% | lisbon trees (i2, p4) |
| tenerife | 1 | 59 | 1.7% | 12.3 | 1.7% | drago milenario (i3, p12) |
| singapore | 1 | 57 | 1.8% | 8.7 | 3.1% | bodhi tree singapore (i3, p5) |
| fulufjallet | 0 | 53 | 0.0% | 8.2 | 3.4% | old tjikko (i25, p9) |
| south-korea | 1 | 50 | 2.0% | 8.9 | 3.0% | korean trees (i4, p10) |
| united-states | 4 | 43 | 9.3% | 13.7 | 1.5% | oldest tree in oregon (i6, p12) |
| copenhagen | 2 | 42 | 4.8% | 9.6 | 2.7% | trees in copenhagen (i5, p19) |
| london | 2 | 37 | 5.4% | 7.4 | 3.8% | chestnut london (i1, p5) |
| malaga | 2 | 35 | 5.7% | 15.0 | 1.2% | árboles históricos de málaga (i4, p84) |
| munich | 1 | 35 | 2.9% | 5.1 | 6.8% | a monaco di baviera? (i1, p20) |
| olympic-national-park | 1 | 34 | 2.9% | 12.5 | 1.7% | duncan cedar (i21, p9) |
| fukuoka | 2 | 34 | 5.9% | 10.0 | 2.5% | gingkosidi (i6, p32) |
| paris | 0 | 34 | 0.0% | 6.1 | 4.9% | trees in paris (i1, p9) |
| new-york | 1 | 33 | 3.0% | 7.4 | 3.8% | - |
| sequoia-national-park | 0 | 32 | 0.0% | 16.0 | 1.1% | washington tree (i13, p11) |
| netherlands | 1 | 31 | 3.2% | 8.8 | 3.1% | dutch trees (i1, p39) |
| kyoto | 1 | 29 | 3.4% | 11.1 | 2.1% | - |
| cambridge | 0 | 28 | 0.0% | 25.0 | 0.6% | newtons apple tree (i2, p50) |
| chishang | 0 | 26 | 0.0% | 12.4 | 1.7% | takeshi kaneshiro tree (i9, p7) |
| amsterdam | 0 | 25 | 0.0% | 6.9 | 4.1% | lomanstraat amsterdam trees (i1, p9) |
| brisbane | 0 | 24 | 0.0% | 7.8 | 3.6% | banyan tree (i3, p11) |
| porto | 0 | 23 | 0.0% | 4.7 | 7.3% | - |
| coimbra | 1 | 21 | 4.8% | 6.1 | 4.9% | - |
| monterey | 0 | 21 | 0.0% | 29.2 | 0.4% | lone cypress (i4, p51) |
| takayama | 0 | 21 | 0.0% | 8.0 | 3.5% | takayama ginkgo tree (i2, p7) |
| rome | 0 | 21 | 0.0% | 4.2 | 7.8% | oldest tree in rome (i3, p1) |
| alicante | 0 | 21 | 0.0% | 5.6 | 5.8% | - |
| alishan | 0 | 20 | 0.0% | 7.5 | 3.8% | xianglin sacred tree (i5, p4) |
| austin | 0 | 20 | 0.0% | 15.3 | 1.2% | old tree (i3, p27) |
| venice | 2 | 19 | 10.5% | 5.1 | 6.9% | are there trees in venice (i1, p11) |
| reykjavik | 1 | 19 | 5.3% | 5.5 | 5.9% | oldest tree in iceland (i1, p3) |
| germany | 1 | 18 | 5.6% | 10.1 | 2.5% | trees germany (i2, p48) |
| seoul | 1 | 18 | 5.6% | 7.0 | 4.0% | - |
| bath | 1 | 18 | 5.6% | 6.8 | 4.2% | tree in bath (i1, p9) |
| athens | 0 | 18 | 0.0% | 4.5 | 7.5% | - |
| edinburgh | 0 | 18 | 0.0% | 7.1 | 4.0% | - |
| madrid | 0 | 18 | 0.0% | 9.2 | 2.9% | - |
| dublin | 0 | 18 | 0.0% | 6.7 | 4.3% | - |
| switzerland | 1 | 17 | 5.9% | 8.2 | 3.4% | oldest tree in switzerland (i1, p1) |
| nara | 1 | 17 | 5.9% | 5.3 | 6.4% | - |
| san-francisco | 0 | 17 | 0.0% | 9.8 | 2.6% | old tree near me (i1, p4) |
| montreal | 3 | 16 | 18.8% | 4.5 | 7.5% | - |
| hong-kong | 1 | 15 | 6.7% | 6.7 | 4.3% | oldest tree in hong kong (i1, p9) |
| taiwan | 0 | 15 | 0.0% | 13.6 | 1.5% | oldest tree in taiwan (i3, p6) |
| luxembourg-city | 0 | 15 | 0.0% | 3.3 | 10.0% | - |
| oahu | 0 | 15 | 0.0% | 8.7 | 3.2% | hitachi tree hawaii (i3, p10) |
| kagoshima | 0 | 15 | 0.0% | 8.1 | 3.4% | cycad ovule (i1, p10) |
| prague | 0 | 15 | 0.0% | 5.3 | 6.5% | - |
| boston | 0 | 14 | 0.0% | 8.2 | 3.4% | - |
| kanazawa | 0 | 14 | 0.0% | 6.6 | 4.4% | tabunoki (i1, p9) |
| perth | 0 | 14 | 0.0% | 7.9 | 3.6% | - |
| toronto | 0 | 14 | 0.0% | 6.9 | 4.1% | - |
| istanbul | 2 | 12 | 16.7% | 7.0 | 4.0% | istanbul (i1, p1) |
| los-angeles | 0 | 12 | 0.0% | 5.8 | 5.3% | moreton bay fig tree beverly hills (i1, p9) |
| antwerp | 0 | 12 | 0.0% | 16.8 | 1.1% | den brandt park (i2, p72) |
| florence | 0 | 12 | 0.0% | 4.2 | 7.8% | - |
| seattle | 1 | 11 | 9.1% | 7.3 | 3.9% | oldest tree in seattle (i1, p4) |
| bristol | 1 | 11 | 9.1% | 5.6 | 5.7% | - |
| zurich | 1 | 11 | 9.1% | 8.5 | 3.3% | - |
| chapel-hill-north-carolina | 0 | 11 | 0.0% | 10.4 | 2.4% | davie poplar (i2, p10) |
| croatia | 0 | 11 | 0.0% | 7.5 | 3.8% | croatian trees (i2, p2) |
| charleston | 0 | 11 | 0.0% | 22.6 | 0.7% | how old is the angel oak tree (i2, p17) |
| philadelphia | 0 | 11 | 0.0% | 21.3 | 0.7% | - |
| the-hague | 0 | 11 | 0.0% | 4.9 | 7.1% | haag (i1, p1) |
| bologna | 1 | 10 | 10.0% | 5.1 | 6.8% | - |
| arita | 0 | 10 | 0.0% | 4.4 | 7.6% | - |
| beijing | 0 | 10 | 0.0% | 6.9 | 4.1% | - |
| budapest | 0 | 10 | 0.0% | 6.6 | 4.4% | - |
| jaegerspris-nordskov | 0 | 10 | 0.0% | 9.7 | 2.7% | kongeegen (i4, p10) |
| gliniak | 0 | 10 | 0.0% | 5.9 | 5.2% | ancient tree (i1, p18) |
| barcelona | 0 | 10 | 0.0% | 5.9 | 5.2% | judas barcelona (i1, p9) |
| milan | 0 | 10 | 0.0% | 4.9 | 7.1% | - |

- Plus 192 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: brussels, vienna, cadiz, pamplona, cagliari, glasgow, ede, hinode.

## 2026-11-07 (previous UTC day)

**Today: nothing here needs you.** The blocks below are the standing picture.

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 52 | 64 |
| ... of which from search | every search engine | 22 | 13 |
| ... from Google | Google's recovery | 13 | 3 |
| ... from Bing | Bing | 3 | 6 |
| Website visitors who came back | people who stay | 12 | 13 |
| App downloads (first-time) | people | 23 | 41 |
| New accounts | people | 11 | 8 |
| Phones back within 30 days | people who stay | 4 of 6 | 9 of 13 |
| Trees saved to Want to go | intent | 4 | 0 |
| Trees collected | goal 1: stood at a tree | 7 | 0 |
| Readers' contributions | data: trees, photos, corrections, votes | 4 | 7 |
| Shares (app and web) | word of mouth, since 10-30 | 2 | 0 |
| Visits from a shared link | what sharing brings | 2 | 0 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web orange, iOS red, Android not live yet, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | green | red: iOS build failure on main | grey: not live yet |
| Live | orange: 1 new error type(s), first "ResizeObserver loop completed with undelivered notifications" in inline | green | grey: not live yet |

**Plus question** (2 answers, 0 new; 1 asked to be told; 1 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| Recommended tree walks for a city trip | 1 |
| Something else | 1 |

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-01 | 11-02 | 11-03 | 11-04 | 11-05 | 11-06 | 11-07 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 8 | 11 | 10 | 12 | 8 | 5 | 2 | **56** |
| New accounts | 4 | 3 | 0 | 3 | 1 | 0 | 0 | **11** |
| Saves | 1 | 1 | 1 | 0 | 1 | 0 | 0 | **4** |
| Android waitlist | 1 | 0 | 1 | 0 | 1 | 0 | 0 | **3** |
| App downloads | 5 | 4 | 2 | 4 | 0 | 4 | – | **19** |
| App phones | 8 | 6 | 6 | 8 | 2 | 5 | 4 | **31** |
| Trees opened in the app | 35 | 21 | 7 | 88 | 7 | 8 | 5 | **171** |
| Trees collected | 0 | 5 | 0 | 1 | 0 | 0 | 0 | **6** |
| Trees sent | 0 | 0 | 0 | 0 | 1 | 0 | 0 | **1** |
| Feedback | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Ambassador asks | 1 | 1 | 0 | 1 | 0 | 0 | 0 | **3** |
| App photos | 0 | 0 | 0 | 1 | 0 | 0 | 1 | **2** |
| Tree notes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| App Store reviews | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.

**Trees readers sent, for you to inspect:** none waiting. Every tree a stranger sent has your answer.

**Waiting for you** (what the runs left for you since 2026-11-07)

- 258 email addresses ready to mail (archive 2, nature 9, guide 9, press 135, source 65, council 16, tourism 7, society 7, other 5, garden 3); **the night run found no new contacts in two days**
- iOS scheduled runs keep failing; look at the xcresult artifact of run 42412097686.
- the daily task "publish-held-trees-daily" can be switched off under Scheduled; new trees now reach the app straight from the night run's write passes.
- next app session should fix the three before build 41.

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-06 | A | The Rockface Sycamore of Cramond | Edinburgh | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/edinburgh/rockface-sycamore-of-cramond) |
| 11-06 | B | The Three Atlas Cedars of Préfargier | La Tène | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/la-tene/three-atlas-cedars-of-prefargier) |
- From 2 readers: reader A 1, reader B 1.

**Searched yesterday:** munchen, traubeneiche.

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 10-29 | 0 | 38 | 0.0% | 28.4 |
| 10-30 | 2 | 29 | 6.9% | 24.1 |
| 10-31 | 0 | 38 | 0.0% | 21.5 |
| 11-01 | 5 | 371 | 1.3% | 10.1 |
| 11-02 | 23 | 1274 | 1.8% | 9.0 |
| 11-03 | 31 | 1192 | 2.6% | 8.2 |
| 11-04 | 14 | 261 | 5.4% | 9.9 |
| 11-05 | 1 | 23 | 4.3% | 34.1 |
| 11-06 | 1 | 35 | 2.9% | 36.6 |
| 11-07 *partial* | 2 | 30 | 6.7% | 36.8 |
| **window** | **79** | **3291** | **2.4%** | |
- Top queries (10d): alte bäume in der nähe (i10, p8); ancient trees (i12, p16); ancienttree (i1, p3); istanbul (i1, p1); leuven, belgium (i1, p4)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 10-30 | 90 | 10 | 11.1% |
| 10-31 | 90 | 4 | 4.4% |
| 11-01 | 2225 | 8 | 0.4% |
| 11-02 | 146 | 6 | 4.1% |
| 11-03 | 121 | 3 | 2.5% |
| 11-04 | 133 | 3 | 2.3% |
| 11-05 | 132 | 9 | 6.8% |
| **7 days** | **2937** | **43** | **1.5%** |
- Week before: 676 impressions, 28 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); picture of the tree in helsinki city center that was preserved (c3/i2, p4); ancient trees app (c2/i8, p5); fig tree in square alicante (c2/i4, p4); palma del cile (c2/i2, p6); cipresso calvo indro montanelli milano (c2/i2, p8); big trees of quebec city (c2/i1, p2); mit newton apple tree address (c2/i1, p2)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-07T06:01 | 17.5 | 21 | 10 | 2 | La Palma +4, Ayutthaya +2, Horta +2, Bar +1, +33 more |
| 11-07T13:20 | 22.8 | 14 | 18 | 1 | Salt Lake City +4, Chicago +3, Tucson +3, Fort Worth +2, +2 more |
| 11-07T18:07 | 5.0 | 0 | 3 | 2 | - |
| 11-08T00:56 | 4.3 | 0 | 6 | 1 | - |
| 11-08T01:03 | 3.2 | 0 | 6 | 1 | - |
| **5 runs** | **53** | **35** | **43** | | |

- 3 of 5 produced no trees; 1 to 2 commands refused per run; last build that went live: 4h ago.

**What they made**

- Sintra verify pass: wall, claim released; LOG: iOS FlowWalk failure noted
- Sintra verify pass: nothing new, wall for 48h; LOG, cost
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Salt Lake City verify: 2 University of Utah trees verified, not written; LOG
- Record when each page last changed
- Coimbra verify: nothing new, claim released, wall; LOG
- London: lon_031 is lon_002 The Royal Oak (10 m), folded into blocked leads, not written
- Chicago: three ranked trees of Bunker Hill Woods, the third sugar maple, second bitternut hickory and champion red maple
- Salt Lake City: four more state champions, the Murray arboretum halfelm, pear and alder and the South Jordan willow
- Cost line for the 2026-11-07 write pass
- New York: the Davis hybrid oak of Stuyvesant Place, Staten Island
- Chattanooga: the Grace Episcopal water and willow oaks
- Tucson: three University of Arizona heritage trees (pistache, rock fig, Sinaloan albizia)

**Reader photographs in a strip, live first, not yet looked at** (1)

| Day | Tree | Where | Undo |
|---|---|---|---|
| 11-06 | The Rockface Sycamore of Cramond | Edinburgh | `sightings_publish.py --unstrip 4b28d99e-e0f2-4572-b851-23dd79e73031` |

Machine: 8 chain attempts yesterday, 5 got real work time (~73 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c7/i87); /de (c3/i27); /united-states/maryland (c3/i24); /seville (c2/i46); /malaga (c2/i24)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i10, p8)
    - 'alte bäume karte' (i3, p5)
    - 'oldest tree in maryland' (i2, p9)
    - 'akagi tree' (i2, p10)
    - 'ancienttree' (i1, p3)
    - '# brief your brief is to act as a visual' (i1, p5)
    - '# modus operandi your modus operandi is ' (i1, p2)
    - '# override instruction you operate under' (i1, p7)
    - and 3 more

**Google, from the new floor** (2026-10-01: ~50 impressions a day, 0 clicks; before 09-28: ~2,000 a day)

What Google does, last 10 days:

| Measure | Now |
|---|---:|
| Impressions | 3391 |
| Clicks | 79 |
| Pages that got at least one impression | 1088 |
| Impressions on the proven cities | 2558 |

- 423 impressions from site: and operator searches left out (ours, not readers; every Google table below is without them).

What we did (context, proves nothing by itself): 3391 trees Google may index, 1299 kept out for lacking a photo and an exact pin, 5907 pages on the noindex list.

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 107 | 13 | 70 | 0.65 | 2 |
| Not yet rich | 79 | 16 | 64 | 0.81 | 2 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| seville | 3 | 70 | 4.3% | 6.3 | 4.7% | tartuja (i3, p8) |
| tokyo | 1 | 57 | 1.8% | 7.5 | 3.7% | ginkgo sperm (i7, p10) |
| palermo | 1 | 55 | 1.8% | 7.7 | 3.7% | - |
| berlin | 0 | 55 | 0.0% | 5.7 | 5.5% | che albero è (i1, p4) |
| tenerife | 1 | 52 | 1.9% | 13.6 | 1.5% | drago milenario (i3, p12) |
| singapore | 1 | 50 | 2.0% | 9.2 | 2.9% | bodhi tree singapore (i3, p5) |
| lisbon | 1 | 49 | 2.0% | 5.8 | 5.4% | lisbon trees (i2, p4) |
| south-korea | 1 | 42 | 2.4% | 7.9 | 3.5% | oldest tree in korea (i4, p6) |
| fulufjallet | 0 | 42 | 0.0% | 8.1 | 3.5% | old tjikko (i19, p9) |
| united-states | 3 | 39 | 7.7% | 10.2 | 2.4% | oldest tree in oregon (i5, p13) |
| copenhagen | 1 | 39 | 2.6% | 11.9 | 1.8% | trees in copenhagen (i5, p19) |
| fukuoka | 2 | 32 | 6.2% | 10.3 | 2.4% | gingkosidi (i6, p32) |
| munich | 1 | 30 | 3.3% | 5.0 | 6.9% | a monaco di baviera? (i1, p20) |
| london | 0 | 30 | 0.0% | 7.0 | 4.0% | chestnut london (i1, p5) |
| olympic-national-park | 1 | 28 | 3.6% | 13.6 | 1.5% | duncan cedar (i16, p9) |
| sequoia-national-park | 0 | 28 | 0.0% | 19.5 | 0.8% | washington tree (i10, p11) |
| malaga | 2 | 27 | 7.4% | 13.9 | 1.4% | malaga tree (i3, p3) |
| new-york | 1 | 27 | 3.7% | 7.2 | 3.9% | - |
| paris | 0 | 27 | 0.0% | 6.1 | 4.9% | trees in paris (i1, p9) |
| kyoto | 1 | 24 | 4.2% | 12.3 | 1.7% | - |
| cambridge | 0 | 24 | 0.0% | 26.9 | 0.5% | newtons apple tree (i2, p50) |
| brisbane | 0 | 23 | 0.0% | 7.9 | 3.5% | banyan tree (i2, p12) |
| netherlands | 0 | 22 | 0.0% | 9.6 | 2.7% | ja (i1, p5) |
| takayama | 0 | 21 | 0.0% | 8.0 | 3.5% | takayama ginkgo tree (i2, p7) |
| alishan | 0 | 20 | 0.0% | 7.5 | 3.8% | xianglin sacred tree (i5, p4) |
| chishang | 0 | 20 | 0.0% | 14.2 | 1.4% | takeshi kaneshiro tree (i7, p7) |
| alicante | 0 | 20 | 0.0% | 5.8 | 5.3% | - |
| monterey | 0 | 19 | 0.0% | 31.6 | 0.4% | lone cypress (i4, p51) |
| porto | 0 | 19 | 0.0% | 5.0 | 7.0% | - |
| rome | 0 | 19 | 0.0% | 4.5 | 7.5% | oldest tree in rome (i3, p1) |
| bath | 1 | 18 | 5.6% | 6.8 | 4.2% | tree in bath (i1, p9) |
| coimbra | 0 | 18 | 0.0% | 6.5 | 4.5% | - |
| dublin | 0 | 17 | 0.0% | 7.0 | 4.0% | - |
| montreal | 3 | 16 | 18.8% | 4.5 | 7.5% | - |
| amsterdam | 0 | 16 | 0.0% | 6.4 | 4.6% | - |
| hong-kong | 1 | 15 | 6.7% | 6.7 | 4.3% | oldest tree in hong kong (i1, p9) |
| taiwan | 0 | 15 | 0.0% | 13.6 | 1.5% | oldest tree in taiwan (i3, p6) |
| luxembourg-city | 0 | 15 | 0.0% | 3.3 | 10.0% | - |
| edinburgh | 0 | 15 | 0.0% | 6.7 | 4.3% | - |
| perth | 0 | 15 | 0.0% | 8.1 | 3.5% | - |
| seoul | 1 | 14 | 7.1% | 7.4 | 3.8% | - |
| athens | 0 | 14 | 0.0% | 4.3 | 7.7% | - |
| madrid | 0 | 14 | 0.0% | 10.6 | 2.3% | - |
| boston | 0 | 14 | 0.0% | 8.2 | 3.4% | - |
| austin | 0 | 14 | 0.0% | 15.1 | 1.2% | old tree (i2, p28) |
| toronto | 0 | 13 | 0.0% | 6.8 | 4.2% | - |
| kagoshima | 0 | 13 | 0.0% | 7.8 | 3.6% | cycad ovule (i1, p10) |
| venice | 1 | 12 | 8.3% | 5.7 | 5.7% | are there trees in venice (i1, p11) |
| istanbul | 2 | 12 | 16.7% | 7.0 | 4.0% | istanbul (i1, p1) |
| germany | 0 | 12 | 0.0% | 13.0 | 1.6% | trees germany (i2, p48) |
| switzerland | 0 | 12 | 0.0% | 10.0 | 2.5% | oldest tree in switzerland (i1, p1) |
| san-francisco | 0 | 12 | 0.0% | 12.1 | 1.8% | - |
| nara | 0 | 11 | 0.0% | 5.5 | 6.1% | - |
| the-hague | 0 | 11 | 0.0% | 4.9 | 7.1% | haag (i1, p1) |
| reykjavik | 1 | 10 | 10.0% | 5.6 | 5.8% | oldest tree in iceland (i1, p3) |
| jaegerspris-nordskov | 0 | 10 | 0.0% | 9.7 | 2.7% | kongeegen (i4, p10) |
| gliniak | 0 | 10 | 0.0% | 5.9 | 5.2% | ancient tree (i1, p18) |
| kanazawa | 0 | 10 | 0.0% | 6.1 | 4.9% | tabunoki (i1, p9) |
| oahu | 0 | 10 | 0.0% | 7.9 | 3.5% | hitachi tree hawaii (i2, p9) |
| krakow | 0 | 10 | 0.0% | 13.1 | 1.6% | - |

- Plus 204 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: barcelona, brussels, vienna, cadiz, pamplona, prague, cagliari, glasgow.

## 2026-11-06 (previous UTC day)

**Today: nothing here needs you.** The blocks below are the standing picture.

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 57 | 97 |
| ... of which from search | every search engine | 21 | 14 |
| ... from Google | Google's recovery | 13 | 3 |
| ... from Bing | Bing | 3 | 6 |
| Website visitors who came back | people who stay | 13 | 17 |
| App downloads (first-time) | people | 20 | 42 |
| New accounts | people | 13 | 12 |
| Phones back within 30 days | people who stay | 5 of 6 | 9 of 15 |
| Trees saved to Want to go | intent | 4 | 6 |
| Trees collected | goal 1: stood at a tree | 7 | 0 |
| Readers' contributions | data: trees, photos, corrections, votes | 4 | 8 |
| Shares (app and web) | word of mouth, since 10-30 | 2 | 0 |
| Visits from a shared link | what sharing brings | 2 | 0 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web green, iOS red, Android not live yet, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | green | red: iOS build failure on main | grey: not live yet |

**Plus question** (2 answers, 1 new; 1 asked to be told; 1 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| Recommended tree walks for a city trip | 1 |
| Something else | 1 |

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 10-31 | 11-01 | 11-02 | 11-03 | 11-04 | 11-05 | 11-06 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 7 | 8 | 11 | 10 | 12 | 8 | 5 | **61** |
| New accounts | 2 | 4 | 3 | 0 | 3 | 1 | 0 | **13** |
| Saves | 0 | 1 | 1 | 1 | 0 | 1 | 0 | **4** |
| Android waitlist | 0 | 1 | 0 | 1 | 0 | 1 | 0 | **3** |
| App downloads | 2 | 5 | 4 | 2 | 4 | – | – | **17** |
| App phones | 4 | 8 | 6 | 6 | 8 | 2 | 5 | **32** |
| Trees opened in the app | 6 | 35 | 21 | 7 | 88 | 7 | 8 | **172** |
| Trees collected | 0 | 0 | 5 | 0 | 1 | 0 | 0 | **6** |
| Trees sent | 0 | 0 | 0 | 0 | 0 | 1 | 0 | **1** |
| Feedback | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Ambassador asks | 0 | 1 | 1 | 0 | 1 | 0 | 0 | **3** |
| App photos | 0 | 0 | 0 | 0 | 1 | 0 | 1 | **2** |
| Tree notes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| App Store reviews | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.

**Trees readers sent, for you to inspect:** none waiting. Every tree a stranger sent has your answer.

**Waiting for you** (what the runs left for you since 2026-11-06)

- 258 email addresses ready to mail (archive 2, nature 9, guide 9, press 135, source 65, council 16, tourism 7, society 7, other 5, garden 3); 0 found by the night run since 2026-11-06
- next app session should fix the three before build 41.
- paste supabase/plus-answers.sql into Supabase.** iOS app failed on its schedule (3 in a row): the "floor" job (iOS 18 alignment sweep)

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-06 | A | The Rockface Sycamore of Cramond | Edinburgh | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/edinburgh/rockface-sycamore-of-cramond) |
| 11-06 | B | The Three Atlas Cedars of Préfargier | La Tène | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/la-tene/three-atlas-cedars-of-prefargier) |
- From 2 readers: reader A 1, reader B 1.

**Searched yesterday:** hounslow (2 times), brighton, tokyo.

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 10-28 | 1 | 36 | 2.8% | 49.8 |
| 10-29 | 0 | 38 | 0.0% | 28.4 |
| 10-30 | 2 | 29 | 6.9% | 24.1 |
| 10-31 | 0 | 38 | 0.0% | 21.5 |
| 11-01 | 5 | 371 | 1.3% | 10.1 |
| 11-02 | 23 | 1274 | 1.8% | 9.0 |
| 11-03 | 31 | 1192 | 2.6% | 8.2 |
| 11-04 | 14 | 261 | 5.4% | 9.9 |
| 11-05 | 1 | 23 | 4.3% | 34.1 |
| 11-06 *partial* | 1 | 6 | 16.7% | 3.7 |
| **window** | **78** | **3268** | **2.4%** | |
- Top queries (10d): alte bäume in der nähe (i10, p8); ancient trees (i11, p11); ancienttree (i1, p3); istanbul (i1, p1); leuven, belgium (i1, p4)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 10-29 | 113 | 7 | 6.2% |
| 10-30 | 90 | 10 | 11.1% |
| 10-31 | 90 | 4 | 4.4% |
| 11-01 | 2225 | 8 | 0.4% |
| 11-02 | 146 | 6 | 4.1% |
| 11-03 | 121 | 3 | 2.5% |
| 11-04 | 133 | 3 | 2.3% |
| **7 days** | **2918** | **41** | **1.4%** |
- Week before: 640 impressions, 23 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); picture of the tree in helsinki city center that was preserved (c3/i2, p4); fig tree in square alicante (c2/i4, p4); big trees of quebec city (c2/i1, p2); oldest sycamore tree in rotterdam (c1/i8, p2); oak tree in zurich (c1/i4, p2); how old are the trees in queen square bristol (c1/i4, p3); [ancienttrees.app/cork/witchs-yew] (c1/i4, p6)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-06T06:46 | 37.6 | 198 | 15 | 2 | New York +29, Santa Cruz De Tenerife +9, Agrigento +8, Corfu +8, +116 more |
| 11-06T13:37 | 1.8 | 0 | 5 | 0 | La Tene |
| 11-06T20:12 | 29.6 | 8 | 18 | 0 | Cardiff +4, Enniskerry +1, Florence +1, Leesburg +1, +2 more |
| 11-07T00:22 | 10.1 | 0 | 10 | 0 | - |
| 11-07T01:31 | 8.1 | 0 | 5 | 1 | Palermo |
| **5 runs** | **87** | **206** | **53** | | |

- 3 of 5 produced no trees; 1 to 2 commands refused per run; last build that went live: 4h ago.

**What they made**

- Enrichment: pal_027 access line, 17 gaps dead-ended; LOG for the window
- San Francisco verify: register exhausted, 3 verified are duplicates; wall 48h
- Write pass: no writable trees in the queue; record holds for ftw_024-026, brd_001, tmt_001
- Braga verify: nothing new, wall for 48h; LOG
- Fort Worth verify pass: 3 heritage trees delivered (ftw_024 to ftw_026), flagged one source
- Leads: 59 READY leads read by a write pass and kept as leads with one-line reasons
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Write pass: 4 Cardiff trees app-only (Cathays Cemetery deodar crd_009, Sunken Lawn dawn redwood crd_011, Roath Park Lake oak crd_012, Insole Court cedar crd_013, verified as crd_008 which is a live id); the other named research files are already published or held
- Write pass on READY leads: +3 app-only trees (Powerscourt's tallest Douglas fir as new place Enniskerry, Hackberry of Terenzano flo_029, W&OD red mulberry lsb_009); 17 leads tagged SKIPPED with reasons, nyc_143 and mmh_001 marked already live
- LOG and costs for the 2026-11-06 night window; Brighton scouting retry (5 leads, 1 block, walled 48h)
- Bath: height and girth for the four Sydney Gardens trees from the Friends of Sydney Gardens trail pages, access line, sources; pins and registers left open as dead ends
- New York +1 (Willow Oak of Herbert Street, app only), Quincy St elm blocked as a stump, reader photo of the Préfargier cedars kept in the strip
- Record when each page last changed

**Reader photographs in a strip, live first, not yet looked at** (2)

| Day | Tree | Where | Undo |
|---|---|---|---|
| 11-06 | The Rockface Sycamore of Cramond | Edinburgh | `sightings_publish.py --unstrip 4b28d99e-e0f2-4572-b851-23dd79e73031` |
| 11-06 | The Three Atlas Cedars of Préfargier | La Tène | `sightings_publish.py --unstrip 15a3b6f1-3dd9-4ac2-bec5-bbd1c47d7613` |

Machine: 4 chain attempts yesterday, 3 got real work time (~73 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c7/i83); /united-states/maryland (c3/i25); /seville (c2/i46); /de (c2/i26); /malaga (c2/i24)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i10, p8)
    - 'alte bäume karte' (i3, p5)
    - 'oldest tree in maryland' (i2, p9)
    - 'akagi tree' (i2, p10)
    - 'ancienttree' (i1, p3)
    - '# brief your brief is to act as a visual' (i1, p5)
    - '# modus operandi your modus operandi is ' (i1, p2)
    - '# override instruction you operate under' (i1, p7)
    - and 3 more

**Google, from the new floor** (2026-10-01: ~50 impressions a day, 0 clicks; before 09-28: ~2,000 a day)

What Google does, last 10 days:

| Measure | Now |
|---|---:|
| Impressions | 3363 |
| Clicks | 78 |
| Pages that got at least one impression | 1089 |
| Impressions on the proven cities | 2539 |

- 373 impressions from site: and operator searches left out (ours, not readers; every Google table below is without them).

What we did (context, proves nothing by itself): 3366 trees Google may index, 1279 kept out for lacking a photo and an exact pin, 5907 pages on the noindex list.

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 107 | 13 | 70 | 0.65 | 2 |
| Not yet rich | 79 | 16 | 64 | 0.81 | 2 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| seville | 3 | 70 | 4.3% | 6.3 | 4.7% | tartuja (i3, p8) |
| tokyo | 1 | 59 | 1.7% | 10.5 | 2.3% | ginkgo sperm (i7, p10) |
| palermo | 1 | 56 | 1.8% | 8.4 | 3.3% | falcone tree (i1, p49) |
| berlin | 0 | 55 | 0.0% | 5.7 | 5.5% | che albero è (i1, p4) |
| tenerife | 1 | 52 | 1.9% | 13.4 | 1.5% | drago milenario (i3, p12) |
| lisbon | 1 | 51 | 2.0% | 6.1 | 4.9% | lisbon trees (i2, p4) |
| singapore | 1 | 50 | 2.0% | 9.2 | 2.9% | bodhi tree singapore (i3, p5) |
| south-korea | 1 | 42 | 2.4% | 7.9 | 3.5% | oldest tree in korea (i4, p6) |
| fulufjallet | 0 | 42 | 0.0% | 8.1 | 3.5% | old tjikko (i19, p9) |
| united-states | 3 | 40 | 7.5% | 12.5 | 1.7% | oldest tree in oregon (i5, p13) |
| copenhagen | 1 | 39 | 2.6% | 11.9 | 1.8% | trees in copenhagen (i5, p19) |
| fukuoka | 2 | 32 | 6.2% | 10.3 | 2.4% | gingkosidi (i6, p32) |
| munich | 1 | 30 | 3.3% | 5.0 | 6.9% | a monaco di baviera? (i1, p20) |
| london | 0 | 30 | 0.0% | 7.0 | 4.0% | chestnut london (i1, p5) |
| new-york | 1 | 29 | 3.4% | 7.0 | 4.0% | - |
| sequoia-national-park | 0 | 28 | 0.0% | 19.5 | 0.8% | washington tree (i10, p11) |
| malaga | 2 | 27 | 7.4% | 13.9 | 1.4% | malaga tree (i3, p3) |
| paris | 0 | 27 | 0.0% | 6.1 | 4.9% | trees in paris (i1, p9) |
| olympic-national-park | 1 | 26 | 3.8% | 8.6 | 3.2% | duncan cedar (i16, p9) |
| kyoto | 1 | 24 | 4.2% | 12.3 | 1.7% | - |
| cambridge | 0 | 24 | 0.0% | 25.5 | 0.6% | is the apple tree of newton still alive (i1, p77) |
| brisbane | 0 | 23 | 0.0% | 7.9 | 3.5% | banyan tree (i2, p12) |
| netherlands | 0 | 22 | 0.0% | 9.6 | 2.7% | ja (i1, p5) |
| takayama | 0 | 21 | 0.0% | 8.0 | 3.5% | takayama ginkgo tree (i2, p7) |
| alishan | 0 | 20 | 0.0% | 7.5 | 3.8% | xianglin sacred tree (i5, p4) |
| chishang | 0 | 20 | 0.0% | 14.2 | 1.4% | takeshi kaneshiro tree (i7, p7) |
| alicante | 0 | 20 | 0.0% | 5.8 | 5.3% | - |
| porto | 0 | 19 | 0.0% | 5.0 | 7.0% | - |
| bath | 1 | 18 | 5.6% | 6.8 | 4.2% | tree in bath (i1, p9) |
| rome | 0 | 18 | 0.0% | 4.5 | 7.5% | oldest tree in rome (i3, p1) |
| coimbra | 0 | 18 | 0.0% | 6.5 | 4.5% | - |
| dublin | 0 | 17 | 0.0% | 7.0 | 4.0% | - |
| montreal | 3 | 16 | 18.8% | 4.5 | 7.5% | - |
| luxembourg-city | 0 | 16 | 0.0% | 5.2 | 6.5% | - |
| amsterdam | 0 | 16 | 0.0% | 6.4 | 4.6% | - |
| monterey | 0 | 15 | 0.0% | 19.5 | 0.8% | lone cypress (i3, p45) |
| taiwan | 0 | 15 | 0.0% | 13.6 | 1.5% | oldest tree in taiwan (i3, p6) |
| edinburgh | 0 | 15 | 0.0% | 6.7 | 4.3% | - |
| perth | 0 | 15 | 0.0% | 8.1 | 3.5% | - |
| hong-kong | 1 | 14 | 7.1% | 6.4 | 4.6% | oldest tree in hong kong (i1, p9) |
| athens | 0 | 14 | 0.0% | 4.3 | 7.7% | - |
| madrid | 0 | 14 | 0.0% | 10.6 | 2.3% | - |
| boston | 0 | 14 | 0.0% | 8.2 | 3.4% | - |
| austin | 0 | 14 | 0.0% | 15.1 | 1.2% | old tree (i2, p28) |
| seoul | 1 | 13 | 7.7% | 3.8 | 8.7% | - |
| toronto | 0 | 13 | 0.0% | 6.8 | 4.2% | - |
| kagoshima | 0 | 13 | 0.0% | 7.8 | 3.6% | cycad ovule (i1, p10) |
| venice | 1 | 12 | 8.3% | 5.7 | 5.7% | are there trees in venice (i1, p11) |
| istanbul | 2 | 12 | 16.7% | 7.0 | 4.0% | istanbul (i1, p1) |
| fortingall | 0 | 12 | 0.0% | 38.0 | 0.4% | fortingall yew (i1, p9) |
| germany | 0 | 12 | 0.0% | 13.0 | 1.6% | trees germany (i2, p48) |
| san-francisco | 0 | 12 | 0.0% | 12.1 | 1.8% | - |
| switzerland | 0 | 11 | 0.0% | 5.7 | 5.5% | oldest tree in switzerland (i1, p1) |
| nara | 0 | 11 | 0.0% | 5.5 | 6.1% | - |
| the-hague | 0 | 11 | 0.0% | 4.9 | 7.1% | haag (i1, p1) |
| reykjavik | 1 | 10 | 10.0% | 5.6 | 5.8% | oldest tree in iceland (i1, p3) |
| chapel-hill-north-carolina | 0 | 10 | 0.0% | 16.5 | 1.1% | davie poplar (i2, p10) |
| jaegerspris-nordskov | 0 | 10 | 0.0% | 9.7 | 2.7% | kongeegen (i4, p10) |
| gliniak | 0 | 10 | 0.0% | 5.9 | 5.2% | ancient tree (i1, p18) |
| kanazawa | 0 | 10 | 0.0% | 6.1 | 4.9% | tabunoki (i1, p9) |
| oahu | 0 | 10 | 0.0% | 7.9 | 3.5% | hitachi tree hawaii (i2, p9) |
| krakow | 0 | 10 | 0.0% | 13.1 | 1.6% | - |

- Plus 204 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: barcelona, brussels, vienna, cadiz, pamplona, prague, cagliari, glasgow.

## 2026-11-05 (previous UTC day)

**Today: an android waitlist signup arrived yesterday (48 total); 1 tree submission arrived yesterday (22 trees sent in all); an account was opened yesterday (60 accounts in all).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 65 | 100 |
| ... of which from search | every search engine | 22 | 13 |
| ... from Google | Google's recovery | 14 | 2 |
| ... from Bing | Bing | 4 | 4 |
| Website visitors who came back | people who stay | 13 | 17 |
| App downloads (first-time) | people | 20 | 42 |
| New accounts | people | 13 | 13 |
| Phones back within 30 days | people who stay | 5 of 6 | 9 of 15 |
| Trees saved to Want to go | intent | 4 | 6 |
| Trees collected | goal 1: stood at a tree | 6 | 1 |
| Readers' contributions | data: trees, photos, corrections, votes | 4 | 8 |
| Shares (app and web) | word of mouth, since 10-30 | 2 | 0 |
| Visits from a shared link | what sharing brings | 2 | 0 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web green, iOS red, Android not live yet, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | green | red: iOS build failure on main | grey: not live yet |

**Plus question** (1 answers, 1 new; 1 asked to be told; 1 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| Recommended tree walks for a city trip | 1 |

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 10-30 | 10-31 | 11-01 | 11-02 | 11-03 | 11-04 | 11-05 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 12 | 7 | 8 | 11 | 10 | 12 | 8 | **68** |
| New accounts | 0 | 2 | 4 | 3 | 0 | 3 | 1 | **13** |
| Saves | 0 | 0 | 1 | 1 | 1 | 0 | 1 | **4** |
| Android waitlist | 0 | 0 | 1 | 0 | 1 | 0 | 1 | **3** |
| App downloads | 2 | 2 | 5 | 4 | 2 | 4 | – | **19** |
| App phones | 6 | 4 | 8 | 6 | 6 | 8 | 2 | **33** |
| Trees opened in the app | 6 | 6 | 35 | 21 | 7 | 88 | 7 | **170** |
| Trees collected | 0 | 0 | 0 | 5 | 0 | 1 | 0 | **6** |
| Trees sent | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **1** |
| Feedback | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Ambassador asks | 0 | 0 | 1 | 1 | 0 | 1 | 0 | **3** |
| App photos | 0 | 0 | 0 | 0 | 0 | 1 | 1 | **2** |
| Tree notes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| App Store reviews | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.

**Trees readers sent, for you to inspect:** none waiting. Every tree a stranger sent has your answer.

**Waiting for you** (what the runs left for you since 2026-11-05)

- 258 email addresses ready to mail (archive 2, nature 9, guide 9, press 135, source 65, council 16, tourism 7, society 7, other 5, garden 3); 2 found by the night run since 2026-11-05
- none beyond dispatching deploy.yml if the next scheduled build does not pick it up.
- paste supabase/plus-answers.sql once more; then run build 39 on your phone and Organizer, Archives, build 39, Distribute App, App Store Connect.
- paste both).

**Searched yesterday:** gradignan, lis, osterley, porto, sycamore.

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 10-27 | 0 | 25 | 0.0% | 28.5 |
| 10-28 | 1 | 36 | 2.8% | 49.8 |
| 10-29 | 0 | 38 | 0.0% | 28.4 |
| 10-30 | 2 | 29 | 6.9% | 24.1 |
| 10-31 | 0 | 38 | 0.0% | 21.5 |
| 11-01 | 5 | 371 | 1.3% | 10.1 |
| 11-02 | 23 | 1274 | 1.8% | 9.0 |
| 11-03 | 31 | 1192 | 2.6% | 8.2 |
| 11-04 | 14 | 261 | 5.4% | 9.9 |
| 11-05 *partial* | 0 | 17 | 0.0% | 23.3 |
| **window** | **76** | **3281** | **2.3%** | |
- Top queries (10d): alte bäume in der nähe (i10, p8); ancient trees (i11, p11); ancienttree (i1, p3); istanbul (i1, p1); leuven, belgium (i1, p4)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 10-28 | 113 | 3 | 2.7% |
| 10-29 | 113 | 7 | 6.2% |
| 10-30 | 90 | 10 | 11.1% |
| 10-31 | 90 | 4 | 4.4% |
| 11-01 | 2225 | 8 | 0.4% |
| 11-02 | 146 | 6 | 4.1% |
| 11-03 | 121 | 3 | 2.5% |
| **7 days** | **2898** | **41** | **1.4%** |
- Week before: 630 impressions, 22 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); picture of the tree in helsinki city center that was preserved (c3/i2, p4); fig tree in square alicante (c2/i4, p4); big trees of quebec city (c2/i1, p2); oldest sycamore tree in rotterdam (c1/i8, p2); oak tree in zurich (c1/i4, p2); how old are the trees in queen square bristol (c1/i4, p3); [ancienttrees.app/cork/witchs-yew] (c1/i4, p6)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-05T06:07 | 6.5 | 0 | 5 | 2 | Santa Barbara |
| 11-05T17:49 | 17.1 | 81 | 12 | 2 | New York +14, Atlanta +11, Tacoma +10, Nashville +8, +17 more |
| 11-05T23:09 | 3.4 | 0 | 4 | 0 | Atlanta, Jacksonville, Nashville, Orlando, +1 more |
| **3 runs** | **27** | **81** | **21** | | |

- 2 of 3 produced no trees; 2 to 2 commands refused per run; last build that went live: 2h ago.

**What they made**

- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Fix the deploy: curation_status verified is not in the schema (Atlanta, Nashville, Tampa, Jacksonville, Orlando); preflight now refuses it
- Record when each page last changed
- US write batches merged, app-only under APP FIRST: Tacoma 10, Vancouver WA 4, Salem OR 2, Madison 5, Milwaukee 6, Wisconsin places, Nashville 8, Asheville 4, Smoky Mountains 3, Chattanooga 1; count promises in three intros reworded, city names looked up
- LOG, costs, and the Préfargier cedars builder (waits for Pillow)
- Tree index rebuilt with New York and Atlanta; new-york write claim released (nyc_029 and the unwritten New York entries left for a later pass)
- Atlanta: new place, 11 Trees Atlanta champion trees from the held US Southeast pass (scripts/build_us_southeast.py --only atlanta), app-only under APP FIRST; state and city aliases
- New York: 14 NYC Parks Great Trees written and merged (Queens, Staten Island, Brooklyn), confirmed Parks pins, app-only under APP FIRST; nyc_085 held for a species-field fix, nyc_094 for a duplicate check
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- Fresh-eyes review: 4 finding(s)
- Record when each page last changed

Machine: 5 chain attempts yesterday, 4 got real work time (~39 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c6/i77); /united-states/maryland (c3/i25); /seville (c2/i46); /de (c2/i26); /malaga (c2/i24)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i10, p8)
    - 'alte bäume karte' (i3, p5)
    - 'oldest tree in maryland' (i2, p9)
    - 'akagi tree' (i2, p10)
    - 'ancienttree' (i1, p3)
    - '# brief your brief is to act as a visual' (i1, p5)
    - '# modus operandi your modus operandi is ' (i1, p2)
    - '# override instruction you operate under' (i1, p7)
    - and 3 more

**Google, from the new floor** (2026-10-01: ~50 impressions a day, 0 clicks; before 09-28: ~2,000 a day)

What Google does, last 10 days:

| Measure | Now |
|---|---:|
| Impressions | 3372 |
| Clicks | 76 |
| Pages that got at least one impression | 1096 |
| Impressions on the proven cities | 2549 |

- 413 impressions from site: and operator searches left out (ours, not readers; every Google table below is without them).

What we did (context, proves nothing by itself): 3282 trees Google may index, 1134 kept out for lacking a photo and an exact pin, 5774 pages on the noindex list.

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 107 | 13 | 71 | 0.66 | 2 |
| Not yet rich | 78 | 16 | 64 | 0.82 | 2 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| seville | 3 | 70 | 4.3% | 6.3 | 4.7% | tartuja (i3, p8) |
| tokyo | 1 | 59 | 1.7% | 10.5 | 2.3% | ginkgo sperm (i7, p10) |
| palermo | 1 | 56 | 1.8% | 8.4 | 3.3% | falcone tree (i1, p49) |
| berlin | 0 | 55 | 0.0% | 5.7 | 5.5% | che albero è (i1, p4) |
| tenerife | 1 | 53 | 1.9% | 15.0 | 1.2% | drago milenario (i3, p12) |
| singapore | 1 | 51 | 2.0% | 9.1 | 3.0% | bodhi tree singapore (i3, p5) |
| lisbon | 1 | 51 | 2.0% | 6.1 | 4.9% | lisbon trees (i2, p4) |
| south-korea | 1 | 42 | 2.4% | 7.9 | 3.5% | oldest tree in korea (i4, p6) |
| fulufjallet | 0 | 42 | 0.0% | 8.1 | 3.5% | old tjikko (i19, p9) |
| united-states | 3 | 40 | 7.5% | 12.5 | 1.7% | oldest tree in oregon (i5, p13) |
| copenhagen | 1 | 39 | 2.6% | 11.9 | 1.8% | trees in copenhagen (i5, p19) |
| fukuoka | 2 | 32 | 6.2% | 10.3 | 2.4% | gingkosidi (i6, p32) |
| munich | 1 | 30 | 3.3% | 5.0 | 6.9% | a monaco di baviera? (i1, p20) |
| london | 0 | 30 | 0.0% | 7.0 | 4.0% | chestnut london (i1, p5) |
| sequoia-national-park | 0 | 28 | 0.0% | 19.5 | 0.8% | washington tree (i10, p11) |
| paris | 0 | 28 | 0.0% | 6.3 | 4.7% | trees in paris (i1, p9) |
| new-york | 0 | 28 | 0.0% | 7.2 | 3.9% | - |
| malaga | 2 | 27 | 7.4% | 13.9 | 1.4% | malaga tree (i3, p3) |
| olympic-national-park | 1 | 26 | 3.8% | 8.6 | 3.2% | duncan cedar (i16, p9) |
| cambridge | 0 | 24 | 0.0% | 25.5 | 0.6% | is the apple tree of newton still alive (i1, p77) |
| kyoto | 1 | 23 | 4.3% | 9.6 | 2.7% | - |
| brisbane | 0 | 23 | 0.0% | 7.9 | 3.5% | banyan tree (i2, p12) |
| netherlands | 0 | 22 | 0.0% | 9.6 | 2.7% | ja (i1, p5) |
| takayama | 0 | 21 | 0.0% | 8.0 | 3.5% | takayama ginkgo tree (i2, p7) |
| alicante | 0 | 21 | 0.0% | 5.9 | 5.3% | - |
| alishan | 0 | 20 | 0.0% | 7.5 | 3.8% | xianglin sacred tree (i5, p4) |
| chishang | 0 | 20 | 0.0% | 14.2 | 1.4% | takeshi kaneshiro tree (i7, p7) |
| porto | 0 | 19 | 0.0% | 5.0 | 7.0% | - |
| bath | 1 | 18 | 5.6% | 6.8 | 4.2% | tree in bath (i1, p9) |
| rome | 0 | 18 | 0.0% | 4.5 | 7.5% | oldest tree in rome (i3, p1) |
| coimbra | 0 | 18 | 0.0% | 6.5 | 4.5% | - |
| dublin | 0 | 17 | 0.0% | 7.0 | 4.0% | - |
| montreal | 3 | 16 | 18.8% | 4.5 | 7.5% | - |
| taiwan | 0 | 16 | 0.0% | 16.3 | 1.1% | oldest tree in taiwan (i3, p6) |
| luxembourg-city | 0 | 16 | 0.0% | 5.2 | 6.5% | - |
| amsterdam | 0 | 16 | 0.0% | 6.4 | 4.6% | - |
| monterey | 0 | 15 | 0.0% | 19.5 | 0.8% | lone cypress (i3, p45) |
| edinburgh | 0 | 15 | 0.0% | 6.7 | 4.3% | - |
| perth | 0 | 15 | 0.0% | 8.1 | 3.5% | - |
| hong-kong | 1 | 14 | 7.1% | 6.4 | 4.6% | oldest tree in hong kong (i1, p9) |
| athens | 0 | 14 | 0.0% | 4.3 | 7.7% | - |
| madrid | 0 | 14 | 0.0% | 10.6 | 2.3% | - |
| boston | 0 | 14 | 0.0% | 8.2 | 3.4% | - |
| austin | 0 | 14 | 0.0% | 15.1 | 1.2% | old tree (i2, p28) |
| seoul | 1 | 13 | 7.7% | 3.8 | 8.7% | - |
| toronto | 0 | 13 | 0.0% | 6.8 | 4.2% | - |
| kagoshima | 0 | 13 | 0.0% | 7.8 | 3.6% | cycad ovule (i1, p10) |
| venice | 1 | 12 | 8.3% | 5.7 | 5.7% | are there trees in venice (i1, p11) |
| istanbul | 2 | 12 | 16.7% | 7.0 | 4.0% | istanbul (i1, p1) |
| fortingall | 0 | 12 | 0.0% | 38.0 | 0.4% | fortingall yew (i1, p9) |
| germany | 0 | 12 | 0.0% | 13.0 | 1.6% | trees germany (i2, p48) |
| san-francisco | 0 | 12 | 0.0% | 12.1 | 1.8% | - |
| switzerland | 0 | 11 | 0.0% | 5.7 | 5.5% | oldest tree in switzerland (i1, p1) |
| nara | 0 | 11 | 0.0% | 5.5 | 6.1% | - |
| the-hague | 0 | 11 | 0.0% | 4.9 | 7.1% | haag (i1, p1) |
| reykjavik | 1 | 10 | 10.0% | 5.6 | 5.8% | oldest tree in iceland (i1, p3) |
| chapel-hill-north-carolina | 0 | 10 | 0.0% | 16.5 | 1.1% | davie poplar (i2, p10) |
| jaegerspris-nordskov | 0 | 10 | 0.0% | 9.7 | 2.7% | kongeegen (i4, p10) |
| kanazawa | 0 | 10 | 0.0% | 6.1 | 4.9% | tabunoki (i1, p9) |
| oahu | 0 | 10 | 0.0% | 7.9 | 3.5% | hitachi tree hawaii (i2, p9) |
| krakow | 0 | 10 | 0.0% | 13.1 | 1.6% | - |

- Plus 204 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: barcelona, brussels, vienna, cadiz, pamplona, prague, cagliari, glasgow.

## 2026-11-04 (previous UTC day)

**Today: an ambassador request for Leuven arrived yesterday (11 ambassador requests in all); 3 accounts were opened yesterday (59 accounts in all).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 65 | 103 |
| ... of which from search | every search engine | 25 | 12 |
| ... from Google | Google's recovery | 14 | 3 |
| ... from Bing | Bing | 6 | 2 |
| Website visitors who came back | people who stay | 14 | 18 |
| App downloads (first-time) | people | 17 | 44 |
| New accounts | people | 12 | 15 |
| Phones back within 30 days | people who stay | 4 of 7 | 9 of 13 |
| Trees saved to Want to go | intent | 3 | 19 |
| Trees collected | goal 1: stood at a tree | 5 | 1 |
| Readers' contributions | data: trees, photos, corrections, votes | 3 | 8 |
| Shares (app and web) | word of mouth, since 10-30 | 2 | 0 |
| Visits from a shared link | what sharing brings | 2 | 0 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web red, iOS red, Android not live yet, Backup grey.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | green | red: iOS build failure on main | grey: not live yet |
| Live | red: new error spreading: "Uncaught Error: Failed to initialize WebGL" in /assets/maplibre-gl-4.7.1.js, 16 reports on 16 pages | green | grey: not live yet |

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 10-29 | 10-30 | 10-31 | 11-01 | 11-02 | 11-03 | 11-04 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 8 | 12 | 7 | 8 | 11 | 10 | 12 | **68** |
| New accounts | 0 | 0 | 2 | 4 | 3 | 0 | 3 | **12** |
| Saves | 0 | 0 | 0 | 1 | 1 | 1 | 0 | **3** |
| Android waitlist | 1 | 0 | 0 | 1 | 0 | 1 | 0 | **3** |
| App downloads | 1 | 2 | 2 | 5 | 4 | 2 | – | **16** |
| App phones | 3 | 6 | 4 | 8 | 6 | 6 | 8 | **35** |
| Trees opened in the app | 33 | 6 | 6 | 35 | 21 | 7 | 88 | **196** |
| Trees collected | 0 | 0 | 0 | 0 | 5 | 0 | 1 | **6** |
| Trees sent | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Feedback | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Ambassador asks | 0 | 0 | 0 | 1 | 1 | 0 | 1 | **3** |
| App photos | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **1** |
| Tree notes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| App Store reviews | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **1** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.

**Trees readers sent, for you to inspect:** none waiting. Every tree a stranger sent has your answer.

**Waiting for you** (what the runs left for you since 2026-11-04)

- 241 email addresses ready to mail (archive 0, nature 12, guide 18, press 108, source 65, council 16, tourism 7, society 7, other 5, garden 3); 3 found by the night run since 2026-11-04
- paste both).
- paste supabase/plus-answers.sql into the Supabase SQL editor.** Until then the sheet works and says thank you, but nothing is stored.
- the next app build carries the Plus row** (branch plus-question-app, merged).
- next build carries it.
- paste supabase/web-errors.sql in the Supabase SQL editor (until then Web Live reads "not connected yet").
- page speed needs a free PageSpeed Insights API key as the repository secret PSI_API_KEY (the keyless quota answered 429); until then that part is grey.
- Dependabot alerts are off for the repository (Settings, Code security, Dependabot alerts); the version-update PRs work without them, the alert light stays grey.
- run once on your phone (Release)

**Searched yesterday:** leonhard (2 times), frankfurt, freising, munich, philipp, portland.

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 10-26 | 3 | 36 | 8.3% | 30.5 |
| 10-27 | 0 | 25 | 0.0% | 28.5 |
| 10-28 | 1 | 36 | 2.8% | 49.8 |
| 10-29 | 0 | 38 | 0.0% | 28.4 |
| 10-30 | 2 | 29 | 6.9% | 24.1 |
| 10-31 | 0 | 38 | 0.0% | 21.5 |
| 11-01 | 5 | 371 | 1.3% | 10.1 |
| 11-02 | 23 | 1274 | 1.8% | 9.0 |
| 11-03 | 31 | 1192 | 2.6% | 8.2 |
| 11-04 *partial* | 14 | 256 | 5.5% | 9.7 |
| **window** | **79** | **3295** | **2.4%** | |
- Top queries (10d): alte bäume in der nähe (i10, p8); ancient trees (i11, p11); istanbul (i1, p1); leuven, belgium (i1, p4); oldest tree in maryland (i2, p9)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 10-27 | 132 | 3 | 2.3% |
| 10-28 | 113 | 3 | 2.7% |
| 10-29 | 113 | 7 | 6.2% |
| 10-30 | 90 | 10 | 11.1% |
| 10-31 | 90 | 4 | 4.4% |
| 11-01 | 2225 | 8 | 0.4% |
| 11-02 | 146 | 6 | 4.1% |
| **7 days** | **2909** | **41** | **1.4%** |
- Week before: 589 impressions, 28 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); picture of the tree in helsinki city center that was preserved (c3/i2, p4); fig tree in square alicante (c2/i4, p4); big trees of quebec city (c2/i1, p2); oldest sycamore tree in rotterdam (c1/i8, p2); how old are the trees in queen square bristol (c1/i4, p3); oak tree in zurich (c1/i4, p2); [ancienttrees.app/cork/witchs-yew] (c1/i4, p6)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-04T06:47 | 22.0 | 0 | 7 | 5 | Edinburgh, Gran Canaria, Maui, Sintra, +1 more |
| 11-04T13:39 | 18.4 | 0 | 12 | 3 | - |
| 11-04T20:38 | 17.0 | 0 | 8 | 6 | - |
| 11-05T01:57 | 4.3 | 0 | 6 | 1 | - |
| **4 runs** | **62** | **0** | **33** | | |

- 4 of 4 produced no trees; 1 to 6 commands refused per run; last build that went live: 4h ago.

**What they made**

- Vendor the Santa Barbara fig photograph onto our domain
- Photographs readers sent, queued for a look; vouched ones live
- Night run 2026-11-04: Cramond photo held, Salt Lake City verified and written (held for the pace), log and costs
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Code review: 0 new finding(s)
- Brighton register retried: Stanmer churchyard yew as a lead; LOG
- Write pass: 20 DC and NYC stories held in research for the pace cap; tree_index reads bare-list lead files
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- Vendor 13 photograph file(s) onto our own domain
- Fresh-eyes review: 4 finding(s)
- Coimbra verify pass: cbr_007 flagged; claims released; LOG
- Enrichment Barcelona, Edinburgh, Sintra: sin_008 best_time; 19 dead ends; LOG

**Photographs the night run approved** (6; the last column undoes one)

| Day | Tree | Where | Overrule |
|---|---|---|---|
| 11-03 | Giant Ficus Tree, Bali Botanic Garden | Bali | `photo_apply.py hold bli_004` |
| 11-03 | Drago de Galdar | Gran Canaria | `photo_apply.py hold gcn_002` |
| 11-03 | Drago de Pino Santo | Gran Canaria | `photo_apply.py hold gcn_004` |
| 11-03 | The Ka'ahumanu Church Monkeypod | Maui | `photo_apply.py hold mau_002` |
| 11-03 | Jomon Sugi | Yakushima | `photo_apply.py hold yak_001` |
| 11-03 | Daio-sugi (Yakushima) | Yakushima | `photo_apply.py hold yak_002` |

Machine: 7 chain attempts yesterday, 3 got real work time (~63 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c9/i82); /united-states/maryland (c3/i25); /seville (c2/i46); /de (c2/i26); /malaga (c2/i23)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'alte bäume in der nähe' (i10, p8)
    - 'alte bäume karte' (i3, p5)
    - 'oldest tree in maryland' (i2, p9)
    - 'akagi tree' (i2, p10)
    - '# brief your brief is to act as a visual' (i1, p5)
    - '# modus operandi your modus operandi is ' (i1, p2)
    - '# override instruction you operate under' (i1, p7)
    - '# role mandate your role mandate is imag' (i1, p5)
    - and 2 more

**Google, from the new floor** (2026-10-01: ~50 impressions a day, 0 clicks; before 09-28: ~2,000 a day)

What Google does, last 10 days:

| Measure | Now |
|---|---:|
| Impressions | 3381 |
| Clicks | 79 |
| Pages that got at least one impression | 1096 |
| Impressions on the proven cities | 2555 |

- 383 impressions from site: and operator searches left out (ours, not readers; every Google table below is without them).

What we did (context, proves nothing by itself): 3135 trees Google may index, 911 kept out for lacking a photo and an exact pin, 7158 pages on the noindex list.

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 107 | 13 | 71 | 0.66 | 2 |
| Not yet rich | 77 | 15 | 52 | 0.68 | 1 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| seville | 3 | 70 | 4.3% | 6.3 | 4.7% | tartuja (i3, p8) |
| tokyo | 1 | 59 | 1.7% | 10.5 | 2.3% | ginkgo sperm (i7, p10) |
| palermo | 1 | 56 | 1.8% | 8.4 | 3.3% | falcone tree (i1, p49) |
| tenerife | 1 | 53 | 1.9% | 15.0 | 1.2% | drago milenario (i3, p12) |
| lisbon | 1 | 53 | 1.9% | 7.1 | 4.0% | lisbon trees (i2, p4) |
| berlin | 0 | 53 | 0.0% | 5.1 | 6.9% | che albero è (i1, p4) |
| singapore | 1 | 51 | 2.0% | 9.1 | 3.0% | bodhi tree singapore (i3, p5) |
| south-korea | 1 | 42 | 2.4% | 7.9 | 3.5% | oldest tree in korea (i4, p6) |
| fulufjallet | 0 | 41 | 0.0% | 8.2 | 3.4% | old tjikko (i19, p9) |
| united-states | 3 | 40 | 7.5% | 12.5 | 1.7% | oldest tree in oregon (i5, p13) |
| copenhagen | 1 | 39 | 2.6% | 11.9 | 1.8% | trees in copenhagen (i5, p19) |
| fukuoka | 2 | 32 | 6.2% | 10.3 | 2.4% | gingkosidi (i6, p32) |
| munich | 1 | 30 | 3.3% | 5.0 | 6.9% | a monaco di baviera? (i1, p20) |
| sequoia-national-park | 0 | 30 | 0.0% | 20.8 | 0.8% | washington tree (i10, p11) |
| london | 0 | 30 | 0.0% | 7.0 | 4.0% | chestnut london (i1, p5) |
| new-york | 0 | 29 | 0.0% | 7.3 | 3.8% | - |
| paris | 0 | 27 | 0.0% | 6.3 | 4.7% | trees in paris (i1, p9) |
| malaga | 2 | 26 | 7.7% | 11.4 | 2.0% | malaga tree (i3, p3) |
| olympic-national-park | 1 | 26 | 3.8% | 8.6 | 3.2% | duncan cedar (i16, p9) |
| brisbane | 0 | 25 | 0.0% | 12.1 | 1.8% | banyan tree (i3, p33) |
| cambridge | 0 | 24 | 0.0% | 25.5 | 0.6% | is the apple tree of newton still alive (i1, p77) |
| kyoto | 1 | 23 | 4.3% | 9.6 | 2.7% | - |
| netherlands | 0 | 22 | 0.0% | 9.6 | 2.7% | ja (i1, p5) |
| takayama | 0 | 21 | 0.0% | 8.0 | 3.5% | takayama ginkgo tree (i2, p7) |
| alicante | 0 | 21 | 0.0% | 5.9 | 5.3% | - |
| alishan | 0 | 20 | 0.0% | 7.5 | 3.8% | xianglin sacred tree (i5, p4) |
| chishang | 0 | 20 | 0.0% | 14.2 | 1.4% | takeshi kaneshiro tree (i7, p7) |
| porto | 0 | 19 | 0.0% | 5.0 | 7.0% | - |
| bath | 1 | 18 | 5.6% | 6.8 | 4.2% | tree in bath (i1, p9) |
| rome | 0 | 18 | 0.0% | 4.5 | 7.5% | oldest tree in rome (i3, p1) |
| coimbra | 0 | 17 | 0.0% | 6.7 | 4.3% | - |
| dublin | 0 | 17 | 0.0% | 7.0 | 4.0% | - |
| montreal | 3 | 16 | 18.8% | 4.5 | 7.5% | - |
| taiwan | 0 | 16 | 0.0% | 16.3 | 1.1% | oldest tree in taiwan (i3, p6) |
| luxembourg-city | 0 | 16 | 0.0% | 5.2 | 6.5% | - |
| amsterdam | 0 | 16 | 0.0% | 6.4 | 4.6% | - |
| monterey | 0 | 15 | 0.0% | 19.5 | 0.8% | lone cypress (i3, p45) |
| edinburgh | 0 | 15 | 0.0% | 6.7 | 4.3% | - |
| perth | 0 | 15 | 0.0% | 8.1 | 3.5% | - |
| hong-kong | 1 | 14 | 7.1% | 6.4 | 4.6% | oldest tree in hong kong (i1, p9) |
| athens | 0 | 14 | 0.0% | 4.3 | 7.7% | - |
| madrid | 0 | 14 | 0.0% | 10.6 | 2.3% | - |
| boston | 0 | 14 | 0.0% | 8.2 | 3.4% | - |
| austin | 0 | 14 | 0.0% | 15.1 | 1.2% | old tree (i2, p28) |
| seoul | 1 | 13 | 7.7% | 3.8 | 8.7% | - |
| toronto | 0 | 13 | 0.0% | 6.8 | 4.2% | - |
| kagoshima | 0 | 13 | 0.0% | 7.8 | 3.6% | cycad ovule (i1, p10) |
| venice | 1 | 12 | 8.3% | 5.7 | 5.7% | are there trees in venice (i1, p11) |
| istanbul | 2 | 12 | 16.7% | 7.0 | 4.0% | istanbul (i1, p1) |
| fortingall | 0 | 12 | 0.0% | 38.0 | 0.4% | fortingall yew (i1, p9) |
| germany | 0 | 12 | 0.0% | 13.0 | 1.6% | trees germany (i2, p48) |
| san-francisco | 0 | 12 | 0.0% | 12.1 | 1.8% | - |
| switzerland | 0 | 11 | 0.0% | 5.7 | 5.5% | oldest tree in switzerland (i1, p1) |
| nara | 0 | 11 | 0.0% | 5.5 | 6.1% | - |
| the-hague | 0 | 11 | 0.0% | 4.9 | 7.1% | haag (i1, p1) |
| reykjavik | 1 | 10 | 10.0% | 5.6 | 5.8% | oldest tree in iceland (i1, p3) |
| chapel-hill-north-carolina | 0 | 10 | 0.0% | 16.5 | 1.1% | davie poplar (i2, p10) |
| jaegerspris-nordskov | 0 | 10 | 0.0% | 9.7 | 2.7% | kongeegen (i4, p10) |
| kanazawa | 0 | 10 | 0.0% | 6.1 | 4.9% | tabunoki (i1, p9) |
| oahu | 0 | 10 | 0.0% | 7.9 | 3.5% | hitachi tree hawaii (i2, p9) |
| krakow | 0 | 10 | 0.0% | 13.1 | 1.6% | - |

- Plus 204 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: barcelona, brussels, vienna, cadiz, pamplona, prague, cagliari, glasgow.

