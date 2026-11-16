#!/usr/bin/env python3
"""Keep score of the Android closed test group (Hidde, 2026-11-16: "can you
keep score of the android test group").

The list lives in data/outreach-android-testers.json, which holds people's
addresses and is therefore private: private_store.py syncs it with the other
data/outreach-*.json files and git never sees it. Pull before reading on a
fresh checkout, push after a change.

Google Play lets a new personal developer account into production only after
at least 12 testers have been opted in to the closed test for 14 days
(drafts/play-console-steps.md, step 4), so the score is counted against 12.

    python3 scripts/android_testers.py                     # the score and the list
    python3 scripts/android_testers.py --add "<name>" <email> <status> "<how>" ["<thread>"]
    python3 scripts/android_testers.py --set <email> <status>
    python3 scripts/android_testers.py --emails            # opted-in-able addresses, comma separated, for Play's tester list

`to_ask` is somebody worth asking who has not been offered the test yet.
A session that offers the test in a mail adds the person as `asked`; their
yes makes it `yes`; the day the opt-in link goes out, `invited`; once Play
shows them opted in, `joined`.
"""
import datetime
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "data", "outreach-android-testers.json")
STATUSES = ["to_ask", "asked", "yes", "invited", "joined", "declined"]
NEEDED = 12


def load():
    if not os.path.exists(PATH):
        sys.exit("No tester list on disk: run python3 scripts/private_store.py pull first.")
    return json.load(open(PATH, encoding="utf-8"))


def save(d):
    json.dump(d, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(PATH, "a", encoding="utf-8").write("\n")
    print("saved; run python3 scripts/private_store.py push")


def show(d):
    rows = d["testers"]
    count = {s: sum(1 for r in rows if r["status"] == s) for s in STATUSES}
    willing = count["yes"] + count["invited"] + count["joined"]
    print(f"Android test group: {willing} of {NEEDED} willing "
          f"({count['joined']} joined, {count['invited']} invited, {count['yes']} said yes), "
          f"{count['asked']} asked and waiting, {count['to_ask']} still to ask, {count['declined']} declined.")
    print()
    for s in STATUSES:
        for r in rows:
            if r["status"] != s:
                continue
            flag = "" if r.get("google_address", True) else "  (not a Google address: ask which one)"
            print(f"  {s:8} {r['since']}  {r['name']}{flag}")


def main(a):
    d = load()
    if not a:
        show(d)
        return 0
    if a[0] == "--add" and len(a) >= 5:
        name, email, status, how = a[1], a[2].lower(), a[3], a[4]
        if status not in STATUSES:
            sys.exit(f"status must be one of {STATUSES}")
        if any(r["email"] == email for r in d["testers"]):
            sys.exit(f"{email} is on the list already; use --set")
        d["testers"].append({
            "name": name, "email": email, "status": status,
            "since": datetime.date.today().isoformat(), "how": how,
            "thread": a[5] if len(a) > 5 else "",
            "google_address": email.endswith(("@gmail.com", "@googlemail.com")),
        })
        save(d)
        show(d)
        return 0
    if a[0] == "--set" and len(a) == 3:
        email, status = a[1].lower(), a[2]
        if status not in STATUSES:
            sys.exit(f"status must be one of {STATUSES}")
        for r in d["testers"]:
            if r["email"] == email:
                r["status"], r["since"] = status, datetime.date.today().isoformat()
                save(d)
                show(d)
                return 0
        sys.exit(f"{email} is not on the list")
    if a[0] == "--emails":
        print(",".join(r["email"] for r in d["testers"] if r["status"] in ("yes", "invited", "joined")))
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
