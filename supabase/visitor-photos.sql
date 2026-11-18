-- FOR HIDDE TO PASTE in the Supabase SQL editor (2026-11-18).
--
-- THE "SEE ALL" PAGE OF NEW FROM VISITORS (Hidde, 2026-11-18: "a see all
-- button from new from visitors that leads to a page that has infinite scroll
-- on it", then "ok build the see all page"). /visitors shows every photograph
-- visitors sent that went live, newest first, 24 at a time as the reader
-- scrolls: Unsplash's and Pinterest's feed (CONVENTIONS.md 2026-10-10,
-- endless similar items).
--
-- new_from_visitors() (new-from-visitors.sql) stops at 24 and mixes people
-- for the home row; this one pages. The same rules for who sees what:
-- * Everyone: the photograph's row, the tree id, when it was taken, and the
--   display name and avatar ONLY of a public profile, else null ("A visitor").
-- * The account id only to a signed-in caller and only for a public profile.
-- * Never our own accounts (the same four hashes as new-from-visitors.sql).
--
-- Paging is by the last row seen (its time and id), so a photograph that
-- goes live while somebody scrolls never repeats or skips a tile. Nothing new
-- is stored; no new column; a function grant only.
--
-- WHEN IT WAS SENT, NOT WHEN IT WAS TAKEN (Hidde, 2026-11-18, second paste:
-- "sort by when it was sent, not when taken"). sightings has no created_at,
-- and updated_at moves with every status write, so the clock is the
-- photograph's own upload: storage.objects.created_at for s.photo in the
-- sightings bucket (measured that day: the Waipoua photographs taken in 2007
-- were sent on 2026-11-15). The camera's time stands in only where the file
-- is gone. published_at in the result is that sent time.

create or replace function public.visitor_photos(
  n int default 24,
  before_at timestamptz default null,
  before_id uuid default null
)
returns table (
  sighting_id uuid,
  tree_id text,
  published_at timestamptz,
  author_name text,
  author_avatar text,
  author_id uuid
)
language sql
security definer
set search_path = public, extensions, storage
stable
as $$
  select id, tree_id, at, author_name, author_avatar, author_id
  from (
    select s.id, s.tree_id,
           coalesce(o.created_at, s.taken_at, s.updated_at) as at,
           case when p.public then p.display_name end as author_name,
           case when p.public then p.avatar_url end as author_avatar,
           case when p.public and auth.uid() is not null then s.user_id end as author_id
    from public.sightings s
    left join storage.objects o on o.bucket_id = 'sightings' and o.name = s.photo
    left join public.profiles p on p.user_id = s.user_id
    where s.status = 'published' and s.tree_id is not null and s.photo is not null
      and encode(digest(s.user_id::text, 'sha1'), 'hex') <> all (array[
        'cc6a542385091392e455911c0d7e351bf0148a4b',
        'ef98f5dbe51e86e6236031d19bdce2364272c6b6',
        'd4e6c578be12fd0916a6277fa7bba4b482405484',
        'a9c1498c827881dd41e3e8cd39edc1a8fbf399f9'
      ])
  ) sent
  where before_at is null or (at, id) < (before_at, before_id)
  order by at desc, id desc
  limit least(greatest(n, 1), 48)
$$;

revoke all on function public.visitor_photos(int, timestamptz, uuid) from public;
grant execute on function public.visitor_photos(int, timestamptz, uuid) to anon, authenticated;

-- AND THE HOME ROW ON THE SAME CLOCK (the same paste; new-from-visitors.sql
-- carries the same text). Hidde asked for "the most recent uploads" on
-- 2026-11-07; taken_at was the nearest clock then, the upload time is the
-- real one. Each person's newest first, everyone once before anyone twice,
-- as before.
create or replace function public.new_from_visitors(n int default 12)
returns table (
  sighting_id uuid,
  tree_id text,
  published_at timestamptz,
  author_name text,
  author_avatar text,
  author_id uuid
)
language sql
security definer
set search_path = public, extensions, storage
stable
as $$
  select id, tree_id, at, author_name, author_avatar, author_id
  from (
    select s.id, s.tree_id, coalesce(o.created_at, s.taken_at, s.updated_at) as at,
           case when p.public then p.display_name end as author_name,
           case when p.public then p.avatar_url end as author_avatar,
           case when p.public and auth.uid() is not null then s.user_id end as author_id,
           row_number() over (partition by s.user_id
                              order by coalesce(o.created_at, s.taken_at, s.updated_at) desc) as turn
    from public.sightings s
    left join storage.objects o on o.bucket_id = 'sightings' and o.name = s.photo
    left join public.profiles p on p.user_id = s.user_id
    where s.status = 'published' and s.tree_id is not null and s.photo is not null
      and encode(digest(s.user_id::text, 'sha1'), 'hex') <> all (array[
        'cc6a542385091392e455911c0d7e351bf0148a4b',
        'ef98f5dbe51e86e6236031d19bdce2364272c6b6',
        'd4e6c578be12fd0916a6277fa7bba4b482405484',
        'a9c1498c827881dd41e3e8cd39edc1a8fbf399f9'
      ])
  ) ranked
  order by turn, at desc
  limit least(greatest(n, 1), 24)
$$;

revoke all on function public.new_from_visitors(int) from public;
grant execute on function public.new_from_visitors(int) to anon, authenticated;

-- Tell the API about the new function at once.
notify pgrst, 'reload schema';
