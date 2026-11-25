-- Reader judge trigger (2026-11-17). FOR HIDDE to paste into the SQL editor,
-- once, AFTER storing the GitHub token in the Vault (steps in
-- supabase/reader-judge-setup.md).
--
-- When a reader shares a photograph of a tree (sightings) or sends a tree
-- from the website or app (submissions, kind tree or city), this asks GitHub
-- to start .github/workflows/reader-judge.yml, which judges and publishes it
-- within about 20 minutes. Hidde, 2026-11-17: "should be instant honestly".
--
-- Nothing about the reader leaves Supabase: the call carries only the words
-- "reader-tree", never an id, a name or a coordinate. The run reads what
-- waits itself, with the service key, as the night run does.
--
-- Revert: drop the two triggers and the function (bottom of this file).

create extension if not exists pg_net with schema extensions;

create or replace function public.ping_reader_judge()
returns trigger
language plpgsql
security definer
set search_path = public, extensions
as $$
declare
  tok text;
begin
  select decrypted_secret into tok
    from vault.decrypted_secrets
   where name = 'github_dispatch_token'
   limit 1;
  if tok is null then
    return new;  -- no token stored yet: the two-hourly knock still picks it up
  end if;
  perform net.http_post(
    url := 'https://api.github.com/repos/Ancient-Trees-Org/ancienttrees/dispatches',
    body := jsonb_build_object('event_type', 'reader-tree'),
    headers := jsonb_build_object(
      'Authorization', 'Bearer ' || tok,
      'Accept', 'application/vnd.github+json',
      'X-GitHub-Api-Version', '2022-11-28',
      'User-Agent', 'ancienttrees-reader-judge',
      'Content-Type', 'application/json'
    )
  );
  return new;
exception when others then
  -- A failed ping must never stop a reader's photograph from saving.
  return new;
end;
$$;

revoke all on function public.ping_reader_judge() from public, anon, authenticated;

-- A photograph a reader shares: on insert, or when it becomes shared or
-- gets its photo after the row was made.
drop trigger if exists reader_judge_on_sighting on public.sightings;
create trigger reader_judge_on_sighting
  after insert or update of photo, shared on public.sightings
  for each row
  when (new.shared is true and new.photo is not null)
  execute function public.ping_reader_judge();

-- A tree or a place sent from the website or the app.
drop trigger if exists reader_judge_on_submission on public.submissions;
create trigger reader_judge_on_submission
  after insert on public.submissions
  for each row
  when (new.kind in ('tree', 'city'))
  execute function public.ping_reader_judge();

-- Revert:
-- drop trigger if exists reader_judge_on_sighting on public.sightings;
-- drop trigger if exists reader_judge_on_submission on public.submissions;
-- drop function if exists public.ping_reader_judge();
