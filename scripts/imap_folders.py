"""Find a mailbox folder by what it is, not by what it is called.

The scripts were written against the old Gmail, whose folders carry English
names ("[Gmail]/Sent Mail", "[Gmail]/Spam", "[Gmail]/All Mail"). Since
2026-11-23 the mailbox is Workspace (hidde@ancienttrees.app), where the
names follow the account's language, so a hard-coded name selects nothing
and the next SEARCH fails ("illegal in state AUTH", digest run of
2026-11-24). Every IMAP server marks these folders with a special-use flag
(RFC 6154: \\Sent, \\Junk, \\All), so we look the flag up and keep the old
name only as the fallback.

    from imap_folders import folder
    d.select(folder(d, '"[Gmail]/Sent Mail"'), readonly=True)
"""

import re

FLAGS = {
    "[gmail]/sent mail": b"\\Sent",
    "[gmail]/spam": b"\\Junk",
    "[gmail]/all mail": b"\\All",
}

_cache = {}


def folder(imap, name):
    """The quoted name of the folder that plays the role of `name` on this
    server. INBOX and unknown names come back unchanged; a server that will
    not LIST gets the old name back."""
    flag = FLAGS.get(name.strip('"').lower())
    if not flag:
        return name
    key = (id(imap), flag)
    if key in _cache:
        return _cache[key]
    found = name
    try:
        ok, rows = imap.list()
        for row in rows if ok == "OK" else []:
            if not isinstance(row, bytes):
                continue
            m = re.match(rb'\((?P<flags>[^)]*)\) (?:"[^"]*"|NIL) (?P<name>.+)$', row)
            if m and flag in m.group("flags").split():
                n = m.group("name").decode("utf-8", "replace").strip()
                found = n if n.startswith('"') else '"%s"' % n
                break
    except Exception:
        pass
    _cache[key] = found
    return found
