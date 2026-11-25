# LOG

## 2026-11-25 session: inbox read, Il Dolomiti interview proposed

- Mattia Sartori (Il Dolomiti, L'altramontagna) asked for an interview. Sent on Hidde's "Verstuur" (Resend, in his thread): a video call proposed for Thursday 26 November at 14:00 CET. His answer will land in hidde@ancienttrees.app.
- Waste Magazine received the article and will publish "as soon as possible"; they asked to be reminded if no link has come in a few days. A session on or after 2026-11-30 checks wastemagazine.es and, if nothing is up, drafts a one-line reminder.
- No reply needed: Jakob's yes (Girona, handled by the reader judge), Alessandro's emoji, the Spokesman-Review and East Hampton Star auto-replies, a Notifier sales mail in spam, DMARC reports.

## 2026-11-25 session: a web error that sat orange as two, fixed

- **Fixed**: the card of a tapped pin on a phone-width city map threw "el is null" (Venice, Milan, Pisa, Vancouver; Chrome and Safari) when painting saves closed it again before it was measured. Live with the next deploy.
- **The gap behind it**: web_errors.py counted Chrome's and Safari's wording of that one fault as two orange types, and one wording was seen once the week before, so it never counted as new and never turned red, and no run picked it up. Now one fault is one type in every browser's words, and a known type firing more in a day than in the whole week before, on 3+ pages, is red too. Tests in scripts/test_web_errors.py.
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

<!-- archive-index -->

**Older entries live in the archive**, moved by `scripts/archive_logs.py`, nothing deleted:

- [2026-11](archive/LOG-2026-11.md)
- [2026-10](archive/LOG-2026-10.md)
- [2026-09](archive/LOG-2026-09.md)
- [2026-08](archive/LOG-2026-08.md)
- [2026-07](archive/LOG-2026-07.md)

So absence from this file is not evidence something was never tried: `grep -ri "<place>" archive/` before concluding a hunt is new. Re-running an exhausted hunt is this project's most repeated waste.
<!-- archive-index -->
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

## 2026-11-24 reader judge: a tall golden larch in the Dolomites, a first photo for the Madison tupelo

- **New place, Toblach (Dobbiaco), South Tyrol:** a reader's very tall European larch beside a forest path south of the village. Its golden crown rises far above the spruces, a column above the pines. Live as toblach/tbl_001. The reader placed the pin by hand, so it is approximate and the story says it marks the stretch of path. Their age (70 to 100) and girth (170 cm) are stated as theirs. Photo filed in November, from the photograph's own date. (`tob` belongs to Toba, so the id is `tbl`.)
- **Madison, the Carolyn Black Tupelo (msn_001):** its first photograph, a reader's bare winter silhouette at dusk with the Visitor Center behind. The reader's location was 2 km from our pin, so the pin stayed where it was.
- Left alone: sighting 3c544597 (Amsterdam, unsure among ams_032). It is from our own account and its file is not on disk.
- No open reports, no open feedback. reader_words: nothing new to quote.

## 2026-11-24 night window, second attempt: checked, shipped nothing

- No claims stood. 4 READY leads (leamington-spa 2, york 1, guimaraes 1) plus 1 Taiwan entry is under the six-candidate floor for a write pass; the "awaiting a writer" list is mostly stale research files.
- reader_words, recognise --stuck, enrich --next: nothing to do. Own research stays paused.
- iOS app red answered with `health.py --answer`: run 45469395864 never got a macOS runner (capacity), no code ran.

## 2026-11-24 night window (22:47 UTC): checked, shipped nothing

- Rung 1: the reader judge owns the waiting photographs (the Carolyn Black Tupelo, msn_001; one unmapped sighting whose file is not on disk), so I left them.
- Rung 2: health.py red on iOS app only. Its newest runs failed with "job was not acquired by runner of type hosted" (macOS capacity), not an app fault, so no fix. Web errors orange: two new types, one page each, below the red threshold.
- Own research is paused, so no verify pass. 4 READY leads wait for a writer. Nothing was committed.

## 2026-11-24 reader judge: a reader's photograph of the Tule tree, added

- A reader's photograph of El Árbol del Tule (tul_001, Santa María del Tule) is now on the page, beside the photo it already had. It shows the whole buttressed trunk under its crown in the courtyard, in daylight. The species and description match, and the photo is filed under October, the month it was taken. The reader is mailed through `sightings_publish.py --send`; the verdict is in data/judgements.json.
- No reports are open, no feedback or tips lack a verdict, no readers' words need quoting, and nothing has waited over 24 hours.
- Still waiting: lead 3c544597 (Amsterdam). It is our own photograph and the file is not on disk, so it was not judged blind.

## 2026-11-24 reader judge: nothing new from readers

- Nothing changed in the product. No reader's photograph or tree is waiting, no reports are open, no tips are unjudged and no readers' words need quoting. Nothing a reader sent has waited over 24 hours.
- Feedback 1633 (a mail reply about Verona) was only an emoji reaction to our mail. Closed `handled`.
- Still waiting: lead 3c544597 in Amsterdam. It is our own account's photograph (`mine`), the file is not on disk and the fetcher skips `mine` rows by design, so it was not judged blind.
- data/judgements.json: the scan put the Mirano magnolia entry in a new place in the file. The content is unchanged.

## 2026-11-24 reader judge: the monumental magnolia of Mirano

- **New place Mirano (Venice), The Magnolia of Villa Belvedere (mir_001)**: a reader sent it from the app (sighting f976cbc6, taken October): a giant southern magnolia whose knotted grey trunk breaks low into a dozen snaking limbs, the reader standing at its foot with arms spread for scale, daylight. Italy's national register (MASAF 02/F241/VE/05, Villa Morosini, Via Luigi Mariutto 4) lists a southern magnolia 15 m from their pin with the same girth, 378 cm, and 20.5 m tall; `girth_cm`, `height_m` and `official_register` are the register's, the 155 years is the reader's. Their pin was placed by hand, so it stays approximate. A one-tree place, so no place page on the web (the tree page only). The congratulation mail (`tree_approved.py --send`) waits until the tree is in the live feed after the deploy.
- Left waiting: lead 3c544597 (Amsterdam, our own account's photo, `mine`) and the other old `mine` leads, photographs not on disk; never judged blind.
- No open reports, no feedback without a verdict, no tips unjudged, no reader words to quote. qa source checks, preflight (0 problems) and i18ncheck are clean.

## 2026-11-24 reader judge: a second view of the Vondelpark Poplar

- **Amsterdam, The Vondelpark Poplar (ams_003)**: the reader whose photograph became this tree's lead earlier today sent another (sighting 720f86c7): a close-up of the base of the same huge furrowed trunk behind its iron railing, with a hollow at the foot and yellow poplar leaves on the path, 36 m from our pin. Species and setting match the entry. It went into the gallery behind their lead (`strip`). They already got the "it's live" mail for the lead today, so this photo waits in their weekly bundle (data/photo-live-mailed.json). The pins catch-up could not read coordinates (HTTPError), but the pin is confirmed, so nothing needed to move.
- Left waiting: 38 leads in data/leads/_sightings.json that are `status: lead` with no `hold`. All of them are our own account's photographs (`mine`: Nara, Kyoto, Kyushu, Tokyo, Baarn, and 3c544597 in Amsterdam), and none of their files is on disk, so none was judged blind. They are not readers' trees.
- No open reports, no feedback without a verdict, no tips unjudged, no reader words to quote. qa source checks, preflight (0 problems) and i18ncheck are clean.

## 2026-11-24 reader judge: the Kirkstall Abbey ginkgo has its first photograph

- **Leeds, Kirkstall Abbey ginkgo (lds_003)**: a reader sent it from the app (sighting d229e334, taken November 2022): the whole tree in full gold on the lawn among the abbey ruins, leaves fallen in a ring. Species and setting match the entry; the tree had no photograph, so it is now the lead, filed under November. Pin moved 43 m from the Abbot's Lodging board to the reader's GPS fix (confirmed); the story's line "The pin is the Abbot's Lodging, not a fix at the trunk" was false after that and named how the pin was made, so it now reads only "No source gives a girth or a height." (no translations of Leeds). The live mail went with `--send`; the pins catch-up could not read coordinates (HTTPError), the move itself is in data.
- Left waiting: lead 3c544597 (Amsterdam, our own account's photo, `mine`), photograph still not on disk; never judged blind.
- No open reports, no feedback without a verdict, no tips unjudged, no reader words to quote. Nothing has waited over 24 hours.

## 2026-11-24 reader judge: a third view of the Verona mulberry; Girona has its ambassador

- **Verona, The Silk Mulberry of Ca' di David (ver_011)**: the reader who added it sent another photograph (sighting 421f46f9, taken in July): the same trunk from the field side, its pale-rimmed knot hole matching their earlier frames, water standing on the grass. Into the gallery behind their lead (`strip`), filed under July. Pin untouched (their coordinate is our pin, not a GPS fix).
- **Girona, feedback 1630**: Jakob answered our ambassador explanation with "I'd be happy to do so!". Badge granted (`ambassador.py --grant`, synced). The "Looking after Girona" mail was only printed: this run has no mail credentials, so `ambassador.py --welcome-missing --send` on the next run that has them owes it. Closed `handled`.
- tip:1612 is the submissions row of app sighting 54cf46dd, already judged a duplicate of the live mulberry: verdict publish, nothing to add.
- Left waiting: lead 3c544597 (Amsterdam, our own account's photo, `mine`), photograph not on disk; never judged blind.
- No open reports. Nothing a reader sent has waited over 24 hours.

## 2026-11-24 session: a new follower shows in Activity

- Live on the server now, web on the next deploy, apps in their next build: whoever follows you appears in Activity (the bell) as "X started following you." with Follow back or Following, Instagram's row; the bell's dot lights for it. Before, a new follower was told nothing at all. Asked by Hidde, design approved ("Ja, bouw het").
- Server: `my_activity()` (supabase/follow-activity.sql), run on Supabase through the Management API; it returns hearts and followers in one list. `my_photo_activity` stays for app builds already out (their bell lights only for hearts). No new data: follows already carried their date.
- Checked: iPhone simulator signed in as apptest with a temporary follow from our +1 account (removed afterwards); the web row rendered from the real style.css and row code at 375 px; Android compiles. 75 follows between 43 people today.

## 2026-11-24 session: US local press, two rounds of 25

- **Why** (Hidde: "teleurgesteld dat we geen enkele reactie uit de US hebben"): US readers are second only to the UK (41 trees, 123 photos since 11-10), but about 30 US press pitches after the Guardian got no answer, while Irish, Australian and Canadian desks did. Reading: the "Dutch designer" angle is not local news in the US. Hidde chose to try more US papers with the same mail plus one local tree in the P.S.
- **Round 1, approved** ("Verstuur alle 25"): drafts/batches/press-us-local-2026-11-24.json (private), 25 local outlets in 20 places, Guardian text word for word with "Earlier this month", a P.S. with a tree page in their city (two quote the outlet's own article). Held by today's daily cap of 100 (the Android wave 3 sent 100 today), so the night run's outreach_continue sends it after midnight, through Resend with the mail brake.
- **Round 2, waits for his word**: drafts/batches/press-us-local-2026-11-25.json, 25 more (Block Club Chicago, Times-Picayune, Houston Public Media, East Hampton Star and others); three are a one-time follow-up to October mails (San Antonio Report, West Side Rag, LAist) with a resend_reason. mailcheck clean.
- Not mailed: Cincinnati, Milwaukee, Madison, St. Louis, Atlanta (except one Decatur ginkgo), Nashville, Tucson and Tacoma have app-only trees and no web page to link.
- Measure: replies from these 50 in data/mail-yield.json (press group) by 12-08.

## 2026-11-24 session: Google sign-in chooser, swipe down on a pin's card checked

- Live (web on the next deploy, apps in their next build): Sign in with Google always shows Google's account chooser (`prompt=select_account` on iOS OAuth.swift, Android Account.kt, web signin-js.ts). Hidde's Samsung took the browser's unknown account with no way to switch. Supabase forwards the parameter (read on the live authorize redirect). Test AccountTest.googleAlwaysAsksWhichAccount; escaped bug recorded.
- Swipe down on a tapped pin's card (Hidde: springs back "zowel ios als android overal"): the let-go needed half the card's height; now 56 or a 125/s flick, Material 3's threshold, both phones (BottomSheet.swift, MapSheet.kt). Checked in simulator and emulator: a slow 60 pt drag that sprang back now closes. Next app builds.
- Share on the full-size photo, both phones: a round share beside the X shares the tree's page (campaign `photo`), as Google Maps and Airbnb do. Web lightbox too (PhotoFigure.astro, share-js.ts; looked at injected on the live elm page at 375 and 1280). CONVENTIONS.md entry added.

## 2026-11-24 night run (second attempt, 18:47 window): nothing shipped, shelf checked again

- No claims standing. `leads.py --ready` lists one lead (York, Riverside London Plane): an ambassador's what3words pin, no photograph, no written source, so no story can be written without inventing one; it waits for a photo. The 382 "awaiting a writer" trees are almost all stale research files or duplicates of live ids (passcheck --pending flags them); folding them is a hand job, not a write pass.
- reader_words (4 mail sentences wait for the sender's yes), recognise --stuck and enrich --next all empty. Own research stays paused. No agent dispatched.

## 2026-11-24 night run (window 18:47): nothing shipped, two reds read

- Rung 1: one tree note (Colchester oak, a how-to-find tip, nothing to hide) read and marked seen; reader backlog empty. The unmapped sighting 3c544597 stays with the reader judge.
- Rung 2: **iOS app red is GitHub, not the app**: the 18:15 scheduled run died with "job not acquired by runner of type hosted", all three jobs, macOS arm64 capacity. Nothing to fix; the next run should clear it. **Web Live red is one photo**: the reader's Palermo fig (pal_001-...-d8741ffa.jpg, 579x833, shown at 390x488 pt on phones, 2.0 file pixels per screen pixel; the check's ceiling is `SOFT_AT = 2.0`). A reader's photo is never refused for size and the ratchet is not mine to loosen, so left red. For Hidde: either let the strip show that file smaller or raise `SOFT_AT` a hair; one reader photo should not keep the light red.
- Rungs 5 to 9: own research paused; 4 READY leads (under the six floor), reader_words and recognise --stuck empty; pagegaps shows only species and park intros, which sit behind the strict cut. No agent dispatched.

## 2026-11-24 session: a second owner everywhere; GitHub move to an organisation prepared

- **Asked by Hidde: what if Google blocks the Workspace account too.** Sending keeps working (Resend). Incoming mail is restored by moving the MX records at TransIP to another mail host. Search Console comes back through DNS; GA would start empty again; Play is the real risk. The cheapest guard is putting billing on the Workspace trial. The recovery address koos.agency ends with his job in December.
- **Second owner, done (Hidde, 2026-11-25)**: a second person is now owner or admin on Google Cloud (project Ancient Trees, after the Domain Restricted Sharing policy was overridden for that project only), Search Console, GA, Play, Supabase and Resend. GitHub is the one left; it waits for the organisation.
- **Prepared, not done**: moving the repo into a GitHub organisation, since a personal repo cannot have a second admin. The steps are in .github/ORG_MOVE.md, and `scripts/move_to_org.py <org> [--write]` rewrites the 7 files that name the owner. Waiting for Hidde to create the org (`ancient-trees-app` suggested) and say "verhuis". After the move, the Supabase dispatch token must be remade with the org as resource owner, and www's CNAME (still on the old account's github.io) should point to the org.

## 2026-11-24 session: weak points after the Google block; incoming-mail alarm live

- **Live, one door to Google** (Hidde: "kunnen we ook iets inbouwen dat we niet ergens anders enthousiast dingen met google doen die ons weer gebanned kan krijgen?"): scripts/google_gate.py is now the only way any script logs in to the Google mailbox. It keeps one connection for the run, allows at most two logins, and never retries after Google refuses one. Seven scripts moved to it: mailer, reader_mail_replies, sent_drafts, signin_watch, outreach_yield, outreach_inbox and outreach_threads, whose reconnect loop could log in three times per address. data/google-touch.json lists every script that touches Google, where it runs and how often: about 37 mailbox logins a day against a budget of 40, where there were ~500 on 2026-11-20. qa `check_google_is_touched_through_one_door()` refuses a push with a login outside the gate, a Google-touching script missing from the list, or a total over budget. The rule is in CLAUDE.md "How runs fire". Tests: test_google_gate.py (5) and test_mailer_copy.py. Tried live: reader_mail_replies and sent_drafts through the gate.

- **Live**: an alarm when mail stops reaching us (Hidde: "dit lijkt me slim"). The reader judge's existing mailbox login now records in data/inbox-health.json whether the login worked and the day the newest mail arrived (scripts/inbox_health.py, 9 tests). health.py goes red when the login fails, when nothing has arrived for 2 days, or when the check has not run for 2 days. It adds no extra login. Tried against the real mailbox: newest mail today, ok.
- **Found**: the database backup has failed all 20 runs since 2026-11-05. Hidde set the secrets today, but the run at 18:30 failed with `password authentication failed for user "postgres"`. The pooler needs the user `postgres.caimvxiyrtifilimlkqw` and the database password.
- **Live, fewer mailbox logins** (Hidde: "Eens mss zelfs minder?"): the reader judge read the Workspace mailbox on every run, about 125 logins a day from changing US GitHub servers, the same pattern as the Gmail before its block. It now reads once per three-hour slot (an empty cache entry per slot keeps it exact; a manual dispatch still reads), so 8 a day. And mailer.keep_copy logged in once for every mail it filed in Sent (367 logins on 2026-11-20); it now keeps one connection per run and never retries a refused login (scripts/test_mailer_copy.py). Left as they were: sent_drafts and outreach_yield once a day in the digest, signin_watch's bounce check only when it has a mail to resend.
- **Found, his**: the Workspace trial needs billing, the recovery address is koos.agency, there is one super admin, Time Machine has no disk, and the Claude login method is unknown. The new GitHub account is one day old and running ~600 runs a day; www still CNAMEs to the old account's github.io, and the domain is not verified for Pages on the new account.

## 2026-11-24 session: new Play app created, build 6 sent for Google's review

- **The new app exists**: "Ancient Trees: Old Tree Map", `app.ancienttrees.map`, app id 4975394642791101357 under developer account 6289749847935270102. Hidde's ID and phone are verified.
- **Filled in from drafts/play-console-forms.md and play-store-listing.md**: privacy policy, app access, ads, content rating, target audience (16+), data safety (9 types, collected, none shared), advertising ID, government, finance, health, category (Travel & Local) and contact (info@, https://ancienttrees.app). The listing went in with icon, feature graphic and the 4 phone screenshots, in en-GB plus 8 translations.
- **Closed test "Alpha"**: available in all 178 countries. Testers are the email list "Android testers": 772 of the 778 wave 3 addresses, after Play refused 6. Feedback goes to info@. The release is 6 (0.1.0), notes "First test of Ancient Trees on Android." Hidde dragged the .aab in himself, because the browser tool's upload limit is 10 MB. All 23 changes were sent for review on 2026-11-24; Google says up to 7 days.
- **Corrected after a read-only review by a second agent (same evening)**: the listing first got the raw screens `out/play/phone-*.png`. They are now the framed panels `out/play/framed/0-hero` to `4-city` that Hidde asked for on 11-17, and all 9 languages fall back to them. Data safety's delete link now goes to https://ancienttrees.app/privacy#deleting, because signed out the /account page says nothing about deleting; privacy.astro got `id="deleting"`. Tags added: Kaarten en navigatie, Reisgids, Reizen en lokaal. The review was restarted once with everything in it. Left as they are: the hero photo with initials carved in the bark (the same as on iOS), the "shared: No" for photos (user-initiated), and the profile country (counts as profile/name).
- **assetlinks.json**: the new app signing key 00:A4:FA:…:BF:80 has been added for `app.ancienttrees.map`.
- **Still open**: once Google approves, the opt-in link is on the Testers tab. Then rewrite the wave 3 batch with that link and show Hidde the text. No mail goes out without his yes. Old testers stay untouched. Play warns about missing native debug symbols, which is known (see android/app/build.gradle.kts).

## 2026-11-24 reader judge: a reader's photograph now leads the Kavousi olive on Crete

- **Crete, crt_002 The Olive Tree of Azoria (Kavousi)** (app, sighting e5c72d4f, taken 2026-07-23, 55 m from our pin). The photo was opened. It shows the whole base of the olive behind the site's wooden rail in daylight and colour: a huge fluted, many-stemmed trunk with buttress roots spread over the gravel, and a bench beside it. The species and description match. It went on as `add`, so the reader's photo is now the lead (1200x1600, filed as July, its own month), and the Commons picture moves into the strip. The reader was mailed. The pin was left as it is: it is confirmed, and the pin step could not read coordinates (HTTPError).
- Left alone again: 3c544597 (our own account, no photo on disk). There were no open reports, feedback or tips, reader_words had nothing to place, and the backlog is empty. qa source clean, preflight 0, i18ncheck clean.

## 2026-11-24 session: Girona answer sent, Astro update merged

- **Girona, feedback 1603**: Jakob's question about the ambassador role was answered on Hidde's line ("for people who enjoy helping, don't think about it too heavily, completely fine if it's not your thing"), sent through contributor_reply.py on his "stuur girona". He asked to keep it as the standard answer: drafts/HIS_VOICE.md 2026-11-24. No badge until Jakob says yes.
- **Dependabot**: Astro 7.2.0 to 7.4.13 merged (#68); the deploy's Chrome check is the test. supabase-js (#67) has a merge conflict and waits for Dependabot to rebase it.

## 2026-11-24 reader judge: a full-size reader photograph now leads the Palermo fig

- **Palermo, pal_001 The Ficus of Piazza Marina** (app, one reader, sightings d9c64779 and a41fc623, taken 2026-10-20). Both files were opened and they are the same photograph, sent twice. It shows the whole colonnade of aerial-root trunks under the crown, from inside the garden, in daylight and colour. The species and description match. d9c64779 goes on as `add`: it is now the lead photograph (1200x1600, filed as October, its own month), and the earlier small reader photo (579x833) moves into the strip. a41fc623 is rejected as a duplicate. The pin move could not read coordinates (HTTPError). pal_001's pin was left as it is.
- Left alone again: the 38 waiting leads in _sightings.json, all from our own account (`mine`) with no photo on disk, 3c544597 among them. There were no open reports, feedback or tips, and reader_words had nothing to place. qa source clean, preflight 0, i18ncheck clean.

## 2026-11-24 reader judge: two old oaks in the Castle Howard car park live

- **Castle Howard (new two-tree place, North Yorkshire), cah_001 The Broken Oak of the Castle Howard Car Park and cah_002 The Twisting Oak of the Castle Howard Car Park** (app, one reader, sightings f7d1128b and 09bc8573, each with GPS from the photo itself, about 60 m apart). Photographs viewed. cah_001 has a broad fluted trunk whose top broke off, with a whole new crown grown sideways from one limb, beside the footpath. cah_002 is a short, massive, ivy-clad trunk among parked cars, its limbs bending, doubling back and crossing. Both are clearly veterans and seen without a ticket. The reader gave no name, species, age or girth, so the species stays "Oak (Quercus sp.)" and the page asks for figures. Both photos are filed as November, their own month. The reader also sent three extra photos with f7d1128b. One shows cah_002 again; two show other big oaks in the same car park. Extras are never published, so those two are noted in verify_notes for a later look. No register entry and no source within 100 m; a reader's tree needs neither.
- Left alone again: 3c544597 (our own account, no photo on disk). There were no open reports, feedback or tips, and reader_words had nothing to place. qa source clean, preflight 0, i18ncheck clean.

## 2026-11-24 reader judge: the great horse chestnut over Wallingford's Coach and Horses live, before it is felled

- **Wallingford (new one-tree place), wfd_001, The Horse Chestnut of the Coach and Horses** (app, sighting 0b7fae72): the photo shows the whole bare tree from across the Kinecroft green. Its domed crown rises far above the brick pub and spreads past both ends of it, with temporary fencing in front. The reader says the tree is due to be cut down soon, and the page says so plainly and tells people to go soon. Wallingford Town Council's 2022 tree update names this tree (its landscape value, a fungal decline and structural defects) and is its source. The reader's age of 150 to 180 years is on the page as theirs. The photo is filed as November, its own month. The reader moved the pin 32 m from where they stood on the green onto the tree while adding it (report 1000147). Their spot is kept as an approximate, hand-placed pin, and the report is closed `holds` with no mail (their congratulation mail comes with the tree). No translations.
- Left alone again: 3c544597 (our own account, no photo on disk). There were no tips or feedback, and reader_words had nothing to place. qa source clean, preflight 0, i18ncheck clean.

## 2026-11-24 reader judge: a big hackberry on Venice's Certosa island live; the Vondelpark Poplar gets its first photograph

- **Venice, ven_012, The Hackberry of the Certosa** (app, sighting 2f5cf480, a GPS fix from the device): the photo looks up a thick, smooth grey trunk wound with old ivy. It splits low into several big limbs under a tall, open crown, with leaves turning in November. It stands on the Certosa island, 258 m from our black poplar there (ven_005), and is a different tree. The reader's figures are on the page as theirs: Common Hackberry, 500 cm round, 200 to 300 years. The species stays at the genus, Hackberry (Celtis sp.), because the photo cannot tell the American species they name from the Mediterranean one usual in Venice, so the page asks readers. Filed as November, the photo's own month. Venice now has 12 trees: the English question_meta and FAQ, and the Italian title, question_meta, FAQ and a new tree entry follow.
- **Amsterdam, ams_003, The Vondelpark Poplar** (app, sighting 4f2dbb86, taken 11 m from the pin): the massive, deeply furrowed trunk and high crown in low sun. It is the tree's first photograph, approved as the lead through sightings_publish. With a photo the story became indexable, so its colon reveal was rewritten ("an open question; the elm").
- Left alone again: 3c544597 (our own account, no photo on disk). There were no open reports, feedback or tips, and reader_words had nothing to place. preflight 0, i18ncheck clean, qa source clean.

## 2026-11-24 reader judge: the Piazza Vanvitelli araucaria in Caserta is a bunya pine, as a reader said

- **Caserta, cas_012 (report 1000146, correction)**: a reader wrote that the tree is Araucaria bidwillii, a bunya pine, not a monkey puzzle. Both registers (MASAF 07/B963/CE/15 and Campania scheda 48) say Araucaria araucana. But the register's own photograph (scheda 48, img/48.jpg) shows a dense column of glossy foliage in tufts at the branch tips, which is a bunya and not a monkey puzzle's bare, rope-like arms. So the reader wins. The species is now Bunya Pine (Araucaria bidwillii). The story says what the registers call it and what the reader and the tree say, and the Chile paragraph is gone. The recognition line, the yew's story (cas_014), the Reggia bunya's story (cas_024, "a second bunya, thicker in the trunk") and the city FAQ follow. Caserta has no translations. The reader wrote their own words, so the report is closed `holds` with no mail, and a suggested answer is in drafts/reply-reader-1000146-2026-11-24.md.
- Left alone again: 3c544597 (our own account, no photo on disk). No other photographs, leads, tips or feedback waited, and reader_words had nothing to place. qa source clean, preflight 0, i18ncheck clean.

## 2026-11-24 reader judge: an old oak with silver limbs at Tranekær, Langeland, live

- **Tranekær (new one-tree place), tnk_001, The Silver-Limbed Oak of Tranekær** (app, sighting 35263410, a GPS fix from the device): a big old oak at the edge of a wood, photographed across an open meadow. Its trunk forks into two stems, and a tangle of bleached silver-white dead limbs reaches out sideways from its lower half. It stands out even among the oaks around it. The app named it "A tree near Taasinge", but the fix is on Langeland, about 500 m east of Tranekær Slot and 14 km from our Tåsinge oak, so it is its own place rather than a second Tåsinge tree. Access comes from VisitLangeland: the castle grounds outside the moats are open to walkers all year. The reader sent no species, age or girth, so the species is Oak (Quercus sp.) and the page asks readers for the rest. Filed as November, the photo's own month. The place has an intro, question fields and three FAQ, and city_names.py was run. With one tree it stays a tree page under PLACE_PAGE_MIN_TREES.
- Left alone: 3c544597 (our own account, no photo on disk). There were no open reports, feedback or tips, and reader_words had nothing to place. preflight 0, i18ncheck clean, qa source clean.

## 2026-11-24 reader judge: a register champion poplar in Amsterdam live, a reader's golden ginkgo now leads in Verona

- **Amsterdam, ams_041, The Canadian Poplar of Entrepothof** (app, sighting ca3121a2, GPS from the photo): several heavy, leaning stems on a bank by the waterside path in the Oostelijk Havengebied, photographed bare in November. The city's Bijzondere Bomen register (no. 486309) is 25 m away and lists it as planted in 1930, with a 585 cm girth and the champion-tree flag. That planting year matches the reader's "96 years". The girth comes from the register and is stored as `girth_cm`. The Dutch overlay has the tree as Canadapopulier, the name already used for ams_027. Both meta lines now count 27 more trees. Filed as November, the photo's own month.
- **Verona, ver_003 ginkgo**: the reader's full golden portrait (fbbb5d62) is now the lead photo, and the Commons photo has moved behind it. The same reader's 2024 shot (1dac0633) is in the strip.
- **Verona, ver_001 cedar, held**: the same reader sent two night photos from Piazza Bra. bf974f50 shows a tree wrapped in Christmas lights, and the lights hide leaf and bark, so we can't tell whether it is the cedar. Held. b11a2e87 shows a deciduous tree in autumn leaf, so it is `other_tree`. Its new lead is held `doubt_location` because the coordinate is where the phone sent it from, 600 m away. hold_reply found no submissions row for it, so no mail went.
- **Verona, ver_011 mulberry**: 54cf46dd was rejected as a duplicate. Its four files have the same checksums as sighting 2cbeafcc, which is already live.
- Left alone: 3c544597 (our own account, no photo on disk) and the old `mine` leads. No open reports, no open feedback, reader_words clear. preflight 0, i18ncheck clean, qa source clean.

## 2026-11-24 reader judge: two readers' trees live, a Naples palace-garden fig and a hollow strangler fig in Khao Yai

- **Naples, nap_032, The Moreton Bay Fig of the Palazzo Reale Gardens** (app, sighting 8bea95ca): the photo is a close shot of the fused grey trunk, with aerial roots and a long pale palace front behind it. The reader first dropped the pin by hand near Lago Patria, 20 km out of town, then moved it four times themselves (reports 1000142 to 1000145) and ended in the Palazzo Reale gardens, which fits the palace in the photo. Because it was placed by hand the pin is approximate, and the story says so. The reports are closed `holds`, with no mail: these were moves on their own new tree. The Naples FAQ and the Italian overlay now count 25 trees, and the overlay has the new tree (ficus magnolioide). Filed as October, the photo's own month.
- **Khao Yai (new one-tree place), kya_001, The Hollow Strangler Fig of Khao Yai** (app, sighting 55890f31, GPS from the photo): a giant strangler fig, hollow where its host tree once stood, with a person at its foot for scale. The reader's note is quoted ("There used to be another tree in the middle"). Their 500 years and 30 m girth are given as their own figures. Species is Fig (Ficus sp.), and the page asks readers which fig it is. The access line says Khao Yai charges an entry fee and that some trails need a ranger or guide. The place has an intro, question fields and three FAQ; city_names.py was run.
- Left alone: the 38 other waiting leads are all `mine` (our own account), and 3c544597 has no photo on disk. There is no open feedback and no tip to judge. reader_words is clear. preflight 0, i18ncheck clean, qa source clean. The congratulation mail goes from deploy.yml once the pages are live.

## 2026-11-24 night run (retry, window 12:57): nothing shipped, rebase repaired

- An earlier attempt had left three unpushed commits that conflicted with the reader judge's (lisbon.json photo note, LOG.md, reader-words-done.json). Resolved keeping the judge's approved note and both sets of lines; pushed. No claims standing.
- Shelf re-checked: 4 READY leads (under the six-tree floor), 1 unpublished verified tree (taiwan, near a live tree, outside focus). Own research is paused, so no verify pass. Nothing to dispatch; the window found no work the rules allow.

## 2026-11-24 reader judge: a second reader photo of the Lisbon pohutukawa; Girona ambassador question

- **Lisbon, lis_038, The Pohutukawa of Campo Santana** (app, sighting c34cee42): a wide daylight view of the garden, with the pohutukawa's leaning stems and its hanging red root mats in the middle. It is this tree (species and recognition line match), so the photo goes into the gallery behind the current reader lead, which shows the roots closer and which Hidde had picked. Filed as November. The pin catch-up hit an HTTPError, which does not matter here because the pin is already a confirmed GPS fix.
- **Girona, feedback 1603** (mail reply from the reader who added gir_008): they don't know the tree's age yet, and they ask what being an ambassador would involve before saying yes. Closed `needs_hidde`. A suggested answer is in drafts/reply-reader-1603-2026-11-24.md (mailcheck clean). No badge yet, because they have not said yes. reader_words row 1603 closed: it is a question to us, with nothing to quote.
- Left as it was: the 37 waiting leads in _sightings.json are all `mine` (our own account), so they are not readers' trees, and none of their photos is on disk. Lead 3c544597 is one of them. No open reports. preflight 0, qa source clean, i18ncheck clean.
## 2026-11-24 night run (window 12:57): quiet, nothing to write

- Rung 1: reader backlog empty. Read 12 new tree notes, none on the closed list, marked seen. Left lis_038's photo and the Amsterdam lead to the reader judge, as the rule says.
- Rung 2: health.py clear (live-pages light GREY only because gh is unavailable here). Code-audit SPEED and CODE rows all fixed.
- Rung 5: own research is paused. Of 382 "awaiting a writer" trees only one is unpublished (taiwan, outside focus, claim refused); the rest are stale research files. 4 READY leads (leamington-spa 2, york 1, guimaraes 1) are under the six-tree floor for a write pass, so not dispatched.
- Depth: `reader_words.py` showed one row (feedback 1603, no tree words), marked done. `recognise.py --stuck` empty.
- No trees added.

## 2026-11-24 reader judge: two readers' trees live (Verona mulberry, Ota zelkova)

- **Verona, ver_011, The Silk Mulberry of Ca' di David** (app, sighting 2cbeafcc): an old pollarded white mulberry splitting low around a hollow, by a country road on Verona's southern edge. The reader's words go on the page quoted (silk farming), and their 120 to 130 years and 320 cm are stated as theirs. The pin is approximate: they placed it by hand, then moved it twice after sending (reports 1000140/1000141, same account), and their last spot is used. Those two reports are closed `holds` with no mail, because they were part of adding their own tree. The tree is behind a wire fence, so `access` says to look from the road. Lead photo (May, the photo's own date) plus two strip frames. Verona's counts are updated in English and in the kept Italian overlay, whose title no longer says 10.
- **Ota (Gunma), otg_001, The Great Zelkova of Kanayama** (website tip 1598, new one-tree place, so no place page): a huge spreading zelkova in autumn colour at Nitta Shrine on the Kanayama Castle summit. Sourced from Gunma Prefecture's Kanayama walking guide ("樹齢800年とも伝えられる「金山の大ケヤキ」") and Ota City's landscape plan. The pin is at the shrine and approximate, with the photo filed as November from the autumn colour. Its girth of 680 cm is the reader's.
- Left as it was: lead 3c544597 (Amsterdam) is `mine` (our own account) and its photo is not on disk, so the run did not judge it.
- No feedback waiting, and reader_words was empty. preflight 0, qa source clean, i18ncheck it/verona clean.

## 2026-11-24 session: Search Console back, under hidde@ancienttrees.app

Google disabled the old Gmail, which killed the GSC and GA refresh tokens (token endpoint 400). Search Console: Domain property ancienttrees.app added under hidde@ancienttrees.app, verified automatically by the existing DNS TXT, all 16 months of history there. Cloud project "Ancient Trees" (ancient-trees-515618): Search Console API and Analytics Data API enabled, Desktop OAuth client "Digest" made. New GSC_CLIENT_ID / GSC_CLIENT_SECRET / GSC_REFRESH_TOKEN minted with `scripts/ga_auth.py --gsc` (new flag), in ~/.ancienttrees-gsc.env and the GitHub secrets; a test read 14 to 22 Nov fine. Google Analytics: the old property could not be handed over, so a new GA4 account "Ancient Trees", property 565667139, web stream G-QQ8TM0E6KY (Netherlands, euro, every optional data-sharing box off). site-config.ts and ga_report.py point at it, GA_* token remade and in GitHub, a test read answers (empty until visitors accept the cookie bar). History before 2026-11-24 stays in the old property; week-on-week visitor numbers in the digest are not comparable for about two weeks.

## 2026-11-24 night run (window from 11:55 UTC): nothing to ship

Rung 1: no reader backlog; read the 11 new tree notes, none on the closed hide list, marked seen. One unmapped reader photo (3c544597, Amsterdam) is the reader judge's. Rung 2: health.py flagged the 11:32 build failure, but the India and South Africa description fix and later builds were already running; no new fault found. Code audit has one open row, a UX row (not a run's). Own research is paused; `reader_words`, `recognise --stuck` and enrich are empty; pagegaps only lists species pages under the strict cut. The 4 READY leads (Leamington Spa, York, Guimaraes) only have a verify brief, not a write path, so nothing was written. Nothing committed except this entry.

## 2026-11-24 reader judge: a reader's photograph leads the Rome cedar

- **Live**: a reader's own photograph of The Cedar of Celimontana (rom_008, Rome) from the lawn path, whole tree, tiered cedar boughs, 21 m from our pin. It is now the lead (unique to us), the Commons picture behind it; filed under November. Verdict `add` through sightings_publish.py; the reader's mail went with `--send`. The pin catch-up could not read coordinates (HTTPError); the pin is confirmed, so nothing to move.
- **Left**: lead 3c544597 (Amsterdam, unsure between it and the Stationsplein elm) and 37 older Japan/Baarn leads are our own photographs (`mine`), never auto-published, and their files are not on this machine.
- No open reports, no unjudged tips, no feedback without a verdict, no reader words waiting. qa source, preflight (0 problems) and i18ncheck clean.

## 2026-11-24 session: build 6 prepared, and a test that reached Hidde's phone

- **Breakage, caused by this session**: `android_walk.py` (ButtonWalk on three screens) ran at about 12:35 with no emulator running and Hidde's Samsung on the USB cable. adb took the phone; the script found "another build's signature", uninstalled his Play copy of `app.ancienttrees.android` and installed a debug build (firstInstallTime 12:36, DEBUGGABLE). Nothing of his is lost on the server (rule 11: nothing a person does lives on the device); he has to install the app again from Play and sign in.
- **Fixed so it cannot happen again**: the emulator lock (scripts/emulator_lock.py), which every installing script takes, now pins ANDROID_SERIAL to a running emulator and refuses when only a phone is attached or ANDROID_SERIAL names one. Tests in scripts/test_emulator_lock.py (6, pass).
- **Android CI red since 11-22, read**: ButtonWalk's Discover saves and "Another maps app" did not repeat locally (both passed); map-pin could not be judged (the run was on the phone, screen off). Spacing failed on the profile flag and the Worth the visit count because data/ios-frames.json was from 11-12, before both changed on both phones; refreshed today from an iPhone 17 Pro appfit run (40 screens, 0 findings).
- **Build 6 not built**: Android moved to a new Play account and package (`app.ancienttrees.map`, entry below) the same hour. The first upload there waits on Hidde's ID check, so the bundle is built when the account is ready, from main as it stands then.

## 2026-11-24 session: Android moves to a new Play account

- **What changed**: Google disabled the Gmail account that owns the old Play developer account (policy mail of 23 Nov to the recovery address; appeal blocked at the SMS step on every phone). Hidde chose to start over: a new personal Play developer account **Ancient Trees Map** (id 6289749847935270102) under hidde@ancienttrees.app, non-trader, created today. The old name "Ancient Trees" stays taken by the old account. The sign-up names the old account honestly ("can't verify", with a short explanation).
- **The app**: applicationId is now `app.ancienttrees.map` (Hidde's pick); the old `app.ancienttrees.android` stays bound to the old account. Scripts, the tester link in mailcheck and drafts/android-test-invite.md follow. assetlinks.json carries both packages; the new app's Play signing fingerprint is added once Play shows it.
- **Later the same day**: trader status saved (non-trader); ID and address proof uploaded, Google is checking. Android device check done: Play Console app on the Samsung (installed remotely from play.google.com, since the phone's Play Store said "no internet"; the phone was stuck in Safe mode, turned off over adb from its own notification), signed in as the Workspace address, "Device checks complete". Left: Google's ID verdict, then the phone number.
- **Testers (Hidde, same day)**: "laat de oude testers lekker in hun huidige build zitten en met rust": the 171 on the old Play list get no mail about the new app. "en dan mailen we gewoon een batch nieuwe": once the new app exists, the ~680 unsent wave 3 invitations go out with the new tester links (the batch file still carries the old group and app.ancienttrees.android links and stays `on_hold` until then), Resend only, after Hidde has seen the text. Signed bundle built for the new package as build 6 (Hidde: "versie 6"; carries everything since build 5, such as the empty species search line): out/play/ancient-trees-0.1.0-6.aab (manifest checked: app.ancienttrees.map, upload key 4F:42:47...). Walked signed out on the emulator (android_release_walk.py: map, Discover, My trees, a tree page; no crash; screens looked at in out/play/walk/). Sign-in returns through ancienttrees://auth-callback, so the package change does not touch it; https links into the app wait for the new app's Play signing fingerprint in assetlinks.json.
- **For Hidde**: tick the trader declaration and Save, upload your ID, sign in to the Play Console app on an Android phone, verify the phone number once ID is approved. Then the store page, forms and closed test (12 testers, 14 days) start again. Never both apps public at once.

## 2026-11-24 session: the repo moved to hidde-ancient-trees

- **Live**: github.com/hidde-ancient-trees/ancienttrees (and ancienttrees-open). The old account (burgmanshidde-ancienttrees) signs in with the blocked Google account, so the repo, its secrets and every run hung on a login that could vanish. Transferred through the API with the old account's gh token (no sudo code was asked), accepted by Hidde on the new account. All 23 secrets, the Pages settings (cname ancienttrees.app) and the github-pages environment came along; hidde-ancient-trees is admin, the old account stays a write collaborator.
- Owner name and commit identity switched in workflows and scripts; supabase/reader-judge-trigger.sql re-applied through the Management API with the new URL; Hidde put a new fine-grained token (contents write, this repo only) in the Vault as `github_dispatch_token`; a test dispatch from Supabase got 204. Claude GitHub app installed on the new account by Hidde. The Mac's gh and git push as hidde-ancient-trees.
- **Also today**: two park titles over the 60-character cap had stopped every deploy since 09:13 (Barcelona from the night run's park intros, and Brooklyn); shortened.
- Not moved: the org `ancienttrees` (old account the only owner, empty) and `SELF_DISPATCH_TOKEN` (an old-account token, inert while self-chaining is off).

## 2026-11-24 session: Joanna answered; Nathalie's mail attachment never used

- Sent via Resend on Hidde's "joanna mag eruit": a short thanks to Joanna (Leamington ambassador) for the promised photos and for looking at the holm oak (drafts/reply-joanna-leamington-2026-11-24.md).
- Nathalie's Shanghai mail carried one attachment, IMG_7535.png (likely a screenshot, not her own photo, per Hidde). It was never opened or used: the inbox script reads no attachments, and sha_002 shows only her own app photograph (GPS on the campus, taken this month).

## 2026-11-24 session: Waste Magazine article sent

- Sent to Waste Magazine on Hidde's "prima verstuur": the Spanish article as a Word file (drafts/waste-article-2026-11.md turned into a document, 973 words, with bio and photo credits) and seven open-licence photos (drafts/waste-photos/, 8.8 MB). The cover mail is in the Crann shape (drafts/reply-waste-magazine-2026-11-24.md).
- Waste's mail of 11-20 sits in the blocked Gmail, so its Message-ID can't be read, and the 10-27 message it would answer had already been replied to. scripts/outreach_send.py now takes `second_reply` (a sentence saying why) for a deliberate second answer to one message, still once per batch, so the mail went in their thread and outside the outreach cap.
- Potential: Waste is a web-only nature magazine from Granada, around since 1997, and it publishes no audience numbers. Expect a modest number of visitors and one good Spanish link.

## 2026-11-24 reader judge: "Bella", a registered oak near Arezzo, held over its photo

- Held e604000d, a downy oak a reader calls "Bella" at Ceciliano, Arezzo, as `doubt_photo` (no mail, same as the Tsagarada plane on 11-22). The picture is a cropped phone screenshot: 1206 px wide in a 4:5 social-media crop, no camera data, a filtered look, and summer leaf under a November date. The tree itself is real and special. The official Italian register lists it 41 m from the reader's hand-placed pin: Albero monumentale d'Italia 01/A390/AR/09, 570 cm round, 24 m tall, at "Casa Fredda, Loc. Ceciliano 82". That address is a house, so a register-backed page would still need a life check and a check that the tree can be seen from public ground. A photo the reader took themselves would also put it live.
- Not judged: 3c544597 (Amsterdam, our own account) still has no photo on this machine.
- There were no reports, tips, feedback or readers' words waiting.

## 2026-11-24 reader judge: the golden ginkgos of Formigine live

- Live after the next deploy: formigine/frm_001, The Golden Ginkgos of Villa Gandini (Formigine, near Modena). A reader sent four autumn photographs of the two ginkgos on the villa's south side, which the comune's tourism page calls the park's symbols. Lead photo is the pair in gold over the pond; the other three are in the strip. The pin is approximate because the reader placed it by hand. Age (135 to 150) and girth (457 cm) are the reader's. Best time is November. It's a one-tree place, so it has no place page.
- Rejected 2414d848 (Grubb Road white oak) as a duplicate: it's the same picture the session already made wtn_003's lead today.
- tip:1533 is the app's row for the Varese ginkgo already live (var_002); verdict publish, nothing to add.
- Not judged: 3c544597 (Amsterdam, our own account) has no photo on this machine. Older leads still marked `lead` (Nara, Kyoto, Taketa, Kagoshima, Tokyo, Baarn: mostly our own account's from September and October) have no files here either, so they wait for a run that has them.
- No open reports, no open feedback, no reader notes to quote.

## 2026-11-24 night run 10:01 UTC: build fixed, nothing else to take

- Rung 2: every deploy since the title fix failed on one more over-long meta description, /parks/botanic-garden-cambridge (164 chars, cap 155). Shortened it (b09c0e2dd, pushed). Preflight 0 problems; the deploy after it was not watched to green by this run.
- Rung 1: the one waiting sighting (3c544597, Amsterdam) has no photo on disk and wtn_003 was already fixed in 8e10faa79; reader work belongs to the reader judge, so left alone.
- Own research is paused, so no verify, scout or refill. No trees added.

## 2026-11-24 session: no database backup has ever been made

- **Found**: db-backup.yml has failed every day since it was built (2026-11-04): the secrets `SUPABASE_DB_URL` and `BACKUP_PASSPHRASE` were never set, so no `ancienttrees-backup-*` artifact exists. Accounts, submissions, notes and readers' photographs exist only in Supabase.
- **Decided (Hidde)**: Pro stays this month (this month's egress overage cannot be undone; Pro adds Supabase's own daily backups, 7 days). Back to Free is mid-December's call on the measured egress after the 11-23 cache fix (~3.5 to 4 GB of 5 expected).
- **Still needs Hidde**: the two secrets (BACKUP_RESTORE.md "Setup, once"). Then a session runs the workflow, checks the artifact, and keeps a copy off GitHub.
- **Laptop backup live** (Hidde: "maar hebben we dan niet nog steeds een probleem als ik deze laptop kwijt raak?"): `scripts/laptop_backup.py`, nightly at 03:15 from ~/Library/LaunchAgents/app.ancienttrees.laptop-backup.plist (log ~/Library/Logs/ancienttrees-laptop-backup.log). One AES-256 archive (openssl, pbkdf2) of the ~/.ancienttrees-* key files (Android upload key included), changed, untracked and gitignored private files under data/ and drafts/, and Claude's project memory: 756 files, 81 MB, into "Ancient Trees backup" in Drive under hidde@ancienttrees.app (not the koos.agency Drive, which ends with his job); the last 14 kept. Passphrase in the Mac keychain (service `ancienttrees-backup`), typed by Hidde, never seen by a session. Tested: a run from the shell and one from launchd wrote archives, `--verify` opened them. Drive refuses to overwrite or delete a file it is still uploading, so each archive has its own timestamped name and a busy file is left for the next night.
- **Database backup live, first one made**: Hidde set `BACKUP_PASSPHRASE` (same as the laptop's) and `SUPABASE_DB_URL` (shared pooler, password reset today). Run 45467272784: database.sql 22 MB, 59 tables with data, 1,697 stored files (86 avatars, 1,611 reader photos, 1,439 MB), one 1.4 GB gpg archive `ancienttrees-backup-2026-11-24`, kept to 2027-02-22. The first try copied one file at a time and ran into the 40-minute limit; now eight at a time and 90 minutes (9dc08e7de), which took 7 minutes. For the mid-December Pro call: reader photos are 1.4 GB, past Free's 1 GB of storage on their own, and each full backup is 1.4 GB of egress every 28 days.

## 2026-11-24 session: sponsor button back on About

- Live after the next deploy: /about has a "Sponsor this project" button under Hidde's signature, straight to ko-fi.com/ancienttrees (event `about-sponsor`), after the first Ko-fi sponsor came in. It sat there on 2026-10-14 and went in that afternoon's rewrite. Looked at on the live page with the button injected, 375px and desktop. Footer and /sponsor unchanged; the app stays without it (Apple 3.1.1).

## 2026-11-24 session: inbox read, three replies drafted, Joey's oak fixed

- Live: willistown/wtn_003 (White Oak on Grubb Road) leads with the reader's unaltered photo showing the old No Trespassing sign on the trunk, at their request by mail; the story's bicycle now stands on its kickstand; the recognition line names the sign. The reader judge had rejected that photo as a duplicate.
- The inbox reader works again: the Workspace app password is in ~/.ancienttrees-mail.env (the old value was not an app password).
- For Hidde: drafts waiting for his yes: drafts/reply-azerbaijan-tourism-2026-11-24.md (data list + accepting their meeting), drafts/reply-felicity-brisbanetimes-2026-11-24.md (call at her 7am, his 22:00), drafts/reply-joey-willistown-2026-11-24.md.
- No reply needed: Kat (Houston, closing note), Loïc (Paris roots fact already in the story), the Patagonia mesquite and the Shanghai ginkgo (judge mailed them live), Volkskrant (Hidde answered).

## 2026-11-24 session: no batch can reach a Google mailbox any more

- **Breakage found**: the "on hold" for the Android wave 3 invitations (2026-11-23) lived only in words; the batch file kept `approved_by_hidde`, so the night run's "Continue an approved outreach batch" step sent another 100 today through the Workspace mailbox (route gmail). about 380 of 777 are still unsent.
- **Fixed**: the batch is `on_hold` (pushed to the private store, read back). And in code: outreach_send.py opens mailer with `google=False`, so every batch goes through Resend only; what Resend will not take waits, it never falls to Gmail or Workspace. Tests in scripts/test_mailer.py (three new cases, all pass). Hidde, 2026-11-24: "lijkt me een slecht idee".
- **And then all of it** (Hidde: "Ja, doe het"): `GOOGLE_ROUTE = False` in scripts/mailer.py, so the single expected mails too (photo-live, ambassador, contributor replies, about 30 a day) go through Resend; no script sends through Google, which now sees only what Hidde types. Sign-in mail already went Resend first. CLAUDE.md mail route rule updated; test_mailer.py passes.
- **Inbox reading widened**: scripts/outreach_inbox.py now opens mail to any @ancienttrees.app address (the Workspace mailbox is all project mail; mail to hidde@ was counted and never opened). Martin Winn (London ambassador) gave the Morden Hall mulberry 200 to 300 years: on the page as a reader's estimate (lon_054). Replies drafted for Felicity (Brisbane Times), Heybat (Azerbaijan Tourism Board), Martin; waiting for Hidde's word.
- Sent via Resend on Hidde's word: Felicity (Brisbane Times, questions by email instead of a call), Martin Winn (London). Drafted, waiting for his yes: Heybat (Azerbaijan, his own words: no meeting now, a marketing proposal by mail; supersedes drafts/reply-azerbaijan-tourism-2026-11-24.md), Kat (Houston, a kind word), Loïc (Paris), the Patagonia mesquite and Nathalie (Shanghai), each with the live page. RedoMap left unanswered on his word ("meer heeft aan ons dan wij aan hem"), recorded in drafts/HIS_VOICE.md.
- CTV: Devika mailed via Resend in her thread to resend her interview time to hidde@ancienttrees.app; her answer may sit in the blocked Gmail (ImprovMX forwarded info@ there until the MX switch on 11-23).

## 2026-11-24 reader judge: the Pine Tree Way mulberry in Lewisham is live

- **Live**: london/lon_056, The Pine Tree Way Mulberry, a black mulberry on the corner of Pine Tree Way and Elmira Street, Lewisham, from a reader's app photograph (sighting 5ecc87a6). Morus Londinium confirms it (heritage and notable, 9 m, 126 cm, probably planted in an 1860s boys' school playground, about 150 years); the reader's 160 years and their note stand beside it. Their pin was placed by hand, so approximate. The photo has no camera data, but the app strips that from every photograph, and it is not the picture Morus Londinium publishes.
- **Not judged, no file on this machine**: 3c544597 (Amsterdam, sent "not sure which tree", near ams_032): the photograph is still not on disk, so it waits for an intake that can fetch it. The 37 older waiting leads (Japan from September, Baarn and Amersfoort from October, several of them our own account's shots) have no photograph on this machine either, so they were not re-judged under the closed list; they need a run that fetches their files.
- No open reports, no feedback, no tips waiting. reader_words: nothing new to quote.

## 2026-11-24 night run (08:42 window): page gaps, nothing else on the shelf

- Rung 1: the reader judge owns the two unmapped sightings (3c544597, 5ecc87a6); I only read and marked seen 11 tree notes (none hidden). Health: only red was 6 of 12 knocks delivered (GitHub cron). Own research is paused, enrichment and recognition lines have nothing left, READY leads are already published, so rung 9.
- **Written, from each subject's own trees:** country intros for India (11 trees, 8 places) and South Africa (3 trees, with a map_focus box); park intros for Boston Public Garden, Cambridge Botanic Garden, Barcelona Jardi Botanic Historic, Brooklyn Botanic Garden, Bois de Vincennes, East Hampton Dayton Arboretum and Préfargier (Laténa). Not shown to Google (strict cut), but the pages exist for readers and Bing.
- **Left, and why:** Arnold Arboretum shows as a gap only because 9 trees sit under the name "Arnold Arboretum" while the existing park file is keyed "Arnold Arboretum of Harvard University" (6 trees); merging the two names changes a live page's counts and wants a build to check. `pagegaps.py` also still lists Préfargier because its slugify turns "Laténa" into lat-na; the site's slug is la-tene, which the new file uses.
- preflight's one failure at the time (sighting 5ecc87a6 without a closed reason) was the reader judge's and is cleared by its mulberry entry above. No site build run.

## 2026-11-24 session: a November photo no longer lands under Winter

- **Seasons row fixed** (Hidde, on the Rungis lime: "dit gaat niet goed qua seizoenen"). The reader's green November photo sat under Winter. The reason: the lime's phenology file says it colours in October only, and `seasonOfMonth` in site/src/lib/seasons.ts filed every month after the colour months as winter. Now a September to November photo after the colour months stays autumn; winter is December to February. A photo before the colour starts still goes to summer (the 11-03 Canton Park rule). The feed carries `season`, so the app follows on the next deploy. New check `check_autumn_months_never_file_as_winter()` in qa.py. Rungis now shows both photos under Autumn and Winter as an empty ask.

## 2026-11-24 session: readers' trees go live about 23 minutes sooner

- **Where the hours went** (Hidde: "waarom zat er dan zo vaak een gat van 4h tussen gister?"). The reader judge was never the slow part. Every tree submitted on 11-23 got a judge run within minutes, and that run finished 15 to 25 minutes later. The deploy after it took 1 to 2 hours. The build itself takes about 47 minutes, 28 of them QA, and a deploy also waits behind the one already running. The gaps of about 4 hours between trees were mostly gaps in what readers sent, overnight in both Europe and the US.
- **Fixed** (5eb0a042d): one QA check, `check_one_tree_places_have_no_question_page`, took 1,395 of QA's 1,663 seconds. It ran one regex per small place on every one of 29,121 pages. It now reads each page once: `links_to_small_question()`, with the same answer on 19 test hrefs, old against new. That should save about 23 minutes on every deploy. The next deploy's "qa timing" lines will show whether it did.
- Left alone: another session's unfinished `check_one_place_head` in scripts/qa.py. PlaceHead.astro is not committed yet, so that check stays out of this commit.

## 2026-11-24 session: two readers' trees Hidde put live, and the judge's lesson

- **Live**: florianopolis/fln_003, a fan palm in the Córrego Grande park whose crown stands above the forest (held `not_special`; Hidde: "ik vind die palm in florianopolis wel vet waarom niet?"), and split/spl_006, the cypress of Šimun Tudor on Marjan with its 1930 plaque (held `doubt_location`; Hidde: "this is sort of a special tree no?"). Both pins approximate, both readers' words or plaque on the page.
- **Lesson in BRIEF_READER_JUDGE.md**: `not_special` is the rare verdict, a tree that stands out in its own setting is special; and a tree with its own plaque or sign on a path past our pin goes live instead of `doubt_location`.
- Hidde agreed with the other 16 verdicts on his page.
- **Also live: brussels/bru_036**, the golden tulip tree a reader photographed by the Solbosch beech (Hidde: "this also looks like a special tree", "het is er gewoon een paar meter van"). The app stored bru_034's pin with the photo, so that is its approximate pin. preflight's `reader_found()` now also takes `SENT_FOR_PIN` (a pin from the tree a photo was sent for) beside a hand-placed one, per his 11-17 rule (a GPS fix or a photo). French overlay entry written, count 34 to 35.
- **For Hidde: a reply to reader 1433** (Tsagarada, the snowy night photo) asks whether they took it and may we use it: drafts/reply-reader-1433-2026-11-24.md, mailcheck clean, waits for his yes.

## 2026-11-24 session: resends no longer reach Hidde

- Hidde on 14 resends on his readers' trees page (the same photograph sent again): "A mag je afwijzen en niet meer vragen". Filed as agreed, and `inspect_readers.is_duplicate()` now keeps any verdict that names a duplicate off his page. 20 trees remain for him (closed-list holds, not-special calls, real doubts).

## 2026-11-24 session: the iPhone's own crash reports can ring

- **Why build 41's crashes never showed in the app's own reports**: two reasons. Build 41 predates the iPhone's exit watcher (added 11-16), so it sends none; build 42 will. And scripts/app_crashes.py dropped every report without a reason, which is every iPhone report (iOS cannot tell a crash from a flat battery), so even build 42's would have been lost. Now an iPhone exit on screen is kept, signed by the last thing the app measured, and rings once two phones end the same way or one phone twice. Both phones' reports also ring until answered, not 48 hours. Test: scripts/test_app_crashes_ios.py.

## 2026-11-24 session: four leaks in bug handling closed

- **An iPhone crash rings until it is answered**, not for 48 hours. Four build 41 reports had expired unread while GitHub dropped half the night's knocks. An answer is a fix build, a server remedy, or `answered_at` with what was looked at; a newer report rings again. The two crashes with no cause found are now recorded that way in data/crash-fixes.json.
- **iPhone hangs ring** when one kind repeats or lasts 5 seconds; one short hang stays quiet (the 11-21 launch hang). Test: scripts/test_crash_single.py.
- **A reader who says something is broken is a bug, never Hidde's call**: `feedback.py --close <id> bug <bug-id>` names the code-audit row, which is rung-2 work. Report 1491 (the country) moved off his list to its bug row this way.
- **The weekly code review reads Android** (BRIEF_CODE_AUDIT.md); it had only read the iPhone and the website.

## 2026-11-24 session: build 41's crashes looked into, the map crash fixed, single iPhone crashes ring

- **The map crash during a pan is fixed for build 42** (one phone, iOS 27.2.1, 11-20). MapLibre stopped the app when a layer of tree pins was added under a name the map already held. Layer names were a counter per map that can start over while the old pins are still drawn. Names now carry the map's own number (`MapLayers.layerID`), and every pin layer removes a same-named one first (`addFresh`). Test: `PinRuleTests.aStateMadeAgainNeverReusesALayerName`. Looked at in the simulator: pins and dots draw as before. For Hidde: next build carries fix for AncientTrees+0x35fccc.
- **Two crashes have no cause found** and are answered here only: data/crash-fixes.json takes no entry without a fix build (qa: it would quiet a live crash on build 41), and both are past the 48 hours health.py reads, so nothing rings for them. If either signature comes back, read it at once: AncientTrees+0x2409a0 (closure #4 in MapTab.body, while a TreeMap is torn down) and an empty stack. On 11-16 the app crashed while closing a map, on memory already freed, with no line of ours. On 11-15 the stack was empty.
- **The 11-21 hang was the system**: 2 seconds at launch preparing graphics, on an iPhone 12 in low power mode. Hangs are not checked automatically yet.
- **One iPhone crash now rings health.py** (e83d9c94d). Before, the check waited for 3 of one kind within a day, so these four rang nothing. The digest's day by day also gained Photo likes and splits Feedback into its kinds (e3d87efc4).

## 2026-11-24 session: the night run leaves readers to the judge, and stops sourcing contacts while a batch waits

- **What changed** (Hidde, "Alleen 1 en 2"). Readers' photographs, trees, reports and feedback no longer start a night window. The reader judge already handles them within about 15 minutes, and two agents were judging the same rows. The switch is `READER_WORK_STARTS_WINDOW = False` in scripts/claude_gate.py. Notes on trees still start a window, because only the night run reads them. Anything the judge misses goes red after 24 hours (reader_backlog.py) and is rung-2 work in the next slot.
- **Contact and press-desk sourcing pauses** while sent_drafts.py lists a batch as open or partly sent. Today that is the Guardian press batch (31 of 39) and the Android wave 3 invitations. CLAUDE.md rung 4 carries the rule.
- **The digest's contacts line is gone** (Hidde: "contacten qua outreach? die mag dan weg"). That line gave the addresses ready to mail per group and the "no new contacts in two days" warning. Switch: `OUTREACH_READY_LINE = False` in scripts/daily_digest.py.
- **Kept, not changed**: the two-hour knock and its four agent slots a day (point 3 of the proposal).

## 2026-11-24 session: a waiting reader judge no longer redoes the run before it

- **Breakage fixed**: reader-judge.yml and nightly.yml now check out `ref: main`. Before, a dispatched run that waited in the queue started from the commit of when it was *created*, so it treated the previous run's work as still open. The 03:53 run re-judged the Colchester cedar for 15 agent minutes that way. The runs never truly overlapped: the concurrency group already ran them one after another.
- The many "cancelled" reader judge runs (201 in a week) are harmless. They are waiting runs replaced by a newer waiting run when a burst of Supabase triggers arrives, and none of them did any work.

## 2026-11-24 session: night runs stop looking for new trees of their own

- **What changed** (Hidde: "mss beter om de nachtruns niet langer nieuwe bomen te laten zoeken nu we zoveel input krijgen", then "Ja, stop het"). From 11-21 to 11-24 the night runs ended mostly on walls (Fort Worth, Braga, Miami, Sheffield and Birmingham came back dry) while readers sent dozens of trees, in the US and UK too. So there are no more verify passes, register scouting or shelf refills for trees of our own.
- **What goes on**: rungs 1 to 4 (readers, health, corrections, outreach) are unchanged. Trees already verified on the shelf still get written (382 are waiting for a writer). A reader's or ambassador's tip is still finished: `passcheck.py --claim <place> --kind verify --tip "<whose>"`. After that comes depth on trees readers touched: their words, enrichment, recognition lines, code rows.
- **How**: the switch is `OWN_RESEARCH_PAUSED = True` in scripts/findable.py. passcheck.py refuses a verify claim without `--tip`. prepare.py --status prints no refill or scout directive and names the depth lanes instead. The nightly.yml prompt follows that block. CLAUDE.md rung 5 carries the rule.
- **Undo**: set `OWN_RESEARCH_PAUSED = False`.

## 2026-11-24 reader judge: the second Tsagarada reader's trunk photograph leads

- **Product**: The Plane of Agia Paraskevi (tsagarada/tsg_001) now leads with the second reader's photograph (sighting 17ff735e): the huge double trunk in its stone bed at night, with a person and dogs for scale. The first reader's lead moved into the gallery. A parallel run (4f6167146) had already taken the same reader's wide view (03cf52a9), the age note and the app's comma fix, so this run added only the trunk frame.
- No waiting leads, no open reports, no open feedback.

## 2026-11-24 reader judge: the Colchester oak is the Wivenhoe Whopper; an app age bug a reader caught

- **Colchester, cls_001**: a reader's two reports pointed to Woodland Trust Ancient Tree Inventory record 177493, the "Wivenhoe Whopper". Read it: pedunculate oak, lapsed pollard, alive, 9.10 m at 1.30 m, grid TM0306224237, 25 m from our pin, so the same tree. The page now has the local name, the register link, `girth_cm` 910 (the recorder's later 8.57 m in the story), the register as source, the register's access line, and "about 300 to 800 years, by readers' estimates". Intro, question answer and context, and FAQ follow it. Reports 1000136 and 1000137 closed `holds` with no mail, because they carry the reader's own words. Suggested reply in drafts/reply-reader-1000137-2026-11-24.md.
- **App bug found by a reader (report 1000138, Tsagarada)**: the tree page's Age field cut the age at the first comma, so "about 1,000 years" read "about 1". That hit 24 trees, iPhone and Android alike. The website and the data were right. Fixed in both sources (`Tree.firstAgeClause`, a comma between digits is no clause break), with AgeClauseTests.swift and AgeClauseTest.kt, and recorded with escaped.py. The tests were not run here (no Gradle or Xcode on this runner), so CI decides. Suggested reply in drafts/reply-reader-1000138-2026-11-24.md. For Hidde: the next build carries the fix for the "about 1" age on the tree page.
- **Tsagarada, tsg_001**: a second reader's night photograph from a balcony over the square went into the gallery behind the lead (`strip`): it shows this plane, but from further off than the current lead.
- Not judged: lead 3c544597 (Amsterdam, "not sure which tree", ams_032 named). Its photograph is not on this runner, so it is left for the next run rather than judged blind.

## 2026-11-24 reader judge: nothing new; a parallel run had the cedar first

- A second run picked up the same Colchester sighting (c3ef540c) and tip 1573. The run below pushed first, so this run dropped its duplicate commit. The only change kept: `taken_month_basis` on cls_002's new lead photo, which the other run had left off.
- No other waiting reader photograph, lead, report, feedback or words to quote. Sighting 3c544597 (Amsterdam, our own `mine`) is still not on disk.

## 2026-11-24 reader judge: a second photograph and the reader's figures for the Colchester cedar

- **colchester/cls_002, The Cedar near Clingoe Hill: a new lead photograph** (sighting c3ef540c, app). It comes from the same reader, 3 m from our pin, a step back from their first frame, and shows the whole crown with the sky above it, the low skirt of branches and the paved path. It is a better lead than the first, which cut off the top. Sent with `add` through sightings_publish.py, so the first photograph moved into the strip. The light score is WEAK, but it is a reader's photo in daylight and colour, so it ships. The second picture (needles and upright cones) confirms a true cedar.
- **The reader's figures are on the page as theirs**: a girth of about 555 cm and an age of about 155 years. The story's sentence "we have no girth or age" now carries them, and `age_estimate` reads "about 155 years, by a reader's estimate". Preflight caught a colon reveal in my first wording, and it was rewritten. Colchester has no overlay.
- `tip:1573` is the app's row for the cedar (sighting 9f5e1316), which is already live, so the verdict is publish with nothing to add.
- **Left for the next run**: lead 3c544597 (Amsterdam, 52.3972,4.8739, "not sure which tree") has no photograph on this runner, so it was not judged blind. The older waiting leads in _sightings.json (Japan and Baarn, mostly from our own accounts) have no files on disk either.
- No open report, no feedback without a verdict, and no reader's words waiting to be quoted.

## 2026-11-24 reader judge: a reader's cedar live in Colchester

- **Live: colchester/cls_002, The Cedar near Clingoe Hill** (sighting 9f5e1316, app). The photograph shows a big cedar on mown parkland whose trunk splits low into tiered, curving limbs, its lowest branches lying along the grass. The pin is the photograph's own GPS fix (confirmed), 199 m east of the Clingoe Hill oak (cls_001), sent by the reader who gave that oak its current lead photograph. The species is the reader's (Cedrus libani), which fits the habit; verify_notes says an Atlas cedar is possible. November photo month taken from the file. No register entry or encyclopaedia article nearby. Colchester now has two trees, so it gets a place page (PLACE_PAGE_MIN_TREES 2): the intro, meta, question_meta, question_context and FAQ are rewritten for two trees. Colchester has no translation overlay.
- Verdicts are recorded (`lead:` and `sight:` 9f5e1316 publish), and the lead and sightings-processed are marked published.
- No open report, no feedback without a verdict, no tip stub, and no reader's words waiting to be quoted.
- Sighting 3c544597 (Amsterdam) is still our own account's `mine` photo and still not on disk, so it was left alone.

## 2026-11-24 reader judge: nothing new waiting

- No reader photograph in the queue, no waiting reader lead, no open report, no tip without a verdict.
- Nathalie's mail reply (feedback 1572, "on university grounds, accessible from the street") closed `handled`: the previous run already put the Shanghai ginkgos (sha_002) live on it.
- Sighting 3c544597 (Amsterdam, near the Last Elm of Stationsplein) is our own account's `mine` photo, not on disk; left alone, never judged blind.

## 2026-11-24 write pass: nothing shipped, the writing pool is empty

- **0 trees written.** `passcheck.py --pending` holds no tree that needs a story. Every suggested file (wisconsin, washington-dc-2, us-photo-batch-1, wales-yews, somerset-dorset-yews, new-york-3) is fully published. The id-collision entries (bri_017, car_001, nyc_027, nyc_031, wol_001, cdl_003, lar_001, tro_001 to 003, sct_001) are all live under other ids by name. Taiwan's a28_001 duplicates alh_002.
- **The 4 READY leads are not ready**: `leads.py` marks them READY because nothing blocks them, not because they hold enough to write. Leamington's silver pendant lime has no pin and no size evidence. The Jephson Gardens conifer line is five species with no single tree to stand at. York's riverside plane (ambassador's what3words) has no source, photo or description, so 150 words would be invented. The Guimaraes Mexican cypress stands in Pacos de Ferreira, 15.7 km out, and is not checked alive or for access. Each needs a verify pass (or the York ambassador's photo), not a writer.
- Stale research files (all-published) can be deleted in a clean-up; not done here.

## 2026-11-24 night run 01:29 UTC: red deploy fixed

- **Rung 2, the site was not updating.** Every deploy since the Cardiff app-only trees went in died on one line: the Bute Park title promised "8 to Find" but the page holds 5, because the build skips app-only trees. Preflight counted all 8, so it passed. Title now says 5; `park_groups.renderable()` skips app-only trees like `treeIsRenderable`, so preflight now sees the same count. Preflight 0 problems; pushed (80f4da4f0).
- `gh workflow run deploy.yml` was refused (HTTP 403, integration token), so the deploy has not been re-run from here. For Hidde: dispatch Build and deploy once, or let the next knock do it, to confirm green.
- Not touched: iOS app red on schedule, the 1 unjudged sighting 3c544597 is our own `mine` photo (Amsterdam). No trees added this window.

## 2026-11-24 reader judge (third run): Travilah Oak gets a reader's lead photo, Shanghai's ginkgos live

- **Live**: shanghai/sha_002, **The Twin Ginkgos of Jiao Tong University**, Shanghai's second tree. It was held `not_public` on 11-23. The reader answered our mail (feedback 1570) that the campus can be entered from the street, so the lead was re-opened and published. Pin from the photo's GPS, age "about 200 years, by a reader's estimate", and the story asks what the inscribed stone says. Shanghai's intro and meta now name both trees. Their mail is not quoted (no yes asked); its fact is the access line.
- **Reader photo**: washington-dc/wdc_016, the Travilah Oak. The reader's summer photo of the whole crown from the split-rail fence is now the lead. The Commons photo moved into the strip. The app sent the same four files six times, so the five copies were rejected as duplicates.
- No open reports, no tips, no other waiting leads (3c544597 in Amsterdam is one of ours, `mine`).

## 2026-11-24 reader judge (second run): the Ngāhinapōuri plane re-judged and live

- **Live**: ngahinapouri/ngh_001, **The Plane of Stewart Reid Memorial Park** (Waikato, NZ), a new one-tree place. The run before held lead 48b2515d `not_special` because the site looked like a school field. The GPS fix in fact stands in Stewart Reid Memorial Park, beside the school. NZHistory: the land was given in 1946 in memory of pilot officer Stewart Reid and planted with 34 memorial trees, one per local man who served in WWII. The park's flagpole on its stepped base shows in the photo. The story does not claim this plane is one of the 34 and asks readers instead. Hidde, overturn it in judgements.json if a memorial park does not make it somewhat special.
- This run also judged the Langwarrin oak and published it ten minutes after the first run had. That duplicate was dropped in the rebase; the first run's lwr_001 stands.

## 2026-11-24 reader judge: the Macedon Oak of Cruden Farm, Langwarrin

- **Live**: langwarrin/lwr_001, The Macedon Oak of Cruden Farm (Victoria, Australia), a new one-tree place. A reader sent three photographs through the app: the whole oak, a wide shot with the farmhouse, and the National Trust plaque. The National Trust register and the Victorian Heritage Database list it (Quercus 'Firthii', 32 m tall in 2010, classified 1982). The reader had picked "Macedonian Oak (Quercus trojana)"; the page uses the plaque's name. Paid, booked garden entry. The id prefix `lgw` was already taken by Longwood, so the tree is `lwr`.
- **Held** `not_special`: lead 48b2515d, a mid-sized London plane in a row on a mown field (school-like buildings) in Waikato, New Zealand. No note, nothing sets it apart. No mail, since this is not a reason the reader can fix.
- **Not judged, photo not on disk**: lead 3c544597 (Amsterdam-west, 52.3972,4.8739, "not sure which tree"). sightings_inbox says to run the intake with the key. The older Japan and Baarn leads (mostly our own account) also have no file here and were left as they were.
- Reader words: submission 1414 (Tsagarada) closed with `--done`. It is a pasted travel text, and its figures are already on the page as the reader's.
- No open reports and no open feedback.

## 2026-11-24 night run: the Tsagarada plane, a reader-intake fix, five park intros and Vietnam

- **New reader's tree live**: tsagarada/tsg_001, The Plane of Agia Paraskevi, a new one-tree place on Mount Pelion, Greece. Submission 1414 (sent 2026-11-22 from the app) had an empty main photograph and three further ones, so no lead was ever written and it sat unjudged for two days (health's reader backlog went red on it). All three frames were viewed: the plane in its village square at night, lit from below, one great limb resting on a stone pillar. Pin from the photograph's own location (confirmed). Their note repeats a travel text, so it is not quoted; their figures (about 1,000 years, 14 to 15 m girth) are stated as theirs. The famous lead for the same tree is marked published. tip-1433 (another reader, a screenshot) stays held `doubt_photo`.
- **Fix**: `sightings_inbox.py` now reads a sighting whose main photograph is empty but whose further photographs are not (`promote_extra_photo`, `TestExtraOnlySighting`). Recorded as an escaped bug, closed with its test.
- **App bug row closed**: the country save (reader 1358). Its server fix is live since 2026-11-22; `scripts/test_flag_upsert.py` now guards the trigger file.
- **Page gaps**: intros for the parks Flamingo Gardens (Fort Lauderdale), Wright Park (Tacoma), Bute Park (Cardiff), Jardin des Plantes and Bois de Boulogne (Paris), and the Vietnam country page, each from its own trees. Arnold Arboretum still reads as a gap: its park file says "Arnold Arboretum of Harvard University" and the trees are grouped as "Arnold Arboretum"; left alone.
- **Dry**: San Francisco 13th verify pass, register exhausted, wall set 48h. Nothing on the shelf is writable: the "awaiting a writer" pile is stale entries and duplicates under other ids.
- **iOS app red**: the newest run's `look` job passed (appfit fixed); its `test` job was never acquired by a macOS runner ("not acquired by Runner of type hosted"), so it is GitHub capacity, not code. Nothing to fix; the next schedule retries.
- `gh workflow run ios.yml` was refused (HTTP 403, the runner's token cannot dispatch workflows), so the iOS re-run waits for the next schedule or a session.
- Amsterdam lead 3c544597 is still our own account with no file on this machine. Nothing sent to anyone; no Reddit.

## 2026-11-23 reader judge: Willistown grows to four with the Quaker meetinghouse oak

- **New reader's tree live**: willistown/wtn_004, The Meetinghouse Oak of Willistown, from the same reader as wtn_001 to wtn_003. Their photograph shows a tall, straight oak on the lawn of the Willistown Friends Meetinghouse in November. Its lower crown still holds brown leaves and its top is bare. The reader gives a girth of 400 cm and an age of more than 150 years; both are stated as theirs. The species is left as Quercus sp. The reader calls it a northern pin oak, but that is a Midwestern species, and the habit looks like pin oak, so the page asks readers which it is. Their note supplies the 1793 date on the east gable, the bigger oak felled for a building expansion and the buggy shed. All of it is in the story, partly quoted, with no bridge claim tying the planks to that oak. The pin is approximate because it was placed by hand. The photograph is filed under November, its own month. Their second photograph shows stacked planks, not the tree, so it stays off the page.
- **Willistown's texts** (intro, meta, question texts, FAQ) now say four trees. The place has no translations.
- No open reports and no feedback without a verdict. Reader notes are for the night run's rung 1. Amsterdam lead 3c544597 is still our own account with no file on this machine. The old Japan and Baarn leads in `status: lead` are owner-account shots whose files are not on this runner; they are left as they were.

## 2026-11-23 reader judge: the Laurel Hill Cutleaf Linden gets its first photograph and a better pin

- **Photo on a tree we map**: a reader's three November photographs of the Laurel Hill Cutleaf Linden in Philadelphia (phl_007, which had none). The lead shows the whole broad tree beside a cemetery drive, autumn colour starting. The two others go in the strip: the hollow, buttressed trunk under cut, lobed leaves (the cultivar's mark), and the crown beside the Sheppard obelisk. All three filed under November. The reader is mailed that it is live.
- **Report 1000135**: a reader moved the same tree's pin by hand, 306 m from our cemetery coordinate to a spot inside Laurel Hill East. No other tree of ours is near it. Our pin only marked the cemetery, so theirs replaces it. It stays approximate because it is hand-placed. The story's line "the pin marks the cemetery, not the trunk" is now false, so it was rewritten to point at the trunk by the drive. Philadelphia has no translations. The standard pin thank-you went.
- No readers' trees, tips, feedback or reader notes were waiting. Amsterdam lead 3c544597 is our own account (`mine`), so it is not reader work.
 trees live (Oslo, Oxford's Magdalen Plane, a Cape Cod cedar, a Maryland white oak), two photos on trees we map

- **Live, new trees**: a willow lying flat on the Akerselva bank in Oslo with its branches grown up into a row of stems, the reader's note quoted (osl_006, photo GPS); **the Magdalen Plane** in Oxford, planted 1801 per Magdalen College's grounds page. It sat in data/leads/oxford.json waiting only for a sign it still stands, and the reader's November photo is that sign (oxf_008, approximate pin on the New Building lawn, paid college entry); a twisted Atlantic white cedar on the swamp boardwalk at the Marconi Station Site, Wellfleet, Cape Cod (wfl_001, a new one-tree place with its texts, hand pin, NPS trail page as source); a broad twin-stemmed white oak beside a woodland path near Boyds, Maryland (wdc_043 in Washington DC, device fix).
- **Photos on our trees**: a second reader's autumn view of the Clingoe Hill oak (cls_001) is now the lead, the earlier photo in the strip. A trunk photo that matched the Sawara cypress (ehp_004) by distance shows a beech, the same reader's many-stemmed beech ehp_001 31 m away; it goes in that tree's strip. Its story now carries their "European beech" and about 300 cm girth as theirs. The photo's location was hand-placed, so the beech's pin stays where it was.
- No reports, feedback, tips or reader notes waiting. The 38 `mine` leads (our own photos, Japan and Baarn) are not reader work and were left as they are.

## 2026-11-23 reader judge: East Hampton grows to six (a sourwood and a zelkova), and the site is the Dayton Arboretum

- **Live**: the same reader's last two photographs from East Hampton, which reached the intake after the earlier run: an old sourwood with deep blocky bark (ehp_005, GPS fix) and a Japanese zelkova in full orange autumn colour by the car park (ehp_006, hand pin, approximate), both named by the arboretum's labels in the reader's photos.
- **Where they stand**: OpenStreetMap puts all six pins on Pleasant Lane, just west of Herrick Park's own outline, on the lots of the Douglas E. Dayton Arboretum (East Hampton Star, 2022-12-15: a former mayor's garden of specimen trees, bought by the town from 2017, still fenced in 2022 while the village worked to open it). All six access lines now say so and ask visitors to check it is open; place intro, question texts and FAQ rewritten for six trees.
- This run first built all six itself and collided with the earlier run's push; the four already live were kept as they were. Its six duplicate photo files were moved to out/tmp/ on this runner, never committed.
- The paulownia held 11-21 on a hand pin in Springs (fba415e7) is very likely ehp_002 with the pin dropped 5 km off; noted on the lead, stays held. No reports, feedback or reader notes waiting.

## 2026-11-23 session: held app trees get the question too

- The Shanghai ginkgos (submission 1506, held `not_public`) now carry the standard "can it be seen from a street or path?" question; it goes at the next knock. The judge had skipped it believing an app tree cannot be mailed; it can, through the row the app writes when a tree is sent.
- `hold_reply.py` now takes a sighting id (`lead:<id>`) and finds that row, and BRIEF_READER_JUDGE.md says app trees get the mail. A sighting only kept in the reader's own collection gets none: the Clarksville oak (d440dd95, photos from inside a yard by a house) was never sent to us, so it stays held and unmailed.

## 2026-11-23 session: the red iOS and deploy runs

- **iOS (three scheduled runs red):** appfit failed the iOS 18 floor on one button, the country flag beside your name on My trees: 44 by 20, under Apple's 44 by 44. It was tappable over 44 points, but a -12 padding shrank what it measured. The tap area is now an overlay of 44 by 44 and the row looks the same. `appfit.py --os 18` on iPhone 16 Pro Max: 0 findings on 40 screens; looked at in the simulator. The next ios.yml run should be green.
- **Deploy:** the red push run (12:35) was two deploys colliding at Pages ("in progress deployment"), which 5110d09b5's shared deploy queue already fixed; every deploy since 13:17 is green. Still open: the Pages artifact is 1.6 GB against GitHub's 1 GB limit (a warning today, "deployment might fail"), which is the next thing that can turn the deploy red.

## 2026-11-23 reader judge: four readers' trees live in East Hampton, Long Island

**What changed:** a new place, East Hampton (New York). One reader sent four trees from the lawns beside Herrick Park in the village, all within about 100 m of each other, and all four are live:
- ehp_001 a broad many-stemmed beech in autumn colour. The reader named it Ginkgo, but the bark, leaves and form are a beech's, so it went live as Beech (Fagus sp.) and the story asks readers to settle it.
- ehp_002 a tall Royal Paulownia (its species from the label on its trunk, which the reader also photographed).
- ehp_003 a southern magnolia standing alone by the ball fields.
- ehp_004 a big Sawara cypress 'Squarrosa', also labelled. Its pin is the reader's device fix, so it is `confirmed`. The other three were pinned by hand and stay `approximate`.

All four photos are from November (`taken_month` 11). Label and leaf photos are in each tree's strip. East Hampton is added to data/us-states.json as New York. The place has intro, question block and three FAQ.

**Also:** tip:1400 is the website copy of the Springs paulownia (sighting fba415e7), whose lead has been held `not_public` since 11-21. It is recorded as `hold`, same reason.

**Left:** sighting 3c544597 (Amsterdam, `mine: true`, our own photo) has no photo on disk. Our own photos are never auto-published, so it waits as before. No reports or feedback were open. `city_names.py` has not been run for east-hampton yet (a preflight note).

## 2026-11-23 session: Android invitations on hold, no batch through a Google mailbox

- **Android now**: build 5 live on both closed tracks; 22 phones on it by the 23rd (14 that day, 4 still on build 4), 158 Android phones ever; no unanswered crash.
- **Decided (Hidde: "eens")**: the 478 unsent wave 3 invitations wait. The send log shows 250 to 400 mails a day through his Gmail from 11-19 to 11-22 (264 invitations on 11-20 alone, plus reader mail), and Google blocked the account on 11-23; the likely cause, not confirmed. Order now: Play access back, one tester confirms the group and opt-in work, then the rest through Resend only in small portions on his "verstuur". No batch goes through a Google mailbox again, Workspace included (CLAUDE.md mail route rule; drafts/android-test-invite.md). The batch's `"kind": "expected"` still routes through Gmail and must change before any send.

## 2026-11-23 session: Supabase egress, the cause found and the waste stopped

- **Why Supabase's free plan ran out**: 12.5 of 5 GB egress this month. Edge logs, last 24 hours: ~690 MB a day was our own runners downloading readers' photographs from the private `sightings` bucket, 784 downloads of 91 files. Every Reader judge run starts on a clean runner and fetched every waiting photograph again in full size; a burst of submissions starts many runs. Visitors' own photo traffic is ~110 MB a day.
- **Live (8f4c60a7e)**: reader-judge.yml and nightly.yml keep out/sightings in GitHub's cache (restore before the intake, save only when the file set changed, files untouched 30 days drop out). Each photograph now leaves Supabase once.
- **Still needs Hidde**: this month's overage cannot be undone, so Pro ($25/month, spend cap on) before the restriction of 25 Nov stands. Without the waste we expect ~3.5 to 4 GB a month, close to the free 5 GB; whether to go back to Free is next month's call on the measured number.
- Measuring it again: the Management API's logs endpoint changed (`analytics/endpoints/logs`, ClickHouse SQL, `FROM logs WHERE source = 'edge_logs'`, `log_attributes['response.headers.content_length']`); REST rows carry no length, so database egress is not measurable this way.

## 2026-11-23 session: deploys faster, readers' trees live sooner

**What changed:** a reader's tree took one to two hours from the judge to the site, sometimes longer (Hidde: "ja wel heel traag"). The deploy took about an hour, and 37 minutes of that went to `qa.py` on the built site (28,938 pages). Two changes:
- **qa.py parses each page once, not twice.** The orphan check reuses the links from the first pass. Each link target is now looked up on disk once, not once per page that carries it. The checks and their answers are the same: on a test site with dead links, orphans, relative links, dir/index and .html links, the old and new versions reported exactly the same failures. On 3,000 test pages it went from 26 s to 3 s. The deploy log now prints `qa: N pages scanned in Ns`.
- **One queue for deploys of main.** Pushes and dispatched runs each had their own queue, so two deploys could reach Pages at once, and Pages refuses the second (12:35 UTC today: an hour of building lost). Every run of main now waits in one line. A running build is still never cancelled.

**Not checked yet:** the time of a real deploy with this change. Read it from the next deploy's QA step.

## 2026-11-23 reader judge: the Tight Grove in Albuquerque has its first photograph (abq_001)

- **abq_001 Tight Grove, University of New Mexico**: a reader's photo of the grove, viewed before approval. It shows tall ponderosas around the Lobo wolf sculpture, with Hodgin Hall's pueblo-style front behind and cottonwoods in autumn yellow at the edge, which is what our recognition line describes. It is now the lead photograph (the tree had none) and is filed in November. The pin moved 73 m to the reader's GPS fix, now confirmed. The reader's "it is live" mail went through sightings_publish `--send`. The script's pins catch-up could not read coordinates (HTTPError), but the move itself was written.
- The judgement for the Greenwich ginkgo lead (c5a932e5, already live as lon_055) was recorded.
- There were no open reports, tips, feedback or readers' words. The only remaining waiting lead (3c544597, Amsterdam) is our own account's test photo (`mine`), and its file is not on disk, so it was left.

## 2026-11-23 reader judge: a reader's gold ginkgo in Greenwich is live (lon_055)

Both photographs were viewed. There were no open reports, tips, feedback or readers' words waiting.

- **lon_055 The Golden Ginkgo of Greenwich**, London: a big ginkgo in full autumn gold, behind low railings beside a public path a few streets west of Greenwich Park. The pin is the photograph's own GPS, so it is confirmed. The lead photo is filed in November from its own date. A second shot from the railings went in the strip, also filed in November, by its autumn colour. We have no age, girth or source yet; the story asks readers for them. London's texts carry no tree count, and there is no London overlay, so nothing else changed.
- The other leads with status `lead` in data/leads/_sightings.json are all our own account's test photos (`mine`), not readers', so they were left as they are.
- Tree notes (rung 1, the night run's) were read but not marked seen. One on the Thalmassing oak (thm_001) describes "a cedar of Lebanon, in Varese, planted in 1859". It looks like it was meant for var_001, but it is not on the hide list, so it stays.

## 2026-11-23 reader judge: five readers' trees live (two Châtenay arboretum trees, a Tamarit oak, a bristlecone, the Patagonia mesquite); one held; Varese ginkgo gets its planting year

Every photograph was viewed. No open reports.

- **cma_002 The Cedar of Lebanon of the Vallée-aux-Loups** and **cma_003 The Elephant-Foot Tulip Tree**, Châtenay-Malabry, both sent by the reader who sent the weeping cedar. Each came with a photo of the Hauts-de-Seine label, which is now the source: the cedar was planted around 1750, is 24 m tall and lost 5 m of crown to Lothar in 1999; the tulip tree was probably planted in 1890 and is 21 m. Both labels went in the strip. The pins were placed by hand, so they are approximate. The place now has 3 trees, so the intro grew, and `oldest_tree_id` is now the cedar.
- **tgn_006 The Oak over the Wall at Tamarit**: a big holm oak arching over a path above an old wall near Tamarit. The reader's phone fixed its position. Tarragona's texts and the es overlay now say five.
- **abp_002 The Twisted Bristlecone by the Rocky Trail**, near Schulman Grove, pinned from the photo's GPS, with two more views in the strip. The forest's texts no longer say it maps one tree. The story names no tree and claims no record. Methuselah stays unmapped.
- **pag_001 The Old Mesquite of North 4th Street**, Patagonia, Arizona (a new one-tree place, in us-states). The reader's mail reply (feedback 1547) answered our "where is it" mail with the address and a map pin. The pin was dropped by hand, so it is approximate; the tree is seen from the street because the lot is private.
- **Held**: the "Hophornbeam" near Shelby NC (2505d7d8), as `not_special`. It is a medium tree in a planting bed by a loading dock. No mail goes.
- **Rejected**: 2414d848 for wtn_003 Willistown. It duplicates the photo already leading that page, from the same reader.
- **Mail replies 1542 and 1543** (the same mail twice, about the Paris plane's eroded roots) were closed as handled; the fact was already on par_077. tip:1530 is the submission row of the already-live rng_001.
- **Readers' words**: var_002 Ginkgo of Varese now carries the reader's note that it was planted in 1865 in Villa Mirabello's garden, as theirs, and that is its age.
- Not touched: the 38 waiting leads marked `mine` (our own photos, never auto-published).

## 2026-11-23 - Night run 2026-11-23 13:57 UTC ended without saying anything

Written by the workflow's Run health step, not by the run. 0.0 minutes of its 120 minute window, 1 turns, ended clean (success). 3 commit(s), none of them a published tree.

This entry exists because the run wrote none. The prompt asks every run to log even when it ships nothing, and a run that gives up is exactly the one that skips that instruction, so the count above is measured rather than reported.

What each attempt said as it stopped, in its own words (secrets scrubbed):

- Attempt 1: You've hit your 5-hour limit · resets 4:20pm (UTC)

## 2026-11-23 reader judge (afternoon): a second Rungis lime photo

**What changed in the product**
- **Rungis rng_001, The Large-leaved Lime**: an October photograph of the lime in its kerbed bed, from the reader who added it, is now in the gallery (`strip`, filed under October) behind their November lead. Its verdict is recorded.

**Overlap**: this run judged the par_077 plate photo at the same time as the run below and reached the same verdict. The rebase kept that run's version, so only the Rungis photo is new here. The 38 waiting leads in _sightings.json are all our own account's (`mine`) and have no photo on disk, so none was judged.

## 2026-11-23 reader judge: the Jardin des Plantes plane's own label proves its age

**What changed in the product**
- **Paris par_077, The Tall Plane of the Jardin des Plantes**: the reader who added it this morning also sent a photograph of its museum label ("Arbres historiques & remarquables": Platanus x hispanica, "planted under Buffon in 1785", its roots bared by erosion of the labyrinth slopes). The label is in the gallery behind their trunk shot (`strip`) and is now the page's source. The age is now 241 years (planted 1785), sourced, which matches the reader's own figure. The story and recognition line are rewritten in English and French to include the label and the bare roots. It is not par_004, the oriental Buffon Plane on the open path; the verify_notes say so. The pin stays approximate (hand-placed).
- tip:1531 is the submission row of that same tree, so its verdict is publish (par_077), with nothing more to add.

**Left as it is**
- Sighting 3c544597 (Amsterdam, "not sure which" near ams_032) is one of our own photos (`mine`) and is not on disk, so it was not judged blind.
- No open reports, no feedback without a verdict, and no reader notes waiting to be quoted.

## 2026-11-23 reader judge (evening): a York plane live, a second Minster Yard beech photo

**What changed in the product**
- **York yor_008, The Minster London Plane** (new, a reader's tree): the York reader who added the Minster Yard beech sent a photograph "of the beech" that shows a big London plane on the Dean's Park lawn, with the Minster tower behind it. Judged `other_tree` and published as its own tree. Their note is quoted and their 325 cm girth is stated as theirs. The pin is approximate: the lead has no `location_kind`, so it is not a fix. The photo is filed under November (leaf-fall, the day it was sent).
- **York yor_007, The Minster Yard Beech**: the same reader's wide shot of the whole beech, bare in November, is in the gallery (`strip`) behind their in-leaf lead. The confirmed what3words pin is unchanged.

**Skipped**
- The Amsterdam lead `3c544597` is still not on this machine and is our own account's (`mine`). It was not judged.
- No open reports, no feedback without a verdict, no tips, no reader words waiting. The congratulation for yor_008 goes out after the deploy (deploy.yml's tell-readers job), the knock as safety net.

**Breakage**
- sightings_publish.py's pin catch-up hit an HTTPError ("could not read coordinates"). No pin was affected this run.

## 2026-11-23 session: readers hear their tree is live after the deploy, not at the next knock

**What changed:** deploy.yml has a third job, `tell-readers`. After every deploy of main that goes through, it waits ten minutes for the Pages cache, then runs `tree_approved.py --send` and `sightings_publish.py --flush-mail --send` (private_store pull and push around them) and commits the two ledgers. Until now these mails went only from the nightly knock, so a tree the reader judge put live in minutes was announced hours later. Today's 13 readers' trees (judge, 11:42 UTC) had not been mailed because no knock had run since. Hidde, 2026-11-23: "is het niet logischer als de judge gelijk de mail activeert?" Not from the judge itself: the build takes about 40 minutes after it, and a link to a page that is not there yet is worse. The knock still sends as the safety net. Both scripts keep their own ledgers, so nobody gets a mail twice. Undo: delete the job.

**Mail route today:** OUTREACH_SMTP_USER is now hidde@ancienttrees.app (Workspace). OUTREACH_SMTP_PASS still holds the old Gmail app password until Hidde sets the new one, so sending falls back to Resend (mailer.py), and reading the inbox (reader mail replies, sent_drafts, bounces) fails until then.

**Not checked yet:** the first real run of the job, on the next deploy.

## 2026-11-23 reader judge (later): Split ginkgo gets its first photo, 4 gallery photos, a Marjan cypress held

**What changed in the product**
- **Split spl_002, the Ginkgo of Đardin**: its first photograph, a reader's shot of it in full yellow leaf (November). Pin: approximate, at the spot the reader placed by hand in report 1000132 (43.509872,16.441251). *Corrected by a parallel run:* this entry first said HEAD had never applied the move and set the pin to 43.5095,16.4404. Git history shows that coordinate is the original pin from d92d6d942, and 4911c5f8b had already moved it to the reader's spot; the sighting carried the old pin echoed back by the app. The reader's spot is restored.
- **Tortworth ttw_001**: two reader photographs in the gallery behind the lead (the fenced ring in autumn leaf, and the estate's interpretation board).
- **Kaštela cdl_003, Mastrinka**: two reader photographs in the gallery (the whole olive on its lawn, and two visitors sitting inside the split trunk). Neither is filed under a month (corrected after the fact). taken_month 11 came from the day they were sent; the files had no date, and a green lawn with daisies is not November.
- Varese var_002: the reader sent the same photograph that already leads the page, rejected as a duplicate.

**Held**
- A reader's photo sent for spl_003 (the Kolombatović cypress) shows a different tree. Its plaque names the cypress planted in 1930 on Marjan's path for Šimun Tudor. The Društvo Marjan chronology confirms it and notes that the plaque wrongly says "first president". It is now a lead, "The Cypress of Šimun Tudor, Marjan", held `doubt_location`: its coordinate is our spl_003 pin, and the path is long. It is an app sighting with no submission row, so hold_reply.py could not mail the reader.

**Breakage**
- sightings_publish.py turned two coordinates with no `location_kind` into a confirmed "reader GPS fix": ttw_001 moved 22 m, spl_002 moved 80 m. preflight refused ttw_001 (`check_a_hand_placed_pin_is_not_a_fix`). I put both back by hand to an honest approximate pin. The script should not call a coordinate a fix when the queue entry's location kind is empty. That is for a session to fix.
- No open reports, no feedback without a verdict, no reader words waiting.

## 2026-11-23 reader judge: 13 readers' trees live, 12 photos placed, 3 reports closed

**What changed in the product**
- **New readers' trees, 13 live** (every photograph viewed). Paris par_077 is a tall plane in the Jardin des Plantes; the reader's 241 years are stated as theirs, and the French overlay is done. Copenhagen gets three trees in Birkerød: cop_051 (an oak on a footpath), cop_052 (an oak standing on bare roots) and cop_053 (a burred village tree by a thatched house; species asked of readers, a lime by its burrs). New places:
  - Varese: var_001, a cedar of Lebanon, and var_002, a gold ginkgo. Both match MASAF register entries 36 m and 15 m away; the register's girth and height are on the ginkgo.
  - Esrum: esr_001, a burred, broken veteran oak in Esbønderup Kohave, 600 years by the reader's estimate.
  - McMinnville, Tennessee: mcm_001, a huge spreading oak with one limb resting on the grass. Added to data/us-states.json.
  - Siliqua, Sardinia: slq_001, "the Queen" olive. The reader's 1,000 years and their Phoenician story are stated as theirs. Hand-placed pin, approximate.
  - Rungis: rng_001, a many-stemmed large-leaved lime. Hand-placed pin, approximate.
- **Photos of trees we map**: rom_024 has its first photograph. New lead photos on lon_036 (pin moved 44 m to the reader's fix), stb_002, par_016 and cma_001. Strip photos on mlr_002, mel_005, rom_028, wai_001 (a person in frame, so never the lead) and par_076.
- **Kett's Oak (hth_001)**: a reader sent a photo marked "not sure which tree". It shows the oak itself (the 1910 plaque, the prop), so it is now hth_001's lead photo and report 1000131 is closed.
- **par_076, the bur oak**: a reader photographed its Muséum label ("Arbre historique, planté en 1811"). The planting year is now on the page in English and French.
- **thm_001**: a photo of the Varese cedar was sent for St. Wolfgang's Oak, 426 km away. Rejected as a duplicate of the Varese lead.
- **rom_024**: rewrote a colon reveal in its story, since a reader photo now puts it in Google.
- **Held, under the closed list**:
  - c3cd1f53 `dead`: the reader says the beech was cut down.
  - c519f040, d40d0b0e, 81bfa129, 8faa5fe0 `not_special`: an ordinary lane tree, a garden tree, a slender fan palm and a common pollard willow.
  - 2beaef82 `not_public`: two ginkgos at Shanghai Jiao Tong University; we cannot tell whether they are visible from outside the campus. hold_reply.py only takes website submissions, so no mail went (the known gap).
- **3c544597** (one of our own, no photo on disk) was left for the intake.

**Reports**
- **1000132, Split spl_002**: the pin moved 80 m to the reader's spot (approximate, hand-placed). Standard pin thank-you sent.
- **1000130, Hamburg hbg_005**: the reader asked for their selfie to come off because their faces show. It is off the page (`--unstrip`), since a recognisable person is the one case that comes off on request. Closed `holds`, with a suggested reply in drafts/reply-reader-1000130-2026-11-23.md. For Hidde: their words were "I didn't realize adding my photo to my trees would post it on the page". Collect-flow photos going public surprised a reader.

Checks: preflight 0 problems, i18ncheck fr/paris clean, qa source-only nothing to fix.

## 2026-11-23 - Night run 2026-11-23 02:08 UTC ended without saying anything

Written by the workflow's Run health step, not by the run. 0.0 minutes of its 120 minute window, 1 turns, ended clean (success). 3 commit(s), none of them a published tree.

This entry exists because the run wrote none. The prompt asks every run to log even when it ships nothing, and a run that gives up is exactly the one that skips that instruction, so the count above is measured rather than reported.

What each attempt said as it stopped, in its own words (secrets scrubbed):

- Attempt 1: Failed to authenticate: OAuth token revoked. Please log in again or contact your administrator.

## 2026-11-23 reader judge: a golden ginkgo at Sakurai Shrine, Itoshima

- New tree live: fukuoka/fuk_019, The Ginkgo of Sakurai Shrine in Itoshima. It sits with the other Itoshima day trips on the Fukuoka page. The reader also sent the Kumamoto Castle ginkgo. Their November photograph shows the crown in full gold behind the shrine's old copper-roofed halls. The shrine facts (founded 1632 by Kuroda Tadayuki, three buildings made Important Cultural Properties in 2023) come from ja.wikipedia. No source mentions the tree itself, so the page asks readers for a girth and a name. The pin was placed by hand, so it is approximate. The photo is filed in November, best_time is November gold, and there is a Japanese overlay entry. The Fukuoka counts in question_meta (en) and in the ja title, meta and question_meta now follow the new number.
- Paavola's Oak had been published by a parallel run (entry below), so I kept its version.
For Hidde: none.

## 2026-11-23 reader judge: Paavola's Oak in Lohja gets its first photograph

- New lead photo: lohja/loh_001, Paavola's Oak. Until now the tree had no photograph. The reader's picture shows the whole broad, low-limbed oak in summer leaf behind its rope fence on the trail, in daylight. Species and description both match. It has no season month: it is plain green, and the date in the file is the day it was sent.
- No open reports, no unjudged tips, no feedback without a verdict, no readers' notes waiting to be quoted. Lead 3c544597 (by Amsterdam Centraal) is still our own account's (`mine`) with no file on disk, so I left it unjudged.
For Hidde: none.

## 2026-11-22 reader judge: a third Willistown tree, the white oak on Grubb Road

- New tree live: willistown/wtn_003, The White Oak on Grubb Road. The same reader sent the Crum Creek sycamore and the Bryan Avenue oak. Their August photograph shows the whole oak on a roadside bank by a split-rail meadow fence, in daylight. They give 435 cm round and about 225 years; both figures are stated as theirs. The pin was placed by hand and lands on Grubb Road (Nominatim), so it is approximate. Access: see it from the road. The photo is filed in August, the month the photo was taken.
- Willistown's intro, meta, question texts and FAQ now count three trees. There is no kept translation.
- No open reports, no feedback without a verdict, no readers' notes waiting to be quoted. The other waiting leads are our own account's (`mine`) with no file on disk, including 3c544597 by Amsterdam Centraal. I left them, because we never judge a photo we haven't seen.
For Hidde: none.

## 2026-11-22 reader judge: one mail reply filed, nothing else waiting

- Nothing changed on the site. No photographs in the queue, no open reports, no unjudged tips, no readers' notes waiting to be quoted.
- Feedback 1500, a mail reply saying thanks and that the sender will photograph trees on a next visit: closed handled, not quoted.
- The one waiting lead, 3c544597 by Amsterdam Centraal, is our own account's (`mine`) and its photograph is still not on disk. Left alone: we never judge a photo we haven't seen.
For Hidde: none.

## 2026-11-22 reader judge: three readers' photographs live (Hamburg, Paris)

- Hamburg's Lehmann plane (hbg_007) has its first photograph: a reader's autumn shot of the crooked trunk and the low heavy limb, 9 m from our pin. Its page now has reader content, so preflight read its story as indexed and caught a colon reveal; rewritten in English and the German overlay.
- Hamburg's Japanese pagoda tree (hbg_005): the readers' dusk selfie at the tree, whole crown and heritage sign behind them, goes in the gallery behind the Commons lead (strip, never lead).
- Paris's bur oak by the Cuvier gate (par_076): a reader's frame in full autumn leaf is now the lead; the bare November photo moves to the gallery.
- Feedback 1499, a mail reply saying thanks and promising photos on a next visit: closed handled, not quoted.
- No open reports. The 38 waiting leads in _sightings.json are all our own account's (`mine`) with no file on disk, including 3c544597 by Amsterdam Centraal; left, never judged blind.
For Hidde: none.

## 2026-11-22 night run, third attempt: Coimbra verify dispatched

Claimed coimbra (only 4 unmined register candidates, 17 open leads) and dispatched a verify agent; portland and porto refused (already over target). 4 READY leads still under the six minimum; pending write files are all stale, duplicates or id clashes. Reader sighting 3c544597 still has no photo on disk, left open. Nothing published yet.
For Hidde: none.

## 2026-11-22 night run, second attempt: nothing published

Nothing shipped. Only 4 READY leads (leamington-spa 2, york 1, guimaraes 1), under the six-candidate minimum. The rest of "awaiting a writer" is duplicates within 50 m or id clashes with live trees (passcheck --pending), so not writable. Claimed fort-worth for a verify pass: its brief had 0 register candidates and the city holds 29 of its 30, so I released it (now a 48h wall). Translations are paused while TRANSLATIONS_OUT holds, and no register is left to scout. One reader sighting of an unmapped tree (3c544597, 52.397,4.874) has no photograph on disk and was left without a verdict, not judged blind.
For Hidde: none.


**Older entries live in the archive**, moved by `scripts/archive_logs.py`, nothing deleted:

- [2026-11](archive/LOG-2026-11.md)
- [2026-10](archive/LOG-2026-10.md)
- [2026-09](archive/LOG-2026-09.md)
- [2026-08](archive/LOG-2026-08.md)
- [2026-07](archive/LOG-2026-07.md)


## 2026-11-22 night run (20:34 UTC window): nothing published

Rung 1: the one open reader photograph (3c544597, Amsterdam, our own account's `mine`) has no file on disk, so it stays open, never judged blind. Rung 2: health red only on open BUG rows. Closed the web row for the explore search pill (fix and pagecheck test already in b8c48b9ae). The app row for the country save stays open: its fix (supabase/flag-upsert-fix.sql) waits for Hidde's paste. For Hidde: paste supabase/flag-upsert-fix.sql.
Supply: every "awaiting a writer" file is stale (already published); READY is 4 leads in walled cities; braga has 4 unmined candidates (under six, released, wall 48h); munich has no coordinates; scout_next says nothing left. No agent dispatched because no lane held six real candidates. Translations stay paused (TRANSLATIONS_OUT).

## 2026-11-22 reader judge (twentieth run): a giant Mexican sycamore live in Xalapa

- **New tree: The Mexican Sycamore of Río Sedeño**, xalapa/xal_001, a new one-tree place in Mexico. A reader sent it through the app with a GPS fix from the path of the Parque Lineal Río Sedeño. The trunk is pale and patched white and olive, with a mossy crown above. The page states the reader's figures as theirs: about 150 years old and 650 cm round. The lead photograph is their second picture, which shows the whole tree. Their first picture, a close portrait of a child at the trunk, is **not** published. The photo is filed in November.
- No reports, feedback or tips are open, and no reader words wait to be quoted.
- Left: lead 3c544597 (Amsterdam, `mine`) still has no photo on disk. It was not judged blind.

## 2026-11-22 reader judge (nineteenth run): two Horn-Lehe mail replies closed, nothing new to publish

- No new trees, photographs, tips or reports came in. This run did nothing on the site.
- **Mail reply 1493** says the country she picks still does not stay. It is the same report today's session fixed in eef9c2bcb, and its reply waits for Hidde in drafts/reply-reader-1358-2026-11-22b.md. Closed `handled`, and in reader_words as not about the tree.
- **Mail reply 1494** asks to be ambassador of Bremen. Our only Bremen place is Horn-Lehe, and she already holds that badge. Closed `handled`. Her "Looking after Horn-Lehe" welcome still did **not** go out, because this machine has no mail credentials. A knock or session that has them should run `ambassador.py --welcome-missing --send`.
- Left: lead 3c544597 (Amsterdam, `mine`) still has no photo on disk. It was not judged blind.

## 2026-11-22 session: the country you pick on iPhone stays picked

- Reader 1358 wrote again after this morning's flag fix: "Helaas wil het land bij mij nog niet blijven staan". The server takes the apps' save now (round-trip on apptest: BE, then NL). Her row still said NL, so her new choice had never reached it.
- The cause sat in the iPhone app. Edit profile filled the name and country in a `.task` on its Form, and the Country list is pushed over that Form, so coming back from the list ran the task again and put the saved country back before Save. It now fills once per opening (ProfileEditor.swift). CountryStaysWalk picks Don't show over NL: without the guard it fails ("Netherlands" back on the row), with it it passes. Android was already fine (`remember`).
- Escaped bug ESC-2026-11-22-edit-profile-put-the-saved-country-back- is recorded, caught and fixed in eef9c2bcb. The fix reaches readers with the next iOS build; until then the website's /account sets the country.
- For Hidde: a reply to her is drafted in drafts/reply-reader-1358-2026-11-22b.md. It waits for your yes.
- The Horn-Lehe reader (mail 1491, eighteenth reader-judge run below) reported the same thing; this is the same cause and the same fix. The morning's server row (ESC-2026-11-22-the-country-picked-in-the-app-was-never-) stays open for the apps' PATCH.

## 2026-11-22 session: a dropped pin, double tap for a heart, a second tap on Map and My trees

- **Touch and hold the map drops a pin**, iPhone, Android and website (right-click on a computer), built to Apple's and Google's own help pages (Hidde: "build it exactly as them"). One red pin above our trees, a "Dropped pin" card with the coordinates, Add a tree here and Directions; a tap elsewhere takes it away. Add a tree here opens the add flow at that spot.
- **Double tap a visitor's photo in the feed gives a heart**, Instagram's way, on all three (gives only, a white heart pops over the photo).
- **Tapping Map again** brings the map back to where you are; **tapping My trees again** scrolls the list up (phones; the website has no tab bar).
- Looked at: the iPhone pin and card in the simulator, the web pin and card on a test map in the live explore page. Android compiles and has not been looked at on a phone; the website waits for CI's build.
## 2026-11-22 reader judge (eighteenth run): a cedar in Piazza Indipendenza, Verona, live; a Tennessee oak held; a Bremen ambassador

- **New tree, verona/ver_010, "The Cedar of Piazza Indipendenza"** (tip-1490, through the app, "Old, very very beautiful"). The tip had two images. The first is a Google Street View capture, used only to place the tree: it is captioned Piazza Indipendenza, with parking and a hedge at the tree's foot, so it is not the Bra cedar (ver_001). The second is the reader's own November photo of the whole tiered cedar, and it is the lead photo, filed in November. The species is left as the genus, Cedrus sp.; the reader calls it a Himalayan cedar, and the story says so and asks. The pin is approximate, on the square's garden. Verona now counts nine trees in the city, plus San Bonifacio. I updated the intro, the question meta and the FAQ in English and in the kept Italian overlay, and added the Italian story.
- **Held `not_public`: d440dd95**, an app sighting from the countryside north-east of Clarksville, Tennessee. All three photographs were viewed. They show a massive old oak in copper and gold leaf, clearly special, standing in a mown yard beside a barn, a coop and a house. Every photo was taken from inside the yard. If the reader says it can be seen from a road, it goes live with the pin on the viewing spot. hold_reply.py only takes website submissions, so no mail went out.
- **Mail replies from the Horn-Lehe reader.** In 1492 she asks to be ambassador of "this part of Bremen": badge granted for horn-bremen (`ambassador.py --grant ... --send`). This machine had no mail credentials, so the "Looking after Horn-Lehe" welcome did **not** go out; a session or knock with credentials needs to send it. In 1491 she says the country she picks in the app still does not stay, even after a restart and after today's flag-upsert fix. Closed as `needs_hidde`; it is the open BUG row ESC-2026-11-22, and a session should check her profile row and her phone and build. Both rows are closed in reader_words as not about the tree.
- Left: lead 3c544597 (Amsterdam, `mine`) still has no photo on disk. There were no open reports.

## 2026-11-22 daily publish: queue empty

- **Daily publish: queue empty.** The only builder newer than build_write_2026_11_21c is build_write_2026_11_22 (lvg_015, lvg_016, nyc_029), and all three are already on main in data/cities (243b8dd02); no out/tmp/held_build.py, and data/research/puglia-held/ was live before. Nothing published, pace untouched. For Hidde: the daily task "publish-held-trees-daily" can be switched off under Scheduled; write passes put trees straight into the app, so nothing waits for it.

## 2026-11-22 session: the country you pick on iPhone stays picked

- Reader 1358 wrote again after this morning's flag fix: "Helaas wil het land bij mij nog niet blijven staan". The server takes the apps' save now (round-trip on apptest: BE, then NL). Her row still said NL, so her new choice had never reached it.
- The cause sat in the iPhone app. Edit profile filled the name and country in a `.task` on its Form, and the Country list is pushed over that Form, so coming back from the list ran the task again and put the saved country back before Save. It now fills once per opening (ProfileEditor.swift). CountryStaysWalk picks Don't show over NL: without the guard it fails ("Netherlands" back on the row), with it it passes. Android was already fine (`remember`).
- Escaped bug ESC-2026-11-22-edit-profile-put-the-saved-country-back- is recorded, caught and fixed in 36d7ad09e. The fix reaches readers with the next iOS build; until then the website's /account sets the country.
- For Hidde: a reply to her is drafted in drafts/reply-reader-1358-2026-11-22b.md. It waits for your yes.

## 2026-11-22 reader judge (seventeenth run): a Patagonia mesquite held for its location; the Tortworth reader's feedback closed

This run judged the same trees as the parallel run (770f4f383), which had already published the Tortworth Chestnut, the Paris bur oak and the Spirit Tree lead. I dropped my duplicate and added only what it had not covered:
- **tip-1487, a mesquite on a town lot in Patagonia, Arizona**: photograph viewed. It is a big, many-limbed mesquite, 14 m tall and 18 m wide by the reader's figures. Held as `no_location`, because "Patagonia" and "town lot" are all we have. The standard reply (`hold_reply.py`) goes at the next knock.
- **Feedback 1488**: the Tortworth reader said the app listed their chestnut under Westonbirt Arboretum. It is now live as tortworth/twc_001, its own place, so the row is closed as `handled`.
Left: lead 3c544597 (Amsterdam, `mine`) still has no file on disk. No open reports, and no new readers' words.

## 2026-11-22 session: an Android tester from the ABC Darwin interview

Sent on Hidde's "Verstuur": a reply to Vincent (North Carolina), who heard Hidde on ABC Darwin and asked to test the Android app. His address is Gmail, so it is the Google Group route (group link, then the Play opt-in link) with no Play Console edit; it ends with a question about a North Carolina tree for the map. He is on the tester list as invited (`android_testers.py`, pushed).

## 2026-11-22 session: Chiang Mai has an ambassador

Live: Jonardon G., who added the Bodhi Tree at Sunset (cnx_003), answered the congratulation mail's P.S. with "Yes happy to be an ambassador". Badge granted (`ambassador.py --grant`), named on /chiang-mai because the profile is public, and the standard "Looking after Chiang Mai" mail sent once from the Ancient Trees address.
Breakage: `--grant` without `--send` is not a dry run when the Supabase key is on the machine; it granted at once. Loading ~/.ancienttrees-mail.env whole overrides the Supabase key (401), so only its OUTREACH_ lines were loaded for the mail.

## 2026-11-22 reader judge (seventeenth run): the Tortworth Chestnut and a Paris bur oak go live from readers

- **Live:** the Tortworth Chestnut (`tortworth/ttw_001`, a new place). The reader sent a May frame of the hollow, fluted giant and a second frame of its 1800 plaque ("six hundred years old"). Wikipedia confirms the tree and the accounts of 1664 and 1712. The reader's 900 years is stated as theirs. The pin is their hand-placed spot, which they moved 70 m while adding the tree (report 1000128, closed `holds`, no mail because it was their own new tree), so it stays approximate.
- **Live:** a bur oak just inside the Jardin des Plantes railings by the gate opposite the Pharmacie Cuvier (`paris/par_076`). It has the photograph's own GPS, and its 215 years is the reader's estimate. It has a French overlay entry, and the Paris meta counts went to 58 more in English and French.
- **Lead:** tip 1486, the Spirit Tree, a cottonwood at an inn near Patagonia, Arizona. It has no photograph and no source, and it is not yet clear whether it can be seen from the road. It is recorded in data/leads/patagonia-arizona.json with the coordinate from the reader's map link.
- **Overlap:** this run also put the Cedar of Jussieu frame into the gallery, but the sixteenth run below pushed it first, so its version stands.
- **Skipped:** the Amsterdam lead `3c544597` was not judged blind because its photograph is still not on this machine. The other waiting leads are our own account's (`mine`), never published. No open feedback and no reader words to quote. Congratulation mails are left to the knock (`tree_approved.py --send`).

## 2026-11-22 reader judge (sixteenth run): a reader's November view of the Cedar of Jussieu joins its gallery

paris/par_002: a reader's photograph (sighting a56bc4d5, 30 m from our pin) went into the gallery behind the reader's lead photo. It shows the cedar's arching side limb and flat crown over the gold ginkgo lawn, but it is overcast and partly screened. It was the one photo the parallel run (9e999d9f2) left unjudged, so it was put back in the queue and published through `sightings_publish.py`. This run had judged the Fontainebleau sequoia, the Argyle Street ash and both Boab frames too, but the parallel run pushed first with the same verdicts (fon_001 live), so that duplicate commit was dropped.
Left: lead 3c544597 (Amsterdam, `mine`) still has no file on disk. No open reports, feedback, tips or readers' words.

## 2026-11-22, night run (window from 17:04 UTC), rung 1

- **Live:** a reader's giant sequoia in the gardens of the Château de Fontainebleau is a new place, `fontainebleau/fon_001` (photograph viewed, GPS fix at the tree, nothing in a register or Wikipedia within 300 m, so age, girth and height are stated as unknown). The reader's Argyle Street ash frame for Glasgow was already in that tree's gallery, so nothing changed there.
- **Left open:** the Amsterdam lead `3c544597` (unsure which of ours, `ams_032` 2650 m away): its photograph was not on this machine, so it was not judged blind; the next reader-judge run takes it. The two open BUG rows in data/code-audit.json were written today by other sessions (app country save, web explore search) and carry a fix or test of their own; not touched.
- **Prepare:** the shelf is under 60 writable leads (5 ready, 907 one field from a source). No verify pass was dispatched this window; the time went to the reader work. `vendor_photos.py` copied the one new Philadelphia lead photograph onto our own domain.
- Nothing was refused by the tool list. `health.py` exits 1 for 6 of 12 knocks delivered and the two open BUG rows above.

## 2026-11-22 reader judge (fifteenth run): a reader's photo leads the Boab Prison Tree, and a reader's 1,500-year estimate goes on its page

Live: a reader's wide October frame of the Boab Prison Tree (der_001, Derby), showing the whole trunk inside its fence with the sign in front, now leads the page, and the earlier reader photo moves to the gallery. Their second upload was the same file and was rejected as a duplicate. The photo's GPS sits 80 km away, so no pin moved (ours is confirmed).
Changed: report 1000127 (same Boab, "estimated a 1500 years old not 500"), plus the same reader's note. The page now gives "about 1,500 years by a reader's estimate" beside the disputed 1905 figure, in the story, age_estimate, the age FAQ and question_context. Derby has no translation. The report is closed `holds` with no mail, because it carried their words.
Notes: three new notes were read (Boab age, Linden of Linn, Vernon Oak in Sheffield). None is on the closed list, so all are marked seen.
Overlap: this run judged the same queue as the fourteenth run below. It reached the same verdicts on the Romanyà stump and the Chiang Mai ambassador. At push those were taken from the fourteenth run as they stand, and only the Boab work above was added on top. Still open: the Chiang Mai welcome mail (no credentials in either run).

## 2026-11-22 reader judge (fourteenth run): the Great Pine of Romanya is gone and comes off the map; Chiang Mai has an ambassador

Off the map: girona/gir_004, the Great Pine of Romanya. A reader's photograph from the app (sighting 3771a756, taken today 7 m from our pin) shows cut sections of a big trunk on a mound and open sky where a 30 m pine would stand. Together with this afternoon's report 1000126 ("could only find a stump") that is the evidence the rule asks for. The tree was retired with `retire.py` (kept as blocked in data/leads/girona.json, the page redirects), and the photograph was rejected for the page and recorded as the evidence. Girona now has seven trees: its FAQ count was fixed in English and Spanish, the Spanish title (now "7, del monte a la ciudad") and the overlay's gir_004 entry were updated too. Because the reporter wrote words, no standard mail went. For Hidde: drafts/reply-reader-1000126-2026-11-22.md is rewritten to thank them and say the tree is off the map.
Ambassador: a reader replied by mail "Yes happy to be an ambassador" (feedback 1478, the Chiang Mai tree's adder), so the Chiang Mai badge is granted. This run had no mail credentials, so the standard "Looking after Chiang Mai" mail was not sent; `ambassador.py --welcome-missing --send` on a later knock picks it up.
Left: lead 3c544597 (Amsterdam, `mine`) still has no file on disk. No open reports, tips or readers' words.

## 2026-11-22 reader judge (thirteenth run): three Hilversum royal trees get readers' photographs; the Romanyà pine reported as a stump

Live: readers' photographs now lead three Hilversum trees that had none: the Coronation Lime of the Spanderslaan (hil_002; its railing with the gilded crown and W, filed under autumn by its fallen leaves), the Bernhard Chestnut (hil_004, with its boulder) and the Juliana Lime (hil_005, the whole tree on the Hilvertsweg). The pages now enter Google's reader cut, so preflight's colon-reveal check caught two sentences in hil_002 and hil_004; both were rewritten (Hilversum has no translation).
Overlap: this run judged the same queue as the twelfth run below. Its Vienna beech photo (723b9c72) turned out to be a second copy of the one the twelfth run put up (4491f36f), so it is recorded as a duplicate and the twelfth run's page, photo and story wording stand. The beach view for the Coqueiros fig (2120e761) was rejected by both runs.
Report 1000126 (Girona, gir_004 the Great Pine of Romanya, "dead or gone"): the reader writes they found only a stump and are fairly sure of the spot. No photograph, no news of a fall, and the Catalan register still lists the pine, so the tree stays and the report is closed `holds`; the report is noted in the tree's verify_notes. Because they wrote words, no standard mail. For Hidde: drafts/reply-reader-1000126-2026-11-22.md thanks them and asks for a photograph of the stump, which would take the tree off the same day.
Left: lead 3c544597 (Amsterdam, `mine`) still has no file on disk. The Hilversum rows carried our own pin, so no pin moved. No open feedback, no tips.

## 2026-11-22 reader judge (twelfth run): the Vienna beech gets its first photograph, and the talking tree's plaque goes into its story

Live: a reader's late-autumn photograph now leads vienna/vie_037, the Alois-Drasche-Park beech. Until now it showed no photograph, because the Commons file was held as a possible copper-beech neighbour. The page is now in Google's reader cut, so three colon reveals in its story were rewritten, in English and in the German overlay.
Changed: fln_001's story used to say we did not know what its plaques say. It now names the hand-burned one ("A árvore que fala", the tree that speaks) from the gallery photo the eleventh run put up, says the leaves are a tropical almond's, and still asks about the second plaque.
Live, against the eleventh run's verdict: 1eefef4c goes into the Coqueiros fig's gallery (fln_002). Its extra frames repeat the lead, but its main frame is a different, wider landscape view of the roots and the low wall. A reader's distinct frame of the tree is never rejected (2026-11-06).
Rejected: 2120e761, a beach and bay view sent for the Coqueiros fig. Only foliage shows at the edge of the frame, and its coordinate repeats the tree's first pin.
Breakage: this run overlapped the eleventh, judged the same queue, and was rebuilt on top of it at push. Along the way, sightings_publish.py moved fln_002's pin back 164 m as a confirmed "reader GPS fix". It took the new photo's coordinate for a fix, but that coordinate only repeats the first lead's hand-placed spot (`location_kind: placed`). The fig keeps the adder's own move (report 1000125, approximate). The script should check the lead's `location_kind` before move_pin(); that is not fixed here, so a later photo sent for a hand-placed tree can do the same again.

## 2026-11-22 reader judge (eleventh run): the talking tree's plaque in the Ribeirão gallery, the Street View fig held

Live: a reader's photo of the hand-burnt plaque "A árvore que fala" on the trunk of the Plaque Tree on the Shore of Ribeirão da Ilha (florianopolis/fln_001) goes in its gallery behind the dusk lead (July, from the photo's own date).
Held: the Figueira de duas pernas in Ribeirão da Ilha (1467) is a Google Street View screenshot (`not_theirs`); the standard friendly reply asking for their own photo goes at the next knock.
Rejected as duplicates: second copies of the photos that already lead the two Delhi trees (dlh_001, dlh_002; their companion rows 1468 and 1469 too), and a repeat of the upward shot that leads the Coqueiros fig (fln_002).
Breakage, caught at the rebase: this run also held the Bad Homburg logs as `dead`, as the tenth run below had already done; same verdict, the rebase kept one entry each. The merge left judgements.json with duplicate ids from both runs, including one already on main (2fabeea6); deduped, keeping the entry with a verdict.
Left: queue item 3c544597 (Amsterdam, `mine`) still has no photograph on disk. sightings_publish's pin step could not read coordinates (HTTPError); fln_001's pin came from the reader's own photo GPS the same day and the new photo stands 5 m from it, so nothing needed moving.

## 2026-11-22 reader judge (tenth run): the Bad Homburg felled trunk held, the Coqueiros fig's pin moved

Held: the Bad Homburg sighting (2f66b206), sawn sections of a felled trunk lying in a beech wood, held as `dead` with no mail.
Changed: report 1000125. The reader who added the Coqueiros fig (florianopolis/fln_002) this morning dragged its pin 164 m. We took the move, kept the pin approximate as a hand-placed pin, and sent the standard pin thank-you.
Breakage, caught at the rebase: this run also built the Fulltofta oak, held the Andaman tip and rejected the Redford redwood photo, but the ninth run had already pushed all three. The rebase kept that run's version (fulltofta/flt_001) and dropped this run's copy (horby/hrb_001). The Andaman hold mail was queued twice, once by each run; hold_reply writes the same reply_text, so the reader gets one mail. For the third time today, two runs judged the same leads at once.

## 2026-11-22 reader judge (ninth run): an oak at Fulltofta live, the Andaman tip held

Live: a reader's bare November oak at Fulltofta, Hörby, Skåne is a new tree, fulltofta/flt_001 "The Wide Oak of Fulltofta" (Oak, Quercus sp.; the photograph's own location, which the app had named "near Torna Hällestad", 25 km off; one-tree place, so no place page).
Held: the Andaman Islands tip (1463), a huge buttressed trunk with only "Andaman Island" as its place, `no_location`; the standard reply asking where it stands goes at the next knock.
Rejected: a photo sent for the Redford Wood Redwood (Edinburgh) that is a picture of a framed print of a fallen log, taken in central Edinburgh, plus a small maple.
Breakage, caught at the rebase: this run also judged the Linden of Linn photos, which the run above had already published; the rebase kept that run's version.
Left: lead 3c544597 (Amsterdam, `mine`) still has no photograph on disk. No open reports, feedback or mail replies. city_names.py found no Wikipedia article for Fulltofta.

## 2026-11-22 reader judge: a summer photo for the Linden of Linn

Live: the Linden of Linn (zurich/boz_001) took a reader's August photo as its lead, filed in summer. The same reader had sent the frame twice, so the second copy was rejected as a duplicate.
Breakage, caught before push: this run also built the Bad Homburg oak (lead 6315b918), but the eighth reader-judge run (314c4b0d7) had already published it as bhg_007 while this one was working. The rebase kept that run's tree and dropped this run's copy and photos. Two runs at once judged the same lead; the in-flight claim covers research passes only.
Reports: 1000124 (same reader, "not showing up in the space for summer") is now true because the photo is live. The reader wrote their own words, so no standard mail went; a suggested answer is in drafts/reply-reader-1000124-2026-11-22.md and the report is closed `holds`. Its reader_words row is closed as a question to us.
Left: lead 3c544597 (Amsterdam, `mine: true`, our own account) still has no photo on disk; not judged blind.

## 2026-11-22 session: three Jephson Gardens trees, from the Leamington ambassador's links

- Joanna (Leamington ambassador, sent lsp_001 and lsp_002 through the app) mailed Warwick District Council's Jephson Gardens tree walk leaflet and its "Trees in Jephson Gardens" records. A verify pass turned them into three trees, stories written here: lsp_003 Japanese oak ("may be one of the finest in the country"), lsp_004 Caucasian oak (large, rare), lsp_005 the sweet gum the council calls the largest in Warwickshire. Approximate pins read off the leaflet map, no photographs, so they are app trees with pins on the web map until a reader adds to them. Intro, meta and FAQ of /leamington-spa name them.
- Not added: the lakeside holm oak shortlisted for Tree of the Year was felled in July 2025 (blocked); the 1848 Ceremony of Oaks holm oak may be the same tree, the silver pendant lime could not be pinned, the Hitchman deodar was probably felled in 2024 (all in data/leads/leamington-spa.json).
- Reply to Joanna drafted (drafts/reply-joanna-leamington-2026-11-22.md), waits for Hidde's yes.

## 2026-11-22 session: the photo heart's tap area (iOS check red)

- ios.yml went red on Visitors: the heart on a visitor's photograph was a 26-point button since it split from its count. Hidde picked A of two screenshots (drafts/heart-tap-A-vs-B.png): the heart and the count now have Apple's 44-point tap area and look exactly as before (negative padding, PhotoLikes.swift). Seen on the simulator; CI is the proof.
- Flags after supabase/flag-upsert-fix.sql: 186 to 211 accounts with a flag within two hours (Apple 5 to 16).

## 2026-11-22 night run (resumed attempt)

Live: Miami gained three Florida champions (mia_018 Bayshore Park rubber fig, mia_019 Chase Avenue sea grape, mia_020 Miami Beach Botanical Garden weeping fig) and Handsworth Park black poplar (hwp_001) went in as a lone Birmingham tree. Earlier in the window, three more trees (lvg_015, lvg_016, nyc_029) went into the app.
Nothing useful: Birmingham's 15th verify pass was dry (claim released). Sheffield was claimed and released at once, because 0 of 4 leads carry a coordinate; it is walled for 48h. The READY pile is empty, so the shelf needs a verify pass on a city whose leads have coordinates.
Not done: city_names.py not run for birmingham.

**Older entries live in the archive**, moved by `scripts/archive_logs.py`, nothing deleted:

- [2026-11](archive/LOG-2026-11.md)
- [2026-10](archive/LOG-2026-10.md)
- [2026-09](archive/LOG-2026-09.md)
- [2026-08](archive/LOG-2026-08.md)
- [2026-07](archive/LOG-2026-07.md)

So absence from this file is not evidence something was never tried: `grep -ri "<place>" archive/` before concluding a hunt is new. Re-running an exhausted hunt is this project's most repeated waste.
## 2026-11-22 session: the + sheet now says a photo is shared

- **Product**: the sheet behind the middle + button (every upload passes it, both phones) said only "add it to your collection", which is how a reader put four holiday photos on public pages without knowing. Now, in Hidde's words: "Photograph a tree to add it to your collection and share it on the map." and, on a tree's page, "Share your photo on this tree's page." Android in all eight languages; the website's photo field adds "They're shared on the tree's page." Seen on the iPhone simulator and the Android emulator. Reaches phones with the next iOS and Android builds, the web line with the next deploy.
- Recorded: PRODUCT_COPY.md ("share", not a warning) and CONVENTIONS.md.
- **Left open for Hidde**: the website's thank-you after adding a photo says "We look at every photograph before it goes on a page", not true when the tree already has a lead photo (live first). The emulator holds a debug build now; uninstall before testing the Play build.

## 2026-11-22 reader judge (eighth run): a forest oak above Bad Homburg live

- **New tree**: bad-homburg/bhg_007, The Tall Oak in the Taunus Beeches (Oak, Quercus sp.), a reader's two photographs looking up a furrowed oak trunk among beeches in autumn colour, pinned from the phone's fix about 4 km north-west of the Schlosspark. The reader's words ("one of the older trees here that are now endangered by logging") are quoted as theirs. The place FAQ "Can I see them all in one walk?" now says the forest oak is a walk of its own.
- **Seville sev_009**: I judged the same Goya fig photo the same way (`add`, the reader's photo leads), but the parallel run below had already pushed it, so I kept its version at the rebase.
- Nothing else was waiting: no open reports, no feedback, no unjudged tips, no readers' words to quote. The 38 `mine` leads are our own account's photos and are left alone. Lead 3c544597 (Amsterdam) is ours too and has no file on disk.
- preflight 0 problems, qa source clean, i18ncheck clean.
## 2026-11-22 session: Report and Block on a person's profile, all three surfaces

- The ... top right of someone's profile now opens Report and Block, as on AllTrails and Instagram (Hidde: "Ja, bouw het"). The app's menu was only on rows in Find people; it is now one shared piece used by both places (iOS and Android). The website had no report or block at all; its profile page has them now, writing the same reports and blocks rows the apps write.
- iOS and Android compile; not looked at on a phone. The website part waits for CI's build.

## 2026-11-22 session: three everyday reflexes the reference apps share, on Hidde's yes

- **Website: the phone's Back closes what is open first** (a photograph, any sheet, sign-in) instead of leaving the page, as on Instagram's and Google Maps' websites (Hidde: "1 ja"). One place, lib/overlay-sheet-js.ts, on every page. Tested on the live Totteridge Yew page by injecting the script: Back closed the photo; after closing it with the cross, one Back returned to London.
- **Someone else's follower counts open their lists**, iPhone, Android and web (Hidde: "4 ja"; AllTrails does it). Signed out, it asks you to sign in.
- **Pull to refresh on a person's profile and on Activity**, iPhone and Android (Hidde: "5 ja"). Not on My trees: it is a sheet over a map, where pulling down lowers the sheet.
- iOS and Android both compile; not looked at on a phone yet. The website part is checked by CI's build (no Node here).
- Research behind it: drafts/convention-gaps-2026-11-22.md, ten gaps ranked. For Hidde: block and report on a profile (question 3) and the five small ones (rows 6 to 10) still wait for his word; push notifications later, his call.

## 2026-11-22 reader judge (seventh run, second copy): a reader's photo now leads the Seville Goya fig

- **Seville sev_009 (Glorieta de Goya fig):** the reader's photo shows the same railed round bed, cars and bougainvillea as the Commons lead, and it has the whole crown, which the Commons photo cuts off. It went in as `add`, so the reader's photo now leads and the Commons one moved to the strip. It is filed in September, the month in the photo. The reader's mail is queued in the weekly bundle.
- **This ran in parallel with the seventh run.** Both built Florianópolis and both held the Brussels photo. I kept that run's version and dropped mine at the rebase. Only the Seville verdict, which it had not reached, is new here.

## 2026-11-22 write pass: three trees into the app, the pending pool is empty

- **Product**: three new trees in the app (APP FIRST, no web page until a reader adds to one): the Nevada champion Mondell pine behind UNLV's Carlson Education Building (lvg_015, Nevada Big Tree Register 2023), the holm oak beside White Hall that UNLV calls a state champion (lvg_016; the state register does not list it, and the story says so), and the American hornbeam across from Prospect Park's Camperdown Elm (nyc_029, NYC Parks Great Trees; the register's trunk figure is impossible for the species, so no girth printed). Merged by scripts/build_write_2026_11_22.py; preflight 0 problems; app-only, so the pace is untouched.
- **The pending pool is empty**: every other unpublished entry in `passcheck.py --pending` is already live under another id (Cardiff, Cyprus, Split, Tenerife, Wolverhampton, Fort Greene, Saratoga Park), folded (Paros stone pine into pao_001), or the Birmingham poplar hwp_001, left for the writer after the Birmingham verify claim now in flight. The Tulsa English oak tsa_003 stays out as kept on 11-15. The next write pass needs a verify pass first.

## 2026-11-22 night run: photo-live bundle mail no longer lists photographs taken out of the pages

Rung 1 had already been handled by the seventh reader-judge run (it put Florianópolis live while this run judged the same two photographs, so this run's duplicate commit was dropped). The run took the open web BUG row instead: `flush_mail` in scripts/sightings_publish.py now rechecks every pending photograph against data/cities and drops one the judge later held, rejected or unstripped (`still_on_the_page`, three new tests in scripts/test_sightings.py, row set fixed). Not touched: the iOS app red (read in its log: appsweep's touch-target check, 7 findings, the photo viewer's heart 'photo-like' is 26 by 44 under Apple's 44 by 44; it comes from the same-day work on the opened photo's heart, and widening it is a visible change, so it is left to the session on that screen), the open APP BUG row on the country pick (Swift and Android, needs the app worktree), and sighting 3c544597 (ours, photo not on disk).

## 2026-11-22 reader judge (seventh run): two trees in Florianópolis live, a Brussels photo held

- **New place, Florianópolis (Brazil), two trees from one reader.** fln_001 is a massive twisted tree on a paved waterfront point at Ribeirão da Ilha, with two plaques on its trunk, photographed at dusk. The pin is the photo's GPS fix, confirmed. I filed it as False Kamani (Terminalia catappa) from the leaves, and the story asks readers to confirm. fln_002 is a fig hung with aerial roots in Coqueiros. Its pin was placed by hand, so it is approximate, and its access line says we have not confirmed it stands on public ground. Each photo is filed under its own month (July, May).
- **Held: e4cfea4f (Brussels), sent for bru_034, the Solbosch beech.** The photo shows a different tree: two trunks forking low, alone on an open lawn, in yellow leaf with leaves like a tulip tree's. The record describes a 5.10 m beech with a nine-metre clean bole beside a woodland path. I gave it `other_tree`, so it became a lead, and held it as `doubt_location` because its coordinate is our pin, not where the photo was taken. hold_reply.py only takes website submissions, so no standard mail went out.
- **Readers' words:** the Ragusa fig note (rgs_001) reads like encyclopedic text, so I did not quote it. Its age, about 170 years, is now on the page "by a reader's estimate" (story and age_estimate). The note ends "Proprietario della foto Giuseppe Piazza". That may be the sender signing, or it may mean the photo is someone else's. A session should check whether the photo is the reader's own (`not_theirs` otherwise).
- **Ran in parallel with the sixth run.** Both built the Bremen sequoia. Theirs, with the sign photo, is the one live as hrn_003, and I dropped my copy at the rebase. No open reports or feedback.

## 2026-11-22 reader judge (sixth run): a national heritage sequoia in Bremen live

- **New tree, horn-bremen/hrn_003, "The Nationalerbe Sequoia of Riensberg Cemetery".** It came from the same reader as this afternoon's Focke-Museum oak, through the app, with four photographs: the whole giant sequoia from beside its railed grave plot, the steel sign in front of it, the trunk from below, and its spire above the cemetery oaks. The sign says the Kuratorium named it a Nationalerbe-Baum of Germany on 10 February 2022, one of the 100 most significant trees in the country (Deutsche Dendrologische Gesellschaft with Umweltbetrieb Bremen). The pin is the reader's GPS fix, so it is confirmed. It stands in the Riensberger Friedhof, 245 m west of hrn_002. The 160 years and the 7.3 m girth are the reader's figures and appear in the story only. The story opens with the reader's own words, quoted. The photo is filed in November, the month it was taken.
- **Horn-Lehe now has three trees.** I updated its intro and meta and added a FAQ entry for the sequoia. There is no kept translation to update.
- 3c544597 (Amsterdam) is still our own photo (`mine`) and its file is still not on disk, so I left it alone. There were no open reports, no open feedback and no tips without a photo.

## 2026-11-22 reader judge (fifth run): a 350-year oak in Bremen live

- **New tree, horn-bremen/hrn_002, "The Old Oak by the Focke-Museum".** A reader sent it today through the app with three photographs: the whole oak in autumn yellow, the trunk from below, and a plaque at its foot. The plaque reads "Stiel-Eiche, Quercus robur. Mit rund 350 Jahren eine der ältesten Eichen in Bremen", number 138. The pin is the reader's GPS fix, confirmed. It lands on the path Unter den Eichen in Riensberg (Schwachhausen), about 140 m south of the Focke-Museum and 730 m from the Horner Linde, so it joined Horn-Lehe rather than starting a one-tree place. The age comes from the plaque; the 6 m girth is the reader's and stays in the story only. The photo is filed in November, the photograph's own month.
- **Horn-Lehe now has two trees**, so it gets a place page (`PLACE_PAGE_MIN_TREES = 2`). Its intro and meta name both trees, and a FAQ entry points to the oak. It has no kept translation.
- 3c544597 (Amsterdam) is still our own photo (`mine`) and its file is not on disk, so I left it alone. There were no open reports, no open feedback and no reader words to quote.

## 2026-11-22 reader judge (fourth run): nothing new from readers to publish

- **Feedback 1446** closed `handled`. It is a third copy of the "remove all photos" mail, sent at 12:52, before the 1419 session finished removing them. Every photo is already off and on data/photos-withheld.json. The draft reply still waits for Hidde.
- No reader trees or photos were waiting. 3c544597 is still our own photo (`mine`), and its file is not on this machine. There are no open reports, and reader_words had nothing to quote.
- **Unblocked preflight**: the bell commit (f7c623216) read "See all" from `ui()` in Base.astro, and preflight's chrome check only accepts `chrome()` strings, so it failed. The words were already translated, so this was a false positive. `seeAll` now lives in `chrome()` (site/src/lib/ui-strings.ts) with the same eight translations, Base.astro reads `{t.seeAll}`, and what visitors see is unchanged.
- Also committed the third run's leftover bookkeeping: its willow judgement moved to the top of data/judgements.json, and `pin_checked` was added on the sighting.

## 2026-11-22 reader judge (third run): a weeping willow near Mantua live, an autumn Evelyn Mulberry in the gallery

- **Live**: the Weeping Willow of Via Dante Alighieri (bagnolo-san-vito/bsv_001), a new one-tree place south-east of Mantua. It's a very wide willow whose curtain of shoots falls almost to the grass. The photo was taken about 3 m from a public lane (OpenStreetMap), so it ships with an honest access line: the ground is private and the tree is seen from the road. The reader gave no note or figures, so the story claims no age. The photo is filed in May, from its own date.
- **Gallery**: a reader's November photo of the Evelyn Mulberry (lon_010), showing the fence, prop and stone marker in autumn leaf. It went in as `strip` behind the summer lead, not in place of it: a group of visitors stands at the right and the current lead is a clean reader photo. The first-photo mail went with `--send`.
- **Feedback 1445** closed `handled`: it is the same "remove all photos" mail the 1419 session acted on this morning (all four photos off, data/photos-withheld.json). Its draft reply still waits for Hidde.
- Not judged: 3c544597 is our own photograph (`mine`), not a reader's, and its file is not on this machine.
- No open reports; reader_words had nothing to quote.

## 2026-11-22 session: every photograph of one reader off the site, on their second ask

- **Removed** (feedback 1419, Hidde: "yes remove all his photos"): after the two with faces came down this morning, the reader asked for all photographs off and none uploaded again. The other two are gone too: the Córdoba courtyard through the arch (cdb_002, strip) and the Granada Parador cypresses (gra_007, lead; the tree is photo-less again). Files deleted, manifest entries out. The Granada pin stays where their GPS fix put it (a coordinate, not a photograph).
- **Never again**: data/photos-withheld.json lists their account code. sightings_publish.py skips them on the live-first and judged routes, and preflight's new `check_a_withheld_readers_photo_stays_off()` refuses a city file that carries one.
- Their photos were taken in February and May and sent around 14 November, so the "sent before 2026-10-04" exception did not apply this morning; it was their choice, not our error.
- **Sent on his word** ("Yes, send it"): the reply in their thread, after a live check (neither page carries their photos, the Granada file 404s). Their profile is public by default and may still show their own trees; not changed.

## 2026-11-22 session: why profiles have no flag

- Only 186 of 977 accounts had a flag (Apple 5 of 353, Google 119 of 299, email 62 of 325). Both apps save the flag with an upsert of user_id and country only; Postgres checks NOT NULL on the would-be insert before the conflict, so the empty display_name refused every app save (reproduced on apptest: 23502). The website PATCHes and works. Android accounts made 11-21 and 11-22 all lack a flag.
- Fix: supabase/flag-upsert-fix.sql, a BEFORE INSERT trigger that takes the existing name when an insert brings none. Works for every installed build; both apps retry while the flag is empty.
- For Hidde: paste supabase/flag-upsert-fix.sql in the Supabase SQL editor and Run.
- Owed: the apps' saveCountry should PATCH like the web (next iOS and Android builds); a test that the save round-trips (SignedInRoundTrip).

## 2026-11-22 reader judge (second run): Barmstedt and Cassano d'Adda live, first photographs for the Bristol cedar and the Donnafugata figs

This run worked through the same queue as the run below. It rebased onto that run's work and kept it (Tewkesbury, Vernon Oak, the three strip photos, Tsagarada held as `doubt_photo`). Only what that run left is added here.

- **New trees, readers' own** (every photograph viewed):
  - **Barmstedt, The Thousand-Year Oak (bms_001)**: the hollow three-stemmed oak by the Rantzauer See, north of Hamburg. The reader linked de.wikipedia, which gives natural monument 01/03 (Kreis Pinneberg, 1997), about 600 to 650 years and 6.75 m girth in 2011. The coordinates match the reader's GPS. One-tree place.
  - **Cassano d'Adda, The Old Mulberry of Taranta (cda_001)**: an ancient pollarded mulberry on props in front of houses, seen from the street. The pin was placed by hand, so it is approximate. Species left as Morus sp.: the reader says black, and the page asks readers which it is. Their 400 years is stated as theirs. One-tree place.
- **First photographs**: Bristol's Victoria Square cedar (bri_007; pin moved 22 m to the reader's fix, now confirmed) and Ragusa's Donnafugata figs (rgs_001; pin moved 26 m to the fix, now confirmed, 3 m from the MASAF register entry). That photo did reach the queue after all. The reader's second copy of it (b478e704, "not sure which tree") is settled onto rgs_001, and report 1000122 is closed.
- **Strip**: one more from Fanal for the Witch Tree (mdr_005): a single twisted til in fog. As with this reader's other photos, it cannot settle which trunk is the Witch Tree.
- **Held**: "A tree near Trento" (404ad610) as `wrong_subject`. It is a lakeshore forest in autumn colour with no single tree in it, so no mail goes.
- **Report 1000123**: the Tewkesbury reader moved the pin on their own new tree, 55 m from the photo's GPS. The photo shows the whole tree from close by, not from far off, so the GPS stays. Closed `holds`, no mail.
- **Corrected in this run**: before seeing the other run's verdict, this run wrote a standard `no_location` reply on submission 1433 (Tsagarada). It was withdrawn before any knock sent it (reply_text and outcome cleared, replied_at still empty), so the other run's `doubt_photo` with no mail stands.
- **Still open**: tip:1435 (Como, sighting 57F46EDF) and submission 1414 (Tsagarada with a location from its photograph, 39.38674, 23.17459, sighting C50BB407). Neither photograph has reached out/sightings/ or the leads. 1414's location is enough to place the plane once a usable photograph exists.

## 2026-11-22 session: who gave a heart, Activity, and Worth the visit written out (web, iPhone, Android)

What changed in the product (Hidde: "kun je ook zien als je een hartje krijgt wie je dat heeft gegeven?", design in drafts/design-2026-11-22-heart-who/product.html, the bell "voor nu is het ok"):
- The count beside a visitor photograph's heart is its own tap and opens who gave one (signed in only; a private profile shows as "A visitor"). The heart sits right after the time, in the apps as on the web.
- A bell: top right of Discover in the apps, beside your face in the website's bar (on the phone a menu row "Activity" and a dot on the menu button). It opens Activity: the hearts other people gave your photographs, one row per photograph, New above Earlier, a dot while something came after you last looked, the same on every device.
- "Worth the visit · 2" written out beside the thumb, no background (reverses 2026-09-04's "de worth the visit tekst mag helemaal weg", now that a heart sits on the photographer's line).
- Fixed on the way: the app's opened photograph showed the licence line instead of a visitor's name, time and heart.
- Privacy page: signed-in visitors and the photographer see who gave hearts; we keep when you last opened Activity.
- Commit b175ac666 carries this message but holds two other sessions' LOG entries (Nick reply, Waste article), which were staged in the shared checkout; their text is unchanged.

FOR HIDDE: paste supabase/photo-hearts-who.sql in the Supabase SQL editor. Until then the list stays empty, the bell has no dot and Activity is empty. The apps carry it from their next build.

## 2026-11-22 session: reply to Nick (Bristol) sent

- Sent on Hidde's "Send it": the reply to feedback 1381 (his redwood correction), in his own mail thread, from info@. It says bri_023 is now a coast redwood and the bri_015 cypress pin sits 12 m from his OS reference, and asks whether both are right now. Text in drafts/reply-nick-bristol-redwood-2026-11-22.md; logged in the send log, row 1381 stamped `replied_at`. No data change needed: the reader judge had fixed both trees on 2026-11-21.

## 2026-11-22 reader judge: a new place, Tewkesbury, for a reader's great beech; the Vernon Oak's first photograph

- **New: Tewkesbury, The Great Beech of Tewkesbury Abbey (tew_001)**. A reader sent this beech from the abbey grounds with the photograph's own GPS. Looked at both frames: a huge fluted grey trunk with roots flaring over the lawn and low spreading limbs, the reader standing at its foot for scale, autumn leaves. Their girth (about 7 m) and age (about 250 years) are on the page as theirs; their words open the story. It is a one-tree place: intro, question block and three FAQ written. Filed under November from the photo's own date.
- **Sheffield, Vernon Oak (shf_002)**: its first photograph, from a reader. The whole oak in the pavement of Vernon Road in low autumn sun, matching the recognition line. Their coordinate is our own pin, so the pin did not move.
- **Strip only, 3 photos**: two of the Hundred-Horse Chestnut (sal_001; the propped stems in April, bare, and the crown in flower from beneath) stay behind the in-leaf lead. The Witch Tree of Fanal (mdr_005) gets a shot of the Fanal grove in fog; it shows the grove, not that tree, so never the lead.
- **Held, doubt_photo: tip-1433, the Tsagarada plane (Pelion)**. The picture is the tree at night under snow, with black letterbox bars like a screenshot of a shared picture, so it may not be the reader's own. No mail. The tree is already the famous lead in data/leads/_famous-greece.json, waiting for a verify pass. Another reader sent the same tree this morning with a GPS fix (submission 1414); its photo has not come in yet.
- **Report 1000121, Perth Old Jarrah Tree (per_005)**: our pin was a rounded approximate one; the reader's hand-placed spot 99 m away is now the pin, still approximate. Closed with the standard pin thank-you.
- **Left open for the next run, photos not here yet**: tip:1435 (Como, sent at 11:52 with a photo location) and report 1000122 (Ragusa, "which tree", sighting B478E704, Donnafugata figs). Neither photo has reached the queue, so neither was judged blind. The `mine` lead 3c544597 still has no file. Feedback: nothing new. Reader words: nothing to quote.

## 2026-11-22 session: Android build 5 sent to Google for review

- **In review** (Hidde: "Ja, indienen"): build 5 (0.1.0) on both closed tracks, Alpha and Beta (Google Group), full rollout, replacing build 4. Hidde had uploaded the bundle to the library but it was in no release; the session put it into an Alpha release and a new Beta release in his Chrome and saved both. Play Console then showed "Wijzigingen worden beoordeeld" (pre-review checks up to 14 minutes, then Google's review). Only warning: no native debug symbols (MapLibre), as on build 4.
- **Live the same day**: Play Console shows Release 5 (0.1.0) green on both closed tracks, Alpha and Beta (Google Group), updated 22 Nov; Publishing overview has nothing waiting for review.

## 2026-11-22 reader judge: the Vienna pagoda tree gets the same reader's photograph

- **Vienna, The Pagoda Tree of the Stadtpark (vie_016)**: the same reader who sent the plane (below) sent this one from 8 m off our pin, taken today. Looked at it: pinnate leaves still green, deeply furrowed trunk forking low with one stem leaning hard away, as the recognition line says, the park balustrade behind. It now leads; the Commons photograph moves to the strip. Filed under November from the photo's own date. The reader's mail joins the weekly bundle with the plane's.
- This run also judged the plane and agreed; the earlier run's entry for it is kept. Nothing else waited: no reports, tips, feedback or notes to quote. The only lead listed (3c544597, Amsterdam) is our own account's photo (`mine`) and has no file here.

## 2026-11-22 session: the Species filter says when a search finds nothing (iPhone and Android)

- **What changes in the apps** (Hidde: "build it for both apps"): on the map's Species sheet, a search with no match showed a blank grey screen. Both apps now show "No species by that name." where the list was, the website's own line, in small grey text. Android in all eight languages from the site's translations. Seen on the iPhone 17 Pro simulator (no match; "oak" still lists every oak) and the Android emulator.
- **For Hidde**: in the next iPhone build and Android build 6, not in build 5. Nothing archived or uploaded.
- Also checked before this: the signed build 5 on the emulator, signed out (map, pin card, its close, Discover bookmark, empty species search, My trees, Collect), no crashes. Signed-in not walked on the Play build.

## 2026-11-22 reader judge, a second run beside the first: the Vienna plane

- **Vienna, vie_023** (The Plane of Dr. Karl Lueger-Platz): a reader's photograph of the buttressed trunk and low limbs in autumn leaf, benches round it on the square. It now leads, and the old photograph moves to the strip. Filed under November. The reader's mail is queued in the weekly bundle.
- This run judged the same Antwerp, Munich and Amsterdam photographs as the earlier "Antwerp copper beech" run. It agreed on everything except Munich's wider shot (3210008a), which this run would have added. I kept the first run's verdicts, and that file stays off the site. No reader was mailed twice: the mails were only queued, never sent.
- Nothing else waited: no reports, no tips, no feedback. The waiting leads still have no file on this runner.

## 2026-11-22 session: Waste Magazine article, first version

- drafts/waste-article-2026-11.md: the Crann article turned to Spain for Waste Magazine (Spanish to send, English to check), seven trees (Granada cypress, Escaleretas pinsapo, Lecina carrasca, Cartuja ombú, Pino Gordo, El Titán, Retiro ahuehuete), seven open-licence photos with credits, bio, cover mail. Waste is cited on seven of our Granada trees; the cover mail says so. Nothing sent; waits for Hidde's read.

## 2026-11-22 reader judge: two off-list holds reversed on Hidde's ask (Malmö weeping beech live, Witch Tree photo in the strip)

- **New tree, malmo/mlm_001, The Weeping Beech of Magistratsparken** (tip-763, sent 2026-11-15 through the website): the whole tree fills the frame, a three-peaked dome of hanging branches, summer daylight. Held on 11-15 for "no GPS and no written source", neither on the closed list. Reader's words quoted unnamed ("Majestic Hängbok"), story 217 words, nothing about age or girth invented. Pin **approximate** at the park's centre (OpenStreetMap way 28482241): no source places the tree inside the park (Overpass timed out, Commons geosearch and a web search found nothing). Malmö is a one-tree place, so no place page; the tree page is live as a reader-found tree. The congratulation mail waits for the deploy (tree_approved.py: "not in the live feed yet"); the knock sends it.
- **The Witch Tree of Fanal (madeira/mdr_005)**: the reader's backlit til in fog (sighting 89fa82ed) goes in the strip, not the lead, via sightings_publish.py `strip` (re-queued from the 11-15 queue entry). The tree's own lead (an iNaturalist photo) is still `held`, so the reader's photo may be the first picture the page shows (not checked in the built page).
- Verdicts: lead:tip-763, sight:tip-763 and sight:89fa82ed publish, each with Hidde's word filed as agreed. qa --source-only clean, preflight 0 problems, i18ncheck clean.

## 2026-11-22 reader judge: the Antwerp copper beech gets its first photograph

- **Antwerp, ant_001** (The Copper Beech of Sint-Willibrorduskerk): a reader's photograph from the website is now its lead, the first picture the tree has had. It shows the whole beech filling its little square in low November sun.
- **Munich, muc_006** (The Fern-leaved Beech): a reader's photograph is the new lead and the Commons one moves to the strip. It shows the trunk bare, from across the Schwabinger Bach, and matches the Commons trunk from the other side. A second, wider shot by the same person minutes earlier was rejected as a duplicate.
- **Amsterdam, ams_002** (Leidsebosje Planes): a reader's backlit shot goes in the strip behind the reader's photograph that already leads.
- All three are filed under November (`taken_month` 11). Readers were mailed through sightings_publish.py --send.
- Notes: I read 12 new tree notes and hid none. A Bristol note gives OS grid reference ST 55327 75129 for bri_015, which converts to 12 m from its confirmed GPS pin, so the pin stays.
- Nothing else waiting: 0 open reports, 0 tips, 0 feedback without a verdict, 0 words to quote. The 37 older waiting leads in _sightings.json are all our own account's test photographs with no file on this runner, which fetch_waiting_photos.py skips. 3c544597 (Amsterdam, near ams_032) is one of them; I did not judge it because it has no file.

## 2026-11-22 session: inbox replies, and every new ambassador now gets the ambassador mail

- **Product**: a badge given through `ambassador.py --grant` (a reader's yes by mail, the reader judge's route) gave no mail at all; only the app's button sent "Looking after <place>". Now `--grant ... --send` sends that standard mail once per person, and a place with one tree gets it without "check the list / remove" (`request_mail()`). BRIEF_READER_JUDGE.md says `--send`. Catch-up `--welcome-missing` found three who never had it and mailed them on Hidde's word: Joanna (Leamington Spa), Teresa (Laténa), David (Castlemaine). The one-line ask under the congratulation mail no longer counts as that mail.
- **Held for Hidde**: Hugo (Lisbon, Quercus), the one other account ambassador without it; the six mail ambassadors with no account (Copenhagen, Florence, Lisbon, Prague, Stockholm, Brighton) are personal threads of his.
- **Sent on his word** (outreach_send): Devika (CTV, interview moved to the weekend after or a weekday), Martin, Arthur, Hélène, Mark, Simon (Android test), Michèle (Réno-Valdieu, winter photos), Beresford (two photos with faces offline, checked live first; feedback 1419 closed).
- **Breakage found**: ~/.ancienttrees-mail.env holds a placeholder SUPABASE_SERVICE_KEY, which made account codes wrong when both env files were sourced; ambassador.py now reads the key through people.service_key(). The placeholder line itself is his file.
- Android test score: 8 willing of 12, none joined yet. Waiting: Andrea, Waste Magazine, Kate, readers 1358 and 1362.

## 2026-11-22 session: Android build 5 built for Play (Hidde: "ok lets do it")

- **Fixed, live on build 4 and dead for every tester**: the bookmark on Discover's tree tiles did nothing (no save signed in, no sign-in sheet signed out), because Discover's tab root never got the save action the other tabs have. The daily ButtonWalk had been red on exactly this since 11-20 and nobody acted on it. Seen on the emulator on build 4 (dead) and on the fix (sign-in sheet; filled mark and "Added to Want to visit"). Commit on main with versionCode 5.
- **Build 5** (0.1.0, versionCode 5): out/play/ancient-trees-0.1.0-5.aab, signed with the upload key. Carries the species picker crash fix (30193f371, GroupedSectionTest) plus everything on main since build 4 (photo heart, clear dots, profile map tabs, photo dates, spam hint). Unit tests green; android.yml on the push was running at upload time.
- **Crash proof**: ExitWatch is unchanged since build 4, whose proof stands (11-20), and build 4's first real crash on a stranger's phone arrived with its line. Not re-run for 5.
- **Not done**: the instrumented walks locally; MapLibre native symbols (Play's warning stays). **Still open from the walk**: on the Map tab signed out, a pin's sheet "Close sheet" button does nothing (red since 11-20).
- **Trap for the next session**: the shared emulator held the Play-signed build, so `adb install -r` of a debug build failed quietly and the old app kept running. Uninstall first.
- **For Hidde**: upload the .aab to Alpha and Beta (Google Group) in Play Console and send for review.

## 2026-11-22 reader judge: a redwood joins the Leamington oak

- Leamington Spa has a second tree (lsp_002), so it now gets a place page. The same reader who sent the Elizabeth Park oak sent this one: a towering red-trunked sequoia at the entrance to Victoria Park. The whole-tree shot leads and the trunk shot sits in the strip. The reader measured it at 450 cm round, and the page states that as their figure. They placed the pin by hand, so it stays approximate. They called it a coast redwood, but the hanging cord-like shoots in both photographs look like a giant sequoia, so the species is Giant Sequoia and the story asks readers which it is. The place's intro, meta, question texts and FAQ now count two trees. No kept translation exists for this place.
- Nothing else waited: no queue photographs, no open reports, no feedback, no tips. Lead 3c544597 (Amsterdam, our own account, `mine`) has no photograph on this runner, so it is left unjudged for a run that has the file.

## 2026-11-22 session: New from visitors stays up; deploys unblocked

- **Why the homepage row vanished**: every deploy since 11-21 22:52 failed qa on one line, the Morris weeping beech's Sources line printing the slug of its blog source ("morris hidden gems", a banned phrase). The live build fell eleven hours behind, none of the 12 newest visitor photos were in it, and the row hides under four tiles.
- **Fixed**: the source named in words (phl_020, URL in verify_notes); `pathHint()` in tree-sources.ts now skips a slug segment carrying a phrase from copy_rules.BANNED_WORDS (read at build), so a cited slug never fails a deploy again. Seven other trees cite such slugs, harmless while each is the only link on its host.
- **The row never waits on a fresh build**: web, iOS and Android ask for 24 and page back through visitor_photos when fewer than four are known (live check against the stale build: 10 tiles). Web paints at once from the public call (it waited for page load, then the sign-in check); a signed-in visitor gets the same tiles repainted with profile links. App tests NewFromVisitorsTests / NewFromVisitorsTest, 4 of 4 each; simulator shows the row with a bundled feed 173 trees behind. The app fix ships with the next build.
- Two stray thumbnails only on the Mac (bat_003, cdb_001 hashed -250.jpg) blocked the pre-push hook; moved to out/tmp/stray-photos/.
- **The miss**: the start brief said deploys had not passed in 14 runs, and the reader-judge runs kept dispatching deploys for eleven hours without reading the failure.

## 2026-11-22 reader judge, a second run beside the first: two Copenhagen photographs

- Thorvaldsen's Robinia (cop_003) has its first photograph: a reader's photo of a black locust standing alone on the Slotsholmen cobbles at our register pin. The Proviantgarden mulberry (cop_001) gets the same reader's yellow autumn shot in the strip. It is behind the lead because scaffolding stands round the tree today.
- Breakage: this run judged the same queue in parallel with the run below and built Gwytherin, Llangernyw and Bristol a second time. On the rebase it dropped its own copies and kept that run's. Each run sent its own photo-live mail, so the Llangernyw and Bristol readers may have had two.

## 2026-11-22 reader judge: the Gwytherin yews, and a reader's Llangernyw yew takes the lead

- New place and tree live: The Gwytherin Yews (gwytherin/gwy_001), two old yews either side of the churchyard path at St Winifred's, Gwytherin, Conwy, sent through the app with four photographs. The lead shows both crowns; two trunk close-ups go in the strip. Pin from the photograph's own position (confirmed); the reader's "2,000+ years" on the page as their estimate; photos filed in November from their own date. A one-tree place, so no place page (PLACE_PAGE_MIN_TREES 2); its texts name Llangernyw, a few miles north.
- Same reader, the Llangernyw Yew (lgy_001): their evening shot of the whole split trunk is now the lead (verdict `add`, the old lead moved into the strip). The light score said underexposed. A reader's photo is never refused on light, and this one is the better picture. Their night shot was not used.
- Bristol, Monterey Cypress at Bishops Knoll (bri_015): a reader's view of the crown through the wood went into the strip, behind the existing lead.
- tip:1423 is the same reader, the same spot and minute as the Gwytherin send, with no words and no photograph: its verdict names gwy_001.
- Left: lead 3c544597 (Amsterdam, our own account), photo still not on this machine. The older waiting leads in _sightings.json are September and October ones, nearly all from our own account (`mine`), as earlier runs left them.
- No open reports, no feedback without a verdict, no reader notes waiting to be quoted. The photo-live mail for the two existing trees went through sightings_publish.py; the congratulation for Gwytherin goes through tree_approved.py on the next knock.

## 2026-11-22 reader judge: a banyan joins the Delhi peepal

- New tree live: The Banyan by the Arcades (delhi/dlh_002), an Indian banyan whose trunk is a bundle of root pillars beside a Mughal pavilion near Humayun's Tomb, sent through the app by the same reader as the peepal. Pin from the photograph's own position (confirmed), 302 m from dlh_001; photo filed in November from its own date. Delhi now has two trees, so its place page comes back (PLACE_PAGE_MIN_TREES 2); intro, meta, question texts and FAQ rewritten for both trees. The garden is still not named on the page (it looks like Sundar Nursery, nothing confirms it).
- Left: lead 3c544597 (Amsterdam, our own account, "not sure which tree" near ams_032): its photo is not on this machine, so it was not judged.
- No open reports, no feedback without a verdict, no reader notes waiting to be quoted. No mail sent; the congratulation goes through tree_approved.py on the next knock.

## 2026-11-22 reader judge, a second run beside the first: four more Emmen trees from the same reader

- Ran at the same time as the entry below and judged the same ten photographs the same way; this run's files are kept because they also carry four photos the other run had not reached: the Lime of the Noordeind (emm_001) and the Oak at the Long Grave (emm_003) get their first photograph, the Plane of the Bonifatius Park (emm_006) too, its pin moved 20 m to the reader's fix and now confirmed, and the Oak in Hunebed D42 (emm_002) takes the reader's golden-light frame as its lead, the old photo moved into the strip. Story wording of emm_005 and zwo_016 is this run's (no colon, same facts). No mail went out from either run: all nine wait in the reader's weekly bundle.
- Left open, as below: 3c544597 and the older own-account leads have no photo on this machine. qa source clean, preflight 0 problems, i18ncheck clean.

## 2026-11-22 reader judge: five Dutch trees get their first photograph

- **Five trees that had no photo now have one, all from one reader's summer walk**: The Plane by Restaurant Urbana (zwo_013, Loetje sign in shot), Huis de Paddestoel's Swamp Cypress (zwo_016), The Weeping Beech of Park Boschwijk (zwo_020), The Beech of the Boschwijk Avenue (zwo_002) in Zwolle, and The Copper Beech of Nieuw-Schoonebeek (emm_005) in Emmen. Each is within 5 to 20 m of our pin, species and description checked against the pixels, taken_month from the photo's date. Pins were already confirmed, nothing moved.
- be8ad361 rejected as a duplicate: the same frame as 3b40b69a, which went up.
- The reader photo made emm_005 and zwo_016 indexable, so their colon sentences tripped preflight; both rewritten without the colon (emm_005 in English and in the nl overlay).
- Left for the next run: lead 3c544597 (Amsterdam, 52.3972,4.8739, "not sure which tree"): the photo is not on disk, never judged blind. No open reports, no open feedback, no tips without a verdict.

## 2026-11-22 reader judge, a second run beside the first: one bug recorded, one report closed

- Two reader-judge runs took the same work at once; this one's Delhi tree and takedown were dropped for the first run's (below), nothing lost.
- **Report 1000119** (Tsagarada pin) closed `holds`, no mail: not a tree of ours (the Tsagarada plane is only an unpinned famous lead), so it is the reader placing their own new tree; their tree is judged when it arrives.
- **Escaped bug** ESC-2026-11-22-photo-live-bundle-mail-sightings-publish: the bundle mail that reader 1419 answered told them six photographs were on the pages that had been held or rejected on 11-15 (Muckross, Dartmoor, Crom, Belfast twice, Palma); `flush_mail` never rechecks pending items against data/cities. Rung-2 work for a session. The draft reply to 1419 might mention it to Hidde: some of the photos they saw listed were never up.

## 2026-11-22 reader judge: a Delhi peepal live, two photos with faces taken down

- **Live**: delhi/dlh_001, The Peepal on the Plinth, a huge sacred fig on a stone plinth in a garden near Humayun's Tomb, sent through the app with a GPS fix from the photo (confirmed pin). Both photographs viewed; the second goes in the strip. New one-tree place Delhi (India is out of focus for our own research only, never for a reader's tree). The garden is not named on the page: the pin fits Sundar Nursery, but nothing confirms it.
- **Photos with faces removed on request** (feedback 1419, a reader's mail reply: "Please remove the photos, as include faces"): of their four live photographs, the two with a person in them came out of the strips with `sightings_publish.py --unstrip` (bat_003 Bath Circus planes, cdb_001 Córdoba olive). cdb_002 (distant figures only) and gra_007 (no people) stay. A confirming answer is drafted in drafts/reply-reader-1419-2026-11-22.md; row closed `needs_hidde`. For Hidde: the reply to 1419 is ready to send; the app's bundled catalogue still names the two photos until the next build.
- **Left open**: report 1000119 (a moved pin, "Oriental Plane in Tsagarada, Greece"): no tree of ours by that name or within 2 km; probably a reader's own tree that has not reached our data yet, so it stays open for the next run. Lead 3c544597 (Amsterdam, our own account) still has no photo on disk.
- Checks: qa source-only clean, preflight 0 problems, i18ncheck clean.

## 2026-11-22 fourth attempt: nothing shipped, and why

No claims stood. READY leads: 2 (york, guimaraes), under the six-candidate minimum. `--pending` holds only duplicates and id clashes. Staged focus cities portland, munich and vienna are refused as full; translations are paused by `TRANSLATIONS_OUT`; the register backup says BUILD. The one unjudged reader photo (3c544597) is not on disk, so it stays open rather than judged blind. A deploy dispatch is refused (403) here; the last dispatched deploy (04:12) failed before fix 64bd619, so a session should re-dispatch one. Next: a verify pass on a city with room, or iNaturalist as a new source.

## 2026-11-22 night run, third attempt: nothing shipped, shelf still dry
No product change. Released the standing stuttgart claim (wall for 48h). READY has 2 leads (York, Guimaraes), under the 6-candidate floor; the "awaiting a writer" files are stale or duplicates. Portland refused (full, 33 of 30). Dublin claimed and released at once: 0 of 9 leads carry a coordinate, so a pass would fail on the pin (now a 48h wall). Translations stay paused (TRANSLATIONS_OUT) and register scouting says BUILD with nothing left. The blocker is the same as the last attempts: supply needs a coordinate source (a rendering browser for Birmingham's Botanical Gardens list, or iNaturalist points), not another search pass. Health reds (deploy and smoke on schedule, app catalogue 175 behind) not touched.

## 2026-11-22 04:39 UTC run (rung 2: red deploy)

- Deploy was red on two qa lines. Fixed both in data/cities/philadelphia.json: the verify note on the Morris Arboretum weeping beech held the banned phrase "hidden gems" (a source's post title, rendered on the page), reworded; Bartram's Ginkgo hero was the 375px iNaturalist medium file, now large.jpg (768x1024, same photograph and licence). Preflight 0 problems. Not rebuilt here; the next deploy confirms.
- Rung 1: 11 new tree notes read, none on the hide list, marked seen. Sighting 3c544597 (Amsterdam) still has no file on this runner, no verdict written.
- Smoke test failure of 11-21 not investigated this window.

## 2026-11-22 reader judge: Shanghai's great plane

- **New tree, new place: The Great Plane of Zhongshan Park (shanghai/sha_001).** A reader sent an "Oriental Plane" from Zhongshan Park with the GPS fix in the photograph: the whole tree behind its rail in a bed of red gravel, the crown just turning. Beside it stands the Shanghai greening bureau's sign. It names the tree as ancient plane no. 0909 and says it was planted in 1866, a gift Thomas Hanbury brought from Italy for Mr Hogg, whose garden became the park. It calls it "East China's No. 1 Plane" (widest crown, thickest trunk, five adults to reach round) and lists it as one of the park's twelve views, "A Lone Tree Braving the Frost". The sign is the source. The species is `Platanus sp.` (the sign does not say which plane, and the story gives "oriental plane" as the reader's word). The reader's 160 years matches the sign. Their girth of 1500 cm is left off because the sign's five adults suggests a slip. Pin confirmed, photo filed as November. Their second picture, a phone translation of the sign, is not published. One tree, so no place page. City names looked up (`city_names.py`).
- **Still not judged: sighting 3c544597** (Amsterdam-Noord, `mine: true`): the photograph is not on disk, the third run in a row. A session with the key has to fetch it. No reports open, no feedback waiting, no reader words to quote. preflight 0 problems, qa source clean, i18ncheck clean.

## 2026-11-22 reader judge: a reader's Pando in autumn

- **Pando (fish-lake-utah/fsh_001) has a reader's photograph as its lead.** Taken 2020-10-07 inside the grove: a white aspen stem in front, the identical stems in yellow leaf behind. Quaking aspen, fits the page; `add`, so the old lead moves to the strip, filed as October. The GPS fix is 437 m from our pin, inside the clone's 106 acres, so the pin stays. Their three further frames (a wide shot of the yellow hillside among them) are not published: sightings_publish.py takes only the main file. The live-photo mail went through the script.
- **Still not judged: sighting 3c544597** (Amsterdam-Noord, `mine: true`, so one of our own accounts): its photograph is still not on disk, the second run in a row. No reports open, no feedback waiting.

## 2026-11-22 reader judge: Kumamoto Castle's Great Ginkgo

- **New tree, new place: The Great Ginkgo of Kumamoto Castle (kumamoto/kmm_001).** A reader sent it as "Ginkgo near Ueki" with three photographs: the whole crown turning yellow above the castle walls, the double trunk inside its fence, and Kumamoto City's sign. The sign and the city's old-trees page (city.kumamoto.jp/kiji00353094) give the story: said to be planted by Kato Kiyomasa, the origin of the name Ginkgo Castle, burned in 1877 and regrown from the stump; a male tree that bears no nuts. The reader's "about 400 years" is on the page as theirs, belonging to the roots. Pin: the reader's own hand-moved spot by the keep (report 1000118, 148 m from their first pin), approximate; the report closed `holds`, no mail (a move on their own new tree). Paid entry. One tree, so no place page yet; congratulation mail waits for the deploy.
- **Not judged: sighting 3c544597** (a tree near 52.397, 4.874, Amsterdam-Noord): its photograph is not on disk. Left for the next run.
- No feedback rows open, no reader words to quote. preflight 0 problems, qa source clean, i18ncheck clean.

## 2026-11-22 night run, second attempt: nothing shipped

No product change. Shelf has 2 READY leads (York, Guimaraes), under the 6-candidate floor; the 386 "awaiting a writer" are stale files or duplicates of live trees. Verify pass on Birmingham found no new tree (14th dry pass; Moseley oak ATI 64085 alive but park-level pin only; the Botanical Gardens plant explorer is the one untried route to tree-level pins). Graz and Nuremberg claimed and released at once (under a quarter of leads carry a coordinate), both now 48h walls. Portland refused (full). Needs a coordinate source before more verify passes in these cities. Standing health reds (deploy and smoke failing on schedule, app catalogue 173 trees behind) not touched this attempt.

## 2026-11-22 reader judge: a second reader's photo of the Gennett Poplar
- **Chattahoochee National Forest, The Gennett Poplar (gnp_001)**: a second reader sent a photo from the same August 2024 visit: one visitor and two dogs at the foot, with the whole trunk rising into the crown. It is now the lead because it shows the height the first photo cropped. The first reader's photo with two visitors moved into the strip. Both are filed as August.
- Lead 3c544597 (near Amsterdam's Last Elm, sent by one of our own accounts) has no file on this machine. It was not judged and is left for a run that can fetch it.
- No open reports, tips, feedback or reader words to quote.

