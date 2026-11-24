-- A NEW FOLLOWER IN ACTIVITY (Hidde, 2026-11-24: "als ik iemand follow krijgt
-- die persoon dan een notificatie net als bij likes?", then "Ja, bouw het"
-- on drafts/design-2026-11-24-follow-activity/index.html). Instagram's
-- Activity: "X started following you." with Follow back at the row's end, in
-- the same list as the likes; Strava the same ("Notify me when someone
-- follows me"). One row per follower, never bundled, so every row has its own
-- Follow back. An unfollow tells nobody: the row simply goes.
--
-- Paste once into the Supabase SQL editor and run it; idempotent. Needs
-- profiles.sql and photo-hearts-who.sql first.
--
-- * my_activity(n): everything Activity lists, newest first, in one call.
--   kind 'heart': my_photo_activity's row (one per photograph, bundled).
--   kind 'follow': one per person who follows the caller: their account,
--   their name and face when the profile is public (else "A visitor" in the
--   apps), when they followed, whether the caller follows them back, and
--   whether it came after the caller last opened Activity (the bell's dot).
--   my_photo_activity stays for app builds that read it.
--
-- NO NEW DATA: who follows whom and since when is already in public.follows,
-- readable as every followers list reads it.

create or replace function public.my_activity(n int default 40)
returns table (
  kind text,
  photo_id text,
  tree_id text,
  hearts bigint,
  latest_at timestamptz,
  names text[],
  avatars text[],
  is_new boolean,
  user_id uuid,
  following boolean
)
language sql
security definer
set search_path = public
stable
as $$
  with seen as (
    select coalesce(activity_seen_at, '-infinity'::timestamptz) as at
    from public.profiles where profiles.user_id = auth.uid()
  ),
  hearts as (
    select 'heart'::text as kind, a.photo_id, a.tree_id, a.hearts, a.latest_at,
           a.names, a.avatars, a.is_new, null::uuid as user_id, null::boolean as following
    from public.my_photo_activity(100) a
  ),
  followers as (
    select 'follow'::text, null::text, null::text, 1::bigint, f.created_at,
           case when p.public and p.display_name is not null then array[p.display_name] else '{}'::text[] end,
           case when p.public and p.display_name is not null then array[coalesce(p.avatar_url, '')] else '{}'::text[] end,
           f.created_at > coalesce((select at from seen), '-infinity'::timestamptz),
           f.follower,
           exists (select 1 from public.follows b
                   where b.follower = auth.uid() and b.followee = f.follower)
    from public.follows f
    left join public.profiles p on p.user_id = f.follower
    where f.followee = auth.uid()
  )
  select * from (
    select * from hearts
    union all
    select * from followers
  ) x
  where auth.uid() is not null
  order by x.latest_at desc
  limit least(greatest(n, 1), 100)
$$;

revoke all on function public.my_activity(int) from public;
grant execute on function public.my_activity(int) to authenticated;

notify pgrst, 'reload schema';
