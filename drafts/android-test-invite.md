# FOR HIDDE: the Android test invitation to the waitlist (2026-11-17)

Who: the `waitlist` table, almost all from the Android download button on the
site (1,897 of 1,919), promised a mail when the Android app exists. Hidde,
2026-11-17: ask them to join the closed test, and tell them what to expect.

Two waves, agreed in chat the same evening:
1. About 200 newest Gmail addresses, the moment Google approves the first
   closed-test build (a Gmail address is a Google account, so they join with
   one tap).
2. The other ~1,700 a few days later, with the build that fixes what wave 1
   found. Spread over several days to stay under the sending limits.

**WAVE 3, prepared 2026-11-20 (Hidde: "Yes, prepare it", then "what ever you think works"): through a Google Group, not the e-mail list.**
Play's tester list refuses some addresses with no reason (two in wave 3's first
50; probably not Google accounts), so finding each one by halving would take
hundreds of saves. Instead: the Google Group **groups.google.com/g/ancienttrees-android-testers**
(anyone can join, findable on the web, members list for managers only, posting
and conversations owners only; its info page shows Hidde as owner with his
Gmail address) is the tester list of a **second closed track, "Beta (Google
Group)"**, with the same build 4, all countries. Play allows one access method
per track, so Alpha keeps its e-mail list (485, including wave 3 lines 1 to 11)
untouched. The Beta release was saved for review on 2026-11-20 and waits for
Hidde's "indienen voor beoordeling" click. New testers need Beta approved.
Batch: drafts/batches/android-test-invite-wave3-2026-11-20.json (gitignored),
777 Gmail addresses (out/play/wave3.csv minus the line Play refused), status
draft, same text plus the group step:
"You can sign up to be a tester in two steps, with the Google account of this email address:
1. Join the tester group: https://groups.google.com/g/ancienttrees-android-testers
2. Then sign up here: https://play.google.com/apps/testing/app.ancienttrees.android"
Send only after Play shows the Beta release approved, on Hidde's "verstuur",
about 170 a day: `OUTREACH_DAILY_CAP=170 python3 out/tmp/send_with_mail_env.py drafts/batches/android-test-invite-wave3-2026-11-20.json --send`
on three to five days in a row (re-running skips who already had it).
Later waves: just mail the same text; nobody has to be added to Play by hand.

**WAVE 2 SENT IN PART, 2026-11-19:** Play's list now holds 474 (wave 1's
172, Lisa and Genziana from the private tester list, and the first 300 of
wave2.csv; Play refused 400 and 500 at once, so a bad address sits in
wave2.csv lines 301 to 400). Mailed: 230 of those 300 through Gmail; the
day's cap held the rest. **Send the remainder on 2026-11-20**, same command:
`OUTREACH_DAILY_CAP=400 python3 out/tmp/send_with_mail_env.py drafts/batches/android-test-invite-wave2-2026-11-19.json --send`
(it skips everyone already sent). Lisa and Genziana get a personal reply in
their own thread, not this text (they did not sign up for the waitlist).

**WAVE 2, agreed 2026-11-19 (Hidde: "shouldnt we invite more?", then "ok"):**
the next 500 Gmail addresses, newest first, in out/play/wave2.csv (gitignored,
built by out/tmp/wave2_csv.py; 543 Gmail addresses remain after it). Only
once version 3 (the Google Maps fix) is approved on the Alpha track. Steps: add
the 500 to "Ancient Trees testers" (a CSV replaces the list, so upload
wave1 list + wave2 together, in steps, leaving out any chunk Play refuses),
build a batch from exactly what Play accepted, same text, kind expected,
send. Non-Gmail addresses wait for the public launch mail.
**Send it over three days, about 170 a day** (Hidde, 2026-11-19, "Yes, split
it"): Gmail stops at about 500 a day, and replies, photo-live and welcome mail
share that route, so 500 in one day would fill Gmail, then Resend (the
fallback), and Yahoo, Apple and BT sign-ins would bounce. Run the batch with
OUTREACH_DAILY_CAP=170 on three days in a row; re-running skips who already had it.

**SENT 2026-11-19, on Hidde's "stuur maar gewoon uit":** 100 of the 172 went
out on 2026-11-19, and the other 68 the same afternoon through Gmail on his "kunnen we niet gewoon via gmail sturen?" (batch kind expected, OUTREACH_DAILY_CAP=200 for that run). Batch drafts/batches/android-test-invite-2026-11-19.json, gitignored,
every send in the private data/outreach-sent.json). Re-running the batch skips everyone already sent: `python3 out/tmp/send_with_mail_env.py drafts/batches/android-test-invite-2026-11-19.json --send`
(it loads ~/.ancienttrees-mail.env and runs outreach_send.py). Four addresses
had another mail from us in the past week and were skipped under the one-week
rest; they can go from 2026-11-24 with the same batch.

**STATUS 2026-11-18: version 2 is uploaded to the closed test "Alpha" and is
with Google for review** (sent 18 November, by the "App crashes" session and
Hidde). Both lists, "Ancient Trees team" and "Ancient Trees testers", are on
the track, so those people get access the moment Google approves. Feedback
goes to info@ancienttrees.app. **Send nothing until Play shows the release
approved** (Testing > Closed testing > Alpha: no longer "In review"); then
step 4 below, on Hidde's "verstuur".
**Wave 1 is 172 people** (Hidde, 2026-11-18: "lets do 200"): the exact list in
Play is out/play/on-play-list.csv on the Mac (gitignored). Mail exactly those
and nobody else. Play refused a few of the 200 newest Gmail addresses without
saying why (most likely no Google account behind them): wave1.csv lines 60
to 62 (out/play/refused.txt) and one of lines 176 to 200, so lines 176 to 200
were left out. Nothing for a session to chase.

**The text below is Hidde's own (2026-11-17) and is agreed. It waits only for
Google's approval.** The order, once he says go:
1. A session rebuilds the .aab (`python3 scripts/android_release.py`).
2. Hidde uploads it to Closed testing (33 MB, too big for the Chrome upload
   tool) and picks "Use Google-generated key".
3. Google reviews it: hours to a few days, up to a week for a new app.
4. The session puts the wave 1 addresses on the tester list, copies the opt-in
   link into the mail, shows it once more, and sends on his "verstuur".
5. Wave 2 a few days later with the fixed build. Friends and family with
   Android may join wave 1: the 14 days only start at the twelfth tester.

Every address goes onto Play's tester email list before its mail goes
(Testing > Closed testing > Testers, a CSV of up to 2,000). The opt-in link
is already in the mail below (Play shows it before any release; it works once
the release is approved). Set up in Play on 2026-11-17: closed test "Alpha"
in all 178 countries, list "Ancient Trees testers" (Hidde only so far),
feedback to info@ancienttrees.app; internal test with list "Ancient Trees
team" (Hidde), and that list is on the closed test too.

**On the tester list in Play now: the 50 newest Gmail addresses** (the first
50 lines of out/play/wave1.csv, saved as out/play/wave1-a.csv; both
gitignored). Mail ONLY those 50 in wave 1: only addresses on the list can
join. Play refused to save 100 or 200 at once ("Je wijzigingen kunnen niet
worden opgeslagen", no reason given; every address is valid Gmail syntax),
so one of lines 51 to 100 is probably an address Google will not take. A CSV
upload REPLACES the list rather than adding to it. Next session: add the rest
in steps of 25 (cumulative files with the first 50 kept), drop the chunk that
fails and halve it. 50 is already four times the 12 needed. Nothing is sent
before Hidde says "verstuur".

The dates are Google's usual times for a new personal account: first review a
few hours to about 7 days, 14 days with 12+ testers opted in, about 7 days to
review the production application, then the release review.

Subject: Help us test the Android app

---

Hey,

Thanks for signing up for the Android app. We are working hard on it at the moment and are looking for people to test the first version. We expect a live version in 3 to 4 weeks.

You can sign up to be a tester here, with the Google account of this email address:
https://play.google.com/apps/testing/app.ancienttrees.android

Thanks so much for your help and your patience. Looking forward to hearing what you think!

Hidde
https://ancienttrees.app
