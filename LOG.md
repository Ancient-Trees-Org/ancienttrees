# LOG

<!-- archive-index -->

**Older entries live in the archive**, moved by `scripts/archive_logs.py`, nothing deleted:

- [2026-11](archive/LOG-2026-11.md)
- [2026-10](archive/LOG-2026-10.md)
- [2026-09](archive/LOG-2026-09.md)
- [2026-08](archive/LOG-2026-08.md)
- [2026-07](archive/LOG-2026-07.md)

## 2026-11-28 reader judge: the Central Park elm avenue gets its first photograph

- The Elm Allee of Literary Walk (nyc_013), New York: a reader's app photograph is now the lead. It shows the Mall's double row of bare American elms in daylight, with Literary Walk's fencing and walkers along it, 86 m from our pin. It is filed under November, the photo's own month. Their second frame of the grove went in the gallery (reader_extras). The pin stays where it was, because it is the confirmed register point. The reader got the "it is on the page" mail through `--send`.
- The same photograph and its extra came in a second time (06d425d1). Rejected as a duplicate.
- With a photograph the page now counts as indexed, so preflight caught two colon reveals in its story. Both sentences were rewritten without changing any fact.
- No open reports, tips, feedback or readers' notes, and nothing late. The 37 waiting leads are all the owner's own account. qa (source), preflight (0 problems) and i18ncheck are clean.

## 2026-11-28 reader judge: an Etna holm oak photo held to ask who took it; the Palermo ficus photo sent twice more

- Three app photographs from the same reader, all kept in their own collection only, so no submissions row and no mail (hold_reply.py said so).
- Ilice di Carrinu (zaf_001), the tree's first photograph: it fits (holm oak, long low arms over a wooded slope, a man photographing it), but it is a 1070x1070 square with no camera data, a social-media download, so held `doubt_photo` under the 2026-11-26 screenshot rule. A good picture; it goes up the day the maker says yes.
- The Ficus of Piazza Marina (pal_001), twice: the same file, byte for byte, as the photo held this afternoon (d1b53020). Rejected as duplicates.
- No open reports, tips, feedback, further photographs or readers' notes. The 37 waiting leads are all the owner's own account.

## 2026-11-28 reader judge: Palermo ficus photo held to ask who took it

- One photograph waited: an app reader's shot of the Ficus of Piazza Marina (pal_001). It is that tree, but the file is 960x720 with no camera data and a heavy glow filter, where the app's own photographs arrive at 1200x1600, so it is held as `doubt_photo` (the screenshot rule of 2026-11-26). The reader kept it in their own collection only, so there is no submission row to ask through and no mail went out (hold_reply.py said so).
- No open reports, no unjudged tips, no feedback, no further photographs, no readers' words waiting. The 37 leads still marked `lead` are all the owner's own account (`mine`), so this run left them alone.

## 2026-11-28 session: Android build 8 ready for Hidde's phone, instead of 7

- Build 8 (versionCode 8) is everything on main: the map no longer jumps when you tap a pin (35ce95e87), and a tree chosen at launch no longer shows a second dot half under its big pin (map-parity row done, walked in Baarn).
- Signed, then walked on the emulator: every tab, a tree, and the Feed opened and scrolled. No crash.
- For Hidde: drag out/play/ancient-trees-0.1.0-8.aab into Play's internal testing release, then install from the internal link on your phone. Build 7 is not uploaded and is skipped.
- Still red: the button walk on two test-side points (the Discover Save heart signed in, map pin Close sheet signed out); not yet proven to be the test's fault.

## 2026-11-28 reader judge: two Rome trees get readers' photographs, one olive and one beech held

- **Rome, the Himalayan Cedar of the German Institute (rom_011)** has its first photograph, a reader's: the broad deodar in Villa Sciarra's statue garden. The register pin stays, since the app's coordinate (1.1 km off) carried no camera data and the same reader sent Villa Sciarra photographs that day.
- **Rome, the Ginkgo of Villa Sciarra (rom_001)** now leads with the same reader's autumn photograph; the Commons one moved to the strip. Their two other uploads were the same file and are rejected as duplicates.
- Held: the Santu Baltolu wild olive photo (sar_002) as `wrong_tree`, because two of ours stand metres apart there and the crown looks more like S'Ozzastru's. It came from the reader's own collection, so there is no mail. A beech near Bergamo is held as `not_special`: a nice frame of an ordinary woodland beech, the same size as its neighbours. Hidde sees both in the digest.
- Breakage found and repaired: the session commit ebaec7d38 dropped four of this afternoon's entries from data/sightings-processed.json (the Cascada she-oak, the Ashbridges pine, the second Toronto pine, the Ciutadella black locust), so the intake queued them again. Restored from the commit before; no photo was published twice.
- No reports or feedback were open. Nine new tree notes are left for the night run; none needs hiding.

## 2026-11-28 session: open mails answered, and what they changed on the map

- **New Orleans, the Enrique Alferez Oak (nol_008)** has its first photographs: two black-and-white frames our ambassador William Guion sent by mail to add to the City Park pages (his words are kept as the permission). His Anseman and McDonogh photographs are in those trees' galleries. Its pin moved about 850 m to the Pavilion of the Two Sisters in the Botanical Garden, where he says it stands (#13 on the 1999 walking tour); still approximate.
- **Genoa, the Cedar of Lebanon of Acquasanta (gnv_012)** now leads with the app reader's own photograph, after they confirmed by mail that they took it. The access line and story now say it stands by the church square, on the wooded slope its photo shows.
- **New place, Scarborough**: two trees from a reader's tips with their own what3words spots, on Hidde's yes. The Raincliffe Woods Beech (sca_001) and the East Ayton Chestnut (sca_002) both have approximate pins and no photo. The chestnut's spot is on Seavegate in East Ayton, 3 km from the woods the tip named. Its page says so and asks, and "second oldest in the country" is given as the reader's claim.
- Mails sent on Hidde's "you can send all these emails": the Lake Waikaremoana and Katikati ambassadors got personal replies instead of the standard welcome (so `--welcome-missing` must skip lake-waikaremoana and katikati). Bill and the cedar reader get theirs once this deploy is live.
- Found: `ambassador.py --welcome-missing` without `--send` wrote Horn-Lehe and Girona into data/ambassadors.json as handled; reverted, and their welcome mails are still owed.

## 2026-11-28 night run (fourth attempt, same window): nothing shipped, same state

- Pulled, no claims, READY 0, prepare.py names no writer work (own research paused; every verified file is stale or an id clash), `enrich.py --next`, `recognise.py --stuck` and `reader_words.py` empty. Only reds: the open app BUG rows (edit a tree you added, Android pin place), which need a device or emulator build this runner lacks. Left for a session.

## 2026-11-28 night run (third attempt, same window): nothing shipped, same state

- Pulled, no claims, READY 0, prepare.py has no writer work (own research paused). Health reds are only the open app BUG rows (edit a tree you added; Android draft on the account; Android pin place). Each needs a design plus an emulator or device build and cannot be verified on this runner, so none was started blind. A session takes them.

## 2026-11-28 night run (retry in the 15:00 window): nothing shipped, nothing left to take

- Pulled, no claims standing, READY 0, no staged verify work (own research paused), `enrich.py --next` and `recognise.py --stuck` empty, `reader_words.py` 0 notes waiting (4 mail sentences wait for the sender's yes). Every non-stale `*-verified.json` is a duplicate or id clash of a live tree, so there is nothing to write. Health reds: the open app BUG rows only; each needs a server design or an emulator and a build (edit a tree you added, Android draft on the account, Android pin picker), so a session takes them. Web error "Unexpected end of input" is 1 report on 1 page, below the red line.

## 2026-11-28 night run (15:00 window): nothing shipped, shelf empty

- Rung 1: read the 9 new tree notes (Barcelona Ciutadella, Copenhagen, Aachen); none on the closed list, all left public, marked seen. Reader backlog clear. Rung 2: health reds only the open app BUG rows. The Android add-a-tree pin row (ESC-2026-11-28) is likely already covered by PinPicker.kt (pin step shipped earlier), so it needs a session to confirm on an emulator. The edit-a-tree-you-added row and the Android draft-on-account row need a server design and a build, so a session takes them. Web errors orange: one inline "Unexpected end of input" type, below the red threshold. READY 0, own research paused, nothing to dispatch.

## 2026-11-28 reader judge: new lead photographs for the Cascada she-oak and the Ashbridges Bay pine; two other trees asked about

- **Barcelona, The Casuarina of the Cascada** (bcn_011, sighting 3eff6d97, the same Barcelona reader as all day): the two fused trunks and the drooping grey green crown, seen from the lawn. Added, so it now leads, and the earlier reader's photo moved to the strip. The pin is confirmed and stays.
- **Toronto, The Pine of Ashbridges Bay** (tro_008, sighting ce4c5494, the reader who added it): the same pine from the other side, with the bench, the taped shore and the lake. Added, so it now leads, and their first photo is in the strip. Report 1000165 (the app's "which tree" for their first photo) was already settled by tro_008, so it is closed `holds`.
- **Held `doubt_location`, Toronto** (sighting 5198b700 from the same reader, sent for tro_008): a different pine, alone on a lawn with long low limbs. It is worth a page, but its coordinate matches the lakeshore pine's to the last digit, so it shows where the phone was, not the tree. The standard mail asking where it stands goes at the next knock (row 1823).
- **Barcelona, The Black Locust of the Ciutadella** (bcn_035): the reader's photo (sighting 6b0ae614) shows a much slimmer black locust than the register's 4.3 m trunk. In report 1000166 they wrote themselves that the big one stands by the drinking fountain near the Cascada. So the photo did not go on the page. It became a lead and is held `doubt_location`: the app coordinate is 206 m off and carries no camera data. It has no submissions row, so no automatic mail went. Their hand-moved pin (report 1000164, 29 m, towards the Cascada) is now the page's pin. It stays approximate, `pin_source` records it, and the standard pin thank-you went out. Report 1000166 carried their own words, so it is closed `holds` with no mail.
- **For Hidde:** a suggested reply to report 1000166 is in drafts/reply-reader-1000166-2026-11-28.md. It says yes, the one by the fountain is ours, and asks where the slimmer one stands.
- Nothing else waited: 0 feedback, 0 tips, 0 further photographs, and the 37 `mine` leads are untouched. The pin read hit an HTTPError again, which changed nothing. qa, preflight (0 problems) and i18ncheck are clean.

## 2026-11-28 night run (second retry): nothing shipped, shelf still empty

- Claims none, READY 0, passcheck --pending only stale or duplicate files, reader_words and recognise --stuck empty, reader backlog clear, health: only the three open app BUG rows (edit a tree you added, Android place picker, Android draft on the account), all features needing a build and design. Own research paused, so nothing was dispatched. Two Barcelona photographs (bcn_035, bcn_012) wait for the reader judge.

## 2026-11-28 night run (retry, 7 min in): nothing shipped, shelf empty

- Claims: none standing. READY leads: 0. Verified-unpublished: one Taiwan tree (below the six-tree floor), everything else in passcheck --pending is stale or duplicate files. enrich, recognise --stuck and reader_words: nothing to do. Own research stays paused.
- Open app BUG rows are all features, not quick fixes: editing a tree you added (iOS), Android's place picker for a new tree (pin went to Amsterdam), Android's draft on the account. They need design and a build, so I left them.
- **Toronto, The Pine of Ashbridges Bay** (tro_008, sighting 8aefa773): the push was blocked by this reader's tree sitting as a lead with no verdict. Photograph viewed (a multi-stemmed pine with orange peeling bark on the lake boardwalk, GPS fix at the tree), so it is live under the closed list, species kept at genus (Pine, Pinus sp.). Place from the fix (The Boardwalk, South Riverdale). Toronto's counts went from seven to eight in the intro, meta and FAQ. The congratulation mail goes on the next knock.
- Two reader photographs (bcn_035, bcn_012) still wait for the reader judge, which owns them.

## 2026-11-28 reader judge: a reader's photograph leads the Ciutadella's Mexican oak; the cheesewood page no longer puts it at the bandstand

- **Barcelona, The Mexican Oak of the Ciutadella** (bcn_012, sighting 3c2e6b81): a reader's daylight photograph of the leaning twin stem in its roped ring now leads the page, and the Commons photograph moved to the strip. The app's coordinate stood 173 m from the register coordinate and from report 1000162, which agree within 18 m, and the file carried no camera data. sightings_publish.py moved the pin to it anyway, so I put it back on the register (approximate) and noted why in `verify_notes`.
- **Barcelona, The Japanese Cheesewood of the Ciutadella** (bcn_037, report 1000163): the reader wrote that the bandstand is not near our pin and that an almost identical tree stands by the bandstand. OSM puts the Glorieta 170 m north of our pin. Our pin is the register's own coordinate, and a reader photographed the roped cheesewood there today, so the pin stays. The register's "in front of the Glorieta" wording came off the address, the recognition line and the story, in English and Spanish. The story now points to the rope ring and gives the twin by the bandstand as a visitor's word. They wrote their own words, so no standard mail went out. The report is closed `holds`.
- **For Hidde:** a suggested reply to report 1000163 is in drafts/reply-reader-1000163-2026-11-28.md.
- No new reader trees, tips or feedback waited. The same 37 `mine` leads stay as they were.
## 2026-11-28 night run (14:29 window): nothing shipped, one note closed

- **Rung picked**: 2 was red only on open app BUG rows in data/code-audit.json (3 open, 2 found by readers). All three need work a run cannot verify: a tree you added cannot be edited afterwards (feature, Collect.swift), the Android draft that must live on the account (Hidde's rule 11, a server table), and the Android place step. I read the last one: `CollectSheet.kt` falls back to `origin`, which is Dam Square when the phone has no fix yet (`MainActivity.kt` `DAM_SQUARE`), and `PlaceStep` opens there. A fix is Android UI I cannot build or run here, so I made no blind change. The rows stay open.
- Rung 1 left to the reader judge as written: bcn_035 and bcn_012 photographs, one unnamed Toronto-area sighting (8aefa773).
- Own research is paused and nothing is READY or verified to write, so there was no supply work. Closed the reader note 1000163 (Ciutadella Japanese Cheesewood) in `reader_words.py --done`: a location report about a lookalike near the bandstand, not story words.
- Web errors ORANGE: "undefined has no property 'getLayer'" inside maplibre-gl, two new types; not looked into this window.

## 2026-11-28 reader judge: a reader's fir in Bentivoglio is live, the Ciutadella's Mexican oak pin moved

- **New tree, Bentivoglio, The Fir of Bentivoglio** (bnt_001, sighting b19c636e). It was held this morning as `no_location` because the pin placed in the Android app landed on Dam Square, Amsterdam. The reader mailed back its place, the centre of Bentivoglio near Bologna, with coordinates (feedback 1813). Their four photographs show a dense conifer about four times the height of the building beside it. The page uses their figures as theirs: about 20 m tall, trunk about 300 cm. The pin is approximate (coordinates they typed, not a fix). The species is listed as fir (Abies sp.) because the photographs could also show a spruce, and the page asks readers. Access: seen from the street, and whether the lawn is open is unconfirmed. It is a one-tree place with its texts and three FAQ, and its names were looked up. All three further photographs went up.
- **Their mail also reported a bug**: on Android they could not set the tree's place on the map, nor correct or delete it afterwards. Filed as ESC-2026-11-28-android-adding-a-tree-the-reader-could-n (rung-2, Contribute.kt), with a reader line. Their wish to choose the app's language is under "Ideas from readers" in PRODUCT_TODO.md. Feedback 1813 is closed `bug`.
- **For Hidde:** a reply to the Bentivoglio reader waits in drafts/reply-reader-1813-2026-11-28.md (it says the tree is on the map, the bug is being fixed, and the language wish is noted).
- **Barcelona, The Mexican Oak of the Ciutadella** (bcn_012, report 1000162): a reader moved our approximate pin 92 m. Barcelona's register of trees of local interest (99400454956) stands 18 m from their spot, between the lake and the Cascada, so the pin moved to the register's coordinate (still approximate) and the standard pin thank-you went out.
- **Not judged, and why:** 37 leads with `status: lead` and no hold are all Hidde's own sightings (`mine`: Nara, Kyoto, Kyushu, Tokyo, Baarn, September and October). Their photographs are not on this runner, and our own are never auto-published, so they stay as they were.
- qa, preflight (0 problems) and i18ncheck are clean.

## 2026-11-28 reader judge: a reader's holm oak near Rome is live, two more Ciutadella photographs

- **New tree, Guidonia Montecelio, The Holm Oak of La Pietrara** (gdm_001, sighting 281ca01f, sent through the app). The photo looks up a thick holm oak trunk that splits into a fan of upright limbs under a dark crown. It stands in the yard of a small sports ground on Via Robert Baden Powell, beside the clubhouse and the netting of a five-a-side pitch. The pin is confirmed: it is the reader's device fix. The reader gives 1935, and the page says "about 90 years, by a reader's estimate". There is no register entry within 100 m. The access line is honest: the tree is inside the sports ground, so visitors should ask at the clubhouse. This is a one-tree place, so it has no place page. Its texts and three FAQ are written and its names have been looked up. The photo is filed under November, the month of its own date.
- **Barcelona, Ciutadella** (the same Barcelona reader again): sighting ace9ab37 shows the whole Osage orange (bcn_013), with its furrowed orange trunk, yellowing leaves and the park label at its foot. Sighting 36abb76b shows the unpruned London plane (bcn_036) in bronze autumn leaf. Both went on as `add`, so the reader's photo now leads and the old one moves into the strip. The reader's mail goes out under the weekly bundling. The pin read hit an HTTPError again, which changed nothing.
- Nothing else was waiting: 0 open reports, 0 feedback, 0 tips, 0 further photographs, 0 notes left to quote, and nothing late. qa, preflight and i18ncheck are clean.

## 2026-11-28 reader judge: the Japanese Cheesewood of the Ciutadella has its first photograph

- **Barcelona, The Japanese Cheesewood of the Ciutadella** (bcn_037, sighting 01e5144b, the same Barcelona reader again): a daylight shot of the cheesewood, roped off on the park lawn. Its broad dome of glossy Pittosporum leaves stands over a short trunk, far past hedge size, as the story says. The tree had no photograph, and now this one leads. The reader gets the "it's on the page" mail. It is filed under November. The pin stays: it is the register's confirmed coordinate, 10 m from where the reader stood. The pin read hit an HTTPError again, which changed nothing.
- Nothing else was waiting: 0 open reports, 0 feedback, 0 tips, 0 further photographs, 0 notes left to quote, and nothing late. The 37 old `lead` rows are our own accounts. qa, preflight and i18ncheck are clean.

## 2026-11-28 reader judge: the Silk Tree of the Ciutadella has its first photograph

- **Barcelona, The Silk Tree of the Ciutadella** (bcn_008, sighting 9f7e0b7a, the same Barcelona reader as today's plane and palms): a daylight shot of the old silk tree leaning on its metal prop in Parc de la Ciutadella, with the fern-like Albizia leaves and the park's green tree sign at its foot. The tree had no photograph, and now this one leads. The reader gets the "it's on the page" mail. It is filed under November. The pin stays: it is the register's confirmed coordinate, 25 m from where the reader stood. The pin read hit an HTTPError again, which changed nothing.
- Nothing else was waiting: 0 open reports, 0 feedback, 0 tips, 0 further photographs, 0 notes left to quote, and nothing late. The 37 old `lead` rows are our own accounts. qa, preflight and i18ncheck are clean.

## 2026-11-28 reader judge: one Copenhagen photograph, held as an ordinary tree

- One app photograph came in, sent for the Ancient Cycad of the Palm House (cop_002, Copenhagen). It shows something else: a bare broadleaf tree with a leaning, forked trunk outside, at the Botanical Garden's fence on Gothersgade. Verdict `other_tree`, so it became a lead. Judged as a tree of its own, it is held `not_special`: an ordinary garden tree in an ordinary photo, with nothing that stands out where it grows. Under the brief, `not_special` gets no mail.
- Nothing else was waiting: 0 open reports, 0 feedback, 0 tips without a photograph, 0 readers' notes left to quote. No photo went live, so there were no extra photos to apply and no deploy is needed for this run.
- For a later run (rung 3, not the judge's work): cop_002's approximate pin (55.684895, 12.573239) sits at the garden's Gothersgade edge. The reader stood there and photographed an outdoor tree, not the Palm House. The Palm House is about 150 m further north, in the middle of the garden, so the pin should move onto it.

## 2026-11-28 fourth attempt: nothing shipped, same findings

No claims standing, `leads.py --ready` 0, `reader_words.py` 0 waiting, `passcheck.py --pending` only stale or duplicate files plus one taiwan tree. Own research is paused, so there is nothing to dispatch.

## 2026-11-28 third attempt: nothing shipped, same findings

Re-checked: no claims, 0 READY, `enrich.py --next` and `recognise.py --stuck` empty, `reader_words.py` 0 waiting. The only unpublished verified tree is one in taiwan (below the six-tree floor for a write pass). Everything else in `passcheck.py --pending` is stale or a duplicate under another id. health.py rung 2 is still the two open app BUG rows, which are features that need a screen or server table.

## 2026-11-28 later attempt: nothing shipped, same findings

No claims standing. `leads.py --ready` is 0. `enrich.py --next` and `recognise.py --stuck` have nothing. `passcheck.py --pending` lists only stale or duplicate research files (e.g. cyprus, croatia, grazalema, which hold the same trees under other ids), so no write pass is possible. `reader_words.py`: 0 waiting; 4 mail sentences wait for the sender's yes. health.py rung 2 is still the same two open app BUG rows (edit-after-add; Android draft on the account). Both need a server table or a new screen, so they are not a night run's.

## 2026-11-28 12:29 run: nothing shipped

Rung 1: the reader judge is current (backlog empty). I read the four new tree notes (Barcelona plane and palms, Birkerød oak, Aachen linden), found none that meets the hide list, and marked them seen. Rung 2: health.py exits 1 on two open app BUG rows. One is the edit-after-add bug (ESC-2026-11-25). The other is the Android draft bug (ESC-2026-11-26), which needs a draft row on the account. Both need a new server table or screen, and the draft one also needs a SQL paste from Hidde. A night run can't test either, so neither is fixed. Web errors are orange only (`getLayer` on 2 pages, a one-off SyntaxError), below the red threshold. Own research is paused and the shelf has 0 ready to write. Nothing was committed apart from this entry.

So absence from this file is not evidence something was never tried: `grep -ri "<place>" archive/` before concluding a hunt is new. Re-running an exhausted hunt is this project's most repeated waste.
<!-- archive-index -->
## 2026-11-28 reader judge: the Oriental Plane of Placa de la Universitat has its first photograph

- **Barcelona, The Oriental Plane of Placa de la Universitat** (bcn_039, sighting 05b74ec7, the same reader as the palms): a daylight shot of the whole tree in autumn leaf, in front of the university building. The council's sign at its foot reads Platanus orientalis. The tree had no photograph, and now this one leads. The reader gets the "it's on the page" mail. It is filed under November, from the photograph's own date. The pin stays: it is the register's coordinate and already confirmed, and the reader stood about 40 m back. The publish step's pin read hit an HTTPError, which changed nothing here.
- **Plus answer plus:30** ("How can we register a remarkable tree?") is closed `handled`: Add a tree is in both apps and on the contribute page. It is the second "how do I add a tree" after plus:13. **For a session:** check whether Add a tree is easy enough to find (a UX question, so it is not this run's to change).
- Three new tree notes (Barcelona palms, the Birkerød oak, the Forster Linde) are fine, with nothing to hide. They are left for the notes pass to mark seen. No open reports, tips, further photographs or words to quote, and nothing late. The 37 old `lead` rows are our own accounts. qa, preflight and i18ncheck are clean.

## 2026-11-28 reader judge: a reader's photo now leads the Barcelona palms, and their pin moved

- **Barcelona, The Palms of Casa de la Misericordia** (bcn_010, sighting 3d6a6a78): a daylight shot looking up at the four fan palms rising out of the walled courtyard. It is now the lead photograph, and the Commons photo moved to the strip. The reader gets the "it's on the page" mail. Filed under November, the month it was taken.
- **Pin fixed**: the reader's GPS, the Commons photo's geotag and the city register's coordinate (no. 99400454978) agree within about 25 m. Our pin sat on the Carrer d'Elisabets 24 street address, about 80 m off, so it now stands on the register's coordinate (`pin_source` says so). The old note claiming the Commons geotag sat "within 15 m" of our pin was wrong, and it's corrected.
- No open reports, feedback, tips or readers' words. The 37 old `lead` rows in _sightings.json are our own test accounts, which the backlog check leaves out. qa, preflight and i18ncheck are clean.

## 2026-11-28 reader judge: two held, nothing went live

- **Tsagarada, The Plane of Agia Paraskevi** (sighting e3ee25ba): a daylight photo from October of what fits our plane (limbs as thick as trunks, patched bark), but the frame is a man posing, standing up on one of the great limbs. Held as `person`, the same reason we leave extra photos off. The tree keeps its night photos. The reader gets no mail.
- **"Silver Fir in Amsterdam"** (lead b19c636e, four photos): a big conifer that is worth a page, about 20 m tall and 300 cm round by the reader's own figures. But the pin was placed by hand on Dam Square, and the scene and the Italian note don't fit Amsterdam. Held `no_location`, and the standard "where does it stand?" mail is queued on submission 1799.
- No open reports, no feedback, no unjudged tips, no readers' words waiting. qa, preflight and i18ncheck are clean.

## 2026-11-28 fourth attempt, same window: nothing left to ship

- Re-checked in order: claims empty, 0 READY leads, `--pending` lists only stale files or copies of live trees under other ids (not written, hard rule 3), pagegaps shows only the Arnold Arboretum park, recognise and reader_words have nothing. Open APP BUG rows (edit a tree you added; Android draft on the account) need a server table and his yes. Nothing shipped, nothing claimed.

## 2026-11-28 third attempt, same window: last species gaps closed, nothing to ship as trees

- 0 READY leads, claims empty, enrich and recognise have nothing, own research paused. The `awaiting a writer` list is stale or duplicates: every verified file left is either a copy of a live tree under another id or claims an id a live tree holds (hard rule 3), so none was written. Rung 2's two open BUG rows (edit a tree you added; Android draft on the account) need a server table and his yes on personal data, so left.
- Rung 9: 9 more species intros from their own trees (False Kamani, Coolibah, Coast Douglas-fir, Catalpa, Black Tupelo, Bitternut Hickory, American Yellowwood, American Chestnut, African Mahogany). `pagegaps.py` now shows 0 species gaps; preflight 0 problems. Only the Arnold Arboretum park gap is left (waits on the address fix below).
- For Hidde: the stale `data/research/*-verified.json` files (duplicates of live trees under other ids) could be folded into leads marked duplicate and removed; not done by a run, as passcheck says to check by hand.

## 2026-11-28 second attempt, same window: closed 8 app bug rows

- Nothing to write (0 READY leads, 1 unpublished tree in taiwan awaiting a writer), own research paused. Rung 2: 8 of the 10 open APP BUG rows (Feed back-keeps-place, share profile, name and badge taps, photo load order, pull to refresh, grid break, tree card drag) already had their fix and test on main (921f2f8d4, 1d8b21a11, 4df1ea0a3, 6cc3a3380) and the scheduled iOS run on main was green after them; set them `fixed` with those commits. Two stay open: editing a tree you added (a feature, needs his word) and Android DraftTree (needs an Android test run).

## 2026-11-28 night run (10:28 window): page gaps, nothing from readers

- Rung 1 empty (no photographs waiting, reader backlog clear). Rung 2: health shows 10 open app BUG rows in data/code-audit.json, all iOS Swift UI fixes that need an XCTest run on a Mac, so left for a session there; web errors are orange only (maplibre `getLayer`, 2 reports). Own research is paused and 0 leads are ready, so the line had nothing to write.
- Rung 9: 8 species intros written from their own trees and committed (`988f5c958`): American Beech, Apple, Aleppo Oak, Yellow Buckeye, Willow, Torrey Pine, Til / Stinkwood, Scarlet Oak. Fixed a false gap in `pagegaps.py` (Préfargier's intro exists under `la-tene`). Arnold Arboretum is still not written: nine trees (bos_030 to bos_038) carry the address "Arnold Arboretum, Jamaica Plain", which would split the existing intro into two pages.
- Second batch (`bbf15affe`): 9 more species intros (Portuguese Oak, Oriental Cork Oak, Northern Catalpa, Mulberry, Lemon-scented Gum, Japanese Umbrella Pine, Hoop Pine, Green Ash, Great Basin Bristlecone Pine). 17 species intros in all this window; the next gaps are False Kamani, Coolibah, Coast Douglas-fir and the rest at three trees or fewer.
- For Hidde: the Arnold Arboretum address fix (nine addresses to "Arnold Arboretum of Harvard University", then rewrite that intro for 15 trees).

## 2026-11-28 reader judge: the Assistens yews, new lead photos for Skovfogedegen and the Birkerød root oak

- **Live**: copenhagen/cop_057, The Yews over the Henrichsen Grave. A reader sent it as a photograph of the Handkerchief Tree (cop_006), but it shows two tall yews with a fluted red trunk, so it went `other_tree` and was judged as a new tree. They stand over an iron-fenced grave a few steps from the handkerchief tree, and the stone with its portrait medallion and the name Henrichsen is the recognition line. The pin is approximate: the app did not say how this sighting's spot was taken. The source line is the Assistens plant list, which names yew among the cemetery's evergreens. We have no age or girth, and the story asks readers for one. The photo is filed under November, because of the autumn leaves around it.
- **Skovfogedegen** (cop_014): a reader's spring photograph of the hollow trunk, with the Sound behind it, is now the lead photo. The Commons photo has moved to the strip.
- **The Oak on Its Roots in Birkerød** (cop_052): the same reader's winter photo of the root plate is now the lead. Their earlier spring photo has moved to the strip.
- Nothing else was waiting: no reports, no feedback, no tips, and no further photographs to sheet. reader_words had nothing to quote. The congratulation mail for cop_057 waits for the deploy, and this machine had no credentials to send it. qa, preflight and i18ncheck are all clean.

## 2026-11-28 reader judge: two more Birkerød trees, a Cooke Town rain tree, a new lead photo for the Assistens weeping beech

- **Live**: copenhagen/cop_055, The Twin-Stemmed Lime by Birkerød Skole: a big lime splitting low into two trunks, standing over a thicket of saplings. The reader gives 150 years and 400 cm. It has four photographs. copenhagen/cop_056, The Leaning Oak on the Birkerød School Path: an old pedunculate oak with a long low limb over the path. The reader gives 130 years and 250 cm, and it has three photographs. Both came from the same reader as cop_051 to cop_054. Both are pinned at the GPS location of their photographs, beside the public footpath at the northern edge of Birkerød Skole, and the access lines say they are seen from the path.
- **Live**: bengaluru/ben_002, The Rain Tree of Cooke Town: a massive rain tree whose huge limbs bend low over a garden path off High Street, with a stone bench at its foot. The reader gives 60 years and 500 cm. Bengaluru now has two trees, so its intro and meta describe both. The access line says honestly that we have not confirmed the garden's hours.
- **Assistens**: a reader's photograph of the Weeping Beech (cop_007) is now its lead photo: the curtain of hanging branches over the Kapelvej wall. Hans Erik Lund's register photograph has moved into the strip. The same frame, sent twice, was rejected as a duplicate. A photo sent for the Great Maple (cop_008) shows a birch 141 m away, so it went `other_tree`. The birch is held `not_special`: an ordinary birch of modest size. That reason sends no mail.
- Nothing else was waiting: no reports, no feedback, no tips. reader_words had nothing to quote. qa, preflight and i18ncheck are all clean.

## 2026-11-28 reader judge: a copper beech in Birkerød

- **Live**: copenhagen/cop_054, The Copper Beech over the Pavement in Birkerød. A reader sent it from the app with three photographs. They show a big forked beech in a front garden, its crown spreading over the pavement, with the last copper leaves of November. The reader is the same one who sent the three Kajerød trees nearby (cop_051 to cop_053). The pin is the GPS location from their photograph. The access line says the garden is private and the tree is seen from the pavement. Their age (about 100 years) and girth (250 cm) are on the page as their figures. All three photographs are up: the lead, plus two in the strip via reader_extras.py. The photo is filed under November, the month it was taken.
- Nothing else was waiting: no reports, no feedback, no tips. reader_words had nothing to quote. qa, preflight and i18ncheck are all clean.

## 2026-11-28 reader judge: an ambassador for Katikati, and the way to its kauri

- The reader who sent the Kaimai Kauri (katikati/kti_001) wrote back by mail. They work as an arborist in Tauranga and the Western Bay of Plenty, want to be ambassador there and plan to add many historic trees. They are now **ambassador of Katikati**, the only place we have in that area, and are named on the page as their public profile shows. Their second line, that the walk starts from the end of Hot Springs Road, is in the tree's access line and walk FAQ, given as their account. Feedback 1785 is closed `handled`.
- For Hidde: the "Looking after Katikati" welcome mail did NOT go out (this runner has no mail credentials), and no knock sends it later. A session with mail access should run `python3 scripts/ambassador.py --welcome-missing --send`.
- Nothing else was waiting: no queued photographs, reports, tips or other feedback. The 37 open leads in _sightings.json are our own account's. qa source checks were clean, preflight found 0 problems and i18ncheck was clean.

## 2026-11-28 night run, fourth attempt: nothing to ship, state re-checked

- Pulled, no claims, `leads.py --ready` 0, `passcheck.py --pending`: only taiwan has one clean unpublished entry (needs a verify pass, paused); the rest is stale or duplicates of live trees. Open app BUG rows (10) are iOS simulator or Android work. Web error `getLayer` in maplibre is orange, not red. Nothing changed on main.

## 2026-11-28 night run, third attempt: nothing to ship, same state

- Pulled, no claims, `leads.py --ready` 0, `prepare.py --status` names no workable write or verify (own research paused). `reader_words.py`: 0 notes waiting; 4 mail sentences wait for the sender's yes. Health unchanged: iOS failure is runner capacity, open app BUG rows need the Mac simulator. Nothing changed on main.

## 2026-11-28 session: Android build 7 ready for Hidde's phone

- **Build 7 (0.1.0)** is signed from main da723febe in a clean worktree: out/play/ancient-trees-0.1.0-7.aab, which replaces the never-uploaded 11-26 bundle. It carries everything up to 11-27 that the iPhone has: the walk's bugs, the Feed v4, Trending, Discover's new order, the signed-out heart given after sign-in, a tapped pin that no longer moves the map, and taps counted per Discover row. CI on main is green (build, walk, spacing). The release walk (R8) found no crash. The Feed was opened by finger in the release build too: Everyone, Following and Near you, scrolled, no crash. The buttonwalk still fails on its two old test findings, not on the app.
- **Internal testing set up** for Hidde alone (list "Hidde (internal)", his Workspace address), so a build reaches his phone before the 63 closed testers. Join link: https://play.google.com/apps/internaltest/4699336765561121853. Play takes the bundle by drag only (the browser tool uploads 10 MB at most), so **For Hidde: drag the .aab into the open release page, roll it out, and join through the link on the phone.** After his five minutes it is promoted to the closed test, and 7 goes into data/android-releases.json.

## 2026-11-28 night run, second attempt: nothing to ship, checked again

- No claims standing, `leads.py --ready` 0. The 382 "awaiting a writer" are mostly stale research files or entries within 50 m of a live tree under another id (alp, car, cdl, hrv, cyp, grx, sgz and others), so a write pass would only duplicate trees already live. Folding those into duplicate leads and deleting the stale files is a cleanup for a session, not a write pass.
- Rung 2 is unchanged: the open app BUG rows are iOS simulator work, and the Android draft row needs a server-side draft on the account (Hidde's ruling), not a run's change. Nothing was changed on main.

## 2026-11-28 night run: nothing writable, health answered

- Rung 1 was empty (0 photographs waiting). Rung 2: the iOS app "failure" (run 46024472034) was GitHub's macOS runner capacity ("job was not acquired"), not code. A newer run is in progress. Answered with `health.py --answer`.
- The web errors are orange only: `getLayer` in maplibre on 2 reports, 1 page, under the red threshold. Watch it.
- The 10 open app BUG rows (the Feed, profile and tree card ones) need the Xcode simulator, which this Linux runner does not have. They wait for a session on the Mac.
- Own research is paused and `leads.py --ready` shows 0 READY, so there was nothing to write. Prepare.py shelf: 382 trees await a writer, all held by missing photo, pin or recognition line.

## 2026-11-28 reader judge: a spring photograph for the Waldmüllerpark Wingnuts

- **The Waldmüllerpark Wingnuts** (vienna/vie_038) got a second photograph in its gallery. It is a close view into the base of the many-stemmed trunk, with the wingnut's long-leaved suckers around it. It comes from the same reader whose November photo leads the page. It sits behind that lead and is filed under April, the photo's own date.
- The publish step's coordinate read hit an HTTPError again ("pins: could not read coordinates"). That did not matter here, because the row carries the tree's own pin and not a device fix.
- Nothing else was waiting: no open reports, tips, feedback, further photographs or words to quote. The 37 open leads in _sightings.json are from our own accounts. The qa source checks were clean, preflight found 0 problems and i18ncheck was clean.

## 2026-11-27 night run (third retry): nothing shipped

- No product change. No claims standing, READY leads 0, pending verified files all stale or duplicate-by-pin, own research paused. Same state as the two earlier attempts; nothing to write or verify.

## 2026-11-27 night run (second retry): nothing shipped, state re-checked

- No product change. No claims, READY leads 0, own research paused, so no verify or write pass was possible.
- The waiting sighting 64eec98b (Brockwell Oak) is already the live lead photograph; the inbox entry is stale, nothing to apply.
- health.py's iOS "failure" is a run cancelled by newer pushes (46024472034), not a failed test. Open app BUG rows (feed back-scroll, share profile, badge tap, card drag) are Swift and need a Mac runner. The web error `getLayer` (maplibre, orange) needs a session with a browser.

## 2026-11-27 night run (retry, 22:10 window): shelf empty, nothing shipped

- No product change. Resolved a LOG.md rebase conflict (kept both entries). No claims standing; READY leads 0; every unpublished verified file is a duplicate-by-pin or an id collision with a live tree (hard rule 3), not writable. Own research stays paused, so no verify pass.
- Depth lanes empty: reader_words 0 notes (4 mail sentences wait for the sender's yes), recognise --stuck 0. Open app BUG rows need a Mac runner; web error getLayer (maplibre, 2 pages) is orange.

## 2026-11-27 reader judge: a new lead photograph for the Brockwell Oak

- New lead photograph: **The Brockwell Oak** (london/lon_026) now opens with a second reader's sunlit autumn shot (taken 2026-11-23): the whole tree inside its new fence, with Brockwell Hall behind. The first reader's photo from 2026-11-20 moved to the gallery. The reader is mailed.
- The pin was not moved. sightings_publish moved it 37 m south to the photo's GPS fix and marked it confirmed. But the photo looks north at the oak from tens of metres away, so that fix is where the camera stood, not where the tree is. The old pin is back and stays approximate (noted in verify_notes and in sightings-processed's `pin_kept`).
- No reports, tips or feedback waiting. The 37 unheld leads in _sightings.json are all our own account's (`mine`), not readers'.

## 2026-11-27 night run (22:08 window): nothing to build

- No product change. Rung 2: the iOS "failure" (run 46024472034) was no macOS runner acquired, no test ran; recorded with `health.py --answer`. The open app BUG rows are iOS fixes that need a Mac runner to prove; none touched. Web errors orange (getLayer, 2 pages) is under the red line.
- Rung 1: one note on a tree ("amazing species", Lisbon) read and marked seen. The Brockwell Oak photograph waits for the reader judge (it owns photographs; its last run was minutes ago, nothing over 24h).
- Rungs 4 to 9: sourcing paused while mail batches are open, own research paused, nothing in enrich, recognise or reader_words. Nothing left to take.

## 2026-11-27 reader judge: Madison's Constitution-Year Oak

- New tree live: **The Constitution-Year Oak** (madison/msn_006), Vilas neighbourhood, Madison, Wisconsin. A reader sent it through the app, with the phone's own location: a big, deeply ridged oak, and at its foot the 1987 bronze plaque of the National Arborist Association and the International Society of Arboriculture, presented by the Wisconsin Arborist Association, saying it "lived here at the time of the signing of our Constitution". The plaque is its age source (over 240 years). The reader's 250+ years, 4 m girth and white oak are stated as theirs, and the page asks readers to confirm the species. All three photographs are up: the lead and two in the gallery. It is now Madison's oldest tree we map, so the intro, question texts and first FAQ follow it. The access line says we have not confirmed who owns the wooded ground. A Vilas Park master plan is said to mention a bur oak with the same 1987 plaque, but its text could not be read, so the park is not named.
- Further photographs: one more for the Fairchild Oak (ormond-beach/obc_001) went into its gallery. Its reader note was closed in reader_words.py because it reads as copied from a web page, and the dedication is already in the story.
- No reports, tips or feedback waiting.

## 2026-11-27 reader judge: a kauri in the Kaimai Range

- New tree live: **The Kaimai Kauri above Katikati** (katikati/kti_001), a new one-tree place in New Zealand. A reader sent it through the app with a GPS fix at the tree: a pale grey kauri column on a boardwalk, its sign giving 2.7 m across and 12.8 m to the first limb. Their 600 years and 8.5 m girth are stated as theirs. Both photographs are up (lead and gallery); the access line says to check DOC for kauri-dieback track closures. The track is not named: nothing ties this pin to the Tuahu kauri or the Herald's 600-year-old boardwalk kauri.
- No other readers' trees, reports, tips or feedback waiting. The other unheld leads in _sightings.json are our own account's (`mine`), not readers'.

## 2026-11-27 night run, fourth attempt in the window

- Nothing shipped. No claims stand, 0 READY leads, own research paused. The last failed deploy's log shows only the fig description error, already fixed on main. Dispatch gives 403 and a local site build was denied, so the fix is unconfirmed until one deploy runs. For Hidde: `gh workflow run deploy.yml` once.

## 2026-11-27 night run, third attempt in the window

- Nothing shipped. No claims, 0 READY leads, own research paused, and `passcheck.py --pending` shows only stale or duplicate-id files.
- Checked the red web error: its filter ("Transition was skipped") has been in site/src/lib/web-errors-js.ts since 18:00 but is not live, because every deploy since failed on the fig description or was skipped (deploy.yml skips pushes by claude[bot]). So the web error, like the fig fix, waits for the one deploy. Dispatch returned 403 again. For Hidde: `gh workflow run deploy.yml` once.
- The iOS failure and 10 open app bugs need Swift on a Mac; not attempted here.

## 2026-11-27 night run, second attempt in the window

- Nothing written. No claims stood, `leads.py --ready` is empty (0 READY), and own research is paused, so there was no verify or write pass to dispatch. The "awaiting a writer" pile (382) is mostly id collisions and stale files that `passcheck.py --pending` says must not be merged as they are.
- The last real deploy (19:57) failed on the fig description; the fix is on main, but both pushes after it were skipped by the workflow. This run could not dispatch a deploy (HTTP 403 from the integration token). For Hidde: run `gh workflow run deploy.yml` once to put the fix live.

## 2026-11-27 night run (rung 2 only)

- **Fixed:** the 19:39 deploy failed because the Cunningham's fig species page had a 159-character meta description (limit 155). Shortened to 150 and pushed; the push redeploys. Run health still listed Open app bugs (10, 9 found by people), the iOS app run and the web error "skipTransition() called" (16 reports, 13 pages) as red. I did none of those this window.
- My local commit queueing two reader photographs conflicted with the reader judge's Coeur d'Alene work upstream, so I dropped mine. Preflight is at 0 problems.
- No trees were written and the shelf is untouched. The window was started at 19:54 UTC and I stopped early.

## 2026-11-27 reader judge: Coeur d'Alene, Idaho, a chestnut and a beech

- **Changed:** a new reader sent two trees through the app, each with a device GPS fix and a trunk girth. Both are live in a new place, Coeur d'Alene (Idaho), with confirmed pins and their photos filed in November from their own dates.
  - coe_001 "The American Chestnut of City Park". The photo shows two furrowed trunks from one base inside a chain ring with information panels, and OpenStreetMap puts the fix in City Park by the Fort Sherman playground. The city's own Historical, Unusual and Big Trees list names an American chestnut in City Park. I read that through a search summary because the page refused a direct fetch, so the story cites it for the park's chestnut, not for this exact trunk.
  - coe_002 "The Beech of West Sherman Court". The photo shows a big multi-stemmed beech far above a two-storey house. It stands in a private front garden right beside the sidewalk, so it ships with the pin on the street and an honest access line.
  - The reader's girths (432 cm and 122 cm) are in the stories as theirs.
- The two fixes share a latitude to the centimetre, which looked odd. Each one lands on what its photo shows, so they stand. The camera data was stripped from both files.
- Also added coeur-dalene to data/us-states.json (Idaho) and ran city_names.py.
- Nothing else was waiting: 0 queue photographs, 0 open reports, 0 feedback, 0 tips, 0 further photographs, 0 notes to quote. Preflight found 0 problems, and qa source checks and i18ncheck were clean.

## 2026-11-27 reader judge: a first tree in Kenya, in Nairobi's Karura Forest

- **Changed:** a reader sent a tree through the app with the photo's own GPS and no name or note. I looked at the photo. It was taken at night and shows three pale, mottled trunks rising from one base, lit from below, with a café umbrella and string lights in the frame. OpenStreetMap puts the point in Karura Forest's Sigiria section, beside the Sigiria Coffee House and Gate F. That is public forest with an entry fee. The tree is live as nairobi/nbo_001 "The Pale Trunks of Sigiria", a new one-tree place (Kenya), with a confirmed pin and the photo filed in November from its own date. The species is left open and the page asks for it. The Karura history (Wangari Maathai, 1999) is cited to Wikipedia. Kenya is out of focus only for our own research, never for a reader's tree.
- Nothing else was waiting: 0 queue photographs, 0 open reports, 0 feedback, 0 tips, 0 further photographs, 0 notes to quote. Preflight found 0 problems after the null age keys were dropped. qa source checks and i18ncheck were clean.

## 2026-11-27 reader judge: Lake Waikaremoana has an ambassador

- **Changed:** the reader who sent the Giant Rata of the Ngamoko Track replied to our mail. They are happy with the page and said yes to being ambassador of Lake Waikaremoana, from abroad for now. Their account now has the badge (`ambassador.py --grant`; the sync shows their public profile name). Feedback 1768 is closed `handled`. reader_words is closed `--done` for the same row, because the mail is about the offer, not the tree.
- **Not sent:** the standard "Looking after Lake Waikaremoana" mail. This runner has no mail credentials for `--grant`. It is listed by `ambassador.py --welcome-missing` together with Horn-Lehe and Girona, which were already waiting. For a session: `python3 scripts/ambassador.py --welcome-missing --send`.
- Nothing else waited: 0 queue photographs, 0 open reports, 0 tips, 0 further photographs. The 37 open leads are September and October photos from our own accounts. qa source checks were clean, preflight found 0 problems and i18ncheck was clean.

## 2026-11-27 night run (fourth attempt): three more species intros

- Changed in the product: species intros for Cucumber Tree Magnolia, Coast Live Oak and Black Cherry, from our own trees' figures (noindexed under the strict cut, so for the app and Bing). Renamed the Cunningham's Fig file to the slug pagegaps expects, so it no longer reports as a gap.
- No claims, READY pool 0, own research paused, enrich and recognise have nothing. The iOS red run is cancelled jobs (cannot rerun from here); open app BUG rows need Xcode. Remaining gaps: Apple, American Beech, Aleppo Oak and 22 more species, two park pages.

## 2026-11-27 reader judge: two repeat photographs of the Bella di Ceciliano

- Nothing changed in the product. The reader who added the Bella di Ceciliano (arezzo/arz_001) sent two more photographs of it through the app. I looked at both: they are the same frames as photographs x3 (storm sky) and x2 (autumn trunk), which are already in the tree's gallery. Both were rejected as `duplicate`, and the page loses nothing.
- The 37 leads still `lead` in data/leads/_sightings.json are all from our own account (`mine`), so they are not reader work. No reports, feedback, tips, further photographs or unquoted notes were waiting.

## 2026-11-27 night run (third attempt): two species intros, rung 2 answered

- Changed in the product: two species intros from our own trees: Earpod Tree (Fort Lauderdale, Singapore, Oahu, Kauai) and Cunningham's Fig (Yungaburra, Palermo, Hong Kong, Brisbane). Species pages stay noindexed under the strict cut, so this serves the app and Bing. Preflight: 0 problems.
- Rung 2 answered with health.py --answer: the skipTransition web error is already filtered (93cb1b69e, reports predate the deploy); the iOS red run was cancelled jobs, not a failed assertion. The open app BUG rows need Xcode, which this runner lacks.
- READY pool 0, own research paused, no claims standing, nothing else to write. Remaining gaps: Arnold Arboretum and Prefargier park pages, 28 species under four trees.

## 2026-11-27 night run (second attempt): web error fix, nothing else to write

- Changed in the product: nothing visible. `web-errors-js.ts` no longer reports a browser view-transition rejection ("Transition was skipped/aborted"; a faster page change replaced the slower one, nothing broke for the visitor). It was the red web-error row (16 reports, 13 pages). Not built or tested here: no dist in this runner, so qa could not run; the next deploy's checks will.
- READY pool is 0 and passcheck --pending lists only stale or duplicate files (all already published under another id), so there was nothing to write. Own research is paused, so no verify pass was dispatched. recognise --stuck is empty, reader_words has 0 waiting.
- iOS "failure" on 46024472034 is two cancelled jobs (look, test), no failed assertion: runner cancellation after a push superseded it. Not fixed, rerun on the next push. The 10 open app BUG rows already name their tests; fixing them needs Xcode, which this Linux runner does not have.

## 2026-11-27 night run (17:48 window): six species intros, three leads handed back

- Changed in the product: six species intros written from our own trees: Cedar, Eastern Cottonwood, Sweet Gum, Grand Fir, Empress Tree, Elm (data/species/). The Elm page keeps the species open and asks readers. Species pages stay noindexed under the strict cut, so this serves the app and Bing.
- The 3 READY leads (York riverside plane, Sanfins cypress, Leamington lime) went back to leads as `held` with reasons: no source or photo, outside the day trip with no life check, no honest pin. READY pool is 0. `leads.py` calls a lead READY unless a block reason matches, so sourceless leads slip through; worth tightening.
- pagegaps.py shows two false gaps: Laténa (its slug is built from the display name, the intro exists under `la-tene`) and Arnold Arboretum (nine newer trees carry the short park name, one page exists under the long name; fix is the trees' `neighbourhood`).
- Rung 1: no photograph waiting past 24h (reader judge owns the rest); one tree note (Lisbon pohutukawa, "amazing species") read and kept.
- Rung 2, answered: iOS run 46024472034 failed only because GitHub could not acquire a macOS runner (capacity), not a code fault. The web error "Transition was skipped" is already filtered (760cd8f1a, 01:35), the 16 reports are from cached old pages. 10 open app BUG rows (11-26 batch, Feed and map walks) need Swift and a Mac; this Linux runner cannot build or test them, so they stay for a session.
- Nothing refused in the shell.

## 2026-11-27 reader judge: Ohio's former champion cottonwood at Alum Creek

- Changed in the product: a new one-tree place, Alum Creek (Delaware County, Ohio): The Giant Cottonwood of Alum Creek (alum-creek/acw_001), a reader's app tree photographed in snow. Two sources confirm it: Columbus Navigator, which the reader cited, and a 2008 Ohio biodiversity blog that puts it at Cheshire Road and Africa Road, where the reader's pin falls. Their figures (380 in round, 122 ft, 527 points) are given as theirs. The page says it lost its state-champion title after 2020 storm damage, so it claims no current crown. The pin was placed by hand, so it is approximate. The photo is filed in February, from its own date.
- Their second photograph (a person hugging the trunk, square crop) was left off as `person`.
- Breakage, fixed before the push: the first id prefix `alc` was already Alerce Costero's, and the place was missing from data/us-states.json. Renamed to `acw_001` and added Ohio.
- No reports, feedback or tips were waiting.

## 2026-11-27 reader judge: a 600-year downy oak in the Vaucluse, a new Methuselah photograph

- Changed in the product: a new one-tree place, Murs (Vaucluse, France): The Great Downy Oak of Murs (murs/mur_001), a reader's app tree. It is a huge lone oak beside a lane in the fields, in copper autumn leaf. All three of the reader's photographs are on the page. Their figures (600 to 1,000 years, 6 m girth) are given as theirs. The pin was placed by hand, so it is marked approximate, and it includes the 64 m move the reader made while adding it (report 1000160, closed `holds`, no mail since it was their own new tree). No register entry within 100 m. The congratulation mail goes from tell-readers.yml after the deploy.
- Woodside's Methuselah Tree (wdd_001) has a second reader's photograph, a whole-tree view from the trail with its burl and split-rail fence. It now leads the page, and the earlier base shot is in the strip. The reader is mailed through the weekly bundle.
- Breakage, fixed before the push: the first id, `mrs_001`, was already Meares Island's and preflight refused it. Renamed to `mur_001` with its photographs. `city_names.py` found no Wikipedia article for Murs (a disambiguation page), so it is listed as unresolved, a note only.
- No feedback, tips or other reports were waiting.

## 2026-11-27 session: readers' notes and our own photographs now reach Google (live)

- Changed in the product: Google now sees what readers give us. Until today the notes ("From people who stood here") were filled only by a script, so every crawler read the empty card. The build now writes them into the page HTML (102 notes on 100 trees; `scripts/notes_for_build.py` in deploy.yml, output gitignored, so their words stay out of the repo). A new note moves the page's sitemap date. Our own photographs (a reader's, ours, one mailed with permission) now go into the tree page's structured data as ImageObjects, with the day and "by a visitor", never a name. sitemap.xml lists them as image:image: 1,139 photographs on 907 indexable urls. Checked live on le-porge/plane-tree-of-place-saint-seurin and in the sitemap.
- Breakage: the first build failed qa on a reader's own em dash in two notes. Notes now render it as a spaced hyphen, on the web and in the script's redraw (hard rule 3).
- Guarded by qa `check_readers_content_is_in_the_html()` (before the push) and `check_readers_content_is_in_the_built_pages()`.
- Context, from the same session: the November core update ended about 11-24 with no recovery (without our own name in the query, ~65 impressions a day at positions 21 to 90, against ~2,150 before 09-28). The December core update started 11-24 and is still rolling: no index changes until a week after it ends. Pages with reader content went from 5% (10-27) to 17% (11-27) of web tree pages. Laid before Hidde, not built: the hard trim (only pages with reader content on the web), "photographed by a visitor on <date>" visible on the page, and a row linking the newest reader pages from home and city pages.

## 2026-11-27 write pass on the 3 READY leads: none shipped, two held

- Changed in the product: nothing. None of the three leads held enough verified fact to write 150 words without making things up.
- Guimaraes, Mexican Cypress at Citania de Sanfins: set `held`. The only source is an ICNF register row last measured in 2006, with no life check and nothing on the museum grounds' access, and it stands in Pacos de Ferreira, outside Guimaraes' day-trip limit. It needs a verify pass, which waits while own research is paused.
- Leamington Spa, silver pendant lime: set `held`. All we have is the council's one line, "view from the path by the lake". There is no measurement, story or photograph, and no pin that picks the tree out.
- York, Riverside London Plane: left as it was, because it is a reader's (the ambassador's) lead under the closed list. It has a what3words pin but no photograph, source or reason. It stays READY until the ambassador sends a photograph, which a reply could ask for. This is the fifth pass to reach that verdict.

## 2026-11-27 night run (15:28 window): health check only, no trees

- Rung 2. The red web error "Transition was skipped" (16 reports, 13 pages) already has its filter on main (760cd8f1a, 01:35 UTC), so the 24-hour count is pre-deploy reports. Answered in health.py. Two new, smaller errors came in: a maplibre `getLayer` TypeError (2 reports) and "Transition was aborted ... Page already revealed" (matches the same filter).
- The 10 open app BUG rows (iOS Feed, profile and card-drag fixes with tests written, awaiting a build) need Swift, Xcode and the simulators, so this Linux runner left them alone. The iOS scheduled run failed 3.4h ago and the postbox and live sign-in checks are over 26h old (GitHub dropped the schedules). Sessions with the right tools should look.
- Reader inbox empty. Only 3 READY leads (York, Guimaraes, Leamington Spa), under the six-tree minimum for a write pass; own research is paused, so no refill. Nothing published.

## 2026-11-27 reader judge: two cedars at Villa Cagnola, Varese, live

- The same reader who sent the three campus trees added two great cedars in the park of Villa Cagnola at Gazzada, about 5 km south of Varese. Both photographs were viewed, both came with the photo's own GPS, and both are live under Varese: var_006 "The Cedar by the Tower at Villa Cagnola" and var_007 "The Blue Cedar of Villa Cagnola". Each has its further photograph in the strip (reader_extras.py), and both are filed in November from the photograph's own date.
- var_006 is left at genus. The reader calls it a blue Atlas cedar, but the sprays look green and drooping, which may mean a deodar, so the page asks. var_007 is an Atlas cedar, as the reader says and the blue foliage shows. The reader's note is quoted: the villa was the Cagnola family's and is now a Vatican-owned guesthouse, "not always possible to go inside, but it is worth a try". The access lines say the same.
- The Varese texts now count seven trees: intro, meta, question answer and context, and two FAQ answers.
- No open reports, no feedback without a verdict, and no reader notes waiting to be quoted.

## 2026-11-27 session: every Discover row counts its taps, and the daily digest shows where trees are opened

- A new app event, `discover_tap` {row}, fires on every tap on a Discover row, on iPhone and Android. That includes the rows that open a page before any tree: cities, records, lists, islands, countries and species. The tree rows count too (best, trending, visitors, want, more-near-you). So a row is measured even when nobody opens a tree after it. Hidde asked: "sommig rijen gaan niet direct naar een boompagina meet je die ook?"
- The daily digest has a new block above Search: "Where trees are opened in the app". It holds two short tables over the last 7 days, counting only people outside the project: `tree_opened` by `from`, and `discover_tap` by row (`tree_doors_section()` in scripts/daily_digest.py; Hidde: "mss niet over 2 weken melden maar gewoon in dd zetten"). It says "no data yet" until the next app build is in use. The one-off report scheduled for 11 December is deleted.
- Checks: TreeSourceTests (iOS, 3 pass) and TreeSourceTest (Android), both builds, and the digest block run against PostHog (it showed "no data yet", as expected).

## 2026-11-27 session: the iPhone map stays still when a pin is tapped; the red feed test fixed

- Tapping a pin used to slide the whole map up by about 115 points as the card rose, and down again when it closed. Now the map stays where it was: the pin grows in place, and the map only moves when the card would cover the pin. Checked in the simulator (Amsterdam: a pin in the upper map stays put, a low one is brought up, closing leaves everything in place) and with TreeMapPinTapTests. Android has not been checked yet; that is an open row in data/map-parity.json.
- The red iOS CI (BackKeepsPlaceWalk) came from moving People you may know lower: that also moved the break in the signed-out feed grid. Now the later break applies only where the row actually shows. The test passes again locally.
- SignedOutWalk testAmbassadorSeatAsks fails locally on the last green commit too, so it is not from these changes. In CI the Discover sign-in test failed once. If CI goes red on either, it needs a look of its own.
- Not on main: the wider tab bar pill (TabBar.swift in the chain-42 worktree), which waits for Hidde's yes on drafts/design-2026-11-27-tabbar-pill.png.

## 2026-11-27 session: the app now says where every tree was opened from (iOS and Android)

- `tree_opened` carries `from` on both phones. It names the tab, plus the page under the tree when it was not the tab's first screen ("map", "feed", "my-trees", "discover/collection", "feed/person", "discover/tree"). On Discover it names the row instead ("discover/best", "discover/trending", "discover/visitors", "discover/want", "discover/more-near-you"). A few other ways in say what they are: "search", "map/pin" (a pin's card), "nearby" (the nearby banner) and "link" (a web link). Hidde asked for it on every page: "kunnen we dit uberhaupt toevoegen op alle paginas dat we zien waar mensen klikken op bomen wat werkt en niet?"
- How it works: Kit/TreeSource.swift and ui/TreeSource.kt. The page comes from the navigation stack, so a new screen is covered without remembering to say so. The row name comes from the tap, counted without taking the tap from the link (the `countsShare` pattern) and read once within two seconds. Nothing is kept on the device.
- Checks: TreeSourceTests (iOS, 3 pass) and TreeSourceTest (Android, passes), both builds, and ShelvesTest. The first events arrive with the next app build. To read them: `python3 scripts/posthog.py --sql "select properties.from f, count() c from events where event='tree_opened' and properties.from is not null group by f order by c desc"`.
- The privacy page needed no change: it already says the app records that a tree was opened. `from` adds only which screen, nothing about the person or a place.

## 2026-11-27 session: Discover in a new order, without the season photo (iOS and Android)

- Discover now opens with At their best now, nearest first. Then come Trending this month, New from visitors (high up but not first, because it is too much like the Feed), the cities with the ambassador row, Lists with an opinion, Want to visit (full or empty), Tree countries, By species, and the endless "More trees near you". Hidde chose it from the mockup in drafts/design-2026-11-27-discover/ ("Ja, bouw het").
- The big season photo ("Autumn is here") is gone. A simulation for 18 cities showed it only found a nearby tree from September to November in the north. It never did in the south, and in winter it showed trees hundreds of kilometres away (Munich for London). The stock "Trees worth the walk" band went with it.
- The Records (oldest, thickest, tallest) and Tree islands are now tiles in the one Lists with an opinion shelf. Tree islands opens a new list page (Route.Index.islands on iPhone, IndexKind.ISLANDS on Android). The page went from 14 blocks to 9.
- Checks: the iOS build, plus simulator screenshots of the top and the lists in London (drafts/design-2026-11-27-discover/built-ios-*.png). The Android build and ShelvesTest pass. There is no Android screenshot yet, because the only emulator was in use by another session. The next session to run the emulator should look at Discover. The UI test now looks for "Lists with an opinion" instead of "The records".
- Benchmark and PostHog numbers are in CONVENTIONS.md, "Discover after the Feed tab". tree_opened carries no shelf, so no shelf can be measured yet.

## 2026-11-27 session: Genoa cedar, the reader's photo is of our tree; asked whether it is theirs

- The app reader whose photo of the Cedar of Lebanon of Acquasanta (gnv_012, sighting fe75421a) was held `doubt_photo` answered our question. It is the register cedar: their map link lands 13 m from our pin. There is no second cedar to chase.
- What is still unknown is who took the photo: a professional-looking summer frame with no camera data, sent in November. Hidde approved a one-line reply asking whether they took it, sent in their thread through Resend (drafts/reply-reader-cedar-acquasanta-2026-11-27b.md).
- On a yes: the photo leads gnv_012 the same day, and the access and recognition lines ("open square before the church steps") are rewritten to match the wooded slope it shows. On a no: rejected `not_theirs`.

## 2026-11-27 reader judge: a reader's photo now leads the Larger Bunya Pine of Catania

- A reader sent a photograph of the Larger Bunya Pine of Villa Bellini (cat_002), Catania, from 27 m away. I looked at it: a tall araucaria rising far above the palms and holm oaks by the Via Etnea steps, in daylight, with its near-identical neighbour just behind. It went up beside the Commons photograph and now leads the page. The reader's "it is on the page" mail is queued.
- The old Anseman Oak photo from New Orleans (sighting 91f2f869) was left as a waiting lead by this afternoon's session, so I recorded its verdict: held `doubt_location`. It shows another oak in the grove, and its coordinate may be our old pin. The photo was only added to the reader's collection, so there is no submissions row and hold_reply.py could not queue the standard "is it that tree, and where?" mail. The text is in drafts/reply-reader-lead-91f2f869-2026-11-27.md, for a session to send as a one-mail batch.
- There were no open reports, feedback, tips, further photographs or words to quote. The other open leads in _sightings.json are our own `mine` test sightings. qa source checks, preflight and i18ncheck were clean.
- For Hidde: one mail to the New Orleans reader waits in drafts/reply-reader-lead-91f2f869-2026-11-27.md (a session sends it).

## 2026-11-27 session: New Orleans, the lagoon oak was the Anseman Oak (ambassador's correction)

- Our New Orleans ambassador, a photographer of City Park's oaks, wrote that "The Oak by the Bayou Metairie Lagoon" (nol_009) is the Anseman Oak and that our Anseman pin was wrong. His photograph of the Anseman matches the reader's photo, and that reader had sent it for the Anseman in the first place. So nol_009 is retired as a duplicate (its URL redirects to the city page), and its photo and GPS pin are now the Anseman's (nol_002), just off Anseman Avenue east of the lagoon bridge. The story's paragraph about the pin was rewritten, and the city and City Park counts went from 9 to 8 and from 7 to 6.
- The Anseman's old lead photo (sighting 91f2f869, a burly knotted trunk 115 m south) shows another oak in the grove, so it is held as a lead (`doubt_location`) in data/leads/_sightings.json until the tour map names it.
- He sent a scan of City Park's 1999 walking tour of the historic oaks: a numbered map plus the girth and height of 26 named oaks. Its girths and heights are now on the Anseman, McDonogh and Suicide oaks, and its heights on the Dueling and Alferez oaks. It is the map that the open City Park leads in data/leads/new-orleans.json were waiting for (Grandjean, Delgado, Flying Horse and others). The scan is in out/mail-photos/bill/ and is not committed. Pinning those leads from the map is a depth lane for the next run.
- The reply went out on Hidde's "Yes, fix and send" (drafts/batches/reply-bill-guion-new-orleans-2026-11-27.json).

## 2026-11-27 reader judge: a Black Poplar on hold until we know where it stands

- One tree was waiting: a reader's "Black Poplar near Ulverston" sent from the app (sighting 36e8a880). I looked at the photograph. It shows a big, deeply furrowed poplar with a hollow high on the trunk, beside a path on a raised bank, with a cyclist at its foot for scale. It is special enough to go live. But the pin, which the reader placed by hand, is on New Quay Road in Aldcliffe, Lancaster, by the Lune estuary path. Ulverston is 25 km away across Morecambe Bay. A wrong location costs trust, so I held it as `doubt_location`, and the standard mail asking where it stands goes at the next knock (submission 1753). When they answer, it goes live the same run.
- There were no open reports, feedback, tips or words to quote. qa source checks were clean and preflight found 0 problems.

## 2026-11-27 reader judge: nothing new; the Catania fig was already live

- The only waiting item was the reader's photograph of the Villa Bellini fig (cat_001). I looked at it and approved it, then found the 13:25 run had published the same photograph minutes earlier. I kept that run's version. The one thing it had not done was queue the reader's "your photograph is on the page" mail, so this commit adds that entry to data/photo-live-mailed.json (pending, nothing sent twice).
- There were no open reports, tips, feedback, tree notes, further photographs, words to quote or late items. qa source checks, preflight and i18ncheck were clean.

## 2026-11-27 night run (second attempt): nothing shipped, the write shelf is empty

- Changed in the product: nothing. No claims stood. `leads.py --ready` lists one lead, the York Riverside London Plane, and two write passes (the fourth such verdict) found no source, photo or facts, so a story would be invented. It leaves READY once the York ambassador sends a photo or a reason, which a reply mail would ask for.
- `passcheck.py --pending` holds no writable tree: every entry is a stale file, a same-tree duplicate within 50 m (about 50) or an id collision with a live tree (nyc_031 = nyc_130, car_001 = crd_004, wol_001 = wvh_001, among others). The US and UK verified shelf is empty; with own research paused it refills from readers' tips only.
- Not done: the research-file cleanup (deleting stale verified files, folding duplicates into leads). iOS CI red and the 10 open app BUG rows are as in the entry below.

## 2026-11-27 13:25 run: a reader's Moreton Bay fig photo is live; iOS CI red needs a Mac

- Changed in the product: the Moreton Bay Fig of Villa Bellini (Catania, cat_001) had no photograph. A reader's wide daylight shot of the whole tree (buttress roots, limbs, species matches) now leads its page. Looked at the pixels first; the verdict is in data/judgements.json.
- Breakage, not fixed here: ios.yml run 45996140371 (commit 12:08) fails three real UI-test assertions: BackKeepsPlaceWalk.testBackFromATreeKeepsTheFeedWhereItWas (the Feed moved on Back), and SignedOutWalk.testDiscoverWantToVisitAsks (tapping discover-want-signin signed out did not open the sign-in sheet; likely linked to the 11:57 "heart given after sign-in" change). Swift cannot be built or run on this runner, so I did not change that code blind. A session with a Mac should reproduce both.
- Web error "Transition was skipped" (16 reports, 13 pages): the filter that ignores the browser's own view-transition rejections went in at 01:35 today (760cd8f1a), so these reports are from older builds; the line should fall. Not touched.
- Open app BUG rows (10) are Swift fixes already written and waiting for a build; nothing to do from here.
- Postbox and live sign-in checks were over 26 h old; GitHub dropped the schedules, not dispatched from here.

## 2026-11-27 reader judge: a Bologna plane photograph goes on the Minghetti plane

- A reader's app photograph (3aadb77e) sent for the Ginkgo of Piazza Cavour (bol_006) actually shows a London plane: mottled bark, lobed leaves and a tall forked crown in a planted bed. Its GPS fix is 17 m from our Plane Tree of Piazza Minghetti (bol_003, register pin) and 167 m from the ginkgo. The queue row was pointed at bol_003 and applied as `add`, so the reader's photo is now the lead and the Commons photo moved into the strip. The photo is filed under November, its own date. The pin stays confirmed. The publish step's coordinate read hit an HTTPError again, but nothing depended on it.
- Nothing else was waiting: no open reports, tips, feedback, tree notes, further photographs or words to quote, and nothing late in reader_backlog. The 37 open leads in _sightings.json are our own accounts' rows, as in earlier runs. qa source checks were clean, preflight found 0 problems and i18ncheck was clean.
- For a session: sightings_publish.py has no verdict for "this shows another tree of ours". This run edited the queue row's tree by hand before applying. A `tree_id` override on the verdict would make that one step.

## 2026-11-27 third attempt in the 12:08 window, nothing shipped

Claims: none standing. READY leads: the same 3 the write agent refused earlier (York, Sanfins, Leamington), so no new dispatch. `passcheck.py --pending` holds only stale files, id clashes and within-50m duplicates (taiwan has 1 real unpublished, no source change). `reader_words.py` 0 notes waiting (4 mail sentences wait for the sender's yes), `enrich.py --next` nothing, `recognise.py --stuck` 0. `pagegaps.py`: 36 species and 2 park pages missing, but the strict cut keeps them out of Google and they are low value in recovery mode, so left alone. Own research stays paused, so no verify pass or scouting. Nothing left that a run may do.

## 2026-11-27 second attempt in the 12:08 window, nothing shipped

A write-stories agent was dispatched on the 3 READY leads and refused all three: York plane (no source, no photo), Sanfins cypress (in Pacos de Ferreira, outside Guimaraes' 30-minute boundary, access unchecked), Leamington lime (no size evidence, no pin). `leads.py --ready` is fail-open and will keep listing them; each lead needs a reason it recognises (needs a verify pass or a reader's photo with GPS). Leads unchanged. `passcheck.py --pending` is otherwise stale entries only. The web error "Transition was skipped" is confirmed already filtered since 760cd8f1a; it clears as old reports age out. Postbox and livecheck dispatch still need a session (403 here).

## 2026-11-27 night run (12:08 window), rung 2 only, nothing shipped

health.py exit 1: (1) postbox.yml and livecheck.yml are 28h old; `gh workflow run` was refused with HTTP 403 from this runner, so they need a session. (2) Web error "Transition was skipped" (16 reports, 13 pages): the ignore filter in web-errors-js.ts already shipped 2026-11-27 01:35 (760cd8f1a), so these are most likely older builds; check again after the next deploy. (3) Open app BUG rows: the Swift fixes for the 2026-11-26 rows are already on main with their walks (2030fd6f8, 6cc3a3380, 1d8b21a11, c05a3e156) but the rows still say open; they close once the iOS CI walks pass on those commits, which this runner cannot run. The 2026-11-25 row "a tree you added cannot be edited" has no test and no fix, and is a UX decision. No tree work: own research is paused, and reader judging belongs to the reader judge.

## 2026-11-27 session: Android test invitation, wave 6

- **Wave 6** (Hidde: "kun je de 22 mensen uitnodigen?"): the Gmail waitlist sign-ups that never had an Android invite. There were 22 yesterday and 31 by now, most of them Italian, from the TGCom24 days. All 31 are on Play's "Android testers" list (956 to 987, saved and counted before any mail). They got wave 5's text, word for word, through Resend only: 25 at once, and 6 half an hour later (the blind brake allows 25 a run). Batch drafts/batches/android-test-invite-newapp-wave6-2026-11-27.json, built by out/tmp/wave6_build.py.
- The closed test "Alpha" shows 63 active testers. Play Console for the new app: developer account 6289749847935270102, app 4975394642791101357. The 8701… ids belong to the old, disabled account.

## 2026-11-27 session: build 44 ready, and what Hidde found on it

- **Build 44 (1.0.5)** is archived and on Hidde's phone, ready for him to upload: the test chain's fixes, CI green (c05a3e156). Builds 42 and 43 carry the stuck rating ask that blocks collecting: never upload them.
- **Fixed after build 44** (next build, 1e376665f): a heart tapped signed out is now given after the sign-in (it asked and forgot); People you may know sits lower in the Feed and is fetched with its first page, so it no longer pops in.
- **Saved for later, needs Hidde (he said "bewaar dit voor later")**: the email sign-in link opens Safari and only then asks for the app, so a bookmark tapped signed out is lost on the way. Prepared in 783202297: the sign-in and welcome mails carry the eight-digit code (the project's OTP length, measured) beside the button, and the app accepts eight digits. To go live: Hidde pastes supabase/functions/send-email/index.ts into the Supabase dashboard (Edge Functions, send-email, Deploy), checks the code arrives, then a session flips `Launch.emailCode` to true for the next build. Until then nothing changes for anyone.
- **Open, needs a screenshot from Hidde**: on his own profile a tile should show his own photograph. My trees already uses your newest photo of a tree (synced from the account), so which screen shows the wrong one is unknown.
- **Explained, not a bug**: a photo strip mixes photos with a person behind them (name and heart) and Commons or mailed photos (neither).
- **Android caught up** (f797d4095): the signed-out heart is given after the sign-in, People you may know sits lower and is fetched with the Feed, Following reads who you follow when chosen. Unit tests green; not yet walked on an emulator.

## 2026-11-27 reader judge: a reader's photographs now lead the Whistler cork oak in Aguas de Moura

- **aguas-de-moura/agm_001, the Whistler Cork Oak, now has a reader's photograph as its lead** (sighting 45cea55f, verdict `add`). It was sent from 12 m from our pin. The frame looks up from under the crown: one huge cork-barked trunk under vast spreading limbs, the low post fence around it, and the village street and houses behind. Both the species and the recognition line fit. The old photograph moved into the strip. The reader's second frame shows the same tree whole from the lawn, and it is in the strip too (reader_extras). The reader was mailed. The photo is filed under November. As in earlier runs, the pin catch-up could not read coordinates (HTTPError); the move does not depend on it.
- There were no open reports, tips, feedback or words to quote. The 37 other open leads in _sightings.json are our own accounts' rows. qa source checks were clean, preflight found 0 problems and i18ncheck was clean.

## 2026-11-27, session (Hidde: dd, then the cedar)

- **The Genoa cedar's reader gets a question, not a silent hold.** The judge held a reader's photo of gnv_012 as doubt_photo (summer frame, no camera data, a wooded slope where our page says church square). Hidde: "the photo looks like a legit phot", "just ask the person if its that tree or another one and ask for location", then "remember this response". Mailed through Resend; the text is now `hold_reply.py <id> photo_elsewhere "<tree>" --where ... --seen ... --kind ...` (test scripts/test_hold_reply_location.py), and BRIEF_READER_JUDGE.md tells the judge to ask it. A photo kept only in the reader's own collection has no reply row, so the script prints the text for a session to send.
- **A reply sent as HTML only is now read.** Feedback 1715 ("no plain-text part") was Andrea's question about the ambassador role; `outreach_inbox.body_of()` falls back to the HTML part (scripts/test_body_of_html.py). Their answer had already gone out 11-26.
- Checked and already done: the spreading web error (5f79931a8), the failed scheduled iOS run (fixed by the Feed back fix, green 06:46), Palheiro's Play address (on the testers list 11-26).

## 2026-11-27 session: a tree you add is named after its own town, not "near" one of ours (both phones)

- **Product (next app builds, iOS and Android):** a tree a reader adds more than 5 km from our nearest place no longer becomes "A tree near Ripon" with a link to Ripon on its page. The phone names the town it stands in ("A tree in Knaresborough"), and a name we made follows it; a name they typed is never touched. Older trees named "near X" are renamed the next time their page opens. Our place is still named and linked within 5 km ("in Nara").
- **Why:** a Plus answer of 2026-11-22 (anonymous, so no reply is possible): "I'd like to add trees in my hometown of Knaresborough but this doesn't seem to be possible. The app thinks I'm in Ripon". Adding was possible; the "near Ripon" label made it look as though it was not. Recorded as ESC-2026-11-27-a-tree-you-add-up-to-30-km-from-one-of-o. Plus answers are read by nobody but the digest, so this sat for five days.
- **Typed Plus answers now reach the reader judge** (Hidde: "Ja, doe het"): `feedback.py --open` lists them as `plus:<id>`, `reader_poll.py` wakes the judge on a new one, and reader_backlog rings when one waits a day; BRIEF_READER_JUDGE.md says how to judge them (anonymous: a bug, a filed idea, a tip, or nothing; never a reply). The 13 waiting were judged in this session: Knaresborough is the bug above; notifications near a tree (asked twice) and camera species identification went to PRODUCT_TODO.md "Ideas from readers"; the rest were already possible or needed nothing.
- **For a session:** a reader asked where the Major Oak is. It is a blocked lead (data/leads/_tree-of-the-year.json), declared dead in spring 2026 but still standing; the standing-dead exception of 2026-11-17 (the Ochi chestnut) may let it ship with a photograph of it standing and a page that says plainly it is dead.
- Tests: MyTreesTests `theTownThePhoneNamesReplacesTheNearestPlaceOfOurs`, `thePlaceIsOursOnlyCloseByAndNothingBeyond`; Android CollectRulesTest `theTownThePhoneNamesReplacesANameWeMade`. Both green.

## 2026-11-27 reader judge: a reader's photograph now leads the Villa Torlonia cedar in Rome

- **rome/rom_018, the Cedar of Lebanon of Villa Torlonia, has a reader's photograph as its lead** (sighting f19ad4b8, `add`). It was sent from 19 m from our confirmed pin. It shows a broad cedar with many stems rising from one massive, flared trunk. It stands on the lawn below the Casino Nobile, with the white columns and a stone urn on the balustrade in frame. That is the setting the recognition line names. The species (tiered sprays of short needles) and the description both fit. The Commons photograph moved into the strip. The reader was mailed. The photo is filed under November (the photograph's own date). The pin catch-up could not read coordinates (HTTPError), but the pin was already confirmed.
- There were no further photographs, open reports, tips, feedback or words to quote. The 37 other open leads in _sightings.json are our own accounts' rows, as in earlier runs. qa source checks were clean, preflight found 0 problems and i18ncheck was clean.

## 2026-11-27 reader judge: a walking sweet chestnut in Betchworth Park, Dorking, live from a reader's photograph

- **Live: dorking/dkg_001, the Walking Chestnuts of Betchworth Park** (sighting e88184b7). This is a new one-tree place in Surrey, so it gets no place page. The photograph shows a massive sweet chestnut with deeply ridged bark splitting into heavy stems, a burr at its foot and a low limb arching towards the ground. It is clearly special. The reader's note explains how "walking" chestnuts layer, and the story quotes it. Their age (the 1500s, about 500 years) and girth (700 cm) are on the page as theirs. Dorking Museum is the source for the parkland's old sweet chestnuts and the 1448 emparkment. Mole Valley council is the source for the public footpaths round the golf course. The access line says to keep to the paths and that we have not checked how close a path passes this trunk.
- **Pin**: the reader placed it by hand, so it is `approximate` (`pin_source` "reader's hand-placed pin"). The photo is filed under November for its autumn leaves. There were no further photographs. city_names.py was run for Dorking.
- No open reports, tips, feedback or words to quote. The 37 other open leads are our own accounts' rows. qa source checks were clean, preflight found 0 problems (after trimming the meta to 155 characters) and i18ncheck was clean.

## 2026-11-27 reader judge: the giant rata at Lake Waikaremoana and two Villa Fabbricotti trees in Livorno, live from readers' photographs

- **Live: lake-waikaremoana/wkm_001, the Giant Rata of the Ngamoko Track** (sighting 24fdccb3). This is a new one-tree place in New Zealand. The reader sent four photographs. They show a huge braided northern rata behind a viewing-platform rail, with the Department of Conservation sign beside it. The sign gives 13 metres around the base and 800 to 1,000 years. Those figures are on the page as the sign's (`girth_cm` 1300, `age_basis` source). The other source is DOC's Ngamoko Track page, which names the giant rata a short detour from the start. The pin is the photo's GPS fix, so it is `confirmed`. Two further trunk photographs are in the strip. The photograph of the sign alone was left out as `no_tree`; its text is now a source line.
- **Live: livorno/lio_001, the Cedar of Villa Fabbricotti, and lio_002, the Magnolia of Villa Fabbricotti** (sightings f466425f and c4a19bef, one reader, sent as "a tree near Pisa"). Both GPS fixes fall in Parco di Villa Fabbricotti, Livorno (OpenStreetMap). The cedar is wide and lopsided, with drooping tiers on a lawn of its own. The species is left as Cedrus sp.; it looks like a deodar and the page asks. The magnolia is a mature southern magnolia under a broad dome. The park's history comes from Regione Toscana's Villa Fabbricotti page: Micheli redesigned it for Fabbricotti after 1881, the city bought it in 1936, and the page names cedars and magnolias among its trees. Livorno is a new place with two trees.
- All three photographs are filed under November, from the photographs' own date. city_names.py was run for the three new places. No open reports, tips, feedback or words to quote. The 37 other open leads are our own accounts' rows. qa source checks were clean, preflight found 0 problems and i18ncheck was clean.

## 2026-11-27 reader judge: a pillar-rooted fig in Hervey Bay, Queensland, live from a reader's photograph

- **Live: hervey-bay/hbq_001, the Pillar-Root Fig of Boat Harbour Drive** (sighting bddb92b5). This is a new one-tree place, so it gets no place page. The photograph shows a broad fig standing on braided grey trunks, with a separate pillar root holding up a level limb. It is clearly special. The species is left as Fig (Ficus sp.) and the page asks readers what it is. The reader gave no species, age, girth or note.
- **Pin**: OpenStreetMap puts the reader's GPS fix on the garden edge of The Anchorage Lifestyle Resort, a private residential village, about 30 m from Boat Harbour Drive and its bus stop. A fig that size so close to the road can be seen from it. So it ships view-only (hard rule 10), with the pin moved 29 m onto the roadside: `approximate`, `pin_source` "viewing place", with the reader's fix kept in the note. The access line says to look from the road and not walk in. The photo is filed under November, from the photograph's own date. A passer-by stands at the right edge of the frame, seen from behind.
- No open reports, tips, feedback, further photographs or words to quote. The 37 other open leads are September and October rows from our own accounts. qa source checks were clean, preflight found 0 problems and i18ncheck was clean. A NOTE remains: city_names.py has not yet looked up Hervey Bay in other languages.

## 2026-11-27 reader judge: a second photograph of the Kyoto Gyoen muku, and its pin now follows that photo's GPS

- **Live: kyoto/kyo_019, the Twisted Muku of Omiya Gate** has a second photograph, in the strip behind the lead (sighting f17b77f9, taken April 2026, filed under April). It shows the pale, twisting trunk rising over the park's stone wall with its roots on the kerb, exactly as the recognition line describes. It was shot from across Marutamachi-dori through a window, and the streaks on the glass keep it out of the lead spot.
- **Pin**: the photograph carries its own GPS (35.017586, 135.76033). That is on the wall line, 59 m from the spot the reader's report placed in words this morning. It is now `confirmed`, `pin_source` "reader GPS fix". This follows Hidde's 2026-11-17 rule that a photo's GPS beats a pin moved by hand. The fix agrees with the report (the south wall of Gyo-en, north of the road), only more precise.
- The coordinate read in the publish step hit an HTTPError ("pins: could not read coordinates"). This did not affect the move above, which came from the queue row. No open reports, tips, feedback, further photographs or words to quote. The 37 open leads in _sightings.json are September and October rows from our own accounts. Their photographs are not on this runner, so none were judged. qa source checks were clean, preflight found 0 problems and i18ncheck was clean.

## 2026-11-27 reader judge: the Kyoto Gyoen muku's pin moves off the road onto the park wall

- **Live: kyoto/kyo_019, the Twisted Muku of Omiya Gate**: its pin moved about 120 m north (35.017 to 35.0181, same longitude). A reader wrote (report 1000159) that the tree is "slightly more north across Marutamachi-Dori on the southern wall of Gyo-en". Our old pin was the Sudajii's (kyo_016) estimated gate-area point, and it sat on Marutamachi-dori itself. The new spot is from their description, so it is now `approximate`. It had been marked `confirmed` under a 2026-10-05 "reader GPS fix" label, but its own verify_notes say the app recorded our pin, not the phone's. Overpass was at capacity, so the street's position comes from Marutamachi Station's known coordinate, not from OSM geometry.
- The reader wrote words of their own, so the report closed `holds` with no mail. A suggested reply is in drafts/reply-reader-1000159-2026-11-27.md for Hidde. kyo_016 still sits on the old point and was not touched (nobody reported it).
- Nothing else was waiting: no queued photographs, tips, feedback, further photographs or words to quote, and nothing late. The 37 open leads in _sightings.json are from our own accounts. Preflight found 0 problems, the qa source checks were clean and i18ncheck was clean.

## 2026-11-27 reader judge: Skarseken in Gothenburg has its first photograph, and its pin follows the reader

- **Live: gothenburg/got_002, Skarseken** now has a lead photograph. Until now it had none. A reader sent it from the tree's page (sighting 53ef0785): a heavy oak with ivy up the trunk and a bare winter crown, standing alone between houses with a white house behind it. The species and the recognition line both match. It is filed under November, the month the photo was taken.
- **Its pin moved 331 m** to where the same tree's reader put it this morning (report 1000158). Our old pin was only an estimate: the city's naturminne decisions give no coordinates. The new spot is still `approximate`, since it was placed by hand and is not a GPS fix. It does not land on any of our other Örgryte oaks. They got the standard pin thank-you.
- Nothing else was waiting: no tips, feedback, notes, further photographs or words to quote, and nothing late in reader_backlog. The 37 open leads in _sightings.json are still from our own accounts, so none were judged. Preflight found 0 problems, the qa source checks were clean and i18ncheck was clean.

## 2026-11-27 Night run, second attempt: nothing shipped

The three READY leads (york plane, guimaraes cypress, leamington-spa lime) cannot be written: no sources, no pin or no photo, the cypress is in Paços de Ferreira 15.7 km out. leads.py counts them READY without checking sources or a pin; worth tightening. The fix commit's deploy runs show skipped and this run cannot dispatch deploy.yml (403), so the red build is unconfirmed until the next push or a session dispatches it. Web error AbortError skipTransition and the open app BUG rows are untouched.

## 2026-11-27 Night run: the site build was red, fixed

Rung 2. Build and deploy had failed since the National Arboretum maple went live: species "Maple" carried two Latin names (Acer pubipalmatum in Washington DC, Acer pycnanthum in Higashiomi), which hard rule 9 refuses. The DC tree is now "Downy Palmate Maple (Acer pubipalmatum)" (common name is a translation of the epithet, a better English name may exist). Preflight clean, pushed; the next deploy should go green, which also clears the smoke test. Not touched: the web error "AbortError: Transition was skipped" (16 reports, 13 pages), the open app BUG rows and the iOS schedule failure; own research is paused and the reader judge handles readers.

## 2026-11-27 Android night walk: every button on every screen, unattended

What changed in the app (Android):
- The locate arrow on the map no longer takes a tap while it has faded to nothing (a full sheet, an open tree card): it leaves the screen instead of standing there invisible for a finger and TalkBack.
- The Feed and Every photo visitors sent keep their posts as one list swapped whole, so a page arriving while the screen reads it can no longer throw (ConcurrentModificationException, seen in the walk).
- A Supabase request that is cancelled stays cancelled instead of pretending it failed.

What changed in the test street:
- ButtonWalk.kt walks the Feed too (the iPhone's list had it), reads the screen on the app's own thread (reading from the test thread threw "performMeasureAndLayout called during measure layout"), waits until the old screen is gone before each launch, names a stall after 30 s with every thread's stack (logcat tag ButtonWalkStall) instead of waiting for ever, gives the root cause of a failure, and skips the locate arrow only when location is allowed (it then moves only MapLibre's camera, which the tree cannot show; CI's emulators have no permission, so there it is tapped and must ask).

Result on a private API 37 emulator, one screen at a time: 28 of 32 green; unit tests 154 of 154.

Morning follow-up (Hidde: "Yes, go ahead"):
- The Feed's "dead" controls were the test clock, not the app: a photo that likes on a double tap fires its single tap after the 300 ms wait for a second one, and under Compose's test clock that wait only moves while frames are asked for. The walk now moves the clock past the window after every tap; FeedTileWalk.kt (new) proves a tile and a title open their tree. Feed, Discover and visitors walks green, signed in and out.
- The launch Android never finished on the API 37 emulator stays an emulator matter (app idle, focus never given). scripts/android_walk.py now runs ButtonWalk one screen at a time with its own limit (20 min a screen, 40 for the other walks together), runs such a screen once more and says so, and never again waits for ever on one call.
- Why the first run sat at 0 of 29 for 2.5 hours: one Gradle call with no limit per test, the Mac asleep, and a second session driving the same emulator. My own scripts skipped scripts/emulator_lock.py, which android_walk.py takes; long walks go through android_walk.py from now on.
- The full run afterwards (android_walk.py, 3.5 h): ButtonWalk green on 15 of 16 screens, Discover once more on its own green signed in and out. The other failures were the emulator, not the app: it had lost its network (no DNS), so the Feed never loaded and FeedTileWalk waited in vain, and one stuck launch took eight FlowWalk tests down after it; each of those is green on its own. I started it again with a fixed DNS (-dns-server 8.8.8.8); android_walk.py does not start emulators itself. One real flaw in the test: the title click found the first text with the tree's name, which can stand where no touch lands; the title under a tile now carries its own tag (feed-tile-title) and the test clicks that. FeedTileWalk 3 of 3.

## 2026-11-27 reader judge: a giant fig in the Big Scrub rainforest near Alstonville, NSW

- **Live: alstonville/aln_001, The Moreton Bay Fig of Victoria Park.** A reader sent it through the app (sighting c428c962), and it is a tree we do not map; no tree of ours stands within 80 km. The photograph looks straight up a huge buttressed fig trunk laced with vines, with a thin palm rising beside it, in daylight and colour. Its GPS fix from the phone falls inside Victoria Park Nature Reserve, about 200 m from the reserve's Wikipedia centroid, so the pin is confirmed. The NSW National Parks page is the source that names the reserve. The species, the age (500 to 1,000 years) and the girth (15 m) are the reader's, and the story says so. The photo is filed in November from its own date.
- Alstonville is a new place with one tree, so it gets no place page yet. Its intro, question texts and three FAQ are written for when it grows. No register entry or encyclopaedia article stands nearby. The congratulation mail waits for the deploy.
- Nothing else was waiting: no open reports, tips, feedback, further photographs or notes to quote, and nothing late in reader_backlog. Preflight 0 problems, qa source clean, i18ncheck clean.

## 2026-11-27 reader judge: a maple in autumn colour at the National Arboretum, and the Yamaki Pine's new lead photo

- **Live: washington-dc/wdc_044, The Flame-Leaved Maple of the Arboretum.** A reader sent it through the app (sighting e53755b2), a tree we do not map. It is a slender maple at the U.S. National Arboretum in full scarlet and orange autumn colour. Their second photograph shows the arboretum's own label held up on its stem, reading "Acer pubipalmatum, maple", so the species comes from that label. The reader placed the pin by hand, so it is approximate and the story says the pin marks the area. Both photographs are up, filed in November from the photo's own date. It is under the closed list: a tree blazing in autumn colour in its setting counts as special.
- **The Yamaki Pine (wdc_025) has a reader's photograph as its lead.** It came from the same reader (sighting 7941c650): the bonsai on its plinth at the Japanese Pavilion in clear daylight, species and description matched. The Commons picture moved to the strip. The reader's fix was 9 m from our pin, so the pin is now confirmed. The congratulation mail for wdc_044 waits for the deploy.
- Nothing else was waiting: no open reports, tips, feedback or reader words to quote. Preflight 0 problems, qa source clean, i18ncheck clean.

## 2026-11-27 reader judge: a hollow cedar at Shannon Falls, Squamish

- **Live: squamish/sqm_001, The Hollow Cedar of Shannon Falls.** A reader sent it through the app (sighting 43dd1d12). It is a western red cedar standing alone on the picnic lawn of Shannon Falls Provincial Park, its trunk open at the foot in a hollow that the reader says "a child can walk through". The photograph is daylight and colour, and its own GPS puts it inside the park (OSM relation 8634839). The pin is confirmed, and the photo is filed in November from its own date. Squamish is a new one-tree place, so it gets no place page yet. Its intro, question texts and three FAQ are written for when it grows.
- No register entry and no encyclopaedia article stand nearby. Every fact on the page is either visible in the photo or the reader's.
- Nothing else was waiting: no open reports, tips, feedback, further photographs or notes to quote, and nothing late in reader_backlog. Preflight 0 problems, qa source clean, i18ncheck clean.

## 2026-11-27 night run: web error cleared, iOS red left for its next run

- **Rung 2.** The web error "AbortError: Transition was skipped" (16 reports, 13 pages) is the browser rejecting its own cross-document @view-transition when a visitor leaves a page mid-transition. No script of ours holds those promises, so web-errors-js.ts now ignores "Transition was skipped/aborted". Preflight 0 problems.
- **iOS red, not fixed.** The 22:27 run failed `BackKeepsPlaceWalk.testBackFromATreeKeepsTheFeedWhereItWas` (Feed tile 152.5 before Back, 55.5 after). It started with 92cfabb94, which touched Feed.swift, TreeDetail.swift and ReviewPrompt.swift. This runner has no iOS, so I did not guess at a fix. The run in progress at 00:55 UTC on main will show if it still fails. If it does, a session with a Mac should look at the Feed's scroll position after Back first.
- 10 open app BUG rows in data/code-audit.json were not taken: they need the iOS toolchain to verify.

## 2026-11-26 reader judge: the La Salle larch is older than 500 years, by its reader

- **Live: la-salle/lsa_001, The Bearded Larch of the Col du Bard Path** now says "more than 500 years, by a reader's estimate". Before, it said "under 500". The reader who sent the tree wrote in report 1000157 that they had typed it wrong ("more than 500 yo"). The age line, the story and the question context changed. There are no translations of the page, and verify_notes records the correction.
- The report carried the reader's own words, so it was closed `holds` and no mail went out. The digest shows Hidde their words. No draft was needed, because the page now says what they meant.
- Nothing else was waiting: no photographs in the queue, no tips, no feedback, and no new notes to quote. The 37 open leads in _sightings.json are all from our own accounts (`mine`), so none were judged.

## 2026-11-26 reader judge: two Brockwell Oak photos were repeats

- **Nothing changed on the site.** The same reader sent two Brockwell Oak photographs again as separate sightings (b6f9f719, ad15692d). They are the same pictures as further photographs 1 and 3 from sighting ad2b3c75 (the crown under grey cloud, and Lambeth's sign). Both are already in lon_026's gallery, so both were rejected as duplicates and given verdicts in judgements.json. No mail went out.
- That reader's note on the oak ("partially fenced off … still had some leaves. Not many acorns") was read and kept, and marked seen.
- Nothing else was waiting: no open reports, tips or feedback, and nothing late in reader_backlog. The 37 open leads in _sightings.json are still from our own accounts (`mine` and the Nara tests), so none were judged.

## 2026-11-26 session: the whole test chain over the next iPhone build (Hidde: "de hele teststraat")

- **Walked** current main (after build 43: Feed, card designs, map links) on an iPhone 16 Pro Max with the test account (pass 1) and on the SE at XXL and offline (pass 2); notes out/tmp/walk-ios-1126-pass1.md and -pass2.md. appsweep on iOS 26 (the SE swept; the 17 Pro did not boot under the load).
- **Fixed, 92cfabb94**:
  - **The rating ask blocked collecting.** Back from the third tree page fired it while the page was leaving; iOS never showed it, the sheet stayed "open", and the camera, Collect and Add a photo did nothing until the app was killed. That is every new user after their third tree, and build 43 carries it: **do not upload build 43**. Now the ask waits until the page has left, and one that never shows is let go and kept for the next pause (ReviewPromptTests). Seen working on the SE: the ask showed, then the camera opened.
  - Feed > Following reloads who you follow on return and on refresh.
  - Offline, a tree with a photograph no longer says "No photograph yet" or "No notes yet" ("The notes did not load. Check your connection and come back.").
  - At XXL: another person's follower counts stack instead of "0 follow..."; the place line under a tree's title puts the verdict below. Both looked at on the SE.
  - Baarn's FAQ said 5.52 m for the Pekingtuin oak; now 5.9 m, as its story and the register.
- **Not confirmed**: Find people missing Helia C. (the server returns her as the test account; the walk could not type in that field). Back to Discover from a Trees-lane result coincided with the stuck ask and is likely the same cause.
- **Nits left** (walk notes): no backdrop under the clock on Discover and Feed when scrolled; email sign-in on the SE hides its button under the keyboard; the hearts list's close X is faint; "Location off" with permission but no fix; search bolds to the end of the name; Collected and species filters leave the map elsewhere; a dropped pin under the chips; short visitor names cut; records shelf "Tallest" without a figure; Settings > Sources says every photo is openly licensed.

## 2026-11-26 reader judge: a reader's Brockwell Oak leads its page, and the council's new fence is on it

- **Live: london/lon_026, The Brockwell Oak** now leads with a reader's own photograph. It shows the whole oak in late autumn leaf: the squat, burred trunk alone in open grass inside a new chestnut-paling fence. The Commons photo moved to the strip. All three further photographs went up: the crown from the other side, the trunk behind the rails, and Lambeth's sign on the fence. The photo is filed under November. The pin did not move, because the app sent our own pin, not a GPS fix. The reader was mailed.
- **Corrected from the reader's photograph of the sign**: Lambeth has fenced off the root area after the oak lost three large branches in recent years, and the sign gives its age as around 600 years (inside our 500 to 700 band). The story no longer says people picnic in its shade. The access line says the tree is seen from outside the fence, and the recognition line names the fence and sign. The sign is listed as a source. The page has no translations to follow.
- No reports, tips or feedback waiting. The 37 open leads in _sightings.json are still our own accounts' (`mine` and the retired Nara tests), with no files on disk, so none were judged.

## 2026-11-26 reader judge: the Kvam oak's pin follows a reader

- Kvam (kvm_001, the Old Oak at Tolo): a reader moved its pin 68 m west (report 1000156). Our pin there was itself placed by hand, not a GPS fix, so their spot stands, still approximate. They got the standard pin thank-you.
- One new note on the Act of Union Beeches of North Berwick Law, from someone who visited today and saw two more old beeches toward the Mill Burn. It needed no hiding and was marked read.
- No photographs, trees, tips or feedback waiting from strangers. The 37 open leads in _sightings.json are all from our own accounts (`mine`, or the retired Nara test photos), which the judge never takes. Their files are not on disk.

## 2026-11-26 Session: no photos since 17:17 was quiet, not broken; Amsterdam sighting closed

- Hidde asked whether the judge had stalled. It had not: reader-judge runs every 10 minutes, all green, and PostHog shows no `sighting_recorded` since 16:00 UTC (fired on the phone before upload), while 15 to 24 people an hour used the app. A quiet day (17 photos against 27 to 80).
- Sighting 3c544597, passed on by runs for eight days as "for the reader judge", was Hidde's own account's photo (`mine`), which the judge never takes. Closed on his word ("Mag weg") in data/leads/_sightings.json; the inbox is empty.
- supabase/feed-live.sql had been overwritten locally with one letter; restored from git (the live function was untouched).

## 2026-11-26 Map: a tree card dragged down closes, the menu stays

- On the map, a tree card dragged down landed on the list's lowest stop, where the tab bar steps away (Hidde: "dan gaat het hele menu weg"). It now closes back to the list with the tab bar, as Google Maps and Airbnb do; the bar stop stays for the results list. iPhone and Android; TreeCardDragWalk fails without the fix and passes with it.

## 2026-11-26 reader judge: one pin report closed, one sighting left

Report 1000155 (Padua, the Certosa di Vigodarzere plane): a reader dragged the pin 41 km from Vigodarzere into the countryside near Conegliano. They wrote nothing and sent no photo, and the story's site is 6 km north of Padua. That is a move into open country with no reason, so I closed it `holds`, kept our pin and sent no mail. Sighting 3c544597 (Amsterdam, near Stationsplein, "not sure which tree") is left for the next run: its photograph is not on disk, so I could not judge it without seeing it. It is also flagged `mine`, our own account's photo. No new tips, feedback or reader words waiting.

## 2026-11-26 night run (seventh attempt): nothing to ship

Pulled, no claims standing. The READY leads are still the same 3 (york, guimaraes, leamington-spa), already judged unwritable. The 382 "awaiting a writer" are stale files or duplicates of live trees, and own research is paused. Nothing claimed or shipped.

## 2026-11-26 night run (sixth attempt): nothing to ship

Pulled, no claims standing. 3 READY leads (york, guimaraes, leamington-spa) still unwritable. `passcheck.py --pending` shows only stale files, duplicates of live trees under other ids, and id clashes with live trees (alpujarras, cardiff, coimbra, croatia, cyprus and others), so no write pass is safe. Own research is paused. reader_words has 0 waiting, 4 mail sentences await the sender's yes. The Amsterdam sighting 3c544597 belongs to the reader judge. Nothing shipped.

## 2026-11-26 night run (fifth attempt): nothing to ship

Same walk again: no claims, 3 READY leads still unwritable, `enrich.py --next` and `recognise.py --stuck` empty, reader_words 0 waiting, the 382 "awaiting a writer" files are stale or duplicates. Health red only on open app BUG rows (iOS fixes needing the Mac build). No tree added, nothing claimed.

## 2026-11-26 night run (20:50 window): nothing to ship

Rung 1: no reader backlog; one new tree note (North Berwick Law beeches, a visitor's own observation) read and left up, marked seen. The Amsterdam sighting 3c544597 is the reader judge's. Rung 2: health red only on open app BUG rows (9, 8 found by people); they are iOS fixes from Hidde's session awaiting build and CI, the Android draft row needs an account-side table (his yes), the Tortworth edit row is a feature. None is a Linux runner's. Own research paused; the 3 READY leads (york, guimaraes, leamington-spa) are the ones earlier attempts today found unwritable; reader_words has nothing waiting. Stopped without committing trees.

## 2026-11-26 night run (fourth attempt): nothing to ship

- Re-checked in order: no claims, READY 3 (unwritable, as judged), own research paused, reader photo 3c544597 not on disk so cannot be judged blind. Open app BUG rows are Swift/Android fixes already carrying tests, needing the Mac build; the Linux runner cannot verify them. Web errors orange only (1 page each). Nothing started, nothing claimed.

## 2026-11-26 night run (third attempt, same window): nothing to ship

- Pulled, claims none, READY still 3 (york, guimaraes, leamington-spa), verified shelf still stale or duplicate ids. iOS red on main was appfit's header padding, fixed by a later commit; its rerun was still building. One reader photo of an unmapped Amsterdam tree (3c544597) waits for the reader judge.

## 2026-11-26 night run (second attempt, 19:2x window): nothing to ship

- Claims: none standing. READY leads: 3 (york, guimaraes, leamington-spa), already judged unwritable by the earlier write pass; the other 382 "awaiting a writer" are stale duplicates of live trees (same coordinates, different ids), not writable. Own research paused, so no verify pass.
- iOS red is the Dependabot branch (supabase-js bump); main's run was still building. Open app bug rows each carry their test already, waiting on that run. Web errors orange (`null has no property 'save'`, 4 new types), under the red bar.
- Left for a session: the duplicate-id verified files in data/research/ (alpujarras, cardiff, croatia, cyprus, grazalema...) need folding into leads marked duplicate; "a tree you added cannot be edited" (bug row, no test yet) is a feature, his call.

## 2026-11-26 session: one map on the website, steps 1 to 3 live (Tokyo first)

- **Tokyo's page is the map opened on Tokyo.** The cross beside share, or dragging the map off Tokyo, turns the panel into the map's trees in view and the address into /explore#map=..., with no page load; Back brings Tokyo back. Only Tokyo so far (`ONE_MAP_CITIES` in site/src/lib/one-map.ts); every other city page is unchanged.
- **A city picked in the search on /explore or Tokyo's map flies there**, then opens that city's page at the view it landed on, behind the browser's own cross-page fade (Hidde: "A, fly and fade"; site/src/lib/fly-to-city-js.ts). Swapping the panel in place would have meant rewriting a dozen page scripts on Google's landing pages; he chose this over that.
- Breakage on the way: Tokyo's map drew no trees for one deploy (the list read its words at load); fixed and checked live.
- **Step 4: a link to a tree on the map opens its card**, on every city page and on /explore (not only Tokyo): the tree page's bigger-map button, a visitor card's app-only tree, and a tree picked in the search on a map now fly to the tree with its card open, as Google Maps opens a shared place. Before, the city map only lit the pin. A tree picked in the search anywhere else still opens its page.
- **Tokyo leaves its panel Airbnb's way (2026-11-27, Hidde: "ja maak gewoon airbnb na")**: the cross is gone; the first drag or zoom of your own (wheel, pinch, double click, + and -) turns the panel into the trees in view; a tapped pin's card does not. On the way: a wheel zoom never counted as a move by hand (no originalEvent, and in the pane it started a second late), so it is now read from the wheel itself; /explore's country search ends on a wheel zoom too. Checked live: wheel, drag, Back, pin tap.
- Open with Hidde: picking a city in the search still loads its page behind a fade; loading nothing at all means swapping the city's panel in place, the bigger rewrite he set aside on 2026-11-26.
- **Every English city page is the one map now** (2026-11-27, Hidde: "Ja, alle steden"; `ONE_MAP_CITIES = "all"`). Checked live: London (wheel), Lisbon (drag), Bilbao on a 375px phone (drag), no console errors.
- **Translated city pages too** (Hidde: "Ja, vertaalde ook"): /de/berlin dragged turns into "Die Karte der alten Bäume" at /de/explore#map=..., checked live.
- **Country pages too** (Hidde: "Eerst landpagina's"): the map draws the neighbours' trees, a drag turns the panel into the trees in view; checked live on Portugal.
- **No reload when a city is searched on a map** (Hidde: "ok bouw optie 2", after the fly and fade showed Lisbon twice: "very cringe"): the map flies, then the city's page is swapped in without a page load, Airbnb's way (site/src/lib/soft-nav-js.ts in Base.astro's head; the fade is gone). Checked live: London to Lisbon, /explore to Kyoto, Kyoto to Osaka on a 375px phone, no console errors; Back returns to where you were (a real load of that page). The phone's full-screen search now closes when a place is picked on the map. Google still gets every page whole from the server.
- Next: state pages; translated pages swap to English cities with a real load (another language).

## 2026-11-26 night run (19:08 window): nothing to ship

- Rung 1 left to the reader judge (one unmapped reader photo, 3c544597, no backlog over 24h). Rung 2: iOS CI red/in progress on the Feed work sessions are on, open app bug rows already carry tests; web errors orange only (4 new types, none over the red bar). Rungs 3 and 4 empty (sourcing paused while mail batches wait). Own research paused.
- Write pass dispatched on the shelf: every US/UK verified file is already published (stale), ten id-collision entries are live under other ids, and the 3 READY leads (York plane, Guimaraes cypress, Leamington lime) lack source, photo, pin or access checks. Zero trees written. About 200 stale research files could be deleted by a session.
- Tool refusals: none.

## 2026-11-26 Feed, second walk: refresh works again, bell beside the gear, sliding title, profiles newest first

- **Pull to refresh on the Feed said "the feed did not load"** (Hidde). Emptying the list cut its own request off. It now keeps the posts until the new ones are in, iPhone and Android; FeedRefreshWalk failed before the fix and passes after.
- **Header buttons**: the bell moved from the Feed to My trees, beside the gear; the gear is the same 44 disc with edge and shadow and now sits at the Feed's height (it was 8 points higher). Discover keeps no button there, the Instagram and Strava way.
- **The Feed's title slides away while reading down and comes back on scroll up**, as on Discover, iPhone and Android.
- **Discover's shelves**: the gap under a title no longer depends on whether it has See all (11 points difference).
- **The hearts on the Feed's tiles** sit on the name line again (they were 13 points lower).
- **The hole in the Feed's grid** (Hidde's screenshot): the grid broke after a fixed six photos for People you may know, leaving the shorter column's gap; it now breaks between four and eight photos where both columns end level, iPhone and Android.
- **Settings says "Dark mode"** instead of Appearance / Theme, all languages.
- **A public profile shows the newest upload first**, iPhone, Android and the website. FOR HIDDE: paste supabase/profile-newest-first.sql in Supabase's SQL editor; until then profiles keep the old order.
- Not built: a tree card dragged down on the map hides the tab bar; advice is to make it close the card instead (waits for his word).

## 2026-11-26 session (19:30): iOS red, second cause fixed

- The 17:15 ios.yml run on main passed every screen (0 layout findings on 82 screens, both phones) but appfit's source check failed: FeedPeople.swift padded the "People you may know" header twice (ShelfHeader pads itself, then -16). The block now runs edge to edge as a whole, same pixels (7f2d53174). The double-padding check passes locally; the next ios.yml run is the proof.

## 2026-11-26 night run (second attempt, 17:30): nothing to ship, checked and left

- Claims: none standing. READY leads: 3 (York, Guimaraes, Leamington Spa), under the six-candidate floor for a pass, and the other verified files are stale or duplicates of live trees. Own research is paused, so nothing was dispatched.
- iOS red: the 15:49 run failed on the Trending "More" button (SMALL, 24 by 44), which 3bb91fdc9 already fixed; the run for that commit was still going. The five open app bug rows wait on that run's new walks. The open "a tree you added cannot be edited" row is a feature for Hidde.
- Web errors: three new types, one page each, under the red threshold (3+ pages).

## 2026-11-26 night run (17:08 window): iOS red fixed, nothing else to take

- Rung 1: only lead 3c544597 (our own account, file not on disk), already noted by the reader judge; left alone. Rung 2: ios.yml's last failure on main was appfit SMALL on Explore, the Trending row's "More for <tree>" button at 24 by 44 (Home.swift). Widened to 44 by 44 with a -20 trailing padding so the layout stays; not run here (no Xcode on this runner), the next ios.yml run is the proof. Open BUG rows in data/code-audit.json (7, 6 found by people) and the web error `null has no property 'save'` were not touched this window.
- Own research is paused and the shelf has 3 READY leads, none written.

## 2026-11-26 reader judge: a reader's autumn photograph now leads the Greenwich sweet chestnut

- London (lon_005, the Sweet Chestnut of Greenwich Park): a reader sent the whole tree in late-autumn gold from the Flower Garden lawn (9a624f9b). It is now the lead photograph, filed under November, and the Commons photograph moves to the strip. The reader was mailed. Their second frame, taken seconds later a step closer (8c2f3642), was rejected as a duplicate.
- Genoa (gnv_012, the Cedar of Lebanon of Acquasanta): photograph fe75421a is held as `doubt_photo`. It is a summer camera frame of a cedar on a wooded slope, with no camera data, sent in November, and its coordinate is our own pin. It looks like a register or stock photograph, and the setting does not match the open church square our recognition line describes. It was only kept in the sender's own collection, so there is no submissions row and hold_reply could send no mail. The tree still has no photograph.
- Not judged: lead 3c544597 (Amsterdam, near the Last Elm of Stationsplein). It came from one of our own accounts (`mine`) and its file is not on disk.
- No open reports, tips, feedback, readers' notes or further photographs.

## 2026-11-26 reader judge: the Queen Elizabeth Oak of Cowdray Park goes live

- New place Lodsworth (ldw_001, the Queen Elizabeth Oak): a reader sent it through the app as "Pedunculate Oak in Stedham". Their photographs show a huge hollow oak behind a wooden fence, with its Tree Council plaque ("one of fifty Great British Trees, June 2002"). Wikidata Q2702029 stands 30 m from their pin. Wikipedia gives the species as sessile, not pedunculate, a girth of 12.5 to 12.8 m and an age of about 800 to 1,000 years. The pin stays approximate because the app did not record how it was set. The plaque and the shot from inside the hollow went into the gallery. Their fourth image, a phone screenshot of a sauna booking page, was left out (`screenshot`). A one-tree place, so it gets a tree page and no place page.
- North Berwick (nbw_001): photograph 2b191dcd was rejected as a duplicate. It is the same reader's frame of two beech trunks that went into the gallery earlier today as ae685cbf extra 2, so nothing is lost from the page.
- Nothing else was waiting: no open reports, tips, feedback or readers' notes. The other waiting leads are our own `mine` test sightings from September and October.

## 2026-11-26 reader judge: a new lead photograph for the Union beeches, a pin moved in Arezzo

- North Berwick (nbw_001, the Act of Union beeches): a stranger sent three photographs through the app. The new lead shows the beeches close up on the slope of the Law, with bare winter crowns in daylight. The earlier reader's wide shot with the ponies moves into the strip. Their other two photographs (the view from the gate, and two trunks on the slope) went into the gallery. The reader was mailed. Their coordinate was our own pin, so the pin did not move.
- Arezzo (arz_001, Bella di Ceciliano): a reader moved the pin 25 m from the register coordinate (report 1000154). We cannot tell which spot is right, so the reader's spot wins. The pin stays approximate because it was placed by hand, and `pin_source` records the old coordinate. The standard pin thank-you was sent.
- Feedback 1715 is a mail reply about the Madrid eucalyptus with no plain-text part, so the run could not read it. It was closed `needs_hidde` so it can be read in the inbox.
- Left as before: 3c544597 (Amsterdam), our own `mine` sighting, has no photo on disk. There were no tips, and no reader notes to quote.

## 2026-11-26 session: Palheiro Gardens on the Android test

- Play Console (new account, app 4975394642791101357): Palheiro Gardens' Play address added to the closed test Alpha's "Android testers" email list (955 to 956), through Hidde's Chrome. Reply sent in their thread on his yes: they're in, with the opt-in link.
- Bella di Ceciliano's maker's yes (her mail of 14:53) was already handled by the reader judge (78fec2f25): photograph back as lead.

## 2026-11-26 reader judge: a reader's eucalyptus in the Retiro goes live

- Live: The White-Trunked Eucalyptus of the Retiro (madrid/mad_019). A stranger sent it through the app with the note "Ancient and fragrant Eucalyptus in a quiet area". The photograph shows a tall, pale, smooth trunk rising well above the dark cedars in the Retiro's southwest corner. The photograph's GPS puts the pin at the tree, so the pin is confirmed. No register entry stands within 100 m, and it is a different tree from our catalogued blue gum (mad_017, 981 m away). The species is left as Eucalyptus sp. and the page asks readers for it. The story quotes the reader and claims no age. A Spanish overlay entry was added. Madrid's counts now read 19 trees and the Retiro's 10, in English and Spanish. The "catalogued and protected" lines were softened because this tree is in no catalogue. The photo is filed under November from its own date. There were no further photos to add.
- Nothing else was waiting: 0 queue photographs, 0 open reports, 0 tips, 0 feedback, 0 reader notes to quote. Every other open lead comes from our own account (`mine`) and has no photo on disk, including 3c544597 (Amsterdam).

## 2026-11-26 session: Trending this month on Discover, iPhone and Android

- In the apps, next build: Discover has a new shelf, "Trending this month", after "At their best now". Hidde asked for it after looking at Polarsteps' Verkennen tab; he approved the design from simulator screenshots ("bouw maar gewoon"). It holds nine trees as numbered rows, three to a column, and pages sideways. A row shows the photo, the rank, the tree's name and its place. A tap opens the tree; the menu offers Want to visit and Share.
- What trends: the trees the most different people photographed, hearted, voted Worth the visit or saved in the last 30 days. Each person counts once per tree, and our own accounts are left out. The count is `trending_trees` (supabase/trending-trees.sql). Hidde pasted it today, and anon gets ids and counts only. Today's top three: the Totteridge Yew (11 people), Ankerwycke and Llangernyw. Saves carry most of the ranking; photographs alone are flat.
- Hidde's corrections on the first design are recorded in CONVENTIONS.md "Trending this month": trees, not cities, and a rank number in the name's own type rather than Polarsteps' big numeral.
- Not on the website. The shelf is an app pattern, and the website home has no shelf like it yet.

## 2026-11-26 reader judge: two more Varese photographs, and a night shot of the Tsagarada plane

- Live: the Varese reader sent two more photographs. The ginkgo (var_002) is shown bare after leaf fall, with its yellow leaves on the path. The Great Cedar (var_001) is shown whole from across the lawn, with the heart bench in front. Both are clearly our trees (23 m and 13 m from our pins, species and setting match), so both went into the gallery. The reader's earlier photographs stay as the leads: the ginkgo's lead shows it in leaf.
- Live: a further photograph of the Plane of Agia Paraskevi (tsg_001). It is a night shot looking up into the lit crown, published through reader_extras.
- Nothing else was waiting: 0 open reports, 0 feedback, 0 tips, nothing late in reader_backlog. Lead 3c544597 (Amsterdam) is from our own account (`mine`) and still has no photo on disk.

## 2026-11-26 reader judge: readers' mail replies filed

- Nothing changed on the site. The Varese reader wrote back to say thanks and that more trees from the area will come over the next few days. There was nothing to act on, so feedback 1711 is closed as handled, and its reader_words row is done (thanks, nothing to quote).
- Nothing else was waiting: 0 queue photographs, 0 open reports, 0 tips. Lead 3c544597 (Amsterdam) is from our own account (`mine`) and still has no photo on disk.

## 2026-11-26 session: a full Mac, and the tidy that keeps it from filling again

- The Mac had 248 MB free. Freed by hand: the user caches, iOS DeviceSupport, the Gradle cache, five reset simulators, five clean merged worktrees, out/ingar/ingar.zip (the photos stay in out/ingar/raw), and the Bin, which the Storage pane of System Settings was holding open. Now about 55 GB free.
- Why it fills: each test phone grows 2 to 5 GB from builds, sessions made their own simulators ("AT dark hertz", "AT edit-design") and second copies of fixed ones, and worktrees outlive their sessions. New `scripts/devices_tidy.py` (test `scripts/test_devices_tidy.py`) runs at every session start, only when under 40 GB is free. It deletes idle simulators outside the fixed set and second copies, erases fixed ones past 1.5 GB, clears idle Android snapshots and removes clean merged worktrees. Nothing running is touched. Android app data past 6 GB is only reported, with the wipe command.
- Left as they were: four worktrees with uncommitted work (address-dark, android-walk-1125, confident-hertz-623564, visitors-see-all-app-0d6e90) and chain-42, which was touched in the last hours. The two Android emulators were not touched (Small Phone is running, Medium Phone was used today).

## 2026-11-26 reader judge: Bella di Ceciliano's photograph back up

- Changed on the site: the reader's photograph leads Bella di Ceciliano (arezzo/arz_001) again. It was held this morning as a screenshot. The reader wrote back that they took it themselves, on a photography commission for the property. That is the yes the hold asked for (feedback 1710, handled). The Arezzo intro says again that the reader sent its photograph.
- Android test: Sílvia (Palheiro Gardens, Madeira) said yes and sent her Play address. She is on the tester list as `yes`, with that address (private store pushed). The opt-in link goes out with the next invite. Feedback 1709 is closed as handled.
- Nothing else was waiting: 0 queue photographs, 0 open reports, 0 tips. The waiting leads in _sightings.json are all from our own account (`mine`). Lead 3c544597 (Amsterdam) still has no photo on disk.

## 2026-11-26 session: the feed's empty tile and the double cedar

- **Empty tile**: a photo sent from a tree's page on the website made no public copy in shared-sightings (the app does), so the live-first feed showed it as an empty tile (Madison tupelo). The website now uploads that copy too (add-photo-js.ts), and feed() shows a just-shared post only once its public file exists. Pasted by Hidde; live feed checked, every photo loads.
- **Same photo twice**: a reader who sends one picture twice (same moment, same fix) shows once before the judge looks, the copy on one of our trees first. The Varese case was the reader correcting a wrong tag; the judge made it a new tree (var_004), right call.

## 2026-11-26 session: a tester's three points (photos, dark mode, pin search)

- **Photos**: no script ever published the further photographs a reader sends with a tree, so 84 live trees showed fewer than were sent. scripts/reader_extras.py gives each one a verdict (data/reader-extras.json); 311 looked at on contact sheets, 278 now in their trees' galleries, 25 left out (selfies and posed visitors, Google Lens screenshots, an engraving, planks, near-duplicates). preflight refuses a published tree whose extra has no verdict; the reader judge's brief has the step. The congratulation mail now says which photos stayed off and why, and that we wrote the story from what they sent. Escaped bug closed with scripts/test_reader_extras.py.
- **Dark mode**: Settings has Appearance (System, Light, Dark) on iPhone and Android, kept on the account like Distances. The dark ground is one step lighter (#1A1D18), all text AA. Next builds.
- **Pin step**: the address field (this morning) now says when nothing is found and takes typed coordinates; the locate arrow was already there. Next builds.
- Not done: the story edit before publishing. That belongs with the "edit your tree" design of 2026-11-25; the mail tells them what we did meanwhile.
- For Hidde: paste supabase/profile-appearance.sql in the Supabase SQL editor (https://supabase.com/dashboard/project/caimvxiyrtifilimlkqw/sql/new). Until then the choice holds on the phone and is not yet on the account.
## 2026-11-26 reader judge: the Palheiro araucaria gets its planting date

- Changed on the site: Palheiro Gardens' Tall Araucaria (mdr_013, Madeira) now says it is about 215 years old, by a reader's estimate. The reader who added it wrote back that the garden believes it was planted around 1810 by the first Count of Carvalhal. The age is on the page in our own words, in English and in the Portuguese overlay. It is not quoted, since a mail needs their yes first.
- For Hidde: the same reader asks when the Android app comes out, because they want to add more of the garden's trees on site. A reply offering them the Android test group is in drafts/reply-reader-1708-2026-11-26.md (mailcheck is clean). Feedback 1708 is closed as needs_hidde.
- No readers' trees, photographs or reports were waiting. The one queue item (3c544597) is from our own account (`mine`) and its photo is not on disk, so it stays.

## 2026-11-26 reader judge: the Varese campus gets its history from a reader

- Changed on the site: the reader who sent the Varese campus beech wrote back that the campus began as a psychiatric hospital in the early 1900s. That fact is now in the stories of var_003, var_004 and var_005, stated as theirs and in our words. It is not quoted, since a mail needs their yes before we quote it. Feedback 1707 is closed as handled, and its reader_words row is done.
- No readers' trees or photographs were waiting, and no reports were open. The one queue item (3c544597, Amsterdam Stationsplein) and the other waiting leads in _sightings.json are all from our own account (`mine`), which never auto-publishes. The Amsterdam photo is also not on disk.

## 2026-11-26 reader judge: two campus trees in Varese and a fox-red conifer in Glasgow, live

- Live: varese/var_004, The Picnic-Table Cedars (two big cedars over the picnic tables on the university campus, a few dozen metres from var_003), and varese/var_005, The Autumn Beech of the Campus (a broad beech in full copper on its leaf carpet, framed by a cedar). Both are from the reader who sent var_003 this morning, and both have the photo's own location. Varese now has 5 trees. Its intro, meta, question texts and FAQ give the new count. It has no kept translation.
- Live: glasgow/gla_012, The Red Conifer by the Pond (West End, a tall feathery conifer blazing fox-red beside an iced pond, with sandstone tenements behind). The reader calls it a European larch. Its narrow shape, fox-red colour and place at the water's edge look like a bald cypress, so the species reads Bald Cypress and the page asks readers to confirm. We did not name the garden; the page asks for that too. Glasgow's meta now says 11 trees. All three photos are filed in November, the photos' own month.
- Rejected as a duplicate: sighting e3899250, sent for var_003. Its main picture is the same picnic-table cedar photo that is now var_004. Its extras show var_003's trunk (which already has this reader's photo) and the beech (now var_005).
- Report 1000152 (pin moved, same reader): the pin was dragged 188 m south while the picnic-table cedar was being added. The photo's own location is from under the tree, so the pin stays there (GPS beats a pin moved by hand). Closed holds with no mail, because the move was part of adding the tree. Noted in var_004's verify_notes.
- Nothing else waited: 0 tips without a verdict, 0 reader notes to quote. Lead 3c544597 (Amsterdam) still has no photo on disk, so it was left alone again.

## 2026-11-26 session: /explore now reads as the city page

- Hidde: the map page still looked "veel lelijker dan een stadspagina", though on 11-22 he had ruled it should look the same ("gebruik dit design als basis ... maak er 1 component van"). That session built it and never committed it; the work sat in the checkout for four days.
- Now on main: one place head (PlaceHead.astro: crumbs, title, share circle) and one intro (PlaceIntro.astro: the intro with Read more, the ambassador box above Highlights) on the city page in every language, the country page and /explore. On a desktop the loose "343 trees" line is gone. A searched country retitles the head to "Ancient Trees in <em>Country</em>" with its own intro (map.ts `_headFor`). qa `check_one_place_head()` refuses a head or intro written by hand. map-parity row: web only, the phones already draw one header.

## 2026-11-26 session: a just-shared tile on /visitors gave a 404

- Cause: feed() linked a not-yet-checked share to /t/?id=, and the live site only answers /t?id= (no slash). The web tile now corrects it (live with deploy 45824261606), and supabase/feed-live.sql hands out /t?id= itself.
- Also: a just-shared photograph of a tree we already have now opens that tree's own page under its name, instead of the bare share page. Web through a new public table feed_trees (id, name, place, link; filled by feed_publish.py), iOS and Android by trying the known tree before the share page (next builds).
- For Hidde: paste supabase/feed-live.sql in the Supabase SQL editor. Until then the web fix covers the 404; the tree-page link for photos waits for the paste and the next feed_publish run.

## 2026-11-26 session: ages cut inside a number, fixed on the website

- Hidde saw an age like "200 -2" on the site. Cause: the tree page, the translated tree page and the card cut age_estimate at its first comma, including the comma in "2,000". Kingley Vale's yews ("500 to 2,000 years") read "500 to 2", and 26 more tree pages read "about 1" / "roughly 2" for trees of 1,000 to 2,600 years (Dujiangyan, Kvam, Llanerfyl, Yakushima, Omishima, Logan Canyon, Osaka and others); 8 cards did the same. The apps had this fixed on 11-24 (report 1000138), the website never got it.
- Live with the next deploy: firstAgeClause() in site/src/lib/age-short.ts, used by all three; qa `check_an_age_is_never_cut_inside_a_number()` runs it over every tree and refuses a hand-written comma cut. Escaped bug recorded and closed with b24814e56.
- The data itself was checked too: no negative bounds, no max below min, no card range running backwards across 5,151 trees.

## 2026-11-26 reader judge: a tall araucaria at Palheiro Gardens, Madeira, live

- Live: madeira/mdr_013, The Tall Araucaria of Palheiro Gardens, from a reader's website tip with a photograph (viewed: a Norfolk Island pine standing alone on a lawn, tier on tier, daylight). It came with no GPS, so the pin is approximate on the garden's point (the same as the pohutukawa, mdr_010). Paid entry. The page gives the reader's 48 m, their survey citation (Árvores Monumentais e Emblemáticas da Madeira, 2008) and their account of the garden as their own words. Photo filed in November, the photo's own month. Madeira now has 13 trees; its intro, meta and question texts (EN and the kept PT overlay) give the new count, and the PT overlay has the tree.
- Nothing else waited: 0 open reports, 0 open feedback, 0 reader notes to quote. Lead 3c544597 (Amsterdam) is still our own account's and its photo is still not on disk, so it was left alone.

## 2026-11-26 night run: nothing useful to ship

- Nothing published. Own research is paused and the shelf holds one unwritten tree (taiwan) plus 3 READY leads, under the six-candidate floor for a write pass. The "382 awaiting a writer" figure is almost all stale files of trees already live.
- Rung 1: the reader judge owns the 2 unmapped reader photographs (3c544597, tip-1700). Nothing a reader sent has waited over 24h. One new note on mdr_013 (Madeira, 48 m Norfolk Island pine, factual) read and left visible.
- Rung 2, left for a Mac session: iOS run 45810490360 is red on `CountryStaysWalk.testAPickedCountryStaysOnTheRow` ("the list did not go back to the editor", "the row does not start on the saved country"). It is the Edit profile Country work of commit 60a0c41ad; the UI test cannot run on this Linux runner. Web errors orange: new type `undefined has no property 'init_ts'` in a promise. Open BUG row ESC-2026-11-25 (edit a tree you added) is a feature, his call.
- Rung 4 sourcing stays paused while mail batches are open. reader_words, recognise --stuck and enrich --next: nothing to do. pagegaps: only species and park intros, whose pages are in the strict cut, so skipped.

## 2026-11-26 reader judge: a campus cedar in Varese live

- Live: varese/var_003, The Cedar of the University Campus, from a reader's app photograph (four frames viewed; photo GPS at the tree, dated November). A broad blue-grey cedar alone on a campus lawn. Species left at Cedrus sp.: the reader says Lebanon, the crown reads Atlas, and the page asks. Varese now has three trees; its intro, meta, question texts and FAQ say so. No kept translation of Varese.
- Reader words: the Cat Tien tung note closed as pasted text (summary prose with an em dash, not the reader's own account).
- Nothing else waited: 0 open reports, 0 open feedback. Lead 3c544597 (Amsterdam, 2026-11-18) is our own account's and its photo is not on disk, so it was left alone.

## 2026-11-26 session: US round 3 sent, round 4 (empty cities) ready

- Round 3 sent through Resend on Hidde's "Verstuur ze": 8 (Charleston City Paper, South Carolina Wildlife, Big Island Now, Delaware County Daily Times, Audubon, Friends of the Parks, Chicagology, Bronx.com). 58 US local mails out since 11-25; one answer so far (The East Hampton Star).
- Round 4 on hold, drafts/batches/press-us-empty-cities-round4.json (private): 14 desks in big US cities with no or hardly any trees (Phoenix, Denver, Detroit, Charlotte, Memphis, Louisville, Sacramento, Nashville, Milwaukee, Indianapolis, Cincinnati, Raleigh, Tampa, Albuquerque). The P.S. asks which tree their readers would put on the map first ("still empty" only where none of ours stands within 30 km). No desk address found for Columbus, Jacksonville, Omaha, Orlando or Tucson. mailcheck clean.

## 2026-11-26 session: Hidde's walk through the new Feed, fixed on both phones and the web

**What changed for people:**
- **Back lands where you were** (Feed, Find people, profiles, Discover): lists no longer reload when they come back into view. Test BackKeepsPlaceWalk.
- **Photos load what is on screen first** and drop the ones scrolled past; a fast scroll no longer stalls the Feed and every other page. Test ImageGateTests.
- **The Feed shows only checked posts** (iPhone, Android, website row and /visitors): a share waits 10 to 30 minutes until it is a tree with its page, save and heart.
- **Following** with nobody followed leads with People you may know; **Near you** without a location leads with a card to turn it on.
- **One card in two sizes**: save top right on every photo, heart at the end of the person's line, share on the tree page.
- **One round header button** on every tab; the bell moved from Discover to the Feed beside Find people, which asks a signed-out person to sign in first. Activity's "New" and "Earlier" in plain type.
- **Share your profile** works again on the iPhone (ShareProfileWalk); a tap on a person's name no longer opens their followers, and an ambassador's badge opens their place (PersonProfileWalk).
- **The photo viewer slides sideways** with the finger; bylines under photos are bigger (15 in the viewer, 13 on tiles).
- **My trees: newest upload first** on both phones. Other people's profiles keep the server's order without dates (the privacy rule): a change there waits for Hidde.
- **Android: "Appearance" is now "Theme"** in all eight languages, Google's word; the iPhone keeps Apple's "Appearance".
- Five bugs Hidde found recorded with escaped.py and closed with their tests. Installed on Hidde's iPhone from this branch for his walk.

## 2026-11-26 session: the Feed's new design on both phones (Hidde approved v4 and menu option 3)

- **The Feed opens zoomed out**, the website's /visitors masonry: whole photographs at their own shape, place on the photo, save top right, name, who and heart under it. One post big is the other half of a tab row under the chips (Instagram's profile tabs).
- **People you may know** (Polarsteps' Activity row): small cards with Follow and an X, between the photographs after the first six, signed in only; See all and a new person-with-a-plus top right open Find people.
- **iPhone tab bar: Polarsteps' balance** (option 3 of five shown beside his Polarsteps screenshot): 22 pt glyph, 2 above a 10 pt semibold word, items not chosen nearly as dark, a grey pill. Android keeps its own docked bar.
- A session the server refuses still gets the public feed (both phones), so a stale sign-in never empties the tab.
- Tests: iOS FeedPostsTests, SignedOutWalk feed Following and name (the name now a button on the tiles); Android FeedPostsTest and a build; screens looked at in the simulator, the emulator and on Hidde's own iPhone (a test install from this branch, 16:30). Android's build needed a clean Gradle cache (the shared one had lost files when the disk ran full).

## 2026-11-26 session: the walk's bugs fixed on Android too, memory given back out of sight (for build 7)

- **Product (Android, ships with build 7)**: every walk finding that was in Android is fixed the iPhone's way: oak search, Back to the results, "You" for your own heart, one avatar letter, a filter closes a hidden tree's card, a My trees lane frames its trees, the viewer returns to its picture, a searchable country list (eight languages) opening on your country, the location chip at large text, "1 follower" in eight languages, no empty photo credit. Bug 11 (Tortworth) was already in from the iPhone session (3 km). The rating question twice was two simulators, not a bug.
- **Memory** (Hidde: "hoe voorkomen we die geheugen crashes"): all four build 6 exits were Android ending the app in the background. A tree being added lives in memory only, so a further photograph with the camera can still lose the whole tree. Keeping it on the phone was built and taken out the same day (Hidde: "NOOIT IETS LOKAALS OPSLAAN ALTIJD AAN ACCOUNT"); the way is a draft on the account, and crossdevice.py now reads Android and refuses any new device store without his yes. The app gives its decoded photographs and map tiles back when out of sight (onTrimMemory). Emulator, 20 trees opened: 403 to 361 MB once home; most of the rest is the map's drawing, which only a real phone measures honestly.
- **Found on the way**: Android's unit tests had been red on main since 11-25 (the snapshot dropped whose photograph a visitor's is), so no spacing or walk run happened since. Fixed (snapshot ATS5).
- **Open, not built**: a tree you added cannot be edited afterwards (ESC-2026-11-25, report 1488): a new flow, on both phones, needs design first.
- **For Hidde**: your own heart says "You" only once the `photo_likers` function from supabase/photo-hearts-who.sql is pasted (the iPhone needs the same paste).

## 2026-11-26 session: the Feed shows a reader's share before the judge looked (feed-live.sql), and its icon is Polarsteps' Activity

- **Unchecked posts** (`checked = false` from feed()) on iPhone, Android and the web row and /visitors: the reader's own name for the tree, "just shared a tree" in the byline (eight languages on Android), no place, no "New on the map", no heart, no save; a tap opens the share page (/t/?id=). When the judge approves, the same post comes back checked in the same spot. Decoder tests with checked true, false and missing: iOS FeedPostsTests, Android FeedPostsTest, both green.
- **Fixed before it reached anybody:** the iOS Feed failed to load any page holding such a row (its tree id is null, the decoder wanted text). No build carried it.
- **The Feed tab's icon** is one person in front of a smaller one on both phones (Hidde: "laten we het activiteit logo van polarsteps overnemen", "die gespiegelde"): Material's `group`, on iOS as a template asset because SF has no such symbol (ICONS-LICENSE-APACHE.txt beside the app).

## 2026-11-26 session: a screenshot waits for its maker's yes; Bella's photo off

- **Rule reversed** (Hidde: "screenshot zijn wel gevaarlijk toch", "Ja, doe het"): the 2026-11-25 line that let a screenshot through unless plainly someone else's is gone from BRIEF_READER_JUDGE.md. A screenshot (no camera data, social crop, letterbox bars, filter) is held as doubt_photo and the reader is asked "Did you take it yourself?"; their yes puts it up.
- hold_reply.py: `doubt_photo` and `doubt_photo_live` (the tree is live without the photo), `--again` for a row we already answered.
- **Bella di Ceciliano** (arezzo/arz_001) stays live on the register; its screenshot photo is held and the texts no longer point at it. Its reader and the Tsagarada plane's reader (submission 1433) are asked, mail at the next knock.
- Settled with Hidde: Raincliffe beech and chestnut stay leads, the two Goll Woods rows stay held, the Tsagarada screenshot stays held.
- Confirmed sent (tell-readers run 45799891977): the "fixed, comes with the next update" mails to #1488, #1491, #1686.

## 2026-11-26 session: the feed comes from the server, live first (Hidde: "yes letsgo")

**What changed for readers.** What a reader shares is in the feed at once, straight from Supabase (`feed()`, supabase/feed-live.sql), with their own name for the tree and their photo but no place or pin until the judge has looked; the judge's hold or reject takes it out, its approval turns it into the full post (name, place, pin) at the same spot in the feed (trigger supabase/feed-sent-time.sql). The checked posts live in a `feed` table with their own photo copies (supabase/feed.sql), written by `scripts/feed_publish.py` right after each judgement. One post per send now (second frames were separate posts). The apps' handling of a live post was handed to the Feed tab session.

**Why New from visitors showed no new trees for days.** `scripts/sightings_link.py` asked for 720 ids in one request, Supabase answered 400, and nothing was linked; it also only ran from the knock, which GitHub stopped delivering. Batched, and the reader judge runs it after every judgement; 21 trees linked at once.

**The clocks moved to Supabase.** GitHub dropped every frequent cron from 02:22 UTC (judge, knock, Site up). pg_cron now starts the judge every 10 minutes (supabase/judge-clock.sql) and the knock watchdog three times an hour (supabase/knock-clock.sql), with a new GitHub token Hidde made; the instant trigger works again with it (the old token had 403'd since the repo move). The California map walk that kept every deploy red from 03:38 to 08:48 UTC: the card now moves the pin aside when no side has room (map-card-js.ts).

## 2026-11-26 session: readers hear "fixed, comes with the next update" before the build lands

- **The order** (Hidde: "dit kan heel lang duren dus ik zou m alvast mailen", "onthou die volgorde"): `scripts/bug_fixed_mail.py` now mails an app fix twice, the day it is on main ("We fixed it ... The fix comes with the next app update") and again when the build is in their store ("The fix is in the app now"); a website fix once. Where a fix lives is read from the files its commit changed.
- Android counts as out only once its versionCode is in the new data/android-releases.json (Play uploads are by hand; android_release.py prints the reminder). 6 is listed.
- Sent now through tell-readers.yml: the first mail to #1488 (Tortworth under Westonbirt), #1491 (country that would not stay, iPhone build 42) and #1686 (could not add trees, Android build 7).

## 2026-11-26 session: the Feed is a tab of its own, on both phones, and the web row reads the server (Hidde: the feed "een eigen tab", design "niet slecht")

**What changed in the product (not in a store build yet; Hidde releases):**
- **iPhone and Android: a Feed tab**, third in the bar (Map, Discover, Feed, My trees; the camera stays apart). One post per thing a reader put live, newest first: face and name (a public profile's, else "A visitor"), "added a new tree" or "photographed a tree" and when; the whole photograph at 4:5 with the place on it and "New on the map" on a tree somebody added; the tree's name and its story's first sentence; heart (a visitor's photograph only), save, share. Chips Everyone, Following, Near you (100 km). Endless, pull to refresh. iOS Screens/Feed.swift + Kit/FeedPosts.swift, Android ui/Feed.kt + account/FeedPosts.kt, strings in all eight Android languages. Tab tag 4 on both phones so My trees stays 2 and the camera 3.
- **Every post comes from the server's feed() only**, never the catalogue: a tree the judge put live a minute ago shows and opens from the post itself (name, place, picture, pin) until the next catalogue knows it.
- **Discover's "New from visitors" row stays**; its See all now opens the Feed tab.
- **Website: the home row and /visitors read feed()**, so a tile needs nothing from the build (the baked #nfv-data and #vp-data are gone from those pages). Only a visitor's photograph carries the heart.
- Side by side at 375: drafts/design-2026-11-26-feed/built-ios-android.png (real rows, simulator and emulator). CONVENTIONS.md "A feed tab"; data/android-parity.json `feed`; ButtonWalk and SweepFrames list the screen (`-tab=4`, and `-feedto=N` scrolls to a post for the sweep).

**Not verified here:** the website change has no local build (no Node on this Mac); CI's build and the deploy's pagecheck are the check. The ButtonWalk and SweepFrames runs for the new screen happen in ios.yml / buttonwalk.yml, not here.
## 2026-11-26 reader judge: the Verona silk mulberry gets its autumn photograph

**The Silk Mulberry of Ca' di David in Verona (ver_011) now leads with an autumn photograph.** The reader who added the tree on 11-24 sent it: the whole tree in yellow leaf, the low split trunk with its hollow, the fence and the road behind. Their summer photograph moved into the strip, and the new one is filed under November. The pin stays where it was, because the photograph's coordinate was our own hand-placed pin and not a GPS fix. The reader was mailed by `sightings_publish.py --send`. The pin catch-up got an HTTPError from the server again.

Left waiting: lead 3c544597 (Amsterdam, near the Last Elm of Stationsplein) has no file on disk. It is marked `mine` (one of our own accounts), so it is never auto-published anyway. There were no open reports, feedback or tips.

## 2026-11-26 reader judge: a reader's autumn photograph now leads the Preston Twin

**The Preston Twin in Brighton (bhm_001) has a reader's photograph as its lead.** It shows the whole elm in autumn yellow in front of the walled garden's wall: a burred trunk forking into two great limbs, small rounded toothed leaves on the lawn. The same trunk as the old Commons close-up, which moves to the strip. The photo is filed under November. The tree's approximate pin moved 98 m to the reader's fix and is now confirmed. The same photograph arrived twice, so the second copy (25947861) was rejected as a duplicate. The reader was mailed by `sightings_publish.py --send`. The script could not read pin coordinates from the server (HTTPError) during its pin catch-up. The move itself is in data/cities/brighton.json.

**Nothing else waiting.** There were no open reports, no feedback without a verdict, no unjudged tips and no reader notes left unquoted. The 38 leads still marked `lead` with no hold all come from our own account (`mine`), so they are not reader work.

## 2026-11-26 session: every bug the build 42 walk found, fixed on the iPhone (Hidde: "ik wil vooral dat je alle bugs gaat fixen de build komt later")

- **Fixed, each with a test unless said** (WalkFindingsTests, SpeciesSearchTests; looked at in the simulator where marked):
  - Search "oak" showed Adriatic and Aleppo Oak and never Pedunculate Oak (426): species ties now go by tree count. Looked at.
  - Back from a tree or species found by Discover's search lands on the same results again; the search's own arrow still goes to Discover. Looked at (no unit seam).
  - Your own heart says "You" in the hearts list. **Needs Hidde to paste** the `photo_likers` function from supabase/photo-hearts-who.sql: your own heart comes back with your account even on a private profile. Until then the app still says "A visitor".
  - One avatar letter: Settings now shows the profile name's letter, and your photo, as My trees does. Looked at ("L" on both).
  - A filter that hides the chosen tree (Want to visit, Collected, any chip) closes its card.
  - My trees: switching between Want to visit and Collected frames that lane's trees.
  - The photo viewer returns the tree page to the picture you closed on (no unit seam).
  - Edit profile > Country: a searchable list ("Search countries"), opening on your country with a tick. Looked at.
  - The Location off chip keeps clear of the locate arrow and drops "Location off ·" at large text (no large-text check exists).
  - Report 1488: a tree you added is labelled with the place the phone named, or our place only within 3 km, never Westonbirt for a Tortworth chestnut. The bug row has its reader line, so the reader hears once the build is out.
- **Not a bug**: the rating question twice in one walk was two different simulators. **Not built**: an offline notice (a new element; design first if Hidde wants it). "Remove from collected" keeping the collect photo is the documented behaviour of the Delete photo sheet.
- **Android owes the same** (prompt handed to Hidde for an Android session): the list above, plus "1 follower", the 71 spacing differences. data/map-parity.json has an open row for the map parts.

## 2026-11-26 session: tests for the bugs people found, and the Tortworth label on Android

**Android carries report 1488 too.** On the Android app, a tree you added in My trees is now named after one of our places only when one of our trees stands within 3 km, the iPhone's number from the entry above (MyTreesPlaceTest). Before, Android took the nearest place up to 50 km away, which is how the Tortworth Chestnut showed under Westonbirt, 15 km off, in the minute before Tortworth's own page reached the phone. The iPhone fix is the session above's; this session's own iPhone version was dropped in its favour.

**Tests where there were none.** Three bugs people found had been closed with "no machine can see this". Each now has a test. The card swipe-away rule (56 points or a flick) is in one place per platform, with CardSwipeTests and CardSwipeTest. The iOS 18 scrolled navigation bar keeping its background has NavigationBarTests. Text running into text at the largest text size has a new OVERLAP rule in `appfit.py --large-text` (test: scripts/test_appfit_overlap.py), which the twice-daily iOS 18 floor job now runs on the small iPhone.

**Crash list.** The build 41 hang (AncientTrees+0x376463, 2 s, iPhone 12) was answered in data/crash-fixes.json. The main thread was waiting on Metal's shader compiler during the map's first draw, and no code of ours was running. A repeat, or a hang of 5 s or more, rings again. The build 41 crash during a pan is fixed in build 42.

**Digest.** "What was fixed" said "a person" for bugs our own test walk found. It now says "our test walk".

## 2026-11-26 reader judge: a hollow chestnut in Guernsey goes live

**Live.** St Peter Port, Guernsey, stp_001 "The Hollow Chestnut of Cambridge Park" (lead 636ce3a4, sent through the app today with the photograph's own location). The photograph shows a veteran whose central trunk has burst open and gone hollow, with thick grey living limbs sweeping low over the park lawn around it. The reader sent it as an oak of 400 years. The long, saw-edged leaves in the crown and on the grass are a sweet chestnut's, so we list it as one, and the story and FAQ name the reader's oak and ask anyone who knows the tree better to say so. The age is published as the reader's estimate. The pin is confirmed. A web search found no written record of the tree; the park's name comes from the coordinate. This is a new one-tree place (no place page under the two-tree rule), with Guernsey as its country. The photo is filed under November by its own date.

**Nothing else waiting.** There were no open reports, no feedback without a verdict and no unjudged tips. reader_words found no note left unquoted. `sightings_inbox.py --status` still lists lead 3c544597 (since 2026-11-18) with its photograph not on disk. It is marked `mine` (our own account), so it is not reader work and was left alone.

**Checks.** qa --source-only, preflight (0 problems) and i18ncheck are clean. preflight notes that st-peter-port has never been looked up in other languages (`city_names.py`).

## 2026-11-26 session: "Not able to add trees" (report 1686) fixed on Android

**What happened.** PostHog put the reader on Android 17, Play build 5, signed in. Twice that phone logged `app_exit_abnormal` reason `memory` right before the reader came back and searched Discover, My trees and Map without ever reaching the add flow. The system camera is another app, and on a phone short of memory Android ends ours behind it. The photograph landed in the cache, but nothing read it after the restart, so the reader met an app that had forgotten their tree. iOS keeps its camera in-process and does not have this.

**Fixed (5ae461a40).**
- A recent shot left in the cache now opens the add flow at the next start, once signed in and located (`Collector.rescueShot`, ShotRescueTest).
- Reproduced on the emulator: with a shot in the cache, force-stop then start opens "Which one is it?" with the photograph.
- The map's empty-place "Add a tree" opens the flow, as EmptyPlace.swift's does. Before, it only cleared the map.
- The bug row is fixed, and the reader gets the standard "fixed" mail once a Play build carries it (bug_fixed_mail.py).

**Not this change:** `feed.SnapshotTest` fails in the Android unit suite. It compares the bundled catalogue, which this change does not touch.

## 2026-11-26 night run (01:27 window): nothing shipped, short orientation only
- Rung 1: no new tree notes; one reader photograph of an unmapped tree (3c544597, Amsterdam area) is the reader judge's, left to it. Rung 2: health.py red on (a) the live site behind main, where `gh workflow run deploy.yml` was refused with HTTP 403 (this runner's token cannot dispatch), so the deploy waits for the schedule or a session; (b) three open APP bug rows from readers. I fixed none: the "no distance limit" in the Tortworth row is wrong for iOS (`Catalogue.nearest` defaults to 50 km, `Collect.swift:200`), the real complaint is a labelling and edit-your-own-tree product choice, and a Linux runner cannot build or test the iOS app. The report-1686 "not able to add trees" row needs a reproduction on a device.
- Own research is paused; 3 READY leads (york, guimaraes, leamington-spa) were not written this window.

## 2026-11-26 reader judge: Ames sycamore gets its corner and age, Woolland Yew pin moved

- **Ames** (amw_001): the reader's mail reply (feedback 1690) gave the spot, the northeast corner of Lincoln Way and University Boulevard (fits the GPS pin), and an age of about 200 years. Now on the page as theirs ("by a reader's estimate"), along with the storms it has come through, in our own words (no quote without their yes). Address, access, FAQ and question texts follow. Closed `handled`.
- **Woolland Yew** (wol_001): a reader moved our approximate grid-reference pin 6 m (report 1000150). We took the move, the pin stays approximate, and they got the standard pin thank-you.
- **Tips 1673 and 1675**: these are app tree rows in Goll Woods whose sightings no longer exist in Supabase. There is no photograph and there are no words, so both are held with that reason. They stand 90 to 150 m from the two Goll Woods oaks that went live yesterday.
- No reader photographs waiting. The open leads in _sightings.json are all our own (`mine`) photos, never auto-published. The newest, 3c544597 (Amsterdam, Stationsplein), has no photo on disk.
- No tree notes, and no readers' words waiting to be quoted.

## 2026-11-25 reader judge: seven readers' trees live, six new places

**Live** (every photograph viewed; all under the closed list, none held):
- Casargo, Valsassina: the Great Beech (cgo_001), a huge many-limbed beech on the track to Chiarino; the reader's 600 years and 930 cm girth stated as theirs. Hand-placed pin, approximate.
- Goll Woods State Nature Preserve, Ohio (new place, two trees): a tall chinkapin oak beside the ODNR sign (gol_001, the reader's 450 cm girth) and a pale-barked white oak 300 m away (gol_002). GPS fixes, confirmed.
- Cape Neddick, Maine: a broad roadside oak, "Very old and very big!" (cpn_001). Approximate.
- Cat Tien National Park, Vietnam: a giant buttressed tung, Tetrameles nudiflora, the reader's "Thunder Lizard" (ctn_001). Approximate. Their long note reads as pasted chatbot text, so it is not quoted (reader_words --done); its 400 years and wartime account are on the page as theirs.
- Stanton upon Hine Heath, Shropshire: an oak whose limb loops back into its own trunk (sth_001), the reader's words quoted. Approximate. Access says plainly we have not confirmed the wood is open to all.
- Thredbo, Kosciuszko National Park: a healthy snow gum among granite boulders (thr_001), the reader's words on snow gum dieback quoted. Approximate.

**Waiting:** tips 1673 and 1675, two more Goll Woods trees from the same reader with GPS fixes, came with no sighting and no photograph on this machine. Left for the next run rather than judged blind.

**Feedback 1686** ("Not able to add trees", app profile form, platform unknown, the account has never sent anything): recorded as an open app bug (ESC-2026-11-25-a-reader-wrote-from-the-app-s-profile-fe) with the line the reader gets once it is fixed. It needs a signed-in reproduction of Add a tree on both apps; rung-2 work.

No open reports on our trees. preflight 0 problems, qa source clean, i18ncheck clean.

## 2026-11-25 session: readers' trees waited five hours; the judge now runs on its own

**What happened.** The repo moved to Ancient-Trees-Org at 13:50 without the Claude GitHub app, so the reader judge's agent died in 16 seconds on every run while the run said success. The intake still wrote readers' trees and photos into the data unjudged, and preflight then refused every deploy from 15:55 to 19:00 (nine red). On top, GitHub delivered the judge's 15-minute cron about once an hour and not at all from 18:26 to 21:46 CET, and the poll looked back only 25 minutes, so what readers sent in the gaps was never seen. The Supabase trigger has not fired since 13:31.

**Fixed.** Hidde installed the app on the organisation; a hand-started judge published Big Belly Oak, Brudenell Oak, the Kingley Vale yews and the Ames sycamore. QA then caught "we will add it with your name" in the Brudenell story; cut. Deploy green, all four pages 200. Now:
- reader-judge.yml ends red when the agent step fails, and its poll looks back to the last green run (25 minutes to a day) instead of a fixed 25 minutes.
- knock.yml and uptime.yml each run `scripts/judge_knock.sh`: no judge run for 20 minutes and none in flight dispatches one with poll=yes (a dispatch is never dropped; the poll still decides whether an agent starts).
- health.py watches reader-judge.yml: red, or no run for two hours, rings.

For Hidde: the Supabase trigger (the instant path) is still dead after the move; the watchdogs cover it at roughly 20-minute pace.

## 2026-11-25 session: the test chain before iPhone build 42 (Hidde: "Ja, start hem")

- **Fixed in the app, from the release walk** (iPhone 16 Pro Max iOS 18.6, SE at XXL text, test account; walk notes in out/tmp/walk-ios.md):
  - The map lost every pin after a light/dark switch until a pan. A style reload cleared the drawn keys but not the drawn array, so nothing was set again. `TreeMap.DrawnTrees.forget()` clears all of it; test MapStyleReloadTests, red with the old forget. Looked at: pins stay through light, dark, light.
  - iOS 18: the navigation bar was see-through once content scrolled under it (the clock and Back over the tree page's facts, Find people, Settings), since 2026-08-20. Below iOS 26 the scrolled bar now takes the system material and the tree page keeps a clear bar only over its photo (`HeroBarBackground`). iOS 26 unchanged. Looked at scrolled and at rest.
  - The tree page credit read "Photo:  · Provided by a reader..." for a reader's photograph: the feed's empty credit_line now means no credit, as on the website. Test CreditLineTests.
  - My trees at large text: "0 followers" wrapped and sat over the name; the counts stay on one line. "1 followers" is "1 follower" (My trees, a person's profile).
- **Data**: the Pekingtuin oak's story said 5.52 m around; the national register (2024) and the facts box say 5.9 m. Story follows the register.
- **Machines**: appsweep 160 screens, the ones looked at clean. Android: unit tests and Play build ok, the Play apk by finger ok; the instrumented run on the minified build hung past its 30 minutes on this Mac (CI's own walk is green, its spacing job red since 11-25 08:30).
- **Owed by Android before its next release**: "1 follower" in the singular (mt_followers and the profile's followers string, eight languages, as a plurals resource); the spacing run's 71 differences (tab bar Discover position, sheet grabber, contribute and feedback sheet tops; out/parity/spacing.json); the instrumented run on the minified build that hung locally.
- **Not fixed, nits from the walk** (should-fix list for a later build): the country list in Edit profile has no search and opens at the top; "A visitor" for your own heart on a private account; Want to visit keeps the card of a tree the filter hides; the review sheet came twice in minutes; searching "oak" misses Pedunculate Oak; offline nothing says so.

## 2026-11-25 session: a reader who reports a bug now hears when it is fixed

- **New mail** (Hidde: "Ja, bouw hem"): `scripts/bug_fixed_mail.py` tells a reader whose feedback was closed as a bug that it is fixed, once the fix reaches them: the live site's commit for web, the App Store build for iPhone, an Android build. One standard line in our words (`reader_line` on the bug row, Dutch when they wrote Dutch), never theirs. Runs in tell-readers.yml after each deploy and in the knock. Tests: scripts/test_bug_fixed_mail.py.
- `escaped.py --reader-line` / `--reader-line-nl`; `--fixed` now refuses a reader's bug without a reader line.
- First in line: #1491 (the country that would not stay), waiting for iPhone build 42 in the App Store. #1488 (Tortworth under Westonbirt) waits for its fix.

## 2026-11-25 reader judge: Big Belly Oak, Brudenell Oak, Kingley Vale yews and an Ames sycamore live

- **Live, new trees from readers** (photographs viewed, the pin is where each reader stood):
  - savernake-forest/svk_001 is the Big Belly Oak: the hollow, steel-banded oak by the A346, with its name sign in the photo. About 1,000 years old per Wikipedia; the reader says 1,100.
  - savernake-forest/svk_002 is the Brudenell Oak: a moss-green oak among golden beeches, with its name sign. The reader puts it at 410 years.
  - kingley-vale/kgv_001 is the ancient yews of Kingley Vale. The photo shows a fluted trunk inside a lattice of limbs, and the reader's note is quoted.
  - ames/amw_001 is a white-limbed American sycamore on a roadside bank in Ames, Iowa. The reader sent the same photo twice; both copies are marked as this tree. Ames is added to data/us-states.json.
  - All three places are new. Each has an intro, question texts and three FAQs.
- **Into the strips:** the Giant Tree (hum_001), the Tall Tree (hum_002) and the Great Cedar of Varese (var_001). The live-first step had already put them there. A second, identical Tall Tree photo was rejected as a duplicate.
- **Pin:** hum_001's approximate pin was 695 m off. It moved to the reader's GPS fix, taken at the trunk with the park's "Giant Tree, Champion Coast Redwood" sign. It is now confirmed.
- **Report 1000149** (St. Wolfgang's Oak, thm_001) was the "wrong location" chip alone: no words and no coordinate. The confirmed pin stays and the reader got the standard pin thank-you.
- **Mail replies 1667 and 1668**: the Raincliffe Woods tipster sent two what3words spots, without saying which is the beech and which the chestnut. Both spots are on the leads in data/leads/scarborough.json, not converted (no what3words key here). There is still no photograph or source, so both stay leads.
- **Still waiting:** sighting 3c544597 (Amsterdam, our own account) has no photo on disk. The older `mine` leads have no files on this runner either.
- qa (source) and preflight (0 problems) are clean; i18ncheck is clean.

## 2026-11-25 session: inbox, two interviews tomorrow

- **Sent** on Hidde's "verstuur alle mails hierboven", through Resend in their threads: Mattia Sartori (Il Dolomiti) Google Meet is fine, Thu 26 Nov 14:00; Lucas Barquero (Inspiring News, Spain) interview proposed Thu 26 Nov 15:00 on Google Meet; Marianne (Android tester, 70+, cannot get out much) the trees of the world from home, mistakes welcome.
- **Sent later the same evening**: Pete (his Play address was already on the "Android testers" list, checked in Play Console through Hidde's Chrome); Joey (Willistown, his White Oak mail of 11-23, which the inbox script had marked answered because an automatic mail about another of his trees went to him later); Stefano (Milan, tested fine: which Milan tree do we miss?); an Android tester whose link did not work (on the list; sign in to Play with that Gmail).
- **Fixed**: scripts/outreach_inbox.py counts a sent mail as an answer only when it is a reply on the same subject (Joey's case). Dave's two Raincliffe Woods what3words spots resolved and put on the right leads (the reader judge had them unassigned); still leads without a photograph.
- **CTV (Devika)**: our 11-24 mail asking her to resend the interview time to hidde@ is sent; no answer in the ancienttrees.app mailbox yet. A short follow-up in her thread on Monday if nothing comes.
- **Rules from Hidde**: calls we propose are Google Meet, never Zoom (mailcheck ZOOM PROPOSED); a tester who cannot get out much gets the trees of the world from home (drafts/HIS_VOICE.md).
- **No reply needed**: Waste Magazine has the article and asks for a reminder if no link within a few days (around 2026-11-30). The ancienttrees.app mailbox starts 2026-11-23; older threads (Joey and the rest) live in the old Gmail, which no script reads now.

## 2026-11-25 - Night run 2026-11-25 13:00 UTC ended without saying anything

Written by the workflow's Run health step, not by the run. 1.7 minutes of its 120 minute window (wall clock: cancelled before it could report its own duration), ended clean (cut off at the cap, no result record). 2 commit(s), none of them a published tree.

This entry exists because the run wrote none. The prompt asks every run to log even when it ships nothing, and a run that gives up is exactly the one that skips that instruction, so the count above is measured rather than reported.

What it cannot tell you is WHY the run stopped: no attempt left closing words on disk. If this shape repeats, the two things worth suspecting are the usage window and the refused commands.

## 2026-11-25 session: two holds overruled by Hidde, Bella di Ceciliano live, the Piazza Bra cedar under its lights

- **Live**: arezzo/arz_001 Bella di Ceciliano, a reader's downy oak outside Arezzo, on the register's coordinate, girth (570 cm) and height (24 m), Albero monumentale d'Italia 01/A390/AR/09; the reader's photograph leads, their 400 years stated as theirs. One tree, so no place page.
- **Gallery**: the reader's night photograph of the cedar of Piazza Bra under its Christmas lights, into verona/ver_001's strip behind the Commons lead.
- **Lesson** (Hidde: "is most likely a cedar", "Ja, zet ze live"): a photo sent for our tree from its square whose shape fits is that tree; a cropped screenshot is doubt_photo only when it is plainly someone else's; a register entry within about 50 m settles the tree. Written into BRIEF_READER_JUDGE.md.
- **Live** (Hidde, later: "Ja, zet live"): verona/ver_012, the reader's second Piazza Bra photo, a gold broadleaf behind the two flagpoles, species unknown and asked; pin on the gardens, approximate. Verona's counts in English and Italian now say eleven in the city; the Italian overlay has the tree.

## 2026-11-25 reader judge: first photograph of the Geneva Place du Cirque plane, a new lead for the George Green chestnuts

- **Live:** the first photograph of the Place du Cirque Plane (geneva/gen_006). It shows the one big plane on its island in the middle of the crossing, in autumn leaf. Its pin moved 13 m to the reader's GPS fix and is now confirmed.
- **Live:** two photographs of the George Green Sweet Chestnuts (london/lon_043), from one reader. The group shot of three chestnuts in autumn gold is now the lead photograph, the single crown went into the strip, and the old lead moved to the strip as well. The pin moved 69 m to the group shot's GPS fix and is now confirmed. The trees fill that frame, so it was not taken from far off.
- **Report 1000148** (Cambridge, the Milton Mulberry cam_002): a reader moved our approximate pin 5 m. I took their spot, it stays `approximate`, recorded `pin_source`, and sent the standard pin thank-you.
- **Still waiting:** sighting 3c544597 (Amsterdam, our own account) still has no photo on disk. The older Japan and Baarn leads (`mine` and September ones) have no files on this runner either, so none of them were judged.
- No feedback, tips or readers' words were waiting. qa (source), preflight and i18ncheck are clean.

## 2026-11-25 reader judge: a reader's photograph now leads the Battersea strawberry tree

- **Live:** a reader's photograph of the Battersea Park Hybrid Strawberry Tree (london/lon_025). It shows the red peeling limbs twisting up into the evergreen crown, in daylight, taken 3 m from our pin. It is now the lead photograph and the old one has moved into the strip. Verdict sight:84640469 is `publish`, and the reader's "it is live" mail goes after the deploy.
- **Still waiting:** sighting 3c544597 (Amsterdam). It comes from our own account (`mine`) and its photo is still not on disk, so it was not judged.
- No open reports, tips, feedback or readers' words were waiting. qa (source), preflight and i18ncheck are clean.

## 2026-11-25 session: US round 3 ready, on hold

- drafts/batches/press-us-local-round3.json (private, `on_hold`): 8 more US addresses on the approved text ("Recently" for "Earlier this month"): Charleston City Paper, South Carolina Wildlife, Big Island Now, Delaware County Daily Times, Audubon magazine, Friends of the Parks Chicago, Chicagology, Bronx.com. mailcheck clean, every address on the organisation's own page. Waits for Hidde after the answers to rounds 1 and 2 (about 12-02). That empties the useful US pool; a round 4 means new searching.

## 2026-11-25 reader judge: two Scarborough tips asked where they stand

- **Nothing went live this run.** A reader sent two trees in Raincliffe Woods near Scarborough as words only, with no photograph: a beech about 400 cm round, and a chestnut about 420 cm round that they say is believed to be the second oldest in the country. Raincliffe Woods is a large wood and neither tip names a spot. A quick search found no register entry or source for either tree, so there is no honest pin yet. Both are now leads in data/leads/scarborough.json. The reader gets the standard "where exactly does it stand?" mail (`hold_reply.py ... no_location`), which goes at the next knock. Verdicts tip:1654 and tip:1655 are `lead`.
- **Still waiting:** sighting 3c544597 (Amsterdam) is our own account's (`mine`) and its photo is still not on disk, so it was not judged.
- No open reports, no feedback waiting, no readers' words waiting.

## 2026-11-25 reader judge: a first photograph for Hajduk's Mulberry in Split

- **Live: split/spl_001, The Hajdukova Murva**, which had no photograph, now has a reader's photo as its lead. It shows the old mulberry in the Stari plac courtyard: one thick leaning trunk in a ring of fallen leaves, the crown turning yellow, and the club terraces behind. Species and setting match. It is filed in November. The pin did not move, because the coordinate the reader's app sent was our own pin, not a GPS fix. The reader was mailed.
- **Left for the next run, still:** sighting 3c544597 (Amsterdam). Its photograph is still not on disk, so it was not judged. The other waiting leads are our own account's photographs (`mine`), which a run never publishes.
- No open reports, no feedback waiting, no readers' words waiting.

## 2026-11-25 reader judge: a lichen-hung larch above La Salle, Aosta Valley

- **Live: la-salle/lsa_001, The Bearded Larch of the Col du Bard Path** (new one-tree place La Salle, Italy). A reader sent it through the app with four photographs, of which two frames were different. They show a broad, leaning old larch beside a mountain path, its limbs hung with beard lichen. The location comes from the photograph's GPS, so the pin is confirmed. One frame is the lead photo and one goes in the strip, both filed in August from the photo's own date. The reader's age (under 500 years) and girth (about 4 m) are stated as theirs. Their note mentions "the monumental Larch/Chavraz", which I could not tie to this trunk, so the page claims no name. Submission 1653 is a second send of the same spot a minute later, with no photo or words, so it gets the same verdict.
- **Left for the next run:** sighting 3c544597 (Amsterdam, 52.3972,4.8739). Its photograph is not on disk, so it was not judged.
- No open reports, no feedback waiting, no readers' words waiting.

## 2026-11-25 session: Android test invitation for the new Play app goes out

- **Google approved build 6** on 11-24, and the closed test "Alpha" is active. The opt-in link https://play.google.com/apps/testing/app.ancienttrees.map works: Hidde joined with his Workspace address, which was added to the "Android testers" list (now 773).
- **The invitation** (drafts/android-test-invite-new-app-2026-11-25.md; batch drafts/batches/android-test-invite-newapp-2026-11-25.json; Hidde: "verstuur maar eerst de eerste 100") goes to the wave 3 addresses that never had an Android invite: 88 never mailed, and 11 who had only other mail (marked with resend_reason). 677 of wave 3 already got the old-app invite on 11-20; they are skipped, as are the old Play list's 171, per Hidde. One address waits for its week's rest.
- **Route: Resend only, no Google contact at all.** out/tmp/send_resend_only.py runs the batch without Workspace credentials, so mailer.keep_copy() files no copy in Sent. 25 went at once, all via `resend`. The brake is blind (no RESEND_READ_KEY), so it allows 25 per run; the other 74 follow in three runs half an hour apart (out/tmp/newapp_rest.py).
- **Afternoon**: the second run sent 25, the third held on the outreach day cap of 100. On Hidde's "is het nog wel de moeite meer uitnodigingen te sturen zodat we die snel halen" (the 14 days only start at 12 opted-in testers), the cap is lifted for this batch and the last 50 of the first 100 go today in two runs (out/tmp/newapp_rest2.py). A tester asked for the invite on his other Gmail, his Play account: added to "Android testers" (now 774), and he got a reply through Resend (batch reply-pete-android-tester-2026-11-25). PostHog: build 6 on 8 phones, 3 of them new testers within an hour of the first mails; the old app ran on 164 phones in 30 days.
- **Evening: 12 testers reached, the 14 days run from 2026-11-25** (production access can be asked around 2026-12-09 if 12 stay opted in). On Hidde's "prima doe maar" to 300 more: the 678 left in the batch had all had the old-app invite, so the guard skipped them (old lane left alone). Wave 4 instead: 176 never-invited Gmail sign-ups (all app-download modal) added to "Android testers" (now 950; Hidde clicked the last save), batch drafts/batches/android-test-invite-newapp-wave4-2026-11-25.json with one new line ("If you use a different Google account in Play, just reply with that address and we'll add it."), 174 sending in Resend runs of 25 (out/tmp/wave4_send.py). PostHog: build 6 on 14 phones. Waitlist split: 2,305 unique; Gmail 1,149 old-app invite only (about 1,000 never used it), 879 non-Gmail never invited: the two pools left, Hidde's call.
- **Stopped by Hidde** ("stop dit hele initiatief"): the re-invite "The Android test has moved" to Gmail sign-ups who only had the old-app invite. 25 had gone (Resend) when he stopped it; the sender is killed and both batch files (android-test-reinvite-newapp-2026-11-25.json, the -b part of 300) carry `"status": "stopped_by_hidde"`, so no run sends them. Never restart it without his word. Wave 4 goes on.
- **Wave 4 done** (18:00): 174 of 176 sent through Resend in seven runs of 25; the other 2 wait for the seven-day rest (ends 11-26 and 11-29). Nobody with an old-app invite was mailed.
- **Wave 5** (Hidde: "zullen we die 108 niet gewoon mailen"): the 6 Gmail sign-ups of 11-25 got the invite through Resend; 5 are on "Android testers" (now 955). Play refused the sixth address (not a Google account), and with it in the field the whole save failed with only "Je wijzigingen kunnen niet worden opgeslagen": take the flagged row out and save again. That invite went before the list was checked; next time save and verify the count first, then mail.
- **Next, after Hidde's word**: the waitlist has 2,292 unique addresses, and 1,149 of them already had an Android invite. 168 Gmail addresses were never invited (out/play/wave4.csv); they first need adding to the Play list (out/play/newapp-list.csv = wave 3 + wave 4 + Hidde, one CSV upload). The 874 non-Gmail addresses can only join through a Google Group as tester list.

## 2026-11-25 session: inbox read, Il Dolomiti interview proposed

- Mattia Sartori (Il Dolomiti, L'altramontagna) asked for an interview. Sent on Hidde's "Verstuur" (Resend, in his thread): a video call proposed for Thursday 26 November at 14:00 CET. His answer will land in hidde@ancienttrees.app.
- Waste Magazine received the article and will publish "as soon as possible"; they asked to be reminded if no link has come in a few days. A session on or after 2026-11-30 checks wastemagazine.es and, if nothing is up, drafts a one-line reminder.
- No reply needed: Jakob's yes (Girona, handled by the reader judge), Alessandro's emoji, the Spokesman-Review and East Hampton Star auto-replies, a Notifier sales mail in spam, DMARC reports.

## 2026-11-25 session: a web error that sat orange as two, fixed

- **Fixed**: the card of a tapped pin on a phone-width city map threw "el is null" (Venice, Milan, Pisa, Vancouver; Chrome and Safari) when painting saves closed it again before it was measured. Live with the next deploy.
- **The gap behind it**: web_errors.py counted Chrome's and Safari's wording of that one fault as two orange types, and one wording was seen once the week before, so it never counted as new and never turned red, and no run picked it up. Now one fault is one type in every browser's words, and a known type firing more in a day than in the whole week before, on 3+ pages, is red too. Tests in scripts/test_web_errors.py.
- **For the runs:** health.py shows this error RED until its reports leave the 24-hour window (about 2026-11-26 08:00 UTC). The fix is on main, so do not fix it again. The iOS red at 08:29 was no macOS runner (capacity); a rerun is dispatched.
- The other two orange ones stay orange: a WebGL gap in Firefox 91 (maplibre's getExtension) and a one-off "Error: Na" from an old build.
- **Play Console is done** (Hidde, 2026-11-25): trader declaration, ID and phone are finished; the Play line under "Waiting for you" is closed.
- Reader 1433 (Tsagarada, the snowy night photo): the reply already went on 2026-11-24 10:01 UTC (submissions.replied_at). The "For Hidde" line was stale; nothing waits.
- Feedback 1603 (Girona, what the ambassador role involves) was answered on 11-24 and Jakob is ambassador; the ledger row said `needs_hidde` still and is now `handled`.

## 2026-11-25 session: 50 US local papers mailed

- Round 1 (25) went out overnight through Resend; round 2 (25) sent this morning on Hidde's word. 50 US local desks in about 40 places now have the Guardian mail with a tree of their own city. Read the answers in data/mail-yield.json (press) around 12-08.
- The mail brake ran blind: without `RESEND_READ_KEY` it cannot read bounces or complaints, so it only caps a run at 25. A read-only Resend key in the mail env and the repo secrets would let it stop on bounces.

## 2026-11-25 session: Suggested people keeps loading as you scroll

- Built on Hidde's yes ("Ja, bouw het"): under the ambassadors and the photographers of your places, Find people goes on with the public profiles who photographed the most trees anywhere, 20 at a time as you scroll, until the last one (297 public photographers today). Web on the next deploy, apps in their next build.
- **For Hidde: paste supabase/suggested-more.sql into the Supabase SQL editor.** The Management API token in ~/.ancienttrees-supabase.env is refused since 2026-11-25 ("Invalid access token"), so it could not be run from here. Until it is pasted the list simply stops where it stopped before.
- Checked: iOS unit test SuggestedPeopleTests.testMoreAppendsNewPeopleOnly; Android compiles; the web script parses. Not seen loading real pages, because the function is not on the server yet.

## 2026-11-25 reader judge: Bologna redwood photo live

- A reader's photograph of The Sequoia of the Giardini Margherita (bologna/bol_002) is on the page: the whole coast redwood from base to crown above autumn trees, 20 m from our pin, species and description match. Added as `add`, so it leads and the old photo moves to the strip; filed under November. The reader's mail went through sightings_publish --send. The pin catch-up could not read coordinates (HTTPError); our pin was left as it was.
- Left waiting: sighting 3c544597 (Amsterdam, sent from one of our own accounts as `mine`, "not sure which tree" near ams_032). Its photograph is not on disk, so it was not judged blind. It is our own photo and never auto-publishes anyway.
- No open reports, no unjudged feedback or tips, no reader words waiting to be quoted.

## 2026-11-25 night run (third attempt): nothing to ship

No claims standing. Same three READY leads (york, guimaraes, leamington-spa), already handed back by the write pass, so not redispatched. prepare.py's "awaiting a writer" pile is stale files or duplicates of live trees (passcheck --pending). Own research is paused. Reader photo tor_003 is the reader judge's. Nothing changed in the product.

## 2026-11-25 night run (second retry): nothing to ship

No claims standing. READY leads (york, guimaraes, leamington-spa) are the ones the earlier write pass already handed back. The rest of the "awaiting a writer" pile is stale or duplicates of live trees (passcheck --pending flags them; several would overwrite live ids). Own research is paused, so no verify pass. Two reader photographs wait for the reader judge (tor_003; 3c544597 is not on disk, so not judged blind). Nothing changed in the product.

## 2026-11-25 night run (retry, 5 min): nothing to ship

- Claims: none standing. READY leads: 3 (York, Guimarães, Leamington Spa), the same ones the earlier write pass handed back as unpublishable; not redispatched. Own research is paused, so no verify pass. enrich --next, recognise --stuck and reader_words: nothing to do. pagegaps shows only species and park pages, which the strict cut keeps out of Google, so left. health: green except 2 new web error types (maplibre `getExtension is not a function`), orange, not yet 3 pages. Nothing published.

## 2026-11-25 reader judge: the Turin ginkgo now leads in its November gold

- **Turin, The Ginkgo of the Giardini Cavour (tor_003):** a reader sent two photographs dated 2026-11-16. One looks up the straight trunk into the tiered limbs and the other shows the whole crown yellow on the lawn. Both match the species and the recognition line. The trunk shot is now the lead photograph (filed under November by its own date) and the old lead moves into the strip. The knock had already put it in the strip live-first. This run promoted it to lead, and the rebase kept that. The "it is on the page" mail is queued in data/photo-live-mailed.json for the next flush. The pin catch-up still could not read coordinates (HTTPError).
- Left alone again: lead 3c544597 (Amsterdam) and the older `mine` leads. They are our own account's photographs and their files are not on disk.
- No open reports, no feedback without a verdict, no tips, no reader words to quote. qa source, preflight (0 problems) and i18ncheck are clean.

## 2026-11-25 night run (07:00 window): Android photo viewer crash fixed, no trees

- **Rung 2, app crash:** Android build 5 crashed on one tester's phone (IndexOutOfBoundsException in PhotoViewer, Index 3 for length 3, plus two paired "no trace" exits) right after recording a sighting on Madison msn_001. The viewer's page index and the cross-fade's old page outlived a shrinking photo list; both reads in PhotoViewer.kt now clamp. No unit test (composable state, no seam); recorded in data/crash-fixes.json, health.py is green on crashes. For Hidde: next Android build carries fix for PhotoViewer IndexOutOfBounds.
- **Write pass:** the four READY leads (two Leamington Spa, York, Guimarães) came back unwritten: no source or reason to visit, a five-species row, and a cypress that sits in Paços de Ferreira with no life or access check. Nothing published. Own research is paused, so no verify pass.
- **Left alone on purpose:** the Turin ginkgo photo (tor_003) and one unplaced Amsterdam sighting belong to the reader judge. Web error "t.getExtension is not a function" in maplibre stays orange, not rung-2 sized.

## 2026-11-25 reader judge: the Madison tupelo now leads in its autumn red

- **Madison, The Carolyn Black Tupelo (msn_001):** the reader who sent yesterday's winter silhouette sent the whole tree in full maroon autumn colour, in daylight, at the Visitor Center as the recognition line describes. It is now the lead photograph and the winter shot moves into the strip. The file has no date, so the photo is filed under autumn (November) by its colour. Their second upload was the same photograph again, so it was rejected as a duplicate. Pin untouched: their coordinate is our own pin. The pin catch-up could not read coordinates (HTTPError), as in the last run.
- Left alone: lead 3c544597 (Amsterdam) and the old `mine` leads. They are our own account's photographs and their files are not on disk.
- No open reports, no feedback without a verdict, no tips to judge, no reader words to quote. qa source, preflight (0 problems) and i18ncheck are clean.

## 2026-11-25 reader judge: a reader's photograph now leads the Hamarikyu pine

- **Tokyo, The Three Hundred Year Pine (tok_006):** a reader's photograph from the app, taken today. It shows the black pine itself: the wide, low, layered crown on its log props behind the bamboo fence, in daylight. Added as the lead photograph, and the old one moves into the strip. Filed in November from the photograph's own date. Sender mailed by sightings_publish. Its pin catch-up could not read coordinates (HTTPError); the tree's pin was untouched.
- **Left for the next run:** the Amsterdam lead 3c544597 ("not sure which tree", near the Stationsplein elm). Its photograph is not on disk and it is marked `mine`, so it was not judged blind.
- No open reports, no feedback without a verdict, no tips to judge, no reader words waiting for a page.

## 2026-11-25 night window 00:51: checked, shipped nothing

- Rung 1: three new tree notes read, none on the closed list, marked seen. No reader backlog over 24h. The one unmapped reader photo (3c544597, Amsterdam) belongs to the reader judge.
- Rung 2: the only red was the iOS app, and both failed runs (45469395864, 45465810275) never got a macOS runner (GitHub capacity), so no test ran. Answered in health.py. Web errors orange: a maplibre `getExtension` TypeError and an "Error: Na", one page each, under the red threshold.
- Rungs 5 to 9: own research paused; 4 READY leads and 1 Taiwan entry sit under the six-candidate floor; no photo-less city has queued candidates; recognise has nothing stuck; the only page gaps are noindexed species pages (36) and 2 parks, left alone under the trim. No tree work available.
- 7-day visits line from prepare.py: not printed this run.

## 2026-11-25 session: the repo moved to the Ancient-Trees-Org organisation

- **Moved**: ancienttrees and ancienttrees-open now live under github.com/Ancient-Trees-Org (Hidde created the org; `scripts/move_to_org.py` rewrote the 7 files). The 25 secrets, Pages (ancienttrees.app, open.ancienttrees.app, both answer 200) and the github-pages environment came along. The Mac's remote points to the org. A deploy (run 45617756403) and a reader-judge run (45617763984) were dispatched on the moved repo as the test.
- **Still Hidde's**: a new fine-grained token for the Supabase trigger with the org as resource owner (the old one only reaches the personal account's repos; until then the 15-minute poll picks readers up), then paste supabase/reader-judge-trigger.sql again; the second person is invited as org Owner by mail (2026-11-25, accepted not yet seen). www needs nothing: it still answers 301 to ancienttrees.app after the move. Steps in .github/ORG_MOVE.md.

