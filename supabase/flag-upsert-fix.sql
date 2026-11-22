-- THE FLAG FROM THE APPS, SAVED AT LAST (2026-11-22).
--
-- Both apps save your flag with an upsert that carries only user_id, country
-- and flag_hidden (Profiles.swift and Profiles.kt, saveCountry). Postgres
-- checks NOT NULL on the row it would insert before it sees the conflict, so
-- the empty display_name refused every save: 5 of 353 Apple accounts had a
-- flag that day, and the ones that did were set on the website, which PATCHes.
--
-- A BEFORE INSERT trigger runs before that check. When an insert arrives
-- without a name for an account that already has a profile, it takes the
-- name already there. On the conflict, PostgREST updates only the columns the
-- request sent, so the name itself is never rewritten. An insert for an
-- account with no profile yet is left as it was (profile_at_signup makes that
-- row when the account is made).
--
-- Every installed build starts working with this, no new app: both apps try
-- again on each open while the flag is still empty.
--
-- Paste in Supabase, SQL editor, and Run. Safe to run twice.

create or replace function public.profile_keep_name()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  if new.display_name is null then
    new.display_name := (select p.display_name from public.profiles p
                         where p.user_id = new.user_id);
  end if;
  return new;
end
$$;

drop trigger if exists profile_keep_name on public.profiles;
create trigger profile_keep_name before insert on public.profiles
  for each row execute function public.profile_keep_name();
