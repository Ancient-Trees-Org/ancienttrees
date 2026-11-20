-- Whether a sighting's date is the photograph's own, and the month of each
-- further photograph.
--
-- Hidde, 2026-11-20 ("Yes, fix them"), after an audit of every route trees
-- come in by: the tree page files each photograph under Spring, Summer,
-- Autumn or Winter by the month it was taken. The apps send taken_at, and
-- for a photograph chosen from the library whose file carries no date (a
-- screenshot, anything forwarded through a messenger) they filled in the
-- moment it was picked, unmarked, so a summer photo picked in November was
-- filed under autumn.
--
-- NOTHING NEW ABOUT A PERSON. taken_basis says which of two things the date
-- already stored in taken_at is: 'photo' (the camera's moment, the library's
-- creation date or the file's EXIF date) or 'fallback' (the moment it was
-- picked, because the file did not say). Null on rows from before the apps
-- sent it. extra_photo_months is coarser than taken_at: the month only, 1 to
-- 12, of each file in extra_photos, in the same order, null where a file had
-- no date. The same pair the website's tip form has sent since 2026-11-20
-- (supabase/submission-photo-month.sql).
--
-- An existing table: no new GRANT (the 2026-10-30 rule is for new tables).
-- Deletion is unchanged: the row goes with the account. The apps send both
-- keys and retry without them until this is pasted (SightingSync.swift,
-- Collector.kt), and scripts/sightings_inbox.py reads them as optional.

alter table public.sightings
  add column if not exists taken_basis text
  check (taken_basis is null or taken_basis in ('photo', 'fallback'));

alter table public.sightings
  add column if not exists extra_photo_months smallint[]
  check (extra_photo_months is null or cardinality(extra_photo_months) <= 3);
