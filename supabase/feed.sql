-- FOR HIDDE TO PASTE in the Supabase SQL editor (2026-11-26). Safe to run twice.
--
-- THE FEED, FROM THE SERVER ONLY (Hidde, 2026-11-26: "dit blijft maar fout
-- gaan ... hoe gaan we zorgen dat die feed niet elke keer afhankelijk is van
-- zon lange deploy"; "ja zoiets is het idee", the Feed tab, AllTrails'
-- Community, iNaturalist's recent observations, Strava's feed).
--
-- Until now the visitors row took its list from the server but each tile's
-- tree name, place and picture from the last deploy, so a tree the judge had
-- just put live was invisible until the build caught up, and a failed deploy
-- stopped the row altogether. Here every row carries all a tile needs: the
-- tree's name and place, its pin, and a picture in the public `feed` bucket.
--
-- WHO WRITES: only scripts/feed_publish.py with the service key, run by the
-- reader judge after it has LOOKED at each photograph (Hidde, same day:
-- "doet de judge dat wel?"). A photograph that went into a tree's strip
-- before the judge saw it (live first, 2026-10-24) reaches the feed only once
-- judged. A photograph or tree taken down (report, retire, unstrip) sets
-- `hidden` on the next run and leaves the feed.
--
-- WHO READS: everyone, through feed() only (the table itself has no anon
-- policy). Same rules as new_from_visitors(): the display name and avatar
-- only of a public profile, else null ("A visitor"); the account id only to a
-- signed-in caller and only for a public profile. Paging by the last row seen.
--
-- PRIVACY: nothing new about a person is stored. user_id is the account the
-- sightings row already names; the rest is the tree as published.

create table if not exists public.feed (
  key text primary key,                -- sighting uuid, or 'tree:<tree id>' for a tip
  kind text not null check (kind in ('tree', 'photo')),
  tree_id text not null,
  sighting_id uuid,
  tree_name text not null,
  place text not null default '',
  url text not null default '',         -- path on ancienttrees.app, e.g. /goll-woods/white-oak-of-goll-woods
  latitude double precision,
  longitude double precision,
  photo_url text,                       -- public URL in the feed bucket
  photo_w int,
  photo_h int,
  user_id uuid,
  published_at timestamptz not null default now(),
  hidden boolean not null default false
);

create index if not exists feed_order on public.feed (published_at desc, key desc) where not hidden;

alter table public.feed enable row level security;
-- No policy for anon or authenticated: the table is read through feed().
grant select, insert, update, delete on public.feed to service_role;

insert into storage.buckets (id, name, public)
values ('feed', 'feed', true)
on conflict (id) do update set public = true;

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
  author_id uuid
)
language sql
security definer
set search_path = public, extensions
stable
as $$
  select f.key, f.kind, f.tree_id, f.tree_name, f.place, f.url,
         f.latitude, f.longitude, f.photo_url, f.photo_w, f.photo_h, f.published_at,
         case when p.public then p.display_name end,
         case when p.public then p.avatar_url end,
         case when p.public and auth.uid() is not null then f.user_id end
  from public.feed f
  left join public.profiles p on p.user_id = f.user_id
  where not f.hidden
    and (before_at is null
         or f.published_at < before_at
         or (f.published_at = before_at and f.key < before_key))
  order by f.published_at desc, f.key desc
  limit least(greatest(n, 1), 48)
$$;

revoke all on function public.feed(int, timestamptz, text) from public;
grant execute on function public.feed(int, timestamptz, text) to anon, authenticated;
