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
## 2026-11-24 (previous UTC day)

**Today: 76 android waitlist signups arrived yesterday (2276 total); 20 tree submissions and an ambassador request for Glasgow and an ambassador request for Rome and 5 feedback reports arrived yesterday (659 submissions of every kind in all); 74 accounts were opened yesterday (1090 accounts in all).**

**North star: 354 people have uploaded a tree or photo of their own (+147 this week); 57 of them did it on more than one day (+37).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 61 | 0 |
| ... of which from search | every search engine | 22 | 0 |
| ... from Google | Google's recovery | 21 | 0 |
| ... from Bing | Bing | 0 | 0 |
| Website visitors who came back | people who stay | 9 | 0 |
| App downloads (first-time) | people | 2130 | 5493 |
| New accounts | people | 356 | 673 |
| Phones back within 30 days | people who stay | 16 of 34 | 5 of 14 |
| Trees saved to Want to go | intent | 443 | 365 |
| Trees collected | goal 1: stood at a tree | 363 | 280 |
| Readers' contributions | data: trees, photos, corrections | 523 | 475 |
| Worth-it votes | one tap, not a contribution | 83 | 126 |
| Shares (app and web) | word of mouth, since 10-30 | 238 | 229 |
| Visits from a shared link | what sharing brings | 74 | 76 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web red, iOS orange, Android grey, Backup green.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | orange: 1 compliance point(s) wait for Hidde (data/compliance.json); 2 compliance fix(es) open | orange: 1 compliance point(s) wait for Hidde (data/compliance.json); 2 compliance fix(es) open | grey: no checks wired yet |
| Live | red: photographs look soft, oversized or broken on the live site (photos-live.yml; python3 scripts/photocheck.py --live names them) | green | grey: no checks wired yet |

**Plus question** (21 answers, 1 new; 5 asked to be told; 12 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| A richer log of every tree you've collected | 9 |
| Something else | 8 |
| Download offline maps | 7 |
| Recommended tree walks for a city trip | 5 |
| Seasonal alerts when trees are at their best | 4 |

**Fixed since 19 Nov: 6.**

| Day | Where | What was wrong | Found by | Test |
|---|---|---|---|---|
| 24 Nov | iPhone | A tapped pin's card would not swipe away: it needed half the card's height of drag; now 56 or a light flick (Material 3), iOS and Android | a person | no |
| 24 Nov | Android | Sign in with Google took the browser's account with no chooser; prompt=select_account on iOS, Android and web | a person | yes |
| 24 Nov | iPhone | Tree page Age field cut a thousands separator as a clause break: about 1,000 years showed as about 1 on 24 trees (report 1000138); Androi... | a person | yes |
| 24 Nov | iPhone | The country picked in the app was never saved: the apps' upsert was refused for an empty display_name (fixed server-side by supabase/flag... | a person | yes |
| 24 Nov | iPhone | A tree sent from the app with only further photographs (main photo empty) was never read by sightings_inbox, so no lead existed and it sa... | a person | yes |
| 22 Nov | iPhone | Edit profile put the saved country back after picking another (the .task on the Form re-ran when the Country list popped) | a person | yes |

**New ambassadors yesterday: 7.** Tonya R. (Olympic National Park); Eryl T. (Ardkinglas); Katharyn J. (Houston); Ged R. (Boston); a reader (Rome); a reader (Glasgow); Jakob G. (Girona). Each got the mail and the badge automatically; 54 ambassadors in all (`python3 scripts/ambassador.py --list`).

**Open for you** (1; everything else handled and recorded, 77 feedback in all)

| What | Why it waits | Summary |
|---|---|---|
| feedback 1603 | your call | Asks what the ambassador role involves before saying yes, no age known yet; suggested answer in drafts/reply-reader-1603-2026-11-24.md |

Reader judge: 109 agent minutes yesterday, 1001 in the last 7 days.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-18 | 11-19 | 11-20 | 11-21 | 11-22 | 11-23 | 11-24 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 0 | 0 | 0 | 0 | 0 | 0 | 61 | **61** |
| New accounts | 62 | 39 | 31 | 41 | 67 | 42 | 74 | **356** |
| Saves | 57 | 28 | 31 | 53 | 60 | 89 | 125 | **443** |
| Android waitlist | 61 | 22 | 16 | 21 | 103 | 35 | 76 | **334** |
| App downloads | 351 | 153 | 127 | 130 | 492 | 165 | – | **1418** |
| App deletions | 10 | 7 | 3 | 9 | 15 | 7 | – | **51** |
| App phones | 624 | 484 | 420 | 421 | 756 | 406 | 772 | **3134** |
| Trees opened in the app | 1104 | 865 | 598 | 843 | 1468 | 704 | 1407 | **6989** |
| Trees collected | 21 | 42 | 14 | 24 | 38 | 17 | 14 | **170** |
| Trees sent | 14 | 30 | 13 | 25 | 34 | 35 | 20 | **171** |
| Pin moved | 5 | 4 | 3 | 11 | 8 | 3 | 8 | **42** |
| Written feedback | 36 | 8 | 4 | 5 | 12 | 3 | 6 | **74** |
| Report on a tree | 1 | 6 | 5 | 1 | 3 | 3 | 3 | **22** |
| Worth-it votes | 16 | 15 | 9 | 8 | 16 | 10 | 9 | **83** |
| Ambassador asks | 0 | 5 | 1 | 1 | 0 | 2 | 2 | **11** |
| Website photos | 3 | 1 | 2 | 1 | 4 | 1 | 0 | **12** |
| iPhone photos | 41 | 47 | 32 | 46 | 66 | 55 | 38 | **325** |
| Android photos | 0 | 26 | 1 | 5 | 6 | 4 | 1 | **43** |
| Tree notes | 15 | 6 | 3 | 8 | 5 | 6 | 6 | **49** |
| Photo likes | 0 | 0 | 0 | 0 | 0 | 3 | 5 | **8** |
| App Store reviews | 0 | 1 | 0 | 0 | 0 | 1 | 0 | **2** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.
- App deletions count only phones that share analytics with developers, and Apple leaves out days too small to show: read it against the installs of the same day, not as a total.

**Trees readers sent, for you to inspect** (4 you have not looked at; ours left out)

| Judged | Reader | Tree | Where | Species | Their girth | Our verdict | Page |
|---|---|---|---|---|---:|---|---|
| 2026-11-24 | A | Roverella | - | Roverella | - | hold | - |
| 2026-11-24 | B | The Cedar of Piazza Bra (2 photos) | Verona | Cedar of Lebanon (Cedrus liban | - | hold | - |
| 2026-11-24 | B | - | Verona | - | - | hold | - |
| 2026-11-22 | C | The Oldest Plane Tree in Europe | Τσαγκαράδα | - | 1300 cm | hold | - |
- From 3 readers: reader B 2, reader A 1, reader C 1.
- Photographs and the readers' own words: `python3 scripts/inspect_readers.py` (a local page, never in this public file). Your answer goes in with `python3 scripts/judgement.py --feedback <id> "..."`.

**Waiting for you** (what the runs left for you since 2026-11-24)

- either let the strip show that file smaller or raise `SOFT_AT` a hair; one reader photo should not keep the light red.
- tick the trader declaration and Save, upload your ID, sign in to the Play Console app on an Android phone, verify the phone number once ID is approved.
- a reply to reader 1433** (Tsagarada, the snowy night photo)
- next build carries fix for AncientTrees+0x35fccc.
- the next build carries the fix for the "about 1" age on the tree page.
- dispatch Build and deploy once, or let the next knock do it, to confirm green.

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-23 | D | Paavola's Oak | Lohja | a reader's photograph, published | [live](https://ancienttrees.app/lohja/paavolas-oak) |
| 11-23 | E |  | ? | a reader's photograph, published | not live yet |
| 11-23 | F |  | ? | a reader's photograph, published | not live yet |
| 11-23 | G |  | ? | a reader's photograph, published | not live yet |
| 11-23 | H |  | ? | a reader's photograph, published | not live yet |
| 11-23 | I |  | ? | a reader's photograph, published | not live yet |
| 11-23 | J | Kett's Oak | Hethersett | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/hethersett/ketts-oak) |
| 11-23 | I |  | ? | a reader's photograph, published | not live yet |
| 11-23 | I |  | ? | a reader's photograph, published | not live yet |
| 11-23 | I |  | ? | a reader's photograph, published | not live yet |
| 11-23 | K |  | ? | a reader's photograph, published | not live yet |
| 11-23 | K |  | ? | a reader's photograph, published | not live yet |
| 11-23 | L |  | ? | a reader's photograph, published | not live yet |
| 11-23 | L |  | ? | a reader's photograph, published | not live yet |
| 11-23 | M | The Hackberry of the Parco degli Scipioni | Rome | a reader's photograph, published | [live](https://ancienttrees.app/rome/hackberry-of-the-parco-degli-scipioni) |
| 11-23 | N | The Chiswick House Cedars | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/chiswick-house-cedars) |
| 11-23 | O | The Tree House Rain Tree of the Netravati Promenade | Mangaluru | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mangaluru/tree-house-rain-tree-of-the-netravati-promenade) |
| 11-23 | P | The Moreton Bay Fig of Curtain Square | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/moreton-bay-fig-of-curtain-square) |
| 11-23 | M | The Hackberry of the Mura Latine | Rome | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/rome/hackberry-of-the-mura-latine) |
| 11-23 | G | Tāne Mahuta | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/tane-mahuta) |
| 11-23 | Q | The Plane of Largo Doutor Francisco Soveral | Setubal | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/setubal/plane-of-largo-doutor-francisco-soveral) |
| 11-23 | K | The Twisted Beech of Square des Arenes de Lutece | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/twisted-beech-of-square-des-arenes-de-lutece) |
| 11-23 | K | The Weeping Cedar of the Vallée-aux-Loups (Cèdre pleureur) | Chatenay-Malabry | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/chatenay-malabry/weeping-cedar-of-the-vallee-aux-loups-cedre-pleureur) |
| 11-23 | K | The Bur Oak by the Cuvier Gate | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/bur-oak-by-the-cuvier-gate) |
| 11-23 | R | The Ginkgo of Đardin | Split | a reader's photograph, published | [live](https://ancienttrees.app/split/ginkgo-of-dardin) |
| 11-23 | S | The Tortworth Chestnut | Tortworth | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tortworth/tortworth-chestnut) |
| 11-23 | S | The Tortworth Chestnut | Tortworth | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tortworth/tortworth-chestnut) |
| 11-23 | R | Mastrinka, the Olive of Kaštel Štafilić | Kaštela | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kastela/mastrinka-the-olive-of-kastel-stafilic) |
| 11-23 | R | Mastrinka, the Olive of Kaštel Štafilić | Kaštela | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kastela/mastrinka-the-olive-of-kastel-stafilic) |
| 11-23 | T | The Minster Yard Beech | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/minster-yard-beech) |
| 11-23 | T | The Minster London Plane | York | a reader's photograph, published | [live](https://ancienttrees.app/york/minster-london-plane) |
| 11-23 | K | The Tall Plane of the Jardin des Plantes | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/tall-plane-of-the-jardin-des-plantes) |
| 11-23 | K | The Large-leaved Lime of Rungis | Rungis | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/rungis/large-leaved-lime-of-rungis) |
| 11-23 | K |  | ? | a reader's photograph, published | not live yet |
| 11-23 | K |  | ? | a reader's photograph, published | not live yet |
| 11-23 | U |  | ? | a reader's photograph, published | not live yet |
| 11-23 | V |  | ? | a reader's photograph, published | not live yet |
| 11-23 | W | The Golden Ginkgo of Greenwich | London | a reader's photograph, published | [live](https://ancienttrees.app/london/golden-ginkgo-of-greenwich) |
| 11-23 | X | Tight Grove, University of New Mexico | Albuquerque | a reader's photograph, published | [live](https://ancienttrees.app/albuquerque/tight-grove-university-of-new-mexico) |
| 11-23 | Y |  | ? | a reader's photograph, published | not live yet |
| 11-23 | Y |  | ? | a reader's photograph, published | not live yet |
| 11-23 | Y |  | ? | a reader's photograph, published | not live yet |
| 11-23 | Y |  | ? | a reader's photograph, published | not live yet |
| 11-23 | Y |  | ? | a reader's photograph, published | not live yet |
| 11-23 | Y |  | ? | a reader's photograph, published | not live yet |
| 11-23 | Z |  | ? | a reader's photograph, published | not live yet |
| 11-23 | A1 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | B1 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | C1 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | D1 | The Oak of Clingoe Hill | Colchester | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/colchester/oak-of-clingoe-hill) |
| 11-23 | Y | The Many-Stemmed Beech of East Hampton | East Hampton | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/east-hampton/many-stemmed-beech-of-east-hampton) |
| 11-23 | E1 | The Laurel Hill Cutleaf Linden | Philadelphia | a reader's photograph, published | [live](https://ancienttrees.app/philadelphia/laurel-hill-cutleaf-linden) |
| 11-23 | E1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | F1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | G1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | H1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | C1 | Travilah Oak | Washington DC | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/washington-dc/travilah-oak) |
| 11-24 | D1 | The Cedar near Clingoe Hill | Colchester | a reader's photograph, published | [live](https://ancienttrees.app/colchester/cedar-near-clingoe-hill) |
| 11-24 | D1 | The Cedar near Clingoe Hill | Colchester | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/colchester/cedar-near-clingoe-hill) |
| 11-24 | I1 | The Plane of Agia Paraskevi | Tsagarada | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tsagarada/plane-of-agia-paraskevi) |
| 11-24 | I1 | The Plane of Agia Paraskevi | Tsagarada | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tsagarada/plane-of-agia-paraskevi) |
| 11-24 | J1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | K1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | M | The Cedar of Celimontana | Rome | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/rome/cedar-of-celimontana) |
| 11-24 | L1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | M1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | N1 | The Pohutukawa of Campo Santana | Lisbon | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/lisbon/pohutukawa-of-campo-santana) |
| 11-24 | O1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | P1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | Q1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | B | The Ginkgo of Piazza Indipendenza | Verona | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/verona/ginkgo-of-piazza-indipendenza) |
| 11-24 | B | The Ginkgo of Piazza Indipendenza | Verona | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/verona/ginkgo-of-piazza-indipendenza) |
| 11-24 | R1 | The Silver-Limbed Oak of Tranekær | Tranekær | a reader's photograph, published | [live](https://ancienttrees.app/tranekaer/silver-limbed-oak-of-tranekaer) |
| 11-24 | S1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | T1 | The Vondelpark Poplar | Amsterdam | a reader's photograph, published | [live](https://ancienttrees.app/amsterdam/vondelpark-poplar) |
| 11-24 | U1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | V1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | V1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | W1 | The Ficus of Piazza Marina | Palermo | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/palermo/ficus-of-piazza-marina) |
| 11-24 | X1 | The Olive Tree of Azoria (Kavousi) | Crete | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/crete/olive-tree-of-azoria-kavousi) |
| 11-24 | L1 | The Silk Mulberry of Ca' di David | Verona | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/verona/silk-mulberry-of-ca-di-david) |
| 11-24 | Y1 | Kirkstall Abbey ginkgo | Leeds | a reader's photograph, published | [live](https://ancienttrees.app/leeds/kirkstall-abbey-ginkgo) |
| 11-24 | T1 | The Vondelpark Poplar | Amsterdam | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/amsterdam/vondelpark-poplar) |
| 11-24 | Z1 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | A2 | El Árbol del Tule | Santa María del Tule | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/santa-maria-del-tule/el-arbol-del-tule) |
| 11-24 | B2 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | C2 | The Carolyn Black Tupelo | Madison | a reader's photograph, published | [live](https://ancienttrees.app/madison/carolyn-black-tupelo) |
| 11-25 | D2 | The Three Hundred Year Pine | Tokyo | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tokyo/three-hundred-year-pine) |
| 11-25 | C2 | The Carolyn Black Tupelo | Madison | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/madison/carolyn-black-tupelo) |
| 11-23 | E2 | The Ginkgo of Đardin | Split | a reader's correction changed the page | - |
| 11-23 | E1 | The Laurel Hill Cutleaf Linden | Philadelphia | a reader's correction changed the page | - |
| 11-24 | M1 | Zelkova serrata of Kanayama | Ota, Japan | a reader's tree changed the page | - |
- From 55 readers: reader K 9, reader Y 7, reader I 4, reader D1 3, reader E1 3, reader M 3, reader R 3, reader B 2, reader C1 2, reader C2 2, reader G 2, reader I1 2, reader L 2, reader L1 2, reader M1 2, reader S 2, reader T 2, reader T1 2, reader V1 2, reader A1 1, reader A2 1, reader B1 1, reader B2 1, reader D 1, reader D2 1, reader E 1, reader E2 1, reader F 1, reader F1 1, reader G1 1, reader H 1, reader H1 1, reader J 1, reader J1 1, reader K1 1, reader N 1, reader N1 1, reader O 1, reader O1 1, reader P 1, reader P1 1, reader Q 1, reader Q1 1, reader R1 1, reader S1 1, reader U 1, reader U1 1, reader V 1, reader W 1, reader W1 1, reader X 1, reader X1 1, reader Y1 1, reader Z 1, reader Z1 1.

**What was sent in, and what we decided**

| seen | what | where | size for its species | ours | Hidde |
|---|---|---|---|---|---|
| 2026-11-25 | The Carolyn Black Tupelo | Madison | - | reject | - |
| 2026-11-24 | Travilah Oak | Washington DC | - | hold | - |
| 2026-11-24 | Travilah Oak | Washington DC | - | hold | - |
| 2026-11-24 | Travilah Oak | Washington DC | - | hold | - |
| 2026-11-24 | Travilah Oak | Washington DC | - | hold | - |
| 2026-11-24 | The Silk Mulberry of Ca' di David | Verona | - | hold | - |
| 2026-11-24 | The Ficus of Piazza Marina | Palermo | - | hold | - |
| 2026-11-22 | a tree we do not map | Brussels | - | hold | - |
| 2026-11-20 | Tyler Arboretum Giant Sequoia | Media | - | lead | - |
| 2026-11-19 | The Ivy Elm of Park Oliwski | Gdansk | - | hold | - |
| 2026-11-19 | A tree I found | - | - | hold | - |
| 2026-11-19 | The Amur Cork Trees and Crimean Linden | Vilnius | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | lead | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | lead | - |

0 waiting for a verdict. Disagree with one and the rule changes: `python3 scripts/judgement.py --feedback <id> "..."`, and `--learn` prints every verdict he has overruled.

**Searched yesterday:** roma (7 times), rome (7 times), ita (5 times), milano (4 times), berlin (3 times), genova (3 times), ital (3 times), mil (3 times), mila (3 times), perugia (3 times), pisa (3 times), turin (3 times), vero (3 times), bologna (2 times), cag (2 times), italy (2 times), kobe (2 times), lampedusa (2 times), londra (2 times), mi (2 times).

**App crashes** (last 7 days, store builds; MetricKit, a sample)

| Crashes | Kind | Build | Where | Phones | Last | Fix |
|---:|---|---|---|---:|---|---|
| 1 | crash | 1.0.4 (41) | AncientTrees+0x35fccc | 1 | 2026-11-20 | fixed in build 42, waiting for release |
| 1 | hang | 1.0.4 (41) | AncientTrees+0x376463 | 1 | 2026-11-21 | none |

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 11-15 | 210 | 363 | 57.9% | 8.2 |
| 11-16 | 116 | 204 | 56.9% | 6.6 |
| 11-17 | 59 | 132 | 44.7% | 15.0 |
| 11-18 | 33 | 67 | 49.3% | 17.8 |
| 11-19 | 19 | 60 | 31.7% | 32.5 |
| 11-20 | 20 | 66 | 30.3% | 22.9 |
| 11-21 | 15 | 47 | 31.9% | 15.7 |
| 11-22 | 204 | 351 | 58.1% | 5.2 |
| 11-23 | 31 | 82 | 37.8% | 12.0 |
| 11-24 *partial* | 176 | 256 | 68.8% | 4.7 |
| **window** | **883** | **1628** | **54.2%** | |
- Top queries (10d): ancient trees app (i869, p1); ancient tree app (i8, p2); ancient trees (i16, p27); ancient tree (i20, p18); hidde burgmans (i3, p2)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-17 | 170 | 6 | 3.5% |
| 11-18 | 177 | 9 | 5.1% |
| 11-19 | 226 | 8 | 3.5% |
| 11-20 | 222 | 13 | 5.9% |
| 11-21 | 242 | 3 | 1.2% |
| 11-22 | 349 | 13 | 3.7% |
| 11-23 | 257 | 11 | 4.3% |
| **7 days** | **1643** | **63** | **3.8%** |
- Week before: 994 impressions, 59 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); ancient trees app (c7/i33, p4); platane du square des batignolles (c4/i2, p1); picture of the tree in helsinki city center that was preserved (c3/i2, p4); 太閤シダレザクラ (c3/i2, p5); evelyns mulberry (c3/i1, p3); ancient trees app (c2/i8, p5); who planted the western red cedar tree in blarney ireland (c2/i8, p2)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-24T06:27 | 3.5 | 0 | 4 | 0 | Colchester, Tsagarada |
| 11-24T08:42 | 5.3 | 1 | 7 | 0 | London +1 |
| 11-24T10:01 | 3.3 | 0 | 5 | 0 | London |
| 11-24T11:55 | 4.2 | 0 | 3 | 0 | - |
| 11-24T12:57 | 4.7 | 0 | 7 | 1 | Lisbon |
| 11-24T18:47 | 4.0 | 0 | 3 | 1 | - |
| 11-24T20:43 | 2.0 | 1 | 5 | 0 | Mirano +1 |
| 11-24T22:47 | 3.6 | 0 | 4 | 0 | - |
| 11-25T00:51 | 3.3 | 0 | 4 | 0 | - |
| **9 runs** | **34** | **2** | **42** | | |

- 7 of 9 produced no trees; 1 to 1 commands refused per run; last build that went live: 0h ago.

**What they made**

- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- Reader judge: the Madison tupelo now leads in its autumn red
- Reader judge: a reader's photograph leads the Hamarikyu pine in Tokyo
- Night window 00:51: checked, shipped nothing; iOS red was runner capacity
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- Readers told their tree or photograph is live, after the deploy
- Readers told their tree or photograph is live, after the deploy
- reader judge: a tall golden larch south of Toblach, a first photograph for the Madison tupelo
- Log: second night attempt, checks only; iOS red answered as runner capacity
- Log: night window 2026-11-24, checks only
- Photographs readers sent, queued for a look; vouched ones live

**Reader photographs in a strip, live first, not yet looked at** (1)

| Day | Tree | Where | Undo |
|---|---|---|---|
| 11-23 | The Tree House Rain Tree of the Netravati Promenade | Mangaluru | `sightings_publish.py --unstrip 1bd94bb4-b914-4baf-861c-c17b843afede` |

Machine: 12 chain attempts yesterday, 10 got real work time (~96 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c870/i1315); /explore (c4/i23); /app (c2/i27); /contribute (c1/i18); /it (c1/i12)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'hidde burgmans' (i3, p2)
    - 'android' (i3, p1)
    - 'ancienttrees' (i1, p3)
    - 'android au' (i1, p1)
    - 'download' (i1, p1)
    - 'এই অ্যাপের লিংক দাও' (i1, p2)
    - 'angeloak' (i1, p99)
    - 'chêne guillotin' (i1, p66)

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 231 | 3 | 15 | 0.06 | 0 |
| Not yet rich | 456 | 13 | 21 | 0.05 | 0 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| monterey | 0 | 22 | 0.0% | 74.6 | 0.4% | lone cypress (i8, p84) |
| london | 0 | 15 | 0.0% | 68.4 | 0.4% | flats to rent clerkenwell (i3, p89) |
| tenerife | 0 | 12 | 0.0% | 86.8 | 0.4% | drago tree tenerife (i2, p96) |
| malaga | 0 | 10 | 0.0% | 91.8 | 0.4% | árboles históricos de málaga (i10, p92) |
| sponsor | 0 | 10 | 0.0% | 2.8 | 11.8% | - |

- Plus 255 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: singapore, lisbon, amsterdam, barcelona, seville, bath, berlin, rome.
**Sign-in mail sent again** (stuck an hour or more, `scripts/signin_watch.py`): 40 people in 7 days, 8 of them got in afterwards.

## 2026-11-23 (previous UTC day)

**Today: 35 android waitlist signups arrived yesterday (2198 total); 35 tree submissions and an ambassador request for Bergamo and an ambassador request for Mexico City and 3 feedback reports arrived yesterday (638 submissions of every kind in all); 42 accounts were opened yesterday (1018 accounts in all).**

**North star: 333 people have uploaded a tree or photo of their own (+162 this week); 52 of them did it on more than one day (+40).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | - | - |
| ... of which from search | every search engine | - | - |
| ... from Google | Google's recovery | - | - |
| ... from Bing | Bing | - | - |
| Website visitors who came back | people who stay | - | - |
| App downloads (first-time) | people | 3553 | 3907 |
| New accounts | people | 382 | 574 |
| Phones back within 30 days | people who stay | 8 of 15 | 4 of 15 |
| Trees saved to Want to go | intent | 357 | 327 |
| Trees collected | goal 1: stood at a tree | 399 | 193 |
| Readers' contributions | data: trees, photos, corrections | 554 | 378 |
| Worth-it votes | one tap, not a contribution | 94 | 106 |
| Shares (app and web) | word of mouth, since 10-30 | 262 | 163 |
| Visits from a shared link | what sharing brings | 87 | 61 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web orange, iOS orange, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | orange: 1 compliance point(s) wait for Hidde (data/compliance.json); 2 compliance fix(es) open | orange: 1 compliance point(s) wait for Hidde (data/compliance.json); 2 compliance fix(es) open | grey: no checks wired yet |
| Live | orange: 1 new error type(s), first "null" in promise | green | grey: no checks wired yet |

**Plus question** (20 answers, 0 new; 5 asked to be told; 12 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| A richer log of every tree you've collected | 8 |
| Download offline maps | 7 |
| Something else | 7 |
| Recommended tree walks for a city trip | 5 |
| Seasonal alerts when trees are at their best | 4 |

**Fixed since 19 Nov: 4.**

| Day | Where | What was wrong | Found by | Test |
|---|---|---|---|---|
| 24 Nov | iPhone | The country picked in the app was never saved: the apps' upsert was refused for an empty display_name (fixed server-side by supabase/flag... | a person | yes |
| 24 Nov | iPhone | A tree sent from the app with only further photographs (main photo empty) was never read by sightings_inbox, so no lead existed and it sa... | a person | yes |
| 22 Nov | iPhone | Edit profile put the saved country back after picking another (the .task on the Form re-ran when the Country list popped) | a person | yes |
| 22 Nov | Web | Explore map search: only the typed text took a click and the browser's blue clear cross sat halfway the pill (.panel-head .ex-search was... | a person | yes |

**New ambassadors yesterday: 3.** a reader (Dresden); Nunzio F. (Bergamo); Manuel G. (Mexico City). Each got the mail and the badge automatically; 49 ambassadors in all (`python3 scripts/ambassador.py --list`).

**Open for you** (1; everything else handled and recorded, 75 feedback in all)

| What | Why it waits | Summary |
|---|---|---|
| feedback 1491 | your call | App country still does not stay after a restart, in reply to our mail of 13:35, after today's server fix; the open BUG row ESC-2026-11-22 (country never saved) covers it. Needs a session to check this account's profile row and their phone and build |

Reader judge: 118 agent minutes yesterday, 1099 in the last 7 days.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-17 | 11-18 | 11-19 | 11-20 | 11-21 | 11-22 | 11-23 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| New accounts | 100 | 62 | 39 | 31 | 41 | 67 | 42 | **382** |
| Saves | 38 | 58 | 28 | 31 | 53 | 60 | 89 | **357** |
| Android waitlist | 158 | 61 | 22 | 16 | 21 | 103 | 35 | **416** |
| App downloads | 712 | 351 | 153 | 127 | 130 | 492 | – | **1965** |
| App deletions | 14 | 10 | 7 | 3 | 9 | 15 | 7 | **65** |
| App phones | 950 | 624 | 483 | 420 | 420 | 756 | 406 | **3151** |
| Trees opened in the app | 1850 | 1104 | 865 | 598 | 843 | 1468 | 704 | **7432** |
| Trees collected | 30 | 21 | 42 | 14 | 24 | 38 | 17 | **186** |
| Trees sent | 37 | 14 | 30 | 13 | 25 | 34 | 35 | **188** |
| Feedback | 15 | 42 | 18 | 12 | 17 | 23 | 9 | **136** |
| Worth-it votes | 20 | 16 | 15 | 9 | 8 | 16 | 10 | **94** |
| Ambassador asks | 2 | 0 | 5 | 1 | 1 | 0 | 2 | **11** |
| Website photos | 6 | 3 | 1 | 2 | 1 | 4 | 1 | **18** |
| iPhone photos | 74 | 41 | 47 | 32 | 46 | 66 | 56 | **362** |
| Android photos | 0 | 0 | 26 | 1 | 5 | 6 | 4 | **42** |
| Tree notes | 11 | 15 | 6 | 3 | 8 | 5 | 6 | **54** |
| App Store reviews | 1 | 0 | 1 | 0 | 0 | 0 | 0 | **2** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.
- App deletions count only phones that share analytics with developers, and Apple leaves out days too small to show: read it against the installs of the same day, not as a total.

**Feedback by kind** (the Feedback row above, split; their words are in the readers-in-full block)

| Kind | 11-23 | **7 days** |
|---|---:|---:|
| Pin moved | 3 | **41** |
| Written feedback | 3 | **74** |
| Report on a tree | 3 | **26** |

**Trees readers sent, for you to inspect** (34 you have not looked at; ours left out)

| Judged | Reader | Tree | Where | Species | Their girth | Our verdict | Page |
|---|---|---|---|---|---:|---|---|
| 2026-11-24 | A | Travilah Oak (5 photos) | Washington DC | White Oak (Quercus alba) | - | hold | - |
| 2026-11-23 | B | Palmeira leque near Florianópolis | - | Palmeira leque | - | hold | - |
| 2026-11-23 | C | St. Wolfgang's Oak (Wolfgangseiche) | Thalmassing | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-23 | D | A tree near Copenhagen | - | - | - | hold | - |
| 2026-11-23 | D | European Beech near Copenhagen | - | European Beech | 200 cm | hold | - |
| 2026-11-23 | D | A tree in Copenhagen | - | - | - | hold | - |
| 2026-11-23 | D | A tree near Jægerspris Nordskov | - | - | - | hold | - |
| 2026-11-23 | E | The Cypress of Kolombatović | Split | Mediterranean Cypress (Cupress | - | hold | - |
| 2026-11-23 | C | The Ginkgo of Varese | Varese | Ginkgo (Ginkgo biloba) | - | hold | - |
| 2026-11-23 | E | The Cypress of Šimun Tudor, Marjan | Split | Mediterranean Cypress (Cupress | - | hold | - |
| 2026-11-23 | F | The White Oak on Grubb Road | Willistown | White Oak (Quercus alba) | - | hold | - |
| 2026-11-23 | G | Hophornbeam | - | Hophornbeam (Ostrya sp.) | - | hold | - |
| 2026-11-22 | B | The Fig of the Hanging Roots in Coqueiros | Florianópolis | Fig (Ficus sp.) | - | hold | - |
| 2026-11-22 | H | The Fern-leaved Beech | Munich | Fern-leaved Beech (Fagus sylva | - | hold | - |
| 2026-11-22 | I | The Oldest Plane Tree in Europe | Τσαγκαράδα | - | 1300 cm | hold | - |
| 2026-11-22 | ? | 57F46EDF-95E2-4A21-935F-5B12D0B23E94 | Como | - | - | lead | - |
| 2026-11-22 | J | A tree near Trento | - | - | - | hold | - |
| 2026-11-22 | K | The Great Beech of the Solbosch Woods | Brussels | European Beech (Fagus sylvatic | - | hold | - |
| 2026-11-22 | K | - | Brussels | - | - | hold | - |
| 2026-11-22 | L | The Linden of Linn | Zurich | Large-leaved Lime (Tilia platy | - | hold | - |
| 2026-11-22 | M | The Redford Wood Redwood | Edinburgh | Giant Sequoia (Sequoiadendron  | - | hold | - |
| 2026-11-22 | N | Unknown Tree | Andaman Island | - | - | hold | - |
| 2026-11-22 | ? | The Banyan by the Arcades | Delhi | Indian Banyan (Ficus benghalen | - | hold | - |
| 2026-11-22 | ? | The Peepal on the Plinth | Delhi | Bodhi Tree (Ficus religiosa) | - | hold | - |
| 2026-11-22 | O | A tree in Bad Homburg | - | - | - | hold | - |
| 2026-11-22 | B | Figueira de duas pernas | - | Fig | - | hold | - |
| 2026-11-22 | ? | C9139A4E-9E9A-4065-8DD9-865527B71C83 | - | - | - | hold | - |
| 2026-11-22 | ? | AFBEEDB0-236E-42CC-814B-B8AA7AB6FABB | Delhi | - | - | hold | - |
| 2026-11-22 | P | The Alois-Drasche-Park Beech | Vienna | European Beech (Fagus sylvatic | - | hold | - |
| 2026-11-22 | Q | The Great Pine of Romanya | Girona | Stone Pine (Pinus pinea) | - | hold | - |
| 2026-11-22 | R | Boab Prison Tree | Derby | Boab (Adansonia gregorii) | - | hold | - |
| 2026-11-22 | ? | Spirit Tree ancient cottonwood tree | Patagonia | - | 600 cm | lead | - |
| 2026-11-22 | S | A tree I found | - | - | - | hold | - |
| 2026-11-21 | ? | FBA415E7-7E56-4859-BBFA-88CA09A74FD6 | - | - | - | hold | - |
- From 19 readers: reader D 4, reader B 3, reader C 2, reader E 2, reader K 2, reader A 1, reader F 1, reader G 1, reader H 1, reader I 1, reader J 1, reader L 1, reader M 1, reader N 1, reader O 1, reader P 1, reader Q 1, reader R 1, reader S 1.
- Photographs and the readers' own words: `python3 scripts/inspect_readers.py` (a local page, never in this public file). Your answer goes in with `python3 scripts/judgement.py --feedback <id> "..."`.

**Waiting for you** (what the runs left for you since 2026-11-23)

- 229 email addresses ready to mail (archive 0, nature 9, guide 4, press 122, source 58, council 16, society 7, tourism 5, other 5, garden 3); **the night run found no new contacts in two days**
- dispatch Build and deploy once, or let the next knock do it, to confirm green.
- their words were "I didn't realize adding my photo to my trees would post it on the page".
- none.

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-22 | T | The Weeping Beech of Magistratsparken | Malmö | a reader's photograph, published | [live](https://ancienttrees.app/malmo/weeping-beech-of-magistratsparken) |
| 11-22 | U | The Witch Tree of Fanal | Madeira | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/madeira/witch-tree-of-fanal) |
| 11-22 | V | The Gennett Poplar | Chattahoochee National Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/chattahoochee-national-forest/gennett-poplar) |
| 11-22 | W |  | ? | a reader's photograph, published | not live yet |
| 11-22 | X | Pando | Fish Lake, Utah | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/fish-lake-utah/pando) |
| 11-22 | Y |  | ? | a reader's photograph, published | not live yet |
| 11-22 | Z |  | ? | a reader's photograph, published | not live yet |
| 11-22 | A1 | The Lime of the Noordeind | Emmen | a reader's photograph, published | [live](https://ancienttrees.app/emmen/lime-of-the-noordeind) |
| 11-22 | A1 | The Plane of the Bonifatius Park | Emmen | a reader's photograph, published | [live](https://ancienttrees.app/emmen/plane-of-the-bonifatius-park) |
| 11-22 | A1 | The Plane by Restaurant Urbana | Zwolle | a reader's photograph, published | [live](https://ancienttrees.app/zwolle/plane-by-restaurant-urbana) |
| 11-22 | A1 | The Copper Beech of Nieuw-Schoonebeek | Emmen | a reader's photograph, published | [live](https://ancienttrees.app/emmen/copper-beech-of-nieuw-schoonebeek) |
| 11-22 | A1 | The Oak at the Long Grave | Emmen | a reader's photograph, published | [live](https://ancienttrees.app/emmen/oak-at-the-long-grave) |
| 11-22 | A1 | Huis de Paddestoel's Swamp Cypress | Zwolle | a reader's photograph, published | [live](https://ancienttrees.app/zwolle/huis-de-paddestoels-swamp-cypress) |
| 11-22 | A1 | The Weeping Beech of Park Boschwijk | Zwolle | a reader's photograph, published | [live](https://ancienttrees.app/zwolle/weeping-beech-of-park-boschwijk) |
| 11-22 | A1 | The Beech of the Boschwijk Avenue | Zwolle | a reader's photograph, published | [live](https://ancienttrees.app/zwolle/beech-of-the-boschwijk-avenue) |
| 11-22 | A1 | The Oak in Hunebed D42 | Emmen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/emmen/oak-in-hunebed-d42) |
| 11-22 | Z |  | ? | a reader's photograph, published | not live yet |
| 11-22 | B1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | B1 | The Llangernyw Yew | Llangernyw | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/llangernyw/llangernyw-yew) |
| 11-22 | C1 | The Monterey Cypress at Bishops Knoll | Bristol | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/bristol/monterey-cypress-at-bishops-knoll) |
| 11-22 | D1 | Thorvaldsen's Robinia | Copenhagen | a reader's photograph, published | [live](https://ancienttrees.app/copenhagen/thorvaldsens-robinia) |
| 11-22 | D1 | The Mulberry of Proviantgarden | Copenhagen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/copenhagen/mulberry-of-proviantgarden) |
| 11-22 | E1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | F1 | The Copper Beech of Sint-Willibrorduskerk | Antwerp | a reader's photograph, published | [live](https://ancienttrees.app/antwerp/copper-beech-of-sint-willibrorduskerk) |
| 11-22 | H | The Fern-leaved Beech | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/fern-leaved-beech) |
| 11-22 | G1 | The Leidsebosje Planes | Amsterdam | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/amsterdam/leidsebosje-planes) |
| 11-22 | H1 | The Plane of Dr. Karl Lueger-Platz | Vienna | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/vienna/plane-of-dr-karl-lueger-platz) |
| 11-22 | H1 | The Pagoda Tree of the Stadtpark | Vienna | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/vienna/pagoda-tree-of-the-stadtpark) |
| 11-22 | I1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | J1 | Vernon Oak | Sheffield | a reader's photograph, published | [live](https://ancienttrees.app/sheffield/vernon-oak) |
| 11-22 | K1 | The Hundred-Horse Chestnut | Sant'Alfio | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/santalfio/hundred-horse-chestnut) |
| 11-22 | K1 | The Hundred-Horse Chestnut | Sant'Alfio | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/santalfio/hundred-horse-chestnut) |
| 11-22 | L1 | The Witch Tree of Fanal | Madeira | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/madeira/witch-tree-of-fanal) |
| 11-22 | M1 | The Cedar of Lebanon in Victoria Square | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/cedar-of-lebanon-in-victoria-square) |
| 11-22 | N1 | Moreton Bay Figs of Donnafugata Castle Park | Ragusa | a reader's photograph, published | [live](https://ancienttrees.app/ragusa/moreton-bay-figs-of-donnafugata-castle-park) |
| 11-22 | L1 | The Witch Tree of Fanal | Madeira | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/madeira/witch-tree-of-fanal) |
| 11-22 | N1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | O1 | The Old Mulberry of Taranta | Cassano d'Adda | a reader's photograph, published | [live](https://ancienttrees.app/cassano-dadda/old-mulberry-of-taranta) |
| 11-22 | P1 | The Thousand-Year Oak of Barmstedt | Barmstedt | a reader's photograph, published | [live](https://ancienttrees.app/barmstedt/thousand-year-oak-of-barmstedt) |
| 11-22 | Q1 | The Weeping Willow of Via Dante Alighieri | Bagnolo San Vito | a reader's photograph, published | [live](https://ancienttrees.app/bagnolo-san-vito/weeping-willow-of-via-dante-alighieri) |
| 11-22 | R1 | The Evelyn Mulberry | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/evelyn-mulberry) |
| 11-22 | S1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | S1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | B |  | ? | a reader's photograph, published | not live yet |
| 11-22 | B |  | ? | a reader's photograph, published | not live yet |
| 11-22 | O |  | ? | a reader's photograph, published | not live yet |
| 11-22 | T1 | The Fig of the Glorieta de Goya | Seville | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/seville/fig-of-the-glorieta-de-goya) |
| 11-22 | L | The Linden of Linn | Zurich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/zurich/linden-of-linn) |
| 11-22 | U1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | B | The Plaque Tree on the Shore of Ribeirão da Ilha | Florianópolis | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/florianopolis/plaque-tree-on-the-shore-of-ribeirao-da-ilha) |
| 11-22 | B | The Fig of the Hanging Roots in Coqueiros | Florianópolis | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/florianopolis/fig-of-the-hanging-roots-in-coqueiros) |
| 11-22 | P | The Alois-Drasche-Park Beech | Vienna | a reader's photograph, published | [live](https://ancienttrees.app/vienna/alois-drasche-park-beech) |
| 11-22 | A1 | The Coronation Lime of the Spanderslaan | Hilversum | a reader's photograph, published | [live](https://ancienttrees.app/hilversum/coronation-lime-of-the-spanderslaan) |
| 11-22 | A1 | The Bernhard Chestnut of the Hilvertsweg | Hilversum | a reader's photograph, published | [live](https://ancienttrees.app/hilversum/bernhard-chestnut-of-the-hilvertsweg) |
| 11-22 | A1 | The Juliana Lime of the Hilvertsweg | Hilversum | a reader's photograph, published | [live](https://ancienttrees.app/hilversum/juliana-lime-of-the-hilvertsweg) |
| 11-22 | R | Boab Prison Tree | Derby | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/derby/boab-prison-tree) |
| 11-22 | V1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | W1 | The Argyle Street Ash | Glasgow | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/glasgow/argyle-street-ash) |
| 11-22 | V1 | The Cedar of Jussieu | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/cedar-of-jussieu) |
| 11-22 | X1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | V1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | Y1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | Z1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | A2 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | B2 | The Lehmann Plane of Planten un Blomen | Hamburg | a reader's photograph, published | [live](https://ancienttrees.app/hamburg/lehmann-plane-of-planten-un-blomen) |
| 11-22 | ? | The Japanese Pagoda Tree of Alsterufer | Hamburg | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/hamburg/japanese-pagoda-tree-of-alsterufer) |
| 11-22 | C2 | The Bur Oak by the Cuvier Gate | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/bur-oak-by-the-cuvier-gate) |
| 11-22 | F |  | ? | a reader's photograph, published | not live yet |
| 11-23 | D2 | Paavola's Oak | Lohja | a reader's photograph, published | [live](https://ancienttrees.app/lohja/paavolas-oak) |
| 11-23 | W |  | ? | a reader's photograph, published | not live yet |
| 11-23 | E2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | Y |  | ? | a reader's photograph, published | not live yet |
| 11-23 | F2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | D |  | ? | a reader's photograph, published | not live yet |
| 11-23 | G2 | Kett's Oak | Hethersett | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/hethersett/ketts-oak) |
| 11-23 | D |  | ? | a reader's photograph, published | not live yet |
| 11-23 | D |  | ? | a reader's photograph, published | not live yet |
| 11-23 | D |  | ? | a reader's photograph, published | not live yet |
| 11-23 | C2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | C2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | C |  | ? | a reader's photograph, published | not live yet |
| 11-23 | C |  | ? | a reader's photograph, published | not live yet |
| 11-23 | H2 | The Hackberry of the Parco degli Scipioni | Rome | a reader's photograph, published | [live](https://ancienttrees.app/rome/hackberry-of-the-parco-degli-scipioni) |
| 11-23 | I2 | The Chiswick House Cedars | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/chiswick-house-cedars) |
| 11-23 | J2 | The Tree House Rain Tree of the Netravati Promenade | Mangaluru | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mangaluru/tree-house-rain-tree-of-the-netravati-promenade) |
| 11-23 | K2 | The Moreton Bay Fig of Curtain Square | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/moreton-bay-fig-of-curtain-square) |
| 11-23 | H2 | The Hackberry of the Mura Latine | Rome | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/rome/hackberry-of-the-mura-latine) |
| 11-23 | Y | Tāne Mahuta | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/tane-mahuta) |
| 11-23 | L2 | The Plane of Largo Doutor Francisco Soveral | Setubal | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/setubal/plane-of-largo-doutor-francisco-soveral) |
| 11-23 | C2 | The Twisted Beech of Square des Arenes de Lutece | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/twisted-beech-of-square-des-arenes-de-lutece) |
| 11-23 | C2 | The Weeping Cedar of the Vallée-aux-Loups (Cèdre pleureur) | Chatenay-Malabry | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/chatenay-malabry/weeping-cedar-of-the-vallee-aux-loups-cedre-pleureur) |
| 11-23 | C2 | The Bur Oak by the Cuvier Gate | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/bur-oak-by-the-cuvier-gate) |
| 11-23 | E | The Ginkgo of Đardin | Split | a reader's photograph, published | [live](https://ancienttrees.app/split/ginkgo-of-dardin) |
| 11-23 | M2 | The Tortworth Chestnut | Tortworth | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tortworth/tortworth-chestnut) |
| 11-23 | M2 | The Tortworth Chestnut | Tortworth | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tortworth/tortworth-chestnut) |
| 11-23 | E | Mastrinka, the Olive of Kaštel Štafilić | Kaštela | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kastela/mastrinka-the-olive-of-kastel-stafilic) |
| 11-23 | E | Mastrinka, the Olive of Kaštel Štafilić | Kaštela | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kastela/mastrinka-the-olive-of-kastel-stafilic) |
| 11-23 | N2 | The Minster Yard Beech | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/minster-yard-beech) |
| 11-23 | N2 | The Minster London Plane | York | a reader's photograph, published | [live](https://ancienttrees.app/york/minster-london-plane) |
| 11-23 | C2 | The Tall Plane of the Jardin des Plantes | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/tall-plane-of-the-jardin-des-plantes) |
| 11-23 | C2 | The Large-leaved Lime of Rungis | Rungis | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/rungis/large-leaved-lime-of-rungis) |
| 11-23 | C2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | C2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | O2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | P2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | Q2 | The Golden Ginkgo of Greenwich | London | a reader's photograph, published | [live](https://ancienttrees.app/london/golden-ginkgo-of-greenwich) |
| 11-23 | R2 | Tight Grove, University of New Mexico | Albuquerque | a reader's photograph, published | [live](https://ancienttrees.app/albuquerque/tight-grove-university-of-new-mexico) |
| 11-23 | S2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | S2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | S2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | S2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | S2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | S2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | T2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | U2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | V2 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | A |  | ? | a reader's photograph, published | not live yet |
| 11-23 | W2 | The Oak of Clingoe Hill | Colchester | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/colchester/oak-of-clingoe-hill) |
| 11-23 | S2 | The Many-Stemmed Beech of East Hampton | East Hampton | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/east-hampton/many-stemmed-beech-of-east-hampton) |
| 11-23 | F | The Laurel Hill Cutleaf Linden | Philadelphia | a reader's photograph, published | [live](https://ancienttrees.app/philadelphia/laurel-hill-cutleaf-linden) |
| 11-23 | F |  | ? | a reader's photograph, published | not live yet |
| 11-24 | X2 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | Y2 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | Z2 |  | ? | a reader's photograph, published | not live yet |
| 11-24 | A | Travilah Oak | Washington DC | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/washington-dc/travilah-oak) |
| 11-24 | W2 | The Cedar near Clingoe Hill | Colchester | a reader's photograph, published | [live](https://ancienttrees.app/colchester/cedar-near-clingoe-hill) |
| 11-24 | W2 | The Cedar near Clingoe Hill | Colchester | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/colchester/cedar-near-clingoe-hill) |
| 11-22 | A3 | The Old Jarrah Tree | Perth | a reader's correction changed the page | - |
| 11-22 | B | Fig | - | a reader's correction changed the page | - |
| 11-22 | Z1 | The cedar of Himalaya | Verona | a reader's tree changed the page | - |
| 11-23 | B3 | The Ginkgo of Đardin | Split | a reader's correction changed the page | - |
| 11-23 | F | The Laurel Hill Cutleaf Linden | Philadelphia | a reader's correction changed the page | - |
- From 72 readers: reader A1 12, reader C2 10, reader S2 7, reader B 5, reader D 4, reader F 4, reader E 3, reader V1 3, reader W2 3, reader Y 3, reader A 2, reader B1 2, reader C 2, reader D1 2, reader H1 2, reader H2 2, reader K1 2, reader L1 2, reader M2 2, reader N1 2, reader N2 2, reader S1 2, reader W 2, reader Z 2, reader Z1 2, reader A2 1, reader A3 1, reader B2 1, reader B3 1, reader C1 1, reader D2 1, reader E1 1, reader E2 1, reader F1 1, reader F2 1, reader G1 1, reader G2 1, reader H 1, reader I1 1, reader I2 1, reader J1 1, reader J2 1, reader K2 1, reader L 1, reader L2 1, reader M1 1, reader O 1, reader O1 1, reader O2 1, reader P 1, reader P1 1, reader P2 1, reader Q1 1, reader Q2 1, reader R 1, reader R1 1, reader R2 1, reader T 1, reader T1 1, reader T2 1, reader U 1, reader U1 1, reader U2 1, reader V 1, reader V2 1, reader W1 1, reader X 1, reader X1 1, reader X2 1, reader Y1 1, reader Y2 1, reader Z2 1.

**What was sent in, and what we decided**

| seen | what | where | size for its species | ours | Hidde |
|---|---|---|---|---|---|
| 2026-11-24 | Travilah Oak | Washington DC | - | hold | - |
| 2026-11-24 | Travilah Oak | Washington DC | - | hold | - |
| 2026-11-24 | Travilah Oak | Washington DC | - | hold | - |
| 2026-11-24 | Travilah Oak | Washington DC | - | hold | - |
| 2026-11-20 | Tyler Arboretum Giant Sequoia | Media | - | lead | - |
| 2026-11-19 | The Ivy Elm of Park Oliwski | Gdansk | - | hold | - |
| 2026-11-19 | A tree I found | - | - | hold | - |
| 2026-11-19 | The Amur Cork Trees and Crimean Linden | Vilnius | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | lead | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | lead | - |
| 2026-11-18 | A tree I found | - | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | The Southern Mahogany of Edinburgh Gar | Melbourne | - | hold | - |
| 2026-11-18 | The Casuarina of the Cascada | Barcelona | - | hold | - |

0 waiting for a verdict. Disagree with one and the rule changes: `python3 scripts/judgement.py --feedback <id> "..."`, and `--learn` prints every verdict he has overruled.

**Searched yesterday:** london (11 times), aarhus (4 times), cop (4 times), copen (4 times), frankfurt (4 times), roma (3 times), bologna (2 times), botanical garden frankfurt (2 times), edinburgh (2 times), lo (2 times), new (2 times), torino (2 times), adelaide, alicante, arcata, ca, bad neus, barce, barcellona, beckenham, beijing.

**App crashes** (last 7 days, store builds; MetricKit, a sample)

| Crashes | Kind | Build | Where | Phones | Last | Fix |
|---:|---|---|---|---:|---|---|
| 1 | crash | 1.0.4 (41) | AncientTrees+0x35fccc | 1 | 2026-11-20 | none |
| 1 | hang | 1.0.4 (41) | AncientTrees+0x376463 | 1 | 2026-11-21 | none |

Search Console: fetch failed today (HTTP Error 400: Bad Request); numbers resume tomorrow.

**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-17 | 170 | 6 | 3.5% |
| 11-18 | 177 | 9 | 5.1% |
| 11-19 | 226 | 8 | 3.5% |
| 11-20 | 222 | 13 | 5.9% |
| 11-21 | 242 | 3 | 1.2% |
| 11-22 | 349 | 13 | 3.7% |
| 11-23 | - | - | 0.0% |
| **7 days** | **1386** | **52** | **3.8%** |
- Week before: 994 impressions, 59 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); ancient trees app (c7/i33, p4); platane du square des batignolles (c4/i2, p1); picture of the tree in helsinki city center that was preserved (c3/i2, p4); 太閤シダレザクラ (c3/i2, p5); evelyns mulberry (c3/i1, p3); ancient trees app (c2/i8, p5); who planted the western red cedar tree in blarney ireland (c2/i8, p2)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-23T13:57 | 0.0 | 0 | 3 | 0 | - |
| 11-24T00:08 | 13.3 | 1 | 11 | 1 | Tsagarada +1 |
| 11-24T01:29 | 5.3 | 0 | 10 | 0 | - |
| **3 runs** | **19** | **1** | **24** | | |

- 2 of 3 produced no trees; 1 to 1 commands refused per run; 1 wrote nothing to LOG.md; last build that went live: 0h ago.

**What they made**

- Readers told their tree or photograph is live, after the deploy
- Colchester cedar: the lead photo's month records its basis
- Reader judge: a fuller photograph of the Colchester cedar leads, the reader's girth and age on the page (cls_002)
- Reader judge: a reader's cedar near Clingoe Hill live in Colchester (cls_002)
- Readers told their tree or photograph is live, after the deploy
- Reader judge 2026-11-24: nothing new waiting; Nathalie's Shanghai mail reply closed as handled
- Fix red deploy: Bute Park title says 5 trees, and preflight's park count now skips app-only trees like the build
- Record when each page last changed
- Reader judge 2026-11-24: the twin ginkgos of Jiao Tong University (shanghai/sha_002) live after the reader said the campus opens from the street; a reader's Travilah Oak photograph leads wdc_016
- Reader judge: the plane of Stewart Reid Memorial Park (ngahinapouri/ngh_001) live, re-judged from not_special on the memorial park's record
- Readers told their tree or photograph is live, after the deploy
- Reader judge 2026-11-24: the Macedon Oak of Cruden Farm (langwarrin/lwr_001) live from a reader's three photographs and the National Trust register; a Waikato plane held not_special
- Compliance review: 2 new finding(s)
- Fresh-eyes review: 7 finding(s)

**Reader photographs in a strip, live first, not yet looked at** (2)

| Day | Tree | Where | Undo |
|---|---|---|---|
| 11-22 | The Argyle Street Ash | Glasgow | `sightings_publish.py --unstrip dcffbd99-b1c4-403e-87c3-48ae83bf6d51` |
| 11-23 | The Tree House Rain Tree of the Netravati Promenade | Mangaluru | `sightings_publish.py --unstrip 1bd94bb4-b914-4baf-861c-c17b843afede` |

Machine: 4 chain attempts yesterday, 3 got real work time (~18 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

**Sign-in mail sent again** (stuck an hour or more, `scripts/signin_watch.py`): 40 people in 7 days, 8 of them got in afterwards.

## Weekly analysis 2026-11-23

Seventeenth weekly analysis. Reads 11-16 to 11-22 against 11-09 to 11-15, from the 11-21
and 11-22 daily entries. The 11-22 entry had no Search Console and no Google Analytics
(HTTP 400), so web and Google rows run to 11-21 and app rows to 11-22; Apple's
downloads lag a day. **Correction to last week's table:** it showed 14 first-time
downloads for 11-09 to 11-15 because Apple had not reported 11-15 yet; the day table now
shows 3,896 on 11-15, so that week is about 3,910.

**Scorecard**

| Week | Google impr. | Google clicks | CTR | Position | Bing impr. / clicks | Visitors (GA, new) | From Google | Downloads (first-time) | New accounts | Saves | Readers' contributions |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 11-09 to 11-15 | ~1,800 | 221 | 12% | 5.5 to 58 | 934 / 48 | 1,818 | 38 | ~3,910 | 369+ | 191+ | 301 |
| 11-16 to 11-22 | 570 (11-16 to 11-21) | 260 | 46% | 6.6 to 32.5 | 1,248 / 54 | 3,042 (11-15 to 11-21) | 70 | 3,061 (11-16 to 11-21, 11-22 not in) | 539 | 410 | 624 |

Per day, accounts 199 / 100 / 62 / 39 / 31 / 41 / 67; downloads 1,588 / 712 / 351 / 153 /
127 / 130; Google impressions 204 / 132 / 67 / 60 / 66 / 41; Google clicks 116 / 59 / 33 /
19 / 20 / 13. Everything after the Guardian day (11-15) decays and then flattens at about
130 downloads and 30 to 70 accounts a day, against 2 a day before 11-15. Android waitlist
2,177 total on 11-22 (103 that day). Device split and per-visit ratios are not in the
entries, so none is claimed.

**Outreach yield** (data/mail-yield.json, mailbox read, built 11-22; weeks keyed by the Monday of our first mail; 11-09 is the week before last, 11-16 is too young to judge)

| Group | Mailed, week of 11-09 | Answered of those | Mailed, total | Answered, total | Rate | Linked |
|---|---:|---:|---:|---:|---:|---:|
| archive | 2 | 2 | 27 | 6 | 22% | 0 |
| nature | 0 | 0 | 81 | 8 | 10% | 1 |
| guide | 1 | 0 | 41 | 2 | 5% | 1 |
| source | 4 | 1 | 63 | 9 | 14% | 0 |
| press | 5 | 2 | 156 | 10 | 6% | 0 |
| tourism | 1 | 0 | 20 | 6 | 30% | 0 |
| garden | 0 | 0 | 97 | 11 | 11% | 0 |
| society | 0 | 0 | 148 | 25 | 17% | 1 |
| council | 0 | 0 | 60 | 10 | 17% | 0 |
| other | 187 | 15 | 1,594 | 96 | 6% | 2 |

The week of 11-16 sent 1,284 mails (other 1,247, press 30, guide 4, council 2, tourism 1);
28 of the 1,247 answered so far (2%), too young to judge. Five links in all, none new.

**What moved:**
1. The Guardian day is a decaying spike with a higher floor: downloads fell from 1,588 to
   about 130 a day, accounts from 199 to 31 to 67, and the floor is still far above the
   2 to 5 accounts a day of before 11-15.
2. Google is brand search only: Google clicks fell 116, 59, 33, 19, 20, 13 a day, position
   6.6 to 32.5; the top query is "ancient trees app" (487 impressions in 10 days, position
   1), "ancient trees" 15 impressions at position 36. No tree query appears. Noise level
   for page recovery.
3. Readers carry the data: 315 people have sent a tree or photo (+207 this week), 49 on
   more than one day; 410 iPhone photos, 204 trees sent, 71 tree notes, 38 Android photos.
4. Bing grows quietly: 1,248 impressions and 54 clicks against 934 and 48; index 4,617 to
   4,929 pages.
5. Quality: Web next version red (deploy failure on main), iOS red (build failure on main),
   Backup red; one new web error type ("null" in a promise). Phones back within 30 days
   8 of 16 (an old cohort, not the Guardian one).

**Suggestions, ranked:**
1. **[run]** The deploy failure on main (Web next version red on both the 11-21 and 11-22
   entries, "1 failed since" the last live build, iOS build also red). Fixes of the week
   (3 listed) only help once a deploy goes green; read the failing run first, it is
   rung-2 work.
2. **[run]** Day-7 and day-30 read of the Guardian cohort: downloads and accounts have
   settled at 130 and 30 to 70 a day, so the question is whether those phones return.
   Compute phones back for the 11-15 and 11-16 arrivals at 11-22 and 12-15 (the 30-day row
   only measures cohorts from five weeks ago, so it cannot answer this).
3. **[FOR HIDDE]** Press is the only lane that has moved anything (6,957 downloads in a
   week against 14, from one article); 156 press mails answered 10 (6%) with 0 links, and
   the 1,247 "other" mails of 11-16 answered 2% so far. Choose between more volume and
   fewer, pitched press stories; the first full read of the 11-16 batch comes in about
   two weeks.
4. **[run]** Search-term gaps in yesterday's site searches: "hove" (5), "victoria" (3),
   "biella" (2) have no city file (Milan, Auckland, Brighton, Palermo, Perth, Toronto,
   Bologna, Como, Baltimore do). Check each against data/leads and the register scouting
   before building; "hove" may only need an alias to Brighton.
5. **[sessie]** The Plus question has 20 answers (richer log of collected trees 8, offline
   maps 7, walks 5, seasonal alerts 4); noise level, but it is the only paywall evidence.
   Keep collecting; do not read it as a ranking yet.

**Watch next week:** whether the daily floor holds at about 130 downloads and 30 to 70
accounts or sinks toward the old 2 a day; Google clicks against the brand-query decay
(13 a day on 11-21); whether Web goes green; the reader judge's agent minutes (981 in the
last 7 days, 198 on the busiest day) against the weekly machine budget.

## 2026-11-22 (previous UTC day)

**Today: 103 android waitlist signups arrived yesterday (2177 total); 34 tree submissions and 11 feedback reports arrived yesterday (597 submissions of every kind in all); 67 accounts were opened yesterday (990 accounts in all).**

**North star: 315 people have uploaded a tree or photo of their own (+207 this week); 49 of them did it on more than one day (+42).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | - | - |
| ... of which from search | every search engine | - | - |
| ... from Google | Google's recovery | - | - |
| ... from Bing | Bing | - | - |
| Website visitors who came back | people who stay | - | - |
| App downloads (first-time) | people | 6957 | 14 |
| New accounts | people | 539 | 375 |
| Phones back within 30 days | people who stay | 8 of 16 | 4 of 14 |
| Trees saved to Want to go | intent | 410 | 187 |
| Trees collected | goal 1: stood at a tree | 520 | 3 |
| Readers' contributions | data: trees, photos, corrections | 624 | 232 |
| Worth-it votes | one tap, not a contribution | 128 | 62 |
| Shares (app and web) | word of mouth, since 10-30 | 321 | 46 |
| Visits from a shared link | what sharing brings | 104 | 34 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web red, iOS red, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | red: deploy failure on main | red: iOS build failure on main | grey: no checks wired yet |
| Live | orange: 1 new error type(s), first "null" in promise | green | grey: no checks wired yet |
| Open bugs | green | orange: 1 open, 1 found by people | grey: no checks wired yet |

**Plus question** (20 answers, 3 new; 5 asked to be told; 12 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| A richer log of every tree you've collected | 8 |
| Download offline maps | 7 |
| Something else | 7 |
| Recommended tree walks for a city trip | 5 |
| Seasonal alerts when trees are at their best | 4 |

**Fixed since 19 Nov: 3.**

| Day | Where | What was wrong | Found by | Test |
|---|---|---|---|---|
| 22 Nov | iPhone | Edit profile put the saved country back after picking another (the .task on the Form re-ran when the Country list popped) | a person | yes |
| 22 Nov | Web | Explore map search: only the typed text took a click and the browser's blue clear cross sat halfway the pill (.panel-head .ex-search was... | a person | yes |
| 20 Nov | Web | Map pins stacked under each other and jumped on hover; the chosen pin stood far from its card (pin CSS set position:relative over MapLibr... | a person | yes |

**Ambassador requests, open** (1 person, 1 place; each stays here until our mail with the questions has gone, or the badge is granted with `python3 scripts/ambassador.py --grant`)

| Asked | Places | From | Our mail with the questions | Waiting on |
|---|---|---|---|---|
| 2026-11-23 | **Bergamo** | the app | not yet (next knock) | the mail |

**New ambassadors yesterday: 2.** Jonardon G. (Chiang Mai); ElleP (Horn-Lehe). Each got the mail and the badge automatically; 43 ambassadors in all (`python3 scripts/ambassador.py --list`).

**Open for you** (1; everything else handled and recorded, 70 feedback in all)

| What | Why it waits | Summary |
|---|---|---|
| feedback 1491 | your call | App country still does not stay after a restart, in reply to our mail of 13:35, after today's server fix; the open BUG row ESC-2026-11-22 (country never saved) covers it. Needs a session to check this account's profile row and their phone and build |

Reader judge: 198 agent minutes yesterday, 981 in the last 7 days.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-16 | 11-17 | 11-18 | 11-19 | 11-20 | 11-21 | 11-22 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| New accounts | 199 | 100 | 62 | 39 | 31 | 41 | 67 | **539** |
| Saves | 141 | 38 | 58 | 28 | 31 | 54 | 60 | **410** |
| Android waitlist | 416 | 158 | 61 | 22 | 16 | 21 | 103 | **797** |
| App downloads | 1588 | 712 | 351 | 153 | 127 | 130 | – | **3061** |
| App deletions | 16 | 14 | 10 | 7 | 3 | 9 | 15 | **74** |
| App phones | 1694 | 950 | 624 | 483 | 420 | 420 | 755 | **4157** |
| Trees opened in the app | 3264 | 1850 | 1104 | 865 | 598 | 843 | 1468 | **9992** |
| Trees collected | 59 | 30 | 21 | 42 | 14 | 24 | 38 | **228** |
| Trees sent | 51 | 37 | 14 | 30 | 13 | 25 | 34 | **204** |
| Feedback | 23 | 15 | 42 | 18 | 12 | 17 | 23 | **150** |
| Worth-it votes | 44 | 20 | 16 | 15 | 9 | 8 | 16 | **128** |
| Ambassador asks | 3 | 2 | 0 | 5 | 1 | 1 | 0 | **12** |
| Website photos | 3 | 6 | 3 | 1 | 2 | 1 | 4 | **20** |
| iPhone photos | 104 | 74 | 41 | 47 | 32 | 47 | 65 | **410** |
| Android photos | 0 | 0 | 0 | 26 | 1 | 5 | 6 | **38** |
| Tree notes | 23 | 11 | 15 | 6 | 3 | 8 | 5 | **71** |
| App Store reviews | 2 | 1 | 0 | 1 | 0 | 0 | 0 | **4** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.
- App deletions count only phones that share analytics with developers, and Apple leaves out days too small to show: read it against the installs of the same day, not as a total.

**Feedback by kind** (the Feedback row above, split; their words are in the readers-in-full block)

| Kind | 11-22 | **7 days** |
|---|---:|---:|
| Pin moved | 8 | **54** |
| Written feedback | 12 | **69** |
| Report on a tree | 3 | **28** |

**Trees readers sent, for you to inspect** (22 you have not looked at; ours left out)

| Judged | Reader | Tree | Where | Species | Their girth | Our verdict | Page |
|---|---|---|---|---|---:|---|---|
| 2026-11-22 | A | The Fig of the Hanging Roots in Coqueiros | Florianópolis | Fig (Ficus sp.) | - | hold | - |
| 2026-11-22 | B | The Fern-leaved Beech | Munich | Fern-leaved Beech (Fagus sylva | - | hold | - |
| 2026-11-22 | C | The Oldest Plane Tree in Europe | Τσαγκαράδα | - | 1300 cm | hold | - |
| 2026-11-22 | ? | 57F46EDF-95E2-4A21-935F-5B12D0B23E94 | Como | - | - | lead | - |
| 2026-11-22 | D | A tree near Trento | - | - | - | hold | - |
| 2026-11-22 | E | The Great Beech of the Solbosch Woods | Brussels | European Beech (Fagus sylvatic | - | hold | - |
| 2026-11-22 | E | - | Brussels | - | - | hold | - |
| 2026-11-22 | F | The Linden of Linn | Zurich | Large-leaved Lime (Tilia platy | - | hold | - |
| 2026-11-22 | G | The Redford Wood Redwood | Edinburgh | Giant Sequoia (Sequoiadendron  | - | hold | - |
| 2026-11-22 | H | Unknown Tree | Andaman Island | - | - | hold | - |
| 2026-11-22 | ? | The Banyan by the Arcades | Delhi | Indian Banyan (Ficus benghalen | - | hold | - |
| 2026-11-22 | ? | The Peepal on the Plinth | Delhi | Bodhi Tree (Ficus religiosa) | - | hold | - |
| 2026-11-22 | I | A tree in Bad Homburg | - | - | - | hold | - |
| 2026-11-22 | A | Figueira de duas pernas | - | Fig | - | hold | - |
| 2026-11-22 | ? | C9139A4E-9E9A-4065-8DD9-865527B71C83 | - | - | - | hold | - |
| 2026-11-22 | ? | AFBEEDB0-236E-42CC-814B-B8AA7AB6FABB | Delhi | - | - | hold | - |
| 2026-11-22 | J | The Alois-Drasche-Park Beech | Vienna | European Beech (Fagus sylvatic | - | hold | - |
| 2026-11-22 | K | The Great Pine of Romanya | Girona | Stone Pine (Pinus pinea) | - | hold | - |
| 2026-11-22 | L | Boab Prison Tree | Derby | Boab (Adansonia gregorii) | - | hold | - |
| 2026-11-22 | ? | Spirit Tree ancient cottonwood tree | Patagonia | - | 600 cm | lead | - |
| 2026-11-22 | M | Ancient mesquite | Patagonia | - | 300 cm | hold | - |
| 2026-11-22 | N | A tree I found | - | - | - | hold | - |
- From 14 readers: reader A 2, reader E 2, reader B 1, reader C 1, reader D 1, reader F 1, reader G 1, reader H 1, reader I 1, reader J 1, reader K 1, reader L 1, reader M 1, reader N 1.
- Photographs and the readers' own words: `python3 scripts/inspect_readers.py` (a local page, never in this public file). Your answer goes in with `python3 scripts/judgement.py --feedback <id> "..."`.

**Waiting for you** (what the runs left for you since 2026-11-22)

- 229 email addresses ready to mail (archive 0, nature 9, guide 4, press 122, source 58, council 16, society 7, tourism 5, other 5, garden 3); **the night run found no new contacts in two days**
- none.
- paste supabase/flag-upsert-fix.sql.
- a reply to her is drafted in drafts/reply-reader-1358-2026-11-22b.md.
- drafts/reply-reader-1000126-2026-11-22.md is rewritten to thank them and say the tree is off the map.
- drafts/reply-reader-1000126-2026-11-22.md thanks them and asks for a photograph of the stump, which would take the tree off the same day.
- the website's thank-you after adding a photo says "We look at every photograph before it goes on a page", not true when the tree already has a lead photo (live first).
- block and report on a profile (question 3)
- paste supabase/photo-hearts-who.sql in the Supabase SQL editor.

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-22 | O | The Weeping Beech of Magistratsparken | Malmö | a reader's photograph, published | [live](https://ancienttrees.app/malmo/weeping-beech-of-magistratsparken) |
| 11-22 | P | The Witch Tree of Fanal | Madeira | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/madeira/witch-tree-of-fanal) |
| 11-21 | Q |  | ? | a reader's photograph, published | not live yet |
| 11-21 | R |  | ? | a reader's photograph, published | not live yet |
| 11-21 | R |  | ? | a reader's photograph, published | not live yet |
| 11-21 | S | The Birnam Oak | Dunkeld | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dunkeld/birnam-oak) |
| 11-21 | S | The Fortingall Yew | Fortingall | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/fortingall/fortingall-yew) |
| 11-21 | J | The Chestnut Avenue of the Hauptallee | Vienna | a reader's photograph, published | [live](https://ancienttrees.app/vienna/chestnut-avenue-of-the-hauptallee) |
| 11-21 | T | The Podocarp of Piazza Vittorio | Rome | a reader's photograph, published | [live](https://ancienttrees.app/rome/podocarp-of-piazza-vittorio) |
| 11-21 | U | The Ankerwycke Yew | Runnymede | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/runnymede/ankerwycke-yew) |
| 11-21 | U | The Ankerwycke Yew | Runnymede | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/runnymede/ankerwycke-yew) |
| 11-21 | U | The Ankerwycke Yew | Runnymede | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/runnymede/ankerwycke-yew) |
| 11-21 | U | The Ankerwycke Yew | Runnymede | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/runnymede/ankerwycke-yew) |
| 11-21 | V | The Minster Yard Beech | York | a reader's photograph, published | [live](https://ancienttrees.app/york/minster-yard-beech) |
| 11-21 | W | The Husalle Lindens | Copenhagen | a reader's photograph, published | [live](https://ancienttrees.app/copenhagen/husalle-lindens) |
| 11-21 | J | The Waldmüllerpark Wingnuts | Vienna | a reader's photograph, published | [live](https://ancienttrees.app/vienna/waldmullerpark-wingnuts) |
| 11-21 | X |  | ? | a reader's photograph, published | not live yet |
| 11-21 | Y | The Holm Oak of the National Garden | Athens | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/athens/holm-oak-of-the-national-garden) |
| 11-21 | Z | The Gnarled Beech of Hampstead Heath | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/gnarled-beech-of-hampstead-heath) |
| 11-21 | Y |  | ? | a reader's photograph, published | not live yet |
| 11-21 | Y | The Holm Oak of the National Garden | Athens | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/athens/holm-oak-of-the-national-garden) |
| 11-21 | W | The Søndermarken Oak | Copenhagen | a reader's photograph, published | [live](https://ancienttrees.app/copenhagen/sondermarken-oak) |
| 11-21 | W | The Beech by the Boat Trip | Copenhagen | a reader's photograph, published | [live](https://ancienttrees.app/copenhagen/beech-by-the-boat-trip) |
| 11-21 | R |  | ? | a reader's photograph, published | not live yet |
| 11-21 | A1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | W | The Pedunculate Oak of Frederiksberg Have | Copenhagen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/copenhagen/pedunculate-oak-of-frederiksberg-have) |
| 11-21 | B1 | The Great Ginkgo of Bodaiji | Nagi | a reader's photograph, published | [live](https://ancienttrees.app/nagi/great-ginkgo-of-bodaiji) |
| 11-21 | W | The Catalpa of Haveselskabets Have | Copenhagen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/copenhagen/catalpa-of-haveselskabets-have) |
| 11-21 | K |  | ? | a reader's photograph, published | not live yet |
| 11-21 | Z | The Marylebone Elm | London | a reader's photograph, published | [live](https://ancienttrees.app/london/marylebone-elm) |
| 11-21 | U |  | ? | a reader's photograph, published | not live yet |
| 11-21 | A1 | The Molkenkur Linden | Heidelberg | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/heidelberg/molkenkur-linden) |
| 11-21 | C1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | D1 | The Monterey Cypress at Bishops Knoll | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/monterey-cypress-at-bishops-knoll) |
| 11-21 | E1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | F1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | G1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | F1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | F1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | D1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | H1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | I1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | J1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | K1 | The Bodhi Tree in the Hillside Shrine | Kandy | a reader's photograph, published | [live](https://ancienttrees.app/kandy/bodhi-tree-in-the-hillside-shrine) |
| 11-21 | L1 | The Fort Canning Rain Tree | Singapore | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/singapore/fort-canning-rain-tree) |
| 11-21 | C1 | The Oak of Kiewit | Hasselt | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/hasselt/oak-of-kiewit) |
| 11-21 | M1 | The Katsura-Tree of Morris Arboretum | Philadelphia | a reader's photograph, published | [live](https://ancienttrees.app/philadelphia/katsura-tree-of-morris-arboretum) |
| 11-21 | M1 | The Weeping European Beech at Morris Arboretum | Philadelphia | a reader's photograph, published | [live](https://ancienttrees.app/philadelphia/weeping-european-beech-at-morris-arboretum) |
| 11-21 | M1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | N1 | Tāne Mahuta | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/tane-mahuta) |
| 11-21 | N1 | Te Matua Ngahere | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/te-matua-ngahere) |
| 11-21 | N1 | Te Matua Ngahere | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/te-matua-ngahere) |
| 11-21 | N1 | Te Matua Ngahere | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/te-matua-ngahere) |
| 11-21 | O1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | P1 | The Survivor Tree | Moffat | a reader's photograph, published | [live](https://ancienttrees.app/moffat/survivor-tree) |
| 11-22 | Q1 | The Gennett Poplar | Chattahoochee National Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/chattahoochee-national-forest/gennett-poplar) |
| 11-22 | R1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | S1 | Pando | Fish Lake, Utah | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/fish-lake-utah/pando) |
| 11-22 | T1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | U1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | V1 | The Lime of the Noordeind | Emmen | a reader's photograph, published | [live](https://ancienttrees.app/emmen/lime-of-the-noordeind) |
| 11-22 | V1 | The Plane of the Bonifatius Park | Emmen | a reader's photograph, published | [live](https://ancienttrees.app/emmen/plane-of-the-bonifatius-park) |
| 11-22 | V1 | The Plane by Restaurant Urbana | Zwolle | a reader's photograph, published | [live](https://ancienttrees.app/zwolle/plane-by-restaurant-urbana) |
| 11-22 | V1 | The Copper Beech of Nieuw-Schoonebeek | Emmen | a reader's photograph, published | [live](https://ancienttrees.app/emmen/copper-beech-of-nieuw-schoonebeek) |
| 11-22 | V1 | The Oak at the Long Grave | Emmen | a reader's photograph, published | [live](https://ancienttrees.app/emmen/oak-at-the-long-grave) |
| 11-22 | V1 | Huis de Paddestoel's Swamp Cypress | Zwolle | a reader's photograph, published | [live](https://ancienttrees.app/zwolle/huis-de-paddestoels-swamp-cypress) |
| 11-22 | V1 | The Weeping Beech of Park Boschwijk | Zwolle | a reader's photograph, published | [live](https://ancienttrees.app/zwolle/weeping-beech-of-park-boschwijk) |
| 11-22 | V1 | The Beech of the Boschwijk Avenue | Zwolle | a reader's photograph, published | [live](https://ancienttrees.app/zwolle/beech-of-the-boschwijk-avenue) |
| 11-22 | V1 | The Oak in Hunebed D42 | Emmen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/emmen/oak-in-hunebed-d42) |
| 11-22 | U1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | W1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | W1 | The Llangernyw Yew | Llangernyw | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/llangernyw/llangernyw-yew) |
| 11-22 | D1 | The Monterey Cypress at Bishops Knoll | Bristol | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/bristol/monterey-cypress-at-bishops-knoll) |
| 11-22 | X1 | Thorvaldsen's Robinia | Copenhagen | a reader's photograph, published | [live](https://ancienttrees.app/copenhagen/thorvaldsens-robinia) |
| 11-22 | X1 | The Mulberry of Proviantgarden | Copenhagen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/copenhagen/mulberry-of-proviantgarden) |
| 11-22 | H1 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | Y1 | The Copper Beech of Sint-Willibrorduskerk | Antwerp | a reader's photograph, published | [live](https://ancienttrees.app/antwerp/copper-beech-of-sint-willibrorduskerk) |
| 11-22 | B | The Fern-leaved Beech | Munich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/munich/fern-leaved-beech) |
| 11-22 | Z1 | The Leidsebosje Planes | Amsterdam | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/amsterdam/leidsebosje-planes) |
| 11-22 | A2 | The Plane of Dr. Karl Lueger-Platz | Vienna | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/vienna/plane-of-dr-karl-lueger-platz) |
| 11-22 | A2 | The Pagoda Tree of the Stadtpark | Vienna | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/vienna/pagoda-tree-of-the-stadtpark) |
| 11-22 | B2 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | C2 | Vernon Oak | Sheffield | a reader's photograph, published | [live](https://ancienttrees.app/sheffield/vernon-oak) |
| 11-22 | D2 | The Hundred-Horse Chestnut | Sant'Alfio | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/santalfio/hundred-horse-chestnut) |
| 11-22 | D2 | The Hundred-Horse Chestnut | Sant'Alfio | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/santalfio/hundred-horse-chestnut) |
| 11-22 | E2 | The Witch Tree of Fanal | Madeira | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/madeira/witch-tree-of-fanal) |
| 11-22 | F2 | The Cedar of Lebanon in Victoria Square | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/cedar-of-lebanon-in-victoria-square) |
| 11-22 | G2 | Moreton Bay Figs of Donnafugata Castle Park | Ragusa | a reader's photograph, published | [live](https://ancienttrees.app/ragusa/moreton-bay-figs-of-donnafugata-castle-park) |
| 11-22 | E2 | The Witch Tree of Fanal | Madeira | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/madeira/witch-tree-of-fanal) |
| 11-22 | G2 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | H2 | The Old Mulberry of Taranta | Cassano d'Adda | a reader's photograph, published | [live](https://ancienttrees.app/cassano-dadda/old-mulberry-of-taranta) |
| 11-22 | I2 | The Thousand-Year Oak of Barmstedt | Barmstedt | a reader's photograph, published | [live](https://ancienttrees.app/barmstedt/thousand-year-oak-of-barmstedt) |
| 11-22 | J2 | The Weeping Willow of Via Dante Alighieri | Bagnolo San Vito | a reader's photograph, published | [live](https://ancienttrees.app/bagnolo-san-vito/weeping-willow-of-via-dante-alighieri) |
| 11-22 | K2 | The Evelyn Mulberry | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/evelyn-mulberry) |
| 11-22 | L2 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | L2 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | A |  | ? | a reader's photograph, published | not live yet |
| 11-22 | A |  | ? | a reader's photograph, published | not live yet |
| 11-22 | I |  | ? | a reader's photograph, published | not live yet |
| 11-22 | M2 | The Fig of the Glorieta de Goya | Seville | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/seville/fig-of-the-glorieta-de-goya) |
| 11-22 | F | The Linden of Linn | Zurich | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/zurich/linden-of-linn) |
| 11-22 | N2 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | A | The Plaque Tree on the Shore of Ribeirão da Ilha | Florianópolis | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/florianopolis/plaque-tree-on-the-shore-of-ribeirao-da-ilha) |
| 11-22 | A | The Fig of the Hanging Roots in Coqueiros | Florianópolis | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/florianopolis/fig-of-the-hanging-roots-in-coqueiros) |
| 11-22 | J | The Alois-Drasche-Park Beech | Vienna | a reader's photograph, published | [live](https://ancienttrees.app/vienna/alois-drasche-park-beech) |
| 11-22 | V1 | The Coronation Lime of the Spanderslaan | Hilversum | a reader's photograph, published | [live](https://ancienttrees.app/hilversum/coronation-lime-of-the-spanderslaan) |
| 11-22 | V1 | The Bernhard Chestnut of the Hilvertsweg | Hilversum | a reader's photograph, published | [live](https://ancienttrees.app/hilversum/bernhard-chestnut-of-the-hilvertsweg) |
| 11-22 | V1 | The Juliana Lime of the Hilvertsweg | Hilversum | a reader's photograph, published | [live](https://ancienttrees.app/hilversum/juliana-lime-of-the-hilvertsweg) |
| 11-22 | L | Boab Prison Tree | Derby | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/derby/boab-prison-tree) |
| 11-22 | O2 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | P2 | The Argyle Street Ash | Glasgow | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/glasgow/argyle-street-ash) |
| 11-22 | O2 | The Cedar of Jussieu | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/cedar-of-jussieu) |
| 11-22 | Q2 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | O2 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | R2 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | S2 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | T2 | The Lehmann Plane of Planten un Blomen | Hamburg | a reader's photograph, published | [live](https://ancienttrees.app/hamburg/lehmann-plane-of-planten-un-blomen) |
| 11-22 | T2 | The Japanese Pagoda Tree of Alsterufer | Hamburg | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/hamburg/japanese-pagoda-tree-of-alsterufer) |
| 11-22 | U2 | The Bur Oak by the Cuvier Gate | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/bur-oak-by-the-cuvier-gate) |
| 11-22 | M1 |  | ? | a reader's photograph, published | not live yet |
| 11-23 | V2 | Paavola's Oak | Lohja | a reader's photograph, published | [live](https://ancienttrees.app/lohja/paavolas-oak) |
| 11-23 | R1 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | D1 | The Monterey Cypress at Bishops Knoll | Bristol | a reader's correction changed the page | - |
| 11-21 | I1 | Plane tree | Le Porge | a reader's tree changed the page | - |
| 11-21 | M1 | The Katsura-Tree of Morris Arboretum | Philadelphia | a reader's correction changed the page | - |
| 11-21 | M1 | The Weeping European Beech at Morris Arboretum | Philadelphia | a reader's correction changed the page | - |
| 11-21 | M1 | The Katsura-Tree of Morris Arboretum | Philadelphia | a reader's correction changed the page | - |
| 11-21 | X | The Castle Linden of Cmurek | Trate | a reader's correction changed the page | - |
| 11-22 | W2 | The Old Jarrah Tree | Perth | a reader's correction changed the page | - |
| 11-22 | A | Fig | - | a reader's correction changed the page | - |
| 11-22 | R2 | The cedar of Himalaya | Verona | a reader's tree changed the page | - |
- From 68 readers: reader V1 12, reader M1 7, reader A 5, reader U 5, reader W 5, reader D1 4, reader N1 4, reader F1 3, reader J 3, reader O2 3, reader R 3, reader Y 3, reader A1 2, reader A2 2, reader C1 2, reader D2 2, reader E2 2, reader G2 2, reader H1 2, reader I1 2, reader L2 2, reader R1 2, reader R2 2, reader S 2, reader T2 2, reader U1 2, reader W1 2, reader X 2, reader X1 2, reader Z 2, reader B 1, reader B1 1, reader B2 1, reader C2 1, reader E1 1, reader F 1, reader F2 1, reader G1 1, reader H2 1, reader I 1, reader I2 1, reader J1 1, reader J2 1, reader K 1, reader K1 1, reader K2 1, reader L 1, reader L1 1, reader M2 1, reader N2 1, reader O 1, reader O1 1, reader P 1, reader P1 1, reader P2 1, reader Q 1, reader Q1 1, reader Q2 1, reader S1 1, reader S2 1, reader T 1, reader T1 1, reader U2 1, reader V 1, reader V2 1, reader W2 1, reader Y1 1, reader Z1 1.

**What was sent in, and what we decided**

| seen | what | where | size for its species | ours | Hidde |
|---|---|---|---|---|---|
| 2026-11-23 | The Tree House Rain Tree of the Netrav | Mangaluru | - | open | - |
| 2026-11-20 | Tyler Arboretum Giant Sequoia | Media | - | lead | - |
| 2026-11-19 | The Ivy Elm of Park Oliwski | Gdansk | - | hold | - |
| 2026-11-19 | A tree I found | - | - | hold | - |
| 2026-11-19 | The Amur Cork Trees and Crimean Linden | Vilnius | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | lead | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | lead | - |
| 2026-11-18 | A tree I found | - | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | The Southern Mahogany of Edinburgh Gar | Melbourne | - | hold | - |
| 2026-11-18 | The Casuarina of the Cascada | Barcelona | - | hold | - |
| 2026-11-18 | a tree we do not map | - | - | lead | - |
| 2026-11-17 | Ahuehuete del Jardin de San Fernando | Mexico City | - | hold | - |
| 2026-11-17 | The Cosgrove House Banyan | Key West | - | hold | - |

2 waiting for a verdict. Disagree with one and the rule changes: `python3 scripts/judgement.py --feedback <id> "..."`, and `--learn` prints every verdict he has overruled.

**Searched yesterday:** milano (9 times), hove (5 times), italy (5 times), bristol (4 times), auckland (3 times), brighton (3 times), ital (3 times), lon (3 times), madrid (3 times), mila (3 times), milan (3 times), palermo (3 times), perth (3 times), roma (3 times), toronto (3 times), victoria (3 times), baltimore (2 times), biella (2 times), bologna (2 times), como (2 times).

**App crashes** (last 7 days, store builds; MetricKit, a sample)

| Crashes | Kind | Build | Where | Phones | Last | Fix |
|---:|---|---|---|---:|---|---|
| 1 | crash | 1.0.4 (41) | AncientTrees+0x2409a0 | 1 | 2026-11-16 | none |
| 1 | crash | 1.0.4 (41) | AncientTrees+0x35fccc | 1 | 2026-11-20 | none |
| 1 | hang | 1.0.4 (41) | AncientTrees+0x376463 | 1 | 2026-11-21 | none |

Search Console: fetch failed today (HTTP Error 400: Bad Request); numbers resume tomorrow.

**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-16 | 211 | 15 | 7.1% |
| 11-17 | 170 | 6 | 3.5% |
| 11-18 | 177 | 9 | 5.1% |
| 11-19 | 226 | 8 | 3.5% |
| 11-20 | 222 | 13 | 5.9% |
| 11-21 | 242 | 3 | 1.2% |
| 11-22 | - | - | 0.0% |
| **7 days** | **1248** | **54** | **4.3%** |
- Week before: 934 impressions, 48 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); ancient trees app (c7/i33, p4); platane du square des batignolles (c4/i2, p1); picture of the tree in helsinki city center that was preserved (c3/i2, p4); 太閤シダレザクラ (c3/i2, p5); evelyns mulberry (c3/i1, p3); ancient trees app (c2/i8, p5); who planted the western red cedar tree in blarney ireland (c2/i8, p2)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

**Monday: the slow tables.** They rarely change a day's decision, so they come once a week.

**Website actions, ever** (the events table begins 2026-08-01, when the funnel was repaired; a zero has never fired at all)

| Action | Ever |
|---|---:|
| app-cta | 287 |
| search-home | 143 |
| waitlist-submit | 53 |
| visitors-page | 46 |
| signin-open | 35 |
| search-bar-m | 23 |
| home-visitors | 22 |
| home-fav | 22 |
| search-none-home | 20 |
| home-country | 15 |
| search-bar | 14 |
| search-explore | 12 |
| signin-oauth | 12 |
| share_arrived | 10 |
| share_tapped | 10 |
| search-empty-home | 9 |
| signin-done | 9 |
| app-open | 6 |
| home-oldest | 5 |
| directions | 5 |
| suggestion-submit | 4 |
| home-species | 4 |
| worthit-worth it | 4 |
| home-dir-species | 3 |
| save | 3 |
| tree-photo-sent | 3 |
| visit | 3 |
| search-empty-explore | 3 |
| signin-link-sent | 3 |
| search-none-bar | 3 |
| empty-place-add | 2 |
| search-none-explore | 2 |
| home-dir-collection | 1 |
| plus-open | 1 |
| search-empty-bar-m | 1 |
| sponsor-open | 1 |
| home-dir-city | 1 |
| worthit-not worth it | 0 |
| **all** | **800** |

**App events, ever** (measured since 2026-08-30)

| What | Ever |
|---|---:|
| app_open | 11721 |
| tab | 6764 |
| tree_opened | 20023 |
| directions | 497 |
| tree_saved | 758 |
| tree_visited | 371 |
| sighting_recorded | 818 |
| sync_skipped | 0 |
| sync_failed | 6 |
| location | 7204 |
| pin_tapped | 836 |
| share_tapped | 333 |
| map_moved | 188 |
| plus-open | 149 |
| app_exit_abnormal | 50 |
| plus-answer | 15 |
| plus-tellme | 3 |
| $exception | 1 |
| **all** | **49737** |

**What readers told us** (7 days, structure only; the words stay in the database)

| Day | Tree | What | Note | From | Outcome |
|---|---|---|---|---|---|
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
| 11-16 | 9CDC79F8-530A-48D5-B9EA-C51D1F28D5 | tree sent in | 67 chars, read it in the database | de08 | holds |
| 11-16 | 0269D848-F4E2-40DB-9157-8F6F951A34 | tree sent in | - | 6f92 | - |
| 11-16 | Boab | correction sent in | 89 chars, read it in the database | de08 | holds |
| 11-16 | 6BB3D492-EA79-4B08-8F63-A66610632B | tree sent in | - | 24da | - |
| 11-16 | DE83AEF2-D85E-4D38-B4EF-73E6365D25 | tree sent in | 1154 chars, read it in the database | de08 | - |
| 11-16 | Boab | correction sent in | 89 chars, read it in the database | de08 | holds |
| 11-16 | Cat Island Bald Cypress | tree sent in | 118 chars, read it in the database | 360c | - |
| 11-16 | 42A31D57-D883-4E4E-9967-EC876A4C40 | tree sent in | - | cc87 | - |
| 11-16 | Ancient totara tree | tree sent in | 59 chars, read it in the database | 250e | changed |
| 11-16 | 92FAC7A0-332E-4B6B-8D54-463B3E592C | tree sent in | - | 9b3c | - |
| 11-16 | elh_001 (Elleholmseken (The Oak of | worth it | - | 59bc | - |
| 11-16 | Millennium Tree of Balete Park | correction sent in | 94 chars, read it in the database | 580c | holds |
| 11-16 | isp_001 (The Plane of Çınar Sokak) | correction sent in | 92 chars, read it in the database | c208 | changed |
| 11-16 | bai_001 (The Gomero de la Recoleta | worth it | - | 04af | - |
| 11-16 | Colchester | ambassador request | - | 4a6e | - |
| 11-16 | sqj_001 (Enchanted Balete Tree of  | worth it | - | 83b7 | - |
| 11-16 | stw_001 (The north door yews of St | worth it | - | 0071 | - |
| 11-16 | E0402F44-1B12-431A-9901-7974F79CCB | tree sent in | 257 chars, read it in the database | 2d8d | - |
| 11-16 | seq_001 (General Sherman Tree) | worth it | - | 24da | - |
| 11-16 | seq_004 (Lincoln Tree) | worth it | - | 24da | - |
| 11-16 | 2AF51C4D-954D-4EBF-AC1F-82DCD5EF4A | tree sent in | - | 365a | - |
| 11-16 | pal_001 (The Ficus of Piazza Marin | worth it | - | f810 | - |
| 11-16 | pal_001 (The Ficus of Piazza Marin | vote undone | worth it | f810 | - |
| 11-16 | pal_001 (The Ficus of Piazza Marin | worth it | - | f810 | - |
| 11-16 | pal_003 (The Ficus of the Orto Bot | worth it | - | f810 | - |
| 11-16 | pal_022 (The White Fig of Villino  | worth it | - | f810 | - |
| 11-16 | aus_001 (The Treaty Oak) | worth it | - | f810 | - |
| 11-16 | par_010 (The Sophora by the Lake) | worth it | - | f810 | - |
| 11-16 | 1500 old olive tree | tree sent in | 87 chars, read it in the database | 744b | changed |
| 11-16 | ath_001 (The Sacred Olive Tree of  | worth it | - | bcf4 | - |
| 11-16 | Linden tree next to the pond | tree sent in | 79 chars, read it in the database | 744b | - |
| 11-16 | A tree I found | correction sent in | 91 chars, read it in the database | 24da | holds |
| 11-16 | F91BD966-DB25-4276-91CE-9FB1C58063 | tree sent in | 1475 chars, read it in the database | 24da | - |
| 11-16 | The Champion Lodgepole Pine | correction sent in | 91 chars, read it in the database | 24da | changed |
| 11-16 | bri_001 (The Domesday Oak) | report | 166 chars | bcd5 | holds |
| 11-16 | 5126EC15-4F8A-45AD-9FA1-996FE64483 | tree sent in | 3705 chars, read it in the database | d5cb | open_question |
| 11-16 | The 180-year-old Moreton Bay Fig a | tree sent in | 341 chars, read it in the database | a622 | - |
| 11-16 | 657DD07E-F174-4CD5-8B89-CB0A88CD8E | tree sent in | - | d0a8 | - |
| 11-16 | The 800-year-old Big Tree in Tsits | tree sent in | 201 chars, read it in the database | a622 | - |
| 11-16 | tok_009 (The Meiji Jingu Gaien Gin | worth it | - | 24da | - |
| 11-16 | The Meiji Jingu Gaien Ginkgo Avenu | correction sent in | 92 chars, read it in the database | 24da | holds |
| 11-16 | The Famous Nossob Camel Thorn Tree | tree sent in | 242 chars, read it in the database | a622 | - |
| 11-16 | South Africa's largest indigenous  | tree sent in | 313 chars, read it in the database | a622 | - |
| 11-16 | kmk_003 (The Tabunoki of the Goryo | report | 86 chars | 7326 | changed |
| 11-16 | The Tassili cypress | tree sent in | 98 chars, read it in the database | 602c | open_question |
| 11-16 | bil_002 (The Bald Cypress of Deust | worth it | - | 8e14 | - |
| 11-16 | The Bald Cypress of Deusto | correction sent in | 92 chars, read it in the database | 8e14 | changed |
| 11-16 | 5784282E-F1A8-4516-AB2E-CCE4D2F0F3 | tree sent in | 43 chars, read it in the database | 2f47 | - |
| 11-16 | Pendulate Oak | tree sent in | 318 chars, read it in the database | 365a | - |
| 11-16 | tku_001 (Kalm's Oak) | worth it | - | ed29 | - |
| 11-16 | 68515BBD-0BDC-475A-BB16-5E8E324DB9 | tree sent in | 96 chars, read it in the database | 852b | - |
| 11-16 | bil_004 (The Centenary Horse Chest | worth it | - | 8e14 | - |
| 11-16 | The Centenary Horse Chestnut of Pa | correction sent in | 92 chars, read it in the database | 8e14 | holds |
| 11-16 | snd_001 (The Sunderland Buttonball | worth it | - | 356b | - |
| 11-16 | BFC89932-0E03-486F-9857-72E11AF252 | report | 159 chars | 8d68 | holds |
| 11-16 | B4902EF7-A641-4D4D-86C4-98B316DA87 | tree sent in | - | 89fe | - |
| 11-16 | Yew | tree sent in | 299 chars, read it in the database | 2f1a | changed |
| 11-16 | stb_004 (The Melaleuca That Grows  | worth it | - | c550 | - |
| 11-16 | stb_004 (The Melaleuca That Grows  | vote undone | worth it | c550 | - |
| 11-16 | stb_004 (The Melaleuca That Grows  | worth it | - | c550 | - |
| 11-16 | stb_004 (The Melaleuca That Grows  | vote undone | worth it | c550 | - |
| 11-16 | stb_004 (The Melaleuca That Grows  | worth it | - | c550 | - |
| 11-16 | Leccio (Quercus Ilex) nel piazzale | tree sent in | 34 chars, read it in the database | e1e3 | - |
| 11-16 | bil_003 (The Centenary Trees of Pa | worth it | - | 8e14 | - |
| 11-16 | ber_016 (The Lietzensee Plane) | worth it | - | 9c8a | - |
| 11-16 | The Centenary Trees of Parque de l | correction sent in | 92 chars, read it in the database | 8e14 | holds |
| 11-16 | Chestnut "Miraglia" | tree sent in | 874 chars, read it in the database | 0f74 | - |
| 11-16 | The Blaise Meadow Sweet Chestnut | correction sent in | 93 chars, read it in the database | 2215 | holds |
| 11-16 | C5A1FD34-70E8-4A81-9496-4E32EDB809 | tree sent in | - | bd74 | - |
| 11-16 | stb_010 (The Peruvian Pepper of th | worth it | - | c550 | - |
| 11-16 | F254C136-8A64-4005-8939-29DB9A7D38 | tree sent in | - | 195b | - |
| 11-16 | The Cedar of Lebanon at Blaise Cas | correction sent in | 93 chars, read it in the database | 2215 | holds |
| 11-16 | bri_003 (The Cedar of Lebanon at B | report | 41 chars | 2215 | changed |
| 11-16 | bri_017 (The Blaise Meadow Sweet C | report | 41 chars | 2215 | holds |
| 11-16 | A tree near Llanfihangel-nant-Mela | correction sent in | 88 chars, read it in the database | c344 | holds |
| 11-16 | Quercia del Parco Massari di Ferra | tree sent in | 361 chars, read it in the database | 7e0c | changed |
| 11-16 | Balmerino Chestnut | tree sent in | 81 chars, read it in the database | 6939 | changed |
| 11-16 | 1BE89823-692C-46DD-BB1C-BE7DBD6ED0 | tree sent in | - | 6f79 | open_question |
| 11-16 | Pioppo bianco dell'Oasi Lagoverde  | tree sent in | 678 chars, read it in the database | 7e0c | changed |
| 11-16 | 230A268F-5AAE-4C91-B133-15982A3ED8 | tree sent in | - | c735 | - |
| 11-16 | E3F862E3-EE04-4D1E-BAF8-49AC5BE624 | tree sent in | - | c735 | - |
| 11-16 | lax_011 (The Huntington Rose Garde | report | on the map twice | bb36 | changed |
| 11-16 | 4CEC5259-AC92-4A7A-9C4C-9F6DDD1ACD | tree sent in | - | c735 | - |
| 11-16 | Portuguese Oak in Lisbon | correction sent in | 89 chars, read it in the database | c735 | holds |
| 11-16 | 7F0038BA-2D3C-4BF4-A206-135905BFF0 | tree sent in | - | 7e27 | - |
| 11-16 | 00FD8D2F-72A7-44C8-9D4A-7F1EB53804 | tree sent in | 33 chars, read it in the database | 65f1 | - |
| 11-16 | DF10CD8A-F0F4-4911-A37F-B5B4E85B74 | tree sent in | 85 chars, read it in the database | 65f1 | - |
| 11-16 | Sydney | ambassador request | - | 750e | - |
| 11-16 | A069351F-FE5C-40FA-9B6A-EFAB20714B | tree sent in | - | 750e | - |
| 11-16 | 665082D2-815B-4630-883A-5F619725CD | tree sent in | 53 chars, read it in the database | 81aa | - |
| 11-16 | 993D2833-D88B-43CC-A6E2-804C1E2C69 | report | 386 chars | 81aa | holds |
| 11-16 | B43D0C0B-469B-44EF-AB4B-BBA2C7B8F7 | tree sent in | - | 951e | - |
| 11-16 | The Yew of Nicorps (If commun de N | correction sent in | 91 chars, read it in the database | 7fec | changed |
| 11-16 | Oriental Plane in Cambridge | correction sent in | 91 chars, read it in the database | 951e | holds |
| 11-16 | B451D1E8-4B8B-4BB0-9680-01874B41C2 | tree sent in | 167 chars, read it in the database | 8380 | - |
| 11-16 | 60878254-21F7-4E0D-8D06-91700DB3E0 | tree sent in | - | a422 | - |
| 11-17 | It is a specimen of the species Fi | tree sent in | 134 chars, read it in the database | f094 | - |
| 11-17 | 4887A7BF-C121-4574-A1F0-8944F1AC00 | tree sent in | 93 chars, read it in the database | 74c9 | - |
| 11-17 | AE132F45-019F-4E63-9723-98DD6E8158 | tree sent in | 75 chars, read it in the database | b54c | - |
| 11-17 | B3D97FD9-33CF-40BC-A557-1C8DCCBFEC | tree sent in | 660 chars, read it in the database | b54c | - |
| 11-17 | 968C829E-EFFD-4454-8B9C-271DA4D798 | tree sent in | 213 chars, read it in the database | b54c | - |
| 11-17 | EC026F7B-A1B8-4316-B8EA-07C111061C | tree sent in | 451 chars, read it in the database | b54c | - |
| 11-17 | A48CAE8C-F582-4CA2-B055-05C4020FCA | tree sent in | 722 chars, read it in the database | b54c | - |
| 11-17 | B41E05CE-7F7E-4AEB-A19E-E1C2526623 | tree sent in | 246 chars, read it in the database | b54c | - |
| 11-17 | B730ACCA-9B47-4CE7-9EBC-5CA8499AC7 | tree sent in | - | 09fe | - |
| 11-17 | River Red Gum near Adelaide | correction sent in | 88 chars, read it in the database | 09fe | holds |
| 11-17 | E4CABEA6-FB02-470F-B13C-7851EB3553 | tree sent in | - | 8d3c | - |
| 11-17 | Oriental Plane in Cambridge | correction sent in | 91 chars, read it in the database | 951e | open_question |
| 11-17 | - | https | 193 chars | 240f | holds |
| 11-17 | B465300F-F064-4C38-9FB9-D3FE2E44E2 | tree sent in | 152 chars, read it in the database | 67c0 | - |
| 11-17 | Pedunculate Oak near Winterswijk | correction sent in | 89 chars, read it in the database | 67c0 | changed |
| 11-17 | 19C1B08D-8577-4E2B-A30F-5827ECF2F6 | tree sent in | 381 chars, read it in the database | ec87 | - |
| 11-17 | Sofia | ambassador request | - | c2da | - |
| 11-17 | Bergmammutbaum im Arboretum 1 | tree sent in | 103 chars, read it in the database | a54a | - |
| 11-17 | Romantik-Eiche | tree sent in | 81 chars, read it in the database | a54a | - |
| 11-17 | Holdermanns-Eiche | tree sent in | 37 chars, read it in the database | a54a | - |
| 11-17 | 0DDAD207-52BA-4A72-8F76-64B3A09F27 | tree sent in | 35 chars, read it in the database | 2335 | - |
| 11-17 | Banyan Tree | tree sent in | 132 chars, read it in the database | a54a | - |
| 11-17 | C936DB57-EABF-4CFF-A8E9-B5AC94850A | tree sent in | 22 chars, read it in the database | 4b18 | open_question |
| 11-17 | American Sycamore at Pawling Farm  | correction sent in | 89 chars, read it in the database | 3471 | changed |
| 11-17 | C4B5F1B1-CE96-469B-805D-CF75390B79 | tree sent in | 186 chars, read it in the database | 3471 | - |
| 11-17 | 074C0198-62AD-43B5-847C-303B146542 | report | 161 chars | b200 | holds |
| 11-17 | 0D0EB3F0-BFE3-4863-8BDF-D594E43512 | tree sent in | - | 86c2 | - |
| 11-17 | - | There’s an ancient yew tree St Hel | - | 5e0a | open_question |
| 11-17 | 0BA575C4-D0B6-4503-B903-7BDC37A45C | tree sent in | - | 8ced | - |
| 11-17 | The St Paul's Churchyard Planes | correction sent in | 91 chars, read it in the database | 9c7a | changed |
| 11-17 | 5E81AF24-C36D-4B03-A6ED-92B1030CCC | tree sent in | 47 chars, read it in the database | 666e | - |
| 11-17 | - | Hi! There are many ancient trees i | - | d56e | holds |
| 11-17 | 2BEF0F92-BD67-4694-8CEE-C97B5F4D3C | tree sent in | 332 chars, read it in the database | 9887 | - |
| 11-17 | lon_003 (The Cheapside Plane) | report | 65 chars | 9c7a | holds |
| 11-17 | 7B889995-25DA-415C-8C05-AFC5A69BFE | tree sent in | - | bfde | - |
| 11-17 | - | new favorite app!!!! anyways how c | - | 9887 | holds |
| 11-17 | 58EFDC92-C382-4B03-B495-C53F027B4E | tree sent in | - | 8f30 | - |
| 11-17 | 4EA907D1-6637-4070-AA8A-9A9D66A71F | tree sent in | 41 chars, read it in the database | 8f30 | - |
| 11-17 | C4A7A901-5433-4336-8CD7-E4317741AA | tree sent in | - | bfde | - |
| 11-17 | Orange | correction sent in | 89 chars, read it in the database | bfde | holds |
| 11-17 | Monterey Pine | correction sent in | 89 chars, read it in the database | bfde | holds |
| 11-17 | F8C010FC-A646-477E-B1F8-DC71C5562E | tree sent in | - | 7395 | - |
| 11-17 | 0305569A-654F-4BB4-9818-A071E60265 | tree sent in | 75 chars, read it in the database | e542 | - |
| 11-17 | BB61E294-5FFB-4378-960A-64DAB336FD | tree sent in | - | e542 | - |
| 11-17 | Budapest | ambassador request | - | 72bf | - |
| 11-17 | Horse Chestnut Tree of Sofienbergp | tree sent in | 79 chars, read it in the database | a54a | changed |
| 11-17 | CAA9C183-3017-433B-A1CA-09E1CAA99B | tree sent in | - | 583a | - |
| 11-17 | 034185B2-9235-4AE9-BA01-54B4FA02CD | tree sent in | - | 583a | - |
| 11-17 | E080B473-D617-4BC1-B917-92D5F0B8AB | tree sent in | - | 798e | - |
| 11-17 | The Signal Tree (Native American'I | tree sent in | 750 chars, read it in the database | 0ec0 | - |
| 11-17 | 9620278D-6885-4B27-B86B-E5211E651A | tree sent in | - | 6f7d | - |
| 11-17 | 4FE1CB00-E56F-42E1-8C89-EC11BC883F | tree sent in | 197 chars, read it in the database | 5142 | - |
| 11-17 | vfg_001 (The Sprawling Sycamore of | report | 104 chars | 3471 | holds |
| 11-17 | vfg_001 (The Sprawling Sycamore of | report | 113 chars | 3471 | holds |
| 11-18 | 12A88725-88E2-4A96-85F6-0966BB59DB | tree sent in | 58 chars, read it in the database | 9d3c | - |
| 11-18 | - | Hi, 

Is there a possibility to ad | - | 35c2 | open_question |
| 11-18 | 991C4102-F159-48B7-88BA-5B82DDC15E | tree sent in | - | d757 | open_question |
| 11-18 | E2A41777-04A8-4864-AAD1-99A9A84BB6 | tree sent in | 70 chars, read it in the database | 24da | - |
| 11-18 | Oriental Plane in Cambridge | correction sent in | 91 chars, read it in the database | 951e | holds |
| 11-18 | 97153CBF-443D-4B42-9801-7463164ED7 | tree sent in | - | 951e | - |
| 11-18 | The Great Indian Banyan Tree | correction sent in | 91 chars, read it in the database | 951e | holds |
| 11-18 | 9E9C5F14-9E15-4617-905B-61D19E0EE3 | tree sent in | - | 327e | - |
| 11-18 | 1BC207E7-A722-4962-95F7-F1AB5A3485 | tree sent in | 72 chars, read it in the database | 24da | open_question |
| 11-18 | 45248B7C-02B4-4B01-BF83-0DD8B4C6FD | I could be an Edinburgh Ambassador | - | f924 | - |
| 11-18 | A giant sequoia | Yes it is, there is some more info | - | 7091 | - |
| 11-18 | F249D2AC-4E34-4BDF-9919-626A212DE1 | Brilliant many thanks!
It’s a grea | 65 chars | e1ef | - |
| 11-18 | Tule Tree - cypress | Hi, I looked up Oaxaca, hence my m | - | 1fce | - |
| 11-18 | AAC60386-7889-4A79-831D-3B506278D4 | Dear Ancient Trees person (are you | 97 chars | a926 | - |
| 11-18 | The Old banyan at the office of Nh | Hi
Yes it's visible from the sidew | - | da7c | - |
| 11-18 | C4B5F1B1-CE96-469B-805D-CF75390B79 | Thank you so much! I’m loving the  | - | 3471 | - |
| 11-18 | 45248B7C-02B4-4B01-BF83-0DD8B4C6FD | I don't know much about it, but he | - | f924 | - |
| 11-18 | C4B5F1B1-CE96-469B-805D-CF75390B79 | ﻿This is great, Hidde!

May I star | 165 chars | 3471 | - |
| 11-18 | Tule Tree - cypress | Dear Hidde,

Thanks well, I'm deli | 113 chars | 1fce | - |
| 11-18 | FF8F7EAC-05BB-4474-A1BF-B44629A370 | Hia!

For the “Big Totara", those  | - | 3e41 | - |
| 11-18 | The Tassili cypress | Hello Ancient Trees
I took the pho | - | 602c | - |
| 11-18 | 5E81AF24-C36D-4B03-A6ED-92B1030CCC | 😊

Simon Wakefield reacted via Gma | 108 chars | 666e | - |
| 11-18 | - | We are very close to both the Nant | - | acda | - |
| 11-18 | 97153CBF-443D-4B42-9801-7463164ED7 | Hey,

Yes, its the Plane in Emmanu | - | 951e | - |
| 11-18 | 97153CBF-443D-4B42-9801-7463164ED7 | Of course | 33 chars | 951e | - |
| 11-18 | 45248B7C-02B4-4B01-BF83-0DD8B4C6FD | I could be an Edinburgh Ambassador | - | f924 | - |
| 11-18 | A giant sequoia | Yes it is, there is some more info | - | 7091 | - |
| 11-18 | F249D2AC-4E34-4BDF-9919-626A212DE1 | Brilliant many thanks!
It’s a grea | 65 chars | e1ef | - |
| 11-18 | Tule Tree - cypress | Hi, I looked up Oaxaca, hence my m | - | 1fce | - |
| 11-18 | AAC60386-7889-4A79-831D-3B506278D4 | Dear Ancient Trees person (are you | 97 chars | a926 | - |
| 11-18 | The Old banyan at the office of Nh | Hi
Yes it's visible from the sidew | - | da7c | - |
| 11-18 | C4B5F1B1-CE96-469B-805D-CF75390B79 | Thank you so much! I’m loving the  | - | 3471 | - |
| 11-18 | 45248B7C-02B4-4B01-BF83-0DD8B4C6FD | I don't know much about it, but he | - | f924 | - |
| 11-18 | C4B5F1B1-CE96-469B-805D-CF75390B79 | ﻿This is great, Hidde!

May I star | 165 chars | 3471 | - |
| 11-18 | Tule Tree - cypress | Dear Hidde,

Thanks well, I'm deli | 113 chars | 1fce | - |
| 11-18 | FF8F7EAC-05BB-4474-A1BF-B44629A370 | Hia!

For the “Big Totara", those  | - | 3e41 | - |
| 11-18 | The Tassili cypress | Hello Ancient Trees
I took the pho | - | 602c | - |
| 11-18 | 5E81AF24-C36D-4B03-A6ED-92B1030CCC | 😊

Simon Wakefield reacted via Gma | 108 chars | 666e | - |
| 11-18 | - | We are very close to both the Nant | - | acda | - |
| 11-18 | 97153CBF-443D-4B42-9801-7463164ED7 | Hey,

Yes, its the Plane in Emmanu | - | 951e | - |
| 11-18 | 97153CBF-443D-4B42-9801-7463164ED7 | Of course | 33 chars | 951e | - |
| 11-18 | D419093C-142B-4FB7-9A9D-962863C404 | tree sent in | 42 chars, read it in the database | 7d0a | - |
| 11-18 | 2D01C8DC-05B6-421A-B6AA-6E113740A1 | tree sent in | - | e028 | - |
| 11-18 | DF9042BD-471F-4E5B-B9F4-8BD8730C23 | tree sent in | 2447 chars, read it in the database | 24da | - |
| 11-18 | A tree I found | correction sent in | 91 chars, read it in the database | 951e | holds |
| 11-18 | 94BE5B76-FD13-46B8-965D-0486DD325D | tree sent in | - | 951e | - |
| 11-18 | Rain tree , National Gallery of Mo | correction sent in | 91 chars, read it in the database | 951e | holds |
| 11-18 | 853A4B12-0595-4189-8E63-1771C3B8CA | tree sent in | - | 951e | - |
| 11-18 | The Great Oriental Plane of Emmanu | correction sent in | 113 chars, read it in the database | 951e | holds |
| 11-18 | nyc_027 (The English Elm of Fort G | report | 79 chars | ed87 | changed |
| 11-18 | C60F88D1-BC14-496A-ABA8-7B90D72869 | tree sent in | 33 chars, read it in the database | 78d5 | - |
| 11-18 | Oak near Copenhagen | correction sent in | 89 chars, read it in the database | 78d5 | holds |
| 11-18 | - | Thanks Hidde. Love the app. I'll b | 51 chars | acda | - |
| 11-18 | - | Thanks Hidde. Love the app. I'll b | 51 chars | acda | - |
| 11-18 | D97CC4C1-C95A-4FF8-B540-A3C20A5421 | tree sent in | 92 chars, read it in the database | d54c | - |
| 11-18 | A882DCB4-1257-47BD-960B-769863F8BA | tree sent in | 750 chars, read it in the database | 2703 | - |
| 11-19 | 7BF536D3-50D1-49F7-8DED-90A84364AC | tree sent in | - | d54c | - |
| 11-19 | 8088D133-B9FE-4AB2-9F16-9C673C1265 | tree sent in | - | a0f3 | - |
| 11-19 | 13CFB80C-819A-4875-A382-2D95F3156B | tree sent in | - | e837 | - |
| 11-19 | Fort Screven Bakery Oak | correction sent in | 88 chars, read it in the database | e837 | holds |
| 11-19 | E6963B72-7820-4989-BD78-F36B52607E | tree sent in | - | e837 | - |
| 11-19 | 8350D39B-7429-41C8-B1E6-18F499D6DF | tree sent in | - | e837 | - |
| 11-19 | 83BB9866-51C0-4012-B95F-A83EC51EA1 | tree sent in | - | e837 | - |
| 11-19 | 1D409917-A8FF-4792-9A65-551E607A6D | tree sent in | - | e837 | - |
| 11-19 | 6AE2D9B6-0162-4005-9AAC-C047D60CD0 | tree sent in | - | e837 | - |
| 11-19 | 1A16EAEC-2A91-4864-8C72-35D0DD2D5D | tree sent in | - | e837 | - |
| 11-19 | 69BE172D-CD73-4193-A6B9-D12DF857D7 | tree sent in | - | e837 | - |
| 11-19 | D4F02AA3-8E55-4F95-833A-EE47C9394B | tree sent in | - | e837 | - |
| 11-19 | A3EA97CE-6E19-436C-99BE-618DC3C487 | tree sent in | - | e837 | - |
| 11-19 | ads_002 (The Red Gum of Glynburn R | report | 68 chars | 6aa2 | holds |
| 11-19 | 4FE1CB00-E56F-42E1-8C89-EC11BC883F | Thank you. I don’t live here so ca | - | 5142 | holds |
| 11-19 | Ginkgo biloba (var. epiphylla) on  | tree sent in | 90 chars, read it in the database | ece5 | - |
| 11-19 | gda_009 (The Cucumber Magnolia of  | report | 67 chars | 7bb5 | holds |
| 11-19 | gda_009 (The Cucumber Magnolia of  | report | 119 chars | 7bb5 | holds |
| 11-19 | C7DCA666-5183-4987-B585-0F10639B5C | ﻿Hello
Thank you very much for you | - | 6ec2 | changed |
| 11-19 | Old Knobbley | I am on Android but will do wheb I | - | 63b2 | - |
| 11-19 | F8D4D7F9-5CA6-429D-8016-D34FF35182 | tree sent in | 269 chars, read it in the database | ecbd | - |
| 11-19 | 81FF86AB-2B28-43B7-81BE-D71C2FCDCE | tree sent in | 87 chars, read it in the database | ecbd | - |
| 11-19 | gda_010 (The Three-Trunked Katsura | report | 77 chars | 7bb5 | holds |
| 11-19 | Gdansk | ambassador request | - | 7bb5 | - |
| 11-19 | A51429EC-837E-4506-BD3B-C369EFA444 | tree sent in | 344 chars, read it in the database | 0933 | - |
| 11-19 | B894C217-92B1-4BDD-9353-6E36EF8F21 | tree sent in | - | 0933 | - |
| 11-19 | BEE9E113-6234-4BAC-B308-D14EF4E3FA | tree sent in | 56 chars, read it in the database | 0933 | - |
| 11-19 | 61BFDBEB-40D4-4654-B2F6-377C44997B | tree sent in | 107 chars, read it in the database | 0933 | - |
| 11-19 | 32B40A81-9200-47FD-B160-EDB577C30E | tree sent in | - | 0933 | - |
| 11-19 | E4E4D964-C61C-484F-9994-CFD5FE96D5 | tree sent in | 121 chars, read it in the database | 0933 | - |
| 11-19 | York | ambassador request | - | ca57 | - |
| 11-19 | Réno-Valdieu | ambassador request | - | 7f7f | - |
| 11-19 | Brisbane | ambassador request | - | 5b0d | - |
| 11-19 | 685B7BB6-A189-4C1E-A74E-701215BB89 | tree sent in | 154 chars, read it in the database | 5b0d | - |
| 11-19 | Old Knobbley | Yes please! | - | 63b2 | - |
| 11-19 | Old Knobbley | Yes please! | - | 63b2 | - |
| 11-19 | E99B9502-2495-44D6-A73F-687C631291 | tree sent in | - | afd4 | - |
| 11-19 | Indian Signal Tree | correction sent in | 89 chars, read it in the database | 2703 | holds |
| 11-19 | - | if you need any help to build the  | - | 7e2e | holds |
| 11-19 | 0BF2F2D8-020E-4258-A925-8B90C6D45D | tree sent in | 222 chars, read it in the database | 462d | - |
| 11-19 | Inistioge | ambassador request | - | 7e2e | - |
| 11-19 | 792FD983-0F7D-4818-9112-8FBDF8E8C4 | tree sent in | 320 chars, read it in the database | cd40 | - |
| 11-19 | CF563122-313C-4D9C-9098-BF01CBB35A | tree sent in | 615 chars, read it in the database | cd40 | - |
| 11-19 | A tree near Westerlo | correction sent in | 89 chars, read it in the database | 9f53 | holds |
| 11-19 | B25A6096-D8F0-4528-A3FB-FA6F6C61FD | tree sent in | - | 9f53 | - |
| 11-19 | 6ACE68F9-6CA3-470C-9511-7E55975FB2 | Thanks for this. Unfortunately, I  | 49 chars | 7159 | - |
| 11-19 | 6ACE68F9-6CA3-470C-9511-7E55975FB2 | Thanks for this. Unfortunately, I  | 49 chars | 7159 | - |
| 11-19 | Hills Fig in Zetland | tree sent in | 176 chars, read it in the database | 9e00 | open_question |
| 11-19 | can_008 (Grant Crescent Blue Gums) | correction sent in | 91 chars, read it in the database | 9e00 | changed |
| 11-19 | ABA8F604-0C2B-4AE7-ADAB-A5E40BC28F | tree sent in | 75 chars, read it in the database | 81aa | - |
| 11-19 | cdf_001 (The Brandywine Sycamore ( | report | 84 chars | 3471 | holds |
| 11-19 | 25826C1E-C83A-4936-86D6-63DBF8A7BC | tree sent in | - | e5c1 | - |
| 11-19 | cdf_001 (The Brandywine Sycamore ( | report | 113 chars | 3471 | holds |
| 11-20 | hni_003 (The banyan of Nhan Dan, 7 | correction sent in | 91 chars, read it in the database | 56c0 | changed |
| 11-20 | 42F66634-36D7-46DF-8A02-7391146803 | tree sent in | 106 chars, read it in the database | 24da | - |
| 11-20 | gda_007 (The Maples of Hugo Conwen | report | 194 chars | 7bb5 | holds |
| 11-20 | 1776F5E7-9154-4A89-90CE-B69C6AD324 | tree sent in | - | 0b1c | - |
| 11-20 | Hills Fig in Zetland | 25 Gadigal Avenue, Zetland

Sent f | - | 9e00 | - |
| 11-20 | Hills Fig in Zetland | 25 Gadigal Avenue, Zetland

Sent f | - | 9e00 | - |
| 11-20 | Stratford-upon-Avon | ambassador request | - | 72f8 | - |
| 11-20 | mum_002 (The Rain Trees of Govt Ga | report | wrong location | 0933 | changed |
| 11-20 | 1C528293-5004-4F58-9DB6-1D635195B4 | tree sent in | - | 0c0d | - |
| 11-20 | 094A2107-6343-4EF6-BF83-C771CEBC64 | tree sent in | - | 86c2 | - |
| 11-20 | C4C911DE-781D-4234-998D-C5C657A9C2 | tree sent in | 434 chars, read it in the database | 4f2a | - |
| 11-20 | DECF2F9F-DB6F-4555-8C46-B940B05509 | tree sent in | 688 chars, read it in the database | 50a4 | - |
| 11-20 | mdp_003 (Tyler Arboretum Painter C | report | dead or gone | 3471 | changed |
| 11-20 | Tyler Arboretum Painter Ginkgo | correction sent in | 92 chars, read it in the database | 3471 | changed |
| 11-20 | mdp_003 (Tyler Arboretum Painter C | report | 33 chars | 3471 | holds |
| 11-20 | Tyler Arboretum Giant Sequoia | correction sent in | 92 chars, read it in the database | 3471 | changed |
| 11-20 | 69CF3021-612B-4AF4-A051-E91406FAC8 | tree sent in | 60 chars, read it in the database | 3471 | - |
| 11-20 | cdf_001 (The Brandywine Sycamore ( | report | 206 chars | 3471 | holds |
| 11-20 | 69CF3021-612B-4AF4-A051-E91406FAC8 | Higge, about the White Oak in Will | 198 chars | 3471 | - |
| 11-20 | 500CB567-07C5-4D7D-8345-D57BFDE0A7 | tree sent in | - | e246 | - |
| 11-20 | F871F444-7053-4566-BC71-C225C09515 | tree sent in | - | e246 | - |
| 11-20 | 6991CD88-4DB1-41EC-8A39-2B58E7E1D0 | tree sent in | 75 chars, read it in the database | e82c | - |
| 11-20 | BD71C73B-E90B-4F73-80B5-881761C554 | tree sent in | - | e246 | - |
| 11-20 | 995A659B-6CA9-45F1-9873-2A9D8CAA9D | tree sent in | - | e246 | - |
| 11-20 | 4FE1CB00-E56F-42E1-8C89-EC11BC883F | Yes, I will!  When I return home i | - | 5142 | - |
| 11-20 | The great cedar from Parc Chambrun | tree sent in | 246 chars, read it in the database | a20c | changed |
| 11-21 | DE314993-8DF5-496C-897D-B262D6F0D3 | tree sent in | 110 chars, read it in the database | 2f5e | - |
| 11-21 | 4DFF68AA-5E39-4DB5-BE9E-D2CDF8C261 | tree sent in | 55 chars, read it in the database | 2f5e | - |
| 11-21 | mdp_001 (Tyler Arboretum Giant Seq | report | 42 chars | 3471 | holds |
| 11-21 | Istanbul | ambassador request | - | 123d | - |
| 11-21 | BEE85803-FDEC-48C4-84BB-E5B061AF19 | tree sent in | 95 chars, read it in the database | ca57 | - |
| 11-21 | 3D93957A-F9BC-4E6A-945D-80943EF691 | tree sent in | - | 3073 | - |
| 11-21 | - | Love de app! Kan alleen het land w | - | 9308 | - |
| 11-21 | F01ADD8B-DD50-44F7-AAFA-CA85190B2F | tree sent in | - | 5c76 | - |
| 11-21 | 3FB92F89-3FEC-4C52-BF64-9D8DFDCC08 | tree sent in | - | 2f5e | - |
| 11-21 | CE8ED8FD-2125-4C9A-AE9A-9CC6B2AD09 | tree sent in | - | 79ed | - |
| 11-21 | 3FB92F89-3FEC-4C52-BF64-9D8DFDCC08 | Hi
Thanks for the email, I live in | - | 2f5e | - |
| 11-21 | B40CEB87-E4E0-4441-8C93-32D663A7CC | tree sent in | 69 chars, read it in the database | b238 | - |
| 11-21 | D00EDA19-E715-4B53-913D-0B6BAB109A | tree sent in | - | f9c3 | - |
| 11-21 | A tree near Bowthorpe | correction sent in | 90 chars, read it in the database | 7050 | holds |
| 11-21 | B57C3977-D5D3-4A97-A199-76433A04D5 | tree sent in | - | 7050 | - |
| 11-21 | The Bowthorpe Oak | correction sent in | 23 chars, read it in the database | 7050 | holds |
| 11-21 | Giant Sequoia near Bowthorpe | correction sent in | 89 chars, read it in the database | 7050 | holds |
| 11-21 | EAF6795D-B900-4A06-B31A-8850AC13FD | tree sent in | - | eafe | - |
| 11-21 | A tree near Dunsfold | correction sent in | 90 chars, read it in the database | eafe | holds |
| 11-21 | 081AFCEE-57A6-4622-8DE5-607F1C1A32 | tree sent in | - | 0e02 | - |
| 11-21 | Oak near Geetbets | correction sent in | 89 chars, read it in the database | 0e02 | holds |
| 11-21 | The Monterey Cypress at Bishops Kn | correction sent in | 91 chars, read it in the database | 2215 | changed |
| 11-21 | 4912EDD4-5E1A-4800-AB16-DC5CB9F632 | tree sent in | - | 1e79 | - |
| 11-21 | E4C07E02-2E9D-4391-8581-47E61BAB1F | tree sent in | - | 9c42 | - |
| 11-21 | 61FACF32-6C1E-4B79-9F4E-F4BD901CCC | tree sent in | - | 9c42 | - |
| 11-21 | 023BF7B4-8706-4819-BA17-6BC7FB6DC7 | tree sent in | - | 9d88 | - |
| 11-21 | The Cedar of Lebanon at Blaise Cas | ﻿We’ve revisited this. The tree we | - | 2215 | - |
| 11-21 | CC4293FF-8120-4C19-A667-25947845B4 | tree sent in | - | 9c42 | - |
| 11-21 | F36E78E1-93F1-4CA3-A6B4-85DDB9FE18 | tree sent in | - | 9c42 | - |
| 11-21 | F0AC690D-989A-4400-A70A-CEE219B249 | tree sent in | 281 chars, read it in the database | 2215 | - |
| 11-21 | Copper Beech in Bristol | correction sent in | 89 chars, read it in the database | 2215 | holds |
| 11-21 | 83D58764-B0B1-44A2-800A-74F016802B | tree sent in | 66 chars, read it in the database | b888 | - |
| 11-21 | Plane tree | tree sent in | 235 chars, read it in the database | 2f1a | changed |
| 11-21 | ADE84360-EE78-453E-B6F1-36DB50F6BC | tree sent in | - | 8379 | - |
| 11-21 | The Katsura-Tree of Morris Arboret | correction sent in | 92 chars, read it in the database | 3471 | changed |
| 11-21 | The Weeping European Beech at Morr | correction sent in | 92 chars, read it in the database | 3471 | changed |
| 11-21 | DAC0493F-948B-4AEC-A3FB-10FD3BD906 | tree sent in | - | 3471 | - |
| 11-21 | Sawtooth Oak in Philadelphia | correction sent in | 89 chars, read it in the database | 3471 | holds |
| 11-21 | FBA415E7-7E56-4859-BBFA-88CA09A74F | tree sent in | - | 95de | - |
| 11-21 | The Katsura-Tree of Morris Arboret | correction sent in | 92 chars, read it in the database | 3471 | changed |
| 11-21 | The Castle Linden of Cmurek | correction sent in | 91 chars, read it in the database | 3073 | changed |
| 11-21 | 27E529B6-7E49-4FD7-853E-6ACC23A947 | tree sent in | 43 chars, read it in the database | 1b04 | - |
| 11-21 | 83D58764-B0B1-44A2-800A-74F016802B | Thank you! I really love the idea  | - | b888 | - |
| 11-22 | 9C8D024B-96BA-4A22-ABEA-504A5D5E4A | tree sent in | - | 74e3 | - |
| 11-22 | Ginkgo near Ueki | correction sent in | 90 chars, read it in the database | 74e3 | holds |
| 11-22 | 04FD1169-96A7-42E1-9679-3F639C82DC | tree sent in | - | 74c9 | - |
| 11-22 | C50BB407-3ADE-4813-B8D8-9C3A9256B7 | tree sent in | 635 chars, read it in the database | 1021 | - |
| 11-22 | Oriental Plane in Tsagarada, Greec | correction sent in | 89 chars, read it in the database | 1021 | holds |
| 11-22 | D6E19C81-357B-4BB8-A5A1-C3C3AF4931 | tree sent in | - | 47bb | - |
| 11-22 | - | Please remove the photos, as inclu | 49 chars | 27c8 | - |
| 11-22 | 272EEA9F-3EBD-4F3A-927C-CCD96B21AB | tree sent in | - | 47bb | - |
| 11-22 | B92312A8-2D7F-43F8-90EE-5A1D2021BF | tree sent in | 114 chars, read it in the database | bddf | - |
| 11-22 | A tree near Llangernyw | correction sent in | 89 chars, read it in the database | bddf | holds |
| 11-22 | 9536657E-9A06-4CE1-9352-DAECAD3E04 | tree sent in | - | bddf | - |
| 11-22 | 803EB2F3-6367-4D67-BEFE-146A0B5D26 | tree sent in | 63 chars, read it in the database | b888 | - |
| 11-22 | The Old Jarrah Tree | correction sent in | 91 chars, read it in the database | 27c6 | changed |
| 11-22 | 59A9BF8F-4D59-4C58-B206-3ECC2A7F7E | tree sent in | 145 chars, read it in the database | daa1 | - |
| 11-22 | The Oldest Plane Tree in Europe | tree sent in | 52 chars, read it in the database | 5b06 | - |
| 11-22 | 57F46EDF-95E2-4A21-935F-5B12D0B23E | tree sent in | - | a87b | - |
| 11-22 | B478E704-F01D-442F-A8DE-1407AA063A | report | 121 chars | 2690 | holds |
| 11-22 | European Beech near Castlemorton | correction sent in | 89 chars, read it in the database | daa1 | holds |
| 11-22 | 5B3F2CB0-14F6-4477-B221-56B2911F76 | tree sent in | - | 2690 | - |
| 11-22 | 404AD610-9009-4C3C-824E-8F05E6AB60 | tree sent in | 20 chars, read it in the database | 1257 | - |
| 11-22 | A29ED9D7-1555-4579-AD0A-759824034C | tree sent in | - | cacc | - |
| 11-22 | 2DBAB77D-6BCF-46E9-AA36-00369790AC | tree sent in | 246 chars, read it in the database | 9a92 | - |
| 11-22 | F22530FF-C15B-4E83-8AFE-2320D295DB | tree sent in | - | 7248 | - |
| 11-22 | - | Please remove all photos, and don’ | 49 chars | 27c8 | - |
| 11-22 | - | Please remove all photos, and don’ | 49 chars | 27c8 | - |
| 11-22 | 6A9217D8-8466-480F-9831-3B3255721C | tree sent in | 32 chars, read it in the database | 9308 | - |
| 11-22 | 84541E96-06D1-42E2-BEC6-1C2CD9DFB5 | tree sent in | 116 chars, read it in the database | 9308 | - |
| 11-22 | 84D248DD-6FA9-4DD5-ACD3-1A33EC1A31 | tree sent in | - | 7933 | - |
| 11-22 | 553F2448-0E51-4AE4-9F09-7553DC6608 | tree sent in | - | 7933 | - |
| 11-22 | 6315B918-2200-4671-8EAB-E0771A6065 | tree sent in | 86 chars, read it in the database | 5f33 | - |
| 11-22 | boz_001 (The Linden of Linn) | report | 106 chars | 9c83 | holds |
| 11-22 | Unknown Tree | tree sent in | 26 chars, read it in the database | 8274 | open_question |
| 11-22 | AD8664D1-E182-4244-9FA2-A6F3AB7CCA | tree sent in | - | 7cd5 | - |
| 11-22 | 2F66B206-9ECE-4AFF-9BB8-0AE799968E | tree sent in | - | 5f33 | - |
| 11-22 | Fig | correction sent in | 90 chars, read it in the database | 7933 | changed |
| 11-22 | D281ADDD-4FA0-40E8-AAEF-E252055655 | tree sent in | 82 chars, read it in the database | 7933 | open_question |
| 11-22 | C9139A4E-9E9A-4065-8DD9-865527B71C | tree sent in | - | 47bb | - |
| 11-22 | AFBEEDB0-236E-42CC-814B-B8AA7AB6FA | tree sent in | - | 47bb | - |
| 11-22 | gir_004 (The Great Pine of Romanya | report | 143 chars | b238 | holds |
| 11-22 | 7F0038BA-2D3C-4BF4-A206-135905BFF0 | Hi

Yes happy to be an amassador.
 | - | 7e27 | - |
| 11-22 | Boab Prison Tree | correction sent in | 57 chars, read it in the database | 6443 | holds |
| 11-22 | 4504258B-6E45-4EAC-8A8F-F4D3FDFC95 | tree sent in | 193 chars, read it in the database | e45f | - |
| 11-22 | 1DA9FE2D-D3B4-4EE8-9E85-287491EFB6 | tree sent in | - | 67c8 | - |
| 11-22 | The Tortworth Chestnut | correction sent in | 89 chars, read it in the database | e45f | holds |
| 11-22 | Spirit Tree ancient cottonwood tre | tree sent in | 150 chars, read it in the database | 9fff | - |
| 11-22 | Ancient mesquite | tree sent in | 112 chars, read it in the database | 9fff | open_question |
| 11-22 | - | I have added an ancient tree but i | - | e45f | - |
| 11-22 | The Tortworth Chestnut | correction sent in | 89 chars, read it in the database | e45f | holds |
| 11-22 | The cedar of Himalaya | tree sent in | 24 chars, read it in the database | b8d5 | changed |
| 11-22 | 84541E96-06D1-42E2-BEC6-1C2CD9DFB5 | Hoi Hidde,

Wat leuk dat je proble | 48 chars | 9308 | - |
| 11-22 | 84541E96-06D1-42E2-BEC6-1C2CD9DFB5 | Hi!

I would love to keep an eye o | 48 chars | 9308 | - |
| 11-22 | 84541E96-06D1-42E2-BEC6-1C2CD9DFB5 | Hoi Hidde,

Wat leuk dat je proble | 48 chars | 9308 | - |
| 11-22 | 84541E96-06D1-42E2-BEC6-1C2CD9DFB5 | Hi!

I would love to keep an eye o | 48 chars | 9308 | - |
| 11-22 | 59E87943-2F6C-4F17-B6C3-7A40B35406 | tree sent in | - | f9ef | - |
| 11-22 | 3FB92F89-3FEC-4C52-BF64-9D8DFDCC08 | Thanks Hidde
There are some superb | 51 chars | 2f5e | - |
| 11-22 | 3FB92F89-3FEC-4C52-BF64-9D8DFDCC08 | Thanks Hidde
There are some superb | 51 chars | 2f5e | - |
| 11-22 | 441FF6CA-2691-46B5-95F6-2273991DE5 | tree sent in | 111 chars, read it in the database | 3471 | - |
| 11-23 | 313C857A-AB44-4040-8562-8D940ACC21 | tree sent in | 20 chars, read it in the database | 74e3 | - |
| 11-23 | 2BEAEF82-D143-42AB-96F8-0DA147AA5F | tree sent in | - | 74c9 | - |
| 11-23 | 81BFA129-EA0E-4F2A-82CD-4625248520 | tree sent in | 161 chars, read it in the database | 7933 | - |
| 11-23 | 65E2AF45-3F00-48F9-9926-93DEA3E166 | tree sent in | - | 99e8 | - |
| 11-23 | hbg_005 (The Japanese Pagoda Tree  | report | 148 chars | 3a3c | - |
| 11-23 | Bergamo | ambassador request | - | 59fa | - |

- 404 rows from 183 accounts.

**App Store downloads** (Apple's own count, not PostHog)

| Day | Downloads |
|---|---:|
| 2026-11-14 | 1 |
| 2026-11-15 | 3896 |
| 2026-11-16 | 1588 |
| 2026-11-17 | 712 |
| 2026-11-18 | 351 |
| 2026-11-19 | 153 |
| 2026-11-20 | 127 |
| 2026-11-21 | 130 |
| **8 days** | **6958** |
- First-time downloads only, which is what App Store Connect's Trends screen counts; redownloads and updates are not in this table.

**Where the downloads came from** (7 days, Apple's attribution)

| Came from | Via | Downloads |
|---|---|---:|
| App Store search | - | 3373 |
| Web referrer | - | 2071 |
| App referrer | - | 1459 |
| App Store browse | - | 54 |
| Unavailable | - | 1 |
| **window** | | **6958** |
- Countries: GB (2898); US (1019); AU (828); DE (289); NL (229); CA (207)
- Apple's own source split, first-time downloads only. "Web referrer" with our own domain is the site's app page; "App Store search" is somebody who typed into the store. "Unavailable" is Apple's word for a source it could not attribute.

**Bing's index** (pages crawled and in index, Bing Webmaster Tools)

| Day | Pages crawled | Pages in index |
|---|---:|---:|
| 11-16 | 409 | 4730 |
| 11-17 | 412 | 4730 |
| 11-18 | 478 | 4801 |
| 11-19 | 215 | 4801 |
| 11-20 | 139 | 4857 |
| 11-21 | 147 | 4901 |
| 11-22 | 240 | 4929 |
- In index the week before: 4617.

audience_section: failed today (HTTP Error 400: Bad Request at request.py:611).

**Google Analytics** (last 7 days, visitors who accepted cookies)

- Google Analytics: fetch failed today (HTTP Error 400: Bad Request); numbers resume tomorrow.

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
| 11-22T13:55 | 19.2 | 9 | 12 | 2 | Miami +3, Florianopolis +2, Las Vegas +2, Birmingham +1, +3 more |
| 11-22T17:04 | 5.2 | 1 | 5 | 0 | Fontainebleau +1, Glasgow |
| 11-22T20:33 | 4.2 | 0 | 8 | 2 | - |
| 11-23T02:08 | 0.0 | 0 | 3 | 0 | Mangaluru |
| **4 runs** | **29** | **10** | **28** | | |

- 2 of 4 produced no trees; 2 to 2 commands refused per run; 1 wrote nothing to LOG.md; last build that went live: 5h ago, 1 failed since.

**What they made**

- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- reader judge: a golden ginkgo at Sakurai Shrine, Itoshima, live on the Fukuoka page
- reader judge: Paavola's Oak in Lohja gets a reader's photograph
- reader judge: the white oak on Grubb Road live in Willistown
- reader judge: mail reply 1500 filed, nothing else waiting
- reader judge: three readers' photographs live in Hamburg and Paris
- Night run: coimbra verify dispatched, log
- Night run: nothing publishable, fort-worth released as a wall, log
- Night run: web search-pill bug row closed, braga wall, log (nothing to publish: no lane with six candidates)
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated

**Reader photographs in a strip, live first, not yet looked at** (2)

| Day | Tree | Where | Undo |
|---|---|---|---|
| 11-22 | The Argyle Street Ash | Glasgow | `sightings_publish.py --unstrip dcffbd99-b1c4-403e-87c3-48ae83bf6d51` |
| 11-23 | The Tree House Rain Tree of the Netravati Promenade | Mangaluru | `sightings_publish.py --unstrip 1bd94bb4-b914-4baf-861c-c17b843afede` |

Machine: 5 chain attempts yesterday, 5 got real work time (~66 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

**Sign-in mail sent again** (stuck an hour or more, `scripts/signin_watch.py`): 39 people in 7 days, 7 of them got in afterwards.

## 2026-11-21 (previous UTC day)

**Today: 21 android waitlist signups arrived yesterday (2064 total); 25 tree submissions and an ambassador request for Istanbul and 4 feedback reports arrived yesterday (549 submissions of every kind in all); 41 accounts were opened yesterday (911 accounts in all).**

**North star: 278 people have uploaded a tree or photo of their own (+263 this week); 42 of them did it on more than one day (+38).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 3042 | 35 |
| ... of which from search | every search engine | 90 | 15 |
| ... from Google | Google's recovery | 70 | 10 |
| ... from Bing | Bing | 9 | 1 |
| Website visitors who came back | people who stay | 616 | 9 |
| App downloads (first-time) | people | 6828 | 17 |
| New accounts | people | 843 | 4 |
| Phones back within 30 days | people who stay | 7 of 16 | 5 of 17 |
| Trees saved to Want to go | intent | 540 | 0 |
| Trees collected | goal 1: stood at a tree | 472 | 0 |
| Readers' contributions | data: trees, photos, corrections | 747 | 4 |
| Worth-it votes | one tap, not a contribution | 174 | 0 |
| Shares (app and web) | word of mouth, since 10-30 | 336 | 1 |
| Visits from a shared link | what sharing brings | 124 | 0 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web red, iOS orange, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | red: deploy failure on main | orange: 1 compliance point(s) wait for Hidde (data/compliance.json) | grey: no checks wired yet |

**Plus question** (18 answers, 2 new; 5 asked to be told; 10 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| Download offline maps | 7 |
| Something else | 7 |
| A richer log of every tree you've collected | 6 |
| Recommended tree walks for a city trip | 4 |
| Seasonal alerts when trees are at their best | 3 |

**Fixed since 19 Nov: 1.**

| Day | Where | What was wrong | Found by | Test |
|---|---|---|---|---|
| 20 Nov | Web | Map pins stacked under each other and jumped on hover; the chosen pin stood far from its card (pin CSS set position:relative over MapLibr... | a person | yes |

**New ambassadors yesterday: 3.** Nick H. (Istanbul); David S. (Castlemaine); Wild Ash 1611 (Royal Leamington Spa). Each got the mail and the badge automatically; 40 ambassadors in all (`python3 scripts/ambassador.py --list`).

**Open for you** (2; everything else handled and recorded, 58 feedback in all)

| What | Why it waits | Summary |
|---|---|---|
| feedback 1358 | your call | Cannot change their home country; both apps have the Country row in Edit profile, so finding it or a failing save; reply drafted asking which platform |
| feedback 1362 | your call | Ambassador yes acted on: Castlemaine badge granted. Their wish to cover a wider region of Central Victoria waits for Hidde; suggested reply in drafts. |

Reader judge: 164 agent minutes yesterday, 783 in the last 7 days.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-15 | 11-16 | 11-17 | 11-18 | 11-19 | 11-20 | 11-21 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 1797 | 734 | 297 | 169 | 81 | 66 | 43 | **3187** |
| New accounts | 371 | 199 | 100 | 62 | 39 | 31 | 41 | **843** |
| Saves | 187 | 143 | 38 | 58 | 28 | 31 | 55 | **540** |
| Android waitlist | 1317 | 416 | 158 | 61 | 22 | 16 | 21 | **2011** |
| App downloads | 3896 | 1588 | 712 | 351 | 153 | 127 | – | **6827** |
| App deletions | 11 | 16 | 14 | 10 | 7 | 3 | 9 | **70** |
| App phones | 3563 | 1694 | 950 | 623 | 482 | 419 | 419 | **6494** |
| Trees opened in the app | 7608 | 3264 | 1849 | 1103 | 864 | 598 | 843 | **16129** |
| Trees collected | 96 | 59 | 30 | 21 | 42 | 14 | 24 | **286** |
| Trees sent | 98 | 51 | 37 | 14 | 30 | 13 | 25 | **268** |
| Feedback | 29 | 23 | 15 | 42 | 18 | 12 | 17 | **156** |
| Worth-it votes | 62 | 44 | 20 | 16 | 15 | 9 | 8 | **174** |
| Ambassador asks | 5 | 3 | 2 | 0 | 5 | 1 | 1 | **17** |
| Website photos | 9 | 3 | 6 | 3 | 1 | 2 | 1 | **25** |
| iPhone photos | 185 | 104 | 74 | 41 | 47 | 32 | 47 | **530** |
| Android photos | 0 | 0 | 0 | 0 | 26 | 1 | 5 | **32** |
| Tree notes | 15 | 23 | 11 | 15 | 6 | 3 | 8 | **81** |
| App Store reviews | 4 | 2 | 1 | 0 | 1 | 0 | 0 | **8** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.
- App deletions count only phones that share analytics with developers, and Apple leaves out days too small to show: read it against the installs of the same day, not as a total.

**Feedback by kind** (the Feedback row above, split; their words are in the readers-in-full block)

| Kind | 11-21 | **7 days** |
|---|---:|---:|
| Pin moved | 11 | **65** |
| Written feedback | 5 | **62** |
| Report on a tree | 1 | **29** |
| Collected far from our pin | 0 | **1** |

**Trees readers sent, for you to inspect** (105 you have not looked at; ours left out)

| Judged | Reader | Tree | Where | Species | Their girth | Our verdict | Page |
|---|---|---|---|---|---:|---|---|
| 2026-11-21 | ? | D00EDA19-E715-4B53-913D-0B6BAB109A59 | Nichinan, Tottori | - | - | lead | - |
| 2026-11-21 | ? | EAF6795D-B900-4A06-B31A-8850AC13FDA4 | Dunsfold | - | - | lead | - |
| 2026-11-21 | ? | 61FACF32-6C1E-4B79-9F4E-F4BD901CCCEC | Leeds | - | - | lead | - |
| 2026-11-21 | A | The Old Beech of St Ives Estate | Bingley | European Beech (Fagus sylvatic | - | hold | - |
| 2026-11-21 | B | The Oak of Kiewit | Hasselt | Oak (Quercus sp.) | - | hold | - |
| 2026-11-21 | C | Te Matua Ngahere | Waipoua Forest | Kauri (Agathis australis) | - | hold | - |
| 2026-11-21 | D | Empress Tree | - | Empress Tree | - | hold | - |
| 2026-11-20 | E | The Last Elm of Stationsplein | Amsterdam | Dutch Elm (Ulmus x hollandica) | - | hold | - |
| 2026-11-20 | F | The Plane of Montée Saint-Sébastien | Lyon | London Plane (Platanus x aceri | - | hold | - |
| 2026-11-20 | G | Tyler Arboretum Giant Sequoia (2 photos) | Media | Giant Sequoia (Sequoiadendron  | - | hold | - |
| 2026-11-20 | G | - | Media | - | - | hold | - |
| 2026-11-20 | H | A tree I found (8 photos) | - | - | - | hold | - |
| 2026-11-19 | I | The Maples of Hugo Conwentz | Gdansk | Field Maple (Acer campestre) | - | hold | - |
| 2026-11-19 | I | The Ivy Elm of Park Oliwski (2 photos) | Gdansk | European White Elm (Ulmus laev | - | hold | - |
| 2026-11-19 | J | Dragon Tree in Madeira | - | Dragon Tree | - | hold | - |
| 2026-11-19 | K | The Cut-Leaved Alder | York | Common Alder (Alnus glutinosa  | - | hold | - |
| 2026-11-19 | K | The Pear-Barked Beech | York | European Beech (Fagus sylvatic | - | hold | - |
| 2026-11-19 | L | Fig | - | Fig | - | hold | - |
| 2026-11-19 | M | The Amur Cork Trees and Crimean Linden of Be (2 photos) | Vilnius | Amur Cork Tree (Phellodendron  | - | hold | - |
| 2026-11-19 | M | - | Vilnius | - | - | hold | - |
| 2026-11-19 | M | The Sapiegos Park Linden | Vilnius | Small-leaved Lime (Tilia corda | - | hold | - |
| 2026-11-19 | M | - | Vilnius | - | - | hold | - |
| 2026-11-18 | G | The Sprawling Sycamore of Pawling Farm | Valley Forge | American Sycamore (Platanus oc | - | hold | - |
| 2026-11-18 | N | The Remnant River Red Gum of Edinburgh Garde (4 photos) | Melbourne | River Red Gum (Eucalyptus cama | - | hold | - |
| 2026-11-18 | N | The Southern Mahogany of Edinburgh Gardens (2 photos) | Melbourne | Southern Mahogany (Eucalyptus  | - | hold | - |
| 2026-11-18 | N | - | Melbourne | - | - | hold | - |
| 2026-11-18 | O | The Bidwill Kauri Pine | Sydney | Queensland Kauri (Agathis robu | - | hold | - |
| 2026-11-18 | N | The Holm Oak of Darling Gardens | Melbourne | Holm Oak (Quercus ilex) | - | hold | - |
| 2026-11-18 | P | The Knotted Tree of Mexikópuszta | Fertőújlak | Japanese Pagoda Tree or Black  | - | hold | - |
| 2026-11-18 | ? | The Casuarina of the Cascada (2 photos) | Barcelona | River She-oak (Casuarina cunni | - | hold | - |
| 2026-11-18 | Q | Ancient Cedar at Makata Jinjya | - | Japanese Cedar | 800 cm | hold | - |
| 2026-11-18 | R | Bur Oak | - | Bur Oak | 323 cm | hold | - |
| 2026-11-17 | S | - | - | - | - | hold | - |
| 2026-11-17 | ? | - | - | - | - | hold | - |
| 2026-11-17 | S | - | - | - | - | hold | - |
| 2026-11-17 | S | - | - | - | - | hold | - |
| 2026-11-17 | T | - | - | - | - | hold | - |
| 2026-11-17 | T | - | - | - | - | hold | - |
| 2026-11-17 | U | A tree in Los Angeles | - | - | - | hold | - |
| 2026-11-17 | V | A tree near Copenhagen | - | - | - | hold | - |
| 2026-11-17 | W | Blue Jacaranda in ISA | - | Blue Jacaranda | - | hold | - |
| 2026-11-17 | W | Judas Tree in ISA | - | Judas Tree | - | hold | - |
| 2026-11-17 | O | Queensland Kauri in Sydney | - | Queensland Kauri | - | hold | - |
| 2026-11-17 | X | Pecan | - | Pecan | - | hold | - |
| 2026-11-17 | Y | Ahuehuete del Jardin de San Fernando (2 photos) | Mexico City | - | - | hold | - |
| 2026-11-17 | X | Pecan | Griffin | Pecan | - | hold | - |
| 2026-11-17 | Z | The Cosgrove House Banyan (2 photos) | Key West | Fig (Ficus sp.) | - | hold | - |
| 2026-11-17 | Z | Jindai-zakura (Yamataka Jindai Zakura) | Hokuto | Higan Cherry (Prunus subhirtel | - | hold | - |
| 2026-11-17 | A1 | Black Mulberry in London | - | Black Mulberry | 250 cm | hold | - |
| 2026-11-17 | B1 | The Finsbury Circus Pagoda Tree | London | Japanese Pagoda Tree (Styphnol | - | hold | - |
| 2026-11-17 | C1 | Le Chêne de la Vierge | - | Oak | 250 cm | hold | - |
| 2026-11-17 | D1 | The Moreton Bay Fig of Curtain Square | - | - | - | hold | - |
| 2026-11-17 | B1 | A London plane in Finsbury Circus Gardens | - | London Plane (Platanus x aceri | - | hold | - |
| 2026-11-17 | E1 | A dead sweet chestnut in the Kastanologos fo | - | Sweet Chestnut (Castanea sativ | - | hold | - |
| 2026-11-17 | F1 | The Totteridge Yew | London | European Yew (Taxus baccata) | - | hold | - |
| 2026-11-17 | G1 | Queen Elizabeth’s Oak in Greenwich Park | - | Pedunculate Oak | - | hold | - |
| 2026-11-17 | H1 | - | - | - | - | hold | - |
| 2026-11-17 | I1 | - | - | - | - | hold | - |
| 2026-11-17 | J1 | - | - | - | - | hold | - |
| 2026-11-17 | K1 | - (2 photos) | - | - | - | hold | - |
| 2026-11-17 | ? | Romantik-Eiche | Heidelberg | - | - | lead | - |
| 2026-11-17 | L1 | - | Azores | - | - | hold | - |
| 2026-11-17 | M1 | Ekebyhovseken | Ekerö | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-17 | N1 | Orange | - | Orange (Citrus sinensis) | - | hold | - |
| 2026-11-17 | ? | BB61E294-5FFB-4378-960A-64DAB336FD46 | - | - | - | hold | - |
| 2026-11-17 | ? | CAA9C183-3017-433B-A1CA-09E1CAA99BF3 | - | - | - | hold | - |
| 2026-11-17 | ? | The Signal Tree (Native American'Indian Sign | Akron, Ohio, USA | - | 122 cm | hold | - |
| 2026-11-16 | O1 | American Elm | - | American Elm | - | hold | - |
| 2026-11-16 | O1 | Eastern Cottonwood (2 photos) | - | Eastern Cottonwood | - | hold | - |
| 2026-11-16 | O1 | White Oak | - | White Oak | - | hold | - |
| 2026-11-16 | O1 | Northern Red Oak | - | Northern Red Oak | - | hold | - |
| 2026-11-16 | P1 | Linden tree next to the pond | - | Lime (Tilia sp.) | 166 cm | hold | - |
| 2026-11-16 | Q1 | Prince Eugen's Oak | - | Oak (Quercus sp.) | - | hold | - |
| 2026-11-16 | R1 | A tree near Helmond | - | - | - | hold | - |
| 2026-11-16 | S1 | - | - | ridged furrowed bark, spreadin | - | hold | - |
| 2026-11-16 | T1 | A tree near Westonbirt Arboretum | - | - | - | hold | - |
| 2026-11-16 | ? | The Famous Nossob Camel Thorn Tree | Kgalagadi Transfrontier Park | - | - | lead | - |
| 2026-11-15 | U1 | Endangered Dawn Redwood in Holborn, legal di | - | Dawn Redwood | - | hold | - |
| 2026-11-15 | L1 | Giant Australian Rubber Tree of Jardim Anton | Azores | Moreton Bay Fig (Ficus macroph | - | hold | - |
| 2026-11-15 | V1 | Deans Oak | - | - | 1200 cm | hold | - |
| 2026-11-15 | W1 | Scots Pine in Dunkeld | - | Scots Pine | 660 cm | hold | - |
| 2026-11-15 | X1 | Tree in Waitangi | - | - | - | hold | - |
| 2026-11-15 | K1 | - | - | - | - | hold | - |
| 2026-11-15 | Y1 | - | - | - | - | hold | - |
| 2026-11-15 | Z1 | - | - | - | - | hold | - |
| 2026-11-15 | Z1 | - | - | - | - | hold | - |
| 2026-11-15 | Z1 | - | - | - | - | hold | - |
| 2026-11-15 | A2 | - | - | - | - | hold | - |
| 2026-11-15 | B2 | The Witch Tree of Fanal | Madeira | Til / Stinkwood (Ocotea foeten | - | hold | - |
| 2026-11-15 | C2 | Marton Oak | - | Pedunculate Oak | - | hold | - |
| 2026-11-15 | D2 | Malmö | - | - | - | hold | - |
| 2026-11-15 | E2 | Blue Jacaranda in Melbourne | - | Blue Jacaranda | - | hold | - |
| 2026-11-15 | F2 | English Hawthorn | - | English Hawthorn (Crataegus la | 50 cm | hold | - |
| 2026-11-15 | G2 | Wistman's Wood | Dartmoor | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-15 | H2 | Grimston's Oak | London | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-15 | G2 | The Crom Yews | Crom | European Yew (Taxus baccata) | - | hold | - |
| 2026-11-15 | G2 | The Dawn Redwood by the Kelvin Statue (2 photos) | Belfast | Dawn Redwood (Metasequoia glyp | - | hold | - |
| 2026-11-15 | G2 | S'Olivera de Cort | Palma de Mallorca | Olive (Olea europaea) | - | hold | - |
| 2026-11-15 | I2 | A tree near Chiang Mai | - | - | - | hold | - |
| 2026-11-15 | J2 | Il cipresso calvo di Villa Smeraldi | - | Cypress (Cupressus sp.) | - | hold | - |
| 2026-11-15 | G2 | The Boole Library Redwoods | Cork | Redwood | - | hold | - |
| 2026-11-15 | ? | Oak tree, Quercus Robur. | Bagni di Lusnizza, Udine | - | 454 cm | lead | - |
| 2026-11-15 | ? | 71F93157-AEF9-41A4-AF61-E1AD9755F9B1 | - | - | - | hold | - |
| 2026-11-15 | ? | 24FDCCB3-A454-4556-8169-2BAD2FB36ABD | - | - | - | hold | - |
| 2026-11-15 | ? | C7962FE1-14DB-407A-B62F-CFA617580655 | - | - | - | hold | - |
- From 62 readers: reader G2 5, reader M 4, reader N 4, reader O1 4, reader G 3, reader S 3, reader Z1 3, reader B1 2, reader I 2, reader K 2, reader K1 2, reader L1 2, reader O 2, reader T 2, reader W 2, reader X 2, reader Z 2, reader A 1, reader A1 1, reader A2 1, reader B 1, reader B2 1, reader C 1, reader C1 1, reader C2 1, reader D 1, reader D1 1, reader D2 1, reader E 1, reader E1 1, reader E2 1, reader F 1, reader F1 1, reader F2 1, reader G1 1, reader H 1, reader H1 1, reader H2 1, reader I1 1, reader I2 1, reader J 1, reader J1 1, reader J2 1, reader L 1, reader M1 1, reader N1 1, reader P 1, reader P1 1, reader Q 1, reader Q1 1, reader R 1, reader R1 1, reader S1 1, reader T1 1, reader U 1, reader U1 1, reader V 1, reader V1 1, reader W1 1, reader X1 1, reader Y 1, reader Y1 1.
- Photographs and the readers' own words: `python3 scripts/inspect_readers.py` (a local page, never in this public file). Your answer goes in with `python3 scripts/judgement.py --feedback <id> "..."`.

**Waiting for you** (what the runs left for you since 2026-11-21)

- 229 email addresses ready to mail (archive 0, nature 9, guide 4, press 122, source 58, council 16, society 7, tourism 5, other 5, garden 3); **the night run found no new contacts in two days**
- the daily task "publish-held-trees-daily" can be switched off under Scheduled; write passes put trees straight into the app, so nothing waits for it.
- preflight and the build disagree on whether app-only trees count toward a park's total; worth making them agree.
- the photo-GPS-over-hand-pin rule and that preflight check disagree here).
- next Android build carries the fix for IndexOutOfBoundsException @ Preconditions.outOfBounds:100.

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-20 | K2 | The Leaf-Seed Ginkgo of Inada Gobo | Kasama | a reader's photograph, published | [live](https://ancienttrees.app/kasama/leaf-seed-ginkgo-of-inada-gobo) |
| 11-20 | L2 | The banyan of Nhan Dan, 71 Hang Trong | Hanoi | a reader's photograph, published | [live](https://ancienttrees.app/hanoi/banyan-of-nhan-dan-71-hang-trong) |
| 11-20 | M2 |  | ? | a reader's photograph, published | not live yet |
| 11-20 | Q |  | ? | a reader's photograph, published | not live yet |
| 11-20 | N2 |  | ? | a reader's photograph, published | not live yet |
| 11-20 | O2 | The St Mary Magdalene Plane | London | a reader's photograph, published | [live](https://ancienttrees.app/london/st-mary-magdalene-plane) |
| 11-20 | F | The Plane of Montée Saint-Sébastien | Lyon | a reader's photograph, published | [live](https://ancienttrees.app/lyon/plane-of-montee-saint-sebastien) |
| 11-20 | P2 |  | ? | a reader's photograph, published | not live yet |
| 11-20 | Q2 |  | ? | a reader's photograph, published | not live yet |
| 11-20 | E | The Last Elm of Stationsplein | Amsterdam | a reader's photograph, published | [live](https://ancienttrees.app/amsterdam/last-elm-of-stationsplein) |
| 11-20 | R2 | The Last Elm of Stationsplein | Amsterdam | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/amsterdam/last-elm-of-stationsplein) |
| 11-20 | F | The Plane of Montée Saint-Sébastien | Lyon | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/lyon/plane-of-montee-saint-sebastien) |
| 11-20 | S2 | The Silky Oaks of Largo Marques de Pombal | Setubal | a reader's photograph, published | [live](https://ancienttrees.app/setubal/silky-oaks-of-largo-marques-de-pombal) |
| 11-20 | T2 | The Twisted Beech of Square des Arenes de Lutece | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/twisted-beech-of-square-des-arenes-de-lutece) |
| 11-20 | U2 | The Betsey Williams Sycamore | Providence | a reader's photograph, published | [live](https://ancienttrees.app/providence/betsey-williams-sycamore) |
| 11-20 | V2 | Il Platano del Giardino Bazlen | Milan | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/milan/il-platano-del-giardino-bazlen) |
| 11-20 | V2 | Il Platano del Giardino Bazlen | Milan | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/milan/il-platano-del-giardino-bazlen) |
| 11-20 | G | Tyler Arboretum Painter Ginkgo | Media | a reader's photograph, published | [live](https://ancienttrees.app/media-pennsylvania/tyler-arboretum-painter-ginkgo) |
| 11-20 | G | Tyler Arboretum Giant Sequoia | Media | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/media-pennsylvania/tyler-arboretum-giant-sequoia) |
| 11-20 | G | Tyler Arboretum Giant Sequoia | Media | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/media-pennsylvania/tyler-arboretum-giant-sequoia) |
| 11-20 | G |  | ? | a reader's photograph, published | not live yet |
| 11-20 | G | The Brandywine Sycamore (Lafayette Sycamore) | Chadds Ford | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/chadds-ford/brandywine-sycamore-lafayette-sycamore) |
| 11-20 | W2 | The Split Oak on the Stoke Park Slope | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/split-oak-on-the-stoke-park-slope) |
| 11-20 | W2 | The Antlered Oak | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/antlered-oak) |
| 11-20 | W2 | The Thick-trunked Willow of the Rideau Canal | Ottawa | a reader's photograph, published | [live](https://ancienttrees.app/ottawa/thick-trunked-willow-of-the-rideau-canal) |
| 11-20 | X2 | The Furrowed Giant of Curtain Square | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/furrowed-giant-of-curtain-square) |
| 11-20 | O | The Furrowed Giant of Curtain Square | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/furrowed-giant-of-curtain-square) |
| 11-20 | O | The Furrowed Giant of Curtain Square | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/furrowed-giant-of-curtain-square) |
| 11-20 | X2 | The Moreton Bay Fig of Curtain Square | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/moreton-bay-fig-of-curtain-square) |
| 11-20 | O | The Moreton Bay Fig of Curtain Square | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/moreton-bay-fig-of-curtain-square) |
| 11-21 | Y2 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | Z2 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | Z2 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | A3 | The Birnam Oak | Dunkeld | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/dunkeld/birnam-oak) |
| 11-21 | A3 | The Fortingall Yew | Fortingall | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/fortingall/fortingall-yew) |
| 11-21 | B3 | The Chestnut Avenue of the Hauptallee | Vienna | a reader's photograph, published | [live](https://ancienttrees.app/vienna/chestnut-avenue-of-the-hauptallee) |
| 11-21 | C3 | The Podocarp of Piazza Vittorio | Rome | a reader's photograph, published | [live](https://ancienttrees.app/rome/podocarp-of-piazza-vittorio) |
| 11-21 | D3 | The Ankerwycke Yew | Runnymede | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/runnymede/ankerwycke-yew) |
| 11-21 | D3 | The Ankerwycke Yew | Runnymede | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/runnymede/ankerwycke-yew) |
| 11-21 | D3 | The Ankerwycke Yew | Runnymede | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/runnymede/ankerwycke-yew) |
| 11-21 | D3 | The Ankerwycke Yew | Runnymede | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/runnymede/ankerwycke-yew) |
| 11-21 | K | The Minster Yard Beech | York | a reader's photograph, published | [live](https://ancienttrees.app/york/minster-yard-beech) |
| 11-21 | E3 | The Husalle Lindens | Copenhagen | a reader's photograph, published | [live](https://ancienttrees.app/copenhagen/husalle-lindens) |
| 11-21 | B3 | The Waldmüllerpark Wingnuts | Vienna | a reader's photograph, published | [live](https://ancienttrees.app/vienna/waldmullerpark-wingnuts) |
| 11-21 | F3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | G3 | The Holm Oak of the National Garden | Athens | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/athens/holm-oak-of-the-national-garden) |
| 11-21 | H3 | The Gnarled Beech of Hampstead Heath | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/gnarled-beech-of-hampstead-heath) |
| 11-21 | G3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | G3 | The Holm Oak of the National Garden | Athens | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/athens/holm-oak-of-the-national-garden) |
| 11-21 | E3 | The Søndermarken Oak | Copenhagen | a reader's photograph, published | [live](https://ancienttrees.app/copenhagen/sondermarken-oak) |
| 11-21 | E3 | The Beech by the Boat Trip | Copenhagen | a reader's photograph, published | [live](https://ancienttrees.app/copenhagen/beech-by-the-boat-trip) |
| 11-21 | Z2 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | I3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | E3 | The Pedunculate Oak of Frederiksberg Have | Copenhagen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/copenhagen/pedunculate-oak-of-frederiksberg-have) |
| 11-21 | J3 | The Great Ginkgo of Bodaiji | Nagi | a reader's photograph, published | [live](https://ancienttrees.app/nagi/great-ginkgo-of-bodaiji) |
| 11-21 | E3 | The Catalpa of Haveselskabets Have | Copenhagen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/copenhagen/catalpa-of-haveselskabets-have) |
| 11-21 | K3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | H3 | The Marylebone Elm | London | a reader's photograph, published | [live](https://ancienttrees.app/london/marylebone-elm) |
| 11-21 | D3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | I3 | The Molkenkur Linden | Heidelberg | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/heidelberg/molkenkur-linden) |
| 11-21 | B |  | ? | a reader's photograph, published | not live yet |
| 11-21 | L3 | The Monterey Cypress at Bishops Knoll | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/monterey-cypress-at-bishops-knoll) |
| 11-21 | M3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | A |  | ? | a reader's photograph, published | not live yet |
| 11-21 | N3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | A |  | ? | a reader's photograph, published | not live yet |
| 11-21 | A |  | ? | a reader's photograph, published | not live yet |
| 11-21 | L3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | O3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | P3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | Q3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | R3 | The Bodhi Tree in the Hillside Shrine | Kandy | a reader's photograph, published | [live](https://ancienttrees.app/kandy/bodhi-tree-in-the-hillside-shrine) |
| 11-21 | S3 | The Fort Canning Rain Tree | Singapore | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/singapore/fort-canning-rain-tree) |
| 11-21 | B | The Oak of Kiewit | Hasselt | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/hasselt/oak-of-kiewit) |
| 11-21 | G | The Katsura-Tree of Morris Arboretum | Philadelphia | a reader's photograph, published | [live](https://ancienttrees.app/philadelphia/katsura-tree-of-morris-arboretum) |
| 11-21 | G | The Weeping European Beech at Morris Arboretum | Philadelphia | a reader's photograph, published | [live](https://ancienttrees.app/philadelphia/weeping-european-beech-at-morris-arboretum) |
| 11-21 | G |  | ? | a reader's photograph, published | not live yet |
| 11-21 | C | Tāne Mahuta | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/tane-mahuta) |
| 11-21 | C | Te Matua Ngahere | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/te-matua-ngahere) |
| 11-21 | C | Te Matua Ngahere | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/te-matua-ngahere) |
| 11-21 | C | Te Matua Ngahere | Waipoua Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/waipoua-forest/te-matua-ngahere) |
| 11-21 | T3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | U3 | The Survivor Tree | Moffat | a reader's photograph, published | [live](https://ancienttrees.app/moffat/survivor-tree) |
| 11-22 | V3 | The Gennett Poplar | Chattahoochee National Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/chattahoochee-national-forest/gennett-poplar) |
| 11-22 | W3 |  | ? | a reader's photograph, published | not live yet |
| 11-22 | X3 | Pando | Fish Lake, Utah | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/fish-lake-utah/pando) |
| 11-22 | Y3 |  | ? | a reader's photograph, published | not live yet |
| 11-20 | L2 | hni_003 (The banyan of Nhan Dan, 71 Hang Trong) | Hanoi | a reader's correction changed the page | - |
| 11-20 | Z3 | mum_002 (The Rain Trees of Govt Gate Road) | Mumbai | a reader's feedback changed the page | - |
| 11-20 | G | mdp_003 (Tyler Arboretum Painter Cedar of Lebanon) | Media | a reader's feedback changed the page | - |
| 11-20 | G | Tyler Arboretum Painter Ginkgo | Media | a reader's correction changed the page | - |
| 11-20 | G | Tyler Arboretum Giant Sequoia | Media | a reader's correction changed the page | - |
| 11-20 | Y2 | The great cedar from Parc Chambrun | Nice | a reader's tree changed the page | - |
| 11-21 | L3 | The Monterey Cypress at Bishops Knoll | Bristol | a reader's correction changed the page | - |
| 11-21 | P3 | Plane tree | Le Porge | a reader's tree changed the page | - |
| 11-21 | G | The Katsura-Tree of Morris Arboretum | Philadelphia | a reader's correction changed the page | - |
| 11-21 | G | The Weeping European Beech at Morris Arboretum | Philadelphia | a reader's correction changed the page | - |
| 11-21 | G | The Katsura-Tree of Morris Arboretum | Philadelphia | a reader's correction changed the page | - |
| 11-21 | F3 | The Castle Linden of Cmurek | Trate | a reader's correction changed the page | - |
- From 51 readers: reader G 14, reader D3 5, reader E3 5, reader C 4, reader A 3, reader G3 3, reader L3 3, reader O 3, reader W2 3, reader Z2 3, reader A3 2, reader B 2, reader B3 2, reader F 2, reader F3 2, reader H3 2, reader I3 2, reader L2 2, reader P3 2, reader V2 2, reader X2 2, reader Y2 2, reader C3 1, reader E 1, reader J3 1, reader K 1, reader K2 1, reader K3 1, reader M2 1, reader M3 1, reader N2 1, reader N3 1, reader O2 1, reader O3 1, reader P2 1, reader Q 1, reader Q2 1, reader Q3 1, reader R2 1, reader R3 1, reader S2 1, reader S3 1, reader T2 1, reader T3 1, reader U2 1, reader U3 1, reader V3 1, reader W3 1, reader X3 1, reader Y3 1, reader Z3 1.

**What was sent in, and what we decided**

| seen | what | where | size for its species | ours | Hidde |
|---|---|---|---|---|---|
| 2026-11-19 | The Ivy Elm of Park Oliwski | Gdansk | - | hold | - |
| 2026-11-19 | A tree I found | - | - | hold | - |
| 2026-11-19 | The Amur Cork Trees and Crimean Linden | Vilnius | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | lead | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | A tree I found | - | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | The Southern Mahogany of Edinburgh Gar | Melbourne | - | hold | - |
| 2026-11-18 | The Casuarina of the Cascada | Barcelona | - | hold | - |
| 2026-11-18 | a tree we do not map | - | - | lead | - |
| 2026-11-17 | Ahuehuete del Jardin de San Fernando | Mexico City | - | hold | - |
| 2026-11-17 | The Cosgrove House Banyan | Key West | - | hold | - |
| 2026-11-17 | European Beech in Baarn | - | - | hold | - |
| 2026-11-17 | European Beech in Baarn | - | - | hold | - |
| 2026-11-17 | a tree we do not map | Baarn | - | hold | - |

0 waiting for a verdict. Disagree with one and the rule changes: `python3 scripts/judgement.py --feedback <id> "..."`, and `--learn` prints every verdict he has overruled.

**Searched yesterday:** australia (3 times), bris (3 times), adelaide (2 times), bahrain (2 times), dublin (2 times), pando (2 times), storrington (2 times), tobago (2 times), uppsa (2 times), 18042, almada, ambonville, antrim, berlin, birmingham, birmingham uk, brentano, brist, bru, cambridge.

**App crashes** (last 7 days, store builds; MetricKit, a sample)

| Crashes | Kind | Build | Where | Phones | Last | Fix |
|---:|---|---|---|---:|---|---|
| 1 | crash | 1.0.4 (41) | (no AncientTrees frame) | 1 | 2026-11-15 | none |
| 1 | crash | 1.0.4 (41) | AncientTrees+0x2409a0 | 1 | 2026-11-16 | none |
| 1 | crash | 1.0.4 (41) | AncientTrees+0x35fccc | 1 | 2026-11-20 | none |
| 1 | hang | 1.0.4 (41) | AncientTrees+0x376463 | 1 | 2026-11-21 | none |

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 11-12 | 1 | 28 | 3.6% | 31.4 |
| 11-13 | 1 | 32 | 3.1% | 55.0 |
| 11-14 | 0 | 51 | 0.0% | 57.5 |
| 11-15 | 210 | 363 | 57.9% | 8.2 |
| 11-16 | 116 | 204 | 56.9% | 6.6 |
| 11-17 | 59 | 132 | 44.7% | 15.0 |
| 11-18 | 33 | 67 | 49.3% | 17.8 |
| 11-19 | 19 | 60 | 31.7% | 32.5 |
| 11-20 | 20 | 66 | 30.3% | 22.9 |
| 11-21 *partial* | 13 | 41 | 31.7% | 17.8 |
| **window** | **472** | **1044** | **45.2%** | |
- Top queries (10d): ancient trees app (i487, p1); ancient trees (i15, p36); ancient tree app (i3, p1); hidde burgmans (i2, p2); android au (i1, p1)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-15 | 132 | 13 | 9.8% |
| 11-16 | 211 | 15 | 7.1% |
| 11-17 | 170 | 6 | 3.5% |
| 11-18 | 177 | 9 | 5.1% |
| 11-19 | 226 | 8 | 3.5% |
| 11-20 | 222 | 13 | 5.9% |
| 11-21 | - | - | 0.0% |
| **7 days** | **1138** | **64** | **5.6%** |
- Week before: 928 impressions, 44 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); ancient trees app (c7/i33, p4); platane du square des batignolles (c4/i2, p1); picture of the tree in helsinki city center that was preserved (c3/i2, p4); 太閤シダレザクラ (c3/i2, p5); evelyns mulberry (c3/i1, p3); ancient trees app (c2/i8, p5); who planted the western red cedar tree in blarney ireland (c2/i8, p2)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-21T09:04 | 8.7 | 1 | 9 | 0 | York +1 |
| 11-21T16:16 | 8.9 | 4 | 8 | 2 | Bristol +1, Kandy +1, Le Porge +1, Leamington Spa +1 |
| 11-21T17:03 | 15.3 | 6 | 9 | 6 | Ottawa +4, Stuttgart +2, Bingley, Hasselt |
| 11-21T21:44 | 5.5 | 0 | 9 | 1 | - |
| 11-21T22:42 | 6.4 | 0 | 4 | 2 | - |
| 11-22T04:39 | 3.7 | 0 | 6 | 0 | Philadelphia |
| **6 runs** | **48** | **11** | **45** | | |

- 3 of 6 produced no trees; 1 to 6 commands refused per run; no build has gone live in the last 40 runs.

**What they made**

- Fix the red deploy: Philadelphia banned phrase in a note, sharper Bartram's Ginkgo hero
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- reader judge: The Great Plane of Zhongshan Park (Shanghai, new)
- reader judge: a reader's Pando photograph leads
- reader judge: Great Ginkgo of Kumamoto Castle (Kumamoto, new), Gennett Poplar photo, Kumamoto pin report
- reader judge: second reader's Gennett Poplar photo leads, first moves to the strip
- reader judge: Bronte Creek heritage white oak (Oakville, new), Survivor Tree photo, two pin reports, Leamington ambassador
- Guimaraes wall, two out-of-range leads; claim graz and nuremberg
- Birmingham verify pass 14: Handsworth poplar, oak lead; LOG, costs
- Dominion Arboretum park title under 60 chars: build was failing on it
- San Francisco pass: wall, one lead; LOG
- Dominion Arboretum title carries no count: preflight and the build count app-only trees differently
- Dominion Arboretum park page: title and closer match the five trees on the web (build was failing on the count check)

Machine: 8 chain attempts yesterday, 8 got real work time (~104 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c466/i718); /app (c1/i23); /explore (c1/i16); /united-states/maryland (c1/i4); /girona (c1/i3)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'hidde burgmans' (i2, p2)
    - 'android au' (i1, p1)
    - 'এই অ্যাপের লিংক দাও' (i1, p2)
    - 'angeloak' (i1, p99)
    - 'chêne allouville' (i1, p82)
    - 'chêne guillotin' (i1, p66)

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 207 | 3 | 18 | 0.09 | 1 |
| Not yet rich | 370 | 9 | 16 | 0.04 | 0 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| monterey | 0 | 25 | 0.0% | 75.2 | 0.4% | lone cypress monterey (i7, p76) |
| london | 0 | 14 | 0.0% | 66.9 | 0.4% | flats to rent clerkenwell (i3, p89) |
| tenerife | 0 | 13 | 0.0% | 83.9 | 0.4% | drago tree tenerife (i2, p96) |

- Plus 256 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: singapore, lisbon, amsterdam, barcelona, seville, bath, berlin, rome.
**Sign-in mail sent again** (stuck an hour or more, `scripts/signin_watch.py`): 38 people in 7 days, 7 of them got in afterwards.

## 2026-11-20 (previous UTC day)

**Today: 16 android waitlist signups arrived yesterday (2040 total); 13 tree submissions and an ambassador request for Stratford-upon-Avon and 4 feedback reports arrived yesterday (519 submissions of every kind in all); 31 accounts were opened yesterday (872 accounts in all).**

**North star: 258 people have uploaded a tree or photo of their own (+244 this week); 34 of them did it on more than one day (+30).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 3014 | 35 |
| ... of which from search | every search engine | 89 | 15 |
| ... from Google | Google's recovery | 68 | 10 |
| ... from Bing | Bing | 10 | 0 |
| Website visitors who came back | people who stay | 608 | 7 |
| App downloads (first-time) | people | 6703 | 19 |
| New accounts | people | 804 | 2 |
| Phones back within 30 days | people who stay | 6 of 15 | 4 of 16 |
| Trees saved to Want to go | intent | 487 | 0 |
| Trees collected | goal 1: stood at a tree | 442 | 0 |
| Readers' contributions | data: trees, photos, corrections | 678 | 3 |
| Worth-it votes | one tap, not a contribution | 166 | 0 |
| Shares (app and web) | word of mouth, since 10-30 | 321 | 2 |
| Visits from a shared link | what sharing brings | 116 | 0 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web orange, iOS orange, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | orange: 1 compliance point(s) wait for Hidde (data/compliance.json) | orange: 1 compliance point(s) wait for Hidde (data/compliance.json) | grey: no checks wired yet |
| Live | orange: 1 new error type(s), first "TypeError: Cannot read properties of null (reading 'getBound" in inline | green | grey: no checks wired yet |

**Plus question** (16 answers, 2 new; 5 asked to be told; 8 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| Download offline maps | 7 |
| Something else | 6 |
| A richer log of every tree you've collected | 4 |
| Recommended tree walks for a city trip | 3 |
| Seasonal alerts when trees are at their best | 3 |

**Fixed since 19 Nov: 2.**

| Day | Where | What was wrong | Found by | Test |
|---|---|---|---|---|
| 20 Nov | Web | Map pins stacked under each other and jumped on hover; the chosen pin stood far from its card (pin CSS set position:relative over MapLibr... | a person | yes |
| 19 Nov | Android | Android: directions to Google Maps showed 'Google Maps can't open this link' when Maps was already running (api=1 link with setPackage) | a person | yes |

**New ambassadors yesterday: 2.** Green Fig 1965 (La Tène); Kathryn T (Stratford-upon-Avon). Each got the mail and the badge automatically; 37 ambassadors in all (`python3 scripts/ambassador.py --list`).

**Open for you: nothing.** Feedback handled and recorded: 56 (`python3 scripts/feedback.py`). Reader judge: 91 agent minutes yesterday, 619 in the last 7 days.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-14 | 11-15 | 11-16 | 11-17 | 11-18 | 11-19 | 11-20 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 3 | 1797 | 734 | 297 | 169 | 81 | 66 | **3147** |
| New accounts | 2 | 371 | 199 | 100 | 62 | 39 | 31 | **804** |
| Saves | 0 | 187 | 143 | 38 | 58 | 28 | 33 | **487** |
| Android waitlist | 0 | 1317 | 416 | 158 | 61 | 22 | 16 | **1990** |
| App downloads | 1 | 3896 | 1588 | 712 | 351 | 153 | – | **6701** |
| App deletions | – | 11 | 16 | 14 | 10 | 7 | – | **58** |
| App phones | 8 | 3563 | 1693 | 950 | 623 | 481 | 418 | **6350** |
| Trees opened in the app | 18 | 7608 | 3264 | 1849 | 1103 | 864 | 595 | **15301** |
| Trees collected | 3 | 96 | 59 | 30 | 21 | 42 | 14 | **265** |
| Trees sent | 0 | 98 | 51 | 37 | 14 | 30 | 13 | **243** |
| Feedback | 0 | 29 | 23 | 15 | 42 | 18 | 12 | **139** |
| Worth-it votes | 0 | 62 | 44 | 20 | 16 | 15 | 9 | **166** |
| Ambassador asks | 0 | 5 | 3 | 2 | 0 | 5 | 1 | **16** |
| Website photos | 0 | 9 | 3 | 6 | 3 | 1 | 2 | **24** |
| iPhone photos | 3 | 185 | 104 | 74 | 41 | 47 | 32 | **486** |
| Android photos | 0 | 0 | 0 | 0 | 0 | 26 | 1 | **27** |
| Tree notes | 1 | 15 | 23 | 11 | 15 | 6 | 3 | **74** |
| App Store reviews | 0 | 4 | 2 | 1 | 0 | 1 | 0 | **8** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.
- App deletions count only phones that share analytics with developers, and Apple leaves out days too small to show: read it against the installs of the same day, not as a total.

**Feedback by kind** (the Feedback row above, split; their words are in the readers-in-full block)

| Kind | 11-20 | **7 days** |
|---|---:|---:|
| Pin moved | 3 | **53** |
| Written feedback | 4 | **57** |
| Report on a tree | 5 | **29** |
| Collected far from our pin | 0 | **1** |

**Trees readers sent, for you to inspect** (98 you have not looked at; ours left out)

| Judged | Reader | Tree | Where | Species | Their girth | Our verdict | Page |
|---|---|---|---|---|---:|---|---|
| 2026-11-20 | A | The Last Elm of Stationsplein | Amsterdam | Dutch Elm (Ulmus x hollandica) | - | hold | - |
| 2026-11-20 | B | The Plane of Montée Saint-Sébastien | Lyon | London Plane (Platanus x aceri | - | hold | - |
| 2026-11-20 | C | Tyler Arboretum Giant Sequoia (2 photos) | Media | Giant Sequoia (Sequoiadendron  | - | hold | - |
| 2026-11-20 | C | - | Media | - | - | hold | - |
| 2026-11-20 | D | A tree I found (8 photos) | - | - | - | hold | - |
| 2026-11-19 | E | The Maples of Hugo Conwentz | Gdansk | Field Maple (Acer campestre) | - | hold | - |
| 2026-11-19 | E | The Ivy Elm of Park Oliwski (2 photos) | Gdansk | European White Elm (Ulmus laev | - | hold | - |
| 2026-11-19 | F | Dragon Tree in Madeira | - | Dragon Tree | - | hold | - |
| 2026-11-19 | G | The Cut-Leaved Alder | York | Common Alder (Alnus glutinosa  | - | hold | - |
| 2026-11-19 | G | The Pear-Barked Beech | York | European Beech (Fagus sylvatic | - | hold | - |
| 2026-11-19 | H | Fig | - | Fig | - | hold | - |
| 2026-11-19 | I | The Amur Cork Trees and Crimean Linden of Be (2 photos) | Vilnius | Amur Cork Tree (Phellodendron  | - | hold | - |
| 2026-11-19 | I | - | Vilnius | - | - | hold | - |
| 2026-11-19 | I | The Sapiegos Park Linden | Vilnius | Small-leaved Lime (Tilia corda | - | hold | - |
| 2026-11-19 | I | - | Vilnius | - | - | hold | - |
| 2026-11-18 | C | The Sprawling Sycamore of Pawling Farm | Valley Forge | American Sycamore (Platanus oc | - | hold | - |
| 2026-11-18 | J | The Remnant River Red Gum of Edinburgh Garde (4 photos) | Melbourne | River Red Gum (Eucalyptus cama | - | hold | - |
| 2026-11-18 | J | The Southern Mahogany of Edinburgh Gardens (2 photos) | Melbourne | Southern Mahogany (Eucalyptus  | - | hold | - |
| 2026-11-18 | J | - | Melbourne | - | - | hold | - |
| 2026-11-18 | K | The Bidwill Kauri Pine | Sydney | Queensland Kauri (Agathis robu | - | hold | - |
| 2026-11-18 | J | The Holm Oak of Darling Gardens | Melbourne | Holm Oak (Quercus ilex) | - | hold | - |
| 2026-11-18 | L | The Knotted Tree of Mexikópuszta | Fertőújlak | Japanese Pagoda Tree or Black  | - | hold | - |
| 2026-11-18 | ? | The Casuarina of the Cascada (2 photos) | Barcelona | River She-oak (Casuarina cunni | - | hold | - |
| 2026-11-18 | M | Ancient Cedar at Makata Jinjya | - | Japanese Cedar | 800 cm | hold | - |
| 2026-11-18 | N | Bur Oak | - | Bur Oak | 323 cm | hold | - |
| 2026-11-17 | O | - | - | - | - | hold | - |
| 2026-11-17 | ? | - | - | - | - | hold | - |
| 2026-11-17 | O | - | - | - | - | hold | - |
| 2026-11-17 | O | - | - | - | - | hold | - |
| 2026-11-17 | P | - | - | - | - | hold | - |
| 2026-11-17 | P | - | - | - | - | hold | - |
| 2026-11-17 | Q | A tree in Los Angeles | - | - | - | hold | - |
| 2026-11-17 | R | A tree near Copenhagen | - | - | - | hold | - |
| 2026-11-17 | S | Blue Jacaranda in ISA | - | Blue Jacaranda | - | hold | - |
| 2026-11-17 | S | Judas Tree in ISA | - | Judas Tree | - | hold | - |
| 2026-11-17 | K | Queensland Kauri in Sydney | - | Queensland Kauri | - | hold | - |
| 2026-11-17 | T | Pecan | - | Pecan | - | hold | - |
| 2026-11-17 | U | Ahuehuete del Jardin de San Fernando (2 photos) | Mexico City | - | - | hold | - |
| 2026-11-17 | T | Pecan | Griffin | Pecan | - | hold | - |
| 2026-11-17 | V | The Cosgrove House Banyan (2 photos) | Key West | Fig (Ficus sp.) | - | hold | - |
| 2026-11-17 | V | Jindai-zakura (Yamataka Jindai Zakura) | Hokuto | Higan Cherry (Prunus subhirtel | - | hold | - |
| 2026-11-17 | W | Black Mulberry in London | - | Black Mulberry | 250 cm | hold | - |
| 2026-11-17 | X | The Finsbury Circus Pagoda Tree | London | Japanese Pagoda Tree (Styphnol | - | hold | - |
| 2026-11-17 | Y | Le Chêne de la Vierge | - | Oak | 250 cm | hold | - |
| 2026-11-17 | Z | The Moreton Bay Fig of Curtain Square | - | - | - | hold | - |
| 2026-11-17 | X | A London plane in Finsbury Circus Gardens | - | London Plane (Platanus x aceri | - | hold | - |
| 2026-11-17 | A1 | A dead sweet chestnut in the Kastanologos fo | - | Sweet Chestnut (Castanea sativ | - | hold | - |
| 2026-11-17 | B1 | The Totteridge Yew | London | European Yew (Taxus baccata) | - | hold | - |
| 2026-11-17 | C1 | Queen Elizabeth’s Oak in Greenwich Park | - | Pedunculate Oak | - | hold | - |
| 2026-11-17 | D1 | - | - | - | - | hold | - |
| 2026-11-17 | E1 | - | - | - | - | hold | - |
| 2026-11-17 | F1 | - | - | - | - | hold | - |
| 2026-11-17 | G1 | - (2 photos) | - | - | - | hold | - |
| 2026-11-17 | ? | Romantik-Eiche | Heidelberg | - | - | lead | - |
| 2026-11-17 | H1 | - | Azores | - | - | hold | - |
| 2026-11-17 | I1 | Ekebyhovseken | Ekerö | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-17 | J1 | Orange | - | Orange (Citrus sinensis) | - | hold | - |
| 2026-11-17 | ? | BB61E294-5FFB-4378-960A-64DAB336FD46 | - | - | - | hold | - |
| 2026-11-17 | ? | CAA9C183-3017-433B-A1CA-09E1CAA99BF3 | - | - | - | hold | - |
| 2026-11-17 | ? | The Signal Tree (Native American'Indian Sign | Akron, Ohio, USA | - | 122 cm | hold | - |
| 2026-11-16 | K1 | American Elm | - | American Elm | - | hold | - |
| 2026-11-16 | K1 | Eastern Cottonwood (2 photos) | - | Eastern Cottonwood | - | hold | - |
| 2026-11-16 | K1 | White Oak | - | White Oak | - | hold | - |
| 2026-11-16 | K1 | Northern Red Oak | - | Northern Red Oak | - | hold | - |
| 2026-11-16 | L1 | Linden tree next to the pond | - | Lime (Tilia sp.) | 166 cm | hold | - |
| 2026-11-16 | M1 | Prince Eugen's Oak | - | Oak (Quercus sp.) | - | hold | - |
| 2026-11-16 | N1 | A tree near Helmond | - | - | - | hold | - |
| 2026-11-16 | O1 | - | - | ridged furrowed bark, spreadin | - | hold | - |
| 2026-11-16 | P1 | A tree near Westonbirt Arboretum | - | - | - | hold | - |
| 2026-11-16 | ? | The Famous Nossob Camel Thorn Tree | Kgalagadi Transfrontier Park | - | - | lead | - |
| 2026-11-15 | Q1 | Endangered Dawn Redwood in Holborn, legal di | - | Dawn Redwood | - | hold | - |
| 2026-11-15 | H1 | Giant Australian Rubber Tree of Jardim Anton | Azores | Moreton Bay Fig (Ficus macroph | - | hold | - |
| 2026-11-15 | R1 | Deans Oak | - | - | 1200 cm | hold | - |
| 2026-11-15 | S1 | Scots Pine in Dunkeld | - | Scots Pine | 660 cm | hold | - |
| 2026-11-15 | T1 | Tree in Waitangi | - | - | - | hold | - |
| 2026-11-15 | G1 | - | - | - | - | hold | - |
| 2026-11-15 | U1 | - | - | - | - | hold | - |
| 2026-11-15 | V1 | - | - | - | - | hold | - |
| 2026-11-15 | V1 | - | - | - | - | hold | - |
| 2026-11-15 | V1 | - | - | - | - | hold | - |
| 2026-11-15 | W1 | - | - | - | - | hold | - |
| 2026-11-15 | X1 | The Witch Tree of Fanal | Madeira | Til / Stinkwood (Ocotea foeten | - | hold | - |
| 2026-11-15 | Y1 | Marton Oak | - | Pedunculate Oak | - | hold | - |
| 2026-11-15 | Z1 | Malmö | - | - | - | hold | - |
| 2026-11-15 | A2 | Blue Jacaranda in Melbourne | - | Blue Jacaranda | - | hold | - |
| 2026-11-15 | B2 | English Hawthorn | - | English Hawthorn (Crataegus la | 50 cm | hold | - |
| 2026-11-15 | C2 | Wistman's Wood | Dartmoor | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-15 | D2 | Grimston's Oak | London | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-15 | C2 | The Crom Yews | Crom | European Yew (Taxus baccata) | - | hold | - |
| 2026-11-15 | C2 | The Dawn Redwood by the Kelvin Statue (2 photos) | Belfast | Dawn Redwood (Metasequoia glyp | - | hold | - |
| 2026-11-15 | C2 | S'Olivera de Cort | Palma de Mallorca | Olive (Olea europaea) | - | hold | - |
| 2026-11-15 | E2 | A tree near Chiang Mai | - | - | - | hold | - |
| 2026-11-15 | F2 | Il cipresso calvo di Villa Smeraldi | - | Cypress (Cupressus sp.) | - | hold | - |
| 2026-11-15 | C2 | The Boole Library Redwoods | Cork | Redwood | - | hold | - |
| 2026-11-15 | ? | Oak tree, Quercus Robur. | Bagni di Lusnizza, Udine | - | 454 cm | lead | - |
| 2026-11-15 | ? | 71F93157-AEF9-41A4-AF61-E1AD9755F9B1 | - | - | - | hold | - |
| 2026-11-15 | ? | 24FDCCB3-A454-4556-8169-2BAD2FB36ABD | - | - | - | hold | - |
| 2026-11-15 | ? | C7962FE1-14DB-407A-B62F-CFA617580655 | - | - | - | hold | - |
- From 58 readers: reader C2 5, reader I 4, reader J 4, reader K1 4, reader C 3, reader O 3, reader V1 3, reader E 2, reader G 2, reader G1 2, reader H1 2, reader K 2, reader P 2, reader S 2, reader T 2, reader V 2, reader X 2, reader A 1, reader A1 1, reader A2 1, reader B 1, reader B1 1, reader B2 1, reader C1 1, reader D 1, reader D1 1, reader D2 1, reader E1 1, reader E2 1, reader F 1, reader F1 1, reader F2 1, reader H 1, reader I1 1, reader J1 1, reader L 1, reader L1 1, reader M 1, reader M1 1, reader N 1, reader N1 1, reader O1 1, reader P1 1, reader Q 1, reader Q1 1, reader R 1, reader R1 1, reader S1 1, reader T1 1, reader U 1, reader U1 1, reader W 1, reader W1 1, reader X1 1, reader Y 1, reader Y1 1, reader Z 1, reader Z1 1.
- Photographs and the readers' own words: `python3 scripts/inspect_readers.py` (a local page, never in this public file). Your answer goes in with `python3 scripts/judgement.py --feedback <id> "..."`.

**Waiting for you** (what the runs left for you since 2026-11-20)

- 229 email addresses ready to mail (archive 0, nature 9, guide 4, press 122, source 58, council 16, society 7, tourism 5, other 5, garden 3); **the night run found no new contacts in two days**
- a suggested reply in drafts/reply-reader-1000104-2026-11-20.md.
- the daily task "publish-held-trees-daily" can be switched off under Scheduled; write passes put trees straight into the app, so nothing waits for it.
- tapping the name itself no longer opens the tree, only the photograph does; say if you want the name to be the tap target at 44 points instead.
- paste supabase/photo-likes.sql** in the Supabase SQL editor.
- paste supabase/photo-authors-time.sql** in the Supabase SQL editor.
- Jakub (dendrologist)
- replies to Deb (1232, ambassador of her hometown)
- the city map's zoomed-out cities list exists nowhere else (explore and both apps list the trees in view); and /explore's nearest tree says km where the apps use the reader's units.

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-19 | G2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | H2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | I2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | I2 | The Kapok Tree | Key West | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/key-west/kapok-tree) |
| 11-19 | I2 | The Cosgrove House Banyan | Key West | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/key-west/cosgrove-house-banyan) |
| 11-19 | I2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | I2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | I2 | Grandfather Pine at Serenbe | Serenbe | a reader's photograph, published | [live](https://ancienttrees.app/serenbe/grandfather-pine-at-serenbe) |
| 11-19 | I2 | Grandmother Beech at Serenbe | Serenbe | a reader's photograph, published | [live](https://ancienttrees.app/serenbe/grandmother-beech-at-serenbe) |
| 11-19 | I2 | The McDonogh Oak | New Orleans | a reader's photograph, published | [live](https://ancienttrees.app/new-orleans/mcdonogh-oak) |
| 11-19 | I2 | The Anseman Oak | New Orleans | a reader's photograph, published | [live](https://ancienttrees.app/new-orleans/anseman-oak) |
| 11-19 | I2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | I2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | I2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | I2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | I2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | I2 | The Moreton Bay Fig of Balboa Park | San Diego | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/san-diego/moreton-bay-fig-of-balboa-park) |
| 11-19 | E | The Maples of Hugo Conwentz | Gdansk | a reader's photograph, published | [live](https://ancienttrees.app/gdansk/maples-of-hugo-conwentz) |
| 11-19 | J2 | The Leaning Fig over the Boardwalk | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/leaning-fig-over-the-boardwalk) |
| 11-19 | J2 | The Leaning Fig over the Boardwalk | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/leaning-fig-over-the-boardwalk) |
| 11-19 | F |  | ? | a reader's photograph, published | not live yet |
| 11-19 | E | The Cucumber Magnolia of Park Oliwski | Gdansk | a reader's photograph, published | [live](https://ancienttrees.app/gdansk/cucumber-magnolia-of-park-oliwski) |
| 11-19 | E | The Cucumber Magnolia of Park Oliwski | Gdansk | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/gdansk/cucumber-magnolia-of-park-oliwski) |
| 11-19 | E | The Giant Thuja of Park Oliwski | Gdansk | a reader's photograph, published | [live](https://ancienttrees.app/gdansk/giant-thuja-of-park-oliwski) |
| 11-19 | E | The Giant Thuja of Park Oliwski | Gdansk | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/gdansk/giant-thuja-of-park-oliwski) |
| 11-19 | E | The Three-Trunked Katsura of Park Oliwski | Gdansk | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/gdansk/three-trunked-katsura-of-park-oliwski) |
| 11-19 | J | The Finer Holm Oak of Edinburgh Gardens | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/finer-holm-oak-of-edinburgh-gardens) |
| 11-19 | J | The Finer Holm Oak of Edinburgh Gardens | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/finer-holm-oak-of-edinburgh-gardens) |
| 11-19 | J | The Gum by the Edinburgh Gardens Skate Bowl | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/gum-by-the-edinburgh-gardens-skate-bowl) |
| 11-19 | K2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | K2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | K2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | K2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | K2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | K2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | L2 | The Giant Sequoias of the Tall Trees Trail | New Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/new-forest/giant-sequoias-of-the-tall-trees-trail) |
| 11-19 | B | The Plane Tree of Place Antoine-Rivoire | Lyon | a reader's photograph, published | [live](https://ancienttrees.app/lyon/plane-tree-of-place-antoine-rivoire) |
| 11-19 | B | The Plane Tree of Place Antoine-Rivoire | Lyon | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/lyon/plane-tree-of-place-antoine-rivoire) |
| 11-19 | M2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | G | The Cut-Leaved Alder | York | a reader's photograph, published | [live](https://ancienttrees.app/york/cut-leaved-alder) |
| 11-19 | G | The Willow-Leaved Ash | York | a reader's photograph, published | [live](https://ancienttrees.app/york/willow-leaved-ash) |
| 11-19 | G | The Pear-Barked Beech | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/pear-barked-beech) |
| 11-19 | G | The Cut-Leaved Hornbeam | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/cut-leaved-hornbeam) |
| 11-19 | G | The Cut-Leaved Hornbeam | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/cut-leaved-hornbeam) |
| 11-19 | N2 | The Cedar of Jussieu | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/cedar-of-jussieu) |
| 11-19 | O2 | The Circus Ground Oak of Saratoga Park | New York | a reader's photograph, published | [live](https://ancienttrees.app/new-york/circus-ground-oak-of-saratoga-park) |
| 11-19 | O2 | The Ginkgo of the United Order of Tents | New York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/new-york/ginkgo-of-the-united-order-of-tents) |
| 11-19 | P2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | W1 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | W1 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | Q2 | The Sweet Chestnut of Hulsbeek | Geetbets | a reader's photograph, published | [live](https://ancienttrees.app/geetbets/sweet-chestnut-of-hulsbeek) |
| 11-19 | R2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | R2 | Grant Crescent Blue Gums | Canberra | a reader's photograph, published | [live](https://ancienttrees.app/canberra/grant-crescent-blue-gums) |
| 11-19 | S2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | T2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | C | The Brandywine Sycamore (Lafayette Sycamore) | Chadds Ford | a reader's photograph, published | [live](https://ancienttrees.app/chadds-ford/brandywine-sycamore-lafayette-sycamore) |
| 11-19 | U2 | Old Albert | Auckland | a reader's photograph, published | [live](https://ancienttrees.app/auckland/old-albert) |
| 11-19 | U2 | Old Albert | Auckland | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/auckland/old-albert) |
| 11-20 | V2 | The Leaf-Seed Ginkgo of Inada Gobo | Kasama | a reader's photograph, published | [live](https://ancienttrees.app/kasama/leaf-seed-ginkgo-of-inada-gobo) |
| 11-20 | W2 | The banyan of Nhan Dan, 71 Hang Trong | Hanoi | a reader's photograph, published | [live](https://ancienttrees.app/hanoi/banyan-of-nhan-dan-71-hang-trong) |
| 11-20 | X2 |  | ? | a reader's photograph, published | not live yet |
| 11-20 | M |  | ? | a reader's photograph, published | not live yet |
| 11-20 | Y2 |  | ? | a reader's photograph, published | not live yet |
| 11-20 | Z2 | The St Mary Magdalene Plane | London | a reader's photograph, published | [live](https://ancienttrees.app/london/st-mary-magdalene-plane) |
| 11-20 | B | The Plane of Montée Saint-Sébastien | Lyon | a reader's photograph, published | [live](https://ancienttrees.app/lyon/plane-of-montee-saint-sebastien) |
| 11-20 | A3 |  | ? | a reader's photograph, published | not live yet |
| 11-20 | B3 |  | ? | a reader's photograph, published | not live yet |
| 11-20 | A | The Last Elm of Stationsplein | Amsterdam | a reader's photograph, published | [live](https://ancienttrees.app/amsterdam/last-elm-of-stationsplein) |
| 11-20 | C3 | The Last Elm of Stationsplein | Amsterdam | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/amsterdam/last-elm-of-stationsplein) |
| 11-20 | B | The Plane of Montée Saint-Sébastien | Lyon | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/lyon/plane-of-montee-saint-sebastien) |
| 11-20 | D3 | The Silky Oaks of Largo Marques de Pombal | Setubal | a reader's photograph, published | [live](https://ancienttrees.app/setubal/silky-oaks-of-largo-marques-de-pombal) |
| 11-20 | E3 | The Twisted Beech of Square des Arenes de Lutece | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/twisted-beech-of-square-des-arenes-de-lutece) |
| 11-20 | F3 | The Betsey Williams Sycamore | Providence | a reader's photograph, published | [live](https://ancienttrees.app/providence/betsey-williams-sycamore) |
| 11-20 | G3 | Il Platano del Giardino Bazlen | Milan | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/milan/il-platano-del-giardino-bazlen) |
| 11-20 | G3 | Il Platano del Giardino Bazlen | Milan | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/milan/il-platano-del-giardino-bazlen) |
| 11-20 | C | Tyler Arboretum Painter Ginkgo | Media | a reader's photograph, published | [live](https://ancienttrees.app/media-pennsylvania/tyler-arboretum-painter-ginkgo) |
| 11-20 | C | Tyler Arboretum Giant Sequoia | Media | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/media-pennsylvania/tyler-arboretum-giant-sequoia) |
| 11-20 | C | Tyler Arboretum Giant Sequoia | Media | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/media-pennsylvania/tyler-arboretum-giant-sequoia) |
| 11-20 | C |  | ? | a reader's photograph, published | not live yet |
| 11-20 | C | The Brandywine Sycamore (Lafayette Sycamore) | Chadds Ford | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/chadds-ford/brandywine-sycamore-lafayette-sycamore) |
| 11-20 | H3 | The Split Oak on the Stoke Park Slope | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/split-oak-on-the-stoke-park-slope) |
| 11-20 | H3 | The Antlered Oak | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/antlered-oak) |
| 11-20 | H3 | The Thick-trunked Willow of the Rideau Canal | Ottawa | a reader's photograph, published | [live](https://ancienttrees.app/ottawa/thick-trunked-willow-of-the-rideau-canal) |
| 11-20 | I3 | The Furrowed Giant of Curtain Square | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/furrowed-giant-of-curtain-square) |
| 11-20 | K | The Furrowed Giant of Curtain Square | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/furrowed-giant-of-curtain-square) |
| 11-20 | K | The Furrowed Giant of Curtain Square | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/furrowed-giant-of-curtain-square) |
| 11-20 | I3 | The Moreton Bay Fig of Curtain Square | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/moreton-bay-fig-of-curtain-square) |
| 11-20 | K | The Moreton Bay Fig of Curtain Square | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/moreton-bay-fig-of-curtain-square) |
| 11-21 | J3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | K3 |  | ? | a reader's photograph, published | not live yet |
| 11-21 | K3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | L3 | C7DCA666-5183-4987-B585-0F10639B5CB3 | Laténa | a reader's feedback changed the page | - |
| 11-19 | R2 | can_008 (Grant Crescent Blue Gums) | Canberra | a reader's correction changed the page | - |
| 11-20 | W2 | hni_003 (The banyan of Nhan Dan, 71 Hang Trong) | Hanoi | a reader's correction changed the page | - |
| 11-20 | K2 | mum_002 (The Rain Trees of Govt Gate Road) | Mumbai | a reader's feedback changed the page | - |
| 11-20 | C | mdp_003 (Tyler Arboretum Painter Cedar of Lebanon) | Media | a reader's feedback changed the page | - |
| 11-20 | C | Tyler Arboretum Painter Ginkgo | Media | a reader's correction changed the page | - |
| 11-20 | C | Tyler Arboretum Giant Sequoia | Media | a reader's correction changed the page | - |
- From 42 readers: reader I2 15, reader C 9, reader K2 7, reader E 6, reader G 5, reader B 4, reader H3 3, reader J 3, reader K 3, reader R2 3, reader G3 2, reader I3 2, reader J2 2, reader K3 2, reader O2 2, reader U2 2, reader W1 2, reader W2 2, reader A 1, reader A3 1, reader B3 1, reader C3 1, reader D3 1, reader E3 1, reader F 1, reader F3 1, reader G2 1, reader H2 1, reader J3 1, reader L2 1, reader L3 1, reader M 1, reader M2 1, reader N2 1, reader P2 1, reader Q2 1, reader S2 1, reader T2 1, reader V2 1, reader X2 1, reader Y2 1, reader Z2 1.

**What was sent in, and what we decided**

| seen | what | where | size for its species | ours | Hidde |
|---|---|---|---|---|---|
| 2026-11-19 | The Ivy Elm of Park Oliwski | Gdansk | - | hold | - |
| 2026-11-19 | A tree I found | - | - | hold | - |
| 2026-11-19 | The Amur Cork Trees and Crimean Linden | Vilnius | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | lead | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | A tree I found | - | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | The Southern Mahogany of Edinburgh Gar | Melbourne | - | hold | - |
| 2026-11-18 | The Casuarina of the Cascada | Barcelona | - | hold | - |
| 2026-11-18 | a tree we do not map | - | - | lead | - |
| 2026-11-17 | Ahuehuete del Jardin de San Fernando | Mexico City | - | hold | - |
| 2026-11-17 | The Cosgrove House Banyan | Key West | - | hold | - |
| 2026-11-17 | European Beech in Baarn | - | - | hold | - |
| 2026-11-17 | European Beech in Baarn | - | - | hold | - |
| 2026-11-17 | a tree we do not map | Baarn | - | hold | - |

0 waiting for a verdict. Disagree with one and the rule changes: `python3 scripts/judgement.py --feedback <id> "..."`, and `--learn` prints every verdict he has overruled.

**Searched yesterday:** frankfurt (12 times), milwaukee (6 times), paris (6 times), milwa (4 times), toronto (4 times), barce (3 times), carlow (3 times), lille (3 times), sound (3 times), bray (2 times), frank (2 times), isle of wight (2 times), london (2 times), maidenhead (2 times), mammutbaum frankfurt (2 times), melbourne (2 times), mukwonago (2 times), seaford (2 times), vancouver (2 times), 11221.

**App crashes** (last 7 days, store builds; MetricKit, a sample)

| Crashes | Kind | Build | Where | Phones | Last | Fix |
|---:|---|---|---|---:|---|---|
| 1 | crash | 1.0.4 (41) | (no AncientTrees frame) | 1 | 2026-11-15 | none |
| 1 | crash | 1.0.4 (41) | AncientTrees+0x2409a0 | 1 | 2026-11-16 | none |
| 1 | crash | 1.0.4 (41) | AncientTrees+0x35fccc | 1 | 2026-11-20 | none |

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 11-11 | 1 | 16 | 6.2% | 22.1 |
| 11-12 | 1 | 28 | 3.6% | 31.4 |
| 11-13 | 1 | 32 | 3.1% | 55.0 |
| 11-14 | 0 | 51 | 0.0% | 57.5 |
| 11-15 | 210 | 363 | 57.9% | 8.2 |
| 11-16 | 116 | 204 | 56.9% | 6.6 |
| 11-17 | 59 | 132 | 44.7% | 15.0 |
| 11-18 | 33 | 67 | 49.3% | 17.8 |
| 11-19 | 19 | 60 | 31.7% | 32.5 |
| 11-20 *partial* | 16 | 46 | 34.8% | 22.7 |
| **window** | **456** | **999** | **45.6%** | |
- Top queries (10d): ancient trees app (i471, p1); ancient trees (i14, p39); ancient tree app (i3, p1); hidde burgmans (i2, p2); android au (i1, p1)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-14 | 103 | 6 | 5.8% |
| 11-15 | 132 | 13 | 9.8% |
| 11-16 | 211 | 15 | 7.1% |
| 11-17 | 170 | 6 | 3.5% |
| 11-18 | 177 | 9 | 5.1% |
| 11-19 | 226 | 8 | 3.5% |
| 11-20 | - | - | 0.0% |
| **7 days** | **1019** | **57** | **5.6%** |
- Week before: 905 impressions, 45 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); ancient trees app (c7/i33, p4); platane du square des batignolles (c4/i2, p1); picture of the tree in helsinki city center that was preserved (c3/i2, p4); 太閤シダレザクラ (c3/i2, p5); evelyns mulberry (c3/i1, p3); ancient trees app (c2/i8, p5); who planted the western red cedar tree in blarney ireland (c2/i8, p2)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-20T07:39 | 5.3 | 0 | 7 | 1 | - |
| 11-20T09:33 | 5.7 | 0 | 13 | 4 | Balmerino, Barcelona, Bologna, Cambridge, +11 more |
| 11-20T18:13 | 10.4 | 0 | 12 | 0 | - |
| 11-20T19:03 | 10.3 | 2 | 7 | 0 | Cofton Hackett +1, Hallstatt +1 |
| 11-21T00:53 | 4.0 | 0 | 8 | 0 | - |
| 11-21T01:03 | 2.6 | 0 | 6 | 1 | - |
| **6 runs** | **38** | **2** | **53** | | |

- 5 of 6 produced no trees; 1 to 4 commands refused per run; last build that went live: 2h ago.

**What they made**

- Reader judge: the Castlemaine stone pine goes live (cmn_002), so the place has two trees; intro and meta name it; LOG
- Reader judge: the 1863 Royal Oak of Castlemaine goes live
- Discover's New from visitors: the tree name under the photograph is plain text, not a 34 point link (appfit SMALL, ios.yml red 2026-11-21)
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- Reader judge: the Great Cedar of Parc Chambrun live in Nice (tip-1340), named by the city's own park page
- Reader judge: the Curtain Square fig's first two photographs, its pin moved to them (confirmed); the plane's register pin set approximate
- Reader judge: two Bristol oaks, a Rideau Canal willow, and an elm in Curtain Square that three photos sent as our fig; mel_005's pin set approximate
- Reader judge: the Willistown oak's owner is happy for it to be on the site (mail reply 1332 handled)
- Reader judge: the White Oak of Bryan Avenue live in Willistown; a reader's 7.25 m and school-children photo on the Brandywine Sycamore
- Reader judge: Tyler sequoia gets a reader's photographs and GPS pin; a second sequoia held for its location; cedar stump rejected
- Night run: Hallstatt deepen, 2 trees written, claims released, LOG
- Write and merge hst_008 (Sterzens Abendsitz limes, Bad Ischl) and cft_001 (Cofton Hackett phoenix yew)

**Reader photographs in a strip, live first, not yet looked at** (1)

| Day | Tree | Where | Undo |
|---|---|---|---|
| 11-19 | The Finer Holm Oak of Edinburgh Gardens | Melbourne | `sightings_publish.py --unstrip b6bb10c9-d418-4437-b701-1015e35e7f5f` |

Machine: 5 chain attempts yesterday, 5 got real work time (~69 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c447/i683); /app (c1/i22); /explore (c1/i15); /united-states/maryland (c1/i4); /girona (c1/i3)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'hidde burgmans' (i2, p2)
    - 'android au' (i1, p1)
    - 'এই অ্যাপের লিংক দাও' (i1, p2)
    - 'angeloak' (i1, p99)
    - 'chêne allouville' (i1, p82)
    - 'chêne guillotin' (i1, p66)

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 200 | 3 | 18 | 0.09 | 1 |
| Not yet rich | 338 | 9 | 15 | 0.04 | 0 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| monterey | 0 | 20 | 0.0% | 77.3 | 0.4% | lone cypress monterey (i5, p79) |
| london | 0 | 14 | 0.0% | 66.9 | 0.4% | flats to rent clerkenwell (i3, p89) |
| tenerife | 0 | 13 | 0.0% | 83.9 | 0.4% | drago tree tenerife (i2, p96) |

- Plus 256 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: singapore, lisbon, amsterdam, barcelona, seville, bath, berlin, rome.
**Sign-in mail sent again** (stuck an hour or more, `scripts/signin_watch.py`): 38 people in 7 days, 6 of them got in afterwards.

## 2026-11-19 (previous UTC day)

**Today: 22 android waitlist signups arrived yesterday (2027 total); 30 tree submissions and an ambassador request for Brisbane and an ambassador request for Gdansk and an ambassador request for Inistioge and an ambassador request for Réno-Valdieu and an ambassador request for York and 8 feedback reports arrived yesterday (500 submissions of every kind in all); 39 accounts were opened yesterday (844 accounts in all).**

**North star: 245 people have uploaded a tree or photo of their own (+232 this week); 30 of them did it on more than one day (+26).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 2972 | 33 |
| ... of which from search | every search engine | 87 | 15 |
| ... from Google | Google's recovery | 67 | 10 |
| ... from Bing | Bing | 8 | 1 |
| Website visitors who came back | people who stay | 588 | 8 |
| App downloads (first-time) | people | 6552 | 19 |
| New accounts | people | 773 | 2 |
| Phones back within 30 days | people who stay | 6 of 13 | 4 of 16 |
| Trees saved to Want to go | intent | 457 | 0 |
| Trees collected | goal 1: stood at a tree | 387 | 1 |
| Readers' contributions | data: trees, photos, corrections | 633 | 1 |
| Worth-it votes | one tap, not a contribution | 157 | 0 |
| Shares (app and web) | word of mouth, since 10-30 | 297 | 2 |
| Visits from a shared link | what sharing brings | 105 | 0 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web red, iOS orange, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | orange: 1 compliance point(s) wait for Hidde (data/compliance.json) | orange: 1 compliance point(s) wait for Hidde (data/compliance.json) | grey: no checks wired yet |
| Live | red: photographs look soft, oversized or broken on the live site (photos-live.yml; python3 scripts/photocheck.py --live names them) | green | grey: no checks wired yet |

**Plus question** (14 answers, 2 new; 5 asked to be told; 7 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| Something else | 6 |
| Download offline maps | 5 |
| A richer log of every tree you've collected | 4 |
| Seasonal alerts when trees are at their best | 3 |
| Recommended tree walks for a city trip | 2 |

**New ambassadors yesterday: 5.** kubacho c. (Gdansk); Laurie G. (York); Michèle G. (Réno-Valdieu); Olivia B. (Brisbane); Ram Jack (Inistioge). Each got the mail and the badge automatically; 35 ambassadors in all (`python3 scripts/ambassador.py --list`).

**Open for you** (5; everything else handled and recorded, 47 feedback in all)

| What | Why it waits | Summary |
|---|---|---|
| feedback 1156 | your call | a short yes, probably to our ask to quote 'well worth a visit' on cam_011; confirm the draft went, then set quote_ok and the quote can go on the page |
| feedback 1232 | your call | Mail reply: declines the ambassador role, asks the standard height for girth; suggested answer in drafts |
| feedback 1240 | your call | Cedar girth added to prf_001 as the reader's measure; commune rename and ambassador wish wait for Hidde, draft in drafts/ |
| feedback 1265 | your call | Yes to the Android test offer in today's reply about Old Knobbley; adding them to the testers is a session's step |
| feedback 1273 | your call | A reader who studied trees and works to save endangered ones offers help with the app and advice; a possible ambassador or adviser, his call how to answer. |

Reader judge: 152 agent minutes yesterday, 528 in the last 7 days.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-13 | 11-14 | 11-15 | 11-16 | 11-17 | 11-18 | 11-19 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 5 | 3 | 1797 | 734 | 297 | 169 | 81 | **3086** |
| New accounts | 0 | 2 | 371 | 199 | 100 | 62 | 39 | **773** |
| Saves | 0 | 0 | 189 | 143 | 39 | 58 | 28 | **457** |
| Android waitlist | 0 | 0 | 1317 | 416 | 158 | 61 | 22 | **1974** |
| App downloads | 2 | 1 | 3896 | 1588 | 712 | 351 | – | **6550** |
| App deletions | – | – | 11 | 16 | 14 | 10 | – | **51** |
| App phones | 5 | 8 | 3563 | 1692 | 950 | 623 | 481 | **6168** |
| Trees opened in the app | 4 | 18 | 7608 | 3264 | 1849 | 1103 | 864 | **14710** |
| Trees collected | 0 | 3 | 96 | 59 | 30 | 21 | 42 | **251** |
| Trees sent | 1 | 0 | 98 | 51 | 37 | 14 | 30 | **231** |
| Feedback | 0 | 0 | 29 | 23 | 15 | 42 | 18 | **127** |
| Worth-it votes | 0 | 0 | 62 | 44 | 20 | 16 | 15 | **157** |
| Ambassador asks | 0 | 0 | 5 | 3 | 2 | 0 | 5 | **15** |
| Website photos | 0 | 0 | 8 | 1 | 9 | 3 | 1 | **22** |
| iPhone photos | 0 | 3 | 145 | 78 | 123 | 50 | 54 | **453** |
| Android photos | 0 | 0 | 0 | 0 | 0 | 0 | 27 | **27** |
| Tree notes | 0 | 1 | 15 | 23 | 11 | 15 | 6 | **71** |
| App Store reviews | 0 | 0 | 4 | 2 | 1 | 0 | 0 | **7** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.
- App deletions count only phones that share analytics with developers, and Apple leaves out days too small to show: read it against the installs of the same day, not as a total.

**Feedback by kind** (the Feedback row above, split; their words are in the readers-in-full block)

| Kind | 11-19 | **7 days** |
|---|---:|---:|
| Pin moved | 4 | **51** |
| Written feedback | 8 | **53** |
| Report on a tree | 6 | **24** |
| Collected far from our pin | 0 | **1** |

**Trees readers sent, for you to inspect** (105 you have not looked at; ours left out)

| Judged | Reader | Tree | Where | Species | Their girth | Our verdict | Page |
|---|---|---|---|---|---:|---|---|
| 2026-11-20 | ? | 42F66634-36D7-46DF-8A02-739114680321 | Tokyo | - | - | lead | - |
| 2026-11-19 | A | The Maples of Hugo Conwentz | Gdansk | Field Maple (Acer campestre) | - | hold | - |
| 2026-11-19 | A | The Ivy Elm of Park Oliwski (2 photos) | Gdansk | European White Elm (Ulmus laev | - | hold | - |
| 2026-11-19 | B | Dragon Tree in Madeira | - | Dragon Tree | - | hold | - |
| 2026-11-19 | C | The Cut-Leaved Alder | York | Common Alder (Alnus glutinosa  | - | hold | - |
| 2026-11-19 | C | The Pear-Barked Beech | York | European Beech (Fagus sylvatic | - | hold | - |
| 2026-11-19 | D | A tree I found (7 photos) | - | - | - | hold | - |
| 2026-11-19 | E | Fig | - | Fig | - | hold | - |
| 2026-11-19 | F | The Amur Cork Trees and Crimean Linden of Be (2 photos) | Vilnius | Amur Cork Tree (Phellodendron  | - | hold | - |
| 2026-11-19 | F | - | Vilnius | - | - | hold | - |
| 2026-11-19 | F | The Sapiegos Park Linden | Vilnius | Small-leaved Lime (Tilia corda | - | hold | - |
| 2026-11-19 | F | - | Vilnius | - | - | hold | - |
| 2026-11-19 | G | Hills Fig in Zetland | Sydney | - | 1000 cm | hold | - |
| 2026-11-18 | H | The Sprawling Sycamore of Pawling Farm | Valley Forge | American Sycamore (Platanus oc | - | hold | - |
| 2026-11-18 | I | The Remnant River Red Gum of Edinburgh Garde (4 photos) | Melbourne | River Red Gum (Eucalyptus cama | - | hold | - |
| 2026-11-18 | I | The Southern Mahogany of Edinburgh Gardens (2 photos) | Melbourne | Southern Mahogany (Eucalyptus  | - | hold | - |
| 2026-11-18 | I | - | Melbourne | - | - | hold | - |
| 2026-11-18 | J | The Bidwill Kauri Pine | Sydney | Queensland Kauri (Agathis robu | - | hold | - |
| 2026-11-18 | I | The Holm Oak of Darling Gardens | Melbourne | Holm Oak (Quercus ilex) | - | hold | - |
| 2026-11-18 | K | The Knotted Tree of Mexikópuszta | Fertőújlak | Japanese Pagoda Tree or Black  | - | hold | - |
| 2026-11-18 | ? | The Casuarina of the Cascada (2 photos) | Barcelona | River She-oak (Casuarina cunni | - | hold | - |
| 2026-11-18 | L | Ancient Cedar at Makata Jinjya | - | Japanese Cedar | 800 cm | hold | - |
| 2026-11-18 | M | Bur Oak | - | Bur Oak | 323 cm | hold | - |
| 2026-11-17 | N | - | - | - | - | hold | - |
| 2026-11-17 | ? | - | - | - | - | hold | - |
| 2026-11-17 | N | - | - | - | - | hold | - |
| 2026-11-17 | N | - | - | - | - | hold | - |
| 2026-11-17 | O | - | - | - | - | hold | - |
| 2026-11-17 | O | - | - | - | - | hold | - |
| 2026-11-17 | P | A tree in Los Angeles | - | - | - | hold | - |
| 2026-11-17 | Q | A tree near Copenhagen | - | - | - | hold | - |
| 2026-11-17 | R | Blue Jacaranda in ISA | - | Blue Jacaranda | - | hold | - |
| 2026-11-17 | R | Judas Tree in ISA | - | Judas Tree | - | hold | - |
| 2026-11-17 | J | Queensland Kauri in Sydney | - | Queensland Kauri | - | hold | - |
| 2026-11-17 | S | Pecan | - | Pecan | - | hold | - |
| 2026-11-17 | T | Ahuehuete del Jardin de San Fernando (2 photos) | Mexico City | - | - | hold | - |
| 2026-11-17 | S | Pecan | Griffin | Pecan | - | lead | - |
| 2026-11-17 | U | The Cosgrove House Banyan (2 photos) | Key West | Fig (Ficus sp.) | - | hold | - |
| 2026-11-17 | U | Jindai-zakura (Yamataka Jindai Zakura) | Hokuto | Higan Cherry (Prunus subhirtel | - | hold | - |
| 2026-11-17 | V | Black Mulberry in London | - | Black Mulberry | 250 cm | hold | - |
| 2026-11-17 | W | The Finsbury Circus Pagoda Tree | London | Japanese Pagoda Tree (Styphnol | - | hold | - |
| 2026-11-17 | X | Le Chêne de la Vierge | - | Oak | 250 cm | hold | - |
| 2026-11-17 | Y | The Moreton Bay Fig of Curtain Square | - | - | - | hold | - |
| 2026-11-17 | W | A London plane in Finsbury Circus Gardens | - | London Plane (Platanus x aceri | - | hold | - |
| 2026-11-17 | Z | A dead sweet chestnut in the Kastanologos fo | - | Sweet Chestnut (Castanea sativ | - | hold | - |
| 2026-11-17 | A1 | The Totteridge Yew | London | European Yew (Taxus baccata) | - | hold | - |
| 2026-11-17 | B1 | Queen Elizabeth’s Oak in Greenwich Park | - | Pedunculate Oak | - | hold | - |
| 2026-11-17 | C1 | - | - | - | - | hold | - |
| 2026-11-17 | D1 | - | - | - | - | hold | - |
| 2026-11-17 | E1 | - | - | - | - | hold | - |
| 2026-11-17 | F1 | - (2 photos) | - | - | - | hold | - |
| 2026-11-17 | ? | Romantik-Eiche | Heidelberg | - | - | lead | - |
| 2026-11-17 | ? | Bergmammutbaum im Arboretum 1 | Heidelberg | - | 765 cm | lead | - |
| 2026-11-17 | ? | Holdermanns-Eiche | Heidelberg | - | - | lead | - |
| 2026-11-17 | ? | Banyan Tree | Ho Chi Minh City | - | - | lead | - |
| 2026-11-17 | ? | It is a specimen of the species Fitzroya cup | La Unión, Chile | - | 420 cm | lead | - |
| 2026-11-17 | G1 | - | Azores | - | - | hold | - |
| 2026-11-17 | H1 | Ekebyhovseken | Ekerö | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-17 | I1 | Orange | - | Orange (Citrus sinensis) | - | hold | - |
| 2026-11-17 | ? | BB61E294-5FFB-4378-960A-64DAB336FD46 | - | - | - | hold | - |
| 2026-11-17 | ? | CAA9C183-3017-433B-A1CA-09E1CAA99BF3 | - | - | - | hold | - |
| 2026-11-17 | ? | The Signal Tree (Native American'Indian Sign | Akron, Ohio, USA | - | 122 cm | lead | - |
| 2026-11-16 | J1 | American Elm | - | American Elm | - | hold | - |
| 2026-11-16 | J1 | Eastern Cottonwood (2 photos) | - | Eastern Cottonwood | - | hold | - |
| 2026-11-16 | J1 | White Oak | - | White Oak | - | hold | - |
| 2026-11-16 | J1 | Northern Red Oak | - | Northern Red Oak | - | hold | - |
| 2026-11-16 | K1 | Linden tree next to the pond | - | Lime (Tilia sp.) | 166 cm | hold | - |
| 2026-11-16 | L1 | Prince Eugen's Oak | - | Oak (Quercus sp.) | - | hold | - |
| 2026-11-16 | M1 | A tree near Helmond | - | - | - | hold | - |
| 2026-11-16 | N1 | - | - | ridged furrowed bark, spreadin | - | hold | - |
| 2026-11-16 | O1 | A tree near Westonbirt Arboretum | - | - | - | hold | - |
| 2026-11-16 | ? | Cat Island Bald Cypress | St Francis ville, LA | - | 1650 cm | lead | - |
| 2026-11-16 | ? | The 180-year-old Moreton Bay Fig at Arderne  | Cape Town | - | 1120 cm | lead | - |
| 2026-11-16 | ? | The 800-year-old Big Tree in Tsitsikamma | Stormsrivier, the Garden Route, South Africa | - | 900 cm | lead | - |
| 2026-11-16 | ? | The Famous Nossob Camel Thorn Tree | Kgalagadi Transfrontier Park | - | - | lead | - |
| 2026-11-16 | ? | Chestnut "Miraglia" | Camaldoli (Ar) - Italy | - | 2000 cm | lead | - |
| 2026-11-15 | P1 | Endangered Dawn Redwood in Holborn, legal di | - | Dawn Redwood | - | hold | - |
| 2026-11-15 | G1 | Giant Australian Rubber Tree of Jardim Anton | Azores | Moreton Bay Fig (Ficus macroph | - | hold | - |
| 2026-11-15 | Q1 | Deans Oak | - | - | 1200 cm | hold | - |
| 2026-11-15 | R1 | Scots Pine in Dunkeld | - | Scots Pine | 660 cm | hold | - |
| 2026-11-15 | S1 | Tree in Waitangi | - | - | - | hold | - |
| 2026-11-15 | F1 | - | - | - | - | hold | - |
| 2026-11-15 | T1 | - | - | - | - | hold | - |
| 2026-11-15 | U1 | - | - | - | - | hold | - |
| 2026-11-15 | U1 | - | - | - | - | hold | - |
| 2026-11-15 | U1 | - | - | - | - | hold | - |
| 2026-11-15 | V1 | - | - | - | - | hold | - |
| 2026-11-15 | W1 | The Witch Tree of Fanal | Madeira | Til / Stinkwood (Ocotea foeten | - | hold | - |
| 2026-11-15 | X1 | Marton Oak | - | Pedunculate Oak | - | hold | - |
| 2026-11-15 | Y1 | Malmö | - | - | - | hold | - |
| 2026-11-15 | Z1 | Blue Jacaranda in Melbourne | - | Blue Jacaranda | - | hold | - |
| 2026-11-15 | A2 | English Hawthorn | - | English Hawthorn (Crataegus la | 50 cm | lead | - |
| 2026-11-15 | B2 | Wistman's Wood | Dartmoor | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-15 | C2 | Grimston's Oak | London | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-15 | B2 | The Crom Yews | Crom | European Yew (Taxus baccata) | - | hold | - |
| 2026-11-15 | B2 | The Dawn Redwood by the Kelvin Statue (2 photos) | Belfast | Dawn Redwood (Metasequoia glyp | - | hold | - |
| 2026-11-15 | B2 | S'Olivera de Cort | Palma de Mallorca | Olive (Olea europaea) | - | hold | - |
| 2026-11-15 | D2 | A tree near Chiang Mai | - | - | - | hold | - |
| 2026-11-15 | E2 | Il cipresso calvo di Villa Smeraldi | - | Cypress (Cupressus sp.) | - | hold | - |
| 2026-11-15 | B2 | The Boole Library Redwoods | Cork | Redwood | - | hold | - |
| 2026-11-15 | ? | Oak tree, Quercus Robur. | Bagni di Lusnizza, Udine | - | 454 cm | lead | - |
| 2026-11-15 | ? | Oliveira de Mouchão, oldest olive tree in Po | Mouriscas | - | - | lead | - |
| 2026-11-15 | ? | 71F93157-AEF9-41A4-AF61-E1AD9755F9B1 | - | - | - | hold | - |
| 2026-11-15 | ? | 24FDCCB3-A454-4556-8169-2BAD2FB36ABD | - | - | - | hold | - |
| 2026-11-15 | ? | C7962FE1-14DB-407A-B62F-CFA617580655 | - | - | - | hold | - |
- From 57 readers: reader B2 5, reader F 4, reader I 4, reader J1 4, reader N 3, reader U1 3, reader A 2, reader C 2, reader F1 2, reader G1 2, reader J 2, reader O 2, reader R 2, reader S 2, reader U 2, reader W 2, reader A1 1, reader A2 1, reader B 1, reader B1 1, reader C1 1, reader C2 1, reader D 1, reader D1 1, reader D2 1, reader E 1, reader E1 1, reader E2 1, reader G 1, reader H 1, reader H1 1, reader I1 1, reader K 1, reader K1 1, reader L 1, reader L1 1, reader M 1, reader M1 1, reader N1 1, reader O1 1, reader P 1, reader P1 1, reader Q 1, reader Q1 1, reader R1 1, reader S1 1, reader T 1, reader T1 1, reader V 1, reader V1 1, reader W1 1, reader X 1, reader X1 1, reader Y 1, reader Y1 1, reader Z 1, reader Z1 1.
- Photographs and the readers' own words: `python3 scripts/inspect_readers.py` (a local page, never in this public file). Your answer goes in with `python3 scripts/judgement.py --feedback <id> "..."`.

**Waiting for you** (what the runs left for you since 2026-11-19)

- 229 email addresses ready to mail (archive 0, nature 9, guide 4, press 122, source 58, council 16, society 7, tourism 5, other 5, garden 3); **the night run found no new contacts in two days**
- the daily task "publish-held-trees-daily" can be switched off under Scheduled; write passes put trees straight into the app, so nothing waits for it.
- 31 people since the Guardian day asked for a sign-in link and never got in** (25 new accounts from 15 and 16 November, 11 of them Yahoo/Apple/BT; 6 existing accounts).
- the La Tène reader wants to be ambassador and the commune named Laténa; see the draft.
- a Gmail filter "To: info@ancienttrees.app → Never send it to Spam" stops this at the source.

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-18 | F2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | J1 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | K |  | ? | a reader's photograph, published | not live yet |
| 11-18 | D2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | G2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | H2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | I2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | J2 | The Camperdown Cemetery Fig | Sydney | a reader's photograph, published | [live](https://ancienttrees.app/sydney/camperdown-cemetery-fig) |
| 11-18 | H | The Sprawling Sycamore of Pawling Farm | Valley Forge | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/valley-forge/sprawling-sycamore-of-pawling-farm) |
| 11-18 | I | The Remnant River Red Gum of Edinburgh Gardens | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/remnant-river-red-gum-of-edinburgh-gardens) |
| 11-18 | I | The Remnant River Red Gum of Edinburgh Gardens | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/remnant-river-red-gum-of-edinburgh-gardens) |
| 11-18 | I | The Finer Holm Oak of Edinburgh Gardens | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/finer-holm-oak-of-edinburgh-gardens) |
| 11-18 | K2 | The Shiba Toshogu Ginkgo | Tokyo | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tokyo/shiba-toshogu-ginkgo) |
| 11-18 | L2 | The north door yews of St Edward's, Stow-on-the-Wold | Stow-on-the-Wold | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/stow-on-the-wold/north-door-yews-of-st-edwards-stow-on-the-wold) |
| 11-18 | M2 | The Inner Temple Mulberry | London | a reader's photograph, published | [live](https://ancienttrees.app/london/inner-temple-mulberry) |
| 11-18 | N2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | O2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | P2 | The Ueno Toshogu Camphor | Tokyo | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tokyo/ueno-toshogu-camphor) |
| 11-18 | L |  | ? | a reader's photograph, published | not live yet |
| 11-18 | Q2 | The Casuarina of the Cascada | Barcelona | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/barcelona/casuarina-of-the-cascada) |
| 11-18 | R2 | The Leidsebosje Planes | Amsterdam | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/amsterdam/leidsebosje-planes) |
| 11-18 | S2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | N2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | N2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | N2 | The Great Oriental Plane of Emmanuel College | Cambridge | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/cambridge/great-oriental-plane-of-emmanuel-college) |
| 11-18 | T2 | The English Elm of Fort Greene Park | New York | a reader's photograph, published | [live](https://ancienttrees.app/new-york/english-elm-of-fort-greene-park) |
| 11-18 | U2 | Chêne de la Vierge à Viroflay | Viroflay | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/viroflay/chene-de-la-vierge-a-viroflay) |
| 11-18 | U2 | Chêne de la Vierge à Viroflay | Viroflay | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/viroflay/chene-de-la-vierge-a-viroflay) |
| 11-18 | T | The Temple Square Cedar of Lebanon | Salt Lake City | a reader's photograph, published | [live](https://ancienttrees.app/salt-lake-city/temple-square-cedar-of-lebanon) |
| 11-18 | T | The Washington Square Ohio Buckeye | Salt Lake City | a reader's photograph, published | [live](https://ancienttrees.app/salt-lake-city/washington-square-ohio-buckeye) |
| 11-18 | T | The Washington Square Hackberry | Salt Lake City | a reader's photograph, published | [live](https://ancienttrees.app/salt-lake-city/washington-square-hackberry) |
| 11-18 | T | The Liberty Park London Planetree | Salt Lake City | a reader's photograph, published | [live](https://ancienttrees.app/salt-lake-city/liberty-park-london-planetree) |
| 11-18 | T | Jardine Juniper | Logan Canyon | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/logan-canyon/jardine-juniper) |
| 11-18 | V2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | V2 | El Árbol del Tule | Santa María del Tule | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/santa-maria-del-tule/el-arbol-del-tule) |
| 11-18 | T | The Fortingall Yew | Fortingall | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/fortingall/fortingall-yew) |
| 11-18 | T | Dughall Mor and the Reelig Glen giants | Reelig Glen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/reelig-glen/dughall-mor-and-the-reelig-glen-giants) |
| 11-18 | W2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | X2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | Y2 | The Copper Beech of the Antonius Abtkerk | Nijmegen | a reader's photograph, published | [live](https://ancienttrees.app/nijmegen/copper-beech-of-the-antonius-abtkerk) |
| 11-18 | Y2 | The Copper Beech of the Antonius Abtkerk | Nijmegen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/nijmegen/copper-beech-of-the-antonius-abtkerk) |
| 11-18 | Y2 | The Copper Beech of the Antonius Abtkerk | Nijmegen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/nijmegen/copper-beech-of-the-antonius-abtkerk) |
| 11-18 | Z2 | The Ada Tree | Powelltown | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/powelltown/ada-tree) |
| 11-19 | X2 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | A3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | B3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | B3 | The Kapok Tree | Key West | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/key-west/kapok-tree) |
| 11-19 | B3 | The Cosgrove House Banyan | Key West | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/key-west/cosgrove-house-banyan) |
| 11-19 | B3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | B3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | B3 | Grandfather Pine at Serenbe | Serenbe | a reader's photograph, published | [live](https://ancienttrees.app/serenbe/grandfather-pine-at-serenbe) |
| 11-19 | B3 | Grandmother Beech at Serenbe | Serenbe | a reader's photograph, published | [live](https://ancienttrees.app/serenbe/grandmother-beech-at-serenbe) |
| 11-19 | B3 | The McDonogh Oak | New Orleans | a reader's photograph, published | [live](https://ancienttrees.app/new-orleans/mcdonogh-oak) |
| 11-19 | B3 | The Anseman Oak | New Orleans | a reader's photograph, published | [live](https://ancienttrees.app/new-orleans/anseman-oak) |
| 11-19 | B3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | B3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | B3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | B3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | B3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | B3 | The Moreton Bay Fig of Balboa Park | San Diego | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/san-diego/moreton-bay-fig-of-balboa-park) |
| 11-19 | A | The Maples of Hugo Conwentz | Gdansk | a reader's photograph, published | [live](https://ancienttrees.app/gdansk/maples-of-hugo-conwentz) |
| 11-19 | C3 | The Leaning Fig over the Boardwalk | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/leaning-fig-over-the-boardwalk) |
| 11-19 | C3 | The Leaning Fig over the Boardwalk | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/leaning-fig-over-the-boardwalk) |
| 11-19 | B |  | ? | a reader's photograph, published | not live yet |
| 11-19 | A | The Cucumber Magnolia of Park Oliwski | Gdansk | a reader's photograph, published | [live](https://ancienttrees.app/gdansk/cucumber-magnolia-of-park-oliwski) |
| 11-19 | A | The Cucumber Magnolia of Park Oliwski | Gdansk | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/gdansk/cucumber-magnolia-of-park-oliwski) |
| 11-19 | A | The Giant Thuja of Park Oliwski | Gdansk | a reader's photograph, published | [live](https://ancienttrees.app/gdansk/giant-thuja-of-park-oliwski) |
| 11-19 | A | The Giant Thuja of Park Oliwski | Gdansk | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/gdansk/giant-thuja-of-park-oliwski) |
| 11-19 | A | The Three-Trunked Katsura of Park Oliwski | Gdansk | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/gdansk/three-trunked-katsura-of-park-oliwski) |
| 11-19 | I | The Finer Holm Oak of Edinburgh Gardens | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/finer-holm-oak-of-edinburgh-gardens) |
| 11-19 | I | The Finer Holm Oak of Edinburgh Gardens | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/finer-holm-oak-of-edinburgh-gardens) |
| 11-19 | I | The Gum by the Edinburgh Gardens Skate Bowl | Melbourne | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/melbourne/gum-by-the-edinburgh-gardens-skate-bowl) |
| 11-19 | D3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | D3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | D3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | D3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | D3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | D3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | E3 | The Giant Sequoias of the Tall Trees Trail | New Forest | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/new-forest/giant-sequoias-of-the-tall-trees-trail) |
| 11-19 | F3 | The Plane Tree of Place Antoine-Rivoire | Lyon | a reader's photograph, published | [live](https://ancienttrees.app/lyon/plane-tree-of-place-antoine-rivoire) |
| 11-19 | F3 | The Plane Tree of Place Antoine-Rivoire | Lyon | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/lyon/plane-tree-of-place-antoine-rivoire) |
| 11-19 | G3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | C | The Cut-Leaved Alder | York | a reader's photograph, published | [live](https://ancienttrees.app/york/cut-leaved-alder) |
| 11-19 | C | The Willow-Leaved Ash | York | a reader's photograph, published | [live](https://ancienttrees.app/york/willow-leaved-ash) |
| 11-19 | C | The Pear-Barked Beech | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/pear-barked-beech) |
| 11-19 | C | The Cut-Leaved Hornbeam | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/cut-leaved-hornbeam) |
| 11-19 | C | The Cut-Leaved Hornbeam | York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/york/cut-leaved-hornbeam) |
| 11-19 | H3 | The Cedar of Jussieu | Paris | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/paris/cedar-of-jussieu) |
| 11-19 | I3 | The Circus Ground Oak of Saratoga Park | New York | a reader's photograph, published | [live](https://ancienttrees.app/new-york/circus-ground-oak-of-saratoga-park) |
| 11-19 | I3 | The Ginkgo of the United Order of Tents | New York | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/new-york/ginkgo-of-the-united-order-of-tents) |
| 11-19 | J3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | V1 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | V1 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | K3 | The Sweet Chestnut of Hulsbeek | Geetbets | a reader's photograph, published | [live](https://ancienttrees.app/geetbets/sweet-chestnut-of-hulsbeek) |
| 11-19 | G | Grant Crescent Blue Gums | Canberra | a reader's photograph, published | [live](https://ancienttrees.app/canberra/grant-crescent-blue-gums) |
| 11-19 | L3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | M3 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | H | The Brandywine Sycamore (Lafayette Sycamore) | Chadds Ford | a reader's photograph, published | [live](https://ancienttrees.app/chadds-ford/brandywine-sycamore-lafayette-sycamore) |
| 11-19 | N3 | Old Albert | Auckland | a reader's photograph, published | [live](https://ancienttrees.app/auckland/old-albert) |
| 11-19 | N3 | Old Albert | Auckland | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/auckland/old-albert) |
| 11-20 | O3 | The Leaf-Seed Ginkgo of Inada Gobo | Kasama | a reader's photograph, published | [live](https://ancienttrees.app/kasama/leaf-seed-ginkgo-of-inada-gobo) |
| 11-20 | P3 | The banyan of Nhan Dan, 71 Hang Trong | Hanoi | a reader's photograph, published | [live](https://ancienttrees.app/hanoi/banyan-of-nhan-dan-71-hang-trong) |
| 11-18 | T2 | nyc_027 (The English Elm of Fort Greene Park) | New York | a reader's feedback changed the page | - |
| 11-19 | G | can_008 (Grant Crescent Blue Gums) | Canberra | a reader's correction changed the page | - |
| 11-20 | P3 | hni_003 (The banyan of Nhan Dan, 71 Hang Trong) | Hanoi | a reader's correction changed the page | - |
- From 49 readers: reader B3 15, reader T 7, reader A 6, reader D3 6, reader I 6, reader C 5, reader N2 4, reader Y2 3, reader C3 2, reader F3 2, reader G 2, reader H 2, reader I3 2, reader N3 2, reader P3 2, reader T2 2, reader U2 2, reader V1 2, reader V2 2, reader X2 2, reader A3 1, reader B 1, reader D2 1, reader E3 1, reader F2 1, reader G2 1, reader G3 1, reader H2 1, reader H3 1, reader I2 1, reader J1 1, reader J2 1, reader J3 1, reader K 1, reader K2 1, reader K3 1, reader L 1, reader L2 1, reader L3 1, reader M2 1, reader M3 1, reader O2 1, reader O3 1, reader P2 1, reader Q2 1, reader R2 1, reader S2 1, reader W2 1, reader Z2 1.

**What was sent in, and what we decided**

| seen | what | where | size for its species | ours | Hidde |
|---|---|---|---|---|---|
| 2026-11-19 | The Ivy Elm of Park Oliwski | Gdansk | - | hold | - |
| 2026-11-19 | The Amur Cork Trees and Crimean Linden | Vilnius | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | lead | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | A tree I found | - | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | The Southern Mahogany of Edinburgh Gar | Melbourne | - | hold | - |
| 2026-11-18 | The Casuarina of the Cascada | Barcelona | - | hold | - |
| 2026-11-18 | a tree we do not map | - | - | lead | - |
| 2026-11-17 | Ahuehuete del Jardin de San Fernando | Mexico City | - | hold | - |
| 2026-11-17 | The Cosgrove House Banyan | Key West | - | hold | - |
| 2026-11-17 | European Beech in Baarn | - | - | hold | - |
| 2026-11-17 | European Beech in Baarn | - | - | hold | - |
| 2026-11-17 | a tree we do not map | Baarn | - | hold | - |
| 2026-11-17 | A tree I found | - | - | hold | - |

0 waiting for a verdict. Disagree with one and the rule changes: `python3 scripts/judgement.py --feedback <id> "..."`, and `--learn` prints every verdict he has overruled.

**Searched yesterday:** edinburgh (4 times), dub (3 times), london (3 times), sydney (3 times), amsterdam (2 times), assisi (2 times), auckland (2 times), canberra (2 times), du (2 times), dublin (2 times), etchingham (2 times), exe (2 times), foligno (2 times), madrid (2 times), new orleans (2 times), silver (2 times), surre (2 times), adelaide, akron, antwer.

**App crashes** (last 7 days, store builds; MetricKit, a sample)

| Crashes | Kind | Build | Where | Phones | Last | Fix |
|---:|---|---|---|---:|---|---|
| 1 | crash | 1.0.4 (41) | (no AncientTrees frame) | 1 | 2026-11-15 | none |
| 1 | crash | 1.0.4 (41) | AncientTrees+0x2409a0 | 1 | 2026-11-16 | none |

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 11-10 | 8 | 196 | 4.1% | 13.0 |
| 11-11 | 1 | 16 | 6.2% | 22.1 |
| 11-12 | 1 | 28 | 3.6% | 31.4 |
| 11-13 | 1 | 32 | 3.1% | 55.0 |
| 11-14 | 0 | 51 | 0.0% | 57.5 |
| 11-15 | 210 | 363 | 57.9% | 8.2 |
| 11-16 | 116 | 204 | 56.9% | 6.6 |
| 11-17 | 59 | 132 | 44.7% | 15.0 |
| 11-18 | 33 | 67 | 49.3% | 17.8 |
| 11-19 *partial* | 18 | 46 | 39.1% | 28.9 |
| **window** | **447** | **1135** | **39.4%** | |
- Top queries (10d): ancient trees app (i456, p1); ancient tree app (i3, p1); ancient trees (i9, p43); android au (i1, p1); এই অ্যাপের লিংক দাও (i1, p2)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-13 | 125 | 5 | 4.0% |
| 11-14 | 103 | 6 | 5.8% |
| 11-15 | 132 | 13 | 9.8% |
| 11-16 | 211 | 15 | 7.1% |
| 11-17 | 170 | 6 | 3.5% |
| 11-18 | 177 | 9 | 5.1% |
| 11-19 | - | - | 0.0% |
| **7 days** | **918** | **54** | **5.9%** |
- Week before: 886 impressions, 42 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); platane du square des batignolles (c4/i2, p1); picture of the tree in helsinki city center that was preserved (c3/i2, p4); ancient trees app (c2/i8, p5); who planted the western red cedar tree in blarney ireland (c2/i8, p2); fig tree in square alicante (c2/i4, p4); cipresso calvo indro montanelli milano (c2/i2, p8); palma del cile (c2/i2, p6)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-19T09:45 | 8.7 | 0 | 6 | 0 | Madeira +1, Melbourne, Gdansk |
| 11-19T18:47 | 3.9 | 0 | 7 | 3 | - |
| 11-19T21:50 | 5.6 | 1 | 8 | 1 | Melbourne +1 |
| 11-20T01:36 | 13.9 | 7 | 10 | 1 | Fort Lauderdale +6, Miami +1 |
| **4 runs** | **32** | **8** | **31** | | |

- 2 of 4 produced no trees; 1 to 3 commands refused per run; last build that went live: 0h ago.

**What they made**

- Reader judge: the Okunitama Shrine keyaki tip (1294) recorded as a Tokyo lead
- Reader judge: the Nhan Dan banyan (hni_003) gets a reader's photograph and their pin
- Reader judge: the Inada Gobo ginkgo (kas_001) gets its first photograph, a reader's
- Night run: Sheffield claim released, wall recorded; log
- Log: Fort Lauderdale and Miami trees live; release claim
- Write pass: six Fort Lauderdale champions and the Deering black olive
- Night run: Birmingham and Miami verify passes, nothing publishable; log and costs
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- Reader judge: Old Albert (akl_001) gets its first photographs, a reader's
- Reader judge: Brandywine Sycamore's first photograph and access from a reader; Castleboro redwood live as cbo_001
- Reader judge: the Brandywine Sycamore gets its first photograph, a reader's
- Melbourne's intro, question and FAQ count its twentieth tree (mel_020)

**Reader photographs in a strip, live first, not yet looked at** (5)

| Day | Tree | Where | Undo |
|---|---|---|---|
| 11-18 | The Fortingall Yew | Fortingall | `sightings_publish.py --unstrip f2e99426-d46c-4a73-9ab9-25f92c7edf6a` |
| 11-19 | The Finer Holm Oak of Edinburgh Gardens | Melbourne | `sightings_publish.py --unstrip b6bb10c9-d418-4437-b701-1015e35e7f5f` |
| 11-18 | The Copper Beech of the Antonius Abtkerk | Nijmegen | `sightings_publish.py --unstrip 1d8d8c2e-a5ad-45d4-ba5f-72956149bc7c` |
| 11-18 | The Copper Beech of the Antonius Abtkerk | Nijmegen | `sightings_publish.py --unstrip e23fe779-5876-4cd3-9fab-c50f7e28dcda` |
| 11-18 | Dughall Mor and the Reelig Glen giants | Reelig Glen | `sightings_publish.py --unstrip 691e83b3-fa05-4961-a56f-9912db89c1ac` |

Machine: 5 chain attempts yesterday, 5 got real work time (~53 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c432/i656); /fr/lyon/arbre-le-plus-vieux (c2/i3); /app (c1/i22); /explore (c1/i15); /munich (c1/i6)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'android au' (i1, p1)
    - 'এই অ্যাপের লিংক দাও' (i1, p2)
    - 'angeloak' (i1, p99)
    - 'biggest chestnut' (i1, p78)
    - 'bunya tree' (i1, p98)

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 187 | 5 | 20 | 0.11 | 1 |
| Not yet rich | 321 | 9 | 17 | 0.05 | 0 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| monterey | 0 | 21 | 0.0% | 74.5 | 0.4% | lone cypress (i5, p89) |
| olympic-national-park | 0 | 15 | 0.0% | 40.2 | 0.4% | olympic national park trees (i1, p48) |
| london | 0 | 14 | 0.0% | 66.1 | 0.4% | flats to rent clerkenwell (i3, p89) |
| tenerife | 0 | 12 | 0.0% | 85.6 | 0.4% | drago tree tenerife (i2, p96) |

- Plus 255 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: singapore, lisbon, amsterdam, barcelona, seville, bath, berlin, rome.
**Sign-in mail sent again** (stuck an hour or more, `scripts/signin_watch.py`): 38 people in 7 days, 4 of them got in afterwards.

## 2026-11-18 (previous UTC day)

**Today: 61 android waitlist signups arrived yesterday (2010 total); 14 tree submissions and 35 feedback reports arrived yesterday (470 submissions of every kind in all); 62 accounts were opened yesterday (801 accounts in all).**

**North star: 227 people have uploaded a tree or photo of their own (+214 this week); 25 of them did it on more than one day (+21).**

**The numbers that matter** (this week against the week before; strangers only)

| Number | Why | This week | Week before |
|---|---|---:|---:|
| New website visitors | people | 2918 | 37 |
| ... of which from search | every search engine | 86 | 14 |
| ... from Google | Google's recovery | 65 | 10 |
| ... from Bing | Bing | 8 | 1 |
| Website visitors who came back | people who stay | 553 | 9 |
| App downloads (first-time) | people | 6202 | 22 |
| New accounts | people | 729 | 2 |
| Phones back within 30 days | people who stay | 6 of 12 | 3 of 15 |
| Trees saved to Want to go | intent | 429 | 1 |
| Trees collected | goal 1: stood at a tree | 342 | 2 |
| Readers' contributions | data: trees, photos, corrections | 555 | 3 |
| Worth-it votes | one tap, not a contribution | 142 | 0 |
| Shares (app and web) | word of mouth, since 10-30 | 272 | 2 |
| Visits from a shared link | what sharing brings | 100 | 0 |

Website visitors are Google Analytics' count, so only people who accepted the cookie bar; a visitor who comes back on another browser or device counts as new, and GA cannot leave our own visits out, so read the came-back row as a direction, not a count. The 30-day row is the phones that arrived five weeks ago, so it moves slowly.

**Quality**: Web red, iOS orange, Android grey, Backup red. Backup: Hidde's one-time setup in BACKUP_RESTORE.md.

| | Web | iOS | Android |
|---|---|---|---|
| Next version | red: deploy failure on main | orange: 1 compliance point(s) wait for Hidde (data/compliance.json) | grey: no checks wired yet |
| Live | orange: 1 new error type(s), first "TypeError: undefined is not an object (evaluating 'n.standar" in inline | green | grey: no checks wired yet |

**Plus question** (12 answers, 2 new; 4 asked to be told; 6 wrote an idea, read them with `python3 scripts/plus_answers.py`; up to two each)

| Choice | Picked by |
|---|---:|
| Something else | 5 |
| Download offline maps | 4 |
| A richer log of every tree you've collected | 4 |
| Recommended tree walks for a city trip | 2 |
| Seasonal alerts when trees are at their best | 2 |

**Open for you** (2; everything else handled and recorded, 43 feedback in all)

| What | Why it waits | Summary |
|---|---|---|
| feedback 1156 | your call | a short yes, probably to our ask to quote 'well worth a visit' on cam_011; confirm the draft went, then set quote_ok and the quote can go on the page |
| feedback 1232 | your call | Mail reply: declines the ambassador role, asks the standard height for girth; suggested answer in drafts |

Reader judge: 173 agent minutes yesterday, 377 in the last 7 days.

**Day by day, the last seven days** (strangers only; visitors are Google Analytics', so only people who accepted the cookie bar)

| | 11-12 | 11-13 | 11-14 | 11-15 | 11-16 | 11-17 | 11-18 | **7 days** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Visitors | 3 | 5 | 3 | 1797 | 734 | 297 | 169 | **3008** |
| New accounts | 1 | 0 | 2 | 370 | 197 | 97 | 62 | **729** |
| Saves | 0 | 0 | 0 | 189 | 143 | 39 | 58 | **429** |
| Android waitlist | 0 | 0 | 0 | 1317 | 416 | 158 | 61 | **1952** |
| App downloads | 2 | 2 | 1 | 3896 | 1588 | 712 | – | **6201** |
| App deletions | – | – | – | 11 | 16 | 14 | 10 | **51** |
| App phones | 6 | 5 | 8 | 3563 | 1692 | 950 | 622 | **5956** |
| Trees opened in the app | 3 | 4 | 18 | 7608 | 3264 | 1848 | 1103 | **13848** |
| Trees collected | 0 | 0 | 3 | 96 | 59 | 30 | 21 | **209** |
| Trees sent | 0 | 1 | 0 | 98 | 51 | 37 | 14 | **201** |
| Feedback | 0 | 0 | 0 | 29 | 23 | 15 | 42 | **109** |
| Worth-it votes | 0 | 0 | 0 | 62 | 44 | 20 | 16 | **142** |
| Ambassador asks | 0 | 0 | 0 | 5 | 3 | 2 | 0 | **10** |
| Website photos | 0 | 0 | 0 | 8 | 1 | 9 | 3 | **21** |
| iPhone photos | 0 | 0 | 3 | 146 | 83 | 125 | 50 | **407** |
| Android photos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Tree notes | 0 | 0 | 1 | 15 | 23 | 11 | 15 | **65** |
| App Store reviews | 0 | 0 | 0 | 4 | 2 | 1 | 0 | **7** |
- – means the source has not reported that day yet (Apple's downloads arrive a day or two late), not zero.
- App deletions count only phones that share analytics with developers, and Apple leaves out days too small to show: read it against the installs of the same day, not as a total.

**Feedback by kind** (the Feedback row above, split; their words are in the readers-in-full block)

| Kind | 11-18 | **7 days** |
|---|---:|---:|
| Pin moved | 5 | **47** |
| Written feedback | 36 | **46** |
| Report on a tree | 1 | **18** |
| Collected far from our pin | 0 | **1** |

**Trees readers sent, for you to inspect** (93 you have not looked at; ours left out)

| Judged | Reader | Tree | Where | Species | Their girth | Our verdict | Page |
|---|---|---|---|---|---:|---|---|
| 2026-11-18 | A | The Sprawling Sycamore of Pawling Farm | Valley Forge | American Sycamore (Platanus oc | - | hold | - |
| 2026-11-18 | B | The Remnant River Red Gum of Edinburgh Garde (4 photos) | Melbourne | River Red Gum (Eucalyptus cama | - | hold | - |
| 2026-11-18 | B | The Southern Mahogany of Edinburgh Gardens (2 photos) | Melbourne | Southern Mahogany (Eucalyptus  | - | hold | - |
| 2026-11-18 | C | A tree I found (6 photos) | - | - | - | hold | - |
| 2026-11-18 | B | - | Melbourne | - | - | hold | - |
| 2026-11-18 | D | The Bidwill Kauri Pine | Sydney | Queensland Kauri (Agathis robu | - | hold | - |
| 2026-11-18 | B | The Holm Oak of Darling Gardens | Melbourne | Holm Oak (Quercus ilex) | - | hold | - |
| 2026-11-18 | E | The Knotted Tree of Mexikópuszta | Fertőújlak | Japanese Pagoda Tree or Black  | - | hold | - |
| 2026-11-18 | ? | The Casuarina of the Cascada (2 photos) | Barcelona | River She-oak (Casuarina cunni | - | hold | - |
| 2026-11-18 | F | Ancient Cedar at Makata Jinjya | - | Japanese Cedar | 800 cm | hold | - |
| 2026-11-18 | G | Bur Oak | - | Bur Oak | 323 cm | hold | - |
| 2026-11-17 | H | - | - | - | - | hold | - |
| 2026-11-17 | ? | - | - | - | - | hold | - |
| 2026-11-17 | H | - | - | - | - | hold | - |
| 2026-11-17 | H | - | - | - | - | hold | - |
| 2026-11-17 | I | - | - | - | - | hold | - |
| 2026-11-17 | I | - | - | - | - | hold | - |
| 2026-11-17 | J | A tree in Los Angeles | - | - | - | hold | - |
| 2026-11-17 | K | A tree near Copenhagen | - | - | - | hold | - |
| 2026-11-17 | L | Blue Jacaranda in ISA | - | Blue Jacaranda | - | hold | - |
| 2026-11-17 | L | Judas Tree in ISA | - | Judas Tree | - | hold | - |
| 2026-11-17 | D | Queensland Kauri in Sydney | - | Queensland Kauri | - | hold | - |
| 2026-11-17 | M | Pecan | - | Pecan | - | hold | - |
| 2026-11-17 | N | Ahuehuete del Jardin de San Fernando (2 photos) | Mexico City | - | - | hold | - |
| 2026-11-17 | M | Pecan | Griffin | Pecan | - | lead | - |
| 2026-11-17 | O | The Cosgrove House Banyan (2 photos) | Key West | Fig (Ficus sp.) | - | hold | - |
| 2026-11-17 | O | Jindai-zakura (Yamataka Jindai Zakura) | Hokuto | Higan Cherry (Prunus subhirtel | - | hold | - |
| 2026-11-17 | P | Black Mulberry in London | - | Black Mulberry | 250 cm | hold | - |
| 2026-11-17 | Q | The Finsbury Circus Pagoda Tree | London | Japanese Pagoda Tree (Styphnol | - | hold | - |
| 2026-11-17 | R | Le Chêne de la Vierge | - | Oak | 250 cm | hold | - |
| 2026-11-17 | S | The Moreton Bay Fig of Curtain Square | - | - | - | hold | - |
| 2026-11-17 | Q | A London plane in Finsbury Circus Gardens | - | London Plane (Platanus x aceri | - | hold | - |
| 2026-11-17 | T | A dead sweet chestnut in the Kastanologos fo | - | Sweet Chestnut (Castanea sativ | - | hold | - |
| 2026-11-17 | U | The Totteridge Yew | London | European Yew (Taxus baccata) | - | hold | - |
| 2026-11-17 | V | Queen Elizabeth’s Oak in Greenwich Park | - | Pedunculate Oak | - | hold | - |
| 2026-11-17 | W | - | - | - | - | hold | - |
| 2026-11-17 | X | - | - | - | - | hold | - |
| 2026-11-17 | Y | - | - | - | - | hold | - |
| 2026-11-17 | Z | - (2 photos) | - | - | - | hold | - |
| 2026-11-17 | ? | Romantik-Eiche | Heidelberg | - | - | lead | - |
| 2026-11-17 | ? | Bergmammutbaum im Arboretum 1 | Heidelberg | - | 765 cm | lead | - |
| 2026-11-17 | ? | Holdermanns-Eiche | Heidelberg | - | - | lead | - |
| 2026-11-17 | ? | Banyan Tree | Ho Chi Minh City | - | - | lead | - |
| 2026-11-17 | ? | It is a specimen of the species Fitzroya cup | La Unión, Chile | - | 420 cm | lead | - |
| 2026-11-17 | A1 | - | Azores | - | - | hold | - |
| 2026-11-17 | B1 | Ekebyhovseken | Ekerö | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-17 | C1 | Orange | - | Orange (Citrus sinensis) | - | hold | - |
| 2026-11-17 | ? | BB61E294-5FFB-4378-960A-64DAB336FD46 | - | - | - | hold | - |
| 2026-11-17 | ? | CAA9C183-3017-433B-A1CA-09E1CAA99BF3 | - | - | - | hold | - |
| 2026-11-17 | ? | The Signal Tree (Native American'Indian Sign | Akron, Ohio, USA | - | 122 cm | lead | - |
| 2026-11-16 | D1 | American Elm | - | American Elm | - | hold | - |
| 2026-11-16 | D1 | Eastern Cottonwood (2 photos) | - | Eastern Cottonwood | - | hold | - |
| 2026-11-16 | D1 | White Oak | - | White Oak | - | hold | - |
| 2026-11-16 | D1 | Northern Red Oak | - | Northern Red Oak | - | hold | - |
| 2026-11-16 | E1 | Linden tree next to the pond | - | Lime (Tilia sp.) | 166 cm | hold | - |
| 2026-11-16 | F1 | Prince Eugen's Oak | - | Oak (Quercus sp.) | - | hold | - |
| 2026-11-16 | G1 | A tree near Helmond | - | - | - | hold | - |
| 2026-11-16 | H1 | - | - | ridged furrowed bark, spreadin | - | hold | - |
| 2026-11-16 | I1 | A tree near Westonbirt Arboretum | - | - | - | hold | - |
| 2026-11-16 | ? | Cat Island Bald Cypress | St Francis ville, LA | - | 1650 cm | lead | - |
| 2026-11-16 | ? | The 180-year-old Moreton Bay Fig at Arderne  | Cape Town | - | 1120 cm | lead | - |
| 2026-11-16 | ? | The 800-year-old Big Tree in Tsitsikamma | Stormsrivier, the Garden Route, South Africa | - | 900 cm | lead | - |
| 2026-11-16 | ? | The Famous Nossob Camel Thorn Tree | Kgalagadi Transfrontier Park | - | - | lead | - |
| 2026-11-16 | ? | Chestnut "Miraglia" | Camaldoli (Ar) - Italy | - | 2000 cm | lead | - |
| 2026-11-15 | J1 | Endangered Dawn Redwood in Holborn, legal di | - | Dawn Redwood | - | hold | - |
| 2026-11-15 | A1 | Giant Australian Rubber Tree of Jardim Anton | Azores | Moreton Bay Fig (Ficus macroph | - | hold | - |
| 2026-11-15 | K1 | Deans Oak | - | - | 1200 cm | hold | - |
| 2026-11-15 | L1 | Scots Pine in Dunkeld | - | Scots Pine | 660 cm | hold | - |
| 2026-11-15 | M1 | Tree in Waitangi | - | - | - | hold | - |
| 2026-11-15 | Z | - | - | - | - | hold | - |
| 2026-11-15 | N1 | - | - | - | - | hold | - |
| 2026-11-15 | O1 | - | - | - | - | hold | - |
| 2026-11-15 | O1 | - | - | - | - | hold | - |
| 2026-11-15 | O1 | - | - | - | - | hold | - |
| 2026-11-15 | P1 | - | - | - | - | hold | - |
| 2026-11-15 | Q1 | The Witch Tree of Fanal | Madeira | Til / Stinkwood (Ocotea foeten | - | hold | - |
| 2026-11-15 | R1 | Marton Oak | - | Pedunculate Oak | - | hold | - |
| 2026-11-15 | S1 | Malmö | - | - | - | hold | - |
| 2026-11-15 | T1 | Blue Jacaranda in Melbourne | - | Blue Jacaranda | - | hold | - |
| 2026-11-15 | U1 | English Hawthorn | - | English Hawthorn (Crataegus la | 50 cm | lead | - |
| 2026-11-15 | V1 | Wistman's Wood | Dartmoor | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-15 | W1 | Grimston's Oak | London | Pedunculate Oak (Quercus robur | - | hold | - |
| 2026-11-15 | V1 | The Crom Yews | Crom | European Yew (Taxus baccata) | - | hold | - |
| 2026-11-15 | V1 | The Dawn Redwood by the Kelvin Statue (2 photos) | Belfast | Dawn Redwood (Metasequoia glyp | - | hold | - |
| 2026-11-15 | V1 | S'Olivera de Cort | Palma de Mallorca | Olive (Olea europaea) | - | hold | - |
| 2026-11-15 | X1 | A tree near Chiang Mai | - | - | - | hold | - |
| 2026-11-15 | Y1 | Il cipresso calvo di Villa Smeraldi | - | Cypress (Cupressus sp.) | - | hold | - |
| 2026-11-15 | V1 | The Boole Library Redwoods | Cork | Redwood | - | hold | - |
| 2026-11-15 | ? | Oak tree, Quercus Robur. | Bagni di Lusnizza, Udine | - | 454 cm | lead | - |
| 2026-11-15 | ? | Oliveira de Mouchão, oldest olive tree in Po | Mouriscas | - | - | lead | - |
| 2026-11-15 | ? | 71F93157-AEF9-41A4-AF61-E1AD9755F9B1 | - | - | - | hold | - |
| 2026-11-15 | ? | 24FDCCB3-A454-4556-8169-2BAD2FB36ABD | - | - | - | hold | - |
| 2026-11-15 | ? | C7962FE1-14DB-407A-B62F-CFA617580655 | - | - | - | hold | - |
- From 51 readers: reader V1 5, reader B 4, reader D1 4, reader H 3, reader O1 3, reader A1 2, reader D 2, reader I 2, reader L 2, reader M 2, reader O 2, reader Q 2, reader Z 2, reader A 1, reader B1 1, reader C 1, reader C1 1, reader E 1, reader E1 1, reader F 1, reader F1 1, reader G 1, reader G1 1, reader H1 1, reader I1 1, reader J 1, reader J1 1, reader K 1, reader K1 1, reader L1 1, reader M1 1, reader N 1, reader N1 1, reader P 1, reader P1 1, reader Q1 1, reader R 1, reader R1 1, reader S 1, reader S1 1, reader T 1, reader T1 1, reader U 1, reader U1 1, reader V 1, reader W 1, reader W1 1, reader X 1, reader X1 1, reader Y 1, reader Y1 1.
- Photographs and the readers' own words: `python3 scripts/inspect_readers.py` (a local page, never in this public file). Your answer goes in with `python3 scripts/judgement.py --feedback <id> "..."`.

**Waiting for you** (what the runs left for you since 2026-11-18)

- 229 email addresses ready to mail (archive 0, nature 9, guide 4, press 122, source 58, council 16, society 7, tourism 5, other 5, garden 3); **the night run found no new contacts in two days**
- the reader stood at the trunk today, so if they answer that the area is open, the tree goes live with their photos.
- in the next TestFlight build and the Android build after 0.1.0 (2).
- send or bin).
- two collect-flow tips from two different readers today (1175, 1177, half an hour apart)
- open Xcode from ~/Developer/Ancienttrees/ios/AncientTrees/AncientTrees.xcodeproj from now on and start Claude sessions in ~/Developer/Ancienttrees.

**What readers gave us, and it went live**

| Day | Reader | Tree | Where | What | Page |
|---|---|---|---|---|---|
| 11-18 | Z1 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | D1 |  | ? | a reader's photograph, published | not live yet |
| 11-17 | A2 | The Dawn Redwood of Kew Gardens | Toronto | a reader's photograph, published | [live](https://ancienttrees.app/toronto/dawn-redwood-of-kew-gardens) |
| 11-18 | E |  | ? | a reader's photograph, published | not live yet |
| 11-17 | B2 | The Act of Union Beeches of North Berwick Law | North Berwick | a reader's photograph, published | [live](https://ancienttrees.app/north-berwick/act-of-union-beeches-of-north-berwick-law) |
| 11-18 | X1 |  | ? | a reader's photograph, published | not live yet |
| 11-17 | X1 | The Hollow Lime of Pabaži | Saulkrasti | a reader's photograph, published | [live](https://ancienttrees.app/saulkrasti/hollow-lime-of-pabazi) |
| 11-17 | X1 | The Great Ash of the Bison's Rib Trail | Białowieża | a reader's photograph, published | [live](https://ancienttrees.app/bialowieza/great-ash-of-the-bisons-rib-trail) |
| 11-17 | F | The Temple Ginkgo of Dujiangyan | Dujiangyan | a reader's photograph, published | [live](https://ancienttrees.app/dujiangyan/temple-ginkgo-of-dujiangyan) |
| 11-17 | C2 | The Leaning Black Poplar of Hancocks Lane | Castlemorton | a reader's photograph, published | [live](https://ancienttrees.app/castlemorton/leaning-black-poplar-of-hancocks-lane) |
| 11-17 | D2 | The Open-Grown Oak of Jelašnica | Jelašnica | a reader's photograph, published | [live](https://ancienttrees.app/jelasnica/open-grown-oak-of-jelasnica) |
| 11-18 | E2 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | F2 |  | ? | a reader's photograph, published | not live yet |
| 11-17 | G2 | The Ada Tree | Powelltown | a reader's photograph, published | [live](https://ancienttrees.app/powelltown/ada-tree) |
| 11-17 | R1 | The Giant Tree | Humboldt Redwoods State Park | a reader's photograph, published | [live](https://ancienttrees.app/humboldt-redwoods-state-park/giant-tree) |
| 11-17 | H2 | The Ginkgo of the United Order of Tents | New York | a reader's photograph, published | [live](https://ancienttrees.app/new-york/ginkgo-of-the-united-order-of-tents) |
| 11-17 | E2 | The Cedar of Lebanon at Blaise Castle | Bristol | a reader's photograph, published | [live](https://ancienttrees.app/bristol/cedar-of-lebanon-at-blaise-castle) |
| 11-17 | I2 | The Moreton Bay Fig of Parque Marechal Carmona | Cascais | a reader's photograph, published | [live](https://ancienttrees.app/cascais/moreton-bay-fig-of-parque-marechal-carmona) |
| 11-17 | J2 | The Pepper Tree That Mended Nets | Setubal | a reader's photograph, published | [live](https://ancienttrees.app/setubal/pepper-tree-that-mended-nets) |
| 11-17 | H | The Huntington Rose Garden Kauri | Los Angeles | a reader's photograph, published | [live](https://ancienttrees.app/los-angeles/huntington-rose-garden-kauri) |
| 11-17 | D | The Wishing Tree | Sydney | a reader's photograph, published | [live](https://ancienttrees.app/sydney/wishing-tree) |
| 11-17 | J2 | The Peruvian Pepper of the Jardim de Palhais | Setubal | a reader's photograph, published | [live](https://ancienttrees.app/setubal/peruvian-pepper-of-the-jardim-de-palhais) |
| 11-17 | K2 | Roath Park Lake Pedunculate Oak | Cardiff | a reader's photograph, published | [live](https://ancienttrees.app/cardiff/roath-park-lake-pedunculate-oak) |
| 11-17 | L2 | The Grand Ginkgo of Goo Shrine | Kyoto | a reader's photograph, published | [live](https://ancienttrees.app/kyoto/grand-ginkgo-of-goo-shrine) |
| 11-17 | L2 | The Grand Ginkgo of Goo Shrine | Kyoto | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kyoto/grand-ginkgo-of-goo-shrine) |
| 11-17 | M2 | Old Knobbley | Mistley | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/mistley/old-knobbley) |
| 11-17 | N2 | Benmore Redwood Avenue | Benmore | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/benmore/benmore-redwood-avenue) |
| 11-17 | J2 | Benmore Redwood Avenue | Benmore | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/benmore/benmore-redwood-avenue) |
| 11-17 | O2 | Boab Prison Tree | Derby | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/derby/boab-prison-tree) |
| 11-17 | I | The Sisi-Platane of Volksgarten | Vienna | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/vienna/sisi-platane-of-volksgarten) |
| 11-17 | I | The Sisi-Platane of Volksgarten | Vienna | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/vienna/sisi-platane-of-volksgarten) |
| 11-17 | P2 | The Cantonspark Giant Sequoia | Baarn | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/baarn/cantonspark-giant-sequoia) |
| 11-17 | G2 | Chief Sequoyah Tree | Sequoia National Park | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sequoia-national-park/chief-sequoyah-tree) |
| 11-17 | Q2 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 11-17 | Q2 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 11-17 | Q2 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/aguas-de-moura/whistler-cork-oak-sobreiro-assobiador) |
| 11-17 | Y1 | The Oak of Molinazzo | Poggio Renatico | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/poggio-renatico/oak-of-molinazzo) |
| 11-17 | R2 | Bleeding Yew of Nevern | Nevern | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/nevern/bleeding-yew-of-nevern) |
| 11-17 | S2 | The Bald Cypresses of the Crystal Palace Pond | Madrid | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/madrid/bald-cypresses-of-the-crystal-palace-pond) |
| 11-17 | T2 | Trolleken (the Troll Oak of Trollskogen) | Trollskogen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/trollskogen/trolleken-the-troll-oak-of-trollskogen) |
| 11-17 | T2 | S'Olivera de Cort | Palma de Mallorca | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/palma-de-mallorca/solivera-de-cort) |
| 11-17 | L2 | The Land Boat Pine | Kyoto | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/kyoto/land-boat-pine) |
| 11-17 | U2 | The Ombu of the Essaouira Medina | Essaouira | a reader's photograph, published | [live](https://ancienttrees.app/essaouira/ombu-of-the-essaouira-medina) |
| 11-17 | V2 | The Norfolk Island Pine of Ingle Hall | Hobart | a reader's photograph, published | [live](https://ancienttrees.app/hobart/norfolk-island-pine-of-ingle-hall) |
| 11-17 | V2 | The Bhutan Cypress of Brisbane Street | Hobart | a reader's photograph, published | [live](https://ancienttrees.app/hobart/bhutan-cypress-of-brisbane-street) |
| 11-17 | V2 | The Dawn Redwoods of Elizabeth Street | Hobart | a reader's photograph, published | [live](https://ancienttrees.app/hobart/dawn-redwoods-of-elizabeth-street) |
| 11-17 | W2 | The Big Totara of Lillburn Monowai Road | Tuatapere | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tuatapere/big-totara-of-lillburn-monowai-road) |
| 11-17 | D | The Wishing Tree | Sydney | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sydney/wishing-tree) |
| 11-17 | D | The Wishing Tree | Sydney | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/sydney/wishing-tree) |
| 11-17 | M | The Big Oak | Thomasville | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/thomasville/big-oak) |
| 11-17 | M | The Big Oak | Thomasville | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/thomasville/big-oak) |
| 11-17 | N | The Moreton Bay Fig of Balboa Park | San Diego | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/san-diego/moreton-bay-fig-of-balboa-park) |
| 11-17 | X2 | The Gomero de la Recoleta | Buenos Aires | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/buenos-aires/gomero-de-la-recoleta) |
| 11-17 | M | The Angel Oak | Charleston | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/charleston/angel-oak) |
| 11-17 | Y2 | The Orroroo Giant Gum | Orroroo | a reader's photograph, published | [live](https://ancienttrees.app/orroroo/orroroo-giant-gum) |
| 11-17 | X2 | Te Waha o Rerekohu | Te Araroa | a reader's photograph, published | [live](https://ancienttrees.app/te-araroa/te-waha-o-rerekohu) |
| 11-17 | M | The Old Lime of Estavayer-le-Lac | Estavayer-le-Lac | a reader's photograph, published | [live](https://ancienttrees.app/estavayer-le-lac/old-lime-of-estavayer-le-lac) |
| 11-17 | M | The Gennett Poplar | Chattahoochee National Forest | a reader's photograph, published | [live](https://ancienttrees.app/chattahoochee-national-forest/gennett-poplar) |
| 11-17 | M | The Knightwood Oak | New Forest | a reader's photograph, published | [live](https://ancienttrees.app/new-forest/knightwood-oak) |
| 11-17 | M | A Cedar of the Meares Island Big Tree Trail | Meares Island | a reader's photograph, published | [live](https://ancienttrees.app/meares-island/a-cedar-of-the-meares-island-big-tree-trail) |
| 11-17 | Z2 | The Red Gum of Overbury Drive | Adelaide | a reader's photograph, published | [live](https://ancienttrees.app/adelaide/red-gum-of-overbury-drive) |
| 11-17 | M | The Giant Sequoias of the Tall Trees Trail | New Forest | a reader's photograph, published | [live](https://ancienttrees.app/new-forest/giant-sequoias-of-the-tall-trees-trail) |
| 11-17 | A3 | The Great Ginkgo of Hida Kokubunji | Takayama | a reader's photograph, published | [live](https://ancienttrees.app/takayama/great-ginkgo-of-hida-kokubunji) |
| 11-17 | B3 | The Churchyard Yew of Cusop | Cusop | a reader's photograph, published | [live](https://ancienttrees.app/cusop/churchyard-yew-of-cusop) |
| 11-17 | H | The Moreton Bay Fig by the White Mansion | Los Angeles | a reader's photograph, published | [live](https://ancienttrees.app/los-angeles/moreton-bay-fig-by-the-white-mansion) |
| 11-17 | C3 | The Elephant-Trunk Fig of Tilarán | Tilarán | a reader's photograph, published | [live](https://ancienttrees.app/tilaran/elephant-trunk-fig-of-tilaran) |
| 11-17 | C3 | The Figs Saved by a Wall | Tilarán | a reader's photograph, published | [live](https://ancienttrees.app/tilaran/figs-saved-by-a-wall) |
| 11-17 | L | The Portuguese Oak of the Agronomy Cloister | Lisbon | a reader's photograph, published | [live](https://ancienttrees.app/lisbon/portuguese-oak-of-the-agronomy-cloister) |
| 11-17 | D3 | The Water Gum that Reaches Out | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/water-gum-that-reaches-out) |
| 11-17 | D3 | The Leaning Fig over the Boardwalk | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/leaning-fig-over-the-boardwalk) |
| 11-17 | E3 | The Gomero of Plaza San Martín | Buenos Aires | a reader's photograph, published | [live](https://ancienttrees.app/buenos-aires/gomero-of-plaza-san-martin) |
| 11-17 | O | The Cosgrove House Banyan | Key West | a reader's photograph, published | [live](https://ancienttrees.app/key-west/cosgrove-house-banyan) |
| 11-17 | O | Jindai-zakura (Yamataka Jindai Zakura) | Hokuto | a reader's photograph, published | [live](https://ancienttrees.app/hokuto/jindai-zakura-yamataka-jindai-zakura) |
| 11-17 | P | The Lewisham Elm | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/lewisham-elm) |
| 11-17 | F3 | Millennium Tree of Balete Park | Maria Aurora | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/maria-aurora/millennium-tree-of-balete-park) |
| 11-17 | G3 | The Monkey Thorn on the Riverbed | Francistown | a reader's photograph, published | [live](https://ancienttrees.app/francistown/monkey-thorn-on-the-riverbed) |
| 11-17 | H3 | The Erler Femeiche | Raesfeld | a reader's photograph, published | [live](https://ancienttrees.app/raesfeld/erler-femeiche) |
| 11-17 | I3 | The north door yews of St Edward's, Stow-on-the-Wold | Stow-on-the-Wold | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/stow-on-the-wold/north-door-yews-of-st-edwards-stow-on-the-wold) |
| 11-17 | W2 | The Big Totara of Lillburn Monowai Road | Tuatapere | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tuatapere/big-totara-of-lillburn-monowai-road) |
| 11-17 | J3 | The Oak of Orkin | Pamplona | a reader's photograph, published | [live](https://ancienttrees.app/pamplona/oak-of-orkin) |
| 11-17 | K3 | Boab Prison Tree | Derby | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/derby/boab-prison-tree) |
| 11-17 | K3 | The Hollow Boab of Rowing Club Road | Kununurra | a reader's photograph, published | [live](https://ancienttrees.app/kununurra/hollow-boab-of-rowing-club-road) |
| 11-17 | A | The Sprawling Sycamore of Pawling Farm | Valley Forge | a reader's photograph, published | [live](https://ancienttrees.app/valley-forge/sprawling-sycamore-of-pawling-farm) |
| 11-17 | T2 | Trolleken (the Troll Oak of Trollskogen) | Trollskogen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/trollskogen/trolleken-the-troll-oak-of-trollskogen) |
| 11-17 | T2 | Trolleken (the Troll Oak of Trollskogen) | Trollskogen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/trollskogen/trolleken-the-troll-oak-of-trollskogen) |
| 11-17 | T2 | Trolleken (the Troll Oak of Trollskogen) | Trollskogen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/trollskogen/trolleken-the-troll-oak-of-trollskogen) |
| 11-17 | L3 |  | ? | a reader's photograph, published | not live yet |
| 11-17 | M3 | The Old Yew of Cremines (If millenaire) | Cremines | a reader's photograph, published | [live](https://ancienttrees.app/cremines/old-yew-of-cremines-if-millenaire) |
| 11-17 | N3 | The Oudemanhuispoort Elm | Amsterdam | a reader's photograph, published | [live](https://ancienttrees.app/amsterdam/oudemanhuispoort-elm) |
| 11-17 | U | The Totteridge Yew | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/totteridge-yew) |
| 11-17 | O3 | The St Paul's Churchyard Planes | London | a reader's photograph, published | [live](https://ancienttrees.app/london/st-pauls-churchyard-planes) |
| 11-17 | V | The Twisted Sweet Chestnut of Greenwich Park | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/twisted-sweet-chestnut-of-greenwich-park) |
| 11-17 | P3 |  | ? | a reader's photograph, published | not live yet |
| 11-17 | X1 | The Weeping Cedar Tunnel of Glasnevin | Dublin | a reader's photograph, published | [live](https://ancienttrees.app/dublin/weeping-cedar-tunnel-of-glasnevin) |
| 11-17 | N | El Sargento | Mexico City | a reader's photograph, published | [live](https://ancienttrees.app/mexico-city/el-sargento) |
| 11-17 | X1 | The Fig That Holds the Stones | Chiang Mai | a reader's photograph, published | [live](https://ancienttrees.app/chiang-mai/fig-that-holds-the-stones) |
| 11-17 | C2 | The Baobab Plane of Penenden Heath | Maidstone | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/maidstone/baobab-plane-of-penenden-heath) |
| 11-17 | W1 | Barney the Plane | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/barney-the-plane) |
| 11-17 | Q3 | The Rhodes Bald Cypress | Richard Bong State Recreation Area | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/richard-bong-state-recreation-area/rhodes-bald-cypress) |
| 11-17 | R3 | The Zamalek Banyan | Cairo | a reader's photograph, published | [live](https://ancienttrees.app/cairo/zamalek-banyan) |
| 11-17 | O3 | The Cheapside Plane | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/cheapside-plane) |
| 11-17 | S3 | The Leaning Apple Row of Linford Wood | Milton Keynes | a reader's photograph, published | [live](https://ancienttrees.app/milton-keynes/leaning-apple-row-of-linford-wood) |
| 11-17 | S3 | The Leaning Apple Row of Linford Wood | Milton Keynes | a reader's photograph, published | [live](https://ancienttrees.app/milton-keynes/leaning-apple-row-of-linford-wood) |
| 11-17 | B1 | Rumskullaeken (the Kvill Oak) | Rumskulla | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/rumskulla/rumskullaeken-the-kvill-oak) |
| 11-17 | B1 | Ekebyhovseken | Ekerö | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/ekero/ekebyhovseken) |
| 11-17 | C1 |  | ? | a reader's photograph, published | not live yet |
| 11-17 | T3 | The Himalayan Cedar of Parc Mon Repos | Geneva | a reader's photograph, published | [live](https://ancienttrees.app/geneva/himalayan-cedar-of-parc-mon-repos) |
| 11-17 | T3 | The Sécheron Plane | Geneva | a reader's photograph, published | [live](https://ancienttrees.app/geneva/secheron-plane) |
| 11-17 | U3 | The Tall Tree on the Kanker Forest Track | Kanker | a reader's photograph, published | [live](https://ancienttrees.app/kanker/tall-tree-on-the-kanker-forest-track) |
| 11-17 | V3 | The White Pine at the Orono Bog Boardwalk | Bangor, Maine | a reader's photograph, published | [live](https://ancienttrees.app/bangor-maine/white-pine-at-the-orono-bog-boardwalk) |
| 11-17 | W3 | The Multisecular Beech of Saint-Jammes | Sorèze | a reader's photograph, published | [live](https://ancienttrees.app/soreze/multisecular-beech-of-saint-jammes) |
| 11-17 | W3 | The Multisecular Beech of Saint-Jammes | Sorèze | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/soreze/multisecular-beech-of-saint-jammes) |
| 11-17 | X3 | The Gunnersbury Park Black Mulberry | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/gunnersbury-park-black-mulberry) |
| 11-17 | X3 | The Gunnersbury Park Black Mulberry | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/gunnersbury-park-black-mulberry) |
| 11-17 | X3 | The Gunnersbury Park Black Mulberry | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/gunnersbury-park-black-mulberry) |
| 11-17 | X3 | The Gunnersbury Park Black Mulberry | London | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/london/gunnersbury-park-black-mulberry) |
| 11-17 | Y3 | The National Mall Jefferson Elm | Washington DC | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/washington-dc/national-mall-jefferson-elm) |
| 11-17 | Z3 |  | ? | a reader's photograph, published | not live yet |
| 11-17 | A4 | The Ankerwycke Yew | Runnymede | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/runnymede/ankerwycke-yew) |
| 11-17 | B4 |  | ? | a reader's photograph, published | not live yet |
| 11-17 | C4 |  | ? | a reader's photograph, published | not live yet |
| 11-17 | A | The Sprawling Sycamore of Pawling Farm | Valley Forge | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/valley-forge/sprawling-sycamore-of-pawling-farm) |
| 11-17 | A | The Sprawling Sycamore of Pawling Farm | Valley Forge | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/valley-forge/sprawling-sycamore-of-pawling-farm) |
| 11-18 | D4 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | E4 | The Camperdown Cemetery Fig | Sydney | a reader's photograph, published | [live](https://ancienttrees.app/sydney/camperdown-cemetery-fig) |
| 11-18 | A | The Sprawling Sycamore of Pawling Farm | Valley Forge | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/valley-forge/sprawling-sycamore-of-pawling-farm) |
| 11-18 | B | The Remnant River Red Gum of Edinburgh Gardens | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/remnant-river-red-gum-of-edinburgh-gardens) |
| 11-18 | B | The Remnant River Red Gum of Edinburgh Gardens | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/remnant-river-red-gum-of-edinburgh-gardens) |
| 11-18 | B | The Finer Holm Oak of Edinburgh Gardens | Melbourne | a reader's photograph, published | [live](https://ancienttrees.app/melbourne/finer-holm-oak-of-edinburgh-gardens) |
| 11-18 | F4 | The Shiba Toshogu Ginkgo | Tokyo | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tokyo/shiba-toshogu-ginkgo) |
| 11-18 | I3 | The north door yews of St Edward's, Stow-on-the-Wold | Stow-on-the-Wold | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/stow-on-the-wold/north-door-yews-of-st-edwards-stow-on-the-wold) |
| 11-18 | G4 | The Inner Temple Mulberry | London | a reader's photograph, published | [live](https://ancienttrees.app/london/inner-temple-mulberry) |
| 11-18 | H4 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | I4 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | J4 | The Ueno Toshogu Camphor | Tokyo | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/tokyo/ueno-toshogu-camphor) |
| 11-18 | F |  | ? | a reader's photograph, published | not live yet |
| 11-18 | K4 | The Casuarina of the Cascada | Barcelona | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/barcelona/casuarina-of-the-cascada) |
| 11-18 | N3 | The Leidsebosje Planes | Amsterdam | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/amsterdam/leidsebosje-planes) |
| 11-18 | L4 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | H4 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | H4 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | H4 | The Great Oriental Plane of Emmanuel College | Cambridge | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/cambridge/great-oriental-plane-of-emmanuel-college) |
| 11-18 | M4 | The English Elm of Fort Greene Park | New York | a reader's photograph, published | [live](https://ancienttrees.app/new-york/english-elm-of-fort-greene-park) |
| 11-18 | N4 | Chêne de la Vierge à Viroflay | Viroflay | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/viroflay/chene-de-la-vierge-a-viroflay) |
| 11-18 | N4 | Chêne de la Vierge à Viroflay | Viroflay | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/viroflay/chene-de-la-vierge-a-viroflay) |
| 11-18 | N | The Temple Square Cedar of Lebanon | Salt Lake City | a reader's photograph, published | [live](https://ancienttrees.app/salt-lake-city/temple-square-cedar-of-lebanon) |
| 11-18 | N | The Washington Square Ohio Buckeye | Salt Lake City | a reader's photograph, published | [live](https://ancienttrees.app/salt-lake-city/washington-square-ohio-buckeye) |
| 11-18 | N | The Washington Square Hackberry | Salt Lake City | a reader's photograph, published | [live](https://ancienttrees.app/salt-lake-city/washington-square-hackberry) |
| 11-18 | N | The Liberty Park London Planetree | Salt Lake City | a reader's photograph, published | [live](https://ancienttrees.app/salt-lake-city/liberty-park-london-planetree) |
| 11-18 | N | Jardine Juniper | Logan Canyon | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/logan-canyon/jardine-juniper) |
| 11-18 | O4 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | O4 | El Árbol del Tule | Santa María del Tule | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/santa-maria-del-tule/el-arbol-del-tule) |
| 11-18 | N | The Fortingall Yew | Fortingall | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/fortingall/fortingall-yew) |
| 11-18 | N | Dughall Mor and the Reelig Glen giants | Reelig Glen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/reelig-glen/dughall-mor-and-the-reelig-glen-giants) |
| 11-18 | P4 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | Q4 |  | ? | a reader's photograph, published | not live yet |
| 11-18 | R4 | The Copper Beech of the Antonius Abtkerk | Nijmegen | a reader's photograph, published | [live](https://ancienttrees.app/nijmegen/copper-beech-of-the-antonius-abtkerk) |
| 11-18 | R4 | The Copper Beech of the Antonius Abtkerk | Nijmegen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/nijmegen/copper-beech-of-the-antonius-abtkerk) |
| 11-18 | R4 | The Copper Beech of the Antonius Abtkerk | Nijmegen | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/nijmegen/copper-beech-of-the-antonius-abtkerk) |
| 11-18 | S4 | The Ada Tree | Powelltown | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/powelltown/ada-tree) |
| 11-19 | Q4 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | T4 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | U4 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | U4 | The Kapok Tree | Key West | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/key-west/kapok-tree) |
| 11-19 | U4 | The Cosgrove House Banyan | Key West | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/key-west/cosgrove-house-banyan) |
| 11-19 | U4 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | U4 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | U4 | Grandfather Pine at Serenbe | Serenbe | a reader's photograph, published | [live](https://ancienttrees.app/serenbe/grandfather-pine-at-serenbe) |
| 11-19 | U4 | Grandmother Beech at Serenbe | Serenbe | a reader's photograph, published | [live](https://ancienttrees.app/serenbe/grandmother-beech-at-serenbe) |
| 11-19 | U4 | The McDonogh Oak | New Orleans | a reader's photograph, published | [live](https://ancienttrees.app/new-orleans/mcdonogh-oak) |
| 11-19 | U4 | The Anseman Oak | New Orleans | a reader's photograph, published | [live](https://ancienttrees.app/new-orleans/anseman-oak) |
| 11-19 | U4 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | U4 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | U4 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | U4 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | U4 |  | ? | a reader's photograph, published | not live yet |
| 11-19 | U4 | The Moreton Bay Fig of Balboa Park | San Diego | a reader's photograph, published beside the one it had | [live](https://ancienttrees.app/san-diego/moreton-bay-fig-of-balboa-park) |
| 11-17 | H3 | Pedunculate Oak near Winterswijk | - | a reader's correction changed the page | - |
| 11-17 | A | American Sycamore at Pawling Farm in Valley Forge National Park | - | a reader's correction changed the page | - |
| 11-17 | O3 | The St Paul's Churchyard Planes | London | a reader's correction changed the page | - |
| 11-17 | Z3 | Horse Chestnut Tree of Sofienbergparken | Oslo | a reader's tree changed the page | - |
| 11-18 | M4 | nyc_027 (The English Elm of Fort Greene Park) | New York | a reader's feedback changed the page | - |
- From 95 readers: reader U4 15, reader N 9, reader M 8, reader A 5, reader T2 5, reader X1 5, reader H4 4, reader X3 4, reader B 3, reader D 3, reader J2 3, reader L2 3, reader O3 3, reader Q2 3, reader R4 3, reader V2 3, reader B1 2, reader C2 2, reader C3 2, reader D3 2, reader E2 2, reader F 2, reader G2 2, reader H 2, reader H3 2, reader I 2, reader I3 2, reader K3 2, reader M4 2, reader N3 2, reader N4 2, reader O 2, reader O4 2, reader Q4 2, reader S3 2, reader T3 2, reader W2 2, reader W3 2, reader X2 2, reader Z3 2, reader A2 1, reader A3 1, reader A4 1, reader B2 1, reader B3 1, reader B4 1, reader C1 1, reader C4 1, reader D1 1, reader D2 1, reader D4 1, reader E 1, reader E3 1, reader E4 1, reader F2 1, reader F3 1, reader F4 1, reader G3 1, reader G4 1, reader H2 1, reader I2 1, reader I4 1, reader J3 1, reader J4 1, reader K2 1, reader K4 1, reader L 1, reader L3 1, reader L4 1, reader M2 1, reader M3 1, reader N2 1, reader O2 1, reader P 1, reader P2 1, reader P3 1, reader P4 1, reader Q3 1, reader R1 1, reader R2 1, reader R3 1, reader S2 1, reader S4 1, reader T4 1, reader U 1, reader U2 1, reader U3 1, reader V 1, reader V3 1, reader W1 1, reader Y1 1, reader Y2 1, reader Y3 1, reader Z1 1, reader Z2 1.

**What was sent in, and what we decided**

| seen | what | where | size for its species | ours | Hidde |
|---|---|---|---|---|---|
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | lead | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | The Remnant River Red Gum of Edinburgh | Melbourne | - | hold | - |
| 2026-11-18 | The Southern Mahogany of Edinburgh Gar | Melbourne | - | hold | - |
| 2026-11-18 | The Casuarina of the Cascada | Barcelona | - | hold | - |
| 2026-11-18 | a tree we do not map | - | - | open | - |
| 2026-11-17 | Ahuehuete del Jardin de San Fernando | Mexico City | - | hold | - |
| 2026-11-17 | The Cosgrove House Banyan | Key West | - | hold | - |
| 2026-11-17 | European Beech in Baarn | - | - | hold | - |
| 2026-11-17 | European Beech in Baarn | - | - | hold | - |
| 2026-11-17 | a tree we do not map | Baarn | - | hold | - |
| 2026-11-17 | A tree I found | - | - | hold | - |
| 2026-11-17 | A tree I found | - | - | hold | - |
| 2026-11-16 | Eastern Cottonwood | - | - | hold | - |
| 2026-11-16 | A tree I found | - | - | hold | - |

1 waiting for a verdict. Disagree with one and the rule changes: `python3 scripts/judgement.py --feedback <id> "..."`, and `--learn` prints every verdict he has overruled.

**Searched yesterday:** london (3 times), amster (2 times), bristol (2 times), canada (2 times), copenhagen (2 times), edi (2 times), oberhausen (2 times), ormiston (2 times), perth (2 times), phil (2 times), san (2 times), seattle (2 times), shropshire (2 times), adel, adelaide, akron, ohio, arn, austra, ballarat, baltimore.

**App crashes** (last 7 days, store builds; MetricKit, a sample)

| Crashes | Kind | Build | Where | Phones | Last | Fix |
|---:|---|---|---|---:|---|---|
| 1 | crash | 1.0.4 (41) | (no AncientTrees frame) | 1 | 2026-11-15 | none |
| 1 | crash | 1.0.4 (41) | AncientTrees+0x2409a0 | 1 | 2026-11-16 | none |

**Search**

Google, the last 10 days it will give us (2-3 days behind; the newest row is still filling, so it reads better than it is):

| Day | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| 11-09 | 28 | 1177 | 2.4% | 8.9 |
| 11-10 | 8 | 196 | 4.1% | 13.0 |
| 11-11 | 1 | 16 | 6.2% | 22.1 |
| 11-12 | 1 | 28 | 3.6% | 31.4 |
| 11-13 | 1 | 32 | 3.1% | 55.0 |
| 11-14 | 0 | 51 | 0.0% | 57.5 |
| 11-15 | 210 | 363 | 57.9% | 8.2 |
| 11-16 | 116 | 204 | 56.9% | 6.6 |
| 11-17 | 59 | 132 | 44.7% | 15.0 |
| 11-18 *partial* | 28 | 58 | 48.3% | 19.0 |
| **window** | **452** | **2257** | **20.0%** | |
- Top queries (10d): ancient trees app (i438, p1); ancient trees (i13, p32); ancient tree app (i3, p1); android au (i1, p1); এই অ্যাপের লিংক দাও (i1, p2)
**What Bing shows and sends** (last 7 days with data, Bing Webmaster Tools)

| Day | Impressions | Clicks | CTR |
|---|---:|---:|---:|
| 11-11 | 97 | 7 | 7.2% |
| 11-12 | 190 | 4 | 2.1% |
| 11-13 | 125 | 5 | 4.0% |
| 11-14 | 103 | 6 | 5.8% |
| 11-15 | 132 | 13 | 9.8% |
| 11-16 | 211 | 15 | 7.1% |
| 11-17 | 170 | 6 | 3.5% |
| **7 days** | **1028** | **56** | **5.4%** |
- Week before: 864 impressions, 43 clicks. No Bing demotion in sight.
- Top Bing queries: oldest tree china (c8/i4, p12); platane du square des batignolles (c4/i2, p1); picture of the tree in helsinki city center that was preserved (c3/i2, p4); ancient trees app (c2/i8, p5); who planted the western red cedar tree in blarney ireland (c2/i8, p2); fig tree in square alicante (c2/i4, p4); palma del cile (c2/i2, p6); cipresso calvo indro montanelli milano (c2/i2, p8)
- Bing alone, from Bing Webmaster Tools. DuckDuckGo and Yahoo draw on the same index and publish no numbers. Bing's data lags about two days.

---

**For the night run, not for you.** You can stop reading here.


**What the machine did, the last 24 hours**

| Started | Minutes | Trees | Commits | Refused | Cities |
|---|---:|---:|---:|---:|---|
| 11-18T07:41 | 2.5 | 0 | 6 | 0 | - |
| 11-18T16:36 | 11.1 | 2 | 12 | 0 | Bengaluru +1, Narita +1 |
| 11-18T18:04 | 4.0 | 0 | 6 | 0 | - |
| 11-18T18:35 | 12.5 | 0 | 10 | 2 | Fortingall, Logan Canyon, Reelig Glen, Salt Lake City |
| 11-18T23:09 | 17.2 | 2 | 10 | 0 | Key West +2, Nijmegen |
| 11-19T01:37 | 6.7 | 0 | 5 | 0 | - |
| 11-19T04:17 | 6.2 | 2 | 9 | 2 | Serenbe +2, New Orleans |
| **7 runs** | **60** | **6** | **58** | | |

- 4 of 7 produced no trees; 2 to 2 commands refused per run; last build that went live: 2h ago, 2 failed since.

**What they made**

- reader judge: Kasama leaf-seed ginkgo live from a reader's tip (Ibaraki register)
- reader judge: Adelaide pin report and a mail reply filed for Hidde
- reader judge: Islamorada banyan, two Key West kapoks, two San Diego trees and a City Park oak live; Balboa fig reader photo as lead
- claim key-west (verify)
- Birmingham verify pass dry, holly lead kept, claim released; LOG
- reader judge: Serenbe trails access from Serenbe's own page; doubt on the Anseman strip photo logged
- claim birmingham (verify)
- reader judge: Serenbe pine and beech live (new place), McDonogh Oak reader photo as lead, Anseman Oak second view
- Photographs readers sent, queued for a look; vouched ones live
- Record when each page last changed
- Contributor replies and ambassador invitations sent, log updated
- reader judge: the Fort Screven oak (savannah/sav_004) and Yellowstone's Petrified Tree (yellowstone/yel_001) live
- reader judge: the Adair Park ginkgo live (atlanta/atl_012), two Key West reader photos as lead
- reader judge: the Palm Beach kapok live (palm-beach/pbh_001), Florida's champion kapok, reader's four photos and GPS fix

**Reader photographs in a strip, live first, not yet looked at** (30)

| Day | Tree | Where | Undo |
|---|---|---|---|
| 11-17 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | `sightings_publish.py --unstrip 5e09bb82-34d7-4622-b626-8251836f6eb4` |
| 11-17 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | `sightings_publish.py --unstrip 62c4bb28-b3f8-46f6-8d7a-c88755acce7b` |
| 11-17 | The Whistler Cork Oak (Sobreiro Assobiador) | Aguas de Moura | `sightings_publish.py --unstrip 5ecc82c8-870b-4961-9a0f-b4fb6bf2e1b6` |
| 11-17 | The Cantonspark Giant Sequoia | Baarn | `sightings_publish.py --unstrip cc8a74d4-d8a7-42fa-865c-f5a12e490f7f` |
| 11-17 | Benmore Redwood Avenue | Benmore | `sightings_publish.py --unstrip cdc0b82c-26f6-4691-94df-3d728924d039` |
| 11-17 | Benmore Redwood Avenue | Benmore | `sightings_publish.py --unstrip 4c161566-17bf-4859-a3cb-2148328999a9` |
| 11-17 | The Gomero de la Recoleta | Buenos Aires | `sightings_publish.py --unstrip e5b4eedf-8140-4bf4-8ce2-c32a1f921168` |
| 11-17 | The Angel Oak | Charleston | `sightings_publish.py --unstrip 78b88780-f090-4c13-8360-95570ebe3113` |
| 11-17 | Boab Prison Tree | Derby | `sightings_publish.py --unstrip 023ed607-1e16-4502-a16c-ba7b77888f82` |
| 11-18 | The Fortingall Yew | Fortingall | `sightings_publish.py --unstrip f2e99426-d46c-4a73-9ab9-25f92c7edf6a` |
| 11-17 | The Land Boat Pine | Kyoto | `sightings_publish.py --unstrip 46766dcd-94f4-4656-8dab-53b5c98b30f8` |
| 11-17 | The Bald Cypresses of the Crystal Palace Pond | Madrid | `sightings_publish.py --unstrip e593be60-987f-469d-97d7-7da2a69503d5` |
| 11-17 | Old Knobbley | Mistley | `sightings_publish.py --unstrip a477d312-0d76-4189-9217-ef167b0b1bc7` |
| 11-17 | Bleeding Yew of Nevern | Nevern | `sightings_publish.py --unstrip 09765ff6-b1e9-4d56-a98a-73c47709468b` |
| 11-18 | The Copper Beech of the Antonius Abtkerk | Nijmegen | `sightings_publish.py --unstrip 1d8d8c2e-a5ad-45d4-ba5f-72956149bc7c` |
| 11-18 | The Copper Beech of the Antonius Abtkerk | Nijmegen | `sightings_publish.py --unstrip e23fe779-5876-4cd3-9fab-c50f7e28dcda` |
| 11-17 | S'Olivera de Cort | Palma de Mallorca | `sightings_publish.py --unstrip 3c756f92-fc89-4a76-a714-06e8a6361b0f` |
| 11-17 | The Oak of Molinazzo | Poggio Renatico | `sightings_publish.py --unstrip c42df403-c159-4896-9c07-223d1122c3d6` |
| 11-18 | Dughall Mor and the Reelig Glen giants | Reelig Glen | `sightings_publish.py --unstrip 691e83b3-fa05-4961-a56f-9912db89c1ac` |
| 11-17 | The Moreton Bay Fig of Balboa Park | San Diego | `sightings_publish.py --unstrip ee80ee46-48b1-4e89-bc8d-23c892d50b1d` |
| 11-17 | Chief Sequoyah Tree | Sequoia National Park | `sightings_publish.py --unstrip c59bfd73-d95b-4cda-9ae3-5f75cf6f9754` |
| 11-17 | The Wishing Tree | Sydney | `sightings_publish.py --unstrip 4be001d1-ee21-48f8-81df-67bf1bb02d41` |
| 11-17 | The Wishing Tree | Sydney | `sightings_publish.py --unstrip f05d3a86-b304-47ac-bf24-2e0f88ad99a1` |
| 11-17 | The Great Ginkgo of Hida Kokubunji | Takayama | `sightings_publish.py --unstrip 65cb49cd-5812-4470-a56c-4b681646b7d2` |
| 11-17 | The Big Oak | Thomasville | `sightings_publish.py --unstrip aa636a2c-f651-42b4-82e2-18f8ce6b981e` |
| 11-17 | The Big Oak | Thomasville | `sightings_publish.py --unstrip c64b5650-6946-456a-b0d4-8af4fd95bacd` |
| 11-17 | Trolleken (the Troll Oak of Trollskogen) | Trollskogen | `sightings_publish.py --unstrip 54dc7d2a-aaf6-4158-8784-3f3c256942a3` |
| 11-17 | The Big Totara of Lillburn Monowai Road | Tuatapere | `sightings_publish.py --unstrip 45e7ad05-a36e-480b-8c4b-fc0e4d5c5a47` |
| 11-17 | The Sisi-Platane of Volksgarten | Vienna | `sightings_publish.py --unstrip 57a1afed-1a15-4782-b4a1-4aeaf08a9f04` |
| 11-17 | The Sisi-Platane of Volksgarten | Vienna | `sightings_publish.py --unstrip 161c7f67-f76d-4527-84b1-d24ab59c798f` |

Machine: 7 chain attempts yesterday, 7 got real work time (~82 min total). Dead-in-seconds attempts cost nothing; few get-throughs means the usage window was full or closed.

**Search work lists**

- Top pages (10d): / (c411/i647); /app (c3/i24); /switzerland (c2/i7); /fr/lyon/arbre-le-plus-vieux (c2/i3); /seville (c1/i31)
- Content leads, biggest first. A lead is a query no page TITLE covers, so some are ranking problems on a page we have rather than a page to write ('vegas trees' against /las-vegas). Check before building:
    - 'android au' (i1, p1)
    - 'এই অ্যাপের লিংক দাও' (i1, p2)
    - 'acient tree' (i1, p3)
    - 'alberi di roma' (i1, p1)
    - 'alte bäume in der nähe' (i1, p5)
    - 'alte bäume karte' (i1, p5)
    - 'alter' (i1, p2)
    - 'angeloak' (i1, p99)
    - and 1 more

**Is enriching working** (indexed tree pages, last 10 days of Google; rich = register record, a measurement and concrete access)

| Indexed tree pages | Pages | With an impression | Impressions | Per page | Clicks |
|---|---:|---:|---:|---:|---:|
| Rich | 172 | 15 | 42 | 0.24 | 1 |
| Not yet rich | 298 | 18 | 77 | 0.26 | 0 |
| Returned to Google's index in the last 7 days | 0 | 0 | 0 | 0.00 | 0 |

- Google lags 2 to 3 days, so a page returned this week has had a few days at most. Compare the per-page numbers across weeks, not the totals across rows.

**Depth is allowed on these cities** (10+ impressions in the window; photos, pins and best_time go here and nowhere else):

| City | Clicks | Impressions | CTR | Position | Normal there | Biggest query, and where it really sits |
|---|---:|---:|---:|---:|---:|---|
| lisbon | 0 | 48 | 0.0% | 5.9 | 5.2% | historic giant plant of lisbon (i1, p12) |
| fortingall | 0 | 38 | 0.0% | 15.1 | 1.2% | fortingall yew (i31, p10) |
| seville | 1 | 35 | 2.9% | 5.3 | 6.3% | seville trees (i1, p12) |
| olympic-national-park | 0 | 30 | 0.0% | 24.3 | 0.6% | duncan cedar (i8, p11) |
| fulufjallet | 0 | 25 | 0.0% | 9.6 | 2.7% | old tjikko (i14, p10) |
| tokyo | 0 | 25 | 0.0% | 5.9 | 5.2% | ginkgo sperm (i1, p11) |
| berlin | 1 | 23 | 4.3% | 5.8 | 5.4% | berlin trees (i1, p4) |
| malaga | 0 | 23 | 0.0% | 27.4 | 0.5% | árboles históricos de málaga (i6, p90) |
| monterey | 0 | 22 | 0.0% | 65.7 | 0.4% | lone cypress (i6, p80) |
| london | 0 | 22 | 0.0% | 40.6 | 0.4% | flats to rent clerkenwell (i3, p89) |
| munich | 1 | 21 | 4.8% | 5.3 | 6.4% | ältester baum münchen (i1, p8) |
| south-korea | 0 | 18 | 0.0% | 26.3 | 0.5% | trees in south korea (i2, p46) |
| palermo | 0 | 18 | 0.0% | 9.6 | 2.7% | palermo tree (i1, p9) |
| kyoto | 1 | 17 | 5.9% | 3.7 | 8.9% | ginkgo tree kyoto (i1, p1) |
| tenerife | 0 | 17 | 0.0% | 60.3 | 0.4% | drago tree tenerife (i2, p96) |
| sequoia-national-park | 0 | 17 | 0.0% | 41.3 | 0.4% | washington tree (i7, p35) |
| singapore | 0 | 17 | 0.0% | 11.1 | 2.1% | baobab tree singapore (i1, p10) |
| copenhagen | 1 | 16 | 6.2% | 13.1 | 1.6% | copenhagen trees (i3, p39) |
| paris | 1 | 15 | 6.7% | 6.1 | 4.9% | - |
| taiwan | 0 | 14 | 0.0% | 12.8 | 1.6% | oldest tree in taiwan (i3, p5) |
| barcelona | 0 | 14 | 0.0% | 10.4 | 2.4% | - |
| seoul | 0 | 13 | 0.0% | 6.6 | 4.4% | - |
| edinburgh | 0 | 12 | 0.0% | 13.4 | 1.5% | - |
| milan | 0 | 11 | 0.0% | 5.5 | 5.9% | - |
| porto | 1 | 10 | 10.0% | 1.7 | 18.9% | - |
| dublin | 1 | 10 | 10.0% | 4.4 | 7.6% | - |
| austin | 0 | 10 | 0.0% | 18.1 | 1.0% | oldest tree in austin (i2, p12) |
| kagoshima | 0 | 10 | 0.0% | 7.3 | 3.9% | - |
| amsterdam | 0 | 10 | 0.0% | 9.0 | 3.0% | lomanstraat (i1, p17) |
| cambridge | 0 | 10 | 0.0% | 30.1 | 0.4% | isaac newton tree (i1, p36) |

- Plus 230 cities on the frozen 09-27 roster (data/depth-roster-frozen.json), biggest: bath, rome, oahu, new-york, brussels, brisbane, vienna, alicante.

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

