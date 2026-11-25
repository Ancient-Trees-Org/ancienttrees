#!/usr/bin/env python3
"""Tell a reader the day a bug they reported is fixed where they use it.

Hidde, 2026-11-25 ("Ja, bouw hem"), after reading the Settings feedback: a
reader who reported that something did not work heard nothing when we fixed
it, unless he answered by hand. The convention is Canny's and Linear's: the
person who asked hears when its status changes. One short standard mail, in
our words, never quoting theirs (their words stay his to answer, CLAUDE.md
"General feedback is Hidde's to read"), signed Ancient Trees.

WHICH READERS: a feedback row closed as a bug (`feedback.py --close <id> bug
<bug-id>`, data/feedback-ledger.json) whose BUG row in data/code-audit.json is
`fixed` with `fixed_in` and carries `reader_line`: what now works, in plain
words for a reader ("the country you pick in Edit profile now stays").
Without that line nothing is sent and the row is listed, because the bug's
own summary is written for us. `reader_line_nl` is used for a reader who
wrote in Dutch.

ONLY ONCE IT REACHES THEM: a fix merged on main is not yet on their phone.
  web (site/, supabase/, scripts/): the live site's commit (/build.txt)
    contains `fixed_in`;
  iPhone (ios/): the first build number raised after `fixed_in` is
    READY_FOR_SALE in data/store-builds.json (crashes.py keeps it), or a
    later one is;
  Android (android/): a versionCode raised after `fixed_in` exists (testers
    get each build from Play).

Once per feedback row, recorded in data/bug-fixed-mailed.json (row and bug
ids and the date, never an address). Our own accounts are never mailed. Every
mail passes mailcheck and the do-not-contact list (sightings_publish.send_mail);
the week's rest does not hold it, as it answers their own report.

    python3 scripts/bug_fixed_mail.py           # dry run
    python3 scripts/bug_fixed_mail.py --send    # needs SUPABASE_SERVICE_KEY and OUTREACH_* secrets
"""
import datetime
import json
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

LEDGER = os.path.join(ROOT, "data", "feedback-ledger.json")
AUDIT = os.path.join(ROOT, "data", "code-audit.json")
STORE = os.path.join(ROOT, "data", "store-builds.json")
MAILED = os.path.join(ROOT, "data", "bug-fixed-mailed.json")
PBX = "ios/AncientTrees/AncientTrees.xcodeproj/project.pbxproj"
GRADLE = "android/app/build.gradle.kts"
SHIPPED = ("READY_FOR_SALE", "REPLACED_WITH_NEW_VERSION")
LIVE_BUILD_URL = "https://ancienttrees.app/build.txt"

DUTCH = {"de", "het", "een", "ik", "niet", "en", "van", "kan", "je", "mijn", "dat", "is", "op", "alleen",
         "waar", "woon", "aanpassen", "werkt", "bij"}


def platform(row):
    f = (row.get("file") or "").split(":")[0]
    if f.startswith("ios/"):
        return "ios"
    if f.startswith("android/"):
        return "android"
    return "web"


def is_dutch(words):
    toks = re.findall(r"[a-zà-ÿ]+", (words or "").lower())
    return len(toks) >= 3 and sum(t in DUTCH for t in toks) / len(toks) >= 0.25


def compose(line, name, plat, dutch):
    if dutch:
        hi = "Hoi %s," % name if name else "Hoi,"
        update = "\n\nWerk de app bij om de oplossing te krijgen." if plat in ("ios", "android") else ""
        return ("Opgelost, dankzij jou",
                "%s\n\nJe liet ons weten dat iets in Ancient Trees niet werkte. Dat is opgelost: %s.%s\n\n"
                "Dank je wel voor het melden.\n\nAncient Trees" % (hi, line, update))
    hi = "Hi %s," % name if name else "Hi,"
    update = "\n\nUpdate the app to get the fix." if plat in ("ios", "android") else ""
    return ("Fixed, thanks to you",
            "%s\n\nYou told us something in Ancient Trees wasn't working. We fixed it: %s.%s\n\n"
            "Thank you for letting us know.\n\nAncient Trees" % (hi, line, update))


def git(*args):
    return subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True, text=True)


def number_at(commit, path, pattern):
    out = git("show", "%s:%s" % (commit, path))
    m = re.findall(pattern, out.stdout) if out.returncode == 0 else []
    return max(int(x) for x in m) if m else None


def first_number_after(sha, path, pattern):
    """The first build number raised after `sha` on main, or None."""
    start = number_at(sha, path, pattern)
    if start is None:
        return None
    log = git("log", "--format=%H", "--reverse", "%s..HEAD" % sha, "--", path)
    for c in log.stdout.split():
        n = number_at(c, path, pattern)
        if n is not None and n > start:
            return n
    return None


def live_commit():
    try:
        req = urllib.request.Request(LIVE_BUILD_URL, headers={"User-Agent": "AncientTreesBot/1.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read().decode().split()[0]
    except Exception:
        return None


def shipped(row, store, live):
    """(True|False, why) for a fixed BUG row."""
    sha = row.get("fixed_in")
    if row.get("status") != "fixed" or not sha:
        return False, "not fixed yet"
    plat = platform(row)
    if plat == "web":
        if not live:
            return False, "live site's commit unreadable"
        if git("cat-file", "-e", live + "^{commit}").returncode != 0:
            git("fetch", "-q", "origin", "main")
        ok = git("merge-base", "--is-ancestor", sha, live).returncode == 0
        return ok, "live on the site" if ok else "not deployed yet"
    if plat == "ios":
        n = first_number_after(sha, PBX, r"CURRENT_PROJECT_VERSION = (\d+);")
        if n is None:
            return False, "no iPhone build carries it yet"
        live_builds = [int(b) for b, v in store.items() if b.isdigit() and v.get("state") in SHIPPED]
        ok = any(b >= n for b in live_builds)
        return ok, ("in App Store build %d or later" % n) if ok else "waits for iPhone build %d in the App Store" % n
    n = first_number_after(sha, GRADLE, r"versionCode = (\d+)")
    return (n is not None), ("in Android build %d" % n) if n else "no Android build carries it yet"


def load(path, default):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return default


def plan(ledger_rows, bugs, mailed, store, live, shipped_fn=shipped):
    """[(feedback id, bug row, why)] ready to mail, and [(feedback id, reason)] waiting."""
    ready, waiting = [], []
    for fid, v in sorted(ledger_rows.items(), key=lambda kv: kv[0]):
        if v.get("status") != "bug" or fid in mailed:
            continue
        row = bugs.get(v.get("bug"))
        if not row:
            waiting.append((fid, "bug row %s missing" % v.get("bug")))
            continue
        ok, why = shipped_fn(row, store, live)
        if not ok:
            waiting.append((fid, "%s: %s" % (row["id"], why)))
        elif not (row.get("reader_line") or "").strip():
            waiting.append((fid, "%s: fixed, needs a reader_line in data/code-audit.json" % row["id"]))
        else:
            ready.append((fid, row, why))
    return ready, waiting


def submission(fid):
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    if not key:
        return None
    from sightings_publish import SUPA
    req = urllib.request.Request(
        "%s/rest/v1/submissions?select=id,user_id,email,why&id=eq.%s" % (SUPA, fid),
        headers={"apikey": key, "Authorization": "Bearer " + key})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            rows = json.loads(r.read()) or []
        return rows[0] if rows else None
    except Exception:
        return None


def main():
    really = "--send" in sys.argv
    ledger_rows = load(LEDGER, {"rows": {}}).get("rows", {})
    bugs = {r["id"]: r for r in load(AUDIT, {"findings": []}).get("findings", []) if r.get("id")}
    mailed = load(MAILED, {"_note": "feedback row -> the bug it reported and the day we told them it is fixed. "
                                    "Ids only. scripts/bug_fixed_mail.py.", "mailed": {}})
    # Ask Apple when the App Store key is at hand (crashes.py caches the
    # answer in data/store-builds.json); otherwise the cache.
    try:
        import crashes
        store = crashes.store_builds()
    except Exception:
        store = load(STORE, {})
    ready, waiting = plan(ledger_rows, bugs, mailed["mailed"], store, live_commit())
    for fid, why in waiting:
        print("  waits  #%s %s" % (fid, why))
    if not ready:
        print("bug_fixed_mail: nothing to send")
        return 0
    import ours
    from sightings_publish import address_of, send_mail
    from tree_approved import display_name
    for fid, row, where in ready:
        sub = submission(fid)
        if sub is None:
            print("  #%s: submission unreadable (no key?), not sent" % fid)
            continue
        uid = sub.get("user_id")
        if ours.is_ours(uid):
            mailed["mailed"][fid] = {"bug": row["id"], "date": None, "skipped": "our own account"}
            continue
        addr = (address_of(uid) if uid else None) or (sub.get("email") or "").strip()
        if not addr:
            print("  #%s: no address on file, not sent" % fid)
            continue
        dutch = is_dutch(sub.get("why"))
        line = (row.get("reader_line_nl") if dutch else None) or row["reader_line"]
        subject, body = compose(line.strip().rstrip("."), display_name(uid), platform(row),
                                dutch and bool(row.get("reader_line_nl")))
        print("  #%s %s (%s)" % (fid, row["id"], where))
        if send_mail(addr, subject, body, really, "feedback-%s" % fid,
                     recent_ok="tells them a problem they reported is fixed", batch="bug-fixed"):
            mailed["mailed"][fid] = {"bug": row["id"], "date": datetime.date.today().isoformat()}
    if really:
        with open(MAILED, "w", encoding="utf-8") as fh:
            json.dump(mailed, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
