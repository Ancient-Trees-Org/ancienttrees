-- Worth-it votes in a table of their own (Hidde, 2026-11-16: "kun je vanaf nu
-- nooit meer worth it stemmen en boominzendingen onder 1 kap gooien dit zijn
-- hele andere dingen", then "prima start maar").
--
-- Until now a thumb was a row in public.submissions, the inbox for trees,
-- reports and messages, and an undo was a second row saying "vote undone".
-- Every script that counted reader input had to guess which rows were taps.
-- Here a vote is what every app stores a like as: one row per person per
-- tree, changed in place, and taking it back deletes the row.
--
-- Paste this once into the Supabase SQL editor (dashboard > SQL) and run it.
-- Everything in it is idempotent; running it twice is safe.
--
-- Design notes:
-- * primary key (user_id, tree_id): one standing vote per person per tree.
-- * references auth.users on delete cascade: deleting the account deletes the
--   votes, so account deletion stays end to end (hard list 1).
-- * RLS: a person reads, writes and deletes only their own rows. Counts reach
--   everybody else through tree_vote_counts(), counts only, no user id.
-- * THE APPS ALREADY IN PEOPLE'S POCKETS keep posting votes to submissions.
--   The trigger at the bottom catches every vote-shaped row on its way in,
--   applies it here, and drops it from submissions, so old builds keep working
--   and submissions keeps only what a person writes to us.
-- * Old vote rows in submissions are copied (the standing vote per person per
--   tree) and left where they are: nothing is deleted (hard list 3).
-- * GRANT in the same file (Supabase stopped granting API access
--   automatically on 2026-10-30; CLAUDE.md, Privacy and accounts).

create table if not exists public.tree_votes (
  user_id    uuid not null default auth.uid() references auth.users (id) on delete cascade,
  tree_id    text not null check (char_length(tree_id) between 1 and 40),
  vote       text not null check (vote in ('up', 'down')),
  -- Where it was cast, for the digest's per-place reading; never shown.
  city       text,
  page       text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (user_id, tree_id)
);

create index if not exists tree_votes_tree_id on public.tree_votes (tree_id);
create index if not exists tree_votes_created_at on public.tree_votes (created_at);

alter table public.tree_votes enable row level security;

drop policy if exists "own votes select" on public.tree_votes;
create policy "own votes select" on public.tree_votes
  for select using (auth.uid() = user_id);

drop policy if exists "own votes insert" on public.tree_votes;
create policy "own votes insert" on public.tree_votes
  for insert with check (auth.uid() = user_id);

drop policy if exists "own votes update" on public.tree_votes;
create policy "own votes update" on public.tree_votes
  for update using (auth.uid() = user_id) with check (auth.uid() = user_id);

drop policy if exists "own votes delete" on public.tree_votes;
create policy "own votes delete" on public.tree_votes
  for delete using (auth.uid() = user_id);

grant select, insert, update, delete on public.tree_votes to authenticated;
grant select on public.tree_votes to service_role;

-- The standing votes that already sit in submissions: the last word per
-- person per tree, and an undo as the last word means no vote. The tree
-- column is "<id>" on the old website and "<id> (<name>)" everywhere else;
-- the id is everything up to the first space.
insert into public.tree_votes (user_id, tree_id, vote, city, page, created_at, updated_at)
select user_id, tree_id,
       case when why = 'worth it' then 'up' else 'down' end,
       city, page, created_at, created_at
from (
  select distinct on (split_part(tree, ' ', 1), user_id)
         split_part(tree, ' ', 1) as tree_id, user_id,
         lower(trim(why)) as why, city, page, created_at
  from public.submissions
  where kind = 'feedback'
    and user_id is not null
    and (lower(trim(why)) in ('worth it', 'not worth it') or lower(trim(why)) like 'vote undone%')
  order by split_part(tree, ' ', 1), user_id, created_at desc
) last_word
where why in ('worth it', 'not worth it')
  and tree_id <> ''
  -- A deleted account's old rows keep its id in submissions, but the account
  -- is gone from auth.users, so its votes have nothing to belong to and are
  -- left behind (the first paste on 2026-11-16 stopped on exactly that).
  and exists (select 1 from auth.users u where u.id = last_word.user_id)
on conflict (user_id, tree_id) do nothing;

-- Counts for every tree, from the votes table now. Same name and shape as
-- vote-counts.sql, so the website and both apps keep calling it unchanged.
create or replace function public.tree_vote_counts()
returns table (tree_id text, up bigint, down bigint)
language sql
security definer
set search_path = public
stable
as $$
  select tree_id,
         count(*) filter (where vote = 'up')::bigint   as up,
         count(*) filter (where vote = 'down')::bigint as down
  from public.tree_votes
  group by tree_id
$$;

revoke all on function public.tree_vote_counts() from public;
grant execute on function public.tree_vote_counts() to anon, authenticated;

-- Catch a vote posted to submissions (every build out there today does this)
-- and apply it to tree_votes instead. Returning null drops the submissions
-- row; PostgREST still answers 201, so the sender sees success. A vote with
-- no account is dropped, as tree_vote_counts always ignored those.
create or replace function public.submission_vote_to_tree_votes()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
declare
  w   text := lower(trim(coalesce(new.why, '')));
  t   text := split_part(coalesce(new.tree, ''), ' ', 1);
  uid uuid := coalesce(new.user_id, auth.uid());
begin
  if coalesce(new.kind, '') <> 'feedback'
     or not (w in ('worth it', 'not worth it') or w like 'vote undone%') then
    return new;
  end if;
  if uid is null or t = '' then
    return null;
  end if;
  if w like 'vote undone%' then
    delete from public.tree_votes where user_id = uid and tree_id = t;
  else
    insert into public.tree_votes (user_id, tree_id, vote, city, page)
    values (uid, t, case when w = 'worth it' then 'up' else 'down' end, new.city, new.page)
    on conflict (user_id, tree_id)
    do update set vote = excluded.vote, city = excluded.city, page = excluded.page,
                  updated_at = now();
  end if;
  return null;
end
$$;

drop trigger if exists submissions_votes_to_tree_votes on public.submissions;
create trigger submissions_votes_to_tree_votes
  before insert on public.submissions
  for each row execute function public.submission_vote_to_tree_votes();
