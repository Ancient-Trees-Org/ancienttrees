#!/usr/bin/env python3
"""Tell a reader that a bug they reported is fixed, in two steps for the apps.

Hidde, 2026-11-25 ("Ja, bouw hem"), after reading the Settings feedback: a
reader who reported that something did not work heard nothing when we fixed
it, unless he answered by hand. The convention is Canny's and Linear's: the
person who asked hears when its status changes. Short standard mails, in our
words, never quoting theirs (their words stay his to answer, CLAUDE.md
"General feedback is Hidde's to read"), signed Ancient Trees.

THE ORDER (Hidde, 2026-11-26: "dit kan heel lang duren dus ik zou m alvast
mailen en zeggen dat we wachten op de nieuwe build", "en onthou die
volgorde"): an app fix can wait weeks for a store build, so
  1. FIXED ("coming"): the day the fix is on main, the reader hears it is
     fixed and comes with the next app update;
  2. OUT ("live"): the day that update is in their store, they hear it is out
     and to update.
A website fix reaches everyone with the next deploy, so it gets one mail, at 2.

WHICH READERS: a feedback row closed as a bug (`feedback.py --close <id> bug
<bug-id>`, data/feedback-ledger.json) whose BUG row in data/code-audit.json is
`fixed` with `fixed_in` and carries `reader_line`: what now works, in plain
words for a reader ("the country you pick in Edit profile now stays").
Without that line nothing is sent and the row is listed, because the bug's
own summary is written for us. `reader_line_nl` is used for a reader who
wrote in Dutch.

WHERE THE FIX LIVES: the files `fixed_in` changed (else the row's `file`):
  web (site/, supabase/, scripts/...): the live site's commit (/build.txt)
    contains `fixed_in`;
  iPhone (ios/): the first build number raised after `fixed_in` is
    READY_FOR_SALE (crashes.store_builds(), cached in data/store-builds.json),
    or a later one is;
  Android (android/): a versionCode raised after `fixed_in` is listed in
    data/android-releases.json (Play uploads are by hand; the session that
    releases a build adds its number).
A fix on both phones is out once both are.

Each step once per feedback row, recorded in data/bug-fixed-mailed.json (ids
and dates, never an address). Our own accounts are never mailed. Every mail
passes mailcheck and the do-not-contact list (sightings_publish.send_mail);
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
ANDROID_RELEASES = os.path.join(ROOT, "data", "android-releases.json")
PBX = "ios/AncientTrees/AncientTrees.xcodeproj/project.pbxproj"
GRADLE = "android/app/build.gradle.kts"
SHIPPED = ("READY_FOR_SALE", "REPLACED_WITH_NEW_VERSION")
LIVE_BUILD_URL = "https://ancienttrees.app/build.txt"

DUTCH = {"de", "het", "een", "ik", "niet", "en", "van", "kan", "je", "mijn", "dat", "is", "op", "alleen",
         "waar", "woon", "aanpassen", "werkt", "bij"}


def platform_of_path(f):
    f = (f or "").split(":")[0]
    if f.startswith("ios/"):
        return "ios"
    if f.startswith("android/"):
        return "android"
    return "web"


def platform(row):
    return platform_of_path(row.get("file"))


def git(*args):
    return subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True, text=True)


def platforms(row):
    """Where the fix landed: the files its commit changed, else the row's file.
    Tests and data alone say nothing; an app fix is app-only when no site,
    supabase or script file changed with it."""
    sha = row.get("fixed_in")
    files = git("show", "--name-only", "--format=", sha).stdout.split() if sha else []
    files = [f for f in files if not re.search(r"(^|/)(test|tests|AncientTreesTests|AncientTreesUITests)/|test_", f)
             and not f.startswith(("data/", "drafts/")) and not f.endswith(".md")]
    got = {platform_of_path(f) for f in files}
    return got or {platform(row)}


def is_dutch(words):
    toks = re.findall(r"[a-zà-ÿ]+", (words or "").lower())
    return len(toks) >= 3 and sum(t in DUTCH for t in toks) / len(toks) >= 0.25


def lower_first(line):
    line = line.strip().rstrip(".")
    return line[:1].lower() + line[1:] if line[:2] != "I " else line


def compose(line, name, app, dutch, stage="live", told=False):
    """(subject, body). stage "coming": fixed on our side, comes with the next
    app update. stage "live": in their hands now; `told` when they had the
    "coming" mail, which makes this one short."""
    line = lower_first(line)
    if dutch:
        hi = "Hoi %s," % name if name else "Hoi,"
        if stage == "coming":
            return ("Opgelost, dankzij jou",
                    "%s\n\nJe liet ons weten dat iets in Ancient Trees niet werkte. Dat hebben we opgelost: %s.\n\n"
                    "De oplossing zit in de volgende update van de app. We laten het je weten zodra die er is.\n\n"
                    "Dank je wel voor het melden.\n\nAncient Trees" % (hi, line))
        if told:
            return ("De oplossing staat nu in de app",
                    "%s\n\nDe update van de app met de oplossing is er: %s. Werk de app bij om hem te krijgen.\n\n"
                    "Ancient Trees" % (hi, line))
        update = "\n\nWerk de app bij om de oplossing te krijgen." if app else ""
        return ("Opgelost, dankzij jou",
                "%s\n\nJe liet ons weten dat iets in Ancient Trees niet werkte. Dat hebben we opgelost: %s.%s\n\n"
                "Dank je wel voor het melden.\n\nAncient Trees" % (hi, line, update))
    hi = "Hi %s," % name if name else "Hi,"
    if stage == "coming":
        return ("Fixed, thanks to you",
                "%s\n\nYou told us something in Ancient Trees wasn't working. We fixed it: %s.\n\n"
                "The fix comes with the next app update. We'll let you know when it's out.\n\n"
                "Thank you for letting us know.\n\nAncient Trees" % (hi, line))
    if told:
        return ("The fix is in the app now",
                "%s\n\nThe app update with the fix is out: %s. Update the app to get it.\n\n"
                "Ancient Trees" % (hi, line))
    update = "\n\nUpdate the app to get the fix." if app else ""
    return ("Fixed, thanks to you",
            "%s\n\nYou told us something in Ancient Trees wasn't working. We fixed it: %s.%s\n\n"
            "Thank you for letting us know.\n\nAncient Trees" % (hi, line, update))


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


def out_on(plat, sha, store, live):
    """(True|False, why) for one platform."""
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
    if n is None:
        return False, "no Android build carries it yet"
    # Play uploads are done by hand, so only a build written down as released
    # counts (data/android-releases.json, the session that uploads adds it).
    released = load(ANDROID_RELEASES, {}).get("released", [])
    ok = any(int(r) >= n for r in released)
    return ok, ("in Android build %d or later" % n) if ok else "waits for Android build %d on Play" % n


def state(row, store, live):
    """("unfixed" | "coming" | "live", app?, why)."""
    sha = row.get("fixed_in")
    if row.get("status") != "fixed" or not sha:
        return "unfixed", False, "not fixed yet"
    plats = platforms(row)
    app = bool(plats & {"ios", "android"})
    results = [out_on(p, sha, store, live) for p in sorted(plats)]
    why = "; ".join(w for _, w in results)
    if all(ok for ok, _ in results):
        return "live", app, why
    # A website fix is out with the next deploy, within the hour: one mail.
    return ("coming" if app else "unfixed"), app, why


def load(path, default):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return default


def plan(ledger_rows, bugs, mailed, store, live, state_fn=state):
    """[(feedback id, bug row, stage, app, told, why)] to mail, and [(feedback id, reason)] waiting."""
    ready, waiting = [], []
    for fid, v in sorted(ledger_rows.items(), key=lambda kv: kv[0]):
        if v.get("status") != "bug":
            continue
        done = mailed.get(fid) or {}
        if done.get("date") or done.get("skipped"):
            continue
        row = bugs.get(v.get("bug"))
        if not row:
            waiting.append((fid, "bug row %s missing" % v.get("bug")))
            continue
        st, app, why = state_fn(row, store, live)
        if st == "unfixed":
            waiting.append((fid, "%s: %s" % (row["id"], why)))
        elif not (row.get("reader_line") or "").strip():
            waiting.append((fid, "%s: fixed, needs a reader_line in data/code-audit.json" % row["id"]))
        elif st == "coming" and done.get("coming"):
            waiting.append((fid, "%s: told it is fixed, %s" % (row["id"], why)))
        else:
            ready.append((fid, row, st, app, bool(done.get("coming")), why))
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
    mailed = load(MAILED, {"_note": "feedback row -> the bug it reported and the days we told them it is fixed "
                                    "(coming) and out (date). Ids only. scripts/bug_fixed_mail.py.", "mailed": {}})
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
    today = datetime.date.today().isoformat()
    for fid, row, stage, app, told, why in ready:
        sub = submission(fid)
        if sub is None:
            print("  #%s: submission unreadable (no key?), not sent" % fid)
            continue
        uid = sub.get("user_id")
        entry = mailed["mailed"].setdefault(fid, {"bug": row["id"]})
        if ours.is_ours(uid):
            entry["skipped"] = "our own account"
            continue
        addr = (address_of(uid) if uid else None) or (sub.get("email") or "").strip()
        if not addr:
            print("  #%s: no address on file, not sent" % fid)
            continue
        dutch = is_dutch(sub.get("why")) and bool(row.get("reader_line_nl"))
        line = row["reader_line_nl"] if dutch else row["reader_line"]
        subject, body = compose(line, display_name(uid), app, dutch, stage, told)
        print("  #%s %s, %s (%s)" % (fid, row["id"], stage, why))
        if send_mail(addr, subject, body, really, "feedback-%s" % fid,
                     recent_ok="tells them a problem they reported is fixed", batch="bug-fixed"):
            entry["coming" if stage == "coming" else "date"] = today
    if really:
        with open(MAILED, "w", encoding="utf-8") as fh:
            json.dump(mailed, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
