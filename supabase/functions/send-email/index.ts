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
// So the split: Yahoo-family addresses (a few a day) go through Resend, signed;
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
  "sbcglobal", "bellsouth", "frontier"];
const onYahoo = (addr: string) =>
  YAHOO_FAMILY.includes(addr.trim().toLowerCase().split("@").pop()!.split(".")[0]);

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
  const [first, second] = onYahoo(to) ? [viaResend, viaGmail] : [viaGmail, viaResend];

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
