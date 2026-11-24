"""Copy the files in the Supabase storage buckets to a local folder, for the
weekly database backup (.github/workflows/db-backup.yml).

Hidde, 2026-11-04: the free Supabase plan keeps no backup we can restore, and
accounts, saves, readers' photos and notes live only there ("ok lets do option
1"). The database itself is dumped with pg_dump; this is the other half, the
files: avatars and readers' photographs.

    python3 scripts/backup_storage.py <out-dir>                  every file
    python3 scripts/backup_storage.py <out-dir> --since <date>   only files
                                                                 changed since

ONLY WHAT IS NEW, MOST WEEKS (Hidde, 2026-11-13: "fix maar", after Supabase
mailed that the org passed the free plan's 5 GB of egress). Downloading every
file every week cost about 150 MB a week, a fifth of the month's allowance on
its own. So the workflow takes every file once in 28 days and, in the weeks
between, only the files created or replaced since the last backup (with two
days of overlap). Restore: the newest full backup, then each `-new` after it.
Listing a bucket costs a few kilobytes; only downloads count.

Needs SUPABASE_SERVICE_KEY. Prints counts only, never a path or a name.
"""
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
import urllib.parse
import urllib.request

URL = "https://caimvxiyrtifilimlkqw.supabase.co"
BUCKETS = ["avatars", "sightings"]
KEY = os.environ.get("SUPABASE_SERVICE_KEY", "")
# The first full copy (2026-11-24) ran one file at a time and hit the job's
# 40 minutes before it was done. Several at once, and one file that will not
# come is counted and left out instead of losing the whole backup.
WORKERS = 8


def req(path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(URL + path, data=data, method="POST" if data else "GET",
                               headers={"apikey": KEY, "Authorization": "Bearer " + KEY,
                                        "Content-Type": "application/json"})
    with urllib.request.urlopen(r, timeout=60) as resp:
        return resp.read()


def walk(bucket, prefix=""):
    """Every object (path, last change) under prefix. A folder has id null."""
    offset = 0
    while True:
        rows = json.loads(req(f"/storage/v1/object/list/{bucket}",
                              {"prefix": prefix, "limit": 1000, "offset": offset,
                               "sortBy": {"column": "name", "order": "asc"}}))
        for r in rows:
            path = (prefix + "/" + r["name"]).lstrip("/")
            if r.get("id") is None:
                yield from walk(bucket, path)
            else:
                yield path, (r.get("updated_at") or r.get("created_at") or "")
        if len(rows) < 1000:
            return
        offset += 1000


def fetch(b, path, out):
    dst = os.path.join(out, b, path)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    quoted = urllib.parse.quote(path)
    for attempt in range(3):
        try:
            data = req(f"/storage/v1/object/authenticated/{b}/{quoted}")
            break
        except Exception:
            if attempt == 2:
                return None
            time.sleep(2 * (attempt + 1))
    with open(dst, "wb") as fh:
        fh.write(data)
    return len(data)


def main(out, since=""):
    if not KEY:
        sys.exit("backup_storage: no SUPABASE_SERVICE_KEY")
    total = skipped = size = failed = 0
    for b in BUCKETS:
        todo = []
        for path, changed in walk(b):
            # ISO timestamps compare as text. A file without a date is taken.
            if since and changed and changed[:10] < since:
                skipped += 1
                continue
            todo.append(path)
        n = 0
        with ThreadPoolExecutor(WORKERS) as pool:
            for got in pool.map(lambda p: fetch(b, p, out), todo):
                if got is None:
                    failed += 1
                else:
                    size += got
                    n += 1
        print(f"backup_storage: {b}: {n} file(s)", flush=True)
        total += n
    print(f"backup_storage: {total} file(s) in all, {size / 1e6:.1f} MB downloaded"
          + (f"; {skipped} unchanged since {since} left out" if since else ""))
    if failed:
        print(f"::warning::backup_storage: {failed} file(s) could not be fetched")


if __name__ == "__main__":
    args = sys.argv[1:]
    since = ""
    if "--since" in args:
        i = args.index("--since")
        since = args[i + 1]
        del args[i:i + 2]
    main(args[0] if args else "backup-storage", since)
