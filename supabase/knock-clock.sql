-- FOR HIDDE TO PASTE in the Supabase SQL editor (2026-11-26). Safe to run twice.
--
-- THE KNOCK WATCHDOG ON SUPABASE'S CLOCK (2026-11-26). GitHub dropped
-- knock.yml's 20-minute cron from 01:44 UTC, so no night run came to fix the
-- red deploy of 03:38 (the California map walk) and readers' trees waited
-- five hours. Like judge-clock.sql, pg_cron asks GitHub for the run instead;
-- knock.yml's own guards still decide whether a night run starts. Uses the
-- same vault token. Carries nothing about anyone.
--
-- Revert: select cron.unschedule('knock-clock');

create or replace function public.knock_watchdog()
returns void language plpgsql security definer set search_path = public, extensions as $$
declare tok text;
begin
  select decrypted_secret into tok from vault.decrypted_secrets where name = 'github_dispatch_token' limit 1;
  if tok is null then return; end if;
  perform net.http_post(
    url := 'https://api.github.com/repos/Ancient-Trees-Org/ancienttrees/actions/workflows/knock.yml/dispatches',
    body := jsonb_build_object('ref', 'main'),
    headers := jsonb_build_object('Authorization', 'Bearer ' || tok, 'Accept', 'application/vnd.github+json',
      'X-GitHub-Api-Version', '2022-11-28', 'User-Agent', 'ancienttrees-knock', 'Content-Type', 'application/json'));
end; $$;
revoke all on function public.knock_watchdog() from public, anon, authenticated;
select cron.unschedule(jobid) from cron.job where jobname = 'knock-clock';
select cron.schedule('knock-clock', '7,27,47 * * * *', $$ select public.knock_watchdog() $$);
select public.knock_watchdog();
