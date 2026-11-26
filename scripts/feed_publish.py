#!/usr/bin/env python3
"""Write what readers put live into the server's feed, so the feed never
waits on a deploy (Hidde, 2026-11-26: "hoe gaan we zorgen dat die feed niet
elke keer afhankelijk is van zon lange deploy"; supabase/feed.sql).

Reads the city files as committed, which hold only what the judge put live:
* a tree a reader found (`found_by_reader`) is a `tree` row, with its lead
  photograph;
* every other photograph a reader sent (`source: contributor` with a
  `sighting_id`) on one of our trees is a `photo` row;
* a photograph that went into a strip before the judge saw it
  (`live_first_on`, 2026-10-24) only once judged (data/sightings-processed.json
  names its outcome), so the feed shows nothing the judge has not looked at;
* never our own accounts (data/our-accounts.json).

Each row carries the tree's name, place, pin and page, and a copy of the
picture (800 px wide) in the public `feed` bucket, so a tile needs nothing
from the build. A row whose photograph or tree is gone from the data (a
report, a retire, an unstrip, a deleted account's unlink) is set hidden.
Idempotent; uploads only what the table does not have yet.

    python3 scripts/feed_publish.py --dry     what it would write
    python3 scripts/feed_publish.py           write (needs SUPABASE_SERVICE_KEY)

Run by reader-judge.yml right after the judge's commit, and by the knock.
"""
import argparse
import datetime
import glob
import io
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import findable  # noqa: E402
import people  # noqa: E402
from sightings_publish import page_slug  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUPA = "https://caimvxiyrtifilimlkqw.supabase.co"
BUCKET = "feed"
WIDTH = 800
UUID = __import__("re").compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
JUDGED = ("published", "added", "approve", "add", "lead")


def ours():
    try:
        doc = json.load(open(os.path.join(ROOT, "data", "our-accounts.json"), encoding="utf-8"))
    except (OSError, ValueError):
        return set()
    return {a.get("ref") for a in doc.get("accounts") or [] if a.get("ref")}


def judged():
    """{sighting_id: date} for every sighting a verdict put live."""
    try:
        doc = json.load(open(os.path.join(ROOT, "data", "sightings-processed.json"), encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    done = doc.get("done") if isinstance(doc.get("done"), dict) else {}
    return {sid: (v.get("date") or "") for sid, v in done.items()
            if isinstance(v, dict) and v.get("outcome") in JUDGED}


def note_day(photo):
    """The latest date our own note on the photograph names (sent, looked
    at, approved), for a row nothing else dates. Server-side, a trigger
    (supabase/feed-sent-time.sql) puts the real sent time on any row with a
    sighting, so this only orders tips and old rows."""
    days = __import__("re").findall(r"20\d\d-\d\d-\d\d", photo.get("note") or "")
    return max(days) if days else None


def at_noon(day):
    try:
        datetime.date.fromisoformat(day)
    except (TypeError, ValueError):
        return None
    return day + "T12:00:00+00:00"


def local_file(url):
    name = (url or "").rsplit("/", 1)[-1]
    path = os.path.join(ROOT, "site", "public", "photos", name)
    return path if name and os.path.exists(path) else None


def tree_url(city_slug, t):
    if findable.app_only(t):
        return f"/{city_slug}#tree={t['id']}"
    return f"/{city_slug}/{page_slug(t.get('name') or '')}"


def cities():
    for path in sorted(glob.glob(os.path.join(ROOT, "data", "cities", "*.json"))):
        try:
            yield os.path.basename(path)[:-5], json.load(open(path, encoding="utf-8"))
        except ValueError:
            continue


def collect(places=None, mine=None, ok=None):
    """{key: row} for everything that belongs in the feed today."""
    mine = ours() if mine is None else mine
    ok = judged() if ok is None else ok
    rows = {}
    for slug, city in (cities() if places is None else places):
        place = city.get("city") or ""
        for t in city.get("trees") or []:
            if not t.get("id"):
                continue
            loc = t.get("location") or {}
            base = {"tree_id": t["id"], "tree_name": t.get("name") or "", "place": place,
                    "url": tree_url(slug, t), "latitude": loc.get("latitude"),
                    "longitude": loc.get("longitude")}
            fbr = t.get("found_by_reader") or {}
            pics = [p for p in [t.get("photo") or {}] + list(t.get("photos") or []) if p.get("url")]
            if fbr:
                sid = fbr.get("sighting_id")
                lead = next((p for p in pics if sid and p.get("sighting_id") == sid), None) \
                    or next((p for p in pics if p.get("source") == "contributor"), None)
                if lead and lead.get("contributor_user_id") not in mine:
                    key = sid or f"tree:{t['id']}"
                    rows[key] = dict(base, key=key, kind="tree", sighting_id=sid,
                                     _photo=lead, _day=fbr.get("date") or ok.get(sid)
                                     or lead.get("live_first_on") or note_day(lead))
            for p in pics:
                sid = p.get("sighting_id")
                if p.get("source") != "contributor" or not sid or sid in rows:
                    continue
                # One post per send, as Strava shows one activity with all its
                # photos: a second frame ("<uuid>-extra-1") is not a post.
                if "-extra-" in sid:
                    continue
                if p.get("contributor_user_id") in mine or p.get("unlinked"):
                    continue
                if p.get("live_first_on") and sid not in ok:
                    continue
                rows[sid] = dict(base, key=sid, kind="photo", sighting_id=sid, _photo=p,
                                 _day=ok.get(sid) or p.get("live_first_on") or note_day(p))
    return rows


def _req(path, key, method="GET", body=None, headers=None, raw=None):
    h = {"apikey": key, "Authorization": "Bearer " + key}
    if body is not None:
        h["Content-Type"] = "application/json"
        raw = json.dumps(body).encode()
    h.update(headers or {})
    req = urllib.request.Request(SUPA + path, method=method, headers=h, data=raw)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    return json.loads(data) if data else None


def existing(key):
    out, start = {}, 0
    while True:
        page = _req(f"/rest/v1/feed?select=key,photo_url,hidden,published_at&order=key&offset={start}&limit=1000", key)
        for r in page or []:
            out[r["key"]] = r
        if not page or len(page) < 1000:
            return out
        start += 1000


def small_jpeg(path):
    from PIL import Image
    im = Image.open(path)
    im = im.convert("RGB")
    if im.width > WIDTH:
        im = im.resize((WIDTH, round(im.height * WIDTH / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=82, optimize=True)
    return buf.getvalue(), im.width, im.height


def upload(key, name, data):
    _req(f"/storage/v1/object/{BUCKET}/{urllib.parse.quote(name)}", key, method="POST", raw=data,
         headers={"Content-Type": "image/jpeg", "x-upsert": "true",
                  "Cache-Control": "max-age=31536000"})
    return f"{SUPA}/storage/v1/object/public/{BUCKET}/{urllib.parse.quote(name)}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    rows = collect()
    kinds = {}
    for r in rows.values():
        kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
    print(f"feed: {len(rows)} rows belong ({kinds})")
    key = people.service_key()
    if args.dry or not key:
        if not key:
            print("no SUPABASE_SERVICE_KEY: nothing written")
        return 0
    try:
        have = existing(key)
    except urllib.error.HTTPError as e:
        print(f"feed table unreadable ({e.code}); is supabase/feed.sql pasted? nothing written")
        return 0
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    new, failed = [], 0
    for k, r in rows.items():
        old = have.get(k)
        if old and old.get("photo_url") and not old.get("hidden"):
            # A row stamped today for want of a day (the first fill,
            # 2026-11-26) takes its own day once one is known.
            day = r.get("_day")
            if day and day < now[:10] and (old.get("published_at") or "")[:10] == now[:10] \
                    and not r.get("sighting_id"):
                _req(f"/rest/v1/feed?key=eq.{urllib.parse.quote(k)}", key, method="PATCH",
                     body={"published_at": at_noon(day)}, headers={"Prefer": "return=minimal"})
            continue
        src = local_file(r["_photo"].get("url"))
        if not src:
            failed += 1
            continue
        try:
            data, w, h = small_jpeg(src)
            url = upload(key, f"{k.replace(':', '-')}.jpg", data)
        except Exception as e:  # one bad file never stops the rest
            print(f"  could not upload {k}: {e}")
            failed += 1
            continue
        uid = people.uid(r["_photo"].get("contributor_user_id"))
        row = {c: r[c] for c in ("key", "kind", "tree_id", "sighting_id", "tree_name", "place",
                                 "url", "latitude", "longitude")}
        # A tip's id ("tip-908") is no sighting: the key keeps it, the uuid column not.
        if not UUID.match(str(row["sighting_id"] or "")):
            row["sighting_id"] = None
        row.update(photo_url=url, photo_w=w, photo_h=h, user_id=uid, hidden=False)
        # A backfilled row keeps the day it went live; a row new today is now.
        # Every row carries the same keys, or PostgREST refuses the batch.
        day = r.get("_day")
        row["published_at"] = (old or {}).get("published_at") or (
            now if (not day or day >= now[:10]) else at_noon(day) or now)
        new.append(row)
    for i in range(0, len(new), 200):
        try:
            _req("/rest/v1/feed?on_conflict=key", key, method="POST", body=new[i:i + 200],
                 headers={"Prefer": "resolution=merge-duplicates,return=minimal"})
        except urllib.error.HTTPError as e:
            print(f"feed: batch {i // 200} refused ({e.code}): {e.read()[:300]!r}")
            return 1
    gone = [k for k, r in have.items() if k not in rows and not r.get("hidden")]
    for k in gone:
        _req(f"/rest/v1/feed?key=eq.{urllib.parse.quote(k)}", key, method="PATCH",
             body={"hidden": True}, headers={"Prefer": "return=minimal"})
    print(f"feed: {len(new)} written, {len(gone)} hidden, {failed} without a picture")
    return 0


if __name__ == "__main__":
    sys.exit(main())
