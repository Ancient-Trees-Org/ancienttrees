#!/usr/bin/env python3
"""A SQL file for Hidde to paste names only columns that exist.

2026-11-27: profile-newest-first.sql sorted by `sightings.created_at`, a column
the table never had (it has taken_at), and Hidde's paste failed in the SQL
editor. Nothing here could see it: sqlcheck.py asks whether a file reached the
database, not whether it can.

This reads every `create table` and `add column` in supabase/*.sql to learn
each public table's columns, then, in each file, every `public.<table> <alias>`
and every `<alias>.<column>` that uses that alias, and names a column the table
does not have. Offline and mechanical: no key, no database.

    python3 scripts/sqlcolumns.py [files...]   # default: every supabase/*.sql

Exit 1 when a file names a missing column.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQL_KW = {"constraint", "primary", "unique", "check", "foreign", "exclude", "like"}


def strip_comments(s):
    return re.sub(r"--[^\n]*", "", s)


def known_columns(files):
    cols = {}
    for f in files:
        s = strip_comments(open(f, encoding="utf-8").read())
        for m in re.finditer(r"create table (?:if not exists )?public\.(\w+)\s*\(", s, re.I):
            depth, i, start = 1, m.end(), m.end()
            while i < len(s) and depth:
                depth += {"(": 1, ")": -1}.get(s[i], 0)
                i += 1
            body, part, d = s[start:i - 1], "", 0
            parts = []
            for ch in body:
                if ch == "(":
                    d += 1
                elif ch == ")":
                    d -= 1
                if ch == "," and d == 0:
                    parts.append(part)
                    part = ""
                else:
                    part += ch
            parts.append(part)
            for p in parts:
                w = p.strip().split()
                if w and w[0].lower() not in SQL_KW:
                    cols.setdefault(m.group(1).lower(), set()).add(w[0].strip('"').lower())
    created = set(cols)
    for f in files:
        s = strip_comments(open(f, encoding="utf-8").read())
        for m in re.finditer(r"alter table (?:if exists )?(?:only )?public\.(\w+)((?:[^;])*);", s, re.I):
            for c in re.finditer(r"add column (?:if not exists )?(\w+)", m.group(2), re.I):
                cols.setdefault(m.group(1).lower(), set()).add(c.group(1).lower())
    # A table made before the repo (submissions, made in the dashboard) has
    # only its later columns on file: judging it would cry wolf.
    return {t: c for t, c in cols.items() if t in created}


def problems(path, cols):
    s = strip_comments(open(path, encoding="utf-8").read())
    out = []
    aliases = {}
    for m in re.finditer(r"\bpublic\.(\w+)\s+(?:as\s+)?([a-z_]\w*)\b", s, re.I):
        table, alias = m.group(1).lower(), m.group(2).lower()
        if table in cols and alias not in {"where", "on", "set", "using", "for", "to", "from",
                                           "enable", "add", "join", "order", "group", "limit",
                                           "returning", "values", "select", "is", "owner",
                                           "drop", "alter", "and", "or", "as", "in", "with",
                                           "cascade", "inner", "left", "union", "default"}:
            aliases.setdefault(alias, set()).add(table)
    for alias, tables in aliases.items():
        if len(tables) != 1:
            continue                      # one alias for two tables: too clever to judge
        table = next(iter(tables))
        for m in re.finditer(r"\b%s\.(\w+)" % re.escape(alias), s, re.I):
            col = m.group(1).lower()
            if col not in cols[table] and col != "*":
                line = s[:m.start()].count("\n") + 1
                out.append("%s:%d  %s.%s: public.%s has no column %s"
                           % (os.path.relpath(path, ROOT), line, alias, col, table, col))
    return sorted(set(out))


def main(argv):
    every = sorted(glob.glob(os.path.join(ROOT, "supabase", "*.sql")))
    files = [os.path.abspath(a) for a in argv if a.endswith(".sql")] or every
    cols = known_columns(every)
    bad = [p for f in files for p in problems(f, cols)]
    for b in bad:
        print(b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
