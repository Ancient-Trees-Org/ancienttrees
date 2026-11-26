-- FOR HIDDE TO PASTE in the Supabase SQL editor (2026-11-26). Safe to run twice.
--
-- THE FEED, LIVE FIRST (Hidde, 2026-11-26: "yes letsgo", on "eerst live,
-- daarna gecheckt"). The convention of AllTrails, Strava, iNaturalist and
-- komoot, and ours for a photograph in a tree's strip since 2026-10-24
-- (CLAUDE.md, Reader input): what a reader shares is public at once, and the
-- check comes after. The feed no longer waits on GitHub, the judge or a deploy.
--
-- feed() now returns two kinds of row, newest first:
-- * CHECKED (checked = true): the `feed` table, written by
--   scripts/feed_publish.py after the judge put it live: tree name, place, pin,
--   page, picture. Unchanged from feed.sql.
-- * JUST SHARED (checked = false): a shared sighting with a photograph that has
--   no feed row yet, straight from `sightings`. The reader's own name for the
--   tree, their photograph (the public copy the app already made for the share
--   link, without location data in the file), and the share page as its link.
--   PLACE SHOWN (Hidde, 2026-11-26: "toon plek gewoon, we kunnen er altijd op
--   terug komen", over the first version that showed none): the nearest of our
--   own places within about 50 km (feed_places, filled by
--   scripts/feed_publish.py) and the point rounded to two decimals, about a
--   kilometre, so the post says where without pointing at a house before the
--   judge has looked (hard rule 10, shared-sightings.sql). The exact pin comes
--   with the checked row.
--
-- What takes a post down: the judge's hold or reject (status checking or
-- declined), the reader unsharing it, a hidden feed row (a report, a retire),
-- or a deleted account. Our own accounts never show. Only the last 14 days
-- are live; anything older and still unjudged waits for the judge.
--
-- Nothing new is stored. The privacy page's sentence on "the list of new
-- photographs from visitors" already covers it.

-- Our places, for the name of a post the judge has not looked at yet. Public
-- facts (a place's name and middle), no person in it.
create table if not exists public.feed_places (
  slug text primary key,
  name text not null,
  lat double precision not null,
  lng double precision not null
);
alter table public.feed_places enable row level security;
grant select, insert, update, delete on public.feed_places to service_role;

drop function if exists public.feed(int, timestamptz, text);

create or replace function public.feed(
  n int default 24,
  before_at timestamptz default null,
  before_key text default null
)
returns table (
  key text,
  kind text,
  tree_id text,
  tree_name text,
  place text,
  url text,
  latitude double precision,
  longitude double precision,
  photo_url text,
  photo_w int,
  photo_h int,
  published_at timestamptz,
  author_name text,
  author_avatar text,
  author_id uuid,
  checked boolean
)
language sql
security definer
set search_path = public, extensions, storage
stable
as $$
  with posts as (
    select f.key, f.kind, f.tree_id, f.tree_name, f.place, f.url,
           f.latitude, f.longitude, f.photo_url, f.photo_w, f.photo_h,
           f.published_at, f.user_id, true as checked
      from public.feed f
     where not f.hidden
    union all
    select lower(s.id::text), case when s.tree_id is null then 'tree' else 'photo' end,
           s.tree_id, coalesce(nullif(s.name, ''), 'A tree'),
           coalesce((select fp.name from public.feed_places fp
                      where abs(fp.lat - s.lat) < 0.5 and abs(fp.lng - s.lng) < 0.7
                      order by (fp.lat - s.lat) ^ 2 + ((fp.lng - s.lng) * cos(radians(s.lat))) ^ 2
                      limit 1), ''),
           '/t/?id=' || lower(s.id::text),
           round(s.lat::numeric, 2)::double precision, round(s.lng::numeric, 2)::double precision,
           'https://caimvxiyrtifilimlkqw.supabase.co/storage/v1/object/public/shared-sightings/' || s.photo,
           null, null,
           coalesce(o.created_at, s.taken_at), s.user_id, false
      from public.sightings s
      left join storage.objects o on o.bucket_id = 'sightings' and o.name = s.photo
     where s.shared and s.photo is not null
       and s.status in ('mine', 'sent', 'published')
       and coalesce(o.created_at, s.taken_at) > now() - interval '14 days'
       and not exists (select 1 from public.feed f2 where f2.key = lower(s.id::text))
       and encode(digest(s.user_id::text, 'sha1'), 'hex') <> all (array[
         'cc6a542385091392e455911c0d7e351bf0148a4b',
         'ef98f5dbe51e86e6236031d19bdce2364272c6b6',
         'd4e6c578be12fd0916a6277fa7bba4b482405484',
         'a9c1498c827881dd41e3e8cd39edc1a8fbf399f9'
       ])
  )
  select p.key, p.kind, p.tree_id, p.tree_name, p.place, p.url,
         p.latitude, p.longitude, p.photo_url, p.photo_w, p.photo_h, p.published_at,
         case when pr.public then pr.display_name end,
         case when pr.public then pr.avatar_url end,
         case when pr.public and auth.uid() is not null then p.user_id end,
         p.checked
    from posts p
    left join public.profiles pr on pr.user_id = p.user_id
   where before_at is null
      or p.published_at < before_at
      or (p.published_at = before_at and p.key < before_key)
   order by p.published_at desc, p.key desc
   limit least(greatest(n, 1), 48)
$$;

revoke all on function public.feed(int, timestamptz, text) from public;
grant execute on function public.feed(int, timestamptz, text) to anon, authenticated;
