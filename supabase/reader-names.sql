-- FOR HIDDE TO PASTE in the Supabase SQL editor (2026-11-17). Idempotent.
--
-- WHO WROTE THE NOTE, WHO TOOK THE PHOTOGRAPH (Hidde, 2026-11-17: "bij foto's
-- wel namen gaan noemen van degene die het heeft opgeloot. Als die een account
-- hebben, dan worden die accounts ook klikbaar"; and a tap on a note's name
-- must open that person's profile, not the sign-in sheet).
--
-- The same rule as new_from_visitors() (new-from-visitors.sql), now for the
-- tree page:
-- * Everyone (anon too): the display name and avatar ONLY when that profile
--   is public, else null; the page then prints no name under a photograph
--   and "A visitor" under a note.
-- * The account id only to a signed-in caller and only for a public profile,
--   so a tap on the name opens the profile; signed out, the tap asks for a
--   sign-in first and lands on the profile afterwards.
-- * Never one of our own accounts (data/our-accounts.json, sha1 of each id):
--   our own photographs are never credited.
--
-- Nothing new is stored: no table, no column. Function grants only.

-- 1. tree_notes_for() gains author_id. The return type changes, so the old
--    function is dropped first (a create or replace cannot change columns).
drop function if exists public.tree_notes_for(text[]);
create function public.tree_notes_for(ids text[])
returns table (
  tree_id text,
  body text,
  created_at timestamptz,
  author_name text,
  author_avatar text,
  author_id uuid
)
language sql
security definer
set search_path = public
stable
as $$
  select n.tree_id, n.body, n.created_at,
         case when p.public then p.display_name end,
         case when p.public then p.avatar_url end,
         case when p.public and auth.uid() is not null then n.user_id end
  from public.tree_notes n
  left join public.profiles p on p.user_id = n.user_id
  where n.tree_id = any(ids) and not n.hidden
  order by n.created_at desc
  limit 200
$$;

revoke all on function public.tree_notes_for(text[]) from public;
grant execute on function public.tree_notes_for(text[]) to anon, authenticated;

-- 2. photo_authors(): who sent each photograph on a tree page, by the id the
--    feed carries (a sightings uuid from the app, "tip-<n>" from the website's
--    form). Only a photograph that went live: a sighting marked published, a
--    submission that carried a photograph.
create or replace function public.photo_authors(ids text[])
returns table (
  photo_id text,
  author_name text,
  author_avatar text,
  author_id uuid
)
language sql
security definer
set search_path = public, extensions
stable
as $$
  with sent as (
    select s.id::text as photo_id, s.user_id
    from public.sightings s
    where s.id::text = any(ids) and s.status = 'published'
    union all
    select 'tip-' || t.id::text, t.user_id
    from public.submissions t
    where ('tip-' || t.id::text) = any(ids) and t.user_id is not null and t.photo is not null
  )
  select distinct on (sent.photo_id) sent.photo_id,
         p.display_name,
         p.avatar_url,
         case when auth.uid() is not null then sent.user_id end
  from sent
  join public.profiles p on p.user_id = sent.user_id and p.public
  where encode(digest(sent.user_id::text, 'sha1'), 'hex') <> all (array[
        'cc6a542385091392e455911c0d7e351bf0148a4b',
        'ef98f5dbe51e86e6236031d19bdce2364272c6b6',
        'd4e6c578be12fd0916a6277fa7bba4b482405484',
        'a9c1498c827881dd41e3e8cd39edc1a8fbf399f9'
      ])
  limit 60
$$;

revoke all on function public.photo_authors(text[]) from public;
grant execute on function public.photo_authors(text[]) to anon, authenticated;

notify pgrst, 'reload schema';
