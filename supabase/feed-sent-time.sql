-- FOR HIDDE TO PASTE in the Supabase SQL editor (2026-11-26). Safe to run twice.
--
-- A FEED POST KEEPS THE MOMENT IT WAS SENT (2026-11-26). The live part of
-- feed() (feed-live.sql) dates a post by when the reader sent the photograph
-- (its upload in storage, as new_from_visitors() does since 2026-11-18). When
-- the judge has looked, scripts/feed_publish.py writes the checked row; this
-- trigger gives that row the same sent time, so a post never jumps to the top
-- of the feed the moment it is approved, and the first fill's rows, stamped
-- with that morning's time, get theirs back. Nothing new is stored.

create or replace function public.feed_sent_time()
returns trigger language plpgsql security definer set search_path = public, storage as $$
declare sent timestamptz;
begin
  if new.sighting_id is not null then
    select coalesce(o.created_at, s.taken_at) into sent
      from public.sightings s
      left join storage.objects o on o.bucket_id = 'sightings' and o.name = s.photo
     where s.id = new.sighting_id
     limit 1;
    if sent is not null then
      new.published_at := sent;
    end if;
  end if;
  return new;
end; $$;

revoke all on function public.feed_sent_time() from public, anon, authenticated;

drop trigger if exists feed_sent_time on public.feed;
create trigger feed_sent_time before insert or update of sighting_id, published_at on public.feed
  for each row execute function public.feed_sent_time();

-- The rows already there.
update public.feed set sighting_id = sighting_id where sighting_id is not null;
