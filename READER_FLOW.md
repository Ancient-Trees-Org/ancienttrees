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
