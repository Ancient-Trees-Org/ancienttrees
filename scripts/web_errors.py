#!/usr/bin/env python3
"""What breaks on the website, grouped so a person can read it.

    python3 scripts/web_errors.py           every error type of the last 8 days
    python3 scripts/web_errors.py --light   only the quality line's verdict
    python3 scripts/web_errors.py --prune   delete rows past 90 days and test rows
                                            (daily, data-digest.yml)

Every page posts its script errors to the Supabase `web_errors` table
(site/src/lib/web-errors-js.ts, supabase/web-errors.sql; Hidde, 2026-11-04,
the digest's quality line). This is the reader, with the service key
(SUPABASE_SERVICE_KEY, or ~/.ancienttrees-supabase.env, as crashes.py).

A TYPE is the message plus the script it came from. The last 24 hours are
read against the seven days before them:
  red     on 3+ pages or 5+ reports in the last 24 hours, and either not seen
          in those seven days or seen fewer times in all seven than in this
          one day (a fault spreading): rung-2 work
Browsers word one fault differently (Chrome "Cannot read properties of null",
Safari "null is not an object"), so `normalise()` reads them as one type.
  orange  any other new type
  green   nothing new (known types still firing are listed, not lit)
  grey    the table is not there yet, or no key
A row holds no visitor id, so "visitors" is counted as reports; the page
caps itself at three a load, which keeps one visitor from looking like five.

PRIVACY: a row holds a message, a file and line, a path, a browser family and
a build. Nothing here prints anything else, and nothing about a person exists
to print.
"""
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inbox import SUPA, load_key  # noqa: E402

RED_PAGES = 3
RED_REPORTS = 5
KEEP_DAYS = 90  # the privacy promise in supabase/web-errors.sql and CLAUDE.md


def fetch(key, days=8):
    """Rows of the last `days` days, or raises. 404 means no table yet."""
    since = (datetime.datetime.now(datetime.timezone.utc)
             - datetime.timedelta(days=days)).isoformat()
    q = ("/rest/v1/web_errors?select=message,source,line,path,browser,build,created_at"
         "&created_at=gte." + urllib.parse.quote(since) + "&order=created_at.desc&limit=5000")
    req = urllib.request.Request(SUPA + q, headers={"apikey": key, "Authorization": "Bearer " + key})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def _when(iso):
    # Postgres drops trailing zeros ("18:16:34.58474"); Python before 3.11
    # only reads 3 or 6 fraction digits, so pad the fraction to six.
    iso = re.sub(r"\.(\d{1,6})", lambda m: "." + m.group(1).ljust(6, "0"), iso.replace("Z", "+00:00"))
    return datetime.datetime.fromisoformat(iso)


# Errors thrown by software that is not ours, inside the visitor's browser:
# wallet extensions (window.ethereum), Firefox iOS reader mode (__firefox__),
# Chrome iOS's injected bridge (__gCrWeb), DarkReader, extension messaging.
# They arrive from the page's "inline" source because the injected script runs
# in the page. Read 2026-11-15, when 36 window.ethereum reports on 15 pages
# lit the quality line red for a fault no change of ours could fix.
FOREIGN = re.compile(
    r"window\.ethereum|__firefox__|__gCrWeb|DarkReader|runtime\.sendMessage"
    r"|Unable to load image data:image/svg\+xml|Can't find variable: ResizeObserver"
    # a fetch that died on the visitor's own connection (offline, tab closed,
    # a request cancelled by navigation), the same in every browser's words
    r"|NetworkError when attempting to fetch resource|^TypeError: (Failed to fetch|Load failed)$",
    re.I)


def is_foreign(message):
    return bool(FOREIGN.search(message or ""))


# Every browser words the same fault its own way, so one bug read as three
# types and none reached the red line (2026-11-25: "el is null" came as
# Chrome's "Cannot read properties of null (reading 'getBoundingClientRect')"
# and Safari's "null is not an object (evaluating 'el.getBoundingClientRect')",
# 3 reports on 3 city pages in a day, two orange types). One wording for all.
_SAME_FAULT = [
    # Chrome: Cannot read properties of null (reading 'x')
    (re.compile(r"Cannot read propert(?:y|ies) of (null|undefined) \(reading '([^']+)'\)"),
     lambda m: "%s has no property '%s'" % (m.group(1), m.group(2))),
    # Safari: null is not an object (evaluating 'a.b.x')
    (re.compile(r"(null|undefined) is not an object \(evaluating '(?:[^']*\.)?([^'.]+)'\)"),
     lambda m: "%s has no property '%s'" % (m.group(1), m.group(2))),
    # Firefox: can't access property "x", a.b is null
    (re.compile(r"can't access property \"([^\"]+)\", \S+ is (null|undefined)"),
     lambda m: "%s has no property '%s'" % (m.group(2), m.group(1))),
]


def normalise(message):
    """The message in one wording whatever the browser: no "Uncaught " in
    front (Chrome's window.onerror adds it), null and undefined reads alike."""
    m = re.sub(r"^Uncaught ", "", (message or "").strip())
    for pattern, say in _SAME_FAULT:
        hit = pattern.search(m)
        if hit:
            return "TypeError: " + say(hit)
    return m


def group(rows, now=None):
    """One dict per type: last-24h reports and pages, the week before, newest."""
    now = now or datetime.datetime.now(datetime.timezone.utc)
    cut = now - datetime.timedelta(hours=24)
    types = {}
    for r in rows:
        if is_foreign(r.get("message")):
            continue
        k = (normalise(r.get("message")), r.get("source") or "")
        t = types.setdefault(k, {"message": k[0], "source": k[1], "day": 0, "pages": set(),
                                 "before": 0, "browsers": set(), "last": ""})
        when = _when(r["created_at"])
        if when >= cut:
            t["day"] += 1
            t["pages"].add(r.get("path") or "")
        else:
            t["before"] += 1
        t["browsers"].add(r.get("browser") or "")
        t["last"] = max(t["last"], r["created_at"])
    out = list(types.values())
    for t in out:
        t["new"] = t["day"] > 0 and t["before"] == 0
        wide = len(t["pages"]) >= RED_PAGES or t["day"] >= RED_REPORTS
        # A known type that fires more in one day than in the whole week
        # before is a fault getting worse, not background noise: it was seen
        # once before, so it never counted as new and never turned red.
        t["rising"] = not t["new"] and t["day"] > t["before"]
        t["spreading"] = wide and (t["new"] or t["rising"])
    out.sort(key=lambda t: (-t["spreading"], -t["new"], -t["day"], -t["before"]))
    return out


def light():
    """(colour, reason) for the quality line's Web "Live" cell."""
    key = load_key()
    if not key:
        return "grey", "no database key here"
    try:
        rows = fetch(key)
    except urllib.error.HTTPError as e:
        if e.code in (404, 400):
            return "grey", "web errors not connected yet (paste supabase/web-errors.sql)"
        return "grey", "error table unreadable (HTTP %d)" % e.code
    except Exception as e:
        return "grey", "error table unreadable (%s)" % str(e)[:60]
    types = group(rows)
    spreading = [t for t in types if t["spreading"]]
    new = [t for t in types if t["new"]]
    if spreading:
        t = spreading[0]
        return "red", "%s error spreading: \"%s\" in %s, %d reports on %d pages" % (
            "new" if t["new"] else "known", t["message"][:60], t["source"] or "?", t["day"], len(t["pages"]))
    if new:
        t = new[0]
        return "orange", "%d new error type(s), first \"%s\" in %s" % (
            len(new), t["message"][:60], t["source"] or "?")
    firing = sum(1 for t in types if t["day"])
    return "green", ("no new errors" + (", %d known type(s) still firing" % firing if firing else ""))


def delete(key, where):
    """DELETE rows matching a PostgREST filter; returns how many went."""
    req = urllib.request.Request(SUPA + "/rest/v1/web_errors?" + where, method="DELETE",
                                 headers={"apikey": key, "Authorization": "Bearer " + key,
                                          "Prefer": "return=representation"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return len(json.load(r))


def prune(key):
    """Rows older than KEEP_DAYS go, and any row a test left (message starts TEST web_errors)."""
    cut = (datetime.datetime.now(datetime.timezone.utc)
           - datetime.timedelta(days=KEEP_DAYS)).isoformat()
    old = delete(key, "created_at=lt." + urllib.parse.quote(cut))
    tests = delete(key, "message=like." + urllib.parse.quote("TEST web_errors*"))
    return old, tests


def main():
    if "--prune" in sys.argv:
        key = load_key()
        if not key:
            print("web_errors: SUPABASE_SERVICE_KEY not set")
            return 1
        try:
            old, tests = prune(key)
        except urllib.error.HTTPError as e:
            print("web_errors: prune failed (HTTP %d)" % e.code)
            return 1
        print("web_errors: removed %d row(s) older than %d days, %d test row(s)" % (old, KEEP_DAYS, tests))
        return 0
    if "--light" in sys.argv:
        print("%s: %s" % light())
        return 0
    key = load_key()
    if not key:
        print("web_errors: SUPABASE_SERVICE_KEY not set")
        return 1
    try:
        rows = fetch(key)
    except urllib.error.HTTPError as e:
        print("web_errors: the table is not there yet (HTTP %d); paste supabase/web-errors.sql" % e.code)
        return 1
    types = group(rows)
    if not types:
        print("web_errors: no errors in the last 8 days")
        return 0
    print("%-6s %5s %5s %6s  %-28s %s" % ("", "24h", "pages", "before", "source", "message"))
    for t in types:
        tag = "RED" if t["spreading"] else ("new" if t["new"] else "")
        print("%-6s %5d %5d %6d  %-28s %s" % (tag, t["day"], len(t["pages"]), t["before"],
                                              t["source"][:28], t["message"][:90]))
    print("\n%s: %s" % light())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
