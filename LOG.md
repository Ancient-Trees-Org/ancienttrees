# LOG

<!-- archive-index -->

## 2026-11-15 session: the rest of the Guardian inbox, and the mails

- Ten more reader trees live: dnk_010 the King of the Forest (Muirward Wood, Scone; largest Scots pine girth on record per the Forestry Commission, 2002), gsh_001 the Geashill sequoia, wtn_001 a big sycamore at the Crum Creek bridge (Willistown, PA), isp_001 the 800-year plane of Cinar Street (Isparta, the municipality's plaque), krn_001 Mariam Dearit, the baobab chapel of Keren, okb_001 Old Knobbley (Mistley), wyo_001 Wyndham's Oak (Silton), pin_001 Pine Island (Connemara, pinned at the viewing spot), vzy_001 the Fau de Saint-Basle (Faux de Verzy) and zaa_006 the Zaandam wingnut. The three reader photos with a hand-placed pin ship as approximate, not held: the 10-21 rule. Old Knobbley, Wyndham's Oak, Pine Island and Verzy carry Commons photographs (the readers' were screenshots, small in frame, or absent).
- Held: the Emmanuel College plane (Fellows' Garden private by the college's own pages). Not new: the Tule tree (tul_001). Still held from earlier: Majesty Oak, Hanoi banyan, Holborn, Burnside red gum, Worthing sequoia, Waitangi pine.
- Mail: ambassador answers sent to Edinburgh, London and Media (badges on). Eight "your tree is on Ancient Trees" mails sent; the afternoon wave's and these ten go when their pages reach the live feed. One reader (Scone spruce and Lytham chestnut) got two congratulations minutes apart: tree_approved does not bundle two trees of one person.
- Fixed: ambassador.py linked Media's list to a 404 (a place of app-only trees has no page); it now links the explore map at the place. tree_approved.py greets a generated profile name ("Rooted Ash 4451") as "Hi there", lowers a name typed in capitals, and asks one missing fact as a plain question.
- Seven reply drafts for tips no script mails (drafts/reply-reader-*-2026-11-15.md: Master Oak and Monfalletto/Telavi live; Majesty Oak, Hanoi, Holborn, Burnside, Worthing held), waiting for Hidde's yes.

## 2026-11-15 session: Yahoo blocks the welcome mail

- Broken: Supabase sends its auth mails through Hidde's Gmail as info@ancienttrees.app (SMTP set 2026-09, drafts/auth-mails.md). Gmail signs for gmail.com, so Yahoo refuses them ("550 5.7.9 ... requires this sender to authenticate with DKIM"). On the Guardian day 6 email sign-ups on Yahoo addresses (8 bounces) never got their welcome mail and stayed unconfirmed; Gmail, Outlook and the rest arrive.
- Sent with Hidde's yes: one mail to each of the 6 through Resend (signed for our domain), with a fresh sign-in link from Supabase's generate_link, saying from tomorrow Yahoo mail works again. Logged as batch yahoo-signin-2026-11-15.
- Not chosen: moving Supabase's SMTP to Resend. Resend is on the free plan (100 a day) and the day had 71 email sign-ups in four hours, so on a press day every email sign-up would fail past the hundredth. Resend Pro ($20 a month) is too dear for Hidde.
- Built, NOT live: supabase/functions/send-email/index.ts, a Send Email hook that routes Yahoo-family addresses (Yahoo, AOL, Verizon and the rest on Yahoo's servers) through Resend and everyone else through Gmail SMTP on 465 (Edge Functions block 25 and 587), each falling back to the other. For Hidde tonight: deploy in the dashboard, four secrets, Auth > Hooks > Send Email on, test with a Gmail and a Yahoo address. Copy the dashboard's current templates in first if they differ from drafts/auth-mails.md. The mail promised the 6 "from tomorrow".

## 2026-11-15 session, part 3: the Guardian afternoon wave

- Seven reader trees with a GPS fix live as tree pages: ngs_001 the A-bombed camphors of Sannō Shrine (Nagasaki), mbw_001 a veteran yew at Market Bosworth, hth_001 Kett's Oak (Hethersett), ots_001 the pine of Ukimidō (Ōtsu, 400 years by the reader), lon_052 a hollow beech on Hampstead Heath, grn_001 a buttressed giant near Mount Horne (Grenada, species uncertain and said so), edi_022 a Wheatley elm in west Edinburgh ("widest in Scotland" is the reader's claim). Five new one-tree places.
- A photo-judge pass on 19 reader photos: first photographs for the Pococke Plane, the Bishops Knoll oak, the Hundred-Horse Chestnut, the Stara Maslina, the Waverley Abbey Yew and the Autograph Tree (record says copper beech, the photo looks green: worth a check); six more strip/lead photos (Atsuta camphor, Piazza Marina fig, Birnam Oak x2, Land Boat Pine, Cut-Leaved Hornbeam); four byte-identical duplicates out; held: Groningen beeches (scars not visible), the Noorderplantsoen ginkgo photo (it is a beech), the Karasaki pine (95 m off, no pond).
- Reader pin moves applied by hand (no script handles them): Redford redwood, Stevenson's Yew, Lytham chestnut, York pear-barked beech.
- Leads waiting for a source or a real pin: Geashill sequoia, King of the Forest (pin placed by hand, then moved 1.1 km by a reader), Media sycamore (hand pin), and the tips Isparta plane, Old Knobbley, Emmanuel College plane (access to check), Pine Island Connemara, Mariam Dearit (Eritrea, a reader's tree so focus does not block it), Waitangi pine; no-photo tips Faux de Verzy, Zaandam wingnut, Tule tree, Wyndham's Oak.
- Mail: the Linford Lime is marked not-to-congratulate (it was already on the map). The knock's `tree_approved.py --send` sends the "your tree is on Ancient Trees" mails for every reader tree once its page is in the live feed; Hidde asked for these to go.

## 2026-11-15 session, part 2: the holds re-read, two tips live

- Two trees a reader tipped (submission 702) are live: lmr_001 the Cedar of Monfalletto, La Morra (planted for a Falletti wedding, 1856 per langhe.net or 1875 per FAI, both stated; Commons photographs) and tlv_001 the Giant Plane of Telavi, Georgia (more than 900 years by the sign at the tree; height on the sign left out, a visitor doubted it).
- Breakage: my 11:06 deploy failed on `"photos": null` for dnk_009 and lyt_001 (the schema wants a list or no key). Fixed and pushed; preflight now refuses a null photos list at the push.
- Holds re-read, all still held: Holborn (two ordinary planes in Lincoln's Inn, the note names dawn redwoods), Burnside red gum (the SA heritage register refuses our fetch and no other source names it; waits for their own photograph), Majesty Oak (private), Worthing sequoia (no fix, no source), second Azores fig (no fix), Hanoi banyan (not shown visible from the street), 691 (no photo arrived). Four 10-30 uploads from our own account got written verdicts matching their lead notes.

- New reader trees live: glg_001 the Geelong Ginkgo (planted 1859, Victoria's Tree of the Year 2026 per Time Out and the gardens' sign; four reader photographs), lyt_001 the Lytham Sweet Chestnut (veteran with a dead central stem; 300 to 400 years and 7 m girth are the reader's), dnk_009 the Sitka Spruce at Scone Palace (reader's fix in the palace grounds, a different tree from the Douglas fir 67 m away; species is theirs). Geelong and Lytham are one-tree places, so tree pages only.
- Reader photographs: first photograph for the Redford Wood Redwood (pin to the reader's fix, confirmed), the Azores Borges fig (matched to the Commons view of the same split trunk) and the Kyushaku-fuji of Byakugo-ji (in bloom, lit at night; the tree had none). Strip photographs for Stevenson's Yew, the Royal Oak and the Windrush Square Plane. Held: a second Azores fig photo (a different tree with hanging roots, no fix).
- Held or leads: the Majesty Oak, Fredville (private land, no public access; hard rule 10); the Worthing sequoia in Lyons Farm Open Space (no fix, no source); the Hanoi banyan at Nhan Dan (still blocked, not shown visible from the street); new leads la-morra (Monfalletto cedar) and telavi (giant plane) from one reader's message.
- Submission 691: an app tree with a photo location in Gisborne, NZ, but no sighting row and no photograph arrived. Either still queued on the phone or the upload failed; watch whether it turns up.
- Edinburgh ambassador request (695): the answer mail with the badge is ready and goes with the next knock (`ambassador.py --requests --send` in nightly.yml).
- Two Tamba story sentences rewritten (colon reveals) now that the page carries a reader photo. The inbox re-queued the three new trees' own lead photographs; marked processed by hand.

## 2026-11-15 08:44 window: readers' photographs and two new reader-found trees

- Rung 1: eight photographs looked at and applied. Coldwaltham Yew (the St Giles sign) and the Belvoir Oak (hollow veteran trunk) get their first photograph; Fulham Palace holm oak, Barney the Plane, the Argyle Street Ash, El Drago Milenario and the Ravenscourt baobab plane gain a strip picture; a duplicate Argyle Street upload came out. The Belvoir pin went confirmed on a "reader fix" that was the tree's own published coordinate, so I put it back to approximate. Two reader trees from Australia are live: mvv_001 the Canary Pine of Leighton Gardens (Moss Vale, planting date 1905 is the reader's account) and ads_001 the River Red Gum of Rostrevor (Adelaide, 200 years is their estimate), each a new one-tree file. Held: the Burnside red gum (the photograph is an archival State Library print, not theirs; plaque text kept as a lead) and a veteran lime tip with no coordinate. Five tree notes read, none hidden.
- Rung 2: web error `window.ethereum` and an injected base64-SVG image rejection are browser extensions (nothing in site/src touches either); web-errors-js.ts now ignores both. iOS: `NameTests.testNoAnswerFromTheServerAsksNobody` aborted again on 11-14, twice (also 10-26); the code under test is a three-line early return, so it is the host app crashing in the simulator, and I cannot read the xcresult from this runner. Needs a Mac session to open the crash report.
- Scouting: Zurich (CC0 Geschuetzte Einzelbaeume, 27 rows, no girth or age, mostly private plots: stalled, 0 trees; the Kanton's 1980 inventory is the next angle) and San Juan retry (no DRNA list, one coordinate-less Rio Piedras fig lead: stalled, next angle a PDF tool for the 2002 USFS champion list). The runner has no PDF reader, which now blocks Buffalo, Leipzig and San Juan alike. Shelf stays dry; no tree beyond the two reader ones was published.

## 2026-11-15 retry window: shelf is dry, walls up

- Leipzig's 5 READY leads were all declined earlier (cadastre-only, no life check, one on a private allotment); leads.py still lists them READY because block-reasons.json lacks their phrasings (widening needs Hidde). Potsdam: 0 new trees, 6 more leads held. Rothenburg claimed and released unworked. Bamberg gave 2 app-only trees. Staged focus cities Portland, Munich, Porto, Salzburg are full. Next: Zurich register scout.

## 2026-11-15 write pass: two Bamberg trees for the app

- Two new trees in the app (app-only, no web page until a reader adds to them): bam_010 the Vollandseiche of Steppach, a pedunculate oak 7.50 m round growing on top of a beer cellar (confirmed pin on the roadside viewing point, age 200 to 300 or about 300 stated as a dispute), and bam_011 the churchyard lime of Hohenpoelz, 6.50 m round over the wall of a fortified churchyard (approximate pin, churchyard as site, best_time June flowers). Both flagged: no dated image since 2017 and 2010, and both stories ask readers to confirm they stand.
- bam_011 species written as the canonical Large-leaved Lime (Tilia platyphyllos), not the verify file's "Summer Linden". The Bamberg page copy keeps saying nine, since the web still shows nine; the Germany intro no longer says Bamberg has "five trees with no age" (it had nine, one dated by legend). Bamberg claim released.

## 2026-11-15 write pass (US/UK first): nothing writable

- Nothing published. Every US and UK file named in the brief (us-photo-batch-1, washington-dc-2, wales-yews, somerset-dorset-yews, new-york-3, wisconsin, boston-*) is already live; passcheck's 391 is mostly stale rows. The true shelf is about 20 trees, and each carries a reason: held for access (brd_001 Brindisi figs, frk_027 Frankfurt mulberry, sgz_005 Zurraque holm oak, inn_007 Innsbruck lime, not_002/not_003 Noto, tmt_001 Tremiti ombu), cannot be told apart (asp_001/asp_002 Aspromonte beeches, ssb_002/ssb_003 Serre firs, cbu_001 Acerone), no sighting after 2019 (dmr_002 Meavy Oak), duplicates of live trees (sfo_012, sfo_014, sfo_015, and the !! rows in cardiff, wolverhampton, new-york, washington-dc), or left as the night run held it (all_001 Allentown cottonwood, alive unconfirmed since its 2009 measurement). The writing lane needs a verify pass before it has work again.

## 2026-11-15 07:00 run

- Rung 1 empty (no sightings). Rung 2: iOS run of 11-14 failed on one test of 274 (`NameTests.testNoAnswerFromTheServerAsksNobody`, signal abrt), the same crash seen 10-26 and read then as a simulator flake; app untouched, watch the next run. Web errors orange: one `window.ethereum` error, a wallet browser extension, not ours. `gh workflow run deploy.yml` was refused (HTTP 403), so the live site stays behind main until a deploy runs.
- Write pass (US/UK): nothing writable, every pending tree held, duplicate or a lone city; phl_010 (Grumblethorpe Ginkgo) hold-noted (hard rule 10). San Francisco verify, ninth pass: nothing new, wall for 48h.
- Scout RETRY Buffalo: one tree verified and written, buf_001 Franklin Street sycamore (confirmed pin, flagged, age disputed, stated on the page), new data/cities/buffalo.json. Leads: Delaware Park Mighty Oak, NY DEC Big Tree Register PDFs (needs a PDF tool, next angle). Not pushed (credential); the Run health step pushes.

**Older entries live in the archive**, moved by `scripts/archive_logs.py`, nothing deleted:

- [2026-11](archive/LOG-2026-11.md)
- [2026-10](archive/LOG-2026-10.md)
- [2026-09](archive/LOG-2026-09.md)
- [2026-08](archive/LOG-2026-08.md)
- [2026-07](archive/LOG-2026-07.md)

So absence from this file is not evidence something was never tried: `grep -ri "<place>" archive/` before concluding a hunt is new. Re-running an exhausted hunt is this project's most repeated waste.
<!-- archive-index -->
## 2026-11-15 night run (window from 01:29 UTC): 11 trees for the app (Chicago 6, Key West 2, Tulsa 1, Philadelphia 2)

Dry lanes, said plainly: Edinburgh and Milwaukee leads carry no coordinates (claimed, then released unused; their walls were reverted by hand because nothing was tried), Leipzig is at its target. Allentown scouted (rung 5 RETRY): one flagged cottonwood (all_001, PA Big Trees, 2009 measurement, alive unconfirmed) held back in data/research/allentown-verified.json, six leads in data/leads/allentown.json, status still stalled, retried 2026-11-15. Cost this window about 650k tokens for 11 published trees, well over the 15k target, because the US and UK shelf is mostly thin or unplaced leads; the cheap lane there is spent.

Philadelphia: the Penn Treaty Elm on College Green (phl_011, 1896, "named for" the original, never claimed as its descendant) and the Morris Arboretum weeping beech (phl_020, verified by an earlier pass and never merged). The Grumblethorpe Ginkgo (phl_010, c. 1830, "one of the oldest female ginkgoes in America") was written and kept out: its sources give appointment or second-Saturday access, which preflight reads as hard rule 10's no; it stays in data/research/philadelphia-verified.json for a session that finds a view from Germantown Avenue. penntoday.upenn.edu answers curl with a Cloudflare challenge (WebFetch reads it); not added to the blocklist.

Tulsa: the Woodward Park arboretum's state-champion Dawn Redwood (tsa_002, a 1964 planting, measured 2023). Its neighbour tsa_003 (English oak, "state champion" on 2015 measurements, no figures in the register, about 60 years old) was written but kept out: preflight's young-and-unmeasured note counted it, so it waits as a lead until someone measures it; story stays in data/research/tulsa-verified.json. The best Tulsa tree, the 200-year Hanging Tree bur oak by the BOK Center, has no usable pin or access evidence (check aerial imagery near 36.154, -95.995).

Reader inbox and notes empty. Chicago: six Cook County champion-register trees (chi_059 to chi_064, GNSS-confirmed pins, no photographs, no ages); chi_058 was a duplicate of chi_004 and was dropped. Key West: the Kapok Tree (1900 vs 1905 stated as open) and the Cosgrove House banyan (view-only from the sidewalk), kyw_003 and kyw_004; its species is "Fig (Ficus sp.)" because rule 9 allows one common name and the other cities use Fig. All app-only under APP FIRST. Preflight 0 problems. 7-day visits line not printed by prepare.py today.

Breakage, separate: iOS app has failed twice in a row (11-14 11:59 and 21:05), both on the same test, `testNoAnswerFromTheServerAsksNobody` in NameTests.swift, "Test crashed with signal abrt", while no ios/ file changed since the last green run (11-13 22:22). The test and Profiles.ensureName read fine, so this looks like a runner or runtime change, not our code; the xcresult artifact (xcresult-43640952064) would say. For a session on the Mac. Web errors orange: one `window.ethereum` TypeError on one page, a wallet extension, not ours; no action.

## 2026-11-15 night run (window from 00:58 UTC): nothing published

Reader inbox empty. health.py: iOS app red (run 43640952064, 273 passed 1 failed; the failing test is only named in the xcresult artifact, unreadable on Linux, left for a session), web errors orange (one new inline-script TypeError), 6 of 12 knocks delivered. San Francisco: an eighth verify pass found the register exhausted, and a write pass found sfo_012/014/015 are duplicates of live sfo_004/003/006. The claim is not released (release refuses while those rows sit in the verified file). For a session: live sfo_005 and sfo_013 look like one Moreton Bay fig (3555 Cesar Chavez, about 80 m apart; check the trunk, then retire sfo_005); sfo_006's pin says confirmed but the register point was never checked; sfo_004's recognition line says "spongy to the touch", which the notes do not support and which invites touching the tree; sfo_015's alive check concerned a different plant.

## 2026-11-14 night run 16:20 UTC: deploy fixed, one note read

Rung 2. Build and deploy had been red since 11:43: qa refused an orphan vendored file, `bcn_061-the-olive-of-the-historic-botanical-garden-gate-500.jpg` (nothing points at it; the tree's photo url is the shorter name). Removed it with git rm, preflight 0 problems, pushed. A reader note on the Istanbul Nettle Tree (ist_013) says the 4.1 m girth looks too big; read, left visible, marked seen. The register's 411 cm stays, and the story's "145 centimetres across" is a different measure, so it is not settled. For Hidde: the run's token cannot dispatch deploy.yml (HTTP 403), so the fix goes live on the next push-triggered or scheduled build. The iOS app run of 11-14 failed after 2h8m (probably the runner's timeout); app work is a session's, not touched. Nothing published; the shelf is under its floor (919 leads need only a source) and I stopped here, no verify pass dispatched.

## 2026-11-14 Istanbul reader's three photographs live (session)

- **A reader's morning walk through Gülhane, three trees in half an hour, now on the pages.** The Gülhane London Plane (ist_012) and the Gülhane Nettle Tree (ist_013) had no photograph and now lead with theirs; the Taşlı Çınar (ist_004) takes theirs as the lead and keeps the old one in the strip. Their note on ist_013 ("the girth is recorded as 4.1m but that appears an over-estimate") is live as a tree note; the 411 cm figure is unchanged until a source or a second reader says otherwise. The "your photos are live" mail is pending for the next knock.

## 2026-11-14 Villa Salina oak live (session, Hidde's yes)

- **New tree: The Oak of Villa Salina (bologna/bol_013)**, a reader's website submission (tip 668) from Castel Maggiore, just north of Bologna. Pedunculate oak, 580 cm and 36 m from the 2023 list of new Alberi Monumentali d'Italia; age 200 to 300 years by the reader's estimate. The reader's photograph is the lead; their words on the Malpighi engraving and the loggia ceiling are quoted unnamed, in English and in the kept Italian overlay. Pin from the July 2023 regional annex's coordinate, approximate. Access: the park opens for events and the Comune's bookable guided walks (rule 10). The reader's three further photographs show the engraving, the ceiling and the gate, not the tree, so they stay unpublished. Bologna's free-to-see FAQ now names the oak, and the oldest-tree answer says "precisely dated" (the reader's estimate runs past 206 years).

## 2026-11-14 daily publish (scheduled task): queue empty

- **Daily publish: queue empty.** No builder newer than 11-12; every written tree in the research files touched since 11-11 (Braga, Chicago, Fort Lauderdale, Kansas City, Leipzig, Miami, New York 3, Sintra) is already live, since write passes now put trees straight into the app. Detroit det_001/002 stay held for a pin, not for the pace. Nothing published, pace untouched. For Hidde: the daily task "publish-held-trees-daily" can be switched off under Scheduled.

## 2026-11-14 Leipzig write pass (session)

- **Leipzig: 1 tree written and live in the app** (lpz_031 the Great Oak of Leinestrasse in Doesen, Naturdenkmal ND 101, one of the six tree monuments Leipzig held before 1992; 5.30 m round; the allotment colony behind it is named after it). Age kept at 300 to 400 years from a 2009 caption, the cadastre's 1686 class named as a class and not a planting; the 24 m versus 28 m height conflict between the two city records stated in the story. Seen from the pavement, recognition line written, no best_time. App-only under APP FIRST. Meta description now says 30 trees; Leipzig is at its target of 30. A CC BY-SA Commons photo (MKBler, 2019) is named in the old verify notes for a photo-judge pass. Claim released.
- Nothing else in the US/UK/Germany pending list was writable. Detroit det_001 and det_002 are written but both have null coordinates and a hold, so they were not merged (no honest pin; they need a map point from the cemetery's tour PDFs or a reader fix). dmr_002 Meavy Oak is held (no sighting since 2019's "irreversible decline" report); frk_027 is held under hard rule 10 (schoolyard, no source shows it seen from the Peterskirchhof); sfo_012 is live sfo_004; car_001, nyc_031 and wol_001 are already live as crd_004, nyc_130 and wvh_001, so those research rows are stale.
- For the next session: Leipzig's question answer lists the Menzellinde (200 to 300 years) as next-oldest after the Starkeiche; lpz_031 at over 300 now arguably ranks between them, if it ever gets a web page.

## 2026-11-14 Fort Lauderdale write pass (session)

- **Fort Lauderdale: 6 trees written and live in the app** (ftl_005 Florida's champion baobab, 10.57 m round, and ftl_006 its challenger, both in ArtsPark at Young Circle, Hollywood, free; ftl_007 the state champion African mahogany in Plantation Woods Park, free, crown 38 m across; ftl_008 a challenger sandbox tree, ftl_009 a challenger gumbo limbo and ftl_010 the state champion candlenut, all three inside Flamingo Gardens, paid). App-only under APP FIRST, outside the pace. The two baobabs stay two entries: separate register records, separate measurements, 115 m apart, no single place to stand. No ages given (register measures size; baobab planting date disputed and stated so). Left out as unsourced: the Millennium Springs fountain, sandbox seed pods, gumbo-limbo bark. Species of ftl_007 set to the canonical "African Mahogany" used in Rio and Singapore. No best_time (no phenology files). Paid share now 7 of 10 (70%, a note); the free trees went some way, more free ones would help. City FAQ still says "all four" are paid at Flamingo Gardens, true of the web page's four. Claim released.

## 2026-11-14 write pass (session)

- **Miami: 2 trees written and live in the app** (mia_013 Fairchild's Tantancayo, the 1942 planting at the Vine Pergola and a former Florida champion; mia_014 Fairchild's Cannon Ball Tree, the 1938 gift from Jamaica's Hope Gardens). App-only under APP FIRST, so no web page and outside the pace. Species of mia_014 set to the canonical "Cannon Ball Tree" used in Oahu and Singapore. No best_time (no phenology file for either). Paid share: Miami now 6 of 13 behind a ticket (46%, a note), so the next Miami work is free trees. Claim released (forced: the refusal named kyw_001, which is live in key-west.json).
- Nothing else on the brief list was writable: sfo_012 is held as the same tree as live sfo_004 (fold its pin and girth there); car_001 (Cardiff) and wol_001 (Wolverhampton) claim ids of other live trees and car_002/003, wol_002, sfo_014/015 sit on live trees; chicago-2026-11, boston-common, boston-arboretum, wisconsin, washington-dc-2 and north-england-yews are fully published. Still unwritten elsewhere in the US/UK: dartmoor (1); detroit has 2 written and waiting on merge.

## 2026-11-14 00:36 run (night-run)

- **Chicago: 3 trees added** (chi_048 and chi_049 red oaks, chi_051 butternut, all Busse Forest South, Cook County champion register, confirmed GNSS pins, no photos). The verify pass delivered 10 rows but 7 were already live under other ids (chi_007/008/009/010/040/041/042); dropped from the research file. The butternut story states two facts outside the verify notes (endangered in Canada, canker first reported in Wisconsin 1967), both true but not yet sourced on the entry. For the next session: live stories chi_007, chi_014 and chi_037 count the ranked trees at Busse and now read too low.
- Rung 1: nothing waiting in the inbox or notes. Tip-668 (Villa Salina oak, Castel Maggiore) has no coordinate and its photographs are not on this runner, so its verdict stays open. Health: only red item was the live site being behind main; dispatching deploy at the end.
- Miami verify: only 2 new rows (mia_013 Fairchild tantancayo, mia_014 cannonball tree), both paid entry with approximate pins, so left staged in data/research/miami-verified.json unwritten (Miami would pass a third paid); claim mia stays until it expires. Stratford-upon-Avon scout: still stalled, no trees; next angle is the Ancient Yew Group Avon PDFs.
- Portland refused (full, 33 of 30); the writable pile is a few trees under the 6-tree floor.

## 2026-11-13 19:05 run (night-run)

- **Build fixed (rung 2).** Deploy had been red because the tip-668 sighting row (Villa Salina oak) carried a raw account id as its photo path's first part; now the `people.ref` code (commit c88e24ed7), qa source checks green. This runner's token could not dispatch deploy.yml or nightly.yml (HTTP 403), so the build waits for the next push or schedule. For Hidde: nothing, unless deploy stays red.
- Rung 1 and notes: nothing waiting. Prepare.py: 0 READY to write; Spokane claimed then released (1 unmined candidate of 19, wall for 48h), Porto refused (full at 32 of 30); Sintra, San Francisco, Guimaraes, Braga, Coimbra still walls.
- Scout: Newark retried, the NJ big-tree list answers 403 to curl, verdict rewritten in data/register-scouting.json. No trees added this window.

## 2026-11-13 night run (window from 17:38 UTC)

- Rung 1: tip-668, a reader's Villa Salina oak (Castel Maggiore, Bologna). Photo looked at: a tall oak in daylight. Regione Emilia-Romagna's 2023 monumental list matches the reader's 580 cm and 36 m. Held, not rejected: no coordinate from the reader, and no source says the park is open outside events. Ships once a GPS fix or an open-access source turns up. Verdict is written in data/leads/_sightings.json.
- Rung 5: Sintra verify pass found 0 new trees (register rows all judged or duplicates; one Monserrate eucalyptus lead with no girth or spot). Sintra and Braga are walls for 48h. Portland is full (33 of 30), so no claim.
- Health: only 5 of 12 knocks delivered in 24h (GitHub dropping the cron). Everything else green.
- Not done: `scripts/prepare.py` says the shelf is under its floor (930 leads need only a source), but the supply lanes I tried are empty. 

## 2026-11-13 session: outreach

- **Five mails sent** (Hidde's 'Verstuur alle vijf'): Rijnmond, Il Messaggero, Prima la Martesana, Turismo Lucca, Corse Orientale (europe-source-2026-11-13, Variant A). Rijnmond source on rot_002 fixed (dead AMP link).
- **US and UK wait for the Guardian piece, live Sunday 2026-11-15** (Hidde). Ready and held: us-uk-2026-11-13 (6) and us-uk-press-2026-11-13 (11). From Monday 11-16, in a session: swap the Wilder P.S. for the Guardian link once it is live, re-check every link, show Hidde, send on his word; Glasgow Live and Cambridge News are both Reach, so not the same day. Night runs leave them alone.
- Found: the Suffragette Oak story (gla_002) says "days after" the 1918 Act; the Act passed 6 February, the oak went in on 20 April. Not fixed yet.

## 2026-11-13 session: Supabase egress back under the free plan

Supabase mailed that the org passed the free plan's 5 GB egress this month (grace until 2026-12-13, then possible restrictions on accounts, saves and uploads). Hidde: no paying for now, and no smaller photographs ("fix maar").
- **Backup**: db-backup.yml takes every stored file once in 28 days and only changed files in the weeks between (`-new` artifacts; BACKUP_RESTORE.md says how to restore). Tested: a week costs 24 MB instead of 145.
- **Tiles**: `scripts/shared_thumbs.py` (night run, after sightings_link) keeps a 600 px copy of each shared photo in the new public bucket `shared-thumbs`; 127 made, 83 KB average against 934. Profile tiles on web, iOS and Android load it and fall back to the full copy; the shared tree page keeps the full photograph. iOS and Android take effect with their next builds.
- **Avatars**: two oversized ones re-encoded to 512 px (476 and 117 KB to 43 and 69); new uploads were already 512.
- **The real source, found after Hidde pasted the usage page** (6.0 GB used 10-28 to 11-13, about 375 MB a day, with 19 active users, so machines, not people): `private_store.py` read the whole private_files table (6.4 MB) four times a knock, about 160 MB a day. Now gzip (5.8 MB to 1.2 on the wire), and a push reads back only files changed since the last pull (snapshot in out/), so a quiet knock's pushes read nothing. `crashes.py` (health and quality: 6 MB of MetricKit payloads) asks for gzip too.
- Restriction comes from 2026-12-13 if the cycle 11-28 to 12-28 also passes 5 GB, so about 165 MB a day is the ceiling. Check the usage page around 2026-11-20 for the new daily level.

## 2026-11-13 night run (window from 07:04 UTC)

- **Braga: 4 new trees in the app** (Turiz oak, Pindela tulip tree, redwood and Douglas fir; app-only under APP FIRST, no web page; Pindela is booking-only, 15 km out, said in the stories). Preflight 0 problems. Rung 1 empty (no sightings, no notes); health.py: only the deploy is behind main and 6 of 12 knocks delivered (deploy dispatched at window end).
- Not done: Newark retry (scout_next), mail batch, sourcing.

## 2026-11-12 daily publish (scheduled task): queue empty

- **Daily publish: queue empty.** No builder newer than 11-10 and every held set has been on main since 11-11; preflight 0 problems, pace not touched. For Hidde: the daily task "publish-held-trees-daily" can be switched off under Scheduled.

## 2026-11-12 session: saved trees show on the map, corners in one style

- **A tree you saved is never a dot any more** (Hidde: four saved in Frankfurt and only two showed): on the website's city map saved trees take their full pin first (city-map-script.ts updatePins), and in the iPhone app they get the first pin priority and are never thinned out. Tested on the live Frankfurt page with a stand-in saved list: before, 3 of 4 bookmarks showed (the Goethe Ginkgo in Rödelheim was a dot).
- **All three pin corners now in the ticket's style** (Hidde: "trek ze allemaal eens naar de ticket stijl"): a white disc with a shadow and a filled icon. The bookmark is moss instead of red (it kept the heart's red; the cards' bookmark is moss), the collected tick is a filled check-circle (Phosphor on the web, Apple's checkmark.circle.fill in the app) instead of a line tick, the ticket stays blue but is now the same 15 disc in the app (was 17) and Phosphor's ticket fill on the web (was a hand-made rounded rectangle), the counterpart of the app's ticket.fill. Web and iPhone in the same change; the iPhone shows it from the next build.
- Fixed in passing: the city map painted the saved corners only if the saved list arrived after the map script; it now paints once on start as well.
- For Android: the same two changes (corner style, saved never a dot) before its first release.
- Benchmark in CONVENTIONS.md "A tree you saved, on every map" (AllTrails heart on the pin, Google Maps' list icons kept on the map, both looked at in the browser). Explore and country maps still carry no saved mark; not part of this change.

## 2026-11-12 session: "Approved" and own trees on a profile, in both apps

- **iPhone and Android now draw what the website's profile already shows (Hidde's approved design, CONVENTIONS.md "Your own trees on a public profile"):** on somebody's Collected grid an "Approved" capsule top-left on the trees they added that we took in (MineCard's moss capsule with the seal-check, at the city pill's size, 6 in), then their own trees with their shared photograph (or their name), each opening its shared page. Your own My trees grid marks your approved trees the same way, read from your own sightings rows. "Approved" in eight languages on Android.
- **Live**: merged to main (PR #59, 4a7eec1a0, all checks green). Hidde pasted supabase/approved-on-profiles.sql the same day, so public_profile returns `approved` and `own` now (7 readers have an approved tree); the iPhone shows it from the next build, Android from its first release. Unit tests on both phones decode a payload with and without the keys.
- **Deleting an account keeps the photographs of trees in both apps** (Hidde, 2026-11-12: "het hele idee is toch dat we de bomen houden als mensen hun account verwijderen"): the iPhone no longer empties the sightings bucket on delete (SightingSync.purge gone), only the avatar goes; Android now deletes the avatar too, which it never did. qa `check_a_deleted_account_keeps_its_photographs()` reads both apps' deleteAccount now (checked red with the purge put back, green without).
- Differences: Android opens an own tree's shared page in the browser (no shared-tree screen there yet; data/android-parity.json "people"). The iPhone's person page has no map, so the own tree's pin shows on the website's profile map only. Android gained the iPhone's `-open=person:<id>` launch argument; both apps take `-approved=<ids>` for the sweep.

## 2026-11-12 session: FNP interview done

- Hidde talked to Hans Hofele (Frankfurter Neue Presse) about the Eschersheimer Linde and the app. Print for sure, maybe online; Hans sends the PDF. Two promises recorded in drafts/OUTREACH.md "FNP interview, 2026-11-12": a mail when Android is out (new list "Tell when Android ships", for the session that publishes Android) and app screenshots with Hans's own photographs of the lime (his photos are not in the mail thread or the app inbox yet).
- Fixed: our press mail to the FNP linked /de/frankfurt/eschersheimer-linde, a 404 since the translation trim of 11-05. Every tree url of a trimmed translation (47 overlays) now redirects to its English tree page (redirect-map.ts, f9c78da5d); checked live.

## 2026-11-12 session: inbox, Valencia's photo ask sent

- **Sent (Hidde: "die naar valencia mag eruit"):** reply to the València parks service's tree heritage section, asking whether the photographs on their geoportal fichas of the monumental trees may go on our pages, credited "Ajuntament de València". Their yes would open photos for the Valencia page (31 trees, almost none photographed).
- **Sent (Hidde: "to cockie is goed"):** KNNV Utrecht, his own text; she is searching her archive and has a new tree book at the publisher.
- **Sent (Hidde: "Send it"):** Genziana Ricci, his text rendered in Italian in Ferrara (asks her favourite old tree between Bologna and Ferrara). No reply needed: Dorit's "gute Idee, das mache ich", Remember Singapore's polite no.

## 2026-11-12 session: four more trees get Rainer Lippert's photographs

- **Live with this deploy**: the Bethmannpark Ginkgo and the Schwanheim Old Oaks in Frankfurt, the Three Oaks of the Weinmeisterweg and the Roadside Oak of Sacrow in Potsdam now lead with his photograph, credited and linked, his 10-10 yes in `permission`. Three had no photo; Sacrow's Commons lead moved into the strip. All four were held on 10-25 on distance alone; matched today on his page text instead (the ginkgo's 4.84 m of 2015 is our girth exactly; his twin oak is our 650 cm trunk; his roadside oak toward Krampnitz is ours; Schwanheim is the same wood-pasture grove). Pixels looked at.
- A looser pass (any genus, 3 km) over our 318 German trees without a unique photo found nothing else: the other ten near pairs are different trees by his own girths and places. His site is mostly rural giants; our gaps are mostly city street trees he has not photographed.
- pot_011's story lost a colon reveal (English and German) now that it faces Google.

## 2026-11-12 session: Rainer Lippert's yes on file

- All 57 of Rainer Lippert's photographs (52 German trees) now carry his 2026-10-10 yes in `permission` {words, date}, as the 11-10 compliance rule asks; they were on the baseline before. Each links his monumentale-eichen.de page; none came from monumentaltrees.com (hard rule 1). His yes covers photos from his own site only.
- Open: 149 of 381 German trees have no approved photograph. The 10-25 coordinate pass over his whole site (1,838 oaks, 551 other pages) found no more matches among our trees; his monumentaltrees.com photos of trees not on his own site are outside his yes and would need a new ask.

## 2026-11-12 night run (window from 11:21 UTC): two app-only trees, San Francisco a wall

- Rung 1 and 2 clear (no sightings, no notes; health only notes that GitHub dropped 7 of 12 knocks). Shelf said refill: verify pass on San Francisco found nothing new (seventh pass, register exhausted; the six Bush Street blue gums have no size, age or pin source, so they stay a lead). San Francisco walled for 48h.
- Write pass over the pending files: merged kcm_005 (Vaile Mansion Smoketree, Kansas City, copy rewritten for five trees) and csc_001 (Moreton Bay fig, Cascais, new one-tree place). Both app-only under APP FIRST. 15 entries held or duplicates (sfo_012/014/015 duplicate live trees; frk_027 schoolyard; dmr_002 unconfirmed standing; inn_007 private plot; brd_001 and cdl_001 access unproven; sgz_003 needs an honest access line, story already written; det_001/002 no coordinates).
- Many `data/research/*-verified.json` files are stale (already published); not deleted.

## 2026-11-12 session: a sign-in ends where the tap was going

- **Fixed (Hidde: tapping Isabelle R. on the home page asked for a sign-in and then landed back on the home page):** the website's sign-in sheet now keeps the exact address it was opened on and, for a visitor's name, whose photograph was tapped; after Google, Apple or the mail link the page goes there and finishes the act, so the name opens the profile. The same cause broke Follow on somebody's profile: Supabase returns to the path without its query, so `/profile?u=X` came back as your own `/profile` and the follow was dropped. Both fixed in signin-js.ts (head relay) and visitors-row-js.ts. Checked in a fake browser (jsc): home, profile with query, an unrelated page, an off-site address refused.
- **Apps:** iPhone (Home.swift `openVisitor`) and Android (Discover.kt `openVisitor`) asked for a sign-in on the same name and then did nothing; the sign-in now re-asks the row with the new session and opens the profile, and the row reloads on any sign-in. Every other gate in both apps already finishes its act (save, collect, map filters, add photo).
- qa `check_a_sign_in_ends_where_the_tap_was_going()`; escaped bug ESC-2026-11-12-a-sign-in-asked-by-a-tap.
- **Tested with the test account (apptest@), live:** website home, tap a visitor's name signed out, sign in: lands on her profile (Isabel R.). Website profile, Follow signed out, sign in: back on her profile, Following, row on the server, removed after. iPhone simulator: name, sign in, her profile opens. Android: CI green, not walked on a device. **Breakage on the way:** the first version failed two deploys (qa: the head read the stored session before catching the token, fixed 669cf1c2f), and the home name first stopped one step short (the profile loader was not ready yet; it now retries when the page has loaded, 73c5a6c98).

## 2026-11-12 session: a website photograph now counts as collected

- **Fixed:** Add photo on a tree page ticked the tree as collected only when it came through the collect flow, so the Lisbon photographer's profile showed nothing under Collected. A photograph now ticks it whichever button sent it, as in the app (add-photo-js.ts; qa `check_web_add_photo_is_shared()` now also guards this; escaped bug ESC-2026-11-12). Her lis_021 was ticked on the account by hand (visited, 2026-11-10); her profile shows the tree with her photo and pin, looked at.
- **Checked, nothing missed:** /contribute's form never received a photograph (0 of 227 submissions; the insert with a photo works, tested as apptest and cleaned up). Strangers' web tree tips: 18, 17 from one German contributor, none since the 2026-09-24 sign-in wall (Hidde: leave the wall). 13 stranger accounts have ever added a photograph, 12 with one live.
- **Drafted, not sent:** drafts/reply-piero-unalberoalgiorno-2026-11-12.md, asking where the weeping sophora of his 11-01 website photo stands and what makes it special (no promise to map it). Waits for Hidde's yes.
- **A photograph is always a visit, every route (Hidde: "waar je hem ook vandaan komt"):** web, iPhone (CollectSheet.claim) and Android (Collector.collect) already tick at the photograph; the hole was readers' NEW trees, which get a tree id only when we publish them, so seven readers' own published trees (Tangier, Palermo, Paris, Freiburg, Lisbon x2, La Tène) plus one of ours were missing from Collected. Ticked now. `scripts/sightings_link.py` (every knock) ticks any photographed sighting on a tree that lacks it, dated the day it reached us, skipping photos a viewing pass rejected as the wrong tree. qa `check_a_photo_is_a_visit_on_every_surface()` refuses a push where the iPhone records a tree photo without the tick or Android sends one around `collect()`; verified red with each fault put back.

- **North star on top of the digest (Hidde: "een totaallijst ... bovenin"):** `north_star_line()` in daily_digest.py, above his numbers: strangers who ever uploaded a tree or photo of their own, and those who did on more than one day, each with this week's change, dated by the photo file's upload time (Hidde: "upload datum is relevanter"). Today: 13 (+2), 4 more than once (+0). **Broken since it was written, fixed:** the "Readers' contributions" row read `sightings.created_at`, a column that does not exist; the query failed silently and no app photograph was ever counted. It now counts the same upload days.
- **Own trees on a profile, checked:** your own view (iPhone My trees, web /account, Android) shows every tree you added, live or not. Somebody else's public profile shows only collected catalogue trees and Want to visit (`public_profile()` returns nothing else), so a reader's own tree we did not take into the map is invisible to others. Today that is no stranger's tree (the one unpublished, Tree Hugger's Santranges well, Hidde closed on 10-21); every other reader tree went live and is now ticked. Building the public half needs a change to public_profile() (a paste for Hidde) and the three profile screens; not started, waiting for his word.

- **North star on the digest page as two stat tiles with a 12-week sparkline each** (show_digest.py; Hidde: "visueler"). Local page only; DATA.md keeps the line.
- **Approved and own trees on a public profile, web half (Hidde approved the design, preview/inspect/approved-mock.html):** supabase/approved-on-profiles.sql (FOR HIDDE to paste: `sightings.added`, public_profile() returns `approved` and `own`); sightings_link.py marks `added` from the city files' found_by_reader every knock (says "FOR HIDDE" until the paste); /profile draws "Approved" top-left (style.css `.appr-chip`, the app's MineCard capsule at the city pill's size) and the person's own trees with their shared photograph, linked to /t?id=, and their pin; privacy page says so (privacycheck green); CONVENTIONS.md "Your own trees on a public profile". Live after the paste and a deploy. **Not done:** the iPhone and Android profile tiles. **Dropped:** a "Hide the exact spot" switch was designed and Hidde said no (a tree on a profile is for walking to; it would cost us the location we need); the column left the SQL before anyone pasted it, and the privacy page no longer mentions it.

- **A deleted account keeps its trees, published or not (Hidde: "als we een boom niet approven maar nog 2 andere m aanmelden we m alsnog goed kunnen keuren"):** the website's account deletion now removes only the avatar from storage (was: every photograph in the sightings bucket); the lead in data/leads/_sightings.json was already unlinked and kept (photo_takedown.py, since 09-04), now its private photo stays with it; `sightings_link.py` takes public shared-sightings copies of gone accounts down every knock (0 today). qa `check_a_deleted_account_keeps_its_photographs()` refuses the web purge coming back (verified both ways); privacy page, terms and CLAUDE.md say the trees stay, unlinked. **Not done:** the iPhone and Android deletion still purge the photos until their next build; sent to the running app session (Approved and own trees on app profiles) with the check to extend. **Supabase audit, read-only:** no duplicate tables (`wishes` is a view over saves); unused: view `shared_trees`, function `tree_save_counts`; loose files from the 08-27 deletion test week and Hidde's replaced photos. Nothing deleted: Hidde wants trees kept, so the clean-up waits for his word per item.

- **Sent (Hidde: "verstuur"):** Piero (un albero al giorno), a follow-up in his thread, Italian: his 11-01 website photo only reached us on 11-11, where does that weeping sophora stand and what makes it special. No promise to map it.
- **Live (Hidde pasted supabase/approved-on-profiles.sql):** sightings_link marked 7 reader-found trees `added`; public_profile returns `approved` for 7 readers (prf_001, lis_038, par_034, tng_001, plm_006, lis_037, frb_008) and `own` lists; the website draws Approved (looked at on Peter Kálnai's profile, Tangier fig). Moderated: the closed Santranges well (not a tree) set unshared so it is off Tree Hugger's public profile. Note for Hidde: his own public profile now shows his 29 own test trees with their pins. App PR #59 green but conflicting with main; its session was asked to rebase and merge.

## 2026-11-12 07:32 UTC night run (rung 2, short)

Rung 1 empty (no sightings, no new notes). health.py had one open APP BUG row: the shared tree's photo URL was force-unwrapped. Fixed in SharedTreeView.swift (percent-encoded, nil when invalid, 0d625d527) and the row set `fixed`. No Swift test: it cannot run on this Linux runner, so the row says so. Health is green apart from "5 of 12 knocks delivered", which is GitHub dropping the cron. I did not start tree work: the shelf wants a verify pass (930 leads one source short), which I did not take in this window. For Hidde: next iOS build carries this fix.


**Older entries live in the archive**, moved by `scripts/archive_logs.py`, nothing deleted:

- [2026-11](archive/LOG-2026-11.md)
- [2026-10](archive/LOG-2026-10.md)
- [2026-09](archive/LOG-2026-09.md)
- [2026-08](archive/LOG-2026-08.md)
- [2026-07](archive/LOG-2026-07.md)

## 2026-11-12 session: Android opens faster, and its sheets grow like the iPhone's

What changed in the Android app:
- The map shows its first trees sooner. On the emulator with a release build, the first pins came after 9 to 13 s on a first launch and 4.5 to 7.5 s after that; now 3.1 s and 2.3 s (median of five each, measured with nothing else on the emulator; the older numbers were taken while other sessions shared it). The iPhone simulator on the same Mac takes 1.5 to 1.7 s and 1.1 to 1.3 s. Two causes fixed: the catalogue only started loading once the screen was drawn (it now starts with the app), and the map's style was fetched from the network every launch (it now comes from the copy on the phone, kept fresh in the background, with one built into the app for the very first launch).
- That leaves Android about 1.5 s behind on a first launch and 1.1 s on a relaunch, mostly MapLibre starting its map; a real phone has not been measured.
- Sign-in and the other fitted sheets now drag up to the full height and back, rubber-banding at the top, as on the iPhone (audit row 12). A drag down from the fitted height still closes them.

Breakage: none known. The emulator's swipe injector sometimes delivers the lift late, so a fast flick reads as a stop there; the logic was checked with flicks that arrived on time and with slow drags.

