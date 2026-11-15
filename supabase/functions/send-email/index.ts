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
const YAHOO = /@(yahoo|ymail|rocketmail|aol|aim|verizon|att|sbcglobal|bellsouth|frontier)\.[a-z.]+$/i;

const gmail = nodemailer.createTransport({
  host: "smtp.gmail.com",
  port: 465,
  secure: true,
  auth: { user: Deno.env.get("GMAIL_USER"), pass: Deno.env.get("GMAIL_APP_PASSWORD") },
});

function esc(s: string) {
  return s.replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");
}

// The two templates of drafts/auth-mails.md, as they stood in the dashboard.
function render(kind: string, url: string): { subject: string; html: string } {
  const a = esc(url);
  const wrap = (inner: string) =>
    `<div style="font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;max-width:480px;margin:0 auto;padding:32px 24px;color:#2b2b24;background:#faf8f2">` +
    `<p style="margin:0 0 24px;font-size:15px;font-weight:600;color:#3A5222">Ancient Trees</p>${inner}</div>`;
  const button = (label: string, gap = 24) =>
    `<p style="margin:0 0 ${gap}px"><a href="${a}" style="display:inline-block;background:#4A6B2A;color:#ffffff;text-decoration:none;font-size:16px;font-weight:600;padding:14px 28px;border-radius:999px">${label}</a></p>`;
  if (kind === "signup" || kind === "invite") {
    return {
      subject: "Welcome to Ancient Trees",
      html: wrap(
        `<p style="margin:0 0 16px;font-size:20px;line-height:1.35;font-weight:600">Welcome. Your account is almost ready.</p>` +
        `<p style="margin:0 0 24px;font-size:17px;line-height:1.5">Tap the button to confirm your email. After that, the trees you save and the ones you tick off follow you from your phone to your laptop.</p>` +
        button("Confirm my email", 28) +
        `<p style="margin:0 0 24px;font-size:15px;line-height:1.5">Then open the map and see which old trees stand near you.</p>` +
        `<p style="margin:0;font-size:13px;line-height:1.5;color:#6b6b60">If you did not create an account, you can ignore this mail.</p>`),
    };
  }
  const subject = kind === "email_change" ? "Confirm your new email address"
    : kind === "recovery" ? "Your Ancient Trees sign-in link"
    : "Your Ancient Trees sign-in link";
  const label = kind === "email_change" ? "Confirm" : "Sign in";
  return {
    subject,
    html: wrap(
      `<p style="margin:0 0 20px;font-size:17px;line-height:1.5">Tap the button to ${kind === "email_change" ? "confirm this address" : "sign in"}.</p>` +
      button(label) +
      `<p style="margin:0;font-size:13px;line-height:1.5;color:#6b6b60">The link works once and expires after a short while. If you did not ask for it, you can ignore this mail.</p>`),
  };
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
  let user: { email: string }, email_data: {
    token_hash: string; redirect_to: string; email_action_type: string;
  };
  try {
    ({ user, email_data } = new Webhook(secret).verify(payload, Object.fromEntries(req.headers)) as any);
  } catch (_e) {
    return new Response(JSON.stringify({ error: { http_code: 401, message: "bad signature" } }),
      { status: 401, headers: { "Content-Type": "application/json" } });
  }

  const kind = email_data.email_action_type;
  const url = `${SUPABASE_URL}/auth/v1/verify?token=${encodeURIComponent(email_data.token_hash)}` +
    `&type=${encodeURIComponent(kind)}&redirect_to=${encodeURIComponent(email_data.redirect_to || "")}`;
  const { subject, html } = render(kind, url);
  const to = user.email;
  const [first, second] = YAHOO.test(to) ? [viaResend, viaGmail] : [viaGmail, viaResend];

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
