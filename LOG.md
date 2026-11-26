# LOG

## 2026-11-26 reader judge: a tall araucaria at Palheiro Gardens, Madeira, live

- Live: madeira/mdr_013, The Tall Araucaria of Palheiro Gardens, from a reader's website tip with a photograph (viewed: a Norfolk Island pine standing alone on a lawn, tier on tier, daylight). It came with no GPS, so the pin is approximate on the garden's point (the same as the pohutukawa, mdr_010). Paid entry. The page gives the reader's 48 m, their survey citation (Árvores Monumentais e Emblemáticas da Madeira, 2008) and their account of the garden as their own words. Photo filed in November, the photo's own month. Madeira now has 13 trees; its intro, meta and question texts (EN and the kept PT overlay) give the new count, and the PT overlay has the tree.
- Nothing else waited: 0 open reports, 0 open feedback, 0 reader notes to quote. Lead 3c544597 (Amsterdam) is still our own account's and its photo is still not on disk, so it was left alone.

## 2026-11-26 reader judge: a campus cedar in Varese live

- Live: varese/var_003, The Cedar of the University Campus, from a reader's app photograph (four frames viewed; photo GPS at the tree, dated November). A broad blue-grey cedar alone on a campus lawn. Species left at Cedrus sp.: the reader says Lebanon, the crown reads Atlas, and the page asks. Varese now has three trees; its intro, meta, question texts and FAQ say so. No kept translation of Varese.
- Reader words: the Cat Tien tung note closed as pasted text (summary prose with an em dash, not the reader's own account).
- Nothing else waited: 0 open reports, 0 open feedback. Lead 3c544597 (Amsterdam, 2026-11-18) is our own account's and its photo is not on disk, so it was left alone.

## 2026-11-26 session: US round 3 sent, round 4 (empty cities) ready

- Round 3 sent through Resend on Hidde's "Verstuur ze": 8 (Charleston City Paper, South Carolina Wildlife, Big Island Now, Delaware County Daily Times, Audubon, Friends of the Parks, Chicagology, Bronx.com). 58 US local mails out since 11-25; one answer so far (The East Hampton Star).
- Round 4 on hold, drafts/batches/press-us-empty-cities-round4.json (private): 14 desks in big US cities with no or hardly any trees (Phoenix, Denver, Detroit, Charlotte, Memphis, Louisville, Sacramento, Nashville, Milwaukee, Indianapolis, Cincinnati, Raleigh, Tampa, Albuquerque). The P.S. asks which tree their readers would put on the map first ("still empty" only where none of ours stands within 30 km). No desk address found for Columbus, Jacksonville, Omaha, Orlando or Tucson. mailcheck clean.

<!-- archive-index -->

**Older entries live in the archive**, moved by `scripts/archive_logs.py`, nothing deleted:

- [2026-11](archive/LOG-2026-11.md)
- [2026-10](archive/LOG-2026-10.md)
- [2026-09](archive/LOG-2026-09.md)
- [2026-08](archive/LOG-2026-08.md)
- [2026-07](archive/LOG-2026-07.md)

So absence from this file is not evidence something was never tried: `grep -ri "<place>" archive/` before concluding a hunt is new. Re-running an exhausted hunt is this project's most repeated waste.
<!-- archive-index -->
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

## 2026-11-25 session: the repo moved to the Ancient-Trees-Org organisation

- **Moved**: ancienttrees and ancienttrees-open now live under github.com/Ancient-Trees-Org (Hidde created the org; `scripts/move_to_org.py` rewrote the 7 files). The 25 secrets, Pages (ancienttrees.app, open.ancienttrees.app, both answer 200) and the github-pages environment came along. The Mac's remote points to the org. A deploy (run 45617756403) and a reader-judge run (45617763984) were dispatched on the moved repo as the test.
- **Still Hidde's**: a new fine-grained token for the Supabase trigger with the org as resource owner (the old one only reaches the personal account's repos; until then the 15-minute poll picks readers up), then paste supabase/reader-judge-trigger.sql again; the second person is invited as org Owner by mail (2026-11-25, accepted not yet seen). www needs nothing: it still answers 301 to ancienttrees.app after the move. Steps in .github/ORG_MOVE.md.

## 2026-11-24 session: a second owner everywhere; GitHub move to an organisation prepared

- **Asked by Hidde: what if Google blocks the Workspace account too.** Sending keeps working (Resend). Incoming mail is restored by moving the MX records at TransIP to another mail host. Search Console comes back through DNS; GA would start empty again; Play is the real risk. The cheapest guard is putting billing on the Workspace trial. The account's recovery address is one that will stop working; move it to an address he keeps.
- **Second owner, done (Hidde, 2026-11-25)**: a second person is now owner or admin on Google Cloud (project Ancient Trees, after the Domain Restricted Sharing policy was overridden for that project only), Search Console, GA, Play, Supabase and Resend. GitHub is the one left; it waits for the organisation.
- **Prepared, not done**: moving the repo into a GitHub organisation, since a personal repo cannot have a second admin. The steps are in .github/ORG_MOVE.md, and `scripts/move_to_org.py <org> [--write]` rewrites the 7 files that name the owner. Waiting for Hidde to create the org (`ancient-trees-app` suggested) and say "verhuis". After the move, the Supabase dispatch token must be remade with the org as resource owner, and www's CNAME (still on the old account's github.io) should point to the org.

## 2026-11-24 session: weak points after the Google block; incoming-mail alarm live

- **Live, one door to Google** (Hidde: "kunnen we ook iets inbouwen dat we niet ergens anders enthousiast dingen met google doen die ons weer gebanned kan krijgen?"): scripts/google_gate.py is now the only way any script logs in to the Google mailbox. It keeps one connection for the run, allows at most two logins, and never retries after Google refuses one. Seven scripts moved to it: mailer, reader_mail_replies, sent_drafts, signin_watch, outreach_yield, outreach_inbox and outreach_threads, whose reconnect loop could log in three times per address. data/google-touch.json lists every script that touches Google, where it runs and how often: about 37 mailbox logins a day against a budget of 40, where there were ~500 on 2026-11-20. qa `check_google_is_touched_through_one_door()` refuses a push with a login outside the gate, a Google-touching script missing from the list, or a total over budget. The rule is in CLAUDE.md "How runs fire". Tests: test_google_gate.py (5) and test_mailer_copy.py. Tried live: reader_mail_replies and sent_drafts through the gate.

- **Live**: an alarm when mail stops reaching us (Hidde: "dit lijkt me slim"). The reader judge's existing mailbox login now records in data/inbox-health.json whether the login worked and the day the newest mail arrived (scripts/inbox_health.py, 9 tests). health.py goes red when the login fails, when nothing has arrived for 2 days, or when the check has not run for 2 days. It adds no extra login. Tried against the real mailbox: newest mail today, ok.
- **Found**: the database backup has failed all 20 runs since 2026-11-05. Hidde set the secrets today, but the run at 18:30 failed with `password authentication failed for user "postgres"`. The pooler needs the user `postgres.caimvxiyrtifilimlkqw` and the database password.
- **Live, fewer mailbox logins** (Hidde: "Eens mss zelfs minder?"): the reader judge read the Workspace mailbox on every run, about 125 logins a day from changing US GitHub servers, the same pattern as the Gmail before its block. It now reads once per three-hour slot (an empty cache entry per slot keeps it exact; a manual dispatch still reads), so 8 a day. And mailer.keep_copy logged in once for every mail it filed in Sent (367 logins on 2026-11-20); it now keeps one connection per run and never retries a refused login (scripts/test_mailer_copy.py). Left as they were: sent_drafts and outreach_yield once a day in the digest, signin_watch's bounce check only when it has a mail to resend.
- **Found, his**: the Workspace trial needs billing, the recovery address is one that will stop working, there is one super admin, Time Machine has no disk, and the Claude login method is unknown. The new GitHub account is one day old and running ~600 runs a day; www still CNAMEs to the old account's github.io, and the domain is not verified for Pages on the new account.

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
- **Laptop backup live** (Hidde: "maar hebben we dan niet nog steeds een probleem als ik deze laptop kwijt raak?"): `scripts/laptop_backup.py`, nightly at 03:15 from ~/Library/LaunchAgents/app.ancienttrees.laptop-backup.plist (log ~/Library/Logs/ancienttrees-laptop-backup.log). One AES-256 archive (openssl, pbkdf2) of the ~/.ancienttrees-* key files (Android upload key included), changed, untracked and gitignored private files under data/ and drafts/, and Claude's project memory: 756 files, 81 MB, into "Ancient Trees backup" in Drive under hidde@ancienttrees.app; the last 14 kept. Passphrase in the Mac keychain (service `ancienttrees-backup`), typed by Hidde, never seen by a session. Tested: a run from the shell and one from launchd wrote archives, `--verify` opened them. Drive refuses to overwrite or delete a file it is still uploading, so each archive has its own timestamped name and a busy file is left for the next night.
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

