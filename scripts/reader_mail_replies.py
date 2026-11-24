#!/usr/bin/env python3
"""A reader's mail reply to one of OUR reader mails becomes a row the reader
judge picks up, instead of waiting in the inbox until a session reads it.

Hidde, 2026-11-18, looking at READER_FLOW.md's gaps: "Mail replies first".
The hold mails ask questions ("where does it stand?", "can it be seen from
the street?"), the congratulation asks for age and a story, and their answers
landed in the info@ inbox where nothing picked them up.

What it opens, and nothing else (the outreach_inbox.py discipline, same
mailbox, same credentials):
- read-only (readonly=True): nothing is marked read, moved or deleted;
- only a message whose sender got a reader mail from us (data/outreach-sent.json,
  outlet "contributor" or "reader (app)", pulled with private_store.py), and
  whose subject, without Re:/Fwd:, is one of our reader-mail subjects below;
- only the last DAYS days.

What it writes: one submissions row per reply, kind "feedback", page
"mail-reply:<id of the reader's newest answered row>", their words in `why`
(quoted history cut off), their account in `user_id` when the address belongs
to one. The existing machinery does the rest: the digest shows their words in
full, the reader judge acts on it (BRIEF_READER_JUDGE.md "Mail replies"), and
contributor_reply.py sends nothing for it (THANK_YOU is off). Message-Ids are
remembered as hashes in data/mail-replies-seen.json, so a reply is filed once.

    python3 scripts/reader_mail_replies.py           # dry run: who and which subject
    python3 scripts/reader_mail_replies.py --file    # write the rows
    python3 scripts/reader_mail_replies.py --count   # how many new replies, nothing written
Needs OUTREACH_SMTP_USER/PASS (IMAP), SUPABASE_SERVICE_KEY, and the send log.
"""
import datetime
import email
import email.utils
import hashlib
import imaplib
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from outreach_inbox import strip_prefixes, decode, body_of, BOXES  # noqa: E402
from imap_folders import folder  # noqa: E402
import inbox_health  # noqa: E402

SUPA = "https://caimvxiyrtifilimlkqw.supabase.co"
SENT = os.path.join(ROOT, "data", "outreach-sent.json")
SEEN = os.path.join(ROOT, "data", "mail-replies-seen.json")
DAYS = 21
READER_OUTLETS = ("contributor", "reader (app)")
# Every mail we send a reader, by the start of its subject (lower case).
SUBJECTS = ("about what you sent us", "your tree is on ancient trees",
            "your trees are on ancient trees", "your photo is on the page of",
            "your photos are on the trees' pages")
QUOTE_START = re.compile(
    r"^(on .{4,200} wrote:|op .{4,200} schreef.*:|am .{4,200} schrieb.*:|le .{4,200} a écrit\s*:|"
    r"el .{4,200} escribió:|em .{4,200} escreveu:|il .{4,200} ha scritto:|"
    r"-{2,}\s*original message\s*-{2,}|from:\s.*ancient ?trees.*|van:\s.*ancient ?trees.*)\s*$", re.I)


def their_words(text):
    """The reply without the quoted mail below it."""
    out = []
    for line in (text or "").splitlines():
        s = line.strip()
        if s.startswith(">") or QUOTE_START.match(s):
            break
        out.append(line.rstrip())
    words = "\n".join(out).strip()
    return re.sub(r"\n{3,}", "\n\n", words)[:4000]


def h(s):
    return hashlib.sha1(s.encode("utf-8", "replace")).hexdigest()[:20]


def folder_ids(imap, since):
    """Message numbers in INBOX, then in Spam, each folder selected (readonly)
    before its numbers are yielded, so a fetch inside the loop hits it."""
    for box in BOXES:
        if imap.select(folder(imap, box), readonly=True)[0] != "OK":
            continue
        _, ids = imap.search(None, "SINCE", since)
        for mid in (ids[0] or b"").split():
            yield mid


def supa(path, key, method="GET", body=None):
    req = urllib.request.Request(SUPA + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"apikey": key, "Authorization": "Bearer " + key,
                                          "Content-Type": "application/json", "Prefer": "return=representation"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
    return json.loads(raw) if raw else None


def readers_mailed():
    try:
        log = json.load(open(SENT, encoding="utf-8")).get("sent", [])
    except (OSError, ValueError):
        return None
    return {(e.get("to") or "").strip().lower() for e in log if e.get("outlet") in READER_OUTLETS and e.get("to")}


def ours(subject):
    s = strip_prefixes(subject or "")
    return s.startswith(SUBJECTS)


def account_ids(key):
    by_mail, page = {}, 1
    while page <= 10:
        batch = (supa("/auth/v1/admin/users?page=%d&per_page=1000" % page, key) or {}).get("users") or []
        for u in batch:
            if u.get("id") and u.get("email"):
                by_mail[u["email"].strip().lower()] = u["id"]
        if len(batch) < 1000:
            break
        page += 1
    return by_mail


def main(argv):
    write, count = "--file" in argv, "--count" in argv
    user, pw = os.environ.get("OUTREACH_SMTP_USER"), os.environ.get("OUTREACH_SMTP_PASS")
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    if not (user and pw and key):
        print("reader_mail_replies: mailbox or Supabase key absent, nothing read")
        print(0) if count else None
        return 0
    mailed = readers_mailed()
    if not mailed:
        print("reader_mail_replies: no send log (run private_store.py pull first), nothing read")
        print(0) if count else None
        return 0
    try:
        seen = set(json.load(open(SEEN, encoding="utf-8")).get("seen", []))
    except (OSError, ValueError):
        seen = set()
    # The same login tells whether mail still reaches us (inbox_health.py,
    # Hidde 2026-11-24): no second login, a failure recorded before it raises.
    try:
        imap = imaplib.IMAP4_SSL(os.environ.get("OUTREACH_IMAP_HOST", "imap.gmail.com"))
        imap.login(user, pw)
    except Exception as e:
        inbox_health.record_failure(e)
        raise
    try:
        inbox_health.record(imap)
    except Exception as e:
        print("reader_mail_replies: inbox check skipped (%s)" % e.__class__.__name__)
    since = (datetime.date.today() - datetime.timedelta(days=DAYS)).strftime("%d-%b-%Y")
    found = []
    # Spam too (2026-11-19): readers' replies reach Gmail through ImprovMX's
    # forwarding and some land in Spam (Old Knobbley, a "Your tree is on
    # Ancient Trees" reply), where this reader never looked.
    for mid in folder_ids(imap, since):
        _, hdr = imap.fetch(mid, "(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT MESSAGE-ID)])")
        head = email.message_from_bytes(hdr[0][1])
        sender = (email.utils.parseaddr(decode(head.get("From", "")))[1] or "").lower()
        if sender not in mailed:
            continue                      # never opened: not a reader we mailed
        subject = decode(head.get("Subject", ""))
        if not ours(subject):
            continue                      # their other mail stays Hidde's
        msgid = (head.get("Message-ID") or "").strip() or (sender + subject)
        if h(msgid) in seen:
            continue
        _, raw = imap.fetch(mid, "(BODY.PEEK[])")
        msg = email.message_from_bytes(raw[0][1])
        found.append((h(msgid), sender, subject, their_words(body_of(msg, limit=8000))))
    imap.logout()
    if count:
        print(len(found))
        return 0
    if not found:
        print("reader_mail_replies: no new reply to a reader mail")
        return 0
    by_mail = account_ids(key) if write else {}
    for hid, sender, subject, words in found:
        print("REPLY  %s  %r  (%d chars)" % (hid, subject[:70], len(words)))
        if not write:
            continue
        uid = by_mail.get(sender)
        orig = None
        if uid:
            rows = supa("/rest/v1/submissions?user_id=eq.%s&kind=neq.feedback&select=id,tree,city"
                        "&order=created_at.desc&limit=1" % uid, key) or []
            orig = rows[0] if rows else None
        row = {"kind": "feedback", "why": words or "(an empty reply)",
               "page": "mail-reply:%s" % (orig["id"] if orig else "unknown"),
               "tree": (orig or {}).get("tree") or "", "city": (orig or {}).get("city") or ""}
        if uid:
            row["user_id"] = uid
        else:
            row["email"] = sender         # an address with no account: the legacy reply column
        supa("/rest/v1/submissions", key, "POST", row)
        seen.add(hid)
    if write:
        json.dump({"_note": "Hashes of reader mail replies already filed (scripts/reader_mail_replies.py).",
                   "seen": sorted(seen)}, open(SEEN, "w", encoding="utf-8"), indent=1)
        open(SEEN, "a").write("\n")
        print("reader_mail_replies: %d repl%s filed as feedback rows" % (len(found), "y" if len(found) == 1 else "ies"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
