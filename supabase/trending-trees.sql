-- TRENDING THIS MONTH, Discover's numbered shelf (2026-11-26, after
-- Hidde's look at Polarsteps' Verkennen tab; his note on the first design:
-- "is het niet veel logischer om bomen trending te maken: bomen die veel
-- worden gefotografeerd, geliked, worth a visit").
--
-- Paste once into the Supabase SQL editor and run it; idempotent. Pasted by
-- Hidde 2026-11-26. Nothing
-- new is stored: it reads four tables that already exist.
--
-- trending_trees(days, n): the trees the most DIFFERENT people did something
-- with in the last `days` days, counting each person once per tree, whatever
-- they did: shared a published photograph of it (sightings), gave a heart to
-- one of its photographs (photo_likes), voted it Worth the visit
-- (tree_votes, 'up') or saved it to Want to visit (saves). Our own accounts
-- are left out (the same list as visitor_photos). Ties go to more actions.
--
-- Returns tree ids and counts only: no account, no name, no date, so anon
-- may call it, as tree_vote_counts and photo_like_counts already allow.

create or replace function public.trending_trees(days int default 30, n int default 9)
returns table (tree_id text, people int, actions int)
language sql
security definer
set search_path = public, extensions
stable
as $$
  with since as (select now() - make_interval(days => least(greatest(days, 1), 90)) as t),
  acts as (
    select s.tree_id, s.user_id from public.sightings s, since
      where s.status = 'published' and s.tree_id is not null and s.photo is not null
        and coalesce(s.taken_at, s.updated_at) >= since.t
    union all
    select s.tree_id, l.user_id from public.photo_likes l
      join public.sightings s on lower(s.id::text) = l.photo_id, since
      where s.status = 'published' and s.tree_id is not null and l.created_at >= since.t
    union all
    select v.tree_id, v.user_id from public.tree_votes v, since
      where v.vote = 'up' and v.created_at >= since.t
    union all
    select sv.tree_id, sv.user_id from public.saves sv, since
      where sv.created_at >= since.t
  )
  select tree_id, count(distinct user_id)::int as people, count(*)::int as actions
  from acts
  where encode(digest(user_id::text, 'sha1'), 'hex') <> all (array[
    'cc6a542385091392e455911c0d7e351bf0148a4b',
    'ef98f5dbe51e86e6236031d19bdce2364272c6b6',
    'd4e6c578be12fd0916a6277fa7bba4b482405484',
    'a9c1498c827881dd41e3e8cd39edc1a8fbf399f9'
  ])
  group by tree_id
  order by people desc, actions desc, tree_id
  limit least(greatest(n, 1), 30)
$$;

revoke all on function public.trending_trees(int, int) from public;
grant execute on function public.trending_trees(int, int) to anon, authenticated;
