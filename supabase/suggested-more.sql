-- SUGGESTED KEEPS GOING (Hidde, 2026-11-25: "is het ook een idee dat bij
-- gesuggereerde mensen om te volgen dat doorloopt en nieuwe mensen laadt als
-- je naar beneden gaat", then "Ja, bouw het"). Instagram's suggested people
-- load more as you scroll. Under the ambassadors and the photographers of
-- your places (suggested-people.sql), Find people goes on with the public
-- profiles who photographed the most trees anywhere, 20 at a time, and stops
-- after the last one.
--
-- suggested_more(skip, n): the next n public profiles with at least one
-- published photograph, most trees first, never the caller, never anybody
-- the caller already follows or shows in `skip` (the rows already on screen),
-- never somebody either of the two has blocked. Signed-in only. Returns the
-- same fields as suggested_photographers, without a place: id, name, avatar
-- and how many trees they photographed.
--
-- No new table, no new column: published photographs and public profiles
-- are already readable this way through suggested_photographers().
--
-- Paste into Supabase, SQL editor, Run. Safe to run twice.

create or replace function public.suggested_more(skip uuid[] default '{}', n int default 20)
returns table (user_id uuid, display_name text, avatar_url text, trees int)
language sql
security definer
set search_path = public
stable
as $$
  select p.user_id, p.display_name, p.avatar_url,
         count(distinct s.tree_id)::int as trees
  from public.sightings s
  join public.profiles p on p.user_id = s.user_id
  where auth.uid() is not null
    and s.status = 'published'
    and p.public
    and coalesce(p.display_name, '') <> ''
    and p.user_id <> auth.uid()
    and not (p.user_id = any(coalesce(skip, '{}')))
    and not exists (select 1 from public.follows f
                    where f.follower = auth.uid() and f.followee = p.user_id)
    and not exists (select 1 from public.blocks b
                    where (b.blocker = auth.uid() and b.blocked = p.user_id)
                       or (b.blocker = p.user_id and b.blocked = auth.uid()))
  group by p.user_id, p.display_name, p.avatar_url
  order by trees desc, p.display_name, p.user_id
  limit least(greatest(n, 1), 50)
$$;

revoke all on function public.suggested_more(uuid[], int) from public;
revoke all on function public.suggested_more(uuid[], int) from anon;
grant execute on function public.suggested_more(uuid[], int) to authenticated;

notify pgrst, 'reload schema';
