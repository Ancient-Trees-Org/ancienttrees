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

**The text below is Hidde's own (2026-11-17) and is agreed. It waits only for
the build.** The order, once he says go:
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
team" (Hidde). Wave 1's 200 addresses are in out/play/wave1.csv on the Mac
(gitignored, rebuilt by a session from the waitlist), not yet uploaded to
Play. Nothing is sent before Hidde says "verstuur".

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
