-- WHEN EACH PHOTOGRAPH ON A TREE PAGE WAS SENT (Hidde, 2026-11-20: "aangeven
-- hoelaat iets is gepost"; "A, met boomnaam"; CONVENTIONS.md "A heart for a
-- visitor's photograph ... who and when on it").
--
-- photo_authors() (reader-names.sql) as it was, plus published_at: the same
-- clock as the feed (visitor-photos.sql), the photograph's own upload in the
-- sightings bucket, the camera's time only where the file is gone; for a
-- photograph sent through the website's form, the submission's created_at.
-- The website prints it after the name under the hero and in the opened
-- photograph ("2 hours ago"). The apps read photo_authors too and ignore a
-- column they do not know (PhotoAuthors.swift Codable, PhotoAuthors.kt optString).
--
-- NOTHING NEW ABOUT A PERSON: no column, no table; a time already in the
-- database, returned only beside a public profile's name, as the feed already
-- returns it. The return type changes, so the function is dropped and made
-- again; the grant follows it.

drop function if exists public.photo_authors(text[]);

create function public.photo_authors(ids text[])
returns table (
  photo_id text,
  author_name text,
  author_avatar text,
  author_id uuid,
  published_at timestamptz
)
language sql
security definer
set search_path = public, extensions, storage
stable
as $$
  with sent as (
    select s.id::text as photo_id, s.user_id,
           coalesce(o.created_at, s.taken_at, s.updated_at) as at
    from public.sightings s
    left join storage.objects o on o.bucket_id = 'sightings' and o.name = s.photo
    where s.id::text = any(ids) and s.status = 'published'
    union all
    select 'tip-' || t.id::text, t.user_id, t.created_at
    from public.submissions t
    where ('tip-' || t.id::text) = any(ids) and t.user_id is not null and t.photo is not null
  )
  select distinct on (sent.photo_id) sent.photo_id,
         p.display_name,
         p.avatar_url,
         case when auth.uid() is not null then sent.user_id end,
         sent.at
  from sent
  join public.profiles p on p.user_id = sent.user_id and p.public
  where encode(digest(sent.user_id::text, 'sha1'), 'hex') <> all (array[
        'cc6a542385091392e455911c0d7e351bf0148a4b',
        'ef98f5dbe51e86e6236031d19bdce2364272c6b6',
        'd4e6c578be12fd0916a6277fa7bba4b482405484',
        'a9c1498c827881dd41e3e8cd39edc1a8fbf399f9'
      ])
  limit 60
$$;

revoke all on function public.photo_authors(text[]) from public;
grant execute on function public.photo_authors(text[]) to anon, authenticated;

notify pgrst, 'reload schema';
