# Reader judge: the brief

The instant run (`.github/workflows/reader-judge.yml`) reads this. It starts minutes after a reader sends a tree or a photograph, so their tree is live while they still remember sending it. Hidde, 2026-11-17: "should be instant honestly". The rules are CLAUDE.md's ("Verify", "Reader input"); this file is only the order of work.

## What you judge

Everything a reader sent that has no verdict yet (and their reports on our trees, see "Reports on our trees" below):

1. `python3 scripts/sightings_inbox.py --status`: photographs of trees we already map (data/sighting-queue.json, files in out/sightings/).
2. Leads in data/leads/_sightings.json with `status: "lead"` and no `hold`: trees we do not map. Their photographs are already on this machine at out/sightings/<sighting id>.jpg (`scripts/fetch_waiting_photos.py` ran before you).

A lead with `status: "lead"` and no `hold` is WAITING, whatever its `why` says. A `why` written before 2026-11-17 ("needs the site named", "no girth", "for a later pass", "a lead") is not a verdict under the closed list; judge it again from the photograph. Do not leave such leads "for the next run": they are the work.

Look at every photograph with Read before you decide. Never judge one blind; if a file is missing, leave that tree for the next run and say so in LOG.md.

## The decision (CLAUDE.md "Verify", the closed list)

A reader's tree goes live when it has a GPS fix or a photograph and is somewhat special. It is held only for a reason from the closed list, written in the lead's `hold` field: `bad_frame`, `wrong_tree`, `wrong_subject`, `not_special`, `dead`, `not_public`, `no_location`, `not_theirs`, and on a real doubt `doubt_location`, `doubt_photo`, `doubt_info`, `inappropriate`. No girth, age, source, site name or "a later pass" is ever a reason. `dead` holds only a stump, a fallen trunk, or a dead tree with no photograph: a reader's photograph of a standing dead tree that is still striking goes live like any other, the story saying plainly it is dead (Hidde, 2026-11-17, the Ochi chestnut); without a photo the reply asks for one. `not_public` only when the tree cannot be seen from public ground: on private land but visible from a street or path, it goes live with the pin on the viewing spot and an honest `access` line ("seen from the street; the garden is private"); when you cannot tell, hold and the reply asks whether it can be seen from the street. A photograph that shows one of OUR trees (check `nearest_published_m` and the species) belongs on that tree, not on a new page; if two of ours could be it, hold as `wrong_tree` and the reply asks which.

**One route** (Hidde, 2026-11-17): every reader's photograph ends with a verdict as a tree of its own unless it shows one of ours. In the queue (a photo sent for a tree we map) that means: a photograph of ANOTHER tree is the verdict `other_tree`, never `reject` or `hold`; sightings_publish.py turns it into a waiting lead with `sent_for`, and you (or the next run) judge it as a new tree under the closed list. `reject` is only for no tree in frame, a duplicate, or a bad frame. A lead with `unsure_among` was sent with "not sure which tree": it carries no name of ours on purpose; if the photograph shows one of the trees listed, it goes on that tree, otherwise judge it as new. A lead's coordinate from a photo sent for one of ours may be our pin rather than where it was taken (its `why` says so): with no other evidence, hold as `doubt_location` and the reply asks where it stands.

## Putting it live

- **A photo of a tree we map**: verdicts JSON, then `python3 scripts/sightings_publish.py verdicts.json --send` (its docstring has the fields). Never by hand.
- **A new tree**: copy the pattern of `scripts/build_reader_trees_2026_11_17.py` (one script per run, under out/tmp/, never committed): `write_image()` for the photo, `found_by_reader.sighting_id`, `pin_source` from the GPS fix, the reader's own words quoted, their figures stated as theirs, a story of 150 to 250 words, a recognition line, an honest `access` line. Readers' girths stay in the story, never in `girth_cm`. A tree without GPS needs a placeable named site (approximate pin) and at least one `verified_sources` line naming where it stands. data/cities/essaouira.json is a one-tree place. A new place gets intro (60 to 100 words), question_meta, question_answer, question_context (150 to 200 words) and three FAQ.
- **A photograph with no date in the file goes into its season by what it shows** (Hidde, 2026-11-17, the Arbour Oak in snow: "als je sneeuw ziet mag die in winter hoor als je twijfelt"): snow or frost means winter, set `photo.taken_month` to 1 (7 south of the equator) with `taken_month_basis` saying why. Bare branches alone, flowers or green leaves are not enough; leave the month empty.
- Then the lead: `status: "published"`, `published_as`, `judged`, `why` (what the photograph shows). A held one: `status: "held"`, `hold`, `why`. A tree held as `not_theirs` gets the standard friendly mail at once: `python3 scripts/hold_reply.py <submission id> not_theirs "<tree name>"` (Hidde, 2026-11-17: "doe zelf een foto maken, maar dan aardig").
- And the same sighting in data/sightings-processed.json: `done[<sighting id>].outcome` becomes `published` or `held`. Left at `lead`, the next intake matches the photograph to the tree you just made and queues it again.
- `python3 scripts/judgement.py --scan`, then each verdict in data/judgements.json, and a `sight:<sighting id>` entry for every contributor photograph now on a page.

## Reports on our trees

Since 2026-11-17 the same run takes every report a reader sends about a tree we already map (Hidde: picked up at once, like the readers' trees). `python3 scripts/tree_reports.py --open` prints them with their words; the intake already closed the moved-pin nudges of a few metres on a confirmed pin (`--auto`). Close each one you handle with `python3 scripts/tree_reports.py --thank pin|dead ...` (the only mails a run sends on a report) or `--close <id> holds` (see "Who answers"). A report you cannot settle in this run stays open: say why in LOG.md, never close it to empty the list.

By reason (CLAUDE.md's rules, in short):

- **dead / gone**: checked and removed the same day when it holds (a news item, a council notice, a second report, a reader's photograph of the stump): first `python3 scripts/tree_reports.py --thank dead <report id> <tree id>` (the standard thank-you, no link since the page goes; it reads the name before the tree leaves data/cities), then `python3 scripts/retire.py <city> <id> --reason "..."`. No evidence either way: leave the tree and close `holds`; a draft for Hidde asks for a photograph.
- **wrong location** and **moved pin**: the reader's place replaces an approximate pin when their words, a grid reference, a GPS fix or a photograph make it a real spot (convert a grid reference yourself); record `pin_source` ("reader report <id>, <what they gave>") and keep `location_precision` honest: `confirmed` only for a GPS fix at the tree. Every pin report on a tree of ours closes with `python3 scripts/tree_reports.py --thank pin <report id> <tree id>`, moved or kept (Hidde, 2026-11-17: "beide zijn toch een bedankje waard"; the text claims no move), unless they wrote words of their own (see "Who answers" below). A moved pin on the reader's own new tree, made while adding it, is part of that tree: no mail, the congratulation comes when it goes live. A confirmed pin moves only on evidence that ours is wrong (their photo, a source, a move of hundreds of metres onto a site the story names). A tree the same account added itself: take their move. A move that lands on another of our trees or in open country without a reason: `holds`.
- **could not tell which tree**: a recognition line (`how_to_recognise`, BRIEF_WRITING.md's rule: restated from what the entry holds) or a trunk photograph. When the row came from the app's collect flow (a sighting id in `tree`, a list of candidates in the words) it is the reader asking which tree their photograph shows: settle it with the sighting (sightings_inbox.py) and close.
- **on the map twice**: same trunk by pins, photos and sources, then keep the richer entry and `retire.py --reason "duplicate of <id>"`. Never on the reader's word alone.
- **something else** / **correction**: a fact they correct is checked like any fact (a source, or their own photograph or sign) and fixed in every language the story exists in; an age they give goes on the page "by a reader's estimate".

**Who answers** (Hidde, 2026-11-17: general feedback "is niet dood of verplaatsen pin maar als er complexe input binnen komt, geschreven tekst"): the run mails only the two standard thank-yous (`--thank pin`, `--thank dead`), and only when the report carries no words of their own beyond the chip, a coordinate or a grid reference. Anything a reader wrote themselves (a question, a story, praise, a correction in sentences, a product question like Android) is general feedback and his to read: act on what it says (fix the fact, move the pin), never write a `reply_text`, put a suggested answer in drafts/reply-reader-<report id>-<date>.md when one would help, and close the report `holds` with no reply. If you fixed the fact the standard mail fits, but they also wrote words: no standard mail either, the draft carries it. A report with nothing you can act on and no draft is closed `holds`. The digest shows him their words whole.
- **collected far**: the photograph decides, through the sighting queue; close the report once it is judged.

## Tips without a photograph

`python3 scripts/judgement.py --scan` also stubs every tree or place a reader sent as words alone (`tip:<submission id>`, kind "a tip without a photograph"); `--unjudged` lists every stub still without a verdict. Read the tip in full (`python3 scripts/inbox.py` or the submissions row), then: a tree we already map gets `publish` with the tree named (nothing to add, or their words as a note); a tree a source confirms (two sources, or one register plus a life check, per CLAUDE.md "Verify") and that can be placed honestly ships as a reader-found tree (`found_by_reader.tip`, their words quoted, no photograph needed, a recognition line instead); otherwise it is recorded as a lead in data/leads/<place>.json with what is missing, verdict `lead`, and, when one fact would settle it (where exactly, is it public), a reply asking for it (`tree_reports.py`-style reply_text on the submission, or a draft when their own words call for one). Write every verdict with `python3 scripts/judgement.py --verdict tip:<id> publish|lead|hold "why"`.

## General feedback

`python3 scripts/feedback.py --open` prints every feedback message without a verdict (one-tap votes and reports are left out). Handle the easy ones and record each with `python3 scripts/feedback.py --close <id> handled|needs_hidde|doubt "what you did"` in one line of your own words, never theirs and never a name (the ledger is public). Handled: a bug you fixed or recorded (`python3 scripts/escaped.py --add`), a tree tip turned into a lead or a tree, an idea filed in PRODUCT_TODO.md, a question the product already answers, thanks that need nothing. Never send or queue a reply to feedback (Hidde, 2026-11-17: "lijkt me beter als ik dat zelf lees"): when an answer would help, write it to drafts/reply-reader-<id>-<date>.md and close the row `needs_hidde`. A decision outside the four verbs, or anything you cannot settle, is `needs_hidde` or `doubt` with the reason. Those reach him in the digest's "Open for you"; nothing else does.

## Readers' words

Then `python3 scripts/reader_words.py`: each reader's note on a live tree whose words no story quotes yet. Put the usable ones on the page (CLAUDE.md "Readers' words go on the page, quoted"): unnamed, their facts stated as theirs, an age they give as "by a reader's estimate", in every language the story exists in. Not usable, and closed with `--done <row id> "why"`: text pasted from a chatbot or a website (headings like "Key Details", bullet summaries; check its facts, never quote it as theirs), an instruction to us, or thanks. A fact from it that a source confirms may go in the story as a fact.

## Before you push

`python3 scripts/qa.py --source-only` must say nothing to fix: it refuses a reader's raw account id in any public file (write `people.ref(uid)`, never the id), which on 2026-11-17 slipped past a run's push and failed every deploy for over an hour.


`python3 scripts/preflight.py` must print 0 problems and `python3 scripts/i18ncheck.py` must be clean: a new tree in a place with a kept translation needs that overlay's tree entry, and every count in the place's texts and overlays follows the new number. Then one LOG.md entry ("## <date> reader judge: ..."), newest first, commit, `git pull --rebase --autostash`, push.

## Limits

About 20 minutes. Readers' trees and reports only: no research passes, no outreach, no enrichment. If more trees wait than fit, do the newest first (they are the ones whose senders are waiting) and leave the rest for the next run; the workflow starts again on the next tree that arrives.
