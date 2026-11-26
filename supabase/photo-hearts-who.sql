-- WHO GAVE A HEART, AND THE PHOTOGRAPHER HEARS IT (Hidde, 2026-11-22: "kun je
-- ook zien als je een hartje krijgt wie je dat heeft gegeven?", "ja benchmarkt
-- dit maak een design", then the bell on Discover "voor nu is het ok").
-- Convention: CONVENTIONS.md "A heart for a visitor's photograph ... Who gave
-- it, and does the photographer hear": Strava, Instagram, komoot and
-- Pinterest open the names from the count, and tell the maker in one
-- activity place, bundled per photograph. Mockup:
-- drafts/design-2026-11-22-heart-who/product.html.
--
-- Paste once into the Supabase SQL editor and run it; idempotent. Needs
-- photo-likes.sql first.
--
-- * photo_likers(photo): who gave this photograph a heart, oldest first, for
--   a signed-in caller only (names are signed-in only, as everywhere). A
--   private profile comes back without name or account: "A visitor", unless
--   it is the caller's own, which the app shows as "You".
-- * my_photo_activity(n): for the caller's own photographs, the hearts other
--   people gave, one row per photograph, newest first: how many, when the
--   last came, up to two public names and faces, and whether any came after
--   the caller last opened Activity.
-- * activity_seen(): the caller opened Activity; the red dot goes.
--
-- ONE NEW COLUMN, profiles.activity_seen_at: when the person last opened
-- Activity, so the dot is the same on every device (hard rule 11: nothing
-- kept on the phone). It goes with the profile when the account is deleted.

alter table public.profiles add column if not exists activity_seen_at timestamptz;

create or replace function public.photo_likers(photo text)
returns table (
  user_id uuid,
  display_name text,
  avatar_url text,
  created_at timestamptz
)
language sql
security definer
set search_path = public
stable
as $$
  -- Your own heart comes back with your account even when your profile is
  -- private, so the list can say "You" (release walk 2026-11-25: the test
  -- account saw itself as "A visitor"). Nobody else sees more than before.
  select case when p.public or l.user_id = auth.uid() then l.user_id end,
         case when p.public or l.user_id = auth.uid() then p.display_name end,
         case when p.public or l.user_id = auth.uid() then p.avatar_url end,
         l.created_at
  from public.photo_likes l
  left join public.profiles p on p.user_id = l.user_id
  where l.photo_id = photo and auth.uid() is not null
  order by l.created_at
  limit 200
$$;

revoke all on function public.photo_likers(text) from public;
grant execute on function public.photo_likers(text) to authenticated;

create or replace function public.my_photo_activity(n int default 40)
returns table (
  photo_id text,
  tree_id text,
  hearts bigint,
  latest_at timestamptz,
  names text[],
  avatars text[],
  is_new boolean
)
language sql
security definer
set search_path = public
stable
as $$
  with mine as (
    select s.id::text as photo_id, s.tree_id
    from public.sightings s
    where s.user_id = auth.uid() and s.status = 'published' and s.photo is not null
  ),
  given as (
    select l.photo_id, l.user_id, l.created_at,
           case when p.public then p.display_name end as name,
           case when p.public then p.avatar_url end as avatar,
           row_number() over (partition by l.photo_id order by l.created_at desc) as k
    from public.photo_likes l
    join mine m on m.photo_id = l.photo_id
    left join public.profiles p on p.user_id = l.user_id
    where l.user_id <> auth.uid()
  ),
  seen as (
    select activity_seen_at as at from public.profiles where user_id = auth.uid()
  )
  select m.photo_id, m.tree_id,
         count(*)::bigint,
         max(g.created_at),
         coalesce(array_agg(g.name order by g.created_at desc) filter (where g.k <= 2 and g.name is not null), '{}'),
         coalesce(array_agg(coalesce(g.avatar, '') order by g.created_at desc) filter (where g.k <= 2 and g.name is not null), '{}'),
         max(g.created_at) > coalesce((select at from seen), '-infinity'::timestamptz)
  from mine m
  join given g on g.photo_id = m.photo_id
  group by m.photo_id, m.tree_id
  order by max(g.created_at) desc
  limit least(greatest(n, 1), 100)
$$;

revoke all on function public.my_photo_activity(int) from public;
grant execute on function public.my_photo_activity(int) to authenticated;

create or replace function public.activity_seen()
returns void
language sql
security definer
set search_path = public
as $$
  update public.profiles set activity_seen_at = now() where user_id = auth.uid()
$$;

revoke all on function public.activity_seen() from public;
grant execute on function public.activity_seen() to authenticated;

notify pgrst, 'reload schema';
