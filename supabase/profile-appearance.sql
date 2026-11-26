-- Light, dark or the phone's setting, kept with the profile like units
-- (2026-11-26, a tester: "The night (dark) mode is very dark, and there's no
-- way to turn it off"). The apps read and write it on their own call, so
-- before this is pasted they simply follow the phone and nothing breaks.
-- profiles already has its grants and its own-row policies; a new column
-- inherits both.

alter table public.profiles
  add column if not exists appearance text
  check (appearance is null or appearance in ('system', 'light', 'dark'));
