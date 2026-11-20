-- The month a tip's photograph was taken.
--
-- Hidde, 2026-11-19 ("Yes, add it"), after a chestnut in copper leaf and
-- cherries in blossom sat on their pages with an empty Seasons row: the tree
-- page files a photograph under Spring, Summer, Autumn or Winter by the month
-- it was taken. The apps send that date (sightings.taken_at); the website's
-- tip form (contribute page, this table) sent none, and its re-encode throws
-- the file's own date away.
--
-- THE MONTH ONLY, 1 to 12: no day, no time, no year. It is all the page
-- needs, and a month says nothing about when somebody stood somewhere. It is
-- read from the photograph's own EXIF date in the browser (atPhotoDate in
-- site/src/lib/image-downsize-js.ts) and left empty when the file has none.
--
-- An existing table: no new GRANT (supabase/README rule of 2026-10-30 is for
-- new tables). Deletion is unchanged: the row goes with the account.

alter table public.submissions
  add column if not exists photo_month smallint
  check (photo_month is null or photo_month between 1 and 12);
