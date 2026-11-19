-- Sign-in links nobody used (2026-11-19, Hidde: "kunnen we dat nagaan?").
-- A link or code Supabase sent stays in auth.one_time_tokens until it is used
-- or replaced. One older than `min_age` whose account has not signed in since
-- means the mail never arrived or did not work. scripts/signin_watch.py reads
-- this at every knock and asks Supabase to send the mail again (at most twice).
-- Returns ids only, never an address; only the service key may call it.
-- Run by the session that wrote it, through the Management API, 2026-11-19.

create or replace function public.stuck_signin_links(min_age interval default '1 hour',
                                                     max_age interval default '3 days')
returns table (user_id uuid, token_type text, asked_at timestamptz)
language sql
security definer
set search_path = ''
as $$
  select t.user_id, t.token_type::text, t.created_at at time zone 'UTC'
  from auth.one_time_tokens t
  join auth.users u on u.id = t.user_id
  where t.token_type::text in ('recovery_token', 'confirmation_token')
    and t.created_at < (now() at time zone 'UTC') - min_age
    and t.created_at > (now() at time zone 'UTC') - max_age
    and (u.last_sign_in_at is null or u.last_sign_in_at < t.created_at at time zone 'UTC');
$$;

revoke all on function public.stuck_signin_links(interval, interval) from public, anon, authenticated;
grant execute on function public.stuck_signin_links(interval, interval) to service_role;
