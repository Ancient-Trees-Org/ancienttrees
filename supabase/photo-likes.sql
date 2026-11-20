-- A HEART FOR A VISITOR'S PHOTOGRAPH (Hidde, 2026-11-20: "dat gebruikers de
-- fotos kunnen hartje geven om elkaar aan te moedigen voor de foto zelf";
-- "Ja, bouw het hartje", his yes to this new table, hard list 1).
-- Convention: CONVENTIONS.md "A heart for a visitor's photograph, beside save
-- and Worth the visit": the heart thanks the photographer and sits on their
-- line, the bookmark saves the tree, the thumb says the tree is worth it.
-- Google Maps' "Helpful": the count is public, who gave it is not.
--
-- Paste once into the Supabase SQL editor and run it; idempotent.
--
-- * One row per account and photograph: primary key (user_id, photo_id),
--   photo_id being the id the feed carries for a visitor's photograph (a
--   sightings uuid, lowercase, or "tip-<n>" for one sent through the
--   website's form), the same id photo_authors() takes.
-- * references auth.users on delete cascade: a deleted account takes its
--   hearts with it (delete-user.sql deletes the auth.users row).
-- * RLS: a person sees, adds and removes only their own hearts. Nobody, not
--   the photographer either, can read who gave one.
-- * photo_like_counts(ids): the public number per photograph (from 1, a
--   photograph nobody liked is not in the result) and whether the caller
--   gave one. Counts only, no account, no date.

create table if not exists public.photo_likes (
  user_id    uuid not null default auth.uid() references auth.users (id) on delete cascade,
  photo_id   text not null check (char_length(photo_id) between 1 and 64),
  created_at timestamptz not null default now(),
  primary key (user_id, photo_id)
);

create index if not exists photo_likes_photo on public.photo_likes (photo_id);

alter table public.photo_likes enable row level security;

drop policy if exists "own photo likes select" on public.photo_likes;
create policy "own photo likes select" on public.photo_likes
  for select using (auth.uid() = user_id);

drop policy if exists "own photo likes insert" on public.photo_likes;
create policy "own photo likes insert" on public.photo_likes
  for insert with check (auth.uid() = user_id);

drop policy if exists "own photo likes delete" on public.photo_likes;
create policy "own photo likes delete" on public.photo_likes
  for delete using (auth.uid() = user_id);

-- A new table carries its own grant (Supabase stopped granting on 2026-10-30).
grant select, insert, delete on public.photo_likes to authenticated;
grant all on public.photo_likes to service_role;

create or replace function public.photo_like_counts(ids text[])
returns table (photo_id text, likes bigint, mine boolean)
language sql
security definer
set search_path = public
stable
as $$
  select l.photo_id,
         count(*)::bigint,
         coalesce(bool_or(l.user_id = auth.uid()), false)
  from public.photo_likes l
  where l.photo_id = any(ids)
  group by l.photo_id
$$;

revoke all on function public.photo_like_counts(text[]) from public;
grant execute on function public.photo_like_counts(text[]) to anon, authenticated;

notify pgrst, 'reload schema';
