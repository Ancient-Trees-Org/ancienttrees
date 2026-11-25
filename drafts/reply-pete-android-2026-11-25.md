To: Pete (thread "Re: Help us test the Android app"), from the new-app invite of 2026-11-25.
He asks to send the invite to the other Gmail address his Play account uses (it is in his mail of 2026-11-25 10:09); the link does not accept the address we mailed.
BEFORE SENDING: add that address to the "Android testers" email list in Play Console (new app app.ancienttrees.map). The draft says it is added.
At send: `python3 scripts/android_testers.py --add "Pete" <that address> yes "asked to be invited on his Play address" "Help us test the Android app"`, then `private_store.py push`.
audience: reader

---

Hi Pete,

Thanks for letting us know! I've added your other address to the test group, so the link should work now when you open it with that Google account:
https://play.google.com/apps/testing/app.ancienttrees.map

Thanks again,
Hidde
