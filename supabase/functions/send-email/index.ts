// Supabase Auth "Send Email" hook: every sign-in and welcome mail passes here.
//
// Why (Hidde, 2026-11-15): Supabase sent its auth mails through his Gmail
// wearing info@ancienttrees.app. Gmail signs for gmail.com, never for our
// domain, and Yahoo (and AOL, on Yahoo's servers) refuse such mail outright:
// "550 5.7.9 ... Yahoo requires this sender to authenticate with DKIM". Six
// new accounts on the Guardian day never got their welcome mail. Resend signs
// for ancienttrees.app, but its free plan stops at 100 mails a day, and that
// day had 71 email sign-ups in four hours: moving everything there would break
// sign-up for everyone on the next press day. Resend Pro was too dear.
//
// Since 2026-11-20 (Resend Pro) every mail here goes through Resend first;
// see RESEND_FIRST below. The split this replaced:
// Yahoo-family addresses (a few a day) go through Resend, signed;
// everyone else keeps going through Gmail exactly as before (SMTP on 465;
// Supabase's Edge Functions block 25 and 587). If one route fails the mail
// tries the other, so a hiccup on either side still reaches the person.
//
// Secrets (Edge Functions > Secrets): SEND_EMAIL_HOOK_SECRET (from Auth > Hooks,
// "v1,whsec_..."), RESEND_API_KEY, GMAIL_USER, GMAIL_APP_PASSWORD.
// Undo: Auth > Hooks > Send Email off. Supabase falls back to its SMTP setting,
// which still points at Gmail.

import { Webhook } from "npm:standardwebhooks@1.0.0";
import nodemailer from "npm:nodemailer@6.9.16";

const FROM = "Ancient Trees <info@ancienttrees.app>";
const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
// The same list as YAHOO_FAMILY in scripts/mailer.py (qa's
// check_one_mail_route_rule() keeps them equal). Every mail this hook sends is
// one the person asked for, so only these addresses go through Resend.
const YAHOO_FAMILY = ["yahoo", "ymail", "rocketmail", "aol", "aim", "verizon", "att",
  "sbcglobal", "bellsouth", "frontier", "sky"];
// Apple's relay forwards only mail signed for a registered domain (bounces of
// 2026-11-17); same list as SIGNED_ONLY_DOMAINS in scripts/mailer.py. BT's
// addresses too: a Gmail-sent welcome was refused "550 User unknown" the same
// evening while a plain Gmail mail to that address was taken.
const SIGNED_ONLY_DOMAINS = ["privaterelay.appleid.com", "btinternet.com", "btopenworld.com", "talk21.com"];
const onYahoo = (addr: string) => {
  const domain = addr.trim().toLowerCase().split("@").pop()!;
  return YAHOO_FAMILY.includes(domain.split(".")[0]) || SIGNED_ONLY_DOMAINS.includes(domain);
};

// AN ADDRESS THAT CANNOT RECEIVE MAIL IS REFUSED BEFORE ANY ACCOUNT WAITS ON IT
// (Hidde, 2026-11-18, after a welcome mail to "hoymail.com" sat retrying for a
// day: "it doesnt stop people from making the mistake"; CONVENTIONS.md "A
// mistyped email address", layer 3). "Did you mean ...?" under the field only
// warns, and a second Send went out as typed. The convention for a hard stop
// is a mail-server lookup at sign-up: a domain that can receive no mail is
// refused. hoymail.com has no mail server but does point at a web server, and
// mail may fall back to that (RFC 5321), so a plain lookup lets it through.
// So the rule: refused when the domain has no mail server AND it is a typo of
// a provider on our list (the same "Did you mean" rule as the field), or when
// the domain resolves to nothing at all. Anything else, or a lookup that fails
// or is slow, goes out as before: never refuse a real address on a hiccup.
// Every surface sends its link through this hook, so web, iPhone and Android
// (old builds too) are held the same way, and each already shows the
// suggestion under the field. The refusal's message is "undeliverable:<the
// corrected address or nothing>", which the sign-in screens read.
// DOMAINS-BEGIN (a copy of data/email-domains.json; qa's check_one_email_domain_list())
const DOMAINS = [
  "gmail.com", "googlemail.com",
  "outlook.com", "outlook.fr", "outlook.de", "outlook.es", "outlook.it", "outlook.pt",
  "hotmail.com", "hotmail.co.uk", "hotmail.fr", "hotmail.de", "hotmail.es", "hotmail.it", "hotmail.nl", "hotmail.be",
  "live.com", "live.co.uk", "live.nl", "live.fr", "live.be", "msn.com",
  "yahoo.com", "yahoo.co.uk", "yahoo.fr", "yahoo.de", "yahoo.es", "yahoo.it", "yahoo.gr", "yahoo.com.au", "ymail.com", "rocketmail.com",
  "icloud.com", "me.com", "mac.com",
  "aol.com", "aol.co.uk",
  "protonmail.com", "proton.me", "pm.me",
  "gmx.com", "gmx.de", "gmx.net", "gmx.at", "gmx.ch", "web.de", "t-online.de", "freenet.de",
  "mail.com", "zoho.com", "fastmail.com",
  "btinternet.com", "sky.com", "virginmedia.com", "talktalk.net", "ntlworld.com",
  "ziggo.nl", "kpnmail.nl", "xs4all.nl", "planet.nl", "home.nl", "hetnet.nl", "telenet.be", "skynet.be",
  "orange.fr", "free.fr", "laposte.net", "sfr.fr", "wanadoo.fr",
  "libero.it", "tiscali.it", "virgilio.it", "alice.it",
  "sapo.pt", "telefonica.net",
  "comcast.net", "verizon.net", "att.net", "sbcglobal.net", "bellsouth.net", "cox.net", "charter.net",
  "bigpond.com", "optusnet.com.au", "shaw.ca", "rogers.com", "sympatico.ca",
  "naver.com", "qq.com", "163.com", "yandex.com",
];
// DOMAINS-END

function dist(a: string, b: string) {
  let prev = Array.from({ length: b.length + 1 }, (_, j) => j);
  for (let i = 1; i <= a.length; i++) {
    const cur = [i];
    for (let j = 1; j <= b.length; j++) {
      cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
    }
    prev = cur;
  }
  return prev[b.length];
}

// The listed domain this one is a typo of, by the field's rule
// (site/src/lib/email-suggest.ts): nearest by edit distance, at most 2 apart
// (1 for six letters or fewer), never on a tie, never for a listed domain.
export function typoOf(dom: string): string | null {
  if (DOMAINS.includes(dom)) return null;
  let best: string | null = null, bestD = 99, tie = false;
  for (const d of DOMAINS) {
    const n = dist(dom, d);
    if (n < bestD) { bestD = n; best = d; tie = false; } else if (n === bestD) tie = true;
  }
  return best && !tie && bestD <= (dom.length <= 6 ? 1 : 2) ? best : null;
}

// "yes", "no" or "unknown" (an error that is not "no such record", or slow).
async function has(dom: string, type: "MX" | "A" | "AAAA"): Promise<"yes" | "no" | "unknown"> {
  const timeout = new Promise<"unknown">((ok) => setTimeout(() => ok("unknown"), 2500));
  const look = (async () => {
    try {
      const recs = await Deno.resolveDns(dom, type) as unknown[];
      // A null MX ("0 .", RFC 7505) says the domain takes no mail.
      if (type === "MX" && recs.every((r: any) => !r.exchange || r.exchange === "." || r.exchange === "")) return "no";
      return recs.length ? "yes" : "no";
    } catch (e) {
      return e instanceof Deno.errors.NotFound ? "no" : "unknown";
    }
  })();
  return await Promise.race([look, timeout]);
}

// A HARD TYPO OF A BIG PROVIDER IS REFUSED EVEN WHEN ITS DOMAIN TAKES MAIL
// (Hidde, 2026-11-20, "ok doe"): outlook.co has a mail server (Microsoft's),
// so the lookup above let it through and the welcome bounced; the reader
// never got in. Refused: the provider's name misspelt (hoymail, tahoo, gmial)
// or ".com" itself mistyped (outlook.co, gmail.con), for Gmail, Outlook,
// Hotmail, Live, Yahoo and iCloud only. A different country ending (yahoo.dk,
// live.ie, outlook.be) is a real domain and only gets the field's warning.
// Checked against all 882 accounts that day: it would have refused the three
// that never got in (hoymail.com, outlook.co, tahoo.com) and nobody who did.
const BIG = /^(gmail\.com|googlemail\.com|outlook\.|hotmail\.|live\.|yahoo\.|ymail\.com|icloud\.com)/;
export function hardTypo(dom: string): string | null {
  const fix = typoOf(dom);
  if (!fix || !BIG.test(fix)) return null;
  const [n1, t1] = [dom.slice(0, dom.indexOf(".")), dom.slice(dom.indexOf(".") + 1)];
  const [n2, t2] = [fix.slice(0, fix.indexOf(".")), fix.slice(fix.indexOf(".") + 1)];
  if (n1 !== n2) return fix;
  if (t2 === "com" && dist(t1, "com") <= 1) return fix;
  return null;
}

// null when the address may receive mail, else the corrected address or "".
export async function undeliverable(addr: string): Promise<string | null> {
  const at = addr.lastIndexOf("@");
  if (at < 1) return null;
  const dom = addr.slice(at + 1).trim().toLowerCase();
  if (!dom || DOMAINS.includes(dom)) return null;
  const hard = hardTypo(dom);
  if (hard) return addr.slice(0, at).trim() + "@" + hard;
  if ((await has(dom, "MX")) !== "no") return null;
  const fix = typoOf(dom);
  if (fix) return addr.slice(0, at).trim() + "@" + fix;
  const [a, aaaa] = await Promise.all([has(dom, "A"), has(dom, "AAAA")]);
  return a === "no" && aaaa === "no" ? "" : null;
}

const gmail = nodemailer.createTransport({
  host: "smtp.gmail.com",
  port: 465,
  secure: true,
  auth: { user: Deno.env.get("GMAIL_USER"), pass: Deno.env.get("GMAIL_APP_PASSWORD") },
});

function esc(s: string) {
  return s.replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");
}

// The dashboard's own templates (Authentication > Emails), copied in verbatim
// by scripts/mail_hook_templates.py, which reads them through the Management
// API: with the hook on, Supabase no longer renders them itself. Edit a
// template in the dashboard, then run that script and redeploy.
// TEMPLATES-BEGIN
const TEMPLATES: Record<string, { subject: string; html: string }> = {
  "confirmation": {
    "subject": "Welcome to Ancient Trees",
    "html": "<div style=\"font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;max-width:480px;margin:0 auto;padding:32px 24px;color:#2b2b24;background:#faf8f2\">\n  <p style=\"margin:0 0 24px;font-size:15px;font-weight:600;color:#3A5222\">Ancient Trees</p>\n  <p style=\"margin:0 0 16px;font-size:20px;line-height:1.35;font-weight:600\">Welcome. Your account is almost ready.</p>\n  <p style=\"margin:0 0 24px;font-size:17px;line-height:1.5\">Tap the button to confirm your email. After that, the trees you save and the ones you tick off follow you from your phone to your laptop.</p>\n  <p style=\"margin:0 0 28px\">\n    <a href=\"{{ .ConfirmationURL }}\" style=\"display:inline-block;background:#4A6B2A;color:#ffffff;text-decoration:none;font-size:16px;font-weight:600;padding:14px 28px;border-radius:999px\">Confirm my email</a>\n  </p>\n  <p style=\"margin:0 0 24px;font-size:15px;line-height:1.5\">Then open the map and see which old trees stand near you.</p>\n  <p style=\"margin:0;font-size:13px;line-height:1.5;color:#6b6b60\">If you did not create an account, you can ignore this mail.</p>\n</div>"
  },
  "magic_link": {
    "subject": "Your Ancient Trees sign-in link",
    "html": "<div style=\"font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;max-width:480px;margin:0 auto;padding:32px 24px;color:#2b2b24;background:#faf8f2\">\n  <p style=\"margin:0 0 24px;font-size:15px;font-weight:600;color:#3A5222\">Ancient Trees</p>\n  <p style=\"margin:0 0 20px;font-size:17px;line-height:1.5\">Tap the button to sign in.</p>\n  <p style=\"margin:0 0 24px\">\n    <a href=\"{{ .ConfirmationURL }}\" style=\"display:inline-block;background:#4A6B2A;color:#ffffff;text-decoration:none;font-size:16px;font-weight:600;padding:14px 28px;border-radius:999px\">Sign in</a>\n  </p>\n  <p style=\"margin:0;font-size:13px;line-height:1.5;color:#6b6b60\">The link works once and expires after a short while. If you did not ask to sign in, you can ignore this mail.</p>\n</div>"
  },
  "recovery": {
    "subject": "Reset your password",
    "html": "<h2>Reset your password</h2>\n\n<p>We received a request to reset your password. Follow the link below to choose a new one.</p>\n<p><a href=\"{{ .ConfirmationURL }}\">Reset password</a></p>\n\n<p>If you didn't request this, you can safely ignore this email.</p>"
  },
  "invite": {
    "subject": "You've been invited",
    "html": "<h2>You've been invited</h2>\n\n<p>You've been invited to create an account. Follow the link below to accept.</p>\n<p><a href=\"{{ .ConfirmationURL }}\">Accept invitation</a></p>"
  },
  "email_change": {
    "subject": "Confirm your new email address",
    "html": "<h2>Confirm your new email address</h2>\n\n<p>Follow the link below to confirm {{ .NewEmail }} as your new email address.</p>\n<p><a href=\"{{ .ConfirmationURL }}\">Confirm new email address</a></p>\n\n<p>If you didn't request this change, you can safely ignore this email.</p>"
  },
  "reauthentication": {
    "subject": "{{ .Token }} is your verification code",
    "html": "<h2>Your verification code</h2>\n\n<p>Use the code below to verify your identity. It expires shortly.</p>\n\n<p>{{ .Token }}</p>"
  }
};
// TEMPLATES-END

// Supabase's email_action_type -> the dashboard template it used to send.
const KIND: Record<string, string> = {
  signup: "confirmation", magiclink: "magic_link", recovery: "recovery",
  invite: "invite", email_change: "email_change", email: "magic_link",
  reauthentication: "reauthentication",
};

function render(kind: string, url: string, token: string, email: string) {
  const t = TEMPLATES[KIND[kind] || "magic_link"];
  const fill = (s: string) => s
    .replace(/\{\{\s*\.ConfirmationURL\s*\}\}/g, esc(url))
    .replace(/\{\{\s*\.Token\s*\}\}/g, esc(token || ""))
    .replace(/\{\{\s*\.(NewEmail|Email)\s*\}\}/g, esc(email))
    .replace(/\{\{\s*\.SiteURL\s*\}\}/g, "https://ancienttrees.app");
  return { subject: fill(t.subject), html: fill(t.html) };
}

async function viaResend(to: string, subject: string, html: string) {
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${Deno.env.get("RESEND_API_KEY")}`, "Content-Type": "application/json" },
    body: JSON.stringify({ from: FROM, to: [to], subject, html }),
  });
  if (!r.ok) throw new Error(`resend ${r.status} ${(await r.text()).slice(0, 200)}`);
}

async function viaGmail(to: string, subject: string, html: string) {
  await gmail.sendMail({ from: FROM, to, subject, html });
}

Deno.serve(async (req) => {
  const payload = await req.text();
  const secret = (Deno.env.get("SEND_EMAIL_HOOK_SECRET") || "").replace("v1,whsec_", "");
  let user: { email: string; new_email?: string }, email_data: {
    token: string; token_hash: string; redirect_to: string; email_action_type: string; site_url: string;
  };
  try {
    ({ user, email_data } = new Webhook(secret).verify(payload, Object.fromEntries(req.headers)) as any);
  } catch (_e) {
    return new Response(JSON.stringify({ error: { http_code: 401, message: "bad signature" } }),
      { status: 401, headers: { "Content-Type": "application/json" } });
  }

  const kind = email_data.email_action_type;
  const url = `${SUPABASE_URL}/auth/v1/verify?token=${encodeURIComponent(email_data.token_hash)}` +
    `&type=${encodeURIComponent(kind)}&redirect_to=${encodeURIComponent(email_data.redirect_to || email_data.site_url || "https://ancienttrees.app")}`;
  const { subject, html } = render(kind, url, email_data.token, user.new_email || user.email);
  const to = user.email;
  // Only the mails a person waits on to get in; a password reset or invite to
  // an account that already exists goes out as before.
  if (["signup", "magiclink", "email"].includes(kind)) {
    const fix = await undeliverable(to);
    if (fix !== null) {
      console.log("refused, cannot receive mail", kind, to.split("@").pop());
      // Status 200 with the error in the body: Supabase Auth passes http_code
      // and message on to the sign-in screen only that way (a 422 status came
      // back to the screen as "unexpected status code from hook", 2026-11-18).
      return new Response(JSON.stringify({ error: { http_code: 422, message: "undeliverable:" + fix } }),
        { status: 200, headers: { "Content-Type": "application/json" } });
    }
  }
  // RESEND FIRST FOR EVERY MAIL HERE, FOR NOW (Hidde, 2026-11-20, "for now
  // yes"): that afternoon a mail wave took his Gmail past its daily limit and
  // nobody could sign in. Resend Pro (same day) has no daily cap, so sign-in
  // mail no longer shares Gmail's limit with outreach; Gmail stands in when
  // Resend fails. Back to the split below by setting RESEND_FIRST false.
  const RESEND_FIRST = true;
  const [first, second] = RESEND_FIRST || onYahoo(to) ? [viaResend, viaGmail] : [viaGmail, viaResend];

  try {
    await first(to, subject, html);
  } catch (e1) {
    console.error("first route failed", kind, String(e1).slice(0, 200));
    try {
      await second(to, subject, html);
    } catch (e2) {
      console.error("both routes failed", kind, String(e2).slice(0, 200));
      return new Response(JSON.stringify({ error: { http_code: 500, message: "mail could not be sent" } }),
        { status: 500, headers: { "Content-Type": "application/json" } });
    }
  }
  return new Response("{}", { status: 200, headers: { "Content-Type": "application/json" } });
});
