-- FOR HIDDE TO PASTE in the Supabase SQL editor (2026-11-26), after putting
-- the new GitHub token in line 1 of step 1. Safe to run twice.
--
-- THE READER JUDGE ON SUPABASE'S CLOCK, NOT GITHUB'S (Hidde, 2026-11-26:
-- "de website heeft nog steeds geen nieuwe bomen"). GitHub dropped every
-- frequent cron of this repository: from 02:22 to past 09:00 UTC on 11-26 not
-- one reader-judge (every 15 min), knock (every 20) or Site up (every 15) run
-- arrived, so the watchdogs built on 11-25 never woke either; only the daily
-- workflows came, hours late. A workflow_dispatch is never dropped, so
-- Supabase's own pg_cron asks GitHub for a judge run every ten minutes, with
-- poll=yes: the run polls first and starts no agent unless a reader sent
-- something (reader-judge.yml), so a quiet ten minutes costs a minute of a
-- runner on a public repository, which is free.
--
-- The same token also brings back the instant trigger
-- (reader-judge-trigger.sql), dead since the repository moved to
-- Ancient-Trees-Org on 11-25: both read the vault secret below.
--
-- Nothing about any reader leaves Supabase: the call carries only "main" and
-- "poll=yes".
--
-- Revert: select cron.unschedule('reader-judge-clock');

-- 1. The token (a fine-grained token, owner Ancient-Trees-Org, repository
--    ancienttrees, Actions and Contents read and write). Replace the text
--    between the quotes on the next line with it.
do $$
declare tok text := 'PASTE_THE_TOKEN_HERE';
begin
  if tok = 'PASTE_THE_TOKEN_HERE' then
    raise exception 'Put the GitHub token on the line above first';
  end if;
  if exists (select 1 from vault.secrets where name = 'github_dispatch_token') then
    perform vault.update_secret((select id from vault.secrets where name = 'github_dispatch_token'), tok);
  else
    perform vault.create_secret(tok, 'github_dispatch_token');
  end if;
end $$;

-- 2. The knock.
create extension if not exists pg_net with schema extensions;
create extension if not exists pg_cron;

create or replace function public.knock_reader_judge()
returns void
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
    return;
  end if;
  perform net.http_post(
    url := 'https://api.github.com/repos/Ancient-Trees-Org/ancienttrees/actions/workflows/reader-judge.yml/dispatches',
    body := jsonb_build_object('ref', 'main', 'inputs', jsonb_build_object('poll', 'yes')),
    headers := jsonb_build_object(
      'Authorization', 'Bearer ' || tok,
      'Accept', 'application/vnd.github+json',
      'X-GitHub-Api-Version', '2022-11-28',
      'User-Agent', 'ancienttrees-reader-judge',
      'Content-Type', 'application/json'
    )
  );
end;
$$;

revoke all on function public.knock_reader_judge() from public, anon, authenticated;

-- 3. Every ten minutes.
select cron.unschedule(jobid) from cron.job where jobname = 'reader-judge-clock';
select cron.schedule('reader-judge-clock', '*/10 * * * *', $$ select public.knock_reader_judge() $$);

-- 4. Did GitHub accept the last knocks? 204 is yes; 401 or 403 is a token
--    that cannot start workflows on this repository.
-- select status_code, created from net._http_response order by created desc limit 5;
