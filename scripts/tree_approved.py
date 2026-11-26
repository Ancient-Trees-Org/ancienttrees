#!/usr/bin/env python3
"""Congratulate a reader the day a tree THEY added goes live on Ancient Trees.

Hidde, 2026-10-09: "I think once a tree is added to the database we should
email the user with the link and congratulate them, eventually we can add
gamification for this." The convention is Google Maps': a place you added that
it accepts arrives as a mail saying so, with the link (CONVENTIONS.md
2026-10-09, the word "Approved").

Narrow on purpose: a PHOTOGRAPH going live on a tree we already had is mailed
by sightings_publish.py instead (MAIL_WHEN_LIVE, since 2026-10-23: the first at
once, then at most one bundle per 30 days). This is only for a tree that did not exist here until a
reader sent it, which is the rarer and bigger thing. How it knows: the sighting
went into data/leads/_sightings.json as a NEW tree (that is where a sighting
matching nothing we map lands), and a published tree now carries a contributor
photograph with that same sighting_id.

Once per sighting, recorded in data/tree-approved-mailed.json (sighting ids and
dates only, never an address: this repository is public). Our own accounts
(scripts/ours.py) are never mailed. Signed "Ancient Trees", never as Hidde
(hard rule 4). Every mail goes through mailcheck and the do-not-contact list by
way of sightings_publish.send_mail.

    python3 scripts/tree_approved.py           # dry run: prints what it would send
    python3 scripts/tree_approved.py --send    # needs SUPABASE_SERVICE_KEY and OUTREACH_* secrets
"""
import datetime
import glob
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import people  # noqa: E402  account ids as codes in public files (2026-10-19)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import ours  # noqa: E402
from sightings_publish import (address_of, send_mail, SUPA,  # noqa: E402
                               BASE_URL, load, save)

LEADS = os.path.join(ROOT, "data", "leads", "_sightings.json")
MAILED = os.path.join(ROOT, "data", "tree-approved-mailed.json")


def lead_sightings():
    """Every sighting id that entered the leads file as a tree we did not have."""
    out = set()

    def walk(o):
        if isinstance(o, dict):
            sid = o.get("sighting_id")
            if sid:
                out.add(str(sid).lower())
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(load(LEADS, {}))
    return out


def approved_trees():
    """[(sighting_id, user_id, tree, city_name, city_slug)] for reader-added trees now live."""
    new_trees = lead_sightings()
    found = []
    for path in sorted(glob.glob(os.path.join(ROOT, "data", "cities", "*.json"))):
        with open(path, encoding="utf-8") as fh:
            city = json.load(fh)
        slug = os.path.splitext(os.path.basename(path))[0]
        for t in city.get("trees") or []:
            for p in [t.get("photo") or {}] + [p for p in (t.get("photos") or []) if p]:
                sid = str(p.get("sighting_id") or "").lower()
                if p.get("source") == "contributor" and sid in new_trees:
                    found.append((sid, p.get("contributor_user_id"), t, city.get("city", slug), slug))
                    break
    return found


def live_urls():
    """{tree_id: page url} from the live feed, so the link is the site's own
    answer (slug rules live in site/src/lib/slug.ts and are not copied here)
    and a tree is only congratulated once its page is actually deployed."""
    try:
        req = urllib.request.Request(f"{BASE_URL}/api/trees.json",
                                     headers={"User-Agent": "AncientTreesBot/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            feed = json.loads(r.read())
        return {t["id"]: BASE_URL + t["url"] for t in feed.get("trees", []) if t.get("url")}
    except Exception as e:
        print(f"tree_approved: live feed unreadable ({e.__class__.__name__}), nothing sent")
        return {}


def display_name(user_id):
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    if not key or not user_id:
        return None
    req = urllib.request.Request(
        f"{SUPA}/rest/v1/profiles?select=display_name&user_id=eq.{user_id}",
        headers={"apikey": key, "Authorization": "Bearer " + key})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            rows = json.loads(r.read()) or []
        name = (rows[0].get("display_name") or "").strip() if rows else ""
    except Exception:
        return None
    # A generated tree name ("Rooted Ash 4451", supabase/profile-at-signup.sql)
    # is not what anybody is called: "Hi there" instead (2026-11-15). Same
    # pattern as Profiles.isGeneratedName in the app.
    if not name or re.fullmatch(r"[A-Z][a-z]+ [A-Z][a-z]+ [0-9]{4}", name):
        return None
    # "MARK T." reads as shouting; a name typed in capitals gets ordinary case.
    if name.isupper():
        name = name.title()
    return name


def full_note(sid):
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    if not key:
        return None
    # A tree sent through the website's form is "tip-<submission id>" and its
    # words are the submission's `why`, not a sighting's note (2026-11-14: the
    # Villa Salina reader gave an age in prose, and the mail asked for it).
    tip = re.fullmatch(r"tip-(\d+)", str(sid))
    path = (f"/rest/v1/submissions?select=why&id=eq.{tip.group(1)}" if tip
            else f"/rest/v1/sightings?select=note&id=eq.{sid}")
    req = urllib.request.Request(
        SUPA + path, headers={"apikey": key, "Authorization": "Bearer " + key})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            rows = json.loads(r.read()) or []
        return (rows[0].get("why") if tip else rows[0].get("note")) if rows else None
    except Exception:
        return None


def what_they_gave(sid):
    """What the reader filled in when adding the tree: age, trunk size, a note."""
    # A note can carry what the fields do not: the Tangier fig's reader gave
    # the trunk as "2.2 to 2.8 m" in prose and left girth empty, and the mail
    # would have asked them for it (2026-10-21).
    sid = str(sid).lower()
    for l in (load(LEADS, {}).get("leads") or []):
        if str(l.get("sighting_id") or "").lower() == sid:
            # data/leads/_sightings.json keeps 500 characters; the measure was
            # in the third paragraph, so read the whole note when we can.
            note = (full_note(sid) or l.get("note") or "").strip()
            size = re.search(r"\d+(?:[.,]\d+)?\s*(?:cm|m|metres?|meters?|ft|feet)\b", note, re.I) \
                and re.search(r"girth|circumference|diameter|trunk|around", note, re.I)
            years = re.search(r"\d{2,4}\s*(?:years|yrs|jaar|ans|años|anni|jahre)", note, re.I)
            return {
                "age": bool(l.get("age") or years),
                "trunk": bool(l.get("girth_cm") or l.get("girth_hugs") or size),
                "story": len(note) >= 40,
            }
    return {"age": False, "trunk": False, "story": False}


AMBASSADORS = os.path.join(ROOT, "data", "ambassadors.json")


def seat_open(uid, slug):
    """True when this place has no ambassador and this reader was never asked
    for it, nor asked never to be mailed (ambassador.py's own skip rules)."""
    doc = load(AMBASSADORS, {})
    if any(e.get("place_slug") == slug for e in doc.get("ambassadors", [])):
        return False
    # Somebody who is already an ambassador somewhere is not asked again in a
    # P.S. (2026-11-15: Media's new ambassador added a tree in Willistown the
    # same afternoon and the draft asked them to look after Willistown too).
    raw = people.uid(uid) if str(uid).startswith("p_") else uid
    if any(e.get("user_id") in (uid, raw) for e in doc.get("ambassadors", [])):
        return False
    ref = people.ref(uid)
    for i in doc.get("invited", []):
        if people.ref(i.get("user_id")) == ref and i.get("place_slug") in (slug, "*"):
            return False
    return True


def note_invited(uid, slug, place, tree_name):
    """Record the P.S. as the invitation, so ambassador.py --invite-scan does
    not send a second mail for the same place."""
    doc = load(AMBASSADORS, {})
    doc.setdefault("invited", []).append({
        "user_id": people.ref(uid), "place_slug": slug, "place_name": place,
        "date": datetime.date.today().isoformat(), "trees": [tree_name],
        "note": "asked in a P.S. under the congratulation mail (tree_approved.py)"})
    save(AMBASSADORS, doc, indent=2)


def what_we_did(sid, tree_name=None):
    """What happened to what they sent, said plainly (2026-11-26, a tester:
    three photographs sent, one shown, the description rewritten, and "I
    wasn't told about either change"). Which photographs stayed off and why,
    from data/reader-extras.json, and that the story is ours, written from
    what they told us. Returns lines for the mail, maybe none."""
    import reader_extras
    rec = reader_extras.ledger()["sightings"].get(sid, {}).get("extras", {})
    lines = []
    if rec:
        total = 1 + len(rec)
        off = [(int(n), v) for n, v in rec.items() if v.get("verdict") == "left_out"]
        about = f" of {tree_name}" if tree_name else ""
        if not off:
            lines.append(f"All {total} of your photographs{about} are on the page.")
        else:
            groups = {}
            for n, v in sorted(off):
                groups.setdefault(v.get("reason"), []).append(n + 1)
            parts = []
            for reason, nums in groups.items():
                text = reader_extras.LEAVE_REASONS.get(reason, "we could not use it")
                if len(nums) == 1:
                    parts.append(f"photo {nums[0]} because {text}")
                else:
                    text = text.replace(" in it", " in them").replace("it shows", "they show").replace(
                        "it looks", "they look").replace("it was", "they were")
                    parts.append("photos " + ", ".join(map(str, nums[:-1])) + f" and {nums[-1]} because {text}")
            kept = total - len(off)
            lines.append(f"{kept} of your {total} photographs{about} {'is' if kept == 1 else 'are'} on the page. "
                         f"We left out {'; '.join(parts)}.")
    if not tree_name:
        lines.append("We wrote the story on the page ourselves, from what you sent and what we "
                     "could check. If anything in it is wrong, tell us and we put it right.")
    return lines


def mail_for(name, tree, city_name, page, gave=None, seat=False, web=False, did=None):
    """THE ASK FOLLOWS WHAT THEY GAVE (Hidde, 2026-10-20, on the Freiburg beech,
    which arrived as a photograph and a pin and nothing else: "ask if they have
    more info on the tree (age, girth, story etc) ... make that standard unless
    they gave a full info thing"). A page built from a photograph alone is a
    page that asks its readers for everything; the person who stood there is
    the one most likely to know. So the one ask in this mail is for what is
    missing, by name, and only when nothing is missing does it ask for the next
    tree. One ask, never two (drafts/HIS_VOICE.md), and a reply to the mail,
    never a form. Nothing here reads as a task: it asks what they know."""
    gave = gave or {"age": False, "trunk": False, "story": False}
    missing = [w for k, w in (("age", "how old it might be"), ("trunk", "how big around the trunk is"),
                              ("story", "a story about it")) if not gave.get(k)]
    if missing:
        wants = ", ".join(missing[:-1]) + (" or " if len(missing) > 1 else "") + missing[-1]
        # One thing missing reads as a plain question ("Do you know a story
        # about it?"); "more about it, a story about it" said it twice.
        lead = "Do you know " if len(missing) == 1 else "Do you know more about it, "
        ask = (f"{lead}{wants}? Just reply to this mail and it goes on the page.")
    else:
        # The way they used, so the ask is one they can do (2026-11-14: a
        # website sender who works from a desktop was told to use the app).
        ask = ("Is there another tree near you that belongs on the map? You can add it "
               + ("on the website" if web else "in the app") + " the same way.")
    subject = "Your tree is on Ancient Trees"
    body = (
        f"Hi {name or 'there'},\n\n"
        f"Congratulations: {tree['name']} in {city_name}, the tree you added, has been "
        f"approved and is now on Ancient Trees for everybody to find:\n"
        f"{page}\n\n"
        f"You stood in front of it and sent it to us, and now other people can go and see it too.\n\n"
        + "".join(f"{line}\n\n" for line in (did or []))
        + f"{ask}\n\n"
        f"Ancient Trees\n{BASE_URL}\n"
    )
    # THE AMBASSADOR ASK RIDES ALONG, SMALL (Hidde, 2026-10-21: "is het niet
    # subtieler om je mail te schrijven en eronder minder groot also: city is
    # still looking for an ambassador - let us know if your interested"). The
    # Freiburg reader got the congratulation and a separate invitation on the
    # same day; one mail with a P.S. replaces the second.
    if seat:
        body += (f"\nP.S. {city_name} is still looking for an ambassador, somebody who adds "
                 f"photos and keeps an eye on the list. Let us know if you're interested.\n")
    return subject, body


def bundle_for(name, items, did=None):
    """ONE MAIL PER PERSON (2026-11-15, the Guardian day: one reader added three
    trees and got three congratulations within the hour, another got two). Every
    tree with its link, one ask for all of them, and the P.S. for the first place
    that still has a seat."""
    lines = "\n".join(f"{t['name']} in {c}:\n{p}" for _, _, t, c, _, p in items)
    count = "both trees" if len(items) == 2 else f"the {len(items)} trees"
    subject = "Your trees are on Ancient Trees"
    body = (
        f"Hi {name or 'there'},\n\n"
        f"Congratulations: {count} you added have been approved and are now "
        f"on Ancient Trees for everybody to find:\n\n{lines}\n\n"
        f"You stood in front of them and sent them to us, and now other people can go and see them too.\n\n"
        + "".join(f"{line}\n\n" for line in (did or []))
        + f"If you know more about any of them, just reply to this mail and it goes on the page.\n\n"
        f"Ancient Trees\n{BASE_URL}\n"
    )
    return subject, body


def mark_tip_published(sid, tree, page, really):
    """Tell the reader's own My trees page that a tree they added on the
    WEBSITE is live, whether or not our mail reaches them.

    Found 2026-11-16 on the Arbour Oak (tip-839): the reader signed in with a
    Google account on the address of a magazine whose domain died years ago,
    so the congratulation bounced and their account page was the one place
    left to tell them. It said "Sent": this script mailed and recorded the
    sighting id, but never touched the submissions row, and My trees
    (site/src/lib/my-trees-js.ts) reads `outcome` from that row. All twelve
    website trees congratulated until then still read "Sent". The app was
    fine: its sightings rows read "published" (sightings_publish.py).

    So the row gets outcome 'changed' (My trees: "Approved"), a one-line
    reply_text that the card prints, and replied_at, so contributor_reply.py
    does not mail a second "on the site now" to the same person."""
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    row = sid[len("tip-"):]
    if not row.isdigit():
        return False
    text = "On the site now as %s: %s\n" % (tree["name"], page)
    if not really:
        print(f"  {tree['id']}: would mark submission {row} approved on the reader's My trees")
        return False
    if not key:
        return False
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    body = json.dumps({"outcome": "changed", "reply_text": text, "replied_at": now}).encode()
    req = urllib.request.Request(f"{SUPA}/rest/v1/submissions?id=eq.{row}&outcome=is.null",
                                 data=body, method="PATCH",
                                 headers={"apikey": key, "Authorization": "Bearer " + key,
                                          "Content-Type": "application/json",
                                          "Prefer": "return=minimal"})
    try:
        with urllib.request.urlopen(req, timeout=30):
            pass
    except Exception as e:
        print(f"  {tree['id']}: could not mark submission {row} ({e.__class__.__name__}), next knock")
        return False
    print(f"  {tree['id']}: submission {row} marked approved on the reader's My trees")
    return True


def main(argv):
    really = "--send" in argv
    mailed = load(MAILED, {"mailed": {}})
    done = mailed.setdefault("mailed", {})
    today = datetime.date.today().isoformat()
    all_trees = approved_trees()
    who_of = {sid: uid for sid, uid, _, _, _ in all_trees}
    # WEBSITE TREES SAY "APPROVED" ON THE READER'S OWN PAGE, mail or no mail,
    # and the ones congratulated before 2026-11-16 are caught up here too.
    marked = mailed.setdefault("marked", {})
    web_urls = None
    for sid, uid, tree, _, _ in all_trees:
        if not sid.startswith("tip-") or sid in marked or not uid or ours.is_ours(uid):
            continue
        if web_urls is None:
            web_urls = live_urls()
        page = web_urls.get(tree["id"])
        if page and mark_tip_published(sid, tree, page, really):
            marked[sid] = today
    # Someone congratulated today waits for tomorrow's knock, so a person who
    # adds trees all afternoon gets one mail a day, not one per tree.
    mailed_today = {who_of.get(s) for s, rec in done.items() if rec.get("date") == today and who_of.get(s)}
    sent = 0
    urls = None
    ready = {}
    for sid, uid, tree, city_name, city_slug in all_trees:
        if sid in done:
            continue
        if not uid or ours.is_ours(uid):
            continue
        if urls is None:
            urls = live_urls()
        page = urls.get(tree["id"])
        if not page:
            print(f"  {tree['id']}: not in the live feed yet, waits for the deploy")
            continue
        if uid in mailed_today:
            print(f"  {tree['id']}: this reader was congratulated today already, tomorrow's knock")
            continue
        ready.setdefault(uid, []).append((sid, uid, tree, city_name, city_slug, page))
    for uid, items in ready.items():
        addr = address_of(people.uid(uid))
        if not addr:
            print(f"  {items[0][2]['id']}: no address for the account (no service key, or the account is gone)")
            continue
        name = display_name(people.uid(uid))
        seat_at = next((it for it in items if seat_open(uid, it[4])), None)
        if len(items) == 1:
            sid, _, tree, city_name, city_slug, page = items[0]
            subject, body = mail_for(name, tree, city_name, page, what_they_gave(sid),
                                     seat=bool(seat_at), web=sid.startswith("tip-"), did=what_we_did(sid))
        else:
            did = [l for it in items for l in what_we_did(it[0], it[2]["name"])]
            did.append(what_we_did("")[-1])
            subject, body = bundle_for(name, items, did=did)
            if seat_at:
                body += (f"\nP.S. {seat_at[3]} is still looking for an ambassador, somebody who adds "
                         f"photos and keeps an eye on the list. Let us know if you're interested.\n")
        if send_mail(addr, subject, body, really, items[0][0]):
            for sid, _, tree, _, _, _ in items:
                done[sid] = {"tree_id": tree["id"], "date": today}
            if seat_at:
                note_invited(uid, seat_at[4], seat_at[3], seat_at[2]["name"])
            sent += 1
    if really:
        save(MAILED, mailed)
    print(f"tree_approved: {sent} congratulation(s) sent")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
