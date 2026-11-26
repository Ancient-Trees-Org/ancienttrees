#!/usr/bin/env python3
"""Every photograph a reader sends with a tree reaches the page, or says why not.

A reader can send a tree with up to four photographs: the main one and three
further ones (`extra_photos` on the sightings and submissions rows). Until
2026-11-26 only the main one was published by any script: the further ones
were fetched as evidence (sightings_inbox.fetch_extras) and reached the page
only when the run that judged the tree happened to copy them by hand. On that
day 84 of the readers' trees that had gone live with more than one photograph
showed fewer than were sent, most of them one, and nobody was told (feedback
from a tester: "I uploaded a tree with three photos, the approved version
shows only one"; Hidde, 2026-11-26: "Yes, build it").

So now each further photograph of a published reader's tree gets a verdict of
its own, recorded in data/reader-extras.json:

  published     in the tree's gallery behind the lead (live first, like any
                reader photograph in the strip: CLAUDE.md "Live first, then
                checked"); its sighting_id is "<sighting id>-extra-<n>", the
                shape sightings_link.py and the site already read
  already_live  a run had put it on the page by hand before this existed
  left_out      with one reason from the closed list LEAVE_REASONS, which the
                congratulation mail (tree_approved.py) tells the reader

    python3 scripts/reader_extras.py --status            what waits, per tree
    python3 scripts/reader_extras.py --sheet DIR         contact sheets of what waits, to LOOK at
    python3 scripts/reader_extras.py --leave SID N REASON "what it shows"
    python3 scripts/reader_extras.py --apply [--only SID] publish everything that waits
    python3 scripts/reader_extras.py --check             exit 1 when a published tree's extra has no verdict

Look before --apply (CLAUDE.md "never judged blind"): --sheet, then --leave
for a photo that shows no tree, a duplicate, a recognisable person who did not
ask to be shown, or a screenshot (BRIEF_READER_JUDGE.md "A screenshot waits
for its maker's yes"). Everything else goes up: a weaker frame than the lead
is never a reason (Hidde, 2026-11-06: "we should embrace all user generated
content").

Needs SUPABASE_SERVICE_KEY (or ~/.ancienttrees-supabase.env) for files not
already in out/sightings/ and for the rows' further photographs; --check and
--leave need neither.
"""
import datetime
import glob
import json
import os
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

LEDGER = os.path.join(ROOT, "data", "reader-extras.json")
LEADS = os.path.join(ROOT, "data", "leads", "_sightings.json")
PROCESSED = os.path.join(ROOT, "data", "sightings-processed.json")
OUT = os.path.join(ROOT, "out", "sightings")
ENV_FILE = os.path.expanduser("~/.ancienttrees-supabase.env")

# What keeps a further photograph off the page, and the words the reader is
# told (tree_approved.py). Nothing else is a reason: not a weaker frame, not
# "the lead says enough".
LEAVE_REASONS = {
    "duplicate": "it was the same picture as another one you sent",
    "no_tree": "we could not see the tree in it",
    "other_tree": "it shows a different tree, so we kept it apart",
    "person": "a person can be recognised in it",
    "screenshot": "it looks like a screenshot, and we can only show a photo once its maker says yes",
    "not_theirs": "it looks like someone else's picture (a print or a board), and we can only show a photo once its maker says yes",
    "withheld":"you asked us not to show your photographs",
    "unreadable": "the file would not open on our side",
}


def _key():
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    if key or not os.path.exists(ENV_FILE):
        return key
    for line in open(ENV_FILE):
        line = line.strip()
        if line.startswith("export "):
            line = line[7:]
        if line.startswith("SUPABASE_SERVICE_KEY="):
            val = line.split("=", 1)[1].strip().strip('"').strip("'")
            return val if val and "PLAK" not in val else None
    return None


def load(path, default):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return default


def save_ledger(doc):
    with open(LEDGER, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False, sort_keys=True)
        fh.write("\n")


def ledger():
    return load(LEDGER, {"_note": "One verdict per further photograph of a reader's tree "
                         "(scripts/reader_extras.py). Keys are sighting ids, then the photo's "
                         "number (1 to 3).", "sightings": {}})


def published_trees():
    """{sighting id: (city_slug, tree_id, user code)} for every reader photograph
    that went live as a tree's main photograph or a new tree."""
    out = {}
    for l in load(LEADS, {"leads": []}).get("leads", []):
        pa = l.get("published_as") or ""
        if l.get("status") == "published" and "/" in pa:
            city, tid = pa.split("/", 1)
            out[l["sighting_id"]] = (city, tid, l.get("user_id"))
    for sid, d in load(PROCESSED, {"done": {}}).get("done", {}).items():
        if d.get("outcome") in ("published", "added") and d.get("city_slug") and d.get("tree_id"):
            out.setdefault(sid, (d["city_slug"], d["tree_id"], None))
    return out


def local_extras(sid):
    """{n: path} of the further photographs already on this Mac."""
    found = {}
    for p in glob.glob(os.path.join(OUT, f"{sid}-extra-*.jpg")):
        try:
            found[int(p.rsplit("-", 1)[-1].split(".")[0])] = p
        except ValueError:
            pass
    return found


def lead_extras():
    """{sighting id: [repo paths]} the judge's leads carry."""
    return {l["sighting_id"]: l.get("extra_files") or []
            for l in load(LEADS, {"leads": []}).get("leads", []) if l.get("extra_files")}


def server_rows(sids):
    """{sighting id: {"paths": [...], "months": [...], "user": uid}} from Supabase."""
    key = _key()
    if not key:
        return None
    os.environ["SUPABASE_SERVICE_KEY"] = key
    import sightings_inbox as si  # noqa: E402  reads the key at import
    si.KEY = key
    rows = {}
    uu = [s for s in sids if not s.startswith("tip-")]
    tips = [s[4:] for s in sids if s.startswith("tip-")]
    for i in range(0, len(uu), 60):
        q = ("/rest/v1/sightings?select=id,user_id,photo,extra_photos,extra_photo_months&id=in.(%s)"
             % ",".join(uu[i:i + 60]))
        for r in _get(si, q):
            ex = [p for p in (r.get("extra_photos") or []) if p]
            months = list(r.get("extra_photo_months") or [])
            if not r.get("photo") and ex:  # promote_extra_photo's shape
                ex, months = ex[1:], months[1:]
            rows[r["id"]] = {"paths": ex[:3], "months": months[:3], "user": r.get("user_id")}
    for i in range(0, len(tips), 60):
        q = ("/rest/v1/submissions?select=id,user_id,extra_photos,extra_photo_months&id=in.(%s)"
             % ",".join(tips[i:i + 60]))
        for r in _get(si, q):
            ex = [p for p in (r.get("extra_photos") or []) if p]
            rows["tip-%s" % r["id"]] = {"paths": ex[:3], "months": list(r.get("extra_photo_months") or [])[:3],
                                        "user": r.get("user_id")}
    return rows


def _get(si, q):
    import urllib.request
    req = urllib.request.Request(si.SUPA + q, headers={"apikey": si.KEY, "Authorization": "Bearer " + si.KEY})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def ahash(path):
    """A 64-bit average hash, to tell whether a further photograph is already
    on the page under a name a run gave it by hand."""
    from PIL import Image, ImageOps
    im = ImageOps.exif_transpose(Image.open(path)).convert("L").resize((8, 8))
    px = list(im.getdata())
    avg = sum(px) / 64.0
    return sum(1 << i for i, v in enumerate(px) if v >= avg)


def tree_of(city, tid):
    path = os.path.join(ROOT, "data", "cities", f"{city}.json")
    doc = load(path, None)
    if not doc:
        return path, None, None
    for t in doc.get("trees", []):
        if t.get("id") == tid:
            return path, doc, t
    return path, doc, None


def on_page_files(t):
    import sightings_publish as sp
    files = []
    for b in [t.get("photo") or {}] + list(t.get("photos") or []):
        f = sp._local_file((b or {}).get("url"))
        if f:
            files.append(f)
    return files


def waiting(led, trees, rows=None, fetch=False):
    """[(sid, n, path or None, month, city, tid, user)] with no verdict yet."""
    out = []
    by_lead = lead_extras()
    for sid, (city, tid, user) in sorted(trees.items()):
        known = led["sightings"].get(sid, {}).get("extras", {})
        have = local_extras(sid)
        n_total = len(by_lead.get(sid, []))
        months = []
        server = (rows or {}).get(sid)
        if server:
            n_total = max(n_total, len(server["paths"]))
            months = server["months"]
            user = user or server["user"]
        n_total = max(n_total, max(have) if have else 0)
        for n in range(1, n_total + 1):
            if str(n) in known:
                continue
            path = have.get(n)
            if not path and fetch and server and n <= len(server["paths"]):
                import sightings_inbox as si
                dest = os.path.join(OUT, f"{sid}-extra-{n}.jpg")
                if si.fetch_photo(server["paths"][n - 1], dest):
                    path = dest
            month = months[n - 1] if n - 1 < len(months) else None
            out.append((sid, n, path, month, city, tid, user))
    return out


def record(led, sid, city, tid, n, verdict, **kw):
    s = led["sightings"].setdefault(sid, {"tree": f"{city}/{tid}", "extras": {}})
    s["tree"] = f"{city}/{tid}"
    s["extras"][str(n)] = dict({"verdict": verdict, "date": datetime.date.today().isoformat()}, **kw)


def publish_one(led, sid, n, path, month, city, tid, user, today, dry=False):
    """Write the file and append it to the tree's gallery. Returns a word."""
    import sightings_publish as sp
    import people
    path_city, doc, t = tree_of(city, tid)
    if t is None:
        return "no_tree_file"
    # Only beside a photograph of theirs that is still on the page: a main
    # photo taken down (a face, a hold, a takedown) takes its further ones too.
    own = [b for b in [t.get("photo") or {}] + list(t.get("photos") or [])
           if str((b or {}).get("sighting_id") or "").lower().startswith(sid.lower())]
    if not own and (t.get("found_by_reader") or {}).get("sighting_id") != sid:
        record(led, sid, city, tid, n, "skipped", why="their main photograph is not on the page")
        return "main_off_page"
    if user and sp.withheld({"user_id": user}):
        record(led, sid, city, tid, n, "left_out", reason="withheld")
        return "withheld"
    # Already on the page under a hand-given name?
    try:
        mine = ahash(path)
        for f in on_page_files(t):
            if bin(mine ^ ahash(f)).count("1") <= 6:
                record(led, sid, city, tid, n, "already_live", file=os.path.basename(f))
                return "already_live"
    except Exception as e:  # noqa: BLE001
        record(led, sid, city, tid, n, "left_out", reason="unreadable", what=str(e)[:80])
        return "unreadable"
    if dry:
        return "would_publish"
    fname = f"{tid}-{sp.slugify(t.get('name') or '')}-{sid[:8]}-x{n}.jpg"
    try:
        w, h = sp.write_image(path, os.path.join(sp.PHOTOS, fname))
    except Exception as e:  # noqa: BLE001
        record(led, sid, city, tid, n, "left_out", reason="unreadable", what=str(e)[:80])
        return "unreadable"
    lead = t.get("photo") or {}
    owner = user or lead.get("contributor_user_id")
    if not owner:
        os.remove(os.path.join(sp.PHOTOS, fname))
        return "no_owner"
    block = {
        "url": f"{sp.BASE_URL}/photos/{fname}",
        "license": "Provided by a reader through the Ancient Trees app, all rights reserved",
        "attribution": None,
        "status": "approved",
        "width": w,
        "height": h,
        **({"taken_month": int(month), "taken_month_basis": "the photograph's own date, kept by the app"}
           if isinstance(month, int) or (isinstance(month, str) and month.isdigit()) else {}),
        "source": "contributor",
        "contributor_user_id": owner if people.is_ref(owner) else people.ref(owner),
        "sighting_id": f"{sid}-extra-{n}",
        "note": (f"The same reader's further photograph {n}, sent with the tree and put in its "
                 f"gallery on {today} (scripts/reader_extras.py). Not an open licence: ask before "
                 f"reuse elsewhere."),
    }
    twin = sp.same_picture(block, [lead] + list(t.get("photos") or []))
    if twin:
        sp.drop_vendored(block["url"])
        record(led, sid, city, tid, n, "left_out", reason="duplicate", what=twin.rsplit("/", 1)[-1])
        return "duplicate"
    t.setdefault("photos", []).append(block)
    sp.save(path_city, doc, indent=2)
    record(led, sid, city, tid, n, "published", file=fname)
    return "published"


def contact_sheets(items, outdir):
    from PIL import Image, ImageDraw, ImageOps
    os.makedirs(outdir, exist_ok=True)
    per, cell = 12, 300
    made = []
    for i in range(0, len(items), per):
        chunk = items[i:i + per]
        sheet = Image.new("RGB", (cell * 4, (cell + 22) * 3), "white")
        d = ImageDraw.Draw(sheet)
        for j, (sid, n, path, _m, city, tid, _u) in enumerate(chunk):
            x, y = (j % 4) * cell, (j // 4) * (cell + 22)
            if path:
                im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
                im.thumbnail((cell - 6, cell - 6))
                sheet.paste(im, (x + 3, y + 3))
            d.text((x + 4, y + cell + 4), f"{i + j + 1} {tid} {sid[:8]} x{n}", fill="black")
        p = os.path.join(outdir, f"extras-{i // per + 1:02d}.jpg")
        sheet.save(p, "JPEG", quality=80)
        made.append(p)
    return made


def check(led=None):
    """Published trees whose judge's lead carries further photographs without a
    verdict. Offline: reads the leads' extra_files, which every reader's tree
    since 2026-09-26 carries."""
    led = led or ledger()
    trees = published_trees()
    missing = []
    counts = {sid: len(files) for sid, files in lead_extras().items()}
    for sid, d in load(PROCESSED, {"done": {}}).get("done", {}).items():
        if d.get("extras"):
            counts[sid] = max(counts.get(sid, 0), d["extras"])
    for sid, total in counts.items():
        if sid not in trees:
            continue
        known = led["sightings"].get(sid, {}).get("extras", {})
        for n in range(1, total + 1):
            if str(n) not in known:
                missing.append((sid, n, "%s/%s" % trees[sid][:2]))
    return missing


def main(argv):
    led = ledger()
    today = datetime.date.today().isoformat()
    if "--check" in argv:
        miss = check(led)
        for sid, n, tree in miss:
            print(f"  {tree}: further photo {n} of {sid[:8]} has no verdict")
        print(f"reader_extras: {len(miss)} further photograph(s) of published readers' trees without a verdict")
        return 1 if miss else 0
    if "--leave" in argv:
        i = argv.index("--leave")
        sid, n, reason = argv[i + 1], int(argv[i + 2]), argv[i + 3]
        what = argv[i + 4] if len(argv) > i + 4 else ""
        if reason not in LEAVE_REASONS:
            print(f"reader_extras: reason must be one of {', '.join(LEAVE_REASONS)}")
            return 2
        trees = published_trees()
        hit = next((k for k in trees if k == sid or k.startswith(sid)), None)
        if not hit:
            print(f"reader_extras: {sid} is not a published reader's tree")
            return 2
        city, tid, _ = trees[hit]
        record(led, hit, city, tid, n, "left_out", reason=reason, what=what[:200])
        save_ledger(led)
        print(f"reader_extras: {tid} further photo {n} left out ({reason})")
        return 0
    trees = published_trees()
    if "--only" in argv:
        want = argv[argv.index("--only") + 1]
        trees = {k: v for k, v in trees.items() if k == want or k.startswith(want)}
    fetch = "--apply" in argv or "--sheet" in argv
    rows = server_rows(list(trees)) if fetch else None
    if fetch and rows is None:
        print("reader_extras: SUPABASE_SERVICE_KEY absent, only files already on this Mac are used")
    items = waiting(led, trees, rows, fetch=fetch)
    if "--sheet" in argv:
        outdir = argv[argv.index("--sheet") + 1]
        have = [x for x in items if x[2] and publish_one(led, *x, today, dry=True) == "would_publish"]
        save_ledger(led)
        for p in contact_sheets(have, outdir):
            print(p)
        print(f"reader_extras: {len(have)} further photograph(s) on {len(have) and (len(have) - 1) // 12 + 1} sheet(s); "
              f"{len(items) - len(have)} could not be fetched")
        return 0
    if "--apply" in argv:
        counts = {}
        for sid, n, path, month, city, tid, user in items:
            if not path and rows is not None and (sid not in rows or n > len(rows[sid]["paths"])):
                # The reader deleted it, or the sighting with their account.
                record(led, sid, city, tid, n, "skipped", why="no longer on the server")
                counts["gone"] = counts.get("gone", 0) + 1
                continue
            if not path:
                counts["not_fetched"] = counts.get("not_fetched", 0) + 1
                continue
            word = publish_one(led, sid, n, path, month, city, tid, user, today)
            counts[word] = counts.get(word, 0) + 1
            print(f"  {word:13} {city}/{tid} {sid[:8]} x{n}")
        save_ledger(led)
        print("reader_extras: " + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())) if counts
              else "reader_extras: nothing waits")
        return 0
    for sid, n, path, _m, city, tid, _u in items:
        print(f"  {city}/{tid} {sid[:8]} x{n} {'on disk' if path else 'not fetched'}")
    print(f"reader_extras: {len(items)} further photograph(s) wait for a verdict")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
