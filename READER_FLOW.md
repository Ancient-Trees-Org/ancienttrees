# What happens after a reader adds a tree

Hidde, 2026-11-18: "remember this visual for further reference". The map of every outcome after a reader adds a tree, what we do, and what the reader hears back, with the gaps marked. Update the row (and its status) in the same change that closes a gap. Rules behind each row: CLAUDE.md "Verify" and "Reader input", BRIEF_READER_JUDGE.md.

A reader adds a tree (app camera, website form, or a tip in words) -> the reader judge on GitHub, within about 15 minutes.

| What it is | What we do | What the reader hears | Status |
|---|---|---|---|
| Photo of a tree we map | In the tree's photo strip at once; lead photo after a look | "Your photo is on the page" (sightings_publish.py; first at once, later ones bundled, at most weekly) | covered |
| New tree, live (GPS or photo, somewhat special) | On the map and its own page | "Your tree is on Ancient Trees" (tree_approved.py): asks what is missing (age, trunk, story), P.S. ambassador | covered |
| Held, the reader can fix it (`bad_frame`, `no_location`, `doubt_location`, `not_public`, `wrong_tree`, `not_theirs`) | Stays on their own profile only | Standard hold mail saying what would put it live (hold_reply.py, since 2026-11-18) | covered |
| Held, the reader cannot fix it (`not_special`, `dead`, `wrong_subject`, `inappropriate`, `doubt_info`, `doubt_photo`) | Stays on their own profile only | Nothing; they never learn why it is not on the map | **gap** |
| Tip without a photo, sources confirm it | Live as a reader-found tree | Website tips: "approved" on their account page; whether a mail always goes is unchecked | partly |
| Tip without a photo, cannot confirm | Kept as a lead | A reply only when one fact would settle it; otherwise nothing | **gap** |
| Duplicate of something already sent or live | Folded into the existing tree | Usually nothing, unless it adds a photo | partly |
| The reader replies by mail to any mail above | Filed as a feedback row within about 15 minutes (reader_mail_replies.py, in the reader judge); the judge re-opens a held tree with the new fact, or puts an age or story on the page; anything else reaches Hidde in the digest | No mail from the run; Hidde answers general feedback himself | covered (2026-11-18) |

Across every row: the one-week rest per address (mailer.py) can hold a mail back by days.

## Every mail a reader can get

Hidde, 2026-11-19: "geef me ook een visualisatie van alle het mailverkeer waar een gebruiker mee kan dealen". Read from the sending scripts that day. A new reader mail, or a change to when one goes, updates this table in the same change.

| Moment | Subject | When | Who sends | Script |
|---|---|---|---|---|
| Account | Welcome to Ancient Trees | After creating an account | automatic | supabase/functions/send-email |
| Account | Sign-in link or code, password reset, confirm new address | Only when they ask for it | automatic | supabase/functions/send-email |
| Account | The same sign-in mail again, when an email sign-up never got in | An hour later; signed-only addresses once more after midnight UTC; never a third time | automatic | scripts/signin_watch.py (knock) |
| New tree | Your tree is on Ancient Trees | Tree goes live; asks for what is missing (age, trunk, story); P.S. ambassador when the place has none | automatic | scripts/tree_approved.py |
| New tree | Your trees are on Ancient Trees | Several of their trees go live close together: one bundled mail with every link (since 2026-11-15) | automatic | scripts/tree_approved.py |
| New tree | About what you sent us: ... (hold mail) | Held for a fixable reason: says what would put it live; a bad photo asks about the tree (2026-11-18); a screenshot asks "did you take it yourself?", also when the tree went live without it (doubt_photo, doubt_photo_live, 2026-11-26); a good photo that seems to show another spot asks "same tree or another one, and where did you take it?" (photo_elsewhere, 2026-11-27) | reader judge | scripts/hold_reply.py, sent by contributor_reply.py |
| New tree | About what you sent us: ... (question) | A tip without a photo, when one fact would settle it | reader judge | contributor_reply.py |
| Photo on our tree | Your photo is on the page of ... | Their first photo goes live: at once | automatic | scripts/sightings_publish.py |
| Photo on our tree | Your photos are on the trees' pages | Later photos: bundled, at most once a week | automatic | scripts/sightings_publish.py |
| Report | About what you sent us: ... (thank-you) | A report with no words of their own (dead tree, pin moved) | reader judge | tree_reports.py --thank |
| Feedback | A reply in Hidde's words | Feedback form, or a report with their own words: only on his yes | Hidde | a session, contributor_reply.py |
| Feedback | Fixed, thanks to you (Opgelost, dankzij jou) | A bug they reported is fixed: an app fix the day it is on main ("comes with the next app update"), a website fix once it is live; our words only (since 2026-11-25, the order since 2026-11-26) | automatic | scripts/bug_fixed_mail.py (tell-readers.yml, knock) |
| Feedback | The fix is in the app now (De oplossing staat nu in de app) | The app update carrying that fix is in their store: App Store build, or an Android build in data/android-releases.json | automatic | scripts/bug_fixed_mail.py |
| Ambassador | Your {place} trees (invitation) | Photos of two trees in one place; once per person and place; badge with it | automatic | scripts/ambassador.py |
| Ambassador | Looking after {place} | They ask to become ambassador: questions and badge within about 15 minutes | automatic | scripts/ambassador.py --requests |
| Ambassador | New on the {place} list | Ambassadors only: new trees in their place | automatic | scripts/ambassador.py --heads-up |
| Their reply | (comes back in) | Any reply to the mails above becomes a feedback row within about 15 minutes; the judge acts or it reaches Hidde | reader judge | scripts/reader_mail_replies.py |

Across every mail: at most one per address in seven days, except a reply in their own thread (mailer.py); no App Store link (mailcheck.py). The templated "we received your tip" thank-you is off (`THANK_YOU = False`, Hidde 2026-10-02), so a reader hears nothing between sending and live, held or a question.

## Every way readers send something, and who handles it

First drawn 2026-11-17; kept on Hidde's word 2026-11-19 ("Zou je die er ook bij kunnen bewaren?"). Who: the reader judge (within about 15 minutes), live directly (public at once), the night run (the knock every two hours), the digest (shown to Hidde daily), a session (only when he asks). "Open for you" is the one digest block that needs him.

| What a person sends | From | Handled by | What happens | Comes to Hidde when |
|---|---|---|---|---|
| A new tree | app, website | reader judge | Live, or held with a reason from the closed list; the matching mail (see the mail table above) | A real doubt (can it be seen from the street?) |
| Words typed with a tree | app, website | reader judge | Their note under the tree, with their profile name | Never |
| Photo of a tree we have | app, website | live directly, then the reader judge | In the photo strip at once; the judge picks the lead photo and moves an approximate pin to its GPS | Never |
| A note on a tree | app, website | live directly, then the night run | Public at once; only abuse or another person's name is hidden | Never |
| Report: dead, wrong pin, which tree, duplicate | app, website | reader judge | Checked and fixed; a report without their own words gets the standard thank-you | Their own words need a reply, or the judge cannot close it |
| Worth-it vote | app, website | live directly | Counted on the tree | Never |
| Ambassador request | app, website | reader judge, digest | Mail with the questions and the badge, automatically; the digest names who was added | Never (a daily line, no action) |
| Feedback and ideas | app, website | reader judge, digest | Handled and recorded when it needs no mail (bug fixed, tip made a lead, idea already on the backlog) | A reply is needed (draft ready), or the decision is his |
| Plus question | app, website | digest; typed answers also the reader judge (since 2026-11-27) | Counts plus their words under the Plus table; a typed answer is judged like feedback: a bug becomes a bug row, a wish goes to PRODUCT_TODO.md "Ideas from readers". Anonymous, so never a reply | Daily, to read |
| App Store review | App Store | digest | Shown, not answered | Daily, to read |
| Android waitlist | website | digest | Counted; asked for the closed test later | Never |
| A reply to one of our reader mails | mail | reader judge (since 2026-11-18) | Filed as a feedback row; a held tree re-opened or an age or story put on the page | Anything that is not one of those |
| Other mail to Ancient Trees | his inbox | session | Read and answered only when he asks | Always his |
| Reddit, public tips | threads | session | His; a session helps when he asks | Always his |

## Feedback: what is handled for Hidde, what comes to him

Drawn 2026-11-17 with the rule "de makkelijke gevallen moet jij gewoon behandelen ... wat ik moet zien, zijn de dingen die openstaan". Every message gets a verdict in data/feedback-ledger.json (`scripts/feedback.py --close`); his answer is recorded and the row goes back to handled.

| Handled for him (recorded, not shown) | Comes to him in "Open for you" |
|---|---|
| One-tap votes ("worth it", "not worth it", vote undone): counted, nothing else | A reply in words to someone's own message: a draft is ready, nothing goes without his yes (example: #849) |
| New trees, photos, words typed with them: live or held with a closed-list reason, the "your tree is live" mail | A decision that is his: an idea outside find, walk, collect, season (example: #786) |
| Reports without their own words (dead tree, moved pin, grid reference, duplicate): fixed plus the standard thank-you | Real doubt: can it be seen from the street, conflicting facts, a pin that may be wrong; marked `doubt` with the reason |
| Feedback with an obvious answer and no mail needed: a bug fixed or logged, a tip made a lead or a tree, a tip we already have, an idea already on the backlog | Reports the judge could not close: left open with what is missing |
| Ambassador requests: mail with the questions plus the badge; the digest names who was added | Mail to Ancient Trees and Reddit: outside the app, read in a session when he asks |
| Notes on a tree: public at once; only abuse or another person's name is hidden | |
