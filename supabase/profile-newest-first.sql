-- A PUBLIC PROFILE RUNS NEWEST FIRST.
--
-- Hidde, 2026-11-26: "de volgorde op je profiel moet zijn dat je laatstgenomen
-- foto als eerste getoond wordt en dat die dan terug in de tijd loopt". This
-- reverses the 2026-10-19 rule "no time order" on a public profile, at his
-- word: the ORDER now shows, still no date. Collected, Want to visit and their
-- own trees come newest first, and 'recent' gives one order across our trees
-- and their own (the phones and profile.astro mix the grid by it).
-- Replaces approved-on-profiles.sql's function; everything else it returns is
-- unchanged.
--
-- Paste into Supabase, SQL editor, Run. Safe to run twice.

create or replace function public.public_profile(uid uuid)
returns json
language sql
security definer
set search_path = public
stable
as $$
  select json_build_object(
    'user_id', p.user_id,
    'display_name', p.display_name,
    'avatar_url', p.avatar_url,
    'country', p.country,
    'created_at', (select u.created_at::date from auth.users u where u.id = p.user_id),
    'followers', (select count(*) from public.follows where followee = p.user_id),
    'following', (select count(*) from public.follows where follower = p.user_id),
    'ambassador', coalesce((select json_agg(a.place_name order by a.since)
                            from public.ambassadors a where a.user_id = p.user_id), '[]'::json),
    'visited', coalesce((select json_agg(v.tree_id order by v.created_at desc)
                         from public.visited v where v.user_id = p.user_id), '[]'::json),
    'saves', coalesce((select json_agg(s.tree_id order by s.created_at desc)
                       from public.saves s where s.user_id = p.user_id
                         and not exists (select 1 from public.visited v
                                         where v.user_id = s.user_id and v.tree_id = s.tree_id
                                           and v.created_at >= s.created_at)), '[]'::json),
    'approved', coalesce((select json_agg(distinct sg.tree_id)
                          from public.sightings sg
                          where sg.user_id = p.user_id and sg.added
                            and sg.status = 'published' and sg.tree_id is not null), '[]'::json),
    -- The shared copy is the only photograph a visitor may load
    -- (shared-sightings.sql). Its path keeps the phone's own spelling of the
    -- id, which is upper case on both apps.
    'own', coalesce((select json_agg(json_build_object(
                        'id', sg.id,
                        'name', sg.name,
                        'species', sg.species,
                        'photo', p.user_id::text || '/' || upper(sg.id::text) || '.jpg',
                        'lat', sg.lat,
                        'lng', sg.lng)
                      order by sg.created_at desc)
                     from public.sightings sg
                     where sg.user_id = p.user_id and sg.tree_id is null
                       and sg.photo is not null and sg.shared), '[]'::json),
    -- One order for the Collected grid, newest upload first: a collected
    -- tree at its newest photograph by this person (else the tick), an own
    -- tree at its upload. Keys only, never a date.
    'recent', coalesce((select json_agg(r.k order by r.at desc) from (
        select 't:' || v.tree_id as k,
               greatest(v.created_at, coalesce((select max(sg.created_at) from public.sightings sg
                                                where sg.user_id = p.user_id and sg.tree_id = v.tree_id),
                                               v.created_at)) as at
        from public.visited v where v.user_id = p.user_id
        union all
        select 'o:' || lower(sg.id::text), sg.created_at
        from public.sightings sg
        where sg.user_id = p.user_id and sg.tree_id is null and sg.photo is not null and sg.shared
      ) r), '[]'::json)
  )
  from public.profiles p
  where p.user_id = uid and p.public
$$;

revoke all on function public.public_profile(uuid) from public;
grant execute on function public.public_profile(uuid) to anon, authenticated;
