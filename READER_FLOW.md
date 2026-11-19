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
| New tree | Your tree is on Ancient Trees | Tree goes live; asks for what is missing (age, trunk, story); P.S. ambassador when the place has none | automatic | scripts/tree_approved.py |
| New tree | Your trees are on Ancient Trees | Several of their trees go live close together: one bundled mail with every link (since 2026-11-15) | automatic | scripts/tree_approved.py |
| New tree | About what you sent us: ... (hold mail) | Held for a fixable reason: says what would put it live; a bad photo asks about the tree (2026-11-18) | reader judge | scripts/hold_reply.py, sent by contributor_reply.py |
| New tree | About what you sent us: ... (question) | A tip without a photo, when one fact would settle it | reader judge | contributor_reply.py |
| Photo on our tree | Your photo is on the page of ... | Their first photo goes live: at once | automatic | scripts/sightings_publish.py |
| Photo on our tree | Your photos are on the trees' pages | Later photos: bundled, at most once a week | automatic | scripts/sightings_publish.py |
| Report | About what you sent us: ... (thank-you) | A report with no words of their own (dead tree, pin moved) | reader judge | tree_reports.py --thank |
| Feedback | A reply in Hidde's words | Feedback form, or a report with their own words: only on his yes | Hidde | a session, contributor_reply.py |
| Ambassador | Your {place} trees (invitation) | Photos of two trees in one place; once per person and place; badge with it | automatic | scripts/ambassador.py |
| Ambassador | Looking after {place} | They ask to become ambassador: questions and badge within about 15 minutes | automatic | scripts/ambassador.py --requests |
| Ambassador | New on the {place} list | Ambassadors only: new trees in their place | automatic | scripts/ambassador.py --heads-up |
| Their reply | (comes back in) | Any reply to the mails above becomes a feedback row within about 15 minutes; the judge acts or it reaches Hidde | reader judge | scripts/reader_mail_replies.py |

Across every mail: at most one per address in seven days, except a reply in their own thread (mailer.py); no App Store link (mailcheck.py). The templated "we received your tip" thank-you is off (`THANK_YOU = False`, Hidde 2026-10-02), so a reader hears nothing between sending and live, held or a question.
