# Reader judge: the brief

The instant run (`.github/workflows/reader-judge.yml`) reads this. It starts minutes after a reader sends a tree or a photograph, so their tree is live while they still remember sending it. Hidde, 2026-11-17: "should be instant honestly". The rules are CLAUDE.md's ("Verify", "Reader input"); this file is only the order of work.

## What you judge

Everything a reader sent that has no verdict yet:

1. `python3 scripts/sightings_inbox.py --status`: photographs of trees we already map (data/sighting-queue.json, files in out/sightings/).
2. Leads in data/leads/_sightings.json with `status: "lead"` and no `hold`: trees we do not map. Their photographs are already on this machine at out/sightings/<sighting id>.jpg (`scripts/fetch_waiting_photos.py` ran before you).

A lead with `status: "lead"` and no `hold` is WAITING, whatever its `why` says. A `why` written before 2026-11-17 ("needs the site named", "no girth", "for a later pass", "a lead") is not a verdict under the closed list; judge it again from the photograph. Do not leave such leads "for the next run": they are the work.

Look at every photograph with Read before you decide. Never judge one blind; if a file is missing, leave that tree for the next run and say so in LOG.md.

## The decision (CLAUDE.md "Verify", the closed list)

A reader's tree goes live when it has a GPS fix or a photograph and is somewhat special. It is held only for a reason from the closed list, written in the lead's `hold` field: `bad_frame`, `wrong_tree`, `wrong_subject`, `not_special`, `dead`, `not_public`, `no_location`, `not_theirs`, and on a real doubt `doubt_location`, `doubt_photo`, `doubt_info`, `inappropriate`. No girth, age, source, site name or "a later pass" is ever a reason. A photograph that shows one of OUR trees (check `nearest_published_m` and the species) belongs on that tree, not on a new page; if two of ours could be it, hold as `wrong_tree` and the reply asks which.

## Putting it live

- **A photo of a tree we map**: verdicts JSON, then `python3 scripts/sightings_publish.py verdicts.json --send` (its docstring has the fields). Never by hand.
- **A new tree**: copy the pattern of `scripts/build_reader_trees_2026_11_17.py` (one script per run, under out/tmp/, never committed): `write_image()` for the photo, `found_by_reader.sighting_id`, `pin_source` from the GPS fix, the reader's own words quoted, their figures stated as theirs, a story of 150 to 250 words, a recognition line, an honest `access` line. Readers' girths stay in the story, never in `girth_cm`. A tree without GPS needs a placeable named site (approximate pin) and at least one `verified_sources` line naming where it stands. data/cities/essaouira.json is a one-tree place. A new place gets intro (60 to 100 words), question_meta, question_answer, question_context (150 to 200 words) and three FAQ.
- Then the lead: `status: "published"`, `published_as`, `judged`, `why` (what the photograph shows). A held one: `status: "held"`, `hold`, `why`.
- And the same sighting in data/sightings-processed.json: `done[<sighting id>].outcome` becomes `published` or `held`. Left at `lead`, the next intake matches the photograph to the tree you just made and queues it again.
- `python3 scripts/judgement.py --scan`, then each verdict in data/judgements.json, and a `sight:<sighting id>` entry for every contributor photograph now on a page.

## Before you push

`python3 scripts/preflight.py` must print 0 problems and `python3 scripts/i18ncheck.py` must be clean: a new tree in a place with a kept translation needs that overlay's tree entry, and every count in the place's texts and overlays follows the new number. Then one LOG.md entry ("## <date> reader judge: ..."), newest first, commit, `git pull --rebase --autostash`, push.

## Limits

About 20 minutes. Readers' trees only: no research passes, no outreach, no enrichment. If more trees wait than fit, do the newest first (they are the ones whose senders are waiting) and leave the rest for the next run; the workflow starts again on the next tree that arrives.
