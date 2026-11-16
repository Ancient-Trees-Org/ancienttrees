#!/usr/bin/env python3
"""Copy Supabase's mail templates from the dashboard into the Send Email hook.

With the hook on (supabase/functions/send-email, 2026-11-16), Supabase no
longer renders its own templates: the hook sends the mail. So the hook carries
the dashboard's subjects and HTML verbatim, between TEMPLATES-BEGIN and
TEMPLATES-END in index.ts. Edit a template in the dashboard, run this, commit,
and redeploy the function.

Needs SUPABASE_ACCESS_TOKEN (a Management API token with Auth Config read) in
~/.ancienttrees-supabase.env or the environment.

    python3 scripts/mail_hook_templates.py
"""
import json
import os
import re
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "supabase", "functions", "send-email", "index.ts")
KINDS = ("confirmation", "magic_link", "recovery", "invite", "email_change", "reauthentication")


def token():
    if os.environ.get("SUPABASE_ACCESS_TOKEN"):
        return os.environ["SUPABASE_ACCESS_TOKEN"]
    for line in open(os.path.expanduser("~/.ancienttrees-supabase.env"), encoding="utf-8"):
        if line.startswith("SUPABASE_ACCESS_TOKEN="):
            return line.split("=", 1)[1].strip().strip('"')
    raise SystemExit("no SUPABASE_ACCESS_TOKEN")


def project_ref():
    src = open(os.path.join(ROOT, "scripts", "inbox.py"), encoding="utf-8").read()
    return re.search(r"https://([a-z0-9]+)\.supabase\.co", src).group(1)


def main():
    req = urllib.request.Request(
        f"https://api.supabase.com/v1/projects/{project_ref()}/config/auth",
        headers={"Authorization": f"Bearer {token()}", "User-Agent": "at-mail-hook"})
    cfg = json.load(urllib.request.urlopen(req, timeout=60))
    tpl = {k: {"subject": cfg[f"mailer_subjects_{k}"], "html": cfg[f"mailer_templates_{k}_content"]}
           for k in KINDS}
    block = ("// TEMPLATES-BEGIN\nconst TEMPLATES: Record<string, { subject: string; html: string }> = "
             + json.dumps(tpl, ensure_ascii=False, indent=2) + ";\n// TEMPLATES-END")
    src = open(INDEX, encoding="utf-8").read()
    new = re.sub(r"// TEMPLATES-BEGIN.*?// TEMPLATES-END", lambda m: block, src, flags=re.S)
    open(INDEX, "w", encoding="utf-8").write(new)
    print("templates written:", ", ".join(f"{k} ({tpl[k]['subject']!r})" for k in KINDS))


if __name__ == "__main__":
    main()
