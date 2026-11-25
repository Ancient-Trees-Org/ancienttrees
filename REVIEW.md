# REVIEW — the fresh-eyes findings

Written daily by the Fresh-eyes review workflow (06:10 UTC): a separate,
empty context reads the last day's changes and the built site against the
corpus, and writes findings here, newest first. It never fixes anything.

Severities: **BLOCKER** (the site is wrong or broken; runs treat as rung 2),
**WARN** (drift or risk; rung 3), **NOTE** (worth knowing, no action forced).

## 2026-11-25 code (full)

Nothing new in the code. Coverage was partial: pattern sweeps (force unwraps, `!!`, `[0]`/`first()`, `uniqueKeysWithValues`, GlobalScope, scroll/input listeners) over the iPhone app, Android app and site scripts, then reading each hit (SuggestedPeople.build, People.swift, CatalogueStore.kt, TreeDetail.kt YourPhotos, MapSearch.kt SearchIndex, map-filters-js, people-js). Every hit was guarded. Not read line by line: the largest Screens and Compose files. The next full sweep should not rely on this one.
"FOR HIDDE" appears only on judgment calls no run may make alone.

An empty day says "Nothing found." A reviewer that never finds anything is
suspect; a reviewer that finds fifteen nitpicks a day is worse.

---

<!-- archive-index -->

**Older entries live in the archive**, moved by `scripts/archive_logs.py`, nothing deleted:

- [2026-11](archive/REVIEW-2026-11.md)
- [2026-10](archive/REVIEW-2026-10.md)
- [2026-09](archive/REVIEW-2026-09.md)
- [2026-08](archive/REVIEW-2026-08.md)

So absence from this file is not evidence something was never tried: `grep -ri "<place>" archive/` before concluding a hunt is new. Re-running an exhausted hunt is this project's most repeated waste.
<!-- archive-index -->
## 2026-11-25

Web half: the last 24 hours were reader-judge photograph batches (Turin ginkgo, Madison tupelo, Tokyo pine), vendored photos, a leads hand-back and an Android crash fix. Turin, Madison and Tokyo pages hold no em dashes. Four earlier WARNs still stand in site/dist (grep today), replacements as in the 2026-11-21 entry:

- WARN site/dist/miami/baobabs-of-collins-park.html, key-west/strangler-figs-of-the-key-west-cemetery.html still carry "writer must not invent any" (ninth review; public copy never narrates process).
- WARN site/dist/explore.html "Each pin opens a tree with its age, its species, why it is worth the walk..." (nineteenth review).
- WARN site/dist/contribute.html "verified against independent sources" (thirtieth review; false since 2026-10-12).
- WARN site/dist/collections/ancient-oaks-of-europe.html and collections/europes-most-remarkable-yews.html "every coordinate verified" (tenth review; hard rule 2; the yews page is new to this list). The sentence also reaches the app, so fix the feed text.

App half (iPhone SE: directions, early-adopter-sheet, early-adopter, explore, feedback, map-bar): looked at all six.

- NOTE APP explore.png (Discover): the hero says "Autumn is here" and "538 trees at their best this month", but the "At their best now" cards below show full summer-green crowns (Baarn, Leiden). The claim and the pictures disagree; check the best_time photos are in season.
- NOTE APP feedback.png: behind the sign-in sheet, a screen titled Feedback says "You need an account to send a tree", a promise about another flow.
- NOTE APP directions, early-adopter, early-adopter-sheet and map-bar read honestly; no findings.

## 2026-11-24 compliance

- privacy-date-stale: the privacy page's "Last updated: 10 November 2026" did not move though the page changed on 11-18, 11-20 and 11-22, and it promises the date changes with it.
- privacy-mail-route-sentence: "Mail we send goes out through Resend" is not the whole route; replies and ambassador mail still go through Gmail.
- Checked and still true: hearts and who gave them, photo month, profile links on notes and photos, the 90-day error reports. Open row hans-photos-app-only-yes stands, not repeated.

## 2026-11-24

Web half: the last 24 hours were reader-judge batches (East Hampton to six, Willistown to four, the Oslo willow, the Magdalen Plane, Albuquerque, Greenwich, Laurel Hill) plus deploy, mail and qa speed work. The new East Hampton, Willistown, Oxford and Oslo pages hold no em dashes. Four earlier WARNs still stand in site/dist (grep today), replacements as in the 2026-11-21 entry:

- WARN site/dist/miami/baobabs-of-collins-park.html (and key-west strangler figs, gpx, api/trees.json) still carry "writer must not invent any" (eighth review; public copy never narrates process).
- WARN site/dist/explore.html "Each pin opens a tree with its age, its species, why it is worth the walk..." (eighteenth review).
- WARN site/dist/contribute.html "verified against independent sources" (twenty-ninth review; false since 2026-10-12).
- WARN site/dist/collections/ancient-oaks-of-europe.html "every coordinate verified" (ninth review; hard rule 2). The same sentence now shows in the app (collection.png, "Every entry is publicly accessible, every coordinate verified"), so the fix must reach the feed text, not only the web page.

App half (iPhone SE: collect-ticked, collect-voted, collection-tab, collection-tab-full, collection, contribute): looked at all six.

- NOTE APP collection-tab-full.png (signed-in test account): both collected trees render as the same grey-green placeholder tree with only an "Amsterdam" chip and no tree name or photograph; a person cannot tell what they collected. Fine if the test fixture has no photos, a real gap if a collected tree without a lead photo looks like this.
- NOTE APP collect-voted.png: the note placeholder "Leave a note: share something you'd like the next visitors to read about this tree" uses a colon to join two clauses; "Leave a note for the next visitors" would do. The Wilhelminalinde "128 years old" is stated flat while the tree's own age is an estimate (age_basis); check it reads "about" elsewhere.
- NOTE APP collection.png, contribute.png, collect-ticked.png read honestly; no findings.

## 2026-11-23

Web half: last 24 hours were a reader-judge batch (Varese, Esrum, McMinnville, Siliqua, Rungis, new Birkerod and Paris trees). The new city pages hold no em dashes. The four earlier WARNs still stand in site/dist (grep today), not repeated in full; replacements as in the 2026-11-21 entry:

- WARN site/dist/miami/baobabs-of-collins-park.html, key-west/strangler-figs-of-the-key-west-cemetery.html (and miami.gpx, key-west.gpx, api/trees.json) still carry "writer must not invent any" (seventh review; public copy never narrates process).
- WARN site/dist/explore.html "Each pin opens a tree with its age, its species, why it is worth the walk..." (seventeenth review).
- WARN site/dist/contribute.html "verified against independent sources" (twenty-eighth review; false since 2026-10-12).
- WARN site/dist/collections/ancient-oaks-of-europe.html "every coordinate verified" (eighth review; hard rule 2).

App half (iPhone SE, collect flow: away, compare, describe, identify, intro, place): looked at all six.

- WARN APP collect-identify.png / collect-compare.png (Amsterdam): the sheet says "You are standing among trees we map. Pick the one in your photograph." but its only candidate is the Wilhelminalinde, "325 m south". A tree 325 m away is not one you stand among; the copy promises a nearness the list does not show. Say it only when a candidate is within a plausible distance, else go straight to "Add a new tree".
- NOTE APP collect-describe.png: the new-tree page opens with a large blank white area where the photograph should sit (hero empty above "A tree in Amsterdam"); reads as a failed image load, not a placeholder.
- NOTE APP collect-place.png: the pin is drawn through the map's "Amsterdam" label, so the label is struck by the pin stem.
- NOTE APP collect-away.png and collect-intro.png are the same screen; no finding.

## 2026-11-22

Web half: the last 24 hours were reader-judge work (Delhi peepal live, five Zwolle and Emmen photographs, two face-photos taken down in Bath and Cordoba). The new Delhi and Zwolle pages hold no em dashes. Four earlier WARNs still stand in site/dist (checked by grep today); not repeated in full, replacements as in the 2026-11-21 entry:

- WARN site/dist/miami/baobabs-of-collins-park.html and site/dist/key-west/strangler-figs-of-the-key-west-cemetery.html still show "writer must not invent any" (sixth review; process narration).
- WARN site/dist/explore.html "Each pin opens a tree with its age, its species, why it is worth the walk..." (sixteenth review).
- WARN site/dist/contribute.html "verified against independent sources" (twenty-seventh review; false since 2026-10-12).
- WARN site/dist/collections/ancient-oaks-of-europe.html "every coordinate verified" (seventh review; hard rule 2).

App half (iPhone SE: species, tree-nophoto, tree, visitors; iOS 18.5: city, city-map-full): looked at all six.

- WARN APP city.png and city-map-full.png (Aachen, one tree): the Forster Linde appears twice in a row, once under "Highlights" and again under "The one tree", and the sheet header says "1 tree". A place of one tree repeats itself; Highlights should not render when it would list the whole list. Also "Become the Aachen ambassador" is offered for a place with one tree (CLAUDE.md Ambassadors: two trees in one place earn it).
- NOTE APP city.png: the floating "Map" pill sits on top of the "Help create Ancient Trees Plus" card, cutting its title in half; reads as a collision, not a scroll crop.
- NOTE APP species.png and visitors.png read honestly; no findings.

## 2026-11-21

Web half: the last 24 hours were reader-judge photographs (Castlemaine's two trees, Birnam Oak, Fortingall Yew, Vienna's Hauptallee), the Stuttgart Rotwildpark write pass, an Android picker crash fix and a Discover link fix. The new Castlemaine, Dunkeld, Fortingall and Stuttgart pages hold no em dashes or banned words, and reader photographs carry their licence line. Earlier findings stand, all still present in site/dist (checked by grep):

- WARN site/dist/miami/baobabs-of-collins-park.html and site/dist/key-west/strangler-figs-of-the-key-west-cemetery.html still show "writer must not invent any" as page text (fifth review). Public copy never narrates our process. Replacement for the access line: "Free. Open access; opening hours not confirmed." Add a preflight check for "writer must" in `access` and `story`.
- WARN site/dist/explore.html still says "Each pin opens a tree with its age, its species, why it is worth the walk, and directions from where you are". Fifteenth review; app-only pins open a card without a story. Replacement: "Each pin opens a tree; some stories are in the app."
- WARN site/dist/contribute.html still says "verified against independent sources before it goes live". Twenty-sixth review. False since "Good reader input IS the source" (2026-10-12). Replacement: "We read every submission before it is kept."
- WARN site/dist/collections/ancient-oaks-of-europe.html and europes-most-remarkable-yews.html still say "every coordinate verified" (sixth review). Hard rule 2, faked precision. Replacement: "every entry is publicly accessible and links onward with a map".

App half (iPhone SE: refused, review-ask, search, signin-email, signin, species-pick): looked at all six. The location, rating and sign-in sheets and search results read honestly.

- NOTE APP signin-email.png is pixel-identical to signin.png (three buttons, "Continue with email" not opened), so the sweep's email step does not show the email form; worth a session checking that the capture taps through.
- NOTE APP species-pick.png: the bare numbers (320, 149, 129...) beside each species have no label, and the checked Pedunculate Oak has none. A reader cannot tell they are tree counts; a session decides whether a unit ("320 trees") or no number is right.

## 2026-11-20

Web half: the last 24 hours were reader-judge photographs (Lyon, London), the bookmark on tree tiles (web and app, iOS and Android), the sign-in last-call script, row thumbnails and Birmingham verify leads. Nothing new broke in what was sampled; the earlier findings are all still present in site/dist (checked by grep):

App half (iPhone SE: people, photo-viewer, place-pin, profile-edit, profile-signed-in, profile): looked at all six. Find people, the photo viewer credit, the "Where is it really?" sheet and both Settings states read honestly.

- NOTE APP profile-edit.png: the Name field is empty ("The name people see") while profile-signed-in.png shows the same account as "test". Every account has a profile name from the moment it exists (CLAUDE.md, Profiles), so an empty field is either a fixture gap or a real state where the edit sheet loses the name; worth a look by a session.
- NOTE APP profile-signed-in.png: "Ancient Trees Plus" sits under the HELP heading beside Send feedback and Rate the app. A paid offer under Help reads as a mislabelled group; a session decides placement (visual, hard list 2 for anything about the price).

- WARN site/dist/miami/baobabs-of-collins-park.html and site/dist/key-west/strangler-figs-of-the-key-west-cemetery.html still show "writer must not invent any" as page text (fourth review; the phrase is still in 11 data/cities files and in site/dist/api/trees.json). Public copy never narrates our process. Replacement for the access line: "Free. Open access; opening hours not confirmed." Add a preflight check for "writer must" in `access` and `story`.
- WARN site/dist/explore.html still says "Each pin opens a tree with its age, its species, why it is worth the walk, and directions from where you are". Fourteenth review; app-only pins open a card without a story. Replacement: "Each pin opens a tree; some stories are in the app."
- WARN site/dist/contribute.html still says "verified against independent sources before it goes live". Twenty-fifth review. False since "Good reader input IS the source" (2026-10-12). Replacement: "We read every submission before it is kept."
- WARN site/dist/collections/ancient-oaks-of-europe.html still says "every coordinate verified" (fifth review). Hard rule 2, faked precision. Replacement: "every entry is publicly accessible and links onward with a map".

## 2026-11-19

Web half: the last 24 hours were reader-judge commits (Ghost Gum of Trephina Gorge, York and Lyon reader photographs, ambassador badges), same-picture dedupe and READER_FLOW.md. The new Trephina Gorge and York pages hold no em dashes, and the photo licences are recorded. Earlier findings stand, all still present in site/dist:

- WARN site/dist/miami/baobabs-of-collins-park.html and site/dist/key-west/strangler-figs-of-the-key-west-cemetery.html still show "writer must not invent any" as page text (third review). Public copy never narrates our process. `grep -rl "writer must" data/cities` now hits 11 files (berlin, miami, dresden, hilo, key-west, leipzig, bamberg, leeds, new-york, potsdam, dartmoor). Replacement for the access line: "Free. Open access; opening hours not confirmed." Add a preflight check for "writer must" in `access` and `story`.
- WARN site/dist/explore.html still says "Each pin opens a tree with its age, its species, why it is worth the walk, and directions from where you are". Thirteenth review; app-only pins open a card without a story. Replacement: "Each pin opens a tree; some stories are in the app."
- WARN site/dist/contribute.html still says "verified against independent sources before it goes live". Twenty-fourth review. False since "Good reader input IS the source" (2026-10-12). Replacement: "We read every submission before it is kept."
- WARN site/dist/collections/ancient-oaks-of-europe.html still says "every coordinate verified" (fourth review). Hard rule 2, faked precision. Replacement: "every entry is publicly accessible and links onward with a map".

App half (iPhone SE: feedback, map-bar, own-tree; map-full, map-pin and map were not opened): feedback sheet, Amsterdam map with "21 trees" bar and the own-tree screen all read honestly. NOTE APP own-tree.png shows a flat illustrated placeholder oak as the hero for "The oak on my street"; likely a fixture, a reader could take it for a photograph of their tree.

## 2026-11-18

Web half: the last 24 hours were reader-judge photographs (Melbourne, Sydney, Tokyo, Edinburgh Gardens), Fort Worth, Philadelphia, Baltimore and Leeds app-only trees, and Play tester setup. Nothing new broke in the sampled built pages; earlier findings stand.

- WARN site/dist/miami/baobabs-of-collins-park.html and site/dist/key-west/strangler-figs-of-the-key-west-cemetery.html still show "writer must not invent any" as page text in the access line (flagged 2026-11-17, unchanged). Public copy never narrates our process. `grep -rn "writer must" data/cities` now hits 15 places in 11 files (bamberg, berlin, dartmoor, dresden, hilo, key-west, leeds, leipzig, miami, new-york, potsdam), so it is still being written by passes. Replacement for the access line: "Free. Open access; opening hours not confirmed." Add a preflight check for "writer must" in `access` and `story`, and a line in BRIEF_RESEARCH.md that the note never goes in a shown field.
- WARN site/dist/explore.html still says "Each pin opens a tree with its age, its species, why it is worth the walk, and directions from where you are". Twelfth review; app-only pins open a card without a story. Replacement: "Each pin opens a tree; some stories are in the app."
- WARN site/dist/contribute.html still says "verified against independent sources before it goes live". Twenty-third review. False since "Good reader input IS the source" (2026-10-12). Replacement: "We read every submission before it is kept."
- WARN site/dist/collections/ancient-oaks-of-europe.html and europes-most-remarkable-yews.html still say "every coordinate verified" (third review). Hard rule 2, faked precision. Replacement: "every entry is publicly accessible and links onward with a map".

App half (iPhone SE: map-pin, map, own-tree, people, photo-viewer, place-pin): looked at all six.

- NOTE APP map-pin.png: the card title is cut mid-parenthesis, "Dąb Fabrykant (the Factory Owner's Oak, als...", because the stored tree name carries a bracketed alias list. A reader sees a half sentence; the name field should hold the main name and the aliases belong elsewhere. Session work (visual), a data tidy of long `name` values may follow.
- NOTE APP map-pin.png: the sheet shows a Polish oak (Łódź) over a map of Amsterdam. Probably the sweep's fixture, not a real state; mentioned only so nobody reads it as a pin-to-card mismatch.
- Nothing else a person would notice: Find people, the photo viewer credit and the "Where is it really?" sheet read honestly.

## 2026-11-17 compliance

- hans-photos-app-only-yes: Hans Hofele's Frankfurt photographs have a phone yes for the app only, yet show on the website too (copyright, scope of permission). Privacy page checked against the week's new tables (votes, reports), crash reports and mail route: still true.

## 2026-11-17

Web half: the last 24 hours were the Miami, Allentown, Aspromonte, Castelbuono, Serra San Bruno and Tremiti write passes (app-only, no web pages), reader photographs into Hobart and Takayama, seven new reader trees, Thailand and Philippines country intros. No em dashes and no banned words in the changed city and country files.

- WARN site/dist/miami/baobabs-of-collins-park.html and site/dist/key-west/strangler-figs-of-the-key-west-cemetery.html show a brief note to the writer as page text in the access line: "hours not fetched, writer must not invent any" (source data/cities/miami.json:260, data/cities/key-west.json:87). It leaks process as text ("public copy never narrates our process"). Replacement: "Free. Open access; opening hours not confirmed." A data fix a run may do; `grep -rn "writer must" data/cities` also hits miami `transport` x3, key-west `transport` and bamberg `notes` (transport is not shown, clean it with the rest). Worth a preflight check for "writer must" in `access` and `story`.
- WARN site/dist/explore.html still says "Each pin opens a tree with its age, its species, why it is worth the walk, and directions from where you are". Eleventh review; app-only pins open a card without a story. Replacement: "Each pin opens a tree; some stories are in the app."
- WARN site/dist/contribute.html still says "verified against independent sources before it goes live". Twenty-second review. False since "Good reader input IS the source" (2026-10-12). Replacement: "We read every submission before it is kept."
- WARN data/collections/ancient-oaks-of-europe.json and data/collections/europes-most-remarkable-yews.json still say "every coordinate verified" (flagged 2026-11-16, unchanged). Many pins are approximate; hard rule 2 "faked precision". Replacement: "every entry is publicly accessible and links onward with a map".

App half (iPhone SE: early-adopter-sheet, early-adopter, explore, feedback, map-bar, map-full): looked at all six.

- NOTE APP feedback.png: the "Feedback" screen opens a sign-in sheet titled "Sign in to have your say" over a line that says "You need an account to send a tree". Reads consistently; no action. Nothing else a person would notice: the badge sheet, Discover counts ("532 trees at their best this month") and the Amsterdam list read honestly.

## 2026-11-16

Web half: the last 24 hours were the Hanoi banyan (hni_003, a reader's tip, visible from the pavement, sources named), Leipzig and Philadelphia app-only trees, reader photographs into strips, sign-in "Did you mean" copy and the tree_votes table. No em dashes in the Hanoi built page.

- WARN site/dist/explore.html still says "Each pin opens a tree with its age, its species, why it is worth the walk, and directions from where you are" while app-only pins open a card with no story. Tenth review. Hard rule 2 and "a decision that changes what the product does also changes what the product says". Replacement: "Each pin opens a tree; some stories are in the app." Translations too.
- WARN site/dist/contribute.html (source site/src/pages/contribute.astro) still says "verified against independent sources before it goes live". False since "Good reader input IS the source" (2026-10-12). Twenty-first review. Replacement: "We read every submission before it is kept."

App half (iPhone SE: collect-voted, collection-tab, collection, contribute, directions): looked at all six.

- WARN APP collection.png, the "Europe's Ancient Oaks" collection intro: "every coordinate verified". Not true of the data (1,715 pins are approximate, `location_precision` says so); hard rule 2 "faked precision" and Never cuttable list. The intro is machine-written text in data/collections/ and reaches web and app; replacement: "every entry is publicly accessible and every page links onward with a map", and grep other collection intros for "verified". Data fix, so a run may do it.
- Nothing else a person would notice: vote sheet, sign-in sheet and directions sheet read honestly.

## 2026-11-15

Web half: the last 24 hours were Buffalo and Bamberg trees (app-only, no pages built, correct under APP FIRST), Potsdam and Fort Worth walls and data digests. No em dashes in the sampled built pages.

- WARN site/dist/explore.html still says "Each pin opens a tree with its age, its species, why it is worth the walk, and directions from where you are" while app-only pins open a card with no story. Ninth review. Hard rule 2 and "a decision that changes what the product does also changes what the product says". Replacement: "Each pin opens a tree; some stories are in the app." Translations too.
- WARN site/dist/contribute.html (source site/src/pages/contribute.astro) still says "verified against independent sources before it goes live". False since "Good reader input IS the source" (2026-10-12). Twentieth review. Replacement: "We read every submission before it is kept."

App half (iPhone SE, collect flow: intro, place, identify, compare, describe, ticked): looked at all six. APP NOTE: collect-describe has a large empty block above the title "A tree in Amsterdam" where the photograph would sit, with only back and overflow buttons in it; a person with a photo would see it, but verify the sweep's fixture does not hide a real no-photo state. Otherwise nothing a person would notice is wrong; copy reads honestly.

## 2026-11-14

Web half: the last 24 hours were Leipzig lpz_031, Fort Lauderdale ftl_005 to ftl_010 (app-only), a Fort Lauderdale FAQ fix and data digests. No em dashes in the sampled pages or the two changed city files. lpz_031 names its sources and register, and its access line says to stay out of the allotment gardens.

- WARN site/dist/explore.html still says "Each pin opens a tree with its age, its species, why it is worth the walk, and directions from where you are" while app-only pins open a card with no story. Eighth review. Hard rule 2 and "a decision that changes what the product does also changes what the product says". Replacement: "Each pin opens a tree; some stories are in the app." Translations too.
- WARN site/dist/contribute.html (source site/src/pages/contribute.astro) still says "verified against independent sources before it goes live" three times plus "independent sources before". False since "Good reader input IS the source" (2026-10-12). Nineteenth review. Replacement: "We read every submission before it is kept."
- NOTE data/cities/windsor.json wsr_002 still narrates our process (iNaturalist sentence, flagged 11-13). Drop it.

App half (iPhone SE: species, tree-nophoto, tree, city-map-full, city, collect-away): looked at tree-nophoto and collect-away; nothing a person would notice is wrong. The no-photo card reads honestly ("Yours would be the first on this page"). Did not open the other four.

## 2026-11-13

Web half: the last 24 hours were a Rotterdam source link, Braga trees (app-only), Android parity harness, data digests. No em dashes in site/dist. The Rotterdam link change is sound.

- WARN site/dist/explore.html still says "Each pin opens a tree with its age, its species, why it is worth the walk, and directions from where you are" while app-only pins open a card with no story. Seventh review. Hard rule 2 and "a decision that changes what the product does also changes what the product says". Replacement: "Each pin opens a tree; some stories are in the app." Translations too.
- WARN site/dist/contribute.html (source site/src/pages/contribute.astro) still says "verified against independent sources" / "check every tip against independent sources", four times in the built page. False since "Good reader input IS the source" (2026-10-12). Eighteenth review. Replacement: "We read every submission before it is kept."
- NOTE data/cities/windsor.json wsr_002 still carries the sentence "An iNaturalist record from August 2026 falls within range of the spot, though nobody has checked...". Narrates our process ("Public copy never narrates our process"). Drop it.

App half (iPhone SE: refused, review-ask, search, signin-email, signin, species-pick):

- NOTE APP search.png: typing "lis" lists Lisbon, then Indianapolis, Minneapolis and Alishan, matched mid-word. A reader typing a place expects names that start with it first; Alishan (2 trees) outranks nothing useful. For a session.
- NOTE APP signin-email.png is byte-identical in look to signin.png (it shows the three-button choice, not an email form), so the screen named for email entry is not being exercised by the sweep. For a session.
- Nothing wrong found on refused.png, review-ask.png or species-pick.png.

## 2026-11-12

Web half: the last 24 hours were Cardiff and Windsor trees into the app, an add-photo fix, Android release prep. No em dashes in site/dist. Standing findings unchanged.

- WARN site/dist/explore.html still says "Each pin opens a tree with its age, its species, why it is worth the walk, and directions from where you are" while app-only pins open a card with no story. Sixth review. Hard rule 2 and "a decision that changes what the product does also changes what the product says". Replacement: "Each pin opens a tree; some stories are in the app." Translations too.
- WARN site/dist/contribute.html (source site/src/pages/contribute.astro) still says "verified against independent sources" / "check every tip against independent sources", twice. False since "Good reader input IS the source" (2026-10-12). Seventeenth review. Replacement: "We read every submission before it is kept."
- NOTE data/cities/windsor.json wsr_002 story: "An iNaturalist record from August 2026 falls within range of the spot, though nobody has checked that it shows this particular oak." Narrates our process and states a non-fact; "Public copy never narrates our process". Drop the sentence.
- NOTE the 11-07 question stands: data/walk-routes.json routing through app-only trees that have no page is unchecked.

App half (iPhone SE: people, photo-viewer, place-pin, profile-edit, profile-signed-in, profile):

- NOTE APP profile-edit.png: Country is pre-filled "United States" with the Name still empty, so a new account shows a country nobody chose, and it is public with the profile. Show it empty until picked, or fill it from the device region and say so. For a session.
- NOTE APP profile.png and profile-signed-in.png: "Ancient Trees Plus" sits under the HELP heading beside Send feedback and Rate the app. The section title disagrees with what the row is (an offer). For a session; the paywall line is Hidde's (hard list 2).
- NOTE APP place-pin.png: two marks stand on the map, the drop pin and the tree disc beneath it, so "until the pin sits on the tree" is ambiguous about which one moves. For a session.
- Nothing wrong found on people.png and photo-viewer.png (credit and licence shown).

## 2026-11-18 code

- WEB-BUG-refresh-blip-signs-out, site/src/lib/signin-js.ts:254: a 429 or 5xx from the token refresh clears the stored session and signs the visitor out; only 400/401/403 mean the refresh token is spent.

## 2026-11-11 code (full)

- APP-BUG-shared-photo-url-force-unwrap, ios/AncientTrees/AncientTrees/Screens/SharedTreeView.swift:108: shared tree photo URL from a server file name is force-unwrapped.

## 2026-11-11

Web half: the last 24 hours were Android parity work, one maps fix (atCanMap() asks for maplibregl, qa holds it) and data. No em dashes in site/dist HTML. Standing findings are unchanged.

- WARN site/dist/explore.html still says "Each pin opens a tree with its age, its species, why it is worth the walk, and directions from where you are" while app-only pins open a card with no story. Fifth review. Hard rule 2 and "a decision that changes what the product does also changes what the product says". Replacement: "Each pin opens a tree; some stories are in the app." Translations too.
- WARN site/src/pages/contribute.astro:17 and :401 (built into contribute.html) still say "verified against independent sources" / "check every tip against independent sources". False since "Good reader input IS the source" (2026-10-12). Sixteenth review in a row. Replacement: "We read every submission before it is kept."
- NOTE the 11-07 question stands: data/walk-routes.json routing through app-only trees that have no page is unchecked.

App half (iPhone SE: feedback, map-bar, map-full, map-pin, map, own-tree; map-full and map read like map-bar):

- NOTE APP feedback.png: "We check every vote, correction and tip" again (third review). Live-first (2026-10-24) means photos and notes are public before a check. "We read every vote, correction and tip" holds for all. For a session.
- NOTE APP map-pin.png: standing since 11-09. The map is on Amsterdam while the open card is "Dąb Fabrykant (the Factory Owner's Oak, als…", a Polish tree not in view. New this time: the card title is cut mid-word at two lines ("als…"), so the name a person reads is a fragment; a short display name or a third line would hold it. Also the locate button sits over a pin at the right edge and the pin shows through it.
- NOTE APP own-tree.png: "Amsterdam" under the title is underlined like a link while nothing around it is; the hero is a flat illustrated placeholder for a tree with no photo. Probably the designed empty state; flagging only the underline.

