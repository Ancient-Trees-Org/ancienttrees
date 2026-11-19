# LOG

<!-- archive-index -->

**Older entries live in the archive**, moved by `scripts/archive_logs.py`, nothing deleted:

- [2026-11](archive/LOG-2026-11.md)
- [2026-10](archive/LOG-2026-10.md)
- [2026-09](archive/LOG-2026-09.md)
- [2026-08](archive/LOG-2026-08.md)
- [2026-07](archive/LOG-2026-07.md)

So absence from this file is not evidence something was never tried: `grep -ri "<place>" archive/` before concluding a hunt is new. Re-running an exhausted hunt is this project's most repeated waste.
<!-- archive-index -->
## 2026-11-19 night run (rung 1): Palheiro stone pines live, Gdansk photographs, the fallen Ivy Elm retired

- New in the product: **The Stone Pines of Palheiro** (Madeira, mdr_012), a reader's photograph with GPS fix, age (planted 1837) stated as the estate sign's claim, Portuguese overlay extended. The reader's Madeira dragon-tree photo is held as `not_special` (young plants on a roadside viewpoint), GPS kept.
- Gdansk, Park Oliwski: the Cucumber Magnolia and the Giant Thuja got their first lead photographs (summer magnolia, autumn frame and the thuja plaque in the strip), the katsura's plaque and label joined its strip, Melbourne's holm oak kept its strip photo. Six weak or ambiguous frames held (underexposed, snow, bent conifers not clearly the thuja).
- Wrong on the site: two readers' photographs (2024-06 and a snow day, Pomnik Przyrody plaque on the trunk) show **the Ivy Elm of Park Oliwski (gda_012) lying fallen**. Retired with `retire.py`; Gdansk and park-page counts and copy rewritten (twelve to eleven, six to five).
- Also fixed: two colon reveals, Madeira counts (twelve). Still open: 3c544597 (unnamed, Amsterdam coordinates, photo not on disk).
- Rung 5: a verify pass on Birmingham (top of the UK-first list, 0 trees) came back dry for the eighth time and shipped nothing; the only route left is a browser read of the Botanical Gardens' Garden Explorer tour #12 (lead updated). Venlo was claimed and released unworked (Netherlands is over-represented), so it is a wall for 48h. Rung 2 was clear (web error orange: one new TypeError, below the red threshold).
- For Hidde: nothing.

## 2026-11-19 reader judge: Gdansk maples get their first photograph, two more of the Melbourne fig, magnolia and cedar girths from readers

- **Gdansk, The Maples of Hugo Conwentz (gda_007)**: a reader's photograph of the trunk by the Abbots' Palace, a fresh natural-monument plaque being hung (May 2026), is now its lead photograph; the tree had none. Their second photo (the palace and parterre, the maples not picked out) rejected as a bad frame. gda_007's story lost a colon reveal now that the page carries a photo.
- **Melbourne, The Leaning Fig over the Boardwalk (mel_018)**: two photographs from a second reader, both this fig, went into the strip behind the finder's lead, which shows the whole curve best.
- **Gdansk, The Cucumber Magnolia (gda_009)**: two reports with the reader's own words: 328 cm round in 2026 (register: 271), and three cucumber magnolias in the park, the second (308 cm) close by. Both now on the page as the reader's, story and recognition line; closed `holds`, no mail (their own words).
- **La Tène, Préfargier cedars (prf_001)**: the reader's mail reply gave about 4.23 m round at 1 m; on the page as theirs. They also ask to rename the commune "Laténa" (the federal name is La Tène, not changed) and to be ambassador. Feedback 1240 `needs_hidde`, draft in drafts/reply-reader-1240-2026-11-19.md. Feedback 1241 (Old Knobbley, on Android, will send when they can) handled.
- **Not judged**: lead 3c544597 (Amsterdam area, "not sure which tree"): photograph not on this runner, left for the next run. The older `lead` rows in _sightings.json (Nara, Kyushu, Tokyo, Baarn, mostly our own account's test photos) also have no file here.
- For Hidde: the La Tène reader wants to be ambassador and the commune named Laténa; see the draft.

## 2026-11-19 session: the Android invitation filled Resend; waitlist batches now go through Gmail

- **Breakage**: the 100 Android test invitations went through outreach_send.py, which always sent as a first mail to a stranger (Resend). Resend's free 100 a day was full by 09:36. Until midnight UTC, sign-in and welcome mail to Yahoo, Apple-relay and BT addresses falls back to unsigned Gmail and may bounce; everyone else is unaffected (Gmail is their route anyway).
- **Fix**: a batch file may say `"kind": "expected"` (people who asked to hear from us: waitlist, testers) and then goes through Gmail, Resend only for the Yahoo/Apple/BT addresses in it. The Android batch carries it, so tomorrow's 68 do not touch Resend.

## 2026-11-19 session: 31 outreach replies found in Gmail Spam, mail readers now read Spam

- **What happened**: Boomzorg (NWST) asked for an interview on 11-02 and 11-12; both mails sat in Gmail Spam, and only today's from redactie@ reached the inbox (Hidde has answered it). Spam held 31 replies from people we wrote to, from 10-20 on: Londonist, Irish Wildlife Trust, Biorama, Waste Magazine, The Simple Things, Uncover Liverpool, Lausanne Tourisme, esMadrid, Hookuleana (Honolulu), Glasgow Necropolis, Dendrologische Vereniging, Arboretum Wespelaar, urban.brussels, Huerto del Rey Moro, Lobo do Mar, Richard Bright (Cramond), Bill Guion, readers (Old Knobbley among them). Likely cause: info@ reaches Gmail through ImprovMX forwarding, which Gmail trusts less. Gmail deletes spam after 30 days.
- **Done, on Hidde's yes ("Ja, doe beide")**: the 31 moved from Spam to the inbox (the rest of Spam is junk and DMARC reports). `outreach_inbox.py` and `reader_mail_replies.py` now read INBOX and Spam (still readonly; a spam hit prints "IN SPAM: mark it Not spam"). Also fixed a crash in outreach_inbox.py's answered/owed comparison when a Date header has no zone.
- **Still owed a reply** (from spam, never answered): Londonist, IWT, Biorama, Waste Magazine, The Simple Things, Uncover Liverpool, esMadrid, Hookuleana, Glasgow Necropolis, Dendrologische Vereniging, Arboretum Wespelaar, urban.brussels, Huerto del Rey Moro, Lobo do Mar, Richard Bright, kabelmail (Frankfurt), Lisa Prest. Run `outreach_inbox.py --read --since 2026-10-20` for their words.
- **For Hidde**: a Gmail filter "To: info@ancienttrees.app → Never send it to Spam" stops this at the source.
- **Then, on his "Ja, maak concepten"**: ten reply drafts (drafts/reply-*-2026-11-19.md, mailcheck clean), waiting for his yes one by one. Done first: new-orleans/nol_007 (Martha Washington oak) corrected on Bill Guion's mail (Live Oak Society founded by Dr Edwin Lewis Stephens, 1934 rule 16 ft), as a local account; his doubt that she still stands is in verify_notes. out/mail/ancient-trees-bruxelles-35-arbres.xlsx made for urban.brussels. Open after replies: Arboretum Wespelaar gave written permission for their Beltrees photos ("mits vermelding ©Arboretum Wespelaar", 2026-10-29), Brussels photo work; Uncover Liverpool invites a free news piece (needs an account, his).

## 2026-11-19 session: Android test invitation sent to the first 100

- **Google approved the closed test** (release 2, "available to selected testers" since 2026-11-18 16:32; Play sent no mail about it, it only showed in the console).
- **Mail sent on Hidde's "stuur maar gewoon uit"**: his own text (drafts/android-test-invite.md) to 100 of the 172 waitlist addresses on Play's tester list, through outreach_send.py; the other 68 the same afternoon through Gmail on his "kunnen we niet gewoon via gmail sturen?" (168 in all). Four had another mail from us within the week and wait until 2026-11-24 (command in the draft). Play showed 5 testers opted in that afternoon, and **12 by the evening of 2026-11-19: the 14 days run from then, so production access can be requested from about 2026-12-03** (Dashboard > Apply for production; keep notes of tester feedback and fixes for its questions).
- **Next**: watch the opted-in count on the Alpha track; the 14 days start at the twelfth tester.

## 2026-11-19 reader judge: the Kasama leaf-seed ginkgo live from a reader's tip
- **Live, new place: kasama/kas_001 The Leaf-Seed Ginkgo of Inada Gobo** (Ibaraki, Japan), from a reader's website tip with no photograph (submission 1233, `tip:1233` publish). Ibaraki Prefecture's own record (kyoiku.pref.ibaraki.jp/bunkazai/ken-160) names it: a prefectural natural monument since 2000 at Sainen-ji, 469 Inada, girth 7.5 m, height 35 m, spread 23 m, more than 300 years, vigorous; temple tradition says planted around 1218 in Shinran's time. Register plus the reader's report from this autumn as the life check. Pin approximate at the temple (OSM node), no photograph yet; the reader's girth matches the register's. One tree, so no place page on the web.
- **For a session: our Mito page (mit_001) calls the Shirahatayama tree the largest leaf-seed ginkgo known**, while Ibaraki's register gives the Inada tree the wider trunk (7.5 m against 6 m). The Kasama story states the register's comparison as the register's and claims no crown; the Mito line wants a look.
- Nothing else waited: no reader photographs in the queue, no open reports, no feedback without a verdict, no reader words to quote. Still open: 3c544597 (our own account, file not on this machine).

## 2026-11-19 reader judge: one Adelaide report and one mail reply, nothing new live
- Nothing changed on the site. No new trees or photographs waited; the one lead left, 3c544597, is our own account and its file is not on this machine, so it waits again.
- **Report 1000088 (Adelaide, ads_002 The Red Gum of Glynburn Road)**: the reader gave "364 Glynburn Road, Kensington Gardens", which is already our address. The pin is a reader's GPS fix at the tree (confirmed), so it stays. tree_reports.py counts the address as the reader's own words, so no standard thank-you: closed `holds`, suggested answer in drafts/reply-reader-1000088-2026-11-19.md.
- **Feedback 1232 (mail reply to row 1120)**: the reader turns down the ambassador role (they do not live there), asks what height girth is measured at, and says they love the site. Closed `needs_hidde`, suggested answer (1.3 m, the register standard) in drafts/reply-reader-1232-2026-11-19.md; closed in reader_words.py as not about the tree.

## 2026-11-19 reader judge: the rest of the batch, six trees live, the Anseman doubt settled
- Same reader's batch as the runs below; Serenbe and the McDonogh photo were already in from them, so this run rebuilt its work on top of theirs. Every photograph viewed.
- **Live, new place**: islamorada/isl_001, the banyan of The Banyan Tree garden and shop, 81197 Overseas Highway (visitor listings as source; named only as a fig, the reader says Indian banyan). Islamorada added to us-states.json and city-aliases.json, with intro, question texts and three FAQ. One tree, so no place page on the web.
- **Live in existing places**: key-west/kyw_007 The Elephant-Foot Kapok (Old Town), kyw_008 The White Street Kapoks (beside City Hall, two photos), san-diego/sdg_014 The Dragon Tree of La Jolla Cove, sdg_015 The Fig with the Long Arms on Sixth Avenue (Balboa Park edge, species left as Ficus sp.). All pins are the reader's GPS fixes.
- **sdg_001 Balboa Park Moreton Bay fig**: the reader's photo (GPS 12 m) now leads, the Commons one moves to the strip.
- **The Anseman doubt the parallel run logged, settled**: f37a9e16 is 126 m north of the Anseman's GPS pin with a different trunk, so it came out of nol_002's strip and is live as **new-orleans/nol_009 The Oak by the Bayou Metairie Lagoon**.
- Counts: San Diego intro and FAQ no longer count trees, Balboa Park page 5 to 6, New Orleans intro, meta, question and FAQ eight to nine, City Park page 6 to 7. The McDonogh story's colon reveal rewritten (the check applies now it has a reader photo).
- Three reader-judge runs took the same batch at once again; worth a look at the trigger's de-duplication. No open reports, no feedback without a verdict. Still open: 3c544597 (our own account, file not on this machine).

## 2026-11-19 reader judge (parallel run): Serenbe access made honest, one doubt on the Anseman strip photo
- This run judged the same six sightings as the two runs below, in parallel, and reached the same verdicts on all but one; their versions are kept and mine dropped before push. Three reader-judge runs at once on one reader's batch: the trigger fired per sighting.
- **Serenbe (srb_001, srb_002)**: Serenbe's own trails page says the trails are for residents and Inn at Serenbe guests and open to the public only at the twice-yearly Serenbe Trail Race. Access lines, question_context and the "Can I visit them?" FAQ now say that instead of "not confirmed", with the page as a source.
- **Doubt, left as it is: the second Anseman Oak photo (f37a9e16, in nol_002's strip).** Its GPS is 126 m from the Anseman's own reader-GPS pin, and the trunk is smooth and forked where the lead photo shows a mass of burls; I think it is another City Park oak. A strip photo, so low harm. A later run or session with a second view can decide: `sightings_publish.py --unstrip f37a9e16-ce5b-48ab-a115-8f435303f92e`, then judge it as a new tree.

## 2026-11-19 night run, second attempt: nothing publishable found
- Shelf empty: leads.py --ready 0, only 3 verified trees awaiting a story (fort-lauderdale 2, taiwan 1). Birmingham verify pass (seventh dry one): 0 trees, one Sutton Park holly lead added (ATI 268643, single source, not a collectible trunk); claim released. Porto and Portland are full (32 and 33 against 30), Zurich and the other focus cities are walls. Translations stay paused (TRANSLATIONS_OUT).
- Still open: 3c544597 (Amsterdam), photo file not on this machine, not judged blind.

## 2026-11-19 reader judge: two Serenbe trees, two New Orleans photographs
- **Live: serenbe/srb_001 Grandfather Pine and srb_002 Grandmother Beech** (new place in Chattahoochee Hills, Georgia, added to data/us-states.json). One reader's two photographs, both viewed, each with a GPS fix at the tree; pin confirmed. The pine is a loblolly with a candelabra crown among straight ones; the beech leans over a small waterfall. No age or girth anywhere, and the pages ask. Access says plainly we have not confirmed which paths are open.
- **New Orleans:** the McDonogh Oak's held lead photograph is replaced by the reader's (daylight, the propped crown); the Anseman Oak already had the reader's photograph in its strip, so it stays there. Preflight flagged a colon reveal in the McDonogh Oak's older story and it is rewritten.
- Still open: 3c544597 (Amsterdam, our own account), file not on this machine. Deploys 44453549235 and 44455643446 were running; the "failing on schedule" line in the start-of-session notice is a scheduled deploy cancelled by the concurrency group (44445919322), not a failed build.

## 2026-11-19 reader judge: the Fort Screven oak and Yellowstone's Petrified Tree
- Same reader as the ginkgo below; this run judged the two leads the run below did not reach (the ginkgo and Key West photos were already in from it, its versions kept).
- **Live: savannah/sav_004, The Fort Screven Bakery Oak** (Tybee Island, about 24 km from Savannah). A broad live oak in front of a brick Fort Screven building, seen from the path, GPS fix; the "bakery" name is the reader's and the page says so. Savannah intro rewritten for four oaks (89 words).
- **Live: yellowstone/yel_001, The Petrified Tree** (new place, Wyoming added to data/us-states.json). A fossil redwood, not alive: shipped under the standing-dead exception (standing, striking, GPS pin), and the page says plainly it is a fossil. Facts from the NPS Tower-Roosevelt page (ancient redwood, buried 45 to 50 million years ago); the fence reason is put as what travel guides say. One tree, so no place page on the web.
- Still open: 3c544597 (Amsterdam), our own account's photo, file not on this machine.

## 2026-11-19 reader judge: the Adair Park ginkgo, two Key West photos
- **Live: atlanta/atl_012, The Adair Park Ginkgo** (Decatur, Georgia). A reader's two photographs (both viewed) of a big single-trunked ginkgo in full autumn gold by the picket fence of Adair Park, with a GPS fix at the tree; pin confirmed. No register entry and no source names it (the DeKalb History Center's plaqued ginkgo is at the Old Courthouse, not here), so it ships on the closed list as a reader's tree; the sign beside it is unreadable in the photos and the story asks readers what it says. best_time November autumn colour. The Atlanta intro now says eleven of the trees come from the champion list and a reader sent the twelfth.
- **Key West, two reader photographs added as lead** (`add`, the earlier reader photos stay in the strip): kyw_003 The Kapok Tree (its buttressed foot with the courthouse behind) and kyw_004 The Cosgrove House Banyan (the whole banyan from the Whitehead Street sidewalk). Species and setting checked against each entry. The pin catch-up could not read coordinates (HTTPError); both trees' pins were already within 15 m of the photos.
- Still open: 3c544597 (Amsterdam, our own account, `mine`): its file is still not on this machine; never judged blind. The other waiting `mine` leads are our own account's sightings, not readers'.
- No open reports, no unjudged feedback, no reader words waiting.

## 2026-11-19 reader judge: the Palm Beach kapok
- **Live: palm-beach/pbh_001, The Royal Poinciana Chapel Kapok** (new place, Palm Beach, Florida). A reader's four photographs (all viewed) plus a GPS fix beside it on the Lake Trail. It is Florida's state champion kapok in the Florida Forest Service register (PK 1124: 899 in round on its buttresses, 74 ft, crown 132 ft, measured 2017), so girth_cm 2283 and height_m 22.6 come from the register; the reader's 190 years is on the page as their estimate. Lead photo is the frame with no people in it, the other three in the strip. One tree, so no place page on the web (PLACE_PAGE_MIN_TREES); state Florida added to data/us-states.json; city_names.py matched West Palm Beach by mistake, so the alias was corrected to Palm Beach, Florida.
- Still open: 3c544597 (Amsterdam, near ams_032) is our own account's photo (`mine`) and its file is not on this machine; left for a run that has it, never judged blind.
- No open reports, no unjudged feedback, no reader words waiting.

## 2026-11-19 night run (window from 01:37 UTC)
- Rung 1: one reader photo (3c544597, 52.3972 4.8739) is not on disk here, so it stays open; never judged blind. Rung 2: health clear.
- Rung 5/UK first: Birmingham verify pass found 0 publishable trees (no naming body, no tree coordinates; leads still single-source). Next angle: a reader GPS fix at the Botanical Gardens beech or the Highbury Park veteran survey. Claim released.
- Fort Lauderdale verify pass: 2 trees verified (ftl_011 Las Olas bridge Canary Island date palm, ftl_012 Flamingo Gardens apple blossom tree), 5 rejects kept as leads. Not written (under six, no write pass). Claim left open for the next writer. 7 of 10 live trees there are behind paid entry, so free ones matter.
- Hosts that failed: ffs.fdacs.gov detail pages (Wayback only), flamingogardens.org 403. Nothing published this window; nothing for Hidde.

## 2026-11-19 reader judge (second run): tree notes read, the Maits Rest beech was already done

- A second reader-judge run judged the same Maits Rest sighting in parallel and reached the same verdict; its duplicate was dropped in favour of the entry below. What it adds: two new tree notes read (pwt_001 Ada Tree, nij_017 Nijmegen copper beech), nothing on the closed list, both stay, marked seen.

## 2026-11-19 reader judge: the Maits Rest myrtle beech live near Apollo Bay

- **New tree, apollo-bay/apb_001, The Myrtle Beech of Maits Rest**: a reader's app photograph with a GPS fix on the Maits Rest Rainforest Walk (Great Otway National Park, 12 km west of Apollo Bay). Fused red-brown trunks among ferns, daylight, colour, plus the reader's own shot of the Heritage Tree disc. The National Trust of Australia's Register of Significant Trees (trusttrees.org.au) lists it: about 200 years, 30 m, "possibly 2 or 3 trees which have grown together". So it has a source and a register link, the pin is `confirmed` from the GPS fix, and the access line says it is free. It is a new one-tree place, so it has no place page yet. It comes from the same reader as wee_001 but is 13 km from it, so it is a different tree. The intake's name for it ("near Weeaproinah") came from reverse geocoding and was wrong.
- Still open: 3c544597 (Amsterdam, near ams_032) still has no photograph on this machine (`fetch_waiting_photos.py` says nothing waits), so it got no blind verdict. The older leads (Nara, Kyoto, Taketa, Tokyo, Baarn) are September and October verdicts, most of them our own account, and none of their photographs is on this runner. I did not re-judge them blind.
- No open reports, no feedback without a verdict, no tips, no reader words waiting.

## 2026-11-18 reader judge: the Ada Tree gets a daylight lead photo and its real pin

- **Powelltown, the Ada Tree (pwt_001)**: a reader's daylight photograph from the fern gully is now the lead (`add`); the earlier reader's dusk frame moves to the strip. Both readers' GPS fixes agree within about 15 m, about 890 m west of our approximate pin, which sat at the picnic area where the 3.6 km loop starts. The pin moved onto the tree by hand (sightings_publish refuses moves over 300 m), now `confirmed`, `pin_source` says why; the address now names the reserve and the walk.
- Left open: 3c544597 (Amsterdam, near ams_032, our own account) still has no photograph on this machine, so no blind verdict.
- No open reports, no feedback without a verdict, no tips, no reader words waiting.

## 2026-11-18 night run, second attempt: shelf dry, nothing shipped

- No change to the product. READY leads: 0. Verified files under data/research/ are stale or duplicates of live trees (Cyprus, Croatia, Cardiff, Granada and others fold into trees already live under other ids).
- Claims tried: portland (33/30) and munich (63/60) refused as full; london claimed and released (0 of 30 leads carry a coordinate, now a 48h wall); spokane claimed and released (1 unmined of 19, under the six-candidate floor, now a 48h wall). Both walls are in data/walls.json.
- Left open: 3c544597 (unmapped, Amsterdam 52.3972 4.8739) has no photograph on this machine, so no blind verdict. Translations stay paused (`TRANSLATIONS_OUT`). Zurich register is walled.
- Next run: refill is the real gap (907 leads need only a source); a verify pass on one of those batches, not another staged city.

## 2026-11-18 reader judge: two more Nijmegen beech photographs judged

- The same reader's other two photographs of nij_017 were already in the gallery from the knock's live-first step: the trunk with the red-brick church right behind it, and a view straight up the trunk to the fork. Both are looked at and judged the same tree (smooth grey beech bark, the church beside it). They stay in the gallery behind the lead. This run overlapped the one above and started on the same three photographs; its duplicate commit was dropped, and only these two verdicts were added.
- 3c544597 (our own account, `mine`) is still unjudged and not on this machine. Nothing else waits.

## 2026-11-18 night run (window from 23:09 UTC)

- **Two more beech photographs** for nijmegen/nij_017 judged by eye (full beech by the church, trunk and crown, both autumn, daylight) and recorded as `add`; live-first had already put them in the strip. Their judgement stubs were missing (the scan only reads the queue), so I wrote them through `judgement.save`.
- **Key West**: kyw_005 (Cuban Lignum Vitae) and kyw_006 (Boardwalk Barringtonia), garden champions with admission now sourced ($15, 10 to 4 daily), merged app-only. Pins are the register point (approximate); `location_site` radius 50 m is a judgement call and may be too wide for a garden. The city intro still says "two remarkable trees" and wants a rewrite.
- **Dry**: Birmingham (sixth pass, no angle left; needs a reader GPS fix or the Friends of Highbury Park survey), Philadelphia (exhausted; one lead added, the Lutheran Seminary scarlet oak). Portland is full, Miami a wall.
- **Stuttgart** dry too (Hohenheim's owner leaflet of record trees is now a lead; the 1779 tulip tree needs a pin). Madeira has no coordinates on its leads, left alone.
- **Page gaps**: ten species intros (chinkapin, black, chestnut, shumard oak, white ash, Spanish black pine, Persian ironwood, carob, tamarind, rock elm) and the Serbia country intro, each from its own trees. These pages stay behind the strict cut for Google.
- 3c544597 (Amsterdam, `mine`) still has no photo on this machine, left open. Health: all green. Prepare.py: 7-day visits line not printed this run.

## 2026-11-18 reader judge: the Nijmegen copper beech gets its first photograph

- **Photo live**: The Copper Beech of the Antonius Abtkerk (nijmegen/nij_017) had no photograph. A reader sent one from the tree's page. It shows one big beech in coppery autumn leaf with a smooth grey trunk, on the planted strip beside the red-brick church and rectory buildings on the street. It is now the lead photo (sighting b496e5e0, through sightings_publish.py). The light scored WEAK, but a reader's photograph is never refused on light. The pin was not moved, because the row's position was our own pin and not a GPS fix.
- The photo makes the page reader content, so it is indexable, and preflight then flagged an old colon reveal in its story ("predates Cuypers by centuries: an older church..."). That sentence is now two sentences in English and Dutch.
- 3c544597 (Amsterdam, our own account, `mine`) is still unjudged and its photo is not on this machine. No open reports, no tips, no feedback without a verdict, no readers' words to quote.

## 2026-11-18 reader judge: a fern-lined myrtle beech in the Otways goes live; the Signal Tree held again

- **New tree, new place**: The Fern-Lined Myrtle Beech of the Otways (weeaproinah/wee_001). A reader sent four photographs with a GPS fix: a myrtle beech in the Otway rainforest whose long limb is lined end to end with kangaroo ferns and moss, shot from above with tree ferns in the gully below. The fix is about 700 m from the Otway Fly Treetop Walk entrance (official coordinates, otwayfly.com.au). The photos look down from canopy height, which fits the walkway, but the reader does not say so, so the access line says which path or walkway is unconfirmed. It is a one-tree place: no place page, only the tree page. city_names.py found no Wikipedia article for Weeaproinah.
- **Held, `not_public`**: the Signal Tree in Akron (sighting a882dcb4, submission 1208). Three good photos of the three-stemmed bur oak and its 1986 plaque. It is the same tree as tip 1115 (data/leads/akron.json). Summit Metro Parks' alerts page, read today, still says the Chuckery Area is closed through at least 2028. The standard not_public mail talks about private property, which is wrong here, so no automatic mail went. The suggested answer for Hidde, drafts/reply-reader-1115-2026-11-17.md, now notes the new photos. For Hidde: the reader stood at the trunk today, so if they answer that the area is open, the tree goes live with their photos.
- 3c544597 (Amsterdam, our own account) is still unjudged: it is `mine`, so the photo fetch skips it and it is not on this machine. Nothing judged blind. No open reports, no feedback without a verdict, no readers' words to quote.

## 2026-11-18 reader judge: the giant chestnut of Mont Mourex goes live

- **New tree, new place**: The Giant Chestnut of Mont Mourex (divonne-les-bains/dvn_001). A reader sent a photo with a GPS fix of a huge, twisting sweet chestnut in autumn leaf in a picnic clearing, plus a second photo of the plaque beside it. The plaque, from the ONF and the town, calls it the largest and oldest tree of the Divonne forest: 6.25 m round, 26 m tall, about four centuries old. The girth, height and age on the page come from that plaque. It is a one-tree place, so it gets no place page and only the tree page. The same reader's earlier tip without a photo (tip 1175, data/leads/geneva.json) is now marked published.
- One lead is left open: 3c544597 (Amsterdam, near the Last Elm, sent from our own account). Its photo is not on this machine, so it waits for the next intake. It was not judged blind.
- One mail reply (thanks) closed as handled. No open reports, no readers' words to quote.

## 2026-11-18 reader judge: a named oak in Rude Skov goes live, a third Tule photograph

- **New tree**: Brewer Jacobsen's Oak in Rude Skov (copenhagen/cop_050), a reader's photo with a GPS fix of a big open-grown oak, bare in mist, beside a gravel path. It goes under Copenhagen as a day trip (S-train to Holte), next to the Dyrehave trees. Its name is on Naturstyrelsen's Rude Skov map. We have no age or girth for it, and the page asks readers for them.
- **El Árbol del Tule**: a reader's close view of the buttressed trunk is now in the gallery. The current lead photo, also a reader's, stays because it shows more of the tree. Their two further frames stayed in out/.
- Fortingall and Reelig: the photos were already in the gallery through live-first. The verdict is `strip`, and the Reelig frame showing two people is not used.
- Eight tree notes read, none hidden. One mail reply (thanks, "will post while travelling") closed as handled. No open reports, no readers' words to quote.
- Still left: 3c544597 (Amsterdam, our own account, photo not on disk).
## 2026-11-18 (session): app checks for the first Android update, on Hidde's yes

- **What changed in the apps** (next TestFlight build and the Android build after 0.1.0 (2)): signed-out My trees on Android opens just high enough to show Sign in at big text on a small phone (the half stop fits short content; the iPhone already opens one stop higher on small phones); Move the pin on Android takes the Android form bar (close X, title beside it); a tree's hero photograph is named "Open the photograph" for TalkBack and VoiceOver (it was an unnamed button).
- **Fixed in the tests**: Android's daily ButtonWalk had not finished once from 11-14 to 11-18. Every push to main cancelled it (android.yml now gives the schedule its own concurrency lane), and when it ran it flagged the Map tab on the map's bar stop, which rightly does nothing (now quiet in both apps' lists, as on the other map stops).
- **Checked, nothing to change**: cold start of the Play apk on a 720x1280 emulator, trees listed after 4 to 5 s with app data, 8 to 10 s on a first launch (polling adds about a second); TalkBack audit of map, Discover, My trees, settings and a tree page (only the hero was unnamed; edge-clipped chips are not); Play Data safety already declares precise location (the place of a sighting) and photos, which covers a gallery photo's GPS; tip 1175's missing photo came from an iPhone on Mont Mourex and is most likely still queued on that phone (1177's arrived 16 minutes late); camera copies already carry the phone's fix since this morning.

## 2026-11-18 reader judge: overlapped the night run's retries, nothing new

- I judged the same seven app photographs: four Salt Lake City leads, plus strip photos for Fortingall, Jardine and Reelig. My readings matched what earlier runs had already pushed, so I dropped my commit and kept theirs. Main passes preflight.
- Still left: lead 3c544597 (Amsterdam), from one of our own accounts, with its photo not on disk. The older Japan and Baarn `lead` rows have no photo on disk either. No open reports, feedback or readers' words.

## 2026-11-18 night run (third attempt): Birmingham and Potsdam verified, 0 trees shipped

- No product change. Birmingham verify (UK, from-zero on): nothing meets the bar again; the Uffculme yew in Kings Heath was felled in 2016 (blocked), a Grove Park cedar and a Highbury Park 515 cm oak added as leads (no coordinate, no photograph). Potsdam verify: already published, its 27 open leads held for private plots or no placeable pin; the Naturdenkmal 54 oak stays a lead.
- READY leads 0. Porto, Portland, Munich and Vienna are full and refuse a claim; Sheffield, Leeds, Braga, San Francisco and the rest are walls. Both claims released.
- Next: the verify shelf needs sources, not more passes on these cities. Try Spokane (18 of 20) or a register scout (Zurich BUILD) in a window with a fresh angle; translation lane is paused while TRANSLATIONS_OUT holds.

## 2026-11-18 night run (second retry): inbox already clear, Birmingham verify dispatched

- Rung 1: `prepare.py --status` listed seven reader photographs as waiting, but sightings_inbox.py shows 550 of 552 handled; the four Salt Lake City ones are already live (see the reader judge entry below) and the two queued are the Fortingall and Reelig strips, judged. Nothing to apply. The status line is stale on these.
- Portland and Porto are full (refused); claimed Birmingham (UK, from-zero on, first in city_queue --next) and dispatched a verify agent. Result and merge follow in the next entry, or the claim expires in 4 hours.

## 2026-11-18 night run (retry window): two reader strip photos judged, Braga a wall

- Live: reader photographs on the Fortingall Yew and the Reelig Glen giants are judged (publish, strip) and live; a duplicate Jardine Juniper photo from a rebase conflict was dropped. Earlier attempt's commits clashed with the reader judge's own; its duplicate Salt Lake City commit was skipped.
- Braga verify pass: 0 new trees (Tibaes cerca still closed, rest outside the municipality); wall for 48h.
- Nothing else: READY leads 0, and Porto is full. Verify shelf still needs refilling (909 leads need only a source); next: a verify pass on portland, spokane, munich or potsdam.

## 2026-11-18 reader judge: five Utah photographs from one reader, four trees get their first picture

- Live: a reader's photographs are now the lead picture of four Salt Lake City trees that had none: the Temple Square Cedar of Lebanon (slc_005), the Washington Square Ohio Buckeye (slc_003) and Hackberry (slc_002), the Liberty Park London Plane (slc_001). Each looked at, species and setting match. Their Jardine Juniper shot (lgc_001, hikers on the platform under the twisted trunk) is added as the lead; the earlier photograph stays in the strip. Reader mails went through sightings_publish --send.
- Stories: the photos make slc_001 and slc_005 indexable, which tripped the colon-reveal check; three sentences rewritten. The cedar's story asked whether it came through the temple renovation; it now says a visitor's November 2026 photograph shows it full and green.
- Pins: no moves (the Liberty Park and Jardine coordinates are our own pins, not GPS fixes); the pin catch-up step hit an HTTP error reading coordinates, harmless here.
- Still left: lead 3c544597 (Amsterdam, our own account), photograph not on disk, not judged blind. No reports, tips or feedback open.

## 2026-11-18 night run (18:04 window): nothing new published

- Rung 1: the one open item, lead 3c544597 (Amsterdam, near ams_032), is from one of our own accounts (`mine`) and its photograph is not on disk, so no verdict, not judged blind. Left open.
- Rung 2: health only red on dropped knocks (6 of 12), not mine to fix.
- Shelf empty (0 READY leads); Birmingham verify pass (new angles: churchyard yews, Bournville, Aston Hall, Handsworth) found 0 trees; Uffculme yew is a stump and Perry Barr yew only an 1898 photo, both added as leads; claim released. Zurich, San Francisco, Fort Worth, Frankfurt are walls. Portland is full. Page-gap intros left alone (all noindexed under the strict cut). Visits line not printed by prepare.py this run.

## 2026-11-18 reader judge: overlapped a parallel run, nothing new

- Judged the same Fort Greene elm photograph (approve, same reading) but the run above had already pushed it; its version kept, this run's commit dropped.
- Still left: lead 3c544597 (Amsterdam, near ams_032), sent from one of our own accounts (`mine`); fetch_waiting_photos skips it, so its photograph is not on disk and it was not judged blind.

## 2026-11-18 reader judge: Fort Greene elm photographed and re-pinned

- Product: The English Elm of Fort Greene Park (nyc_027, New York) has its first photograph, a reader's, and its pin moved 153 m to their GPS fix, now confirmed. The open "wrong location" report on it (1000085) closed with the pin thank-you.
- This run also judged the two Viroflay photos, but a parallel run had already published them (entry below); its version kept.
- No feedback, tips or reader words waiting. Checks clean (qa source, preflight 0 problems, i18ncheck).

## 2026-11-18 reader judge: two reader photographs on the Viroflay oak

- Product: Chêne de la Vierge à Viroflay (vir_001) now leads with a reader's own photograph (the Virgin statue on the trunk, autumn crown, GPS 5 m from our pin). A second shot from the other side, with roses tied to the bark, is in the strip. The reader is mailed through sightings_publish --send.
- Left for the next run: lead 3c544597 (Amsterdam, "not sure which tree", near ams_032). It was sent from one of our own accounts (`mine`) and its photograph is not on disk, so it was not judged blind.
- No open reports, no feedback, no tips waiting. Pin catch-up could not read coordinates (HTTPError). No pin needed moving: the GPS fixes are 4 to 5 m from our pin.

## 2026-11-18, night run (second attempt): shipped nothing, supply is dry

- Product: no change. No tree went live.
- Birmingham (UK) verify: no naming body, one Sutton Park ATI oak added as a lead, nothing met the bar. Released.
- Coimbra verify: the unmined register rows are all duplicates of live trees; leads still blocked on access or pins. cbr_007 in coimbra-verified.json is a duplicate of a live tree (stale file). Wall for 48h. If anyone wants more: fetch the UC tomography PDF for the botanical-garden eucalyptus pin.
- Write pass on every waiting entry and the 5 READY leads: all held for a closed reason (access x3, duplicate x1, no pin x2, street row, shrubs, no size or story). Detroit det_001 and det_002 stories are written and wait for a pin.
- For Hidde: nothing. READY is 0 and the focus cities are walls or full, so the shelf cannot refill from desk research alone.

## 2026-11-18 reader judge: nothing new (overlapped a parallel run)

- This run judged the Bengaluru rain tree and the Emmanuel plane photograph (b43d0c0b), but a parallel run had already pushed both (ben_001, entries below). My duplicate was dropped in the rebase.
- 3c544597 (Amsterdam) came from our own account and its photograph is not on this machine, so it was left alone. No open reports, no unjudged feedback, no unquoted reader notes.

## 2026-11-18 reader judge: the Makata Shrine cedar live in Narita (tip 1183)

- **narita/nrt_001, The Great Cedar of Makata Shrine: new one-tree place (Japan), live without a photograph.** This is the step the Aihole entry below left for the next window. Tip 1183 is words only, pasted from a chatbot, so none of it is quoted, plus a hand-placed pin. Japanese Wikipedia (麻賀多神社) and travel.co.jp are cited, with Chiba Prefecture's list of Narita designations for the shrine wood (designated 1977-03-08). They give the cedar as about 40 m tall and 8 to 9 m round, and 1,200 to 1,400 years old by tradition. The reader's own 1,400 from the held lead 1bc207e7 is on the page as theirs. The pin is approximate, on their spot in the shrine grounds. The recognition line names it as the thickest cedar in the wood behind the main hall. The held lead now notes that the tree is live and that a photograph of their own would lead the page.
- This run also judged the Bengaluru rain tree, the Aihole fig and the Emmanuel plane photographs, but parallel runs had already put all three on main, so their versions stand and mine were dropped at the rebase. Not judged: 3c544597 (our own account, photo not on this runner). Reports open: 0. Feedback without a verdict: 0. Reader words: 0.

## 2026-11-18 night run (16:36 UTC window): the Bengaluru rain tree, reports closed, one bug row closed

- **New: The Rain Tree of the National Gallery of Modern Art, bengaluru/ben_001** (new one-tree place, India), a reader's tree from the app (sighting 853a4b12), photograph viewed: a wide fan of dark limbs over a lawn, daylight, colour. The photograph's own coordinate lay 1.3 km north of the museum; the reader then moved the pin by hand into the grounds (report 1000083). OpenStreetMap puts the museum at 12.9895, 77.5881 and the hand pin falls inside its box, so that spot is used, approximate, with OSM as the named source. Same as Aihole and Howrah. Report closed `holds`.
- **Cambridge, Emmanuel plane (cam_011)**: the reader's extra photographs (trunk, layering limbs, autumn gold) are viewed and already in the strip live-first. Report 1000084 (a photo sent from 3.7 km away, "merged") closed `holds`: pin left alone, the photograph's coordinate is too far to trust.
- **Tree note on Djanet's Tassili cypress** read, kept.
- **Left alone**: Amsterdam row 3c544597 is ours (`mine`, no photograph on disk), not a reader's tree.
- **Health**: closed the open WEB bug row (readers' photographs had no 500 copy), already fixed in ba0575b69 with qa's `check_every_own_photo_has_a_card_copy`. Nightly knocks 6 of 12 in 24h (GitHub dropping cron, knock.yml covers it).
- **Shelf**: no write pass possible. READY is 5 leads (under the six-candidate floor) and the verified-awaiting-a-writer pile is stale or parked. The refill went to Fort Worth (verify agent, about 68k tokens): its three READY leads and the others rest on the city's heritage-tree layer alone (campus without open-grounds evidence, a streetscape block, a name with no content), so nothing verified, claim released, the city is a wall for 48h. Its forestry office is the next step and that is outreach, not search.

## 2026-11-18 reader judge: a new temple fig at Aihole

- **New: The Galaganatha Temple Fig, aihole/aih_001** (new one-tree place, India), a reader's tree from the app with four photographs: a wide, low fig on the ground of the Galaganatha temple group at Aihole with a stone Nandi beside it. The reader calls it an Indian banyan; the species is kept at "Fig (Ficus sp.)" with their name stated as theirs. The photograph's coordinate was 1.9 km off the temples. The reader then moved the pin by hand (report 1000082) onto the spot where the national monuments list places the group, so that spot is used, approximate, as at Howrah. Report closed `holds`, no mail: it is a pin on their own new tree. The congratulation mail waits for the deploy, as tree_approved.py says.
- **Tip 1183 (Kozaki)**: the Makata Shrine great cedar again, the tree of held lead 1bc207e7 (not_theirs), now sent as words alone with a hand-placed pin. The text reads as pasted from a chatbot, so nothing is quoted. Verdict `lead`: travel articles confirm a 1,300 to 1,400-year cedar in the precinct. It ships as a reader-found tip once two of them are cited by URL. That is the next step, but it did not fit this window.
- **Left open**: Report 1000083 (same reader as Aihole) moves a "Rain tree, National Gallery of Modern Art" pin in Bengaluru, but no sighting of that tree has reached us yet. It stays open until the tree arrives.
- The Dartington yew's photograph was also judged here, but a parallel run pushed it first (entry below); its version stands and mine was dropped in the rebase.
- Checks: preflight 0 problems, qa source clean, i18ncheck clean.

## 2026-11-18 reader judge: the Dartington yew has its reader's photographs

- **dartington/dtg_001, The Yew by Dartington's Old Church Tower, now has photographs.** The reader's two frames for tip 1177 arrived (sighting 2d01c8dc). I viewed both: the whole yew by the stone tower, a huge burred and folded bole in a rope ring among gravestones, daylight, colour; and the bole close up. The wide frame is the lead and the close-up is in the strip. One paragraph of the story now says the photographs came and that the burred bole on flat ground fits the Ancient Yew Group's knobbly tree 401 west of the tower, and it still asks to be told if that is the wrong yew. With a reader's photo the page can now go to Google under the reader cut.
- This run first built the tree as dtn_001 before seeing the parallel run's dtg_001. The duplicate is dropped; nothing of it was pushed. The draft asking for the photo (drafts/reply-reader-1177-2026-11-18.md) is deleted because the photo is here. **Correction to the entries below:** tip 1177's photo was late, not lost, so the "app dropping uploads" worry rests on 1175 alone.
- Amsterdam sighting 3c544597 (our own Android test account, photo not on disk) is again left alone. 0 open reports, 0 open feedback, 0 reader notes to quote.

## 2026-11-18 (session): "See all" on New from visitors in both apps

- **What changed**: Discover's "New from visitors" row now has "See all >" in the iOS and Android apps. It opens the website's /visitors page as an app screen: every photograph visitors sent that went live, newest sent first, as two columns of whole photographs (each at its own shape, not the row's 3:4 crop), the city tag on the photo and the visitor's name under it, 24 more loading as the end comes near, and "You have seen every photograph so far." at the end. A public name opens the profile; signed out the tap asks for a sign-in first and then finishes on that profile, as in the row.
- **How**: the server's `visitor_photos` keyset paging (already live). iOS Screens/VisitorPhotos.swift (the visitor line moved there so the row and the page share it), Kit/NewFromVisitors.page/author, Route.visitors, `-open=visitors:all`. Android ui/VisitorPhotos.kt (Compose staggered grid), the same paging in account/Visitors.kt, DiscoverPage.Visitors; the Android feed now reads each photograph's width and height (snapshot ATS4), so tiles take their shape before the picture loads; intro and end line in the seven languages from the website's strings. Added to ButtonWalk (both), SweepFrames, appsweep and android_parity's pairs (data/android-parity.json `visitors`).
- **Caught while building**: a page whose 24 photographs the feed did not carry yet left the spinner turning forever; a load cancelled by a sign-in counted as the end; and on a fresh install (iPhone SE, iOS 18, big text) the page stayed empty because the bundled feed did not know the newest photographs yet. All fixed on both platforms: the next page is asked at once, a stale load is dropped, and the tiles are read from the current feed as the page draws (as the row does), so they appear the moment the feed arrives.
- **Checked**: iPhone 17 Pro and iPhone SE (iOS 18.6, extra large text), signed out (a name asks for sign-in) and signed in with the test account (a name opens the profile; nothing written); Android emulator, fresh install, font 1.3; endless loading to the end line on iOS; the same first photographs in the same order on web, iPhone and Android. Not checked: airplane mode (no answer stops the page after its intro, as the website does).
- **For Hidde**: in the next TestFlight build and the Android build after 0.1.0 (2). Nothing archived, uploaded or submitted.
## 2026-11-18 reader judge: tip 1177 re-judged, a Dartington churchyard yew is live

- **Live: Dartington (Devon), The Yew by Dartington's Old Church Tower (dtg_001)**, a new one-tree place. Tip 1177's app sighting (2d01c8dc) did reach the server after the run below looked (row updated 15:46 UTC). It carries a GPS fix "standing at the tree", species Taxus baccata, "Ancient" and a girth of 800 cm, but still no photograph. The fix is about 10 m from the listed tower of Dartington's demolished church (SX 79780 62693), where the Ancient Yew Group records three yews; the biggest, west of the tower, has been measured since 1787 (655 cm in 2012). The pin is confirmed from the reader's fix, with no photo, so the page stays out of Google until a reader adds to it. The story gives the group's figures as the group's and the 800 cm as the reader's, and asks which trunk they stood at. The lead in data/leads/dartmoor.json is marked published. The draft reply now says the tree is on the map and asks for the photo; bin it if the tree_approved congratulation goes first.
- **Correction to the For Hidde line below:** for 1177 the sighting row did arrive, just without its photo (`photo` null). So the app is losing the photo upload, not the sighting. The collect-flow look is still worth doing.
- This run had also written the Trollskogen beech before it saw the parallel run's `thl_001`. That version was dropped; theirs stands.

## 2026-11-18 reader judge: the Trollskogen twisted beech is live; Dartington tip recorded as a lead

- **Live: Torna Hällestad (Lund, Sweden), The Twisted Beech of the Trollskogen (thl_001)**, re-opened on Hidde's word (not a bad frame): the reader's photo looks up into a contorted beech in summer leaf, GPS fix in the Gryteskog reserve. Pin confirmed, sources are Länsstyrelsen Skåne's reserve pages, a new one-tree place. The reader's three extra photos show other trees and are not used. Congratulation mail goes out with the knock once the tree is in the live feed.

- **Leidsebosje Planes (ams_002)**: a parallel run judged the same reader photograph minutes earlier, the same way (`add`, now the lead); its version is kept. Both runs ran sightings_publish with --send, so the reader may have had the "on the page" mail twice.
- **Tip 1177** (Dartmoor in the app, GPS fix by Dartington about 2 km north of Totnes, no words): its app sighting is not on the server, so no photo arrived. Verdict `lead`, in data/leads/dartmoor.json; suggested reply asking for the photo in drafts/reply-reader-1177-2026-11-18.md (For Hidde: send or bin).
- **For Hidde: two collect-flow tips from two different readers today (1175, 1177, half an hour apart) arrived with a sighting id the server never got.** That looks like the app dropping the photo upload rather than the readers deleting anything; worth a look at the collect flow before more go missing.
- Sighting 3c544597 (Amsterdam, "The Last Elm of Stationsplein") is our own Android test account (`mine`), left alone. 0 open reports, 0 open feedback, 0 reader notes to quote.
## 2026-11-18 reader judge: Mont Mourex tip recorded as a lead, nothing went live

- **Tip 1175** ("The biggest and oldest tree on Mont Mourex", GPS fix at the tree above Grilly, Ain, about 25 km from Geneva): the app sighting it came with no longer exists, so no photograph reached us, and no source or species. Verdict `lead`, recorded in data/leads/geneva.json. None of hold_reply.py's standard mails fits a tip without a photo, so a suggested reply asking them to send it again waits in drafts/reply-reader-1175-2026-11-18.md (For Hidde: send or bin).
- **Sighting 3c544597** (Amsterdam, near ams_032, our own account `mine`): photograph not on disk, left unjudged for the next run, never judged blind.
- 0 open reports, 0 open feedback, 0 reader notes to quote. The other waiting `mine` leads are our own test photographs, not readers'.
- **Added by a parallel run: a reader's photograph now leads amsterdam/ams_002, The Leidsebosje Planes** (sighting 4ffdc2fe, which the run above did not take). I looked at it before deciding. It shows both planes on their lawn by Leidseplein, in autumn leaf and daylight, and the two massive trunks match the entry. It went in as `add`, so the reader's photograph now leads the page and the old lead moves into the strip. The pin stays where it was: the photo's coordinate was our own pin, not a GPS fix. The "on the page" mail went with `--send`. The tip 1175 lead and verdict above were kept, and my duplicate of them was dropped in the rebase. qa --source-only clean, preflight 0 problems, i18ncheck clean.
## 2026-11-18 (session): Android closed test submitted to Google

- **Android 0.1.0 (2) sent for review in Play Console, closed test "Alpha"** (Hidde's yes in chat; his two tester lists, 177 countries). Google's review usually takes hours to days; the 14-day clock for a personal account starts when it is live. Updates during the test do not restart it.
- Fixed on the way: advertising-ID declaration set to No (the build asks no AD_ID); `android.hardware.screen.portrait` marked optional (Play hid the app from tablets and Chromebooks because of portrait lock); versionCode 2.
- Found on Hidde's phone: the Play build came up signed out when opened without internet; `Account.restore()` now keeps the token and asks again until there is a signal (in this build).
- **The R8 run is green** (later the same day, from ~/Developer): all 27 instrumented tests pass against the Play build's own R8 (`-PtestMinified`, ButtonWalk left out, it runs daily on CI). Native debug symbols for Play cannot be added: MapLibre ships its .so files already stripped, so the upload warning stays and blocks nothing.
- `scripts/android_prelaunch.py` + RELEASE_CHECKLIST "The whole chain in one go": the whole machine chain on the Play build. The R8 instrumented run is not yet green on a local emulator (the Mac ran out of memory and swap; ButtonWalk alone took over 20 minutes); rerun it from ~/Developer before the next update. Play warns that native debug symbols are missing (MapLibre): add them in the next upload.
## 2026-11-18 reader judge: the Worthing giant sequoia is live; the 16 mail replies arrived twice

- **New tree from a reader**: **The Giant Sequoia of Lyons Farm** (worthing/wor_001, a new one-tree place in the UK). This is tip 709. It was held on 11-15 because it had no location. The reader has since answered our mail: yes, it is the sequoia in Lyons Farm Open Space, Broadwater. Its photograph was on this machine this time. I looked at it: the shot looks straight up a huge, flaring, mossy red-brown trunk under a crown of curling limbs, and a trunk shot goes live. The pin is approximate, at the centre of the park (OpenStreetMap way 287672394), and the page says the pin marks the park, not the tree. The reader called it a redwood and their note says it was planted in the gardens of a former house. Those words are quoted on the page as theirs. Who planted it, and when, is asked on the page; the reader says they are looking it up. Built by out/tmp/build_reader_tree_2026_11_18d.py, not committed. The congratulation mail (tree_approved.py) goes after the deploy.
- **The same 16 mail replies were filed twice**: rows 1157 to 1172 are the same mails as 1141 to 1156, filed at 14:21. data/mail-replies-seen.json already held all 16 hashes from 14:06, so the most likely cause is a second reader-judge run that checked out before that commit landed. All 16 duplicates are closed `handled` as "same mail as N". 1156 (Jairam's "Of course :)") is still the one open for Hidde. **Bug for a session**: reader_mail_replies.py should check Supabase before it posts, skipping a row when a `mail-reply:` row with the same words already exists, so a race between runs cannot file a mail twice.
- No photos waiting on our trees, no open reports, no unjudged tips. The old Japan and Baarn leads are owner-account photos, never auto-published. reader_words: nothing new. preflight 0 problems, qa --source-only clean, i18ncheck clean.

## 2026-11-18 session: a See all page for New from visitors; a photo test that measures what a screen shows

- **What changed in the product:** the home row New from visitors has "See all >" on its heading, opening /visitors (and its seven language twins): every visitor's photograph in a masonry of whole photographs, newest first, 24 more as you scroll, the row's own card (Unsplash and Pinterest; CONVENTIONS.md 2026-11-18). Noindex while recovery mode holds, so it adds nothing to Google's crawl. The card data moved into lib/visitor-cards.ts so the row and the page read one source; the home row itself is unchanged.
- **Pasted by Hidde (twice, the second with the sent-time order):** both the page and the home row (web and app) sort by when a photograph was SENT, its upload time in storage, not when it was taken ("sort by when it was sent, not when taken"). Checked live: 369 photographs in 8 pages, none repeated, newest sent first; the home row starts with the same five. Upload times checked against October photographs (uploaded minutes after they were taken), so the 169 on 11-15 and 87 on 11-16 are real sends, many of them old library photos.
- **Photo test:** scripts/photocheck.py opens home, /visitors, London, the UK page, /cities and the three newest readers' tree pages in Chrome as a 3x phone and a 2x laptop, and fails on a photograph stretched over 2 screen pixels per file pixel (soft), shrunk more than 3.5 times (heavy, the readers' originals), or broken; weight alone is a note. Daily in photos-live.yml into quality.py's Web Live light. First live run (before this deploy): 115 heavy, all readers' originals; 0 soft, 0 broken. qa `check_every_copy_is_its_photograph()` refuses a card copy that is a different picture from its photograph (Palermo scored 46, a true copy 0.1).
- **Not verified:** no local build (no Node); the page script was run on the live site against the real server in the browser pane at 546 and 1280 px; the deploy's build and pagecheck are the first full test.

## 2026-11-18 session: readers' photographs get their small copy (New from visitors, the strip)

- **What changed in the product:** the New from visitors tiles, every card and a tree's photo strip now load a 500 pixel copy of a reader's photograph instead of the 1600 pixel original the browser shrank seven times (Hidde: "something feels off with the quality of the photos ... weve made this mistake before"). 388 readers' photographs had no small copy, because vendor_photos.py only ever sized a tree's lead and named it after the tree; `own_copies()` now sizes every photograph on our own domain, lead and strip, from the original on disk, nightly and in the deploy before the build. Palermo's ficus card showed an old Commons frame under the reader photo's name; the reader photo is renamed (-997e5830) and has its own copy now.
- **Guard:** qa `check_every_own_photo_has_a_card_copy()` fails the deploy when a photograph on our domain wider than 575 px has no 500 copy; escaped bug ESC-2026-11-18 recorded with that test.
- **Size:** the 500s add 44 MB. A 1000 copy as well (sharper on a 3x phone) was measured at 148 MB more and left out: the repo-size call of 2026-09-03 is Hidde's.
- **Next, waiting for his word on the design:** a See all page for New from visitors, a masonry grid of whole photographs with endless scroll (Unsplash and Pinterest; CONVENTIONS.md 2026-10-04 See all and 2026-10-10 endless similar items). It needs one SQL paste (a paging version of new_from_visitors).

## 2026-11-18 reader judge: the Makata shrine cedar held (not their photo), 16 mail replies filed

- **Held, `not_theirs`**: the Ancient Cedar at Makata Jinja (sighting 1bc207e7), from the reader behind the Tokyo, Dujiangyan and Big Bear trees. The main photo is a screenshot of another person's post in a photo app: their name, "a year ago" and like and share buttons sit over the picture, and the reader's profile has a different name. The roped-trunk close-up gives no sign of being theirs either. The standard not_theirs mail is queued (submission 1140). A photo of their own puts it live at their pin, with their 1,400 years and 800 cm given as theirs.
- **Worthing sequoia re-opened** (tip-709): the reader answered our mail "yes it is" the one in Lyons Farm Open Space. The lead is `lead` again with the park in `why`, but its photograph was not on this machine, so it is left for the next run to judge with the park as its named site. Overpass was down (502), so no pin was looked up.
- **Mail replies (feedback 1141 to 1156)**: 15 closed `handled`. Earlier sessions had already acted on each one: the Edinburgh and Adelaide ambassadors were already granted; the Hanoi banyan, Cathedral Grove, Tassili, Emmanuel plane and Willistown sycamore are live; the totara figures were checked; the rest were thanks. 1156 (Jairam's "Of course :)") is `needs_hidde`: it is probably the yes to quoting "well worth a visit" on cam_011, but only if the draft asking for it was sent.
- **Bug for a session**: reader_words.py lists these mail-reply feedback rows as notes on whichever tree the sender's newest row named, so Jairam's Emmanuel plane mail showed under the Howrah banyan and Erin's totara mail under the Curtain Fig. All nine rows are closed with `--done`. Mail replies should not enter that list (their words need a quote_ok anyway).
- No open reports, no tips without a photograph. preflight 0 problems, qa --source-only clean, i18ncheck clean.

## 2026-11-18 session: app health read from PostHog, build number in every event, the repo left iCloud

- **App health (PostHog, App Store phones, 15 to 18 Nov)**: 2.3% of cold launches come within two minutes of the app being on screen (it died: crash, memory kill or a swipe), the same on iOS 18, 26 and 27; about half right after a tree page (median ~45 s), which fits the big-photo memory reading of 11-16. MetricKit: two store crashes on build 41 in 30 days, one phone each. `sync_failed` 6 times on 4 phones.
- **Product (next iOS build, and Android before its release)**: every app event now carries `build_number` (iOS CFBundleVersion, Android versionCode), so that relaunch rate and the crash reports can be compared build by build. iOS builds; Android MeasureTest green. Query: `count where event='app_open' and gap<120s, group by properties.build_number`.
- **The repo moved to ~/Developer/Ancienttrees** (Hidde: "Verhuis de repo"). ~/Documents is iCloud-synced with Optimise Mac Storage on a 97%-full disk, so macOS evicted git's own files and `git worktree add` failed. Fresh clone from GitHub; local-only files copied across (out/ without out/tmp, private drafts, settings.local.json), git config (hooksPath, author, inflight merge driver), Claude memory, the daily publish task's path, CLAUDE.md. Android needs `android/local.properties` (sdk.dir=/Users/hidde/Library/Android/sdk) per checkout.
- **For Hidde**: open Xcode from ~/Developer/Ancienttrees/ios/AncientTrees/AncientTrees.xcodeproj from now on and start Claude sessions in ~/Developer/Ancienttrees. The old ~/Documents/Ancienttrees stays until you say it may go (it still holds old unpushed session branches, nothing current). The disk at 97% is yours to free.

## 2026-11-18 reader judge: the Ginkgo of Kuhonbutsu live in Tokyo; a reader's photo leads the Barcelona casuarina

- **New tree from a reader**: **The Ginkgo of Kuhonbutsu** (tokyo/tok_023), in autumn gold at Joshin-ji, Setagaya. The reader's GPS fix is in the temple grounds. Their photographs show the stone post (都天然記念物 九品仏のイチョウ) and the Setagaya 名木百選 plaque (selected 1987, reselected 2020), and the Tokyo register lists the designation (1963). Two more of their photos are in its strip. A Japanese overlay entry was written for it, and the counts in the Tokyo texts now follow the trees: 23 trees and 10 ginkgos. The English intro said "seven ginkgos" and the Japanese one said "16 trees, 6 ginkgos"; both were already stale. Built by out/tmp/build_reader_tree_2026_11_18c.py, not committed. The Kaya at the same temple stays a lead in data/leads/tokyo.json.
- **Photos on our trees**: the Casuarina of the Cascada (bcn_011) now has a reader's photo of the whole tree as its lead, and the old one moved to the strip. The same frame was sent three times, so two copies were rejected as duplicates. Fertőújlak fbcb3c91 was rejected because the same photo by the same reader already leads fuj_001.
- No open reports, no tips without a photograph, no feedback waiting. reader_words: nothing new.
- preflight 0 problems, qa --source-only clean, i18ncheck ja/tokyo clean.

## 2026-11-18 reader judge: five more readers' trees live, a reader's photo leads the Ueno camphor

- **New trees from readers** (every photograph viewed; written by out/tmp/build_reader_trees_2026_11_18.py, not committed):
  - **The Kapok of the Kisantu Botanic Garden** (kisantu/kis_001, DR Congo, new one-tree place): GPS at the tree, the garden's own Ceiba pentandra label in frame. The photograph is **cropped above the people seated in front**, so no one in it is recognisable.
  - **Four Hidde had looked at today**: Lincoln NE (lincoln-nebraska/lne_001, new place in us-states.json; species left open and asked, since the leaves are pinnate and not an elm's), Fertőújlak (fertoujlak/fuj_001, new place; a pagoda tree or locust, left open), Chiang Mai (cnx_003, a bodhi tree whose 100 years are the reader's) and Bristol bri_023.
  - **About Bristol**: the photograph was sent for bri_015, the Monterey cypress, but its red stringy bark and feathery sprays are not a cypress (the earlier hold said the same). So it is a tree of its own at Bishops Knoll, and its page asks whether it is the cypress after all. Bristol's intro and meta now say twenty-three.
- **Ueno Toshogu Camphor (tok_003)**: the reader's second shot, the crown over the Toshogu wall and lanterns, went in as `add` and leads now. Their first shot (the trunk half behind shrubs) was not used.
- **Ran in parallel with the run below**: both judged the Great Banyan. Its how_001 stands; my hwh_001 was dropped in the rebase before it was pushed.
- **Still to happen**: the congratulation mails (tree_approved.py) wait for the deploy, since the trees are not in the live feed yet. No open reports, no open feedback, no readers' words to quote.

## 2026-11-18 reader judge: the Great Banyan of Howrah is live

- **New: The Great Banyan, howrah/how_001** (new one-tree place, India), a reader's tree from the app with four photographs: the grove of prop roots and the Botanical Survey of India board, which supplies the facts (over 270 years, trunk removed 1925, 4,208 prop roots, 18,918 sq m). The reader's age, 275, is on the page as theirs. Lead photo plus two in the strip. The photograph's coordinate was 2.6 km off, outside the garden; the reader then moved the pin into the garden by hand (report 1000079), 70 m from Wikidata's point, so that spot is used, approximate.
- **Cambridge cam_011**: the same reader moved their Emmanuel College plane's pin once more, 23 m (report 1000078); taken as their own tree's move.
- Both reports closed `holds` with no mail (moves on their own trees). Tip 1093 was the app's row for mkn_003, already live: verdict publish, nothing to add. No feedback waiting, no reader words to quote.
- Left alone: the old owner-account leads (Japan, Baarn), which are ours and never auto-published.

## 2026-11-18 session: dd, three feedback replies sent, the iOS sweep retries

- **Replies sent on Hidde's "verstuur"** to three messages from the Settings feedback form: 1128 (how to add a tree), 1092 (following, editing, seasons; his own lines: overwhelmed, Android first, which features they'd add, seasons from the photo date and he can add a control) and 1075 (the Darley Dale yew at St Helen's, asked for a photo; still a lead in _famous-united-kingdom.json). Then 786 (UK heritage-tree initiatives), in his words: wants to talk further about giving them a place, "This platform needs to have a positive impact on trees", proposed a page on visiting trees responsibly and asked whether they would help. All four closed in the feedback ledger; "Open for you" is empty. A page on visiting trees responsibly is an idea only, not built and not decided.
- **Rules from his corrections**: adding a tree in the app is the camera button in the bottom bar, never "Add a tree on Discover" (mailcheck ADD A TREE VIA DISCOVER); a reply on how to add a tree gives both routes, app and the web form (HIS_VOICE.md 2026-11-18). "Feedback" means the Settings form (source `app-profile`); the Plus answers are "Plus feedback".
- **iOS red on main**: the nightly's `look` job failed on "the test left no measurements behind" with no cause printed, while the same job rendered all 39 screens; first time seen. appfit.py now prints xcodebuild's own failure lines and sweeps once more before failing (b3521eb96). Tonight's nightly is the test.
- **Privacy**: drafts/reply-bill-tassili and reply-erin-totara (another session, 11-18) carried readers' mail addresses into the public repo; the pre-push qa caught it on the next push. Replaced by their hash. The addresses remain in GitHub history (6d98ddccc); removing them needs a force-push, which is Hidde's.
- Digest: the scheduled data-digest had not run for 11-17 by the morning; dispatched by hand.

## 2026-11-18 session: the Emmanuel College plane live (Cambridge, two readers)

- **Live**: cambridge/cam_011, the Great Oriental Plane of Emmanuel College. Held 11-15 and 11-17 as `not_public` (the college calls the Fellows' Garden private); the app reader who moved its pin wrote today that he first saw it over the wall from the street, was let in at the main gate and walked up to it, "not private, at least during certain hours". Under the closed list that clears it.
- Lead photo from the website tip (tip-748, spring, the weeping limbs and chairs); the app reader's autumn photo in the strip. Facts from the college's own booklet (girth 478 cm in 2006, planting dated 1816 to 1836 by girth, 1802 "unprovable", limbs rooting where they touch the ground, Pakenham's book). Pin approximate, from the reader's map mark; his photo's own location tag pointed 3 km off. Verdicts written (`lead:` and `sight:` for both).
- **Mail**: reply sent to Jairam in his thread on Hidde's "ok stuur" (drafts/batches/reply-jairam-emmanuel-2026-11-18.json), after the page answered 200 with both photos: it's live, plus one ask, may we quote his "well worth a visit" line. On his yes the line goes in data/outreach-words.json with `quote_ok`.
- Not done: the tip-748 reader got "if it opens, it goes on the map" on 11-15 and has not heard it is live; the congratulation mail (`tree_approved.py --send`) goes to the app reader only.

## 2026-11-18 session: a sign-up to an address that can't receive mail is refused

- **Product, LIVE in the hook since about 10:30 UTC** (send-email v9): a sign-in or sign-up link to an address whose domain has no mail server and is a typo of a provider on data/email-domains.json (hoymail.com for hotmail.com), or whose domain does not exist at all, is refused instead of sent. Hidde, after a welcome mail to "hoymail.com" sat retrying for a day: the "Did you mean" warning "doesnt stop people from making the mistake". Benchmarked (CONVENTIONS.md "A mistyped email address", layer 3): the hard stop at sign-up is a mail-server lookup; nobody mails a guessed address after a bounce. A lookup that errs or is slow lets the mail through. qa's `check_one_email_domain_list()` now also holds the hook's copy of the list.
- **Website** (with this deploy): the sign-in sheet and /account say "That address can't receive mail." in all eight languages, and the field stays blocked until the address changes or the "Did you mean" address is tapped. **Apps**: blocked already through the server; they show their could-not-send line with the suggestion under it. For the next iOS and Android build: show `noMail` (site/src/lib/signin-strings.ts) when /auth/v1/otp answers 422 with `msg` starting "undeliverable:".
- Tested against the live hook: hoymail refused with the corrected address, a non-existent domain refused, our own address and a real domain sent; a real /auth/v1/otp call for a hoymail address comes back 422 "undeliverable:…@hotmail.com" and leaves no account behind. Not checked: the web message rendered in a browser (checked after the deploy).
- Slip: one test call sent a "Reset your password" mail with a dead link to test@mail.com; it bounced, so it reached nobody.
- The reader of 11-16 (hoymail, unconfirmed) signed up at 06:45 UTC, seven hours before the warning existed. Sent on Hidde's yes: one plain mail to the hotmail address through Resend (batch `signup-typo-2026-11-18`), "sign in again with this address", no sign-in link in it.
- Bounces since 11-01, read from the mailbox (bounce notices only): 15 addresses, two of them typo domains. The other, outlook.co for outlook.com (11-15), signed up again correctly a minute later and is active; her unconfirmed outlook.co account is left as it is. The rest were the Yahoo, Apple relay and BT route refusals already handled on 11-16 and 11-17, plus one magazine address.

## 2026-11-18 session: a reader's Saharan cypress live (Djanet, Algeria)

- **Product**: the Tassili cypress (reader tip 947) is live as djanet/djn_001, a Saharan cypress (Cupressus dupreziana) on the Tassili n'Ajjer. It was held on 11-17 for no_location; the reader mailed a Google Earth screenshot marking it north of Djanet (saved with `outreach_inbox.py --save-from`, out/mail-photos/colegravebill/). The pin is read off a tilted 3D view, so it is `approximate` and the access line says plainly that it is the reader's map mark and that the Djanet guides know the cypress sites. The story quotes the reader unnamed; species facts are from Wikipedia (212 left in March 2026). The congratulation mail goes through tree_approved.py as usual.
- **Checked, nothing to change**: a reader's mail about the Big Totara sign. It is tuatapere/tua_001 (Lillburn Monowai Road), not akaroa/akr_001 as first noted here. Her sign photograph arrived through the app (sighting 0b414558) and the page already rests on it (8.31 m, about 1,000 years). Replies to both readers drafted for Hidde: drafts/reply-bill-tassili-2026-11-18.md, drafts/reply-erin-totara-2026-11-18.md. Hidde said "Verstuur beide": Erin's went at once, Bill's once https://ancienttrees.app/djanet/tassili-cypress answered 200 (both sent, in their own threads). One deploy failed QA because those two drafts carried mail addresses, mine, since replaced by hashes; the addresses remain in git history.
- **Checked, nothing to change**: a reader's mail about the Big Totara sign. It is tuatapere/tua_001 (Lillburn Monowai Road), not akaroa/akr_001 as first noted here. Her sign photograph arrived through the app (sighting 0b414558) and the page already rests on it (8.31 m, about 1,000 years). Replies to both readers drafted for Hidde: drafts/reply-bill-tassili-2026-11-18.md, drafts/reply-erin-totara-2026-11-18.md.

## 2026-11-18 session: reply to Joey (Willistown) sent

- **Mail**: Joey R. (Willistown ambassador) got a reply in his "Pawling Farm American Sycamore" thread, sent on Hidde's "Verstuur" (drafts/batches/reply-joey-willistown-2026-11-18.json). It covers his sycamore (his own photos lead, his 6.95 m is on the page) and his front-yard oak question (talk to the owner first, then it can go on the map with the pin on the sidewalk). The oak paragraph is Hidde's own; the lesson is in drafts/HIS_VOICE.md (2026-11-18). This replaces the unsent drafts/reply-reader-1000077-2026-11-17.md.

## 2026-11-17 session: Android before the Play closed test (PR 64), found on Hidde's Samsung and by three walks

- **Product changes, all on claude/android-tabbar-proposal (PR 64), on Hidde's phone**: English only, as the iPhone (`localeFilters`, translations kept in res/values-xx; Hidde: "eens"); portrait only; camera photos also saved to Pictures/Ancient Trees (CameraRoll, as iOS keeps one in Photos); the keyboard no longer pushes the screen up (`adjustResize`); a Discover search no longer leaves the map without its menu; back from a page over the map leaves the page; back from a place link returns to the page it came from; a theme switch no longer restarts the app; Distances in miles reach every label; your own photos of our trees show as a row and as the hero, with delete in the viewer; tappable names on notes and "Photo: name"; refresh on return to the app; photo picker is Android's own again (Samsung Gallery via ACTION_PICK failed); My trees map draws your own trees in your photo; the gear and Find people share one size; the tab bar is one white ground with Polarsteps' soft top line.
- **A bug on both apps since launch**: every request said `Content-Type: application/json` even with no body, and Supabase storage refuses such a DELETE, so removing a photo, a tree's photo or an avatar (account deletion) left the file behind. Fixed in Android Supa.kt and iOS Account.swift (iOS from the next build). On Hidde's word ("Openbare kopieën weg") the 31 public copies (shared-sightings + thumbs) whose sightings row was gone and that nothing in data/ or site/ names were removed; 26 that the repo names and all 157 private files stay.
- **Ratchet**: FlowWalk `theKeyboardLeavesTheFieldInView` (also asserts portrait) and `aPlaceFromDiscoverSearchKeepsTheMenu`, both shown red with the fault put back; two escaped-bug rows closed with them. RELEASE_CHECKLIST.md "Every build" now has the three passes a session runs before Hidde tests a build (test-account walk incl. sending and cleanup; small old phone, big text, no network; screen pairs + app-level settings).
- **Test account**: a walk sent a real collect, a new tree and a note, then removed them; what the app could not remove (one sighting, submission 1110, four files) was removed by id, and the profile set back to private.
- **Rounds 2 and 3 (small phone at 130% text, no network; every screen beside the iPhone, 39 pairs)**: a full-height sheet now scrolls (Add note was under the keyboard); one map snapshot at a time and the map stopped before it is destroyed (two freezes on a GPU-less emulator, unconfirmed on a real phone); Take me there drops the distance rather than cutting it; Find people's reason on one line; number and unit never split; location asked once per install (it asked again every cold start after a refusal); the site's Open in app link (open.ancienttrees.app) opens the Android app; Kilometers spelled as on the iPhone.
- **For Hidde, not decided by a run**: signed-out My trees at 130% text on a small phone puts Sign in under the tab bar at the half stop (as the iPhone's half stop); the place-pin header is neither the iPhone's nor Android's form; the gallery copy of a camera photo carries the camera's own GPS only (iOS writes the phone's).
- **Open, not done**: offline town search says "check the spelling" on both apps; notes say "No notes yet" offline; Discover's visitor shelf does not reload when the network returns; debug builds read the catalogue in 17 to 50 s on a loaded emulator (release on the S21 is quick, not measured on a cheap phone); CI walk on PR 64 to be read again.

## 2026-11-18 reader judge: the Inner Temple Mulberry has its first photograph; the Cusop yew gets a reader's age

- **Live: the first photograph of lon_020, the Inner Temple Mulberry in London** (sighting 145ff4d3, `approve`). I looked at it: a low, leaning black mulberry with a gnarled, burred trunk in two stems, held up by stakes, in a fern bed on the garden lawn. It has yellowing heart-shaped leaves and the brick chambers behind. It was taken in daylight and colour, with a small lens smudge in one corner clear of the tree. The pin moved 107 m from our approximate spot to the reader's GPS fix inside the garden, and it is now confirmed. The pin catch-up step hit HTTPError again.
- **Cusop yew (cus_001)**: the reader who added it left a note: "Locally supposed to be between 1,500 and 2,000 years old." It is now on the page as a reader's estimate, labelled as local belief and not a ring count. It is in the story (quoted), the age field, the FAQ, the intro and the question context. The note was not on the closed list, so it stays up.
- Nothing else was waiting: no open reports, tips or feedback without a verdict, and no reader words to quote. The 37 own-account (`mine`) leads were left alone, as in earlier runs.

## 2026-11-18 reader judge (fourth, in parallel): nothing new

- This run judged the same Melbourne sighting (2f335c62) as the run below and reached the same verdict, a duplicate of mel_001's lead. That run's entry was kept. Nothing else was waiting: no open reports, tips, feedback or notes. The 37 own-account leads were left alone.

## 2026-11-18 reader judge (in parallel): a second reader frame of the Stow north door yews

- This run judged the same Stow sighting as the run below, which pushed first and rejected it. My verdict replaces that one because it adds something: the extra frame is now in the strip.
- **Live: the reader's close frame of stw_001, the north door yews of St Edward's, Stow-on-the-Wold** (sighting 0dc02495, `strip`). I looked at it: both trunks either side of the arched door, red flaking bark, the root plates over the path, wet daylight. The sighting's main frame was a near-copy of the lead the same reader gave on 10-26 (ea481510). So I pointed the queue entry at the extra file and stripped that instead, which works around "the publisher only handles a sighting's main file".
- **Rejected as a duplicate: 2f335c62**, sent for mel_004 (Darling Gardens holm oak). It is the same picture that already leads mel_001, the Edinburgh Gardens holm oak, and its GPS is 38 m from that tree. mel_004 still has no photograph.

## 2026-11-18 reader judge: a second Stow yew photograph rejected as a duplicate; three tree notes read

- **stw_001, the north door yews of St Edward's, Stow (sighting 0dc02495)**: this is the right tree. It comes from the same reader and the same visit (26 October) as the lead photograph already on the page (ea481510), taken from the same viewpoint a step to the side. I rejected it as a duplicate. Its extra file is a close-up of the roots and the door between the two trunks. It could go in the strip, but the publisher only handles a sighting's main file (the same gap the Edinburgh Gardens run found).
- **Tree notes (3, all kept and marked read)**:
  - Setúbal stb_010: a reader asks whether the tree is a Peruvian or a Brazilian pepper. That is a species question for a session to check against the photograph and sources.
  - Melbourne mel_002 and mel_013: two kind notes from one reader.
  - No note matched the closed list for hiding.
- Nothing else was waiting: no open reports, no tips without a verdict, no feedback without a verdict, no reader words to quote. The 37 `mine` leads in _sightings.json were left alone, as in earlier runs. The pin catch-up in sightings_publish could not read coordinates (HTTPError), so the next knock retries it.

## 2026-11-18 reader judge (third, in parallel): the last two Edinburgh Gardens sightings rejected as duplicates

- This run judged the same queue as the run below and came to the same three verdicts (mel_001, tok_005, 47b1b1f2). That run pushed first, so its versions stand. I added only the two sightings it left without a verdict.
- Rejected as duplicates, after comparing image hashes with what is already live:
  - 69ef60d5 (sent for mel_002) and c650049c (sent for mel_013) both have the backlit gum as their main photograph, the frame held `wrong_tree` this morning as 86a63f45.
  - 69ef60d5's extra is mel_019's lead photograph.
  - c650049c's extra is a new frame of mel_019 by the skate bowl, with a bicycle in it. It could join mel_019's strip, but the publisher only handles a sighting's main file.
- The 37 `status: "lead"` rows in data/leads/_sightings.json are all our own photographs (`mine`), not readers' trees, and their files are not on this machine.

## 2026-11-18 reader judge (second, in parallel): Melbourne's finer holm oak gets its first photograph, a reader's photo leads the Shiba Toshogu ginkgo

- **Live: mel_001, the Finer Holm Oak of Edinburgh Gardens, has its first photograph** (sighting 976d3d1b). It shows a thick dark trunk among lighter park trees, beside a club building, 43 m from our confirmed pin. A second register holm oak stands 50 m from the fix. I went with ours because it matches the recognition line ("near the bowling club") and the reader picked it. Its story is now indexed, so I rewrote its two colon reveals as plain sentences. The preflight check for colon reveals had refused them.
- **Live: a reader's photograph now leads tok_005, the Shiba Toshogu Ginkgo** (sighting 12844fcf, `add`). The stone post in frame reads 天然紀念物 芝東照宮公孫樹 (Natural Monument, Shiba Toshogu ginkgo). The Commons photograph moved to the strip.
- **Rejected as a duplicate: 47b1b1f2.** It was sent for the Bidwill Kauri Pine (syd_001). Every frame is the Wishing Tree (syd_006): the GPS is 0 m from its pin and the photo shows its Norfolk Island pine label. The same reader's identical crown and trunk shots already lead and fill its strip.
- **Overlap.** This run started on the same queue as the entry below and judged the Edinburgh Gardens red gums more cautiously (held). The other run pushed first, so its Melbourne red gum verdicts (mel_002 photograph, the new mel_019), its India hold and its 1128 draft stand. I kept only the three verdicts above, which it had not touched.

## 2026-11-18 reader judge: Edinburgh Gardens gets its red gum photograph and a new gum

- **Live: the first photograph of mel_002, the Remnant River Red Gum of Edinburgh Gardens, Melbourne** (sighting 83d2e9a2). It shows the whole leaning gum, with smooth, pale, mottled bark down to the ground, in daylight. Its GPS fix is 17 m from our pin, which sits on Yarra register ref 104. One reader sent seven photographs from the park in one walk, all tagged mel_002 or mel_013, and they show three different trees.
- **Live: a new reader's tree, mel_019, the Gum by the Edinburgh Gardens Skate Bowl** (sighting cf563d69, verdict `other_tree`, then published). It is a big straight gum: rough grey bark low on the trunk, smooth pale bark above, and the painted skate bowl beside it. The pin comes from the reader's GPS fix. The species is left at the genus (Eucalyptus sp.) because the fix sits among several Yarra register gums (ref 111 is 36 m off), so I have not tied it to one row. The Melbourne intro, question_meta, question_context and the walk FAQ now count 19 trees, eight of them on the north walk. The congratulation mail waits for the deploy (no credentials in this run).
- Held as `wrong_tree`: sighting 86a63f45, a tall gum by the park shelter shot against the sun. It may be mel_002 or mel_019 from another side.
- Rejected as duplicates: 40cb274a and d079d8a5, both sent for the Southern Mahogany (mel_013). They are the same frame as 83d2e9a2 and show the smooth red gum, not the rough-barked mahogany. Also rejected: 8aa6d2ec, the same frame as 86a63f45, and e1b0ab73, the same skate-bowl tree as cf563d69. e1b0ab73 can join mel_019's strip.
- Held as `bad_frame`: 991c4102, a reader's "tree I found" near Tiruvannamalai, India. The photograph is only a close-up of white tubular flowers and leaves, with no trunk or tree in frame.
- Feedback 1128 ("Is there a possibility to add trees to the map?") is closed `needs_hidde`. A suggested answer pointing to the app's "Add a tree" button is in drafts/reply-reader-1128-2026-11-18.md. There were no open reports and no reader notes to quote. The pin catch-up step hit HTTPError again.

## 2026-11-18 reader judge: a third photograph of the Pawling Farm sycamore

- **Live: the finder's new photograph of vfg_001, the Pawling Farm sycamore in Valley Forge** (sighting 79399d95). I looked at it: the huge burred trunk base and the mottled white limbs above it, in daylight, with a person seen from behind for scale. Species and description both match. It went in as `strip`, so it sits in the gallery behind the wide lead photograph and does not replace it. The pin was already confirmed, so it stays where it is; the pin catch-up step hit HTTPError again.
- Nothing else was waiting. There were no open reports, no tips without a verdict, no feedback without a verdict and no reader notes to quote. The 37 `lead` rows from our own account (`mine`) were left alone, as in earlier runs.

## 2026-11-18 reader judge: the Camperdown Cemetery Fig has its first photograph

- A reader's photograph of syd_005, the Camperdown Cemetery Fig in Sydney (viewed: the buttress-rooted Moreton Bay fig among the headstones, daylight, colour), is now its lead photograph. The tree had none before. The pin stays as it was: the photo's coordinate was our own pin, not a GPS fix.
- A second photograph for vfg_001, the Pawling Farm sycamore in Valley Forge, was rejected: it shows only the National Park Service entrance sign for Pawling Farm, with no tree in it. The tree keeps the reader's earlier photographs.
- Nothing else was waiting: no reports, no tips, no feedback without a verdict, no reader notes to quote. The 37 open leads all come from our own account (`mine`). The pin catch-up step could not read coordinates (HTTPError), so the next knock retries it.

## 2026-11-18 reader judge (second run): the fig's trunk close-up added

- A second reader-judge run started on the same sighting (12a88725) and built the tree again; the 00:13 run had already published it, so that copy was dropped at the rebase. What it added: the reader's second photograph (the buttressed trunk with its hollow base, viewed, daylight, colour), now in syd_008's strip. Nothing else waited: no reports, tips, feedback or reader notes. The other 37 waiting leads are our own account's (`mine`). Two judge runs firing on one sighting is worth a look at the trigger's concurrency.

## 2026-11-18 night run (window from 00:23 UTC): Philadelphia and Baltimore, one tree each

No reader photos, notes or red health rows (only 5 of 12 knocks delivered, GitHub's drop). Rung 5, US deepen. Verify passes on Philadelphia and Baltimore each found one flagged tree; both cities are close to mined out at this bar and their leads were kept. Write pass merged `phl_022` (Morris Arboretum weeping wych elm, paid entry) and `bal_005` (Bolton Hill walnut, flagged, thin confirmation stated on the page). The three Fort Worth READY leads stay leads (each already declined: a row of young oaks, a seminary campus, a bare city-layer point); `leads.py --ready` still counts them because it does not read those `why` notes. Five other pending files held for access or duplicate; `sfo_012` is the same tree as `sfo_004` (fold its pin and girth in an enrichment pass). Philadelphia intro no longer promises "four trees". Preflight 0 problems. Both claims released.

## 2026-11-18 reader judge: a Moreton Bay fig in Rushcutters Bay Park, Sydney, is live

- **New tree**: sydney/syd_008, The Moreton Bay Fig of Rushcutters Bay Park, from a reader's app photograph (12a88725) with a GPS fix. OpenStreetMap places the fix inside Rushcutters Bay Park. Both pictures were viewed: a lone fig on a lawn with buttress roots, and a close shot of the hollow trunk with the skate park behind. The reader's note is quoted, and their age (150) and girth (7.5 m) are written on the page as their figures. The pin is confirmed. Sydney's FAQ now counts eight pins. Photo month left empty: green leaves alone don't settle a season.
- Nothing else was waiting. There were no open reports, no feedback without a verdict, no new tree notes, and reader_words found nothing to quote. The 37 `lead` rows marked `mine` (our own account, September and October) were left alone, as before.
- Preflight first stopped on a colon reveal in the new story. The sentence was rewritten before the push.

## 2026-11-18 night run (window from 23:58 UTC)

- **Product: three Fort Worth trees added, app-only under APP FIRST** (ftw_021 Southern Magnolia in the Botanic Garden, ftw_028 Downtown Red Mulberry, ftw_029 Veterans Memorial Park oaks), all flagged: one source, approximate pins, no photographs. Preflight 0 problems. Fort Worth is at 29 trees.
- Rung 1: nothing waiting (no photographs, no tree notes). Rung 2: health was red only on two open escaped-bug rows whose fixes and tests had already landed on 11-17 (mailcheck "walks" verb, Android map sheet drag); closed them. Nightly knocks 4 of 12 in 24h is GitHub dropping the cron; knock.yml covers it.
- Rung 5: the shelf was under its floor (the "awaiting a writer" list is stale files, only single trees need stories). Claimed Leeds (Hidde's UK-first list) but released it, since none of its 5 leads has a coordinate (the 2026-10-03 warning: ~410k tokens for one tree). Fort Worth verify pass gave only 2 trees for ~90k tokens, because the city layer holds no girth, age or address. Portland and others refused as full.
- **Product, later in the window: Leeds opens with two trees** (lds_003 Kirkstall Abbey ginkgo, gold every November; lds_004 Bingley Arms yew at Bardsey, "over a thousand years" said to be pub lore and written as such). Both app-only, flagged, approximate site pins, no photographs; Leeds is below four so it has no place page. The Leeds verify pass (~170k tokens, UK-first) also found Nellie's Tree, but it is already live as abf_001 in Aberford, so it was dropped as a duplicate; the Shire Oak successor (about 1957, young) stays a lead. Lesson: check `backlog.py` by distance before dispatching a from-zero pass on a city whose famous trees may sit under a neighbouring village. Sheffield was claimed and released (no coordinates); it is walled 48h.
- Enrichment for Lisbon, Barcelona and Oahu closed nothing (no register page for the ISA oak, London plane has no striking season, Honolulu's record has no better coordinate); the 6 gaps are recorded as dead ends for 90 days. For whoever picks up Oahu: the Honolulu exceptional-tree record lists the aquarium banyan at 54 ft and a 160.4 inch diameter, unit of the circumference field unconfirmed.
- Birmingham (UK) verify pass: 0 trees, ~90k tokens. No tree-level pin anywhere (no OSM node, Wikidata entry or Geograph grid reference for a named tree; Nominatim returned only streets). Four leads added, three blocked (Selly Oak stump, Centenary Square plane felled 2017, the Sutton Park oak reported dead). The best lead is the Botanical Gardens copper beech (paid, walk-through garden so no site pin allowed); it ships on a reader's GPS fix or geotagged photo. Birmingham is walled 48h and a UK id prefix other than `bhm` (Alabama) is needed, e.g. `bmu`. No further from-zero pass on Birmingham without a new angle.
- Nothing refused by the tool list. Fort Worth is now thin on supply; next windows should open a UK city that has coordinates, or scout a register for Birmingham, Sheffield or Leeds.

## 2026-11-17 reader judge: a second run on the Daintree fig and the Valley Forge photos

- A second run judged the same three photographs at the same time as the run below and reached the same verdicts. At push it found that run's commit already live and dropped its own copy. Its two additions: daintree/dtr_001 now has `paid_entry: true`, and the four tree notes from today are marked read (Valley Forge, Ankerwycke, Oslo, Washington DC; none hidden). The older `lead` rows from September and October (Nara, Kyoto, Kyushu, Tokyo, Baarn) have no photograph on this machine and most are from our own account, so they were not judged.

## 2026-11-17 reader judge: a Daintree strangler fig is live; the Valley Forge sycamore's lead photo was not the sender's and is off

- **Live: The Strangler Fig of the Daintree Discovery Centre (daintree/dtr_001, Queensland, Australia), sighting 4fe1cb00.** The photograph was viewed: from the boardwalk it looks up a column of fused, latticed fig roots climbing into the canopy among fan palms, with a visitor at the rail. The pin is the reader's GPS fix (confirmed). The reader's 500 to 600 years are stated as theirs. Only their sentence about the lost host tree is quoted, because the rest of their note reads like the centre's own description. Their second file is a 194 by 260 pixel thumbnail that may not be theirs, so it is not used. The species is "Fig (Ficus sp.)", matching Tilarán, because preflight allows one common name per species. Entry is paid. It is a new one-tree place (no place page), and "Daintree Rainforest" is now in city-aliases.
- **Valley Forge sycamore (vfg_001).** The finder sent two more photographs of their tree, bare in November (455f464a, fd777c00). Then they wrote that the lead photograph from their first sighting (c4b5f1b1) **was not one they took** (report 1000077). That photograph is deleted from the site. Their own fd777c00 now leads, and 455f464a is in the gallery. They also measured the girth that day at 6.95 m (report 1000076): the story and FAQ now quote it as theirs (it was their 650 cm estimate), and `girth_cm` stays empty. The pin is unchanged. Both reports carry their own words, so they are closed `holds` with no mail. **For Hidde: a suggested reply is in drafts/reply-reader-1000077-2026-11-17.md.**
- Nothing else was waiting: no tips, no feedback without a verdict, no other reports.

## 2026-11-17 reader judge: nothing new (a second run on the Lightning Ridge coolibah)

- A second run picked up the coolibah (9620278d) at the same time as the one below and wrote it too. At push it found lightning-ridge/lri_001 already live and threw its copy away. Its one addition: Lightning Ridge is now looked up in data/city-aliases.json (no other names), which clears preflight's note. No other reader's tree, report, tip or feedback was waiting.

## 2026-11-17 reader judge: an old coolibah near Lightning Ridge is live

- **Live: The Coolibah South of Lightning Ridge (lightning-ridge/lri_001, NSW, Australia), sighting 9620278d.** It was sent through the app with a GPS fix at the tree and two photographs, both viewed. The tree is a massive hollow trunk in open bush with limbs sweeping almost to the ground and a man at its foot for scale, in daylight and colour. It ships under the closed list. The pin is the GPS fix (confirmed). The reader's 500 years (with their question mark) and 7.5 m girth are stated as theirs, and `girth_cm` is left empty. OpenStreetMap names no road or site at the fix, so the access line says the landowner is unconfirmed and to ask locally (as Tilarán did). It is a new one-tree place, so there is no place page yet (`PLACE_PAGE_MIN_TREES`). The photo has no date, shows no snow and has no `taken_month`. The reader's congratulation goes through the usual `tree_approved.py` route.
- No open reports, no unjudged tips, no feedback without a verdict, no reader words waiting. The 37 older leads noted below still have no photograph on this runner and stay unjudged.
- preflight notes that `city_names.py` has not looked up lightning-ridge yet. This is not a problem.

## 2026-11-17 reader judge: a reader's photograph now leads the Ankerwycke Yew

- **Live: a reader's photograph of the Ankerwycke Yew (Runnymede, ank_001), sighting 5e906833.** It shows the hollow, fluted, buttressed trunk in daylight, and its GPS fix is 7 m from our pin. It went in as `add`, so the reader's photo is now the lead and the old one moves into the strip. The pin was already confirmed, so it stays where it is; the pin step's HTTPError changed nothing. The reader's mail goes through the usual weekly bundle.
- No open reports, no unjudged tips, no feedback without a verdict, no reader words waiting.
- **Not judged: 37 older leads in data/leads/_sightings.json** (status `lead`, no `hold`; Nara, Kyoto, Taketa, Kagoshima, Miyazaki, Tokyo, Baarn). None of their photographs are on this runner, since only today's file is in out/sightings/, and a photograph is never judged blind. Most are Hidde's own account (`mine`), not readers' trees. A run that fetches their files can judge them.

## 2026-11-17 reader judge: the Signal Tree in Akron waits as a lead

- **Lead: tip 1115, the Signal Tree, Akron.** It is a three-pronged bur oak of 250 to 350 years in Cascade Valley Metro Park, alive and cared for by Davey Tree (2025). It is not live because Summit Metro Parks has closed the Chuckery Area and its Peck Road entrance since 2023 for the Gorge Dam work, with closures expected through at least 2028. It is recorded in data/leads/akron.json with its sources and the reader's pin. The tip carries the reader's own words, so the answer is a draft, not a sent mail.
- For Hidde: drafts/reply-reader-1115-2026-11-17.md asks the Akron reader whether the tree can be seen from open ground. A yes ships it, with the pin on the viewing spot.
- This run also judged the Puebla fir (e080b473) and would have published it. A parallel run had already pushed it as held `not_special`, so that verdict stands and this run's version was dropped. It was a close call either way: the bared roots against "common on any eroding bank".

## 2026-11-17 reader judge: a Mexican hillside fir held

- **Held `not_special`: sighting e080b473** (app, GPS 19.1284, -97.5133, highland forest near Tlachichuca, Puebla, Mexico). Photograph viewed: a mid-sized fir, among others, on top of an eroded earth bank, with its roots hanging bare down the cut. Daylight, colour, a GPS fix. Bare roots like these are common on any eroding bank, and nothing in the tree marks it as old, big or storied. It was sent as "A tree I found" with no words; a name, age, girth or story from the reader would change it.
- No open reports, no feedback without a verdict, no reader words waiting. Nothing went live, so no deploy was dispatched.

## 2026-11-17 reader judge: a Colombian roadside tree held

- **Held `not_special`: sighting 034185b2** (app, GPS 6.4777, -73.1174, Santander, Colombia). Photograph viewed: a slender young tree alone by a dirt road, its small crown hung with moss. A good frame, but sent as "A tree I found" with no words, and nothing marks it as old or big. A name, age or story from the reader would change it. Tip 1112 is the app's companion row for the same photograph and is closed as a duplicate.
- This run also judged the Sofienbergparken horse chestnut (tip 1111), but an earlier run had already published it as osl_005, so that part was dropped at the rebase. No open reports, no unhandled feedback, no reader words waiting.

## 2026-11-17 session: BT refuses our sign-up mail through Gmail

Breakage: a reader who signed up at 18:45 UTC with a btinternet.com address never got in. Their welcome mail (with the confirm link) went through Gmail as info@ and BT answered "550 User unknown". Hidde's own Gmail mail to the same address at 20:18 UTC was taken, with no bounce. So the address is real and BT refuses mail that is unsigned for our domain, as Apple's relay did this afternoon. Four other BT accounts confirmed on 11-15, so BT does this only some of the time. Fix: btinternet.com, btopenworld.com and talk21.com join `SIGNED_ONLY_DOMAINS` in scripts/mailer.py and in the hook, and qa's `check_one_mail_route_rule()` holds btinternet.com. LIVE in the hook since 20:33 UTC: send-email v6 deployed with a fresh 7-day token Hidde made (it carries this afternoon's Apple relay line too, which had waited for a redeploy). Tested: a signed test welcome to our own Gmail alias arrived, an unsigned call is refused (401), the hook is still switched on. Not tested: a real BT inbox (we have none). Sent with Hidde's yes: a fresh sign-in link with an apology to that reader, through Resend only (batch `bt-signin-resend`).

Every bounce since 11-15 checked again (Hidde: "ga die ook nog maar eens na"), each against Supabase: ours were Yahoo's servers (fixed 11-16, resent), Apple's relay (fixed and resent today) and BT (above). Theirs, proven: outlook.co and a misspelt gmail.com address (both people signed up again correctly within minutes and are in), hoymail.com (no mail server at all, a typo of hotmail; that person never came back), a Google account whose own domain no longer exists (they sign in through Google, only our mails miss). Since the hook went live, Yahoo-family sign-ups confirm 4 of 6, others 71 of 80: no sign of a further fault, too few to be sure. Resend's delivery log cannot be read with our key (send-only).

For Hidde: 9 Yahoo-family sign-ups from 11-15/16 are still not in, after our two mails failed them. drafts/signin-sorry-yahoo-2026-11-23.md is one last apology with a working link, sendable from Monday 2026-11-23 (week's rest); it goes on your yes only. Hidde asked on 11-17 to be reminded in a day. Who: email sign-ups on Yahoo's servers (`YAHOO_FAMILY`) created 11-15 to 11-16 10:40 UTC and still unconfirmed on the day, picked fresh from Supabase (out/tmp/yahoo_after_fix.py shows them). How: a fresh magic link each (generate_link, redirect /account), Resend only, logged in data/outreach-sent.json, as out/tmp/bt_signin_link.py did for the BT reader. One mail each, never a second. Subject: "Your Ancient Trees sign-in link".

## 2026-11-17 reader judge: a reader's horse chestnut live in Oslo

- **Oslo (osl_005, the Low-Armed Chestnut of Sofienbergparken)**: a reader sent this tree through the website, with a photograph and the park's name. The photo shows a horse chestnut with a leaning dark trunk and long crooked limbs that sweep out almost to the ground, in daylight. It is somewhat special, so it went live under the closed list. There was no GPS fix, so the pin marks the park (approximate) and the story says so. Their age of 150 to 168 years is given as their estimate. It fits the park's history (a cemetery from 1858, turned into a park from 1918), but no record names the tree. The photo has no date and shows no snow, so no month was set. Oslo now has five trees. The congratulation mail goes with the next knock.
- **Baarn (brn_008)**: a photograph sent as the Town Hall Plane came from one of our own accounts (`mine`). It shows a plane on an open park lawn with no building, so it is a different tree. The verdict is `other_tree`, and the lead is held as `doubt_location` because its coordinate is our own pin. Nothing was published.
- No open reports, no feedback without a verdict, and no reader words to quote.

## 2026-11-17 session: Google Play listing set up, nothing uploaded yet

- **For Hidde, later: the waitlist test mail is agreed and waits for the build.** Text and plan in drafts/android-test-invite.md: two waves (about 200 newest Gmail addresses the day Google approves the first closed-test build, the other ~1,700 a few days later), "We expect a live version in 3 to 4 weeks", sent only on his "verstuur". Next step is his go for the rebuild and his upload of the .aab. Lesson recorded in PITCH_VOICE.md: say we want to test, never blame Google's rule.
- **Play test setup done the same evening**: closed test "Alpha" in all 178 countries, tester list "Ancient Trees testers" with the 50 newest Gmail addresses from the waitlist (Play refused 100 and 200 in one save, no reason given; details and next step in the draft), list "Ancient Trees team" (Hidde) on both the closed and the internal test, feedback to info@. The join link https://play.google.com/apps/testing/app.ancienttrees.android is in the mail; it works once Google approves the first build. Store tags: Maps and navigation, Travel guide, Travel and local, Science education (Play has no nature or walking tag). The publishing overview shows nothing else open: everything left is locked until the first .aab is uploaded.

- **Play Console, with Hidde**: phone verified on his Samsung (Play Console app), app created (`app.ancienttrees.android`, en-GB, free). All eleven setup tasks done: privacy policy, sign-in details, ads, content rating, audience 16+, Data safety (crash logs added, PostHog since 11-16), government, financial, health, category Travel & Local, contact info@ancienttrees.app and https://ancienttrees.app.
- **Reviewer account**: Google's reviewers may not create accounts, so Hidde made a Gmail for them and its Supabase account exists (profile private, in data/our-accounts.json, so it never counts as a reader). Its address and password are in Play Console > Sign-in details only.
- **Store listing in nine languages** (en-GB, en-US, nl, de, fr, es, it, pt-PT, ja): the iPhone's name and text, plus one paragraph and a longer season line that carry the iOS keyword field, because Play has no keyword field and indexes the description (drafts/play-store-listing.md). Icon and feature graphic labelled as made with AI (Hidde: the logo tree is AI-made).
- **Screenshots**: scripts/play_frames.py dresses the Android screens like the App Store's (cream ground, his captions, his opener photo, an Android phone running off the bottom, 1080x1920). Five panels on Play. The screens themselves are from 2026-11-11: play_shots.py could not run today (his Samsung and two emulators attached, one in use by the debugging session); retake before production.
- **Status**: everything "ready to send for review"; nothing is public until a release goes out. **Next**: rebuild the .aab with today's fixes, upload to the closed test (Google-generated signing key), then the Play App Signing SHA-256 into assetlinks.json. Testers: 1 of 12 (`python3 scripts/android_testers.py`).

## 2026-11-17 daily publish

- **Daily publish: queue empty.** The two builders newer than the last check (build_write_2026_11_17, ten app-only trees; build_reader_trees_2026_11_17, eleven reader trees) are already on main, and neither counts against the pace. Nothing published, pace untouched, preflight 0 problems. For Hidde: the daily task "publish-held-trees-daily" can be switched off under Scheduled; write passes put trees straight into the app, so nothing waits for it.

## 2026-11-17 reader judge: a reader's photograph now leads the Jefferson Elm in Washington

- **Washington DC (wdc_004)**: a reader sent a daylight summer photo of the National Mall Jefferson Elm. It shows the full crown on the Mall lawn, with the Natural History Museum dome across the green. The species and setting match our record. It is now the lead photograph (`add`), and the iNaturalist picture moved into the strip. The reader got the "on the page" mail. The pin stays approximate because the photo's coordinate was our own pin, not a GPS fix. The file has no date and shows green leaves, so no month was set.
- No open reports, no feedback without a verdict, no tips to judge, and no reader words to quote. The 37 waiting leads in _sightings.json are our own (`mine`), as before.

## 2026-11-17 reader judge: the five photo-less tips settled, nothing new live

- No product change. No reader photographs waiting, no open reports, no open feedback, and reader_words lists nothing to quote.
- The five tips (1102, 885, 755, 691, 707) now have verdicts. None of them was a photograph waiting to be fetched: each is the app's companion submission row for a sighting that no longer exists on the server, so no photograph can ever arrive. 755 (Waipoua Forest) is our Tane Mahuta and Te Matua Ngahere, whose reader photographs from that day are already on wai_001 and wai_002 (`publish`, nothing to add). 707 duplicates the photograph that made lyt_001 (Lytham) live (`hold`). 691, 885 ("Ridiculously tall") and 1102 have no place, coordinate or name, so there is nothing to place or record (`hold`, no_location).
- Not reader work: the 37 waiting leads in _sightings.json are our own photographs (`mine`) or have no photograph at all (fetch_waiting_photos `--count` is 0).

## 2026-11-17 reader judge: the fallen Gunnersbury mulberry, whole, from a reader

- Live: two more photographs from the same reader of the Gunnersbury Park Black Mulberry (lon_030). The wide one shows the whole tree as the page describes it, the trunk lying along the grass with branches rising straight up, and went on as `add`. The close-up of a young shoot with a green fruit spike went into the gallery behind the lead (`strip`). Species and description both checked against the photographs. The pin did not move: these came from the web page and carry our own pin, not a GPS fix.
- Notes: seven new notes on trees read. One ("bla test" on the Glorieta de Goya fig) hidden as a test line; the other six stay (Amsterdam, Balmerino, Ferrara, Bologna, Finsbury Circus, Stow-on-the-Wold). reader_words lists nothing waiting.
- Repaired: the previous run's push had stopped mid-rebase on a timestamp conflict in data/ambassadors.json. That is resolved and its commit carried over. The intake's autostash clashed in data/judgements.json, so the stubs were rewritten from upstream.
- Still waiting: the same five photo-less tips (1102, 885, 755, 691, 707). Their photographs are still not on this machine, so they were not judged blind. The 37 waiting leads in _sightings.json are our own (`mine`). No open reports and no open feedback.

## 2026-11-17 session: Baarn sequoia story no longer says dog walkers

A reader who knows the park (Hidde's mother) said dogs are not allowed in the Cantonpark. The giant sequoia's story said the trees "share a lawn with dog walkers"; it now says "with anyone who walks in off the street". English only, Baarn has no translation.

## 2026-11-17 reader judge: two mulberry photos in the gallery, 12 tips recorded as leads

- Live: a reader's two close-ups of the Gunnersbury Park Black Mulberry (lon_030), one of its leaves and one of it in spring flower, are in the tree's gallery behind the lead (`strip`; mulberry leaf and flower checked against the species; the lead stays). Mail to the reader sent by sightings_publish.py. The pin did not move: the photographs were sent from the web page and carry our pin, not a GPS fix.
- Tips without a photograph, 12 named trees: recorded as leads with the reader's words and map links, verdict `lead`. Heidelberg (Arboretum 1 sequoia, Romantik-Eiche, Holdermanns-Eiche), Ho Chi Minh City banyan, Alerce Costero (Fitzroya), Cat Island bald cypress (US), Arderne Gardens fig (Cape Town), Tsitsikamma Big Tree, Nossob camel thorn, Bagni di Lusnizza oak, the Mouchao olive (Portugal) and a map link for the held Castagno Miraglia. None shipped here: each needs sources and a resolved pin, which is a verify pass, not this run. The Cat Island cypress (US, press source named) and the Mouchao olive (Portugal, Wikipedia) are the cheapest.
- Still waiting: five tips named only by an app photo id (1102 Maine, 885 Tasmania, 755 Waipoua, 691 Gisborne area, 707 near Southport). Their photographs are not on this machine, so they were not judged blind; 707's sighting was rejected before. The 37 waiting leads in data/leads/_sightings.json are all our own (`mine`) photos, so they are not readers' trees. No open reports, no open feedback, no reader words to quote.

## 2026-11-17 session: Apple relay mails bounced, now through Resend

Breakage: since the 11-16 route split, mails to Sign in with Apple addresses (@privaterelay.appleid.com) went through Gmail, unsigned for our domain. Read from his Sent folder and bounces: about 30 went that way and 5 bounced "user not found", all from the reader judge's run at 17:19 UTC today (one of those addresses had taken a Gmail mail on 11-16), against none of 33 through Resend before. So Apple refuses unsigned mail some of the time. The 5 were resent unchanged through Resend only and logged (batch `apple-relay-resend`). Fix: scripts/mailer.py sends those addresses through Resend like Yahoo (`on_apple_relay()`), the Supabase hook has the same line (only matters on its next paste; Apple users never get its sign-in mails), qa's `check_one_mail_route_rule()` holds both. Load on Resend: 10 to 24 a day of its 100. Deploy: the afternoon failures were the Dublin cedar's "a page of its own", fixed 17:27 by a run; deploy 44138841637 running.

## 2026-11-17 night run, third attempt: 0 trees, Guimaraes a wall

- READY shelf empty (0). Guimaraes verify (4th deepen pass): its 12 near register rows fold into gui_001 to gui_010, the rest are 15 to 19 km out in other concelhos. Lead logged: Ermal oak, Vieira do Minho (6.48 m girth, 313 y), for a Braga-region pass if access and transport are sourced. Claim released, wall 48h.
- Translations stay paused (TRANSLATIONS_OUT). Next: Zurich register BUILD, or new reader trees reopening walled cities.

## 2026-11-17 night run, later attempt: 0 trees, shelf and staged cities empty

- Write shelf empty (see the write pass below). Verify passes: San Francisco (10th, nothing new) and Frankfurt (no register, 2 leads kept, nothing verified). Graz and Nuremberg claimed and released: under a quarter of their leads have a coordinate. All four are walls for 48h; Portland is full.
- Next: Zurich register BUILD (23 unjudged rows) or a register scout. A new reader tree or register is what reopens San Francisco.

## 2026-11-17 write pass: nothing to write, no trees shipped

- **No trees shipped.** `passcheck.py --pending` lists only nine unpublished trees. The suggested US and UK files (new-york-3 and -4, wisconsin, washington-dc-2, the Boston files, wales-yews, somerset-dorset-yews, southeast-england-yews) are all fully published already. Every one of the nine was held by an earlier pass for a reason this pass cannot clear without new research: brd_001 Brindisi figs and frk_027 Frankfurt mulberry (no public entry or viewing place, hard rule 10), inn_007 Innsbruck lime (probably in a private yard), not_002 Noto carob (nobody knows who owns the land), det_001 and det_002 Detroit Elmwood (no coordinate in an 86-acre cemetery), nyc_031 Saratoga Park oak (only a park-level pin, no recognition line), and sfo_012 (the same tree as live sfo_004, to be folded in by enrichment). bri_017 in bristol-verified.json has the same name as the live bri_017 and is the same chestnut, so it is not a new tree.
- **Coimbra's one READY lead** (the two Buçaco sequoias at the Ermida de Santo Elias) is now `held` in data/leads/coimbra.json. The live bsc_011 story already says that pair stands off any path the forest maintains, and the verify pass could not tell whether it is bsc_010. It needs a Buçaco pass on access and identity. READY is now 0.
- **What a write pass needs next**: a verify pass to fill the shelf (US and UK first), or a Detroit Elmwood pin from the cemetery's tree-tour maps, which would let det_001 and det_002 ship as they are already written.

## 2026-11-17 reader judge (twelfth pass): a reader's photographs are the first on the Saint-Jammes beech

- **soreze/sor_001, The Multisecular Beech of Saint-Jammes**: a reader sent two photographs from the tree's web page, and the tree had none until now. The lead is the whole beech in autumn leaf, its long limb on two steel props, with a walker beside the trunk for scale. The second photograph, the same tree in fog with the chapel ruins beside it, is in the strip. Now that the page has reader content it can be indexed, so its one colon-reveal sentence ("which is rather the point:") is rewritten. The photo-live mail is queued.
- **Bangor and Kanker**: this run judged the same two trees as the eleventh pass, which pushed first, so its bnm_001 and knk_001 stand. My copy of the Bangor tree was dropped. On Kanker I would have held the tree as `not_special`: it is a straight forest trunk about half a metre across, no bigger than its neighbours, with no note from the reader. That is a difference in judgement, not an error, and the tree stays live.
- **preflight**: `check_a_readers_age_reaches_the_page` now skips "Unknown", "not sure" and similar answers in a reader's age field, so a run no longer has to clear the reader's own field to pass.
- **Still open**: the same 17 photo-less tips.

## 2026-11-17 night run (window 17:18 UTC): rung 1 then rung 2
- **Saint-Jammes beech**: the twelfth reader-judge pass published the same two photographs while this run judged them, so this run's copy was skipped in the rebase.
- **Build fix:** the last deploy failed QA on the Dublin Weeping Cedar Tunnel story ("so it has a page of its own", our publishing rule shown to the reader); rewritten. The Sorèze colon reveal rewritten too.
- Not reached: 16 tip rows without a photograph still wait for a verdict (health.py LATE), the open BUG rows in data/code-audit.json and the WebGL web error.

## 2026-11-17 reader judge (eleventh pass): readers' trees live in Bangor, Maine, and Kanker, India

- **bangor-maine/bnm_001, The White Pine at the Orono Bog Boardwalk** (sighting 0305569a): a huge twin-stemmed eastern white pine beside the trailhead kiosk in the Bangor City Forest. The pin is the reader's GPS fix (confirmed), and the story quotes their note ("strikingly large"). This is a new US place, so `bangor-maine` is added to data/us-states.json. The app's age field held the word "Unknown", which is not an age, so it was cleared on the lead.
- **kanker/knk_001, The Tall Tree on the Kanker Forest Track** (sighting f8c010fc): a ruler-straight forest tree in Chhattisgarh with a person at its foot for scale. The species is not established and the page asks readers to name it. Access is honest: the forest manager is not confirmed. India is out of focus for our own research only, never for a reader's tree.
- This run also judged the Quito pine and orange, and reached the same verdicts as the tenth pass, which pushed first. Its uio_001 stands, and this run's copy was dropped in the rebase.
- Both new places have one tree each, so they get no place page. Congratulation mails go out on the next knock. There were no open reports and no feedback without a verdict, and reader_words had nothing new. **Still open**: the 17 photo-less tips (newest 1102, 1065, 1061 to 1063 Heidelberg, 1032), which need a source check that would not fit in this run. The older (September and October) Japanese and Dutch leads have no photograph on this runner, so they were not judged again.

## 2026-11-17 reader judge (tenth pass): a many-stemmed pine opens Quito

- **New tree, quito/uio_001, The Many-Stemmed Pine of La Pradera** (sighting c4a7a901): a pine that splits low into five or more straight stems and rises into one tall crown at the pavement edge. A second frame looks up the stems and is in the strip. The species (Monterey pine) and the 450 cm girth are the reader's, stated as theirs. While adding the tree, the reader moved its pin 91 m south of the app's fix, which had landed on an apartment block, to La Pradera street by the FLACSO campus. We took their placement because it is their own tree, kept it `approximate`, and recorded the site from OpenStreetMap. Quito is a new one-tree place: it has its intro, question fields and three FAQ, and no place page.
- **Held `not_special`: the orange tree beside it** (7b889995): a healthy, ordinary street orange in fruit. The pine behind it is the tree worth the walk, and that one is now live.
- **Reports 1000073 and 1000074** were the pin moves the same reader made while adding those two trees. Both are closed `holds` with no mail, per the brief: their congratulation comes with the tree.
- **Geneva**: this run judged the same two photographs as the ninth pass, which pushed first, so its version stands. On top of it, the two colon sentences in gen_019 are now also rewritten in the French overlay.
- No feedback was open, and reader_words found nothing. **Still open**: the 16 photo-less tips from the fourth pass.

## 2026-11-17 reader judge (ninth pass): first photographs for the Geneva cedar and plane

- **geneva/gen_019, the Himalayan Cedar, and geneva/gen_012, the Sécheron Plane**: one reader photographed both at dusk by the lake, 39 m and 28 m from our pins. Neither page had a photograph, so these now lead. Two colon reveals in gen_019's story were rewritten, because the check reads a page once it has a photo. The pin catch-up hit an HTTP error, so the next knock moves the pins. The reader's "it is on the page" mail is pending in data/photo-live-mailed.json.
- This run judged the Milton Keynes apple row, the Kvill Oak and Ekebyhovseken photographs and feedback 1092 as well. The eighth pass pushed first, so its work stands and this run's copies were dropped in the rebase. **Still open**: the 16 photo-less tips. Four of their stubs (707, 691, 755, 885) carry a sighting UUID as the tree name: 707 is sighting 71f93157, already judged, so they look like app bookkeeping rows rather than tips.

## 2026-11-17 reader judge (eighth pass): an apple row in Milton Keynes goes live; readers' photographs now lead the Kvill Oak and Ekebyhovseken

- **New tree, milton-keynes/mkn_003, The Leaning Apple Row of Linford Wood** (sighting 4ea907d1, the same photograph also sent as 58efdc92 from 40 m along the path, so one entry): a line of old apple trees beside a public paved path off Foxhunter Drive (place from OpenStreetMap). Their trunks are grey, split and hollowed and all lean out over the path. The pin is the reader's GPS fix (confirmed). The story quotes their note ("possibly Bramley") as their own. There is no age, girth or source. Milton Keynes now has three trees, and its intro names the row.
- **Kvill Oak (rumskulla/rkm_001)**: a second reader's late-summer photograph, with a person for scale, is added and now leads the page. The earlier reader's photo moves to the strip.
- **Ekebyhovseken (ekero/eke_001)**: a reader's photograph of the whole trunk in a snowy field (February 2019) now leads the page in place of the Commons photo, which moves to the strip. The second copy (64d7a378) was the same file and is rejected as a duplicate.
- **Feedback 1092** (an app user asking how to follow uploaders, edit a sent description and tag seasons): closed `needs_hidde`. The draft is drafts/reply-reader-1092-2026-11-17.md. One point is checked (the app has no season control, the date sets it); the other two are marked to check before any reply.
- Seville sev_009 (84c4d953): the seventh pass rejected it (an all-black test frame from our own account); its verdict stands.
- No open reports, and reader_words found nothing.
- **Still open**: the same 16 photo-less tips as the fourth pass, for the reasons given there. None names a tree we already map. The pin catch-up hit an HTTPError again, which has no effect because every pin involved is a confirmed GPS fix.

## 2026-11-17 reader judge (seventh pass): one test frame rejected

- **seville/sev_009** (sighting 84c4d953): rejected. The frame is all black, taken in the Netherlands by one of our own accounts, so it was a test. The sixth pass had already handled Cheapside, so this run kept main's version of that work.
- No reports or feedback were open, and reader_words found nothing. **Still open**: the 16 photo-less tips. Several name well-sourced trees (Castagno Miraglia, the Mouchão olive, the Lusnizza oak in the MASAF register, the Cat Island cypress, Tsitsikamma, Arderne Gardens, the Heidelberg Arboretum 1 sequoia). Writing them takes a story pass, which does not fit a reader-judge window.

## 2026-11-17 reader judge (sixth pass): the Cheapside Plane's pin is on its corner now, and a reader's photograph leads its page

- **The Cheapside Plane (lon_003)**: a reader sent a photograph through the app showing the tree in full leaf behind the churchyard railings, in daylight. It was added and now leads the page. The same reader reported "wrong location" (1000072, "Corner of wood street and cheapside"), and they were right. Our "confirmed" pin stood 190 m up Wood Street. It now sits on their GPS fix at the corner the story names, and `pin_source` records the move. `tree_reports.py --thank` refused because their line counts as their own words, so the report is closed `holds` and a suggested reply is in drafts/reply-reader-1000072-2026-11-17.md for Hidde.
- This run also built the Zamalek Banyan, but the fifth pass (below) pushed it first. On the rebase, main's version was kept whole and only the Cheapside work was carried over.

## 2026-11-17 reader judge (fifth pass): the Zamalek Banyan is live in Cairo

- **New tree, cairo/cai_001, The Zamalek Banyan** (sighting 2bef0f92, sent through the app today): the photograph shows a banyan's grey limbs dropping aerial roots grown into pillar trunks, behind a low wall and railing, daylight. The reader linked Egyptian Streets (2022), which places a banyan about 150 years old on Al Borg street towards the Cairo Tower and dates the import of banyans by Khedive Ismail to 1868. The reader's GPS fix falls on that street, so the pin is confirmed. The source also calls the tree "the last standing one in Egypt" while naming another banyan at the Manial Palace, so the page makes no "last" claim. Cairo is a new one-tree place: it has its intro, question fields and three FAQ, and no place page until it grows. Egypt is out of focus only for our own research. Verdicts are recorded as `lead:` and `sight:`.
- No reports or feedback were open. reader_words found nothing.
- **Still open**: the same 16 photo-less tips as the fourth pass, left for a session for the reasons given there. The old `status: lead` rows in _sightings.json with no hold are all our own account's (`mine`) September and October shots. They are not readers' trees, so this run did not judge them.

## 2026-11-17 reader judge (fourth pass): the ledger caught up, sixteen tips left for a session

- **Rhodes Bald Cypress (bng_001)**: judged the same snow photograph as the third pass, same verdict; theirs kept. Added only the season: no date in the file and deep snow in frame, so `taken_month` 1 with the basis recorded (it said 11, the upload month).
- **Ledger catch-up**: five reader leads held earlier today (four `not_special`, one `bad_frame`) and tip:944 (the Sagole Baobab, already sgl_001) had their verdict in the lead files but not in data/judgements.json; now recorded there.
- **Left open, on purpose (session work, beyond this run's 20 minutes)**: 16 tips without a photograph still have no verdict, most of them famous, sourced trees that should ship: Oliveira do Mouchão (850, Wikipedia), Cat Island bald cypress (906, press link), Castagno Miraglia (970, already a held lead in _famous-italy.json for want of a pin; the reader sent a Maps link), Tsitsikamma Big Tree (939), Arderne Gardens fig (937), Nossob camel thorn (943), Alerce Costero Fitzroya (1032), three Heidelberg trees (1061 to 1063, Maps links), the Ho Chi Minh City banyan (1065), the Lusnizza oak (802, the reader's own figures), and the photo-less app trees 691, 707, 755 and 885. They need sources and pins, and stay on the late alarm rather than being filed as "lead".
- No open reports, no unjudged feedback, no readers' notes left to quote. The 37 older `mine` leads are our own account's and were left alone.

## 2026-11-17 reader judge (third pass, merged onto the second): three more reader photos go up

- A parallel pass judged the same queue and published El Sargento, the Glasnevin cedar and the Chiang Mai fig first. Its versions stand, and this pass's copies were dropped in the merge. Its Azores hold (abb593f0, `doubt_location`) also stands.
- **Added on top of it:**
  - **The Rhodes Bald Cypress (bng_001)** has the reader's winter snow photograph (017db4cf) as its lead. The sign close-up moves to the strip.
  - The two "duplicate" sightings each carried a further frame the second pass did not use. The new trunk view of **the Baobab Plane of Penenden Heath (mdb_001, e7bef8af extra 1)** and the close trunk view of **Barney the Plane (lon_008, 9c93b205 extra 1)** are now in those trees' strips. sightings-processed and judgements say `added` and `publish` for these sightings.
- The queue was already empty, so `judgement.py --scan` could not stub 017db4cf. Its `sight:` verdict was written into judgements.json by hand.
- The photo-less tips listed by `judgement.py --unjudged` still wait for the next run.

## 2026-11-17 session: the late-trees alarm counts from when a reader sent it

- **Measured**: of 649 things strangers sent in the last 7 days, 94% had a verdict. Reports, notes, ambassador requests and written feedback 100%, app photos 98%, trees added 82%: 31 without a recorded verdict while reader_backlog.py said 3 were late.
- **Fixed**: reader_backlog.py also checks every tree or city a stranger sent, by its own send time, against every place a verdict can live (`trees_without_a_verdict()`); it reports 17 late. judgement.py stubs an app tree whose sighting no longer exists as a tip (eight sat in no route: five were the same tree sent twice and are live via the second copy, rows closed `holds`; three are tips now: 691, 755 Waipoua, 885 Tasmania). tip:820 recorded as live (a-coruna/acr_001).
- **Breakage, fixed**: the `other_tree` route copied the queue's raw photo path into the public leads file (account id where a code belongs); `to_lead()` now codes it (test), the five paths are coded, and the pre-push qa check had stopped it.
- **Left for the reader judge (dispatched)**: 17 tips without a photograph from 11-15 to 11-17 (Mouchão olive, Cat Island bald cypress, Tsitsikamma big tree, Ferrara oak, Heidelberg x3, Chile's Fitzroya, Ho Chi Minh banyan, and others).

## 2026-11-17 reader judge (second pass): El Sargento, a weeping cedar and a Chiang Mai fig go live

- **Live (every photograph viewed, GPS fix at each)**: **El Sargento** (mexico-city/mex_011), Chapultepec's ahuehuete, dead since 1969 and still standing, under the standing-dead exception, sourced (Wikipedia, Chapultepec, CDMX tourism, Mexico Desconocido), with the Spanish overlay entry; the Mexico City intro and FAQ, which said it was not on the page, now say it is (English and Spanish). **The Weeping Cedar Tunnel of Glasnevin** (dublin/dub_020): the reader was unsure which of five trees it was, and it is none of them; Dublin's counts go from 19 to 20. **The Fig That Holds the Stones** (chiang-mai/cnx_002), a strangler fig west of the old city. This run also built the Morden mulberry, but the pass above had already published it as lon_054, so its version stands.
- **Queue**: El Sargento and the Chiang Mai fig had been sent for mex_006 and cnx_001, so both became `other_tree` first. Two photos the 11-17 session listed as "worth a page" are exact copies of pictures already on our trees: e7bef8af is the Baobab Plane's lead (mdb_001), and 9c93b205 is in Barney's strip (lon_008). Both were rejected as duplicates. The Kanazawa snow pine (0942bd2b) is held: it does not show the Karasaki pine's low branches over the pond, and Kenrokuen has hundreds of rigged pines.
- **Held**: the Azores aerial-root fig (abb593f0) is held as `doubt_location`. It was sent from azo_001's page, so its coordinate is our pin, and it is a different trunk from azo_001's lead photograph. **For a session**: our azo_001 recognition line ("mass of aerial roots") may fit this fig better than the lead photo does. Check which fig is the regional sheet's.
- Not done: _famous-mexico.json still lists El Sargento as a lead (preflight note). This run's duplicate mulberry image was moved out of site/public/photos into out/tmp/ and never committed.

## 2026-11-17 reader judge: a burred mulberry in Morden Hall Park goes live; the Dujiangyan ginkgo's pin is now marked approximate

- **The Burred Mulberry of Morden Hall Park (london/lon_054)** is live from a reader's photograph and GPS fix: a low, leaning black mulberry with a burred trunk, behind a protective fence in the National Trust park. The pin is confirmed. Its story quotes the reader's note. There is no age or girth yet, and the page asks for them.
- **The Temple Ginkgo of Dujiangyan (djy_001)**: the reader who sent it left a note on the tree saying "LOCATION ON MAP IS A GUESS", followed by a pasted chatbot-style summary naming it the Zhang Song ginkgo of Lidui Park. The pin was marked confirmed as a GPS fix. It is now marked approximate. The story, FAQ and answer no longer claim a GPS fix. The Lidui Park identification is on the page as the reader's own, unconfirmed, with a Chuanguan News source (2020) placing the Zhang Song ginkgo in Lidui Park. The pasted text was not quoted (closed in reader_words). A session could move the pin onto Lidui Park once the trunk is matched.
- Feedback 1080 (a reader asking how to add the old trees near them): a reply pointing to "Add a tree" is in drafts/reply-reader-1080-2026-11-17.md, closed `needs_hidde`.
- No open reports. The other leads still at `lead` are our own account's (`mine`), so no reader is waiting on them.

## 2026-11-17 session: two more ways a signed-in person was asked to sign in

- **Web (Hidde: "kun je nagaan of er nog anders zon loop zit?")**: back on the site after more than an hour, the bar said signed in but save, collect, Add a tree (/contribute opened sign-in by itself) and /account asked to sign in. The access token lasts an hour; signin-js renews it on load, but the one door (collection-js verify) and those pages decided first and kept "signed out". Now signin-js exposes the renewal as `window.atRefreshing` and the door, /contribute, /account and /account/settings wait for it.
- **App**: signed in with no signal and a spent token, writing a note, following someone (two screens), asking to be an ambassador or joining Plus opened the sign-in sheet. No signal is not a sign-out (Account.apply), so these now say it did not go through; only a real sign-out asks. In the next build.
- qa `check_signed_in_is_never_asked_to_sign_in()` guards both (it flagged all five app places before the fix). Two escaped-bug rows, closed with it. Every other sign-in call on web and app was read and asks only when signed out.

## 2026-11-17 session: the reader system's holes closed

- **Deploy unblocked**: every deploy since 12:53 failed QA on a reader's raw account id in data/leads/_sightings.json (a photo path written by a reader judge run); now coded with people.ref. `check_no_reader_traces_in_the_repo()` moved into qa's source-only checks, so it refuses the push, not the deploy an hour later. The raw id stays in git history (no force-push, hard rule 3); it is an opaque account id, no name or address.
- **Tips without a photograph get a verdict**: judgement.py's scan stubs them as `tip:<id>` (the app's uuid-named row beside a photographed tree is skipped); `--count` and `--unjudged`; the reader judge's gate and brief take them. Escaped bug closed with scripts/test_judgement_tips.py. 14 such tips from 11-15/16 now wait for the judge (Heidelberg oaks, Cape Town fig, Tsitsikamma, Nossob, Sagole baobab, Camaldoli chestnut, Mouchão olive and others).
- **Judge minutes counted, never capped** (Hidde: "ik heb liever niet dat die stopt"): scripts/judge_budget.py (82 agent minutes on its first day, invisible to run_health until now); a line under "Open for you" in the digest.
- **Alarm**: scripts/reader_backlog.py, read by health.py: anything a reader sent that waited over 24h without a verdict is RUNG 2. It found three at once (tips 802, 820, 850 from 11-15).
- **Found, not fixable here**: GitHub dropped the reader judge's 15-minute schedule all day and 8 of 12 night knocks; the Supabase trigger carries the instant route.

## 2026-11-17 session: one route for every reader's photograph

- **What changed**: a reader's photograph now always ends with a verdict as a tree of its own unless it shows one of ours (Hidde: "1 route"). Before, a photo sent for one of our trees could only be "this tree" or "rejected"; readers' trees died there (Dublin's weeping cedar arch in Glasnevin, an Azores fig curtained in aerial roots, a vast burred plane in London woods, El Sargento's dead ahuehuete in Chapultepec among them). Now: `other_tree` verdict in sightings_publish.py turns such a photo into a waiting lead (`to_lead()`, test in test_sightings.py); sightings_inbox.py sends every "not sure which tree" photograph down the lead route without the app's first-candidate name (`unsure_sightings()`, `unsure_among`); BRIEF_READER_JUDGE.md "One route".
- **Backfill, viewed here**: 13 photos set aside since September looked at again. 6 held under the closed list (Stockholm maple, Melbourne park tree, Paris square tree, Padua garden pagoda tree, Groningen beech: `not_special`; Bristol redwood: `bad_frame`). 7 worth a page go back through the intake for the reader judge to build: Dublin b59c4873, Azores abb593f0, Kanazawa pine 0942bd2b, the burred plane e7bef8af, Chiang Mai strangler fig c1046494, London plane 9c93b205, El Sargento fb383f1e (dead and standing: the 11-17 exception).
- Dublin's and Stockholm's queued "it is none of those" replies withdrawn.

## 2026-11-17 session: website and mailed photographs count as collected

- **Changed (Hidde, Katie on the Arbour Oak had 0 collected: "alle bomen die niet via de app zijn gekomen, maar via web of mail ... dat moet natuurlijk wel vanaf nu")**: `sightings_link.py tick_collected()`, which runs every knock, ticked only app photographs. It now also ticks a tree added through the website's form with a photograph (`submissions`, photo id `tip-<n>`, whether or not the photo made the page) and a mailed photograph whose sender has an account (name on the photo, address in the private send log, account with that address; `mailed_ticks()`).
- **Recovered today**: 14 website-form trees now in their senders' Collected (Katie's ntm_001 among them), plus 3 mailed ones (Michael Roe edi_003, un albero al giorno pad_013 and pad_014; the Cramond Association already had edi_008). The same run linked 22 app sightings the knock had not reached yet. Not recoverable: the Singapore mail photos carry no name, and Hannah Mayr, Hans Hofele, Ricard Llerins Bonet and the Barcelona archive have no account.

## 2026-11-17 reader judge: a new lead photo for the Greenwich chestnut

- **The Twisted Sweet Chestnut of Greenwich Park (lon_053)** has a new lead photo from the same reader who sent the old one: the whole tree, lit from the front under a gold crown. The older, backlit shot moved into the gallery. The reader's mail waits in the weekly bundle (pending, not sent).
- This run also judged the St Paul's planes and Queen Elizabeth's Oak with the same outcomes as the parallel run below. Its version was kept. The 37 older leads still at `lead` all come from our own account (`mine`, Japan and Baarn), so no reader is waiting on them.

## 2026-11-17 reader judge: the St Paul's Churchyard Planes get their first photograph; Queen Elizabeth's Oak held as fallen

- **lon_011, The St Paul's Churchyard Planes** (London): a reader's photograph is the tree's first. It shows a tall plane in autumn leaf behind the churchyard railings, and its GPS fix is 30 m from our pin. The species and the setting match. The pin moved to the reader's fix and is now confirmed. They got the "it's on the page" mail.
- **Report 1000071** (a pin move on the same planes, 43 m from the old approximate pin): the reader's spot is about 13 m from the photograph's fix, so the pin already sits where they pointed. Closed with the standard pin thank-you.
- **Queen Elizabeth's Oak, Greenwich Park** (a new tree from the app): held as `dead`. The photograph shows the fallen, hollow trunk lying inside its railings. The reader's second photograph, the Royal Parks board, says it "died many years ago". A fallen trunk never ships, and we retired it from London on 2026-07-27 for the same reason (lon_005, the sweet chestnut, stands for that corner of the park).
- No general feedback was waiting, and reader_words had nothing to quote.

## 2026-11-17 reader judge: the Darley Dale yew tip becomes a lead

- **Feedback 1075** (a tree tip from the app): an ancient yew at St Helen's Church, Darley Dale, which the reader says is thought to be 2000 years old. We don't map it yet. It is now a lead in data/leads/_famous-united-kingdom.json, waiting for a verify pass (no pin or source yet), and its ledger row is `handled`.
- This run also judged the same three photographs as the parallel run below, with the same outcomes. Its version was kept.

## 2026-11-17 reader judge: Amsterdam's tallest tree gets its first photograph; a second view of the Totteridge Yew

- **Oudemanhuispoort Elm (ams_021)** had no photograph. A reader's photo from today is now its lead: the tall, furrowed trunk rising past three storeys in the inner courtyard, with autumn leaves on the paving.
- **Totteridge Yew (lon_001)**: the same reader sent two photographs. The one looking up into the pollarded crown is now in the gallery behind the current lead, not leading, because a child peers out of the branches. The other is rejected as `wrong_subject`: it is a portrait of the child in the foliage, and the trunk is hidden.
- No open reports, no unjudged feedback, no waiting leads from strangers (the 37 waiting leads are our own photographs, marked `mine`), and no readers' notes left to quote. Both pins were already confirmed, so the pin catch-up's HTTPError changed nothing.

## 2026-11-17 reader judge: a rain tree in Mangaluru goes live (mlr_001); the Cremines yew gets its first photograph

- **New: The Rain Tree of Bolar** (mangaluru/mlr_001), a new one-tree place in India. A reader sent the photograph today with a GPS fix from the lane: a huge umbrella crown on fern-covered limbs above a garden wall and a transformer. They gave no name, species or note. The species is read from the photograph, and the story asks readers to confirm it. There is no register entry and no article nearby. It went live under the closed list, with the pin on the public lane and an access line saying the garden may be private. India is out of focus only for our own research.
- **Cremines (cre_001)**: Switzerland's oldest yew had no photograph. A reader's summer shot of the fluted trunk on its forest slope is now the lead.
- **Trolleken**: this run judged the same three photographs as the parallel run below and reached the same verdicts. On the rebase, main's version was kept.
- **Readers' words**: the three notes still open (Friedewald, Geelong, Te Araroa) were already reflected on their pages, so they are closed with `--done`. Raesfeld's note was quoted by the parallel run. Friedewald's age field read "350 to 700 years", which blended in the reader's figure. It now reads "350 to 440 years by published estimates; 500 to 700 by a reader's estimate".
- No open reports and no unjudged feedback. `sightings_publish.py` could not read coordinates for its pin catch-up (HTTPError). None was needed: both trees already had their pins.
- **Two reader-judge runs overlapped on the same queue.** Both judged Trolleken; the photographs and verdicts were identical, so nothing broke. The workflow could do with a concurrency group.

## 2026-11-17 reader judge: three readers' photographs on Trolleken, the Femeiche reader quoted

- **Live**: three photographs of Trolleken, the Troll Oak of Trollskogen on Öland (trs_001), from one reader, taken 2025-07-20, GPS 0 m from our pin. Looked at each: lobed oak leaves, the burred, hollowed trunk inside its rail fence, and in one the Naturum board reading "Trolleken". The shot where the trunk fills the frame now leads; the board shot and the backlit one sit in the strip (`add`). Its page now has a lead photograph unique to us.
- **Readers' words**: the Erler Femeiche (rsf_001) story now quotes the reader's own sentence on its NRW heritage title instead of paraphrasing it. Three older notes still wait in `reader_words.py` (Hammundeseiche, Geelong, Te Araroa) for a later run.
- The Baarn lead 7ff766ff (our own account) was held by the parallel run below; its verdict stands. The 37 older `mine` leads were left alone: our own accounts, never auto-published.
- No open reports, no feedback without a verdict. Preflight 0 problems, i18ncheck clean.

## 2026-11-17 reader judge: North Berwick's Act of Union beeches go live (nbw_001); the Isparta plane moves to where its finder put it

- **New: The Act of Union Beeches of North Berwick Law** (north-berwick/nbw_001), a new one-tree place. A reader's photograph from 11-15, held then "for Hidde" for want of a source, was judged again under the closed list when the same reader moved its pin (report 1000032). The Union planting has sources: Sir Hew Dalrymple, Lord North Berwick, planted the beeches for 1707 (Wikipedia citing Scotland on Sunday 2009, six left then; the Scotsman; a 2013 blog counting five). The reader's words are quoted, and the pin is their own move, marked approximate. Report 1000032 was closed with the standard pin thank-you. A custom reply written first was replaced, because the rule that landed on main during this run allows runs only the standard mails.
- **Isparta (isp_001)**: the reader who sent the plane, also the place's ambassador, moved its pin 892 m, from the middle of Çınar Sokak in Kafeler to 144. Cadde in Sülübey. Under the rule for a tree its own finder placed, their move stands (still approximate). Our "café street in Kutlubey" reading was a guess from the street name, so it is gone from the address, access, story, intro, question texts and FAQ. The name and slug stay: "Çınar Street" is the finder's own name for the tree, so the rename with a redirect that the parallel entry below asked about is not needed. Report 1000042 was closed with the standard pin thank-you.
- **Held**: 7ff766ff "European Beech in Baarn" came from one of our own accounts. The photograph shows a desk fan, so it is held as `wrong_subject` (a test).
- **Readers' words**: two notes were closed as not quotable (the Gennett Poplar's trailhead line; Moss Vale's pasted 1905 newspaper text plus an encyclopedia paragraph). Four are still open for a later run: Friedewald's Hammundeseiche (a German reader dates it to 500 to 700 years, which needs a "by a reader's estimate" edit), Geelong, Raesfeld and Te Araroa. There was no time left in this window.
- No reader photographs of trees we map were waiting. Preflight shows 0 problems and i18ncheck is clean.

## 2026-11-17 reader judge: the kauri's photo off the Huntington cypress, two more reports answered

- **Fixed (reader report 1000061, "on the map twice")**: the Huntington Montezuma Cypress (lax_017) was showing the kauri's photograph, byte for byte. The same reader sent one picture twice, once tagged to the cypress, and a viewing pass approved it (broad leaves, the orange trunk and the champion sign: the kauri). Taken off lax_017, which is back to no photo; the file is deleted and sighting ee54ed84 is now held `wrong_tree`. lax_011 keeps the photo. Reply queued.
- **Reports closed**: 1000028 (Husalle Lindens: the page is the whole avenue, and the reply says so), 1000035 (Chiang Mai: collected 2 km from our GPS-confirmed pin, no sighting on file; answered).
- **Still open, Isparta 1000042**: the drag comes from the tree's own finder, so it should be taken. But it lands on 144. Cadde in Sülübey (Nominatim), about 900 m from the city's only Çınar Sokak, and the name, slug, story, intro, question texts and FAQ all say Çınar Sokak. Needs a session to rename with a redirect, or the finder's word on which street.
- This run also judged the Valley Forge sycamore and the three holds, but the parallel run's commit got there first (entry below) and its version stands.
- preflight 0 problems.

## 2026-11-17 session: every feedback message gets a recorded verdict

- **Built** (Hidde: "Hou er ergens bij of feedback is behandeld of niet ... wat ik moet zien, zijn de dingen die openstaan"): scripts/feedback.py and data/feedback-ledger.json (id, status handled/needs_hidde/doubt, our one-line summary, never their words); the reader judge now handles new feedback too (brief "General feedback", the poll wakes on it, one-tap votes ignored), never sends a reply; the digest gets "Open for you" (`open_for_you_section()`): only what needs Hidde plus reports the judge left open.
- **Backlog walked**: 219 feedback rows, of which 109 open votes ("worth it", Hidde: nothing needed), 75 ours, the reports already in tree_reports. Six real messages: four handled (405 location row exists since 10-14; 702 and 756 answered 11-15; 1052 the Nationalerbe list, a lead list since 10-02), two for Hidde (786 an idea about UK heritage-tree initiatives; 849 a reply drafted in drafts/reply-reader-849-2026-11-17.md).
- **Cambridge plane**: the reader moved the pin twice to Emmanuel College; the plane stands in the Fellows' Garden, which the college calls private, so the hold stays `not_public` with the right reason, and the reader is asked whether visitors can see it (report 1000067, reply queued).
- **For Hidde:** two feedback rows wait for your call (786 idea, 849 reply draft); five reports the judge left open are listed under "Open for you".

## 2026-11-17 session: mailcheck no longer refuses the verb "walks"

- The Blaise reply to the reader who sent grid references (report 1000054) was held for "so the next person walks straight to them": mailcheck read the bare word as the walks feature. Hidde: "we mogen best walks zeggen wtf". The bare `walks` pattern is gone; "guided walks", "walking routes" and the like still count as the feature. Test: scripts/test_mailcheck_walks.py, on the escaped-bug row. The reply goes with the next knock.

## 2026-11-17 session: the Ochi chestnut forest (submission 936) judged

- Hidde asked what happened to an app submission about the Kastanologos chestnut forest on Mount Ochi, Evia (2026-11-16): nothing. Text only, no photograph, so no sighting row, and the reader judge never saw it.
- Verdict: the pinned trunk is held as `dead` (the reader's own words), filed in data/leads/_sightings.json and data/judgements.json. The living forest is a lead in data/leads/karystos.json (ochi.gr, Reforest'Action, Enel: ~60 ha, 200 to 450 years), waiting for one living trunk with a photo or GPS fix.
- Reply drafted, drafts/reply-reader-936-2026-11-17.md (mailcheck clean), asks for their favourite living chestnut there. For Hidde: goes as reply_text with outcome `holds` on his yes.
- Reply sent on Hidde's yes: queued as reply_text with outcome `open_question` on submission 936 (dry run passes mailcheck); the next knock's contributor_reply.py mails it.
- New rule (Hidde, same day): a standing dead tree still worth the detour ships with a photograph showing it standing and a page that says it is dead; never a stump or fallen trunk (CLAUDE.md "Selection", BRIEF_READER_JUDGE.md). The Ochi reply now asks only for a photo of their dead chestnut.
- Breakage: a tree submission without a photograph gets no verdict (937 Cape Town fig and 939 Tsitsikamma from the web form also sit unjudged). Recorded as an escaped bug (escaped.py), rung-2 work.

## 2026-11-17 session: Kamakura's two tabunoki untangled, Hasedera's is a new tree (kmk_007)

- Report 1000047 was right: the reader photograph put on kmk_003 (Goryo Shrine) on 11-16 shows a plaque reading 椨の木 and a sign reading 長谷寺, so it is the tabunoki at Hasedera. It is now kmk_007, "The Tabunoki of Hasedera", with that photograph and the reader's GPS fix as a confirmed pin, live as a reader's tree.
- kmk_003 is back on Goryo Shrine (the fix had moved it 182 m north), approximate again, photo missing.
- Kamakura intro and meta no longer say "the six" (the city has seven trees now). Report closed as changed with a reply. No local build: qa runs in CI.

## 2026-11-17 session: the Bristol FAQ no longer dates the Domesday Oak to 1086

- **What changed**: Bristol's FAQ context said the Tree Council believes the Domesday Oak was growing when the Domesday Book was made, beside its 700-year estimate. It now says the name comes from the estate's Domesday entry, not the tree's age, matching the story fixed on 11-16 (submission 935) and today's answer to report "something else" on the same point.

## 2026-11-17 reader judge: a sprawling Valley Forge sycamore goes live, three held, five reports closed

- **New tree**: valley-forge/vfg_001, The Sprawling Sycamore of Pawling Farm (Valley Forge National Historical Park, Pennsylvania). The reader's photograph shows pale, mottled limbs that lie along the lawn and climb back up; daylight, GPS fix. The pin follows the finder's own 56 m move onto the trunk (report 1000069, standard pin thanks). Their 650 cm, 260 to 285 years and 42 m spread stay theirs in the story. It is a new one-tree place with intro, question texts and three FAQ, and it is in data/us-states.json as Pennsylvania.
- **Held** (photographs viewed): Chêne de la Vierge, Meuse (`not_theirs`: a low-resolution autumn oak with a copyright mark, the look of a Street View crop; it goes live at their GPS fix once they confirm). A pruned street fig at night in North Melbourne (`not_special`): the app named it after our Curtain Square fig, which is 2.3 km away; report 1000070 got an answer. The photo sent for lon_021, the Finsbury Circus pagoda tree, shows a London plane, so it was rejected for that tree and judged on its own as `not_special` (one of many big City planes, no note).
- **Reports closed**: 1000069 (pin), 1000070, 1000050 (Stockholm: a maple-like tree about 1 km from the three offered; the lead now carries `wrong_tree`), and 1000034 (Dublin: already judged on 11-15 as a weeping conifer, not one of the five offered). Each has a short reply.
- **Still open (8)**, the same as the entry below says: 1000047 (Kamakura), 1000065/1000067 (Cambridge plane), 1000042 (Isparta), 1000032 (North Berwick), 1000061 (lax_011 twice), 1000028 (Copenhagen Husalle lindens), 1000035 (Chiang Mai). There was not enough time in this window.
- **Readers' words**: closed six that do not belong on a page (three pasted chatbot or website summaries for bbl_001, esl_001 and mrs_001; Coldwaltham's two thank-you notes; the Domesday Oak question, already answered). Six still wait to be quoted (fwd_001, glg_001, gnp_001, mvv_001, rsf_001, tar_001).
- preflight 0 problems, i18ncheck clean.

## 2026-11-17 session: the Arbour Oak gets its seasons row, its snow photo under winter

- Hidde asked why the Arbour Oak (nottingham/ntm_001) showed no season photos. Two causes: `Quercus x rosacea` was not in the deciduous list in site/src/lib/seasons.ts (so no row at all, on web and in the app feed), and the reader's photo had no month (a website tip, no date in the file). Fixed both: the hybrid oak is in the list, the photo has `taken_month` 1 with `taken_month_basis` (preflight's bookkeeping set names the field).
- New rule (Hidde: "als je sneeuw ziet mag die in winter hoor als je twijfelt"): an undated photo with snow or frost is winter, in CLAUDE.md "Photos" and BRIEF_READER_JUDGE.md "Putting it live". Older undated snow photos were not swept.

## 2026-11-17 reader judge: a hollow boab gives Kununurra its first tree, 29 reports closed

- **New tree**: kununurra/knx_001, The Hollow Boab of Rowing Club Road. A reader's photograph with a GPS fix: a tall boab on red ground with a doorway in its foot and a crown in fresh leaf. New one-tree place (Kununurra, WA) with its intro, question texts and three FAQ. The pin falls on open ground off Rowing Club Access Road (OpenStreetMap: a camp site), and the access line says we have not confirmed who manages it.
- **Photo**: der_001's reader photograph was already applied by the parallel reader-judge run (entry below); this run kept its version.
- **Pins moved on reports**, mailed the standard thanks: tro_007, mnc_002, crh_001 and rsf_001 were each dragged by the reader who found the tree, and their own GPS fix keeps them confirmed. Hand moves on approximate pins: dnk_010 (the finder's own move), nic_001, bil_002 and tok_009. bbl_001 moved 9.3 km east onto the Champion Lodgepole Trail on its finder's move; it was sitting by the lake, and is now approximate. Already moved by earlier sessions, now thanked: cor_004, hum_001, the two Colinton trees (edi_017, edi_021), the two Blaise grid references (bri_003, bri_017) and the Bilbao park pair (bil_003, bil_004). Each reader got one mail; their duplicate rows were closed without a second mail.
- **Answered (`holds`)**: the Domesday Oak's age (the name comes from Ashton Court's Domesday entry, and the tree is about 700); Android ("in the works, not out yet; the website works on any phone"); Coldwaltham's thank-you; three drags on pins confirmed by GPS (yor_003, bhm_002, and obc_001, which an earlier session had already declined to follow). Maria Aurora's 65 km drag got a reply asking for a photograph. The Melbourne "which tree" row closed, because its sighting went live today as mel_018.
- **Still open (10)**, needing more than this window had: 1000047 (Kamakura kmk_003: the reader says the tabunoki is in Hasedera, and our GPS-confirmed pin does sit at Hasedera, but the story says Goryo Shrine, so which tree is it?); 1000065/1000067 (the reader's held Cambridge plane, dragged 3.7 km into the centre near Emmanuel College; this may lift its not_public hold, but its photograph is not on this machine); 1000042 (Isparta isp_001, an 892 m drag on the street midpoint); 1000032 (a held North Berwick lead, waiting on Hidde); 1000061 (lax_011, "on the map twice"); 1000028, 1000034, 1000050 ("could not tell which tree" in Copenhagen, Dublin and Stockholm); 1000035 (Chiang Mai, collected 2.2 km off).
- **Readers' words**: reader_words.py lists 12. Several are pasted chatbot summaries (bbl_001, esl_001, mrs_001) and are left for a pass with time; none were quoted this run.

## 2026-11-17 session: a note's name no longer opens sign-in; readers' names on their photographs (web)

- **Fixed (found by Hidde, the Arbour Oak of Wollaton Park)**: a tap anywhere in a tree page's notes, a writer's name included, opened the sign-in sheet, signed in or not. The notes section carried its "Sign in first" text as `data-signin`, which signin-js reads as "this opens sign-in". Renamed to `data-signin-first`; qa `check_data_signin_only_on_controls()` keeps that attribute on links and buttons (ESC-2026-11-17, closed by that check).
- **Changed in the product (Hidde: "bij foto's wel namen gaan noemen ... Als die een account hebben, dan worden die accounts ook klikbaar")**: a note's writer with a public profile is now a link to their profile (signed out: sign in first, then it lands on the profile, the New from visitors way). A reader's photograph on a tree page names its sender under the photo ("Photo: <name>", linked) when their profile is public; private stays nameless. Terms and privacy rewritten to say so. Feed photos carry `by` (the photo's server id) for the app.
- **SQL live**: Hidde pasted supabase/reader-names.sql the same morning; checked on the Arbour Oak: notes and photo_authors answer, anon gets the name and no account id, the page shows "Photo: Katie Elizabeth". One name per person everywhere: the profile's display_name (Hidde: "maar 1 naam voor een gebruiker over het hele platform"). The management token in the env file is invalid, so sessions cannot run SQL themselves.
- **App**: the same in TreeDetail.swift follows in a worktree.

## 2026-11-17 reader judge: a reader's Boab Prison Tree photograph leads

- **Changed in the product**: a reader's photograph of `derby/der_001` Boab Prison Tree, the whole bottle trunk with its hollow entrance inside the post-and-rail ring, daylight, GPS at our pin, now leads that page (verdict `add`; the old lead moved into the gallery). Reader mail queued through `sightings_publish.py --send`.
- This run judged the Oak of Orkin photograph too; the parallel run's commit below got there first and its entry stands.
- **Left out**: the Boab reader also sent two extra frames (a wide shot with two people for scale, a trunk close-up). `sightings_publish.py` publishes only the main file, and it names every gallery file by the first 8 characters of the sighting id, so the extras would overwrite each other. They stay in out/sightings/, unpublished.
- **Not judged, on purpose**: the 37 waiting leads are all our own account (`mine`). No reader leads were waiting. The open tree reports (new in the brief while this ran) were not taken up.
- preflight 0 problems, i18ncheck clean.

## 2026-11-17 session: readers' reports on our trees are now picked up within 15 minutes

- **What changed**: a report on a tree we map (dead, wrong location, could not tell which tree, on the map twice, something else, a moved pin) now wakes the reader judge the way a reader's tree does. reader_poll.py counts new open rows in `tree_reports`; reader-judge.yml closes the small nudges and starts the judge when reports are open; BRIEF_READER_JUDGE.md "Reports on our trees" says what to do per reason. New commands in scripts/tree_reports.py: `--open`, `--count`, `--auto` (a moved pin on a confirmed pin under 30 m closes as `holds`, no mail), `--close <id> changed|holds|open_question ["reply"]`.
- **Why**: nothing closed these rows. 51 sat open since 11-15 (two Bristol grid references, the Domesday Oak's age, Kamakura's tabunoki in the wrong temple, Coldwaltham's thank-you, four "could not tell which tree").
- **Done by hand**: report 1000023 (Gomero de la Recoleta, bai_001) closed as `holds`: it was the app's "not sure which tree" on a photograph that already leads bai_001 since 11-15, and the tree already has its recognition line. 11 nudges closed by `--auto`. 39 remain for the judge.
- **Standard thank-you mails** (Hidde, same day: a moved pin earns "bedankt, het is live, bekijk het hier", "zelfde voor dood"): `tree_reports.py --thank pin|dead <report> <tree>` writes it as the reply and closes the report `changed`; contributor_reply.py mails it at the knock after mailcheck (both texts pass). The dead one carries no link. The judge run dispatched at 17-11 started on the brief from before this, so its replies are its own words.

## 2026-11-17 reader judge: the Oak of Orkin gets its first photograph

- **Changed in the product** (photograph viewed): a reader's sunlit photograph of the Oak of Orkin, Ultzama valley (`pamplona/pam_002`), the whole broad pollarded crown alone in its pasture behind a rail fence, GPS fix 29 m from our pin. The tree had no photograph; this one leads (verdict `approve`). Reader mail queued through `sightings_publish.py --send`.
- This run also judged the Stow yews and the totara sign the same way; a parallel run's commit below got there first and is kept as it stands. The Stow reader's two extra shots of the same door are not on the page (the publish script takes the main file only).
- preflight 0 problems, i18ncheck clean.

## 2026-11-17 reader judge: two readers' photographs on trees we map

- **Changed in the product**: a reader's wet-day photograph of both north door yews of St Edward's framing the arched door now leads `stow-on-the-wold/stw_001` (verdict `add`; the Geograph photograph moves into the strip), and its pin moved 101 m to the reader's GPS fix, now confirmed. The Tuatapere totara's own reader sent the trail sign beside the trunk ("Halls Totara, Podocarpus Hallii, Girth at chest height 8.31 m, Approximate age - 1000 years"); it sits in `tuatapere/tua_001`'s gallery behind the lead (verdict `strip`). The tree is now Hall's Tōtara (Podocarpus laetus, the sign's hallii), `girth_cm` 831 and its age rest on the sign, and the story, recognition line, intro and question context say so.
- **Not judged, on purpose**: the 37 leads with `status: "lead"` and no `hold` are all from our own account (code in data/our-accounts.json): 32 already flagged `mine` and 5 Nara photographs from 2026-09-07/08 without the flag (retired then for having no source). Our own photographs are never auto-published, so they are not readers' trees under the closed list. The intake still fetches the 5 Nara files each time because they lack `mine`.
- preflight 0 problems, i18ncheck clean. Reader mails went through `sightings_publish.py --send`.

## 2026-11-17 session: Plus answers on the digest page, two items on the backlog

- **Digest page**: every typed Plus answer now stands word for word under the Plus table (show_digest.py `plus_words()`, local page only).
- **Web error checked**: "Failed to initialize WebGL" is one browser on one page in 24 hours that cannot draw maps at all (old device, graphics off, or a headless browser); not a fault in our code, nothing changed.
- **For Hidde:** readers cannot find how to add a tree on the web, or a photo from a computer (three Plus answers say so); PRODUCT_TODO.md item 19, a design to show you first.
- **For Hidde:** the Major Oak as a monument is parked for your call: it died in 2026 (RSPB), so the dead-tree rule keeps it off; PRODUCT_TODO.md item 20.

## 2026-11-17 reader judge: the 22 older reader leads judged again, six live

- **Changed in the product, new trees live** (closed list, every photograph viewed in this run, each with the reader's GPS fix as a confirmed pin): an open-grown pedunculate oak by Jelašnica, east of Niš, Serbia (`jelasnica/jls_001`, reader: "300 years old ... state protection ... Photo by me"); a dawn redwood with a fluted, flaring trunk in Kew Gardens, Toronto (`toronto/tro_007`; Toronto's texts now count seven); a mossy temple ginkgo in Guankou, Dujiangyan, Sichuan (`dujiangyan/djy_001`, 1,300 years by the reader, a sign on its fence mentions the 1986 Journey to the West); a leaning, once-pollarded native black poplar beside Hancocks Lane, Castlemorton, under the Malverns (`castlemorton/ctm_001`, the app said "near Linton"); a hollow lime at Pabaži, Saulkrasti, Latvia (`saulkrasti/slk_001`; a famous-trees lead, "Catherine's lindens", sits 26 m off, so the story names that Commons label and asks); a great diamond-barked ash on the Żebra Żubra trail near Budy, Białowieża (`bialowieza/bwz_001`, species asked). Five are new one-tree places with intro, question texts and three FAQ; places named by reverse-geocoding the fixes (OpenStreetMap). Readers' girths and ages stay in the stories as theirs.
- **Held, each with a closed-list code**: Holborn plane sent as "dawn redwoods" (doubt_info, reply asks); Tassili cypress, no GPS and no place below the plateau (no_location, reply asks where: it goes live with that); Villa Smeraldi cypress, another photographer's signature on the picture (not_theirs, reply asks); a Swedish crown seen only from below (bad_frame); a mangrove stand (wrong_subject); and not_special for the Waitangi Norfolk pine, a young Melbourne jacaranda, a Chiang Mai roadside palm, four Nebraska and one Pennsylvania woodland trees, the Močile lime sign (166 cm), a Helmond plane avenue and a redwood trunk near Westonbirt.
- **Not touched**: 32 leads from Hidde's own and test accounts (Nara, Kyushu, Tokyo, Baarn, 2026-09-07 to 10-30) still sit as `lead`; they are ours, not readers', and most have no photo on the runner. They need his word or a session, not this run.
- sightings-processed, leads and judgements updated (`lead:` verdicts plus `sight:` publish rows). preflight 0 problems, i18ncheck clean.

## 2026-11-17 reader judge: Ladywell mulberry held (private garden), two self-matches closed

- **Held**: a black mulberry in the garden of Ladywell House, Lewisham (sighting 19c1b08d; both photographs viewed). The reader says the former vicarage was rebuilt in 1692, the tree is probably that old, a developer cut it hard in 2022 and it is regrowing in 2026. The photograph shows a hollow stump with fresh shoots on a private lawn, so it is held as `not_public` (same call as the Trumpington garden earlier today) unless the reader says it is seen from the street. Its story is good: if it can be seen from Ladywell Road, it ships.
- **Closed without change**: the photographs that lead the Erler Femeiche (rsf_001) and the Francistown monkey thorn (frt_001) came back into the queue as matches for themselves, because their processed rows still said `lead`. Now `published`, and the two judgement stubs the intake made for them carry verdicts.
- **Still left**: the 27 older reader leads from the entry below, unchanged. preflight 0 problems, i18ncheck clean.

## 2026-11-17 reader judge: two new trees, five photographs live, every queued photograph closed

- **New trees, live** (closed list, photographs viewed): the Erler Femeiche at Raesfeld-Erle, Germany (`raesfeld/rsf_001`; the app called it "near Winterswijk"). A reader's dusk photograph and GPS fix, backed by the DDG champion record (1245 cm, measured 2021, the reader's own figure) and German Wikipedia (Feme court until 1589, national heritage tree 2021). And a towering monkey thorn on a sandy riverbed 11 km north of Francistown, Botswana (`francistown/frt_001`; reader's photo and GPS, their 450 cm girth stays in the story; Africa is out of focus for our research only, never a reader's tree). Both are new one-tree places with intro, question texts and three FAQ.
- **Photographs on trees we map**: the Cosgrove House Banyan (kyw_004, no photo before; pin moved 57 m to the fix, now confirmed) and the Jindai-zakura at Hokuto (hok_001, no photo before) got their first photographs; the Balete Park fig (mra_001) got a wider, clearer reader photo as lead, the old narrow one moves to the strip; the Lewisham Elm (lon_045) got a close-up of its leaves and seeds in the strip. Three byte-identical resends (same md5) rejected as duplicates.
- **Closed without change**: eight queue entries were the photographs that already lead the trees they created earlier today (Cusop, Pasadena, two Tilarán, Lisbon ISA, two Melbourne, Plaza San Martín); the intake had re-queued them because their processed rows still said `lead`. Now `published`.
- **Fixed to pass preflight**: Hokuto's story had a colon reveal that only bit once the page gained a photograph; rewritten in one sentence.
- **Left for the next run**: 27 older reader leads (2026-09-07 to 11-16) still sit as `status: lead` with a written `why` but no closed-list `hold` code. Some read like `not_special` or `bad_frame`; a few (the Jelasnica oak 68515bbd, the Toronto dawn redwood fe8fc7e4, the Tassili cypress tip-947) may now qualify to go live under today's rule. They need a viewing pass, not a guess.

## 2026-11-17 session: readers' trees judged within minutes (reader judge)

- **Built** (Hidde: "should be instant honestly can it just trigger a flow??", then "Yes, build it"): `.github/workflows/reader-judge.yml` starts on a `reader-tree` repository_dispatch (or by hand), waits ten minutes so a burst becomes one run, reads the inbox, fetches every waiting photograph, and an Opus agent judges and publishes per the new BRIEF_READER_JUDGE.md (closed list from CLAUDE.md), then a deploy is dispatched. At most one run waits behind a running one.
- **Fixed for every run**: `scripts/fetch_waiting_photos.py` puts the photograph of every waiting reader lead on the runner; the night run calls it too, so "files not on this runner" cannot recur. 27 older leads have their photos fetched on the first run.
- **No setup needed** (Hidde: "do i have to do all this or can you do parts of it?"): the workflow also polls every 15 minutes with `scripts/reader_poll.py` (two id lists, no photographs, so almost no Supabase egress); only a sighting not yet in sightings-processed.json or a tree submission from the last 25 minutes starts the rest. A tree is judged roughly 15 to 45 minutes after it is sent, GitHub's cron allowing. The Supabase trigger (supabase/reader-judge-setup.md) stays as an optional faster path, his to paste if he wants it; a session cannot create the token or run SQL on production.

## 2026-11-17 session: 29 reader trees without a verdict, judged; a closed list for holding one

For Hidde: compliance review, 1 point(s) wait for your word (data/compliance.json).

- **Changed in the product:** eleven readers' trees are live, each photograph viewed in this session: the churchyard yew at Cusop by Hay-on-Wye (cus_001, new place), the Moreton Bay fig by the white mansion in Pasadena (lax_033), two giant figs near Tilarán, Costa Rica (tlr_001, tlr_002, new place; the reader calls them kapoks, the page asks), the Portuguese oak in the agronomy cloister, Lisbon (lis_039, pt overlay), two Royal Botanic Gardens trees in Melbourne (mel_017 water gum, mel_018 leaning fig), the Gomero of Plaza San Martín, Buenos Aires (bai_005, on the city's notable-tree list), the Parco Massari oak, Ferrara (fer_006), the Balmerino Abbey chestnut, Fife (blm_001, new place, 400 to 450 years by the Gazetteer), and the white poplar of the Oasi Lagoverde, Bologna (bol_014, it overlay). Counts in the Melbourne, Buenos Aires, Bologna, Ferrara and Lisbon texts follow. Readers' girths stay in the stories, never in `girth_cm`.
- **Held, each with a reason from the list:** an LA street magnolia, an ISA jacaranda and Judas tree (not_special); a far-off Copenhagen field oak and a Chiang Mai sunset silhouette (bad_frame); a Sydney kauri that could be either of the garden's two big kauris (wrong_tree: ask the reader); a Cambridge plane in a private garden on Trumpington High Street and the Griffin wedding-venue pecan (not_public). The other ten of the 29 were already live; their verdicts were never written.
- **Why they waited:** the night runs cannot see a reader's photograph that an earlier runner downloaded (out/ is gone on the next machine), and the 11-17 viewing notes kept good trees back for "needs the site named" and "no girth", two of them describing the wrong photograph (the Chiang Mai and Costa Rica notes were swapped).
- **Rule (Hidde, 2026-11-17):** "we need either a gps or photo and it needs to be somewhat special"; "only other reasons if we really doubt the location or photo or info to be incorrect or in appropriate photo". A held reader lead names one of the closed reasons in `hold`; preflight's `check_a_reader_lead_names_a_closed_reason()` fails a push otherwise (leads seen from 2026-11-17). CLAUDE.md "Verify".
- **Not done:** about 20 older reader leads from 11-15/16 (preflight's NOTE list) still sit as leads under the old reasons. The instant judging flow is proposed, not built.

## 2026-11-17 write pass: ten held trees written into the app

- **Changed in the product:** ten new trees, all app-only under APP FIRST (no web page, pace not counted): the Lehigh Parkway cottonwood (all_001, new place Allentown, PA), the Gornelle and Tre Aie beeches (asp_001, asp_002, new place Aspromonte), the Acerone of the Madonie (cbu_001, new place Castelbuono; species set to canonical Sycamore), the Meavy Oak (dmr_002, Dartmoor), the Zurraque holm oak (sgz_005, Grazalema), the San Nicola ombu (tmt_001, new place Isole Tremiti), the Santa Lucia di Mendola holm oak (not_003, Noto), and the Monte Pecoraro and Rosarella silver firs (ssb_002, ssb_003, Serra San Bruno). Their earlier holds were judgements (register point only, thin life evidence, which trunk in a wood), which CLAUDE.md says never block; each story states its gap plainly and asks the reader, and each has a recognition line. Meavy Oak: no news of a fall found, the 2019 decline report and the last Geograph photo (2015) are on the page. Merged with scripts/build_write_2026_11_17.py; allentown added to data/us-states.json. preflight 0 problems.
- **Still held (hard rules, not judgement):** det_001 and det_002 Elmwood Cemetery (no coordinate at all, a pin is needed before either can ship, though both stories are written), brd_001 Brindisi hospital courtyard, frk_027 Frankfurt schoolyard mulberry (pin is in the schoolyard, not at a viewing place), inn_007 Innsbruck lime (pin on a private plot), not_002 Cava Candelaro carob (land tenure unknown): hard rule 10. sfo_012 is live sfo_004 (fold its DataSF pin and girth in by enrichment).

## 2026-11-17 06:37 night run: queue tidy, two Miami trees (rungs 1, 2, 5)

- **Changed in the product:** two new Miami trees (the Pinecrest Gardens banyan, Vizcaya's pigeon-plum champion). The Miami intro no longer says "Only Vizcaya charges admission", which was false.
- **Readers:** the 8 photographs in the queue were already live as the lead photos of the trees they created, so they were marked processed and the queue emptied. The Takayama ginkgo (tky_001) had a photograph but no written verdict, which made preflight fail; the verdict is written (looked at the pixels: trunk, crown, the temple's sign, daylight).
- **Not done:** about 40 stranger photographs with a GPS fix are still leads that preflight says to look at and publish; their files are not on this runner (no service key), so I did not judge them blind. Needs a session with the key.
- **Writer pile:** `passcheck.py --pending` listed 15 candidates; the write pass merged 2. The rest are held with reasons (no coordinate, private yard, declining tree, schoolyard, duplicate of sfo_004: its pin and girth belong in an enrichment pass). The "390 awaiting a writer" line in prepare.py is mostly stale research files for trees already live.
- **Health:** iOS app failure 6h ago, a new run (after the MainActor fix) was still building. Web error "Failed to initialize WebGL" is a headless browser, not a page fault. 6 of 12 knocks delivered.
- **Page gaps:** country intros for Thailand and Philippines written from their own trees (93fd475ea).
- **Why it stopped:** every top-queue US/UK/DE city is on the 48-hour wall, Stuttgart has no register supply, `recognise.py --stuck` is empty, translations are paused. Nothing refused; no tool call was denied.
- **For Hidde:** Miami is now 47% behind paid entry; it needs free trees.

## 2026-11-17 session: three readers' tree notes worked into the stories

- **Queue**: Birmingham, Sheffield and Leeds lead `city_queue.py --next` (PHONES_FIRST, Hidde: "Ja, vooraan"), from-zero research on, ten trees each. Why: since the Guardian piece app phones opened there (GeoIP: 30, 28, 25) with 1 or 2 of our trees within 25 km. The same look showed browsing depth does not follow coverage (about 2 trees opened per phone with 0 or 20+ trees near), so the shallow browsing is the app's first screen, not the map's gaps.
- **iOS scheduled run**: the three red runs were the two iOS 18 deinit crashes (fixed 11-16 and in 66d624e1b this morning, after the night run) and, at 14:13 UTC, no Mac runner from GitHub. Failed job rerun to prove it green.

- **Product**: Deusto bald cypress (bil_002): a reader measured the trunk at no more than 2 m across, perhaps 2.3 at the base. The story now says so beside the website's 3 m. `girth_cm` 942 is gone: we had worked it out from that one website's diameter, and a girth may only come from a register or a plaque. Gülhane hackberry (ist_013): the register's own figures disagree (145 cm across but 411 round, which is about 131 across). The story says so and adds the reader's doubt; the girth stays the register's. Molinazzo oak (pgr_001): the reader's monitoring details (stability scans, dead-wood pruning, root zone) and Molinazzo's history as a hamlet with a lost oratory, stated as theirs.
- **Rule** (Hidde, "mensen kiezen hier zelf voor"): a note signed with its writer's own name stays; the closed list means another person's name (CLAUDE.md rung 1, tree_notes.py).
- **Mail**: Joey R. (Willistown ambassador) got the link to his profile with the badge, sent in his thread on Hidde's "Verstuur" (drafts/batches/reply-joey-willistown-2026-11-17.json).
- **Numbers**: the digest's Android waitlist row stopped at 1,000, because Supabase returns 1,000 rows at most. Fixed (de084f6d1): every digest count now pages through all rows and all accounts; the waitlist row reads 1,317 / 416 / 58 for 11-15 to 11-17.
- **Mexico City, San Fernando ahuehuete (mex_006)**: a reader's note says it died in 1969. That is El Sargento in Chapultepec (their held photos carry GPS 3.9 km away). The story says so in English and Spanish; the tree is alive in the 2025 register.

## 2026-11-17 06:11 night run: reader photographs (rung 1)

- **Photographs judged**: 15 queued app photographs looked at. Three became lead photographs for Hobart trees that had none (Norfolk Island pine, Bhutan cypress, dawn redwoods); nine went into the strips of Thomasville, Sydney, San Diego, Charleston, Buenos Aires, Tuatapere and Orroroo trees; three of a dead trunk tagged to the Mexico City Ahuehuete were held (GPS 3.9 km from our tree, a dead snag, not the living broad crown we describe). The Thomasville pin moved 18 m to the reader's fix.
- **Seven new trees from readers' photographs with GPS fixes**, each with its photograph as lead: Te Waha o Rerekohu, the pohutukawa at Te Araroa (NZ); the Gennett Poplar in Georgia; the Knightwood Oak and the Tall Trees sequoias in the New Forest; a cedar on the Meares Island Big Tree Trail (BC); the old lime of Estavayer-le-Lac (CH); the Overbury Drive red gum in Adelaide. Sources are named in each tree's verify_notes. Five new place files, so the places carry no translations yet.
- **Held**: the Meadowlark 1939 pecan (Griffin, GA) stays a lead: a wedding venue, no public access shown, one source (the venue). The Llanfihangel-nant-Melan yew and the Balmerino chestnut (both UK, found by readers) stay leads: their photographs are not on this runner and a verdict needs a look.
- Stories: three Hobart stories lost colon reveals when their photographs made them indexable. 21 tree notes read, none hidden.
- **Verify passes, both dead ends**: Zurich (27 register rows, no size, age or access evidence, all rejected as leads) and Miami (two paid-entry trees delivered to data/research/miami-verified.json and left unwritten, since Miami is already 46% behind a ticket). Both are walls for 48 h.
- Health: iOS CI red 6 h ago (a session fixed the iOS 18 fault this morning, awaiting the next run); web error "Failed to initialize WebGL" is a browser without WebGL, not ours to fix.

## 2026-11-17 session: Android looks like Android

- On Hidde's word ("if you are sure about 1-6 than fix them all") the remaining iPhone forms on Android took Android's: short sheets dock to the bottom edge (full width, top corners rounded, handle, no X, closed by swipe or back); forms have an X left, the title left and Save right; pushed pages put the title left beside the back arrow; list rows lost their chevrons and section headers their capitals; form fields are outlined. Sign-in shows Google first on Android (Apple stays, second, for accounts made on an iPhone). A sharp adaptive icon and splash replaced the blown-up 192 px PNG; that change crashed the camera's sign-in sheet for an hour on his phone (fixed, escaped bug recorded, FlowWalk.collectGate catches it). FlowWalk 24 of 24 on the emulator. All in PR 64.

## 2026-11-17 session: Android gets Android's tab bar

- Hidde on his Samsung: the floating capsule "voelt als iOS specifiek". Looked at AllTrails and Polarsteps on his phone: both dock a white bar to the bottom edge, 56 high, a word under every item, the chosen one coloured with a filled icon, no pill. On his word ("volg maar gewoon polarsteps en alltrails") Android's bar is now that: Map, Discover, My trees and the camera with "Collect" (eight languages). The iPhone keeps its capsule. Parity list and CONVENTIONS.md "A tab bar on Android" carry the why.

## 2026-11-17 session: Android on Hidde's Samsung, the list follows the finger

- The Android app is on Hidde's Galaxy S21 Ultra (Android 14), the signed release build.
- He found at once that the map's list did not scroll up: dragging the list up from half moved the sheet DOWN (the scroll connection passed the drag with its sign turned round), and the sheet's gesture handlers kept the first composition's stops and lock. Fixed in MapSheet.kt; checked on the emulator from peek to half to page, the list scrolling at the page and handing back to the sheet at its top. New FlowWalk test `theListFollowsTheFinger`, passing.
- My trees: the gear stood flush against Android's thin status bar and read too high next to the iPhone; it has the full sheets' 10 of air now.
- Open: Hidde saw "rare dingen" with the locate arrow on his phone (the list going down, the map not minding the sheet). On the emulator the sheet stayed and the dot came to the middle above the sheet; a second press zooms to street level. Waiting for his description or a screen recording.

## 2026-11-17 session: iOS 18 crash when the map redraws, fixed

- The nightly iOS 18 test run was red: not the photo test it named, but the map's TreesMemo dying through Swift's MainActor deinit hop, which aborts on iOS 18 (the same fault as the sheet's drag clock the day before). Every class @State builds inline (ten of them) now dies with `nonisolated deinit {}`. All 231 unit tests green on an iOS 18.6 simulator.
- New ratchet check in qa.py, `check_a_state_class_dies_without_an_actor_hop()`, so an eleventh one cannot slip in.
- For Hidde: build 42 carries this fault for iPhones still on iOS 18; the next build carries the fix.

## 2026-11-17 night run (window from 23:57 UTC)

- **Rung 1, reader photographs: all 36 matched ones looked at and applied** (sightings_publish.py, judgement.py verdicts written, preflight 0 problems, commit 503bfc04a). 12 became a tree's first photograph (Ada Tree, Humboldt Giant Tree, nyc_024 ginkgo, Huntington cypress and kauri, Blaise Castle cedar, Cascais fig, two Setubal peppers, Wishing Tree, Roath Park oak, Goo Shrine ginkgo); 19 added to the strips of trees that had a lead; 5 held (duplicate frames, one sign-only shot, one picture sent for two trees 380 m apart). Pins moved to the reader's fix on csc_001, syd_006, crd_012, bmr_001.
- **Three colon reveals reworded** (nyc_024, pwt_001, stb_010): they became indexable with their new reader photographs and preflight refused them.
- **19 photographs of trees we do not map: looked at, each with a `why` in data/leads/_sightings.json.** None published yet: they need the site named or a source (60878254 River Red Gum has a sign giving 10.89 m girth and 500+ years, 471cdeb1 yew near Llanfihangel-nant-Melan, tip-993 Balmerino chestnut and b451d1e8 Buenos Aires fig are the strongest). For Hidde: nothing.
- **New tree from a reader's photograph: orroroo/orr_001, The Orroroo Giant Gum** (South Australia, river red gum). The council's sign in the reader's photo gives 10.89 m and over 500 years; search results add an older sign (about 10.4 m) and the Big Trees register (9.90 m, 485 years), stated on the page. GPS fix at the tree, reader's photo is the lead. One tree, so no place page. Open: Wikipedia has no Orroroo article within 40 km, so city_names.py leaves it unresolved.
- Closed the open escaped bug (reader tree links its sighting) with its fix commit; the iOS failure at 19:45 was GitHub not acquiring a macOS runner, not code.
- Not done: the REFILL THE SHELF verify pass and the other ladder rungs; this window went to rung 1.

## 2026-11-16 daily publish

- **Daily publish: queue empty.** Today's builders (build_write_2026_11_16, 16b: phl_010 Grumblethorpe Ginkgo, lpz_032 Papiermuehlstrasse horse chestnut, gui_010 Casa de Margaride camellia) are already on main; Allentown all_001 stays held for a life check, not the pace. Nothing published, pace untouched, preflight 0 problems. For Hidde: the daily task "publish-held-trees-daily" can be switched off under Scheduled; write passes put trees straight into the app, so nothing waits for it.

## 2026-11-16 session: the old yew of Vigeois live; two readers asked back

- **New tree, Vigeois (Corrèze)**: vgs_001 The Old Yew of Vigeois (https://ancienttrees.app/vigeois/old-yew-of-vigeois), from a reader's website tip (tip-959, '1 Rue Du Vieil If'). Ancient Yew Group tree 5617: 915 cm, access public, by the school playground; its coordinate is the pin (approximate). No photograph: theirs carries the signature 'krapo arboricole'. One tree, so no place page.
- **Replies sent** (Hidde's yes on the text, contributor_reply.py): tip 959 got the link plus "is that you? may we put it on the tree's page?"; tip 947 (Tassili cypress, no place) got "where exactly does it stand, or the original photo from your phone". Their answers come to info@.

## 2026-11-16 session: Nathalie (Auckland ambassador) answered

- **Mail**: Hidde's own reply sent in her thread on his "Verstuur" (drafts/batches/reply-nathalie-2026-11-16.json): she asked how to send trees from around the world; the app is easiest (iOS live, Android being built), otherwise email; suggestions on features and trees welcome. She has trees on file for the coming week: each one that comes is a tree to finish.
- **Voice**: my first draft thanked her for the app photo she had sent the day before; he: "ze stuurt toch helemaal geen foto mee?". Recorded in HIS_VOICE.md (answer the mail in front of you).

## 2026-11-16 session: Cathedral Grove's Big Tree, from a reader's mail

- **Product**: the Big Tree of Cathedral Grove (cgv_001, MacMillan Provincial Park, Vancouver Island) is live as a lone tree page: a Coast Douglas-fir over 9 m round and about 76 m tall, 800+ years by BC Parks and the park sign. Sources BC Parks, Wikipedia, the HMDB marker; pin confirmed from the OSM tree node and komoot's highlight (within 15 m, south of Highway 4). A reader's tip by mail (`found_by_reader.tip`), so it gets its page under APP FIRST. No place page (one tree).
- **Photo**: none shown. Gillian's "Biggest Tree" names this trunk but scores POOR (blown sky); Aaron Carlson's grove shot is in good light but geotagged 1.6 km off, so `held`. A photo of this trunk is still wanted.
- **Mail**: the reply to the reader (drafts/reply-jonathan-king-2026-11-16.md), saying it is on the map with the link, was sent in his thread on Hidde's "Verstuur", after the page loaded. His words are not quoted: a mail needs their yes first.

## 2026-11-16 session: Joey is ambassador for Willistown

- **Product**: Joey R. (Crum Creek sycamore, wtn_001) is ambassador for Willistown instead of Media, at his own ask ("just Willistown, where I live"); `ambassador.py --grant` willistown and `--revoke` media-pennsylvania, synced.
- **Mail**: reply sent in his thread on Hidde's "Verstuur" (drafts/batches/reply-joey-willistown-2026-11-16b.json): yes to Willistown, and his two photos (a sycamore of 260 to 285 years with a 147 ft spread, and an oak) arrived without attachments, so he is asked to resend or add both in the app. When they come: new Willistown trees, his description quoted once the sycamore has a page.
- **Broke**: Gmail refused IMAP ("too many simultaneous connections") because 13 `sent_drafts.py --quiet` processes from session starts had hung for up to 40 minutes; killed them. Fixed: sent_drafts.py fetches all Sent headers in one IMAP request instead of one per message (2m13s to 16s) and stops reading Sent after 90 seconds, so overlapping session starts no longer pile up connections.

## 2026-11-16 session: the Guardian on the about page

- **Product**: /about shows "Featured in" with the Guardian and Wilder logos under the photo, each linking to its article (Guardian 2026-11-15, Wilder 2026-10-23); the "was in Wilder in October 2026" line under the signature is gone. Reference Polarsteps' featured-in strip; under the photo because a block under the title broke the letter (Hidde: "het loopt gewoon niet zo"). On a phone it sits between photo and title, 48px above it. Logos in site/public/press/ (Guardian wordmark SVG; Wilder's own full logo, unchanged, trimmed to its ink at 3x).
- **Broke and fixed**: the photo's img rule also styled the logos (300px tall) for one deploy; scoped to `.about-photo > img`. On an 800px laptop the logos sat below the fold under the sticky photo, so the photo column now narrows on low screens (3:4 kept, uncropped).
- Hidde chose names without months ("dan blijft het actueel"); recorded in drafts/PITCH_VOICE.md.

## 2026-11-16 session: the 18 reader trees without a verdict, judged

- **New tree, Essaouira**: ess_001 The Ombu of the Essaouira Medina, a reader's app photo plus GPS fix of the ombu in a café courtyard ("Oldest tree in Morocco inside the ombu cafe", quoted); age 250 and girth 10 m stated as theirs. One tree, so a tree page and no place page.
- **New tree, Verona (day trip)**: ver_009 The Holm Oak of San Bonifacio Station, from a reader's website tip; their picture was a Google Street View capture (not used), the MASAF register (01/H783/VR/05, 263 cm, 9 m) matches their 265 cm. No photograph, recognition line, approximate register pin. Intro, FAQ and the it overlay (title now 9) updated.
- **Kvam kvm_001 enriched**: the reader's website tip (tip-951) is the same oak and photo as their app sighting live this morning; it adds the name Den freda eika, girth 706 cm and the 1950s protection, quoted as theirs.
- **Verdicts written** for the other 15: 7 trees already live (La Tène x4, Elleholm, Maidstone, Colchester) got their publish verdict; leads: Jelasnica oak (200 cm by the reader's tape), Helmond plane avenue, Tassili cypress (no place), Vigeois yew (another photographer's watermark; worth a verify pass), Westonbirt conifer trunk, Toronto dawn redwood; holds: "Prince Eugen's Oak" (the photo shows a maple), Madeira Witch Tree (as 11-15).
- **For Hidde**: preflight's note says a stranger's photo plus GPS is held back only for wrong tree, subject or frame; the leads above (and about 15 like them from 11-15/16) were kept back for lack of size or age, as earlier runs did. Your call whether those go live anyway.

## 2026-11-16 session: Ricard Llerins Bonet's first Barcelona tree is live

- **New tree, Barcelona**: bcn_062 The Plane of Carrer de Cantabria (https://ancienttrees.app/barcelona/plane-of-carrer-de-cantabria), a hollow London plane of about 1917, Tree of Local Interest since 1997 (register 99400454963). Ricard (book author, answered our archive ask of 10-25 from his spam on 11-15) mailed four photos, one tree per mail he says; his 2015 summer photo leads, the 2014 hollow trunk in the strip, credited, `permission` with his words. Found by reader (mail), so it has a web page under APP FIRST; es overlay added (count 57 to 58).
- **For Hidde**: the reply drafts/reply-ricard-llerins-2026-11-16.md (Catalan, no ask: he promised current photos and more trees). Next mails from him: one tree each, same route.

## 2026-11-16 session: Supabase egress after the Guardian weekend

- Usage page (Hidde's paste): 7.48 GB of 5 this cycle (28 Oct to 28 Nov); grace until 2026-12-13, restriction only if the next cycle (from 28 Nov) also passes 5 GB, so about 165 MB a day. The 11-13 fix held (database egress fell to about 50 MB a day on 11-14); 11-15 was about 850 MB and 11-16 about 450, almost all storage.
- The gateway logs (a 7-day read-only token Hidde made; logs keep one day on the free plan) say who: of 979 MB of storage reads in 24 h, about 935 MB were our own scripts (Python), 30 MB visitors' browsers and the apps. The Mac (one session at 05:00 UTC: 344 reader photographs, 310 MB, in a fresh worktree whose out/ was empty) and the night runs during the weekend's inbox (100 to 200 MB a knock while the queue was long; 2 photographs at the 14:31 knock). shared_thumbs is fine (it makes only the new ones).
- Fixed: `sightings_inbox.fetch_photo` (used by the inbox, reader_photos and inspect_readers) reads and fills the MAIN checkout's out/sightings when it runs in a worktree, so a photograph is downloaded once per Mac. Not done: an Actions cache for the runners' photos (the repo is public and private reader photos would sit in a cache other workflows can read).
- Check: the usage page around 2026-11-20; under 165 MB a day is the aim. Delete the logs token when done.

## 2026-11-16 session: iOS CI green again

- The red ios.yml runs of today were the sheet's drag clock aborting the app process (fixed in BottomSheet.swift at 15:54 by another session), which took down a different unit test each time (last: PhotoMemoryTests.testNotAPictureGivesNothing, which passes on its own). The runs after the fix were cancelled or never got a GitHub Mac runner; run 43904601383, re-run once for runner capacity, is green: 277 passed, 0 failed. No code change needed.

## 2026-11-16 session: a tap on somebody's profile picture shows it full screen

- **What changed**: on a public profile (web /profile, iPhone, Android) a tap on the person's picture opens it full screen on black in the photo viewer tree photographs already use: the whole picture, X or swipe down to close (Escape and a click beside it on the web, system back on Android), pinch to zoom in the apps, no credit line. A letter avatar is not a button and opens nothing. Your own picture on My trees is unchanged. Benchmarked first (WhatsApp, Facebook, X, LinkedIn, Instagram, Strava) into CONVENTIONS.md "Tapping somebody's profile picture to see it bigger"; Hidde picked the whole-photo form over X's circle ("Yes, build it").
- **Checked**: iPhone 17 simulator and Android emulator, tap opens, swipe down / back closes, same frame on both; web tested from the page's own code at 375 and desktop (opens, Escape, X, click beside it; the letter stays a span). No local Astro build on this Mac, so the deployed page is CI's to build. qa --source-only and preflight pass.
- **New words**: none on the web (the existing photoOpen label); Android gets photo_open in all eight languages. The demo person (-people-demo) now has a picture so sweeps reach the viewer.
- **For Hidde: next iOS build carries it.** No difference between iPhone and Android, so nothing in data/android-parity.json.
## 2026-11-16 session: an app crash in the sheet, readers' notes acted on, Nick asked to be Bristol's ambassador

- **App crash fixed (next build)**: ios.yml went red twice today with a different unit test "crashed with signal abrt" each time. The crash report in the result bundle (AncientTrees-2026-11-16-152543.ips) shows the app itself aborting: "pointer being freed was not allocated" in Swift's back-deployed deinit-on-executor hop, under `SheetDragClock`'s deinit (BottomSheet.swift). Under default MainActor isolation the class's deinit hopped to the main actor, and @State throws a new clock away on nearly every sheet redraw. Now `nonisolated` (08f53480a). Could also hit people in the store build; whether it explains the 1.5% quick reopens shows once PostHog's crash capture ships in the same build. No unit test reproduces it on demand (a runtime race on dealloc); ios.yml is the check.
- **Readers' notes acted on**: a Bristol reader's two tree notes moved the Blaise Meadow Sweet Chestnut and the Blaise cedar about 1 km east to the Bristol Tree Forum's grid references (confirmed). The Tree of Life (Olympic): a reader says it is gone; nothing after July 2025 confirms it, so the story's unsourced "2026 still there" became the January 2025 slump plus the reader's report, unconfirmed; retire on a second account or a photo.
- **Nick (Bristol)**: Hidde's own reply sent (thanks for the pins and his photos of four Bristol trees, "are they correct now?", would he be the Bristol ambassador), recorded in ambassadors.json `invited` so the automatic invitation skips him. His rewrite is in HIS_VOICE.md.

## 2026-11-16 session: reports and moved pins get their own table (step 2 of splitting submissions)

- **What changes** (Hidde: the catch-all `submissions` is "een troep", step 2 "later als het rustiger is"): supabase/tree-reports.sql makes `tree_reports` (the name `reports` is taken by reports about a person). One row per report: tree, reason (the chip, or pin moved, collected far, merged, typed correction), the person's follow-up words filled IN PLACE instead of a second "report detail" row, the coordinate of a moved pin, and the verdict and reply fields (outcome, reply_text, replied_at, thanked_at). Own-rows RLS (a reader may only insert a bare report, never a verdict), cascade on account deletion, GRANT in the file, ids from 1,000,001 so they never equal a submissions id. A trigger on `submissions` moves every report, follow-up and correction posted there (every build out today, and the website, posts there) across and drops it from submissions with a 201 to the sender. The 68 existing rows are copied with their verdicts and replies (only accounts that still exist; 3 rows without an account stay readable in submissions); nothing deleted. Trees sent, ambassador requests and general feedback stay in submissions.
- **Reading**: website (worthit-js.ts), iPhone (`MyVotes.standingReports`) and Android (`MyVotes.standingReports`) read your reports from `tree_reports`, the old reading as fallback until the paste; the apps carry it in their next build. Senders are unchanged (the trigger routes them). Scripts read both tables through scripts/tree_reports.py (submissions row shape, each report once, PATCH back to the table it came from): contributor_reply.py, inbox.py, show_digest.py readers in full, daily_digest.py (every feedback count), reader_words.py, and claude_gate.py, so a report still wakes the knock. qa `check_reports_are_read_from_their_own_table()`. privacy-map maps the file to "Suggestions, corrections and votes".
- **Live in Supabase** (Hidde pasted it the same evening). Checked: of 68 report rows in submissions, 56 copied and the 8 follow-ups folded into their report (so 56 rows in tree_reports, 43 with a pin coordinate), verdicts and replies carried with no row losing one; 3 rows without an account stay in submissions, 1 of a deleted account was not copied. Round trip on the test account: a report posted to submissions gets 201 and lands in tree_reports with no submissions row, its follow-up fills the same row, a pin move lands with its coordinate; the account reads its own reports back, sees nobody else's, and is refused (403) when it tries to write a verdict. Test rows deleted.

## 2026-11-16 session: the Nhan Dan banyan in Hanoi is live (a reader's tip)

- New tree hni_003, the banyan of Nhan Dan at 71 Hang Trong, Hanoi (Hidde: "Yes, put it live"). It was blocked as a lead: it stands in a newspaper's courtyard. The reader who tipped it (submission 700) answered our question by mail: "visible from the sidewalk", which meets hard rule 10 under the El Pino ruling. Age over 300 years (Nhan Dan 2022 and 2026, VietnamPlus 2026), over 400 by the reader's estimate. No photo, so it carries a recognition line; species asked on the page (Ficus sp.). Approximate pin on the Le Thai To pavement. `found_by_reader.tip`, so it gets a web page under APP FIRST. Hanoi intro and meta grew with it; the lead left data/leads/hanoi.json.
- Submission 700 set to `changed`. The reply with the link is in drafts/reply-reader-700-2026-11-16.md (mailcheck clean), sent the same afternoon by contributor_reply.py (Hidde: "Yes, send it").

## 2026-11-16 session: website-added trees now say "Approved" on the reader's My trees

- Hidde saw the Arbour Oak congratulation bounce. Cause: the reader signed in with Google on the address of Natural Athlete Magazine, a domain dead since about 2019 and unregistered today; Google still calls it verified, so login works and mail cannot arrive. Nothing wrong on our side.
- Found on the way: every tree a reader added through the website form kept reading "Sent" on their My trees after going live, because tree_approved.py never set the submissions row. The app was fine (all 60 sighting rows read published).
- Fix: `mark_tip_published()` in tree_approved.py sets outcome changed, a one-line reply_text with the link (the card prints it) and replied_at (so contributor_reply.py sends no second mail), mail or no mail. Backfilled all 12 live website trees. qa `check_a_website_tree_says_approved_on_my_trees()`; escaped bug recorded with that test.

## 2026-11-16 session: worth-it votes get their own table (step 1 of splitting submissions)

- **What changes** (Hidde: votes and tree submissions are "hele andere dingen", then "prima start maar"): supabase/tree-votes.sql makes `tree_votes`, one row per person per tree, deleted when taken back, own-rows RLS, cascade on account deletion, GRANT in the file. A trigger on `submissions` catches every vote posted there (every build out today posts there) and applies it to `tree_votes` instead, so no old app breaks and `submissions` keeps only what people write. The standing votes are copied across; old rows stay (nothing deleted). `tree_vote_counts()` now counts from `tree_votes`, same name, so the thumbs' numbers need no client change.
- **Reading**: website (worthit-js.ts), iPhone (`MyVotes.standingVotes`) and Android (`MyVotes.standingVotes`) read your own vote from `tree_votes`, falling back to the old reading while the table is missing; the apps carry it in their next build. tree_saves.py and the digest's vote rows (`vote_rows()`) read `tree_votes` the same way. privacy-map maps the file to the existing "Suggestions, corrections and votes" sentence. vote-counts.sql carries a do-not-paste-again note.
- **Step 2, later**: reports, report details and moved pins to their own table (they need a verdict and a reply, so they move together, not with the votes).
- **Live in Supabase** (Hidde pasted it the same afternoon; the first paste stopped on a deleted account's votes and rolled back whole, fixed in ac85b7961). Checked: 109 standing votes copied, strangers' 95 up on 91 trees exactly as before; the 4 not copied belong to deleted accounts. Round trip on the test account: a vote posted to submissions lands in tree_votes and leaves no submissions row (201 to the sender); the undo deletes it.

## 2026-11-16 session: Ross's facts on the Wheatley Elm of Balgreen

The reader who added the Edinburgh Wheatley elm (edi_022) answered the congratulation mail: about 150 years old, likely Britain's second widest Wheatley elm, verified by Owen Johnson, one of six on the avenue. All on the page as his account (age as a reader's estimate, recognition line says the pin marks this one of six). Reply sent in his thread on Hidde's "Verstuur".

Bug found by Hidde on Damien's profile: a reader's tree published without their photograph (his Glynburn Road gum, an archive print we did not use) never got its sighting linked, so the profile showed it twice and without Approved. sightings_link.py now links found_by_reader sightings too; ads_002 and hum_001 linked; qa check_a_readers_tree_links_its_sighting.

## 2026-11-16 session: worth-it votes counted apart from trees and photos

- **Rule** (Hidde: "kun je vanaf nu nooit meer worth it stemmen en boominzendingen onder 1 kap gooien dit zijn hele andere dingen"): `daily_digest.is_vote()` decides what a vote is. The headline's "Readers' contributions" now counts trees, photos, corrections and ambassador asks only, with a new "Worth-it votes" row beside it; the day table's Feedback row leaves votes out and they get their own row. qa `check_votes_never_count_as_contributions()` (green as built, red with the old lumped label put back).
- **Open**: whether votes move out of the `submissions` table into a table of their own is Hidde's call (asked).

## 2026-11-16 night run (window from 14:32 UTC)

- **Rung 1, reader photographs (5 on mapped trees, 2 on unmapped ones), all looked at.** Two trees got their first photograph: the Centenary palms of Parque de la Misericordia in Bilbao (pin also moved 139 m to the reader's GPS fix, now confirmed) and the Huff Creek Road White Pine in Nicolet National Forest. Three planes (Jardines de Albia, Brunswick Square, Lietzensee) were already in the strip; the Albia pin moved 46 m to the fix, confirmed. The two unmapped ones stay leads with a written verdict: the Westonbirt-labelled redwood (pin is south of Wotton-under-Edge, species and size unconfirmed) and the San Bonifacio holm oak (looks like a Street View screenshot, no GPS). The five verdicts had to be written by hand into the judgement file because `judgement.py --scan` reads only the queue and publishing had already emptied it.

## 2026-11-16 session: "New from visitors" in the apps shows only tiles with the visitor's photograph

Hidde: in the iOS app the first four tiles of "New from visitors" had no photograph, on the web every tile had one. Cause: the server names a reader's photograph the moment it is published (bri_018, bos_047, bil_004, lef_001, all today 11:39 to 13:12), the feed only after the next deploy; those four trees had no photograph in the live feed yet. The website skips a tree its build does not know; the apps drew the tree without a picture. Now both apps use the website's rule: a tile only when the feed already carries that visitor's photograph (`NewFromVisitors.tiles` in Kit/NewFromVisitors.swift and account/Visitors.kt). Reaches phones with the next iOS and Android builds; the four tiles appear with their photographs after the deploy now running. iOS compiled locally; Android left to CI (no SDK on the Mac).

## 2026-11-16 session: Android pins wear the saved, collected and ticket corners

- **Android's map now marks your trees as the iPhone and the website do** (follow-up of 2026-11-12, Hidde: "Ja, doe Android"): a saved tree wears the moss bookmark top right, a collected one the moss tick bottom right, a paid one the blue ticket bottom left, each a white disc with a soft shadow; a saved tree takes the first full pin and is never thinned out. Before, Android drew only the ticket and did not know which trees you had saved or collected. Looked at side by side with the iPhone over Amsterdam (5 saved, 2 collected): the same. In the next Android build.

## 2026-11-16 session: mistyped email addresses (web live, apps with their next builds)

- Website, live with this deploy: under the sign-in email field, "Did you mean <address>?" when the part after the @ is a letter or two off a known provider (data/email-domains.json, 91 domains; outlook.co, gmial.com, hotmial.com, yaho.co.uk caught; mail.com, me.com, company domains left alone). The first Send holds once so the line is seen, the second sends as typed. The check-your-inbox step has "Use a different address"; /account shows the whole address instead of a masked one. The "expires in 15 minutes" line is gone in all eight languages (links last 24 hours).
- iPhone and Android: the same rule and list (Kit/EmailSuggest.swift, account/EmailSuggest.kt), the check-your-email step names the address and offers "Use a different address" (Android in its eight languages). Both build; the iPhone step was looked at in the simulator, the suggestion line and Android only in code (simctl cannot type, no emulator ran). Ships with the next builds.
- qa `check_one_email_domain_list()` keeps the app copies equal to data/email-domains.json. CONVENTIONS.md "A mistyped email address". Not done (Hidde's call): moving bounces out of his inbox.
- Seen: a reader's tip address had a domain that does not exist; no layer catches that.

## 2026-11-16 Guimaraes write pass: gui_010 live in the app

- **Product**: gui_010 The Camellia of Casa de Margaride is in data/cities/guimaraes.json (now 10 trees): 246-word story leading with the 2024 Portuguese Tree of the Year vote, age dispute kept (about 300 by Wilder, over 100 by the decree, 130 by ICNF), recognition line separating it from the taller Casa de Fresco camellia, best_time March flowers, paid_entry true, no photo. APP FIRST: app feed only, no web page. Species set to the canonical Common Camellia (five cities use it). Access gains one sentence ("Anyone can book a visit through the association's published contact; the garden is not open without one."), so preflight reads the appointment as a public booking; the price stays "confirm". Merged with scripts/build_write_2026_11_16b.py; preflight 0 problems.

## 2026-11-16 Guimaraes verify pass: one tree delivered

- **Product**: one verified entry, gui_010 The Camellia of Casa de Margaride (2024 Portuguese Tree of the Year, 4th in European Tree of the Year 2025, Despacho 837/2022), flagged, in data/research/guimaraes-verified.json. Its access, the block of two earlier passes, is settled by the Portuguese Historic Gardens Association's entry (paid entry by appointment, contact given) and the bookable-tour rule. Pin approximate (ICNF coordinate, front courtyard as small site); age kept broad 100 to 300 with the dispute in verify_notes.
- **Rejected / stays lead**: Casa da Covilha camellia (still no stated access), Moreira de Conegos pine (no access or exact pin), Casa da Ribeira (wood, no collectible point); all other register rows within 20 km are live, outside the day-trip boundary or belong to Braga, Paços de Ferreira and Santo Tirso.
- **Breakage**: evasoes.pt (403 on the Margaride visit article, not archived) and the Overpass mirrors; the 8 EUR price is only a search summary and is flagged as to confirm.

## 2026-11-16 write pass: nothing to write

- **Product**: nothing new. The seven research files suggested for this pass (wisconsin, us-photo-batch-1, wales-yews, somerset-dorset-yews, southeast-england-yews, washington-dc-2, new-york-3) are fully published. `passcheck.py --pending` lists only the 15 entries the earlier write pass today judged as standing holds (all_001, asp_001/002, ssb_002/003, brd_001, cbu_001, dmr_002, det_001/002, frk_027, sgz_005, inn_007, tmt_001, not_002/003) or duplicates (sfo_012, taiwan a28_001); no new verified file since. No story written over a hold.
- **Next**: the write shelf needs a verify pass first; US and UK verify targets from `city_queue.py --next`.

## 2026-11-16 later attempt: Coimbra verify found nothing

- **Product**: nothing new. The shelf is nearly empty: of 19 pending verified entries only 2 shipped (see below); 17 stand on earlier holds. Coimbra verify pass (claimed, released, now a 48h wall): the open leads are private quintas, already live, or have no pin or current measurement; a lead for the Buçaco sequoia twins (bsc_010 or separate) and notes on the Botanical Garden Eucalyptus cornuta (1984 figures via Goes, no pin) were added to data/leads/coimbra.json. Next for a window: Guimaraes, Porto, Setubal, Stuttgart, or a register scout (Zurich, BUILD).
- **Breakage**: Overpass answers 406 or times out from the runner.

## 2026-11-16 write pass: pending verified trees and the five READY Leipzig leads

- **Product**: 2 trees into the app (app-only under APP FIRST, outside the pace). phl_010 the Grumblethorpe Ginkgo (Philadelphia, c. 1830, "one of the oldest female ginkgoes in America" by its owner): its hard-rule-10 hold is lifted because the owner's visit page (philalandmarks.org/contact-visit) now gives public hours (second Saturdays May to October, 12 to 4, garden mornings Aug to Oct, $10), so access, `paid_entry` and the last paragraph are written from that page. lpz_032 the Horse Chestnut of Papiermühlstrasse (Leipzig ND 34, cadastre N79444 re-read today: 354 cm, 14 m, planting class 1876, not felled; 96% of the horse-chestnut reference), best_time May flowers. The Commons file Rosskastanie_Lzg._Papiermühlstr.jpg is named on the ND list; not looked at, a photo pass can.
- **Skipped, standing holds unchanged** (each reason is in its research file): all_001 (no sighting since 2009), asp_001/002 and ssb_002/003 (register point only in a forest, no tell), brd_001 (gated hospital courtyard), cbu_001 (doline with no route), dmr_002 (no sign it stands after 2019), det_001/002 (no coordinate), frk_027 (schoolyard, no viewing source), sgz_005 (no path), inn_007 (likely a private yard), tmt_001 (register group, access unknown), not_002/003 (access unproven). Duplicates or already live: sfo_012 (= sfo_004), taiwan a28_001 (= alh_002), lul_001 live, `_notes` is not a tree.
- **Leipzig leads marked** (no longer READY): Badeweg oak held (allotment colony, rule 10), Plausig lime and Lützowstrasse oak held (cadastre only, 39% and 48% of their species reference), Kleindoelzig oak held (outside the cadastre, needs a verify pass). Builder: scripts/build_write_2026_11_16.py. Preflight 0 problems.

## 2026-11-16 night run (window from 13:14 UTC): rung 1, 19 reader photographs looked at

- **Product**: 19 reader photographs judged. 9 trees that had no picture now have one (Kamakura Tabunoki, Bilbao chestnut and bald cypress, Boston Public Garden ginkgo, bur oak and pagoda tree, Bristol Combe Dingle sequoias, Setubal sideways melaleuca, Llanerfyl yew); 7 more went into strips beside the lead (Quinault spruce, Tree of Life, Borrowdale yews, Bishops Knoll oak, Royal Hotel vine, Champion Lodgepole, Bird Tree Road blackbutt). Pins moved to readers' GPS fixes at Kamakura, Bilbao, Bristol and Olympic. 1 duplicate dropped.
- **Held**: Bishops Knoll "Monterey cypress" (photo reads as a redwood, no railings) and the Public Garden "Bagheera beech" (furrowed bark, not a beech): species unsure, wrong tree possible.
- **Fixed on the way**: a colon-reveal sentence in the Setubal melaleuca story and the Boston FAQ that promised "thirteen" for a city of sixteen. Preflight 0 problems.
- **Seven unmapped tips** got a verdict in data/leads/_sightings.json. Strong, still to publish with a source: the Essaouira ombu (fix, huge), the Jelasnica oak in Serbia (fix), Den freda eika near Norheimsund (girth 706 cm, no coordinate yet). Held as leads: Prince Eugen's "oak" (photo is a maple), the Helmond plane avenue, the Tassili cypress (no pin), the Vigeois yew (photo credited to someone else, not usable).
- **Found**: a kamakura_003 reader note says the tree stands in Hase-dera temple, slightly north of our pin; not acted on. judgement.py --scan only stubs trees still in the queue, so after sightings_publish the sight: verdict rows had to be written by hand (preflight refuses without them).
- Health: green except 2 web-error types (getCurrentPosition in maplibre); no BLOCKER.

## 2026-11-16 session: the totara and the olive the run could not place

- **Product**: two readers' website tips live, app first. The Giant Tōtara of Montgomery Park, Banks Peninsula (akr_001, new place Akaroa): DOC says it may be 2,000 years old and 8.5 m round, the reader's own figures; pin and 819 cm, 19.8 m from NZ Tree Register CR/1424 (observed Dec 2025). Mastrinka, the olive of Kaštel Štafilić (cdl_003, Kaštela now two trees, olive the hero): Bioportal natural monument ps.4639 pin, 1,500+ years, 6 m, 10 m from kastela-info.hr; access over the railing at the town's visitor point beside the Maslina kindergarten; the reader's note quoted.
- **Found**: both were held as "no coordinate or place name", but the submission's city field named the place (Akaroa, Kaštel Štafilić). The night run reads the lead row, which has no city; inbox.py shows it. Preflight 0 problems.

## 2026-11-16 session: crash reports in PostHog, iPhone and Android

- **Product (next iOS build, and Android before its release)**: every crash on every phone now reaches the PostHog project the app already measures into, through PostHog's own SDK with only its crash handler on (Kit/CrashReporter.swift, account/CrashReporter.kt; Hidde chose one tool over Sentry or Crashlytics). Screen views, lifecycle events, taps, session replay, flags and person profiles stay off; Measure's own events are unchanged. Library named per hard list 5: posthog-ios 3.56+ and posthog-android 3.77.1. Privacy page says it (crash report to PostHog, EU). Builds and unit tests green on iOS; Android compiles.
- **For Hidde**: (1) create a PostHog personal API key with the scopes "error tracking write" and "organization read", so each build's dSYMs (iOS) and R8 mapping (Android) can be uploaded and crashes read as file and line; until then they arrive as addresses. (2) App Store Connect, App Privacy: check that Crash Data is declared (not linked to the person, used for app functionality). (3) PostHog, Billing: a limit of 0 on every product keeps it free.

## 2026-11-16 session: the Royal Hotel grapevine live, and "not a tree" is no reason

- **Product**: the grapevine of the Royal Hotel, Gilgandra NSW (gil_001, new place, app first): one twisted trunk roofing the whole beer garden on a steel pergola, a reader's photograph and GPS fix, their note quoted (planted early 1900s, well established by the 1904 extensions); the hotel's 1892 build as the Bridge Hotel from publocation.com.au.
- **Rule**: held earlier today as "a vine rather than a tree"; Hidde: "boeie het is blijkbaar de moeite - de cactus staat ook live". CLAUDE.md "Which trees get a page" now says an old vine, wisteria or giant cactus worth the walk ships like a tree. Wisteria (Kasukabe, Tokyo, Florence) and cacti (Tucson, Seville) were already live. Preflight 0 problems.

## 2026-11-16 session: the Champion Lodgepole Pine live

- **Product**: the Champion Lodgepole Pine, south of Big Bear Lake, California (bbl_001, new place big-bear-lake, app first): a reader's sighting held this morning for want of a whole-tree frame. Looked again: the trunk frame with hikers at its foot reads as this tree and leads; their meadow shot of the whole tree goes in the strip. bigbearlake.net and NBC San Diego give 110+ ft, 22 ft trunk, 36 ft base; age about 450 from the visitor bureau. Pin from the reader's GPS fix.
- **Looked at, not published**: the Slovenian lime (tip-930): its own Kolpa park sign says 166 cm and 16 m, registered but nothing to walk for. Holborn "dawn redwoods" (photos are planes), the Melbourne jacaranda (young), the Linton poplar (person at centre, 300 cm) and the Royal Hotel grapevine (not a tree) keep their holds. Tripped over: a strip photo named `…-2.jpg` reads to qa as a downscaled copy; named `…-f91bd966.jpg` instead.

## 2026-11-16 session: how often the app really ends on screen

- **Why**: MetricKit reported one store crash from ~4,000 new phones over the Guardian weekend. It only reports from phones that share analytics and never reports memory kills; meanwhile 58 of 4,183 phones reopened the app within two minutes, 53 of those reopens right after a tree page (spread over many trees, all iOS versions, median 48 s after opening).
- **Product (next iOS build, and Android before its release)**: every run that ends on screen now sends one `app_exit_abnormal` event to PostHog with the last event and tree (Kit/ExitWatch.swift, the Crashlytics-style unclean-shutdown flag; Android reads ApplicationExitInfo). Apple's daily foreground exit counts (memory, bad access, watchdog) go in as `app_exit_counts` instead of being thrown away. Photos are decoded at most 2048 px (ImageIO thumbnail decode): 1,172 feed photos are Wikimedia originals of 20 to 50 MP, about 100 MB each in memory the old way; no visible change. PhotoMemoryTests green; Android compiles.
- **Not proven**: big originals are not over-represented before the reopens (69% vs 64% of all tree opens), so they are a risk removed, not the confirmed cause. The new events will say after the build is out.

## 2026-11-16 session: three more readers' trees live (Hidde: "doe ze nu")

- **Product**: three readers' trees live, app first: a giant blackbutt by Bird Tree Road in Middle Brother National Park, NSW (mbr_001, new sighting, GPS fix; the reader's 11 m girth and 300 years match the state's and the National Trust's Bird Tree, but no source puts that name at the fix, so the page leaves it open); the Arbour Oak of Wollaton Park, Nottingham (ntm_001, tip-839, pinned from the Friends of Wollaton Park's uMap tree survey, 1460s per their leaflet); the Oak of Molinazzo, Poggio Renatico (pgr_001, tip-875, MASAF register 01/G768/FE/08, 461 cm, 23 m, register pin approximate).
- **Not published**: the blackbutt reader's two extra photographs show a different, fire-hollowed trunk with a person in front. The morning run had already handled the other 21 open sightings (11 live, the rest leads with a reason); tips 908 (totara), 928 (olive) and 930 (Slovenian lime, NV 8628) still have no coordinate.
- **Tripped over, again**: `judgement.py --verdict sight:<id>` cannot write a row the scan never stubbed, so the three photo rows were added by script (out/tmp/add_sight_rows.py); `verified_sources` must be plain URLs or preflight's register_ids crashes. Preflight 0 problems.

## 2026-11-16 third attempt: shelf still dry

- Nothing published. No claims stood. Braga claimed, only 5 open leads (under the six-candidate floor), released, walled 48h. Portland refused (33 of 30, full). Translations stay paused (TRANSLATIONS_OUT); Zurich register stalled earlier (private plots, no PDF reader on the runner). The 5 Leipzig READY leads were declined earlier; leads.py lists them because block-reasons.json lacks their phrasing.
- Next run: a US/UK city not walled with 6+ open leads (Philadelphia, Milwaukee, Key West) for a verify pass on the 913 source-only leads.

## 2026-11-16 second attempt of the window: shelf empty, Sintra a wall

- Nothing published. leads.py --ready lists only reader sightings (9, handled at rung 1) and 5 Leipzig leads (leipzig is fully published). prepare.py's "awaiting a writer" list is stale: wales-yews and us-photo-batch-1 (27 trees) are already live; the rest are held rows. A verify pass on Sintra found every register row already judged or a duplicate; the Monserrate Eucalyptus linearis lead needs a session with PDF text extraction (Parques de Sintra forestry plan, note added to data/leads/sintra.json). Claim released, Sintra walled 48h. Munich is at 60/60, so claim refused.
- Next run: the refill pile (913 leads lacking only a source) is the real shelf; try a US/UK city not walled (Miami, Key West, Fort Lauderdale, Philadelphia, Milwaukee).

## 2026-11-16 write pass: nothing writable, again

- Nothing published. The 15 pending rows in allentown, aspromonte, brindisi, castelbuono, dartmoor, frankfurt, grazalema-rediam, innsbruck, isole-tremiti, noto, san-francisco and serra-san-bruno are the same shelf the 11-15 pass found, each with a standing hold and no new evidence: access unproven (brd_001, frk_027, sgz_005, inn_007, not_002, not_003, tmt_001), cannot be told apart in a wood (asp_001, asp_002, ssb_002, ssb_003), location not statable (cbu_001), no sighting since 2019 (dmr_002), duplicate of live sfo_004 (sfo_012). taiwan-verified.json holds only a _notes row. all_001 (Allentown cottonwood) now carries its hold in the file. passcheck `--pending` still counts held rows as needing a story; this lane needs a verify pass (sightings, GPS, access) before it has work.

## 2026-11-16 session: one mail route rule (Yahoo and first mails signed, the rest through Gmail)

- Every mail now picks its route by recipient and kind (scripts/mailer.py, `wants_resend()`): Resend for addresses on Yahoo's servers and for first mails to strangers (outreach_send.py, `mailer.FIRST`); Gmail for mail people asked for or expect (contributor_reply, sightings_publish, ambassador: `mailer.EXPECTED`); either route takes over when the other refuses or cannot be reached. Builds on the Gmail fallback below. Tested against fake servers (scripts/test_mailer.py, nine cases); no real mail sent by this change.
- The Supabase hook (supabase/functions/send-email/index.ts) follows the same rule and the same Yahoo list; qa `check_one_mail_route_rule()` keeps the lists equal and reader scripts on EXPECTED. Rule in CLAUDE.md (Reader input), why in DECISIONS.md.
- LIVE since 10:40 UTC: the Send Email hook is deployed (send-email v2, JWT off, signature checked) and switched on through the Management API, with a 7-day token Hidde made. Supabase's SMTP setting (Gmail) stays as the fallback when the hook is switched off. The hook now carries the dashboard's own templates verbatim (`python3 scripts/mail_hook_templates.py` copies them in; run it and redeploy after editing a template in the dashboard). Tested: an unsigned call refused (401); a real sign-up and a real sign-in link to Gmail aliases arrived via the hook, both links signed in and confirmed (303 to /account with tokens); Resend's API accepted the hook's key. Both test accounts deleted. Not tested: a real Yahoo inbox (we have none); the first Yahoo sign-up shows in Resend's Emails log.
- Follow-up sent with Hidde's yes (about 11:50 CET): Yahoo's servers refused mail to 16 addresses since 11-15 (yahoo.*, aol.com, sky.com); 14 still had no confirmed account (4 of them had the 11-15 link mail, expired). Each got a fresh sign-in link through Resend, "the problem is fixed". sky.com added to the Yahoo list in mailer.py and the hook (redeployed). No bounce since the hook went live.
- Hidde: links valid for 24 hours ("make it valid for 24 hours for them"): Supabase's `mailer_otp_exp` 3600 -> 86400. It is one project-wide setting, so every sign-in and welcome link now lasts a day; Supabase checks the age at click time, so the 14 links sent that morning count too.
- Undo: `python3 out/tmp/hook_switch.py off` (scratch) or Authentication > Hooks > Send Email off in the dashboard.
- Seen while there: Supabase's email rate limit is 30 an hour (`rate_limit_email_sent`); the Guardian morning's busiest hour had 25 email sign-ups plus sign-in links, so some people may have hit "rate limit exceeded". Raising it is Hidde's call.

## 2026-11-16 session: mail goes through Gmail when Resend is full

Resend warned at 80% of its free 100 a day. Reason: the Guardian wave. On 11-15, about 84 script mails went through Resend (59 photo-live, 15 replies, 6 Yahoo sign-ins, 4 ambassador). The 129 welcome mails went through Gmail, so they don't count. Past 100, Resend refused and the scripts retried a day later. Now (Hidde: "Yes, add fallback") scripts/mailer.py sends a mail Resend refuses, and the rest of that connection, through Gmail, as the Supabase sign-in hook already does. A dropped connection does not fall back (the mail may have left). Gmail mail is unsigned for our domain, so a Yahoo address still bounces on a full day. Tested against fake servers (refusal, unreachable, no Gmail route raises). Watch the month: the free plan stops at 3,000.

## 2026-11-16 run (window from 10:07 UTC): reader photographs, rung 1

The photo-judge pass viewed all 25 photographs matched to our trees: 4 first photographs live (Hiroshima Aogiri, Palermo Embracing Fig, Lazi balete, Balete Park), 7 already in the strip, 13 were already the lead of the reader-found tree they created (closed only), 1 held. Commit a4cb10bab.
- **Fixed in scripts/sightings_publish.py**: a verdict on a sighting that is already the tree's lead no longer duplicates or rewrites the photo (prints KEPT); `move_pin` no longer upgrades a pin to confirmed on a "fix" that is our own pin echoed back (mra_001 set back to approximate by hand; test added).
- **Correction (rung 3)**: La Tène prf_002 was recorded as a giant sequoia; the reader's photograph shows an Atlas cedar. Renamed "The Tall Cedar of Préfargier", species, story, recognition line, intro and Q&A rewritten; the 705 cm girth stays as the reader's figure. Preflight 0 problems.
- **The 31 unmapped sightings all have a verdict now** (commit 2f3402c41): 11 live as reader-found trees (cnk_004 Cannock Chase, bne_022 Brisbane, and new places Lumbini, Earlysville, Tuatapere, Yungaburra, La Lande-Patry, Mbissel, Sagole, Darwin, Kvam), 20 left as leads with a reason (6 tips without a coordinate, 9 weak frames, 2 with a person posing, 3 not remarkable). The Molinazzo oak (tip-875) and the Močile lime (tip-930) could be pinned from their registers. tip-871's photo carries another photographer's signature, so it is not used. The two baobab photos and the Tolo oak look polished and the app strips metadata, so authorship is unconfirmed; flagged for a look. Not done: translations of the nine new place names (`city_names.py`), the shelf refill (verify pass on a staged city). qa.py has not run on these (needs a build), so CI is its first run. Commits are local; the run-health step pushes them.

## 2026-11-16 session: the red "Maximum call stack" web error is not ours

- The quality line's red Web Live cell ("RangeError: Maximum call stack size exceeded.", 5 reports on 3 pages, 11-15) comes from one client, not our code. All 5 rows say Chrome 157, from two bursts (09:43 and 19:59 UTC) by the same client that also sent 7 "Failed to fetch" rows and an "Error: Na" that day. Lines 190 to 194 point at unrelated code on each page (a comment on /, an `if (!dlg) return` on /explore, a headers() builder on /bilbao); none of it can recurse. It is a script injected by an extension or automated browser, reported with our page as its file. /, /explore and /bilbao run without a console error in Chrome today.
- No filter added: "Maximum call stack" in FOREIGN would hide a real loop of ours. The cell counts 24 hours and goes off by itself around 20:00 UTC on 11-16. If it comes back from more than one browser version, it is real.
- `window.atDownsize is not a function` on /account/settings (3 reports, 3 browsers, 11-15) was already fixed in d0a57c1fd, live since 20:39 UTC; every report predates it.

## 2026-11-16 night run (04:21): reader photograph inbox, rung 1

- **Product**: four first photographs live on photo-less trees from readers: the Becks Prime Augusta Live Oaks and the Old Pecan Tree (Houston), the Kapok Tree (Key West), the Rhodes Bald Cypress (Bong State Rec Area); two pins moved to the reader's fix, now confirmed. Four strip photographs kept behind the lead (the Fraternal Four's National Trust sign, the Angel Oak limbs, the Mexico City ahuehuete plaque and whole trunk). A colon reveal fixed in the Houston pecan story.
- **Left open**: 24 reader photographs of trees we do not map (leads in data/leads/_sightings.json) still wait for a verdict; the other 14 queued rows are the five reader-found trees' own photographs, already live as their leads. Preflight 0 problems. Tripped over: `sightings_publish.py` wants the full sighting id, and a published row leaves the queue before `judgement.py --scan` can register it (verdict added by hand in data/judgements.json).

