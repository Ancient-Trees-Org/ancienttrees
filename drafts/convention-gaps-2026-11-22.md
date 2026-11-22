# Convention gaps, 2026-11-22

Research only, nothing built. Question: which everyday reflexes do AllTrails, Instagram, komoot, Strava, Google Maps, Airbnb and Polarsteps share that Ancient Trees misses or does differently?

Method: CONVENTIONS.md headings grepped first (what is recorded there counts as covered); the iOS Swift screens read for each reflex; the live website walked at 375 px in the built-in browser; reference help pages read where they would load (AllTrails through its help-centre JSON, Apple's HIG and App Review Guidelines in the browser). Instagram's and Strava's help centres and Google's pin page would not give their article text to a fetch or a browser read, so those rows say **from memory**.

**Looked up** = read today on the page named. **From memory** = not re-read today.

## Already covered (no gap)

Recorded in CONVENTIONS.md and present in the code, so left out of the ranking: tapping the tab you are on empties its stack (ContentView.swift:306); Undo after removing a save or a tick (SaveHeart.swift:150, TreeDetail.swift:2760, tree-actions-js.ts:88); the system share sheet (Kit/ShareSheet.swift, share-js.ts); recent searches; Back on a web tree page returns where you came from (tree-page-js.ts:145); editing and deleting your own note (TreeDetail.swift:2307); deleting your own photograph; the Activity bell with a dot (Activity.swift, web page built, not live yet because the site deploy is failing today); double tap zooms in the full-screen photo viewer (PhotoViewer.swift:102, as in Apple Photos); landing on the Map tab (a map app's first screen, as Google Maps and AllTrails Explore).

## The ranked list

| # | Gap | What the references do (source) | What we do | Matters for |
|---|---|---|---|---|
| 0 | Your own name or picture opens your public profile; changing picture or country takes face, gear, card | AllTrails: "Tap your profile image at top right", then "..." and "Edit profile" (support.alltrails.com 4409900896148, looked up). Instagram: your picture in the tab bar, "Edit profile" under the name (from memory) | Name links to `/profile?u=<you>` (site/src/lib/reader-names-js.ts:58, :66); app pushes `.person(id)` for your own id too (TreeDetail.swift:2536) | Being mocked up in another session; listed as the example only |
| 1 | **On a phone's web page, Back with a photo or sheet open leaves the page** instead of closing what is open | Instagram web opens a post over the feed with its own address, so Back closes it; Google Maps mobile web and Airbnb mobile web close the open panel or photo tour on Back (from memory). Android's own rule: system Back dismisses the topmost thing first (from memory) | Tested live today: on /london/totteridge-yew, opened the photograph, pressed Back, landed on the previous site. No sheet or viewer writes a history entry (no `pushState` in Sheet.astro or the photo viewer) | **Goal 1, high.** Seven in ten mobile visitors are on Android, where Back is the reflex; one press throws them off the tree they were reading |
| 2 | **No push notifications at all** (a heart on your photo, a new follower, your tree is live) | Everybody tells the contributor: Strava, komoot, iNaturalist, Polarsteps (CONVENTIONS.md "Hearing that something you saved has news", looked up 2026-11-20); AllTrails pushes "updates about your AllTrails Community", per category (support.alltrails.com 37215941812116, looked up) | No notification registration anywhere in the iOS app (no `registerForRemoteNotifications`); news waits behind the bell on Discover until you open the app | **Traction, high.** The loop that brings a contributor back; costs a permission ask and server work |
| 3 | **Block and report are not on a person's profile** | AllTrails: on the person's profile, the "..." overflow menu, "Remove follower" or "Block user"; on the web "Block" under their picture (support.alltrails.com 360019244871, looked up). Instagram: ... on the profile, Block / Report (help.instagram.com 426700567389543 "Blocking people", path from memory). Apple App Review 1.2: an app with user content must offer reporting, "the ability to block abusive users" and contact details (developer.apple.com/app-store/review/guidelines, looked up) | Report and Block exist only behind the ... on a row in Find people (People.swift:320-326, :529). PersonProfile.swift has no menu; the website's profile has none either | **Traction and store risk, medium-high.** As people and photos grow, the person you want to block is the one whose profile you are looking at |
| 4 | **Someone else's follower counts are not tappable** | AllTrails: "Click the number next to 'Followers'" opens the list (360019244871, looked up); Strava and Polarsteps the same (CONVENTIONS.md "Finding and following people") | App: plain text on another person's profile (PersonProfile.swift:116). Your own counts on the web do open lists (people-js.ts:342) | Traction, medium. Following is how people find people; Hidde wants it bigger in phase 2 |
| 5 | **Pull to refresh is missing on My trees, a profile and Activity** | Instagram, Strava, AllTrails: every feed and profile refreshes on a downward pull (from memory; Apple's "Refresh content controls" page no longer loads) | Only Discover (Home.swift:376) and Find people (People.swift:605) | Traction, medium. A reader who just added a photo pulls to see it, nothing happens, and they think it failed |
| 6 | **A long press on the map does nothing** | Google Maps: "Drop a pin on the map" (support.google.com/maps/answer/3092445, listed, steps from memory: touch and hold, then save, share, or add a missing place). Apple Maps: the same (from memory) | No long-press handler on any map (only CollectIntro.swift:136 uses one) | Collecting data, medium. "Add a tree here" at a pressed spot is the shape every map app uses for a missing place |
| 7 | **Double tap on a visitor's photograph in a feed does not heart it** | Instagram: double tap a photo to like it (from memory) | Hearts only through the heart button (Activity and VisitorPhotos); double tap in the full-screen viewer zooms, which is right there | Traction, low-medium. Only the feed tiles, never the viewer |
| 8 | **Tapping the Map or My trees tab again does not scroll or recentre** | Instagram and Strava: tapping the tab you are on scrolls to the top (from memory) | Only Discover scrolls up (Home.swift:267); on My trees and Map a second tap with nothing pushed does nothing | Low |
| 9 | **No long-press menu on a tree card** (Save, Share, Directions) | Apple HIG: context menus hold the most likely commands, "Support context menus consistently throughout your app", and every item must also be in the main interface (developer.apple.com/design/human-interface-guidelines/context-menus, looked up) | None anywhere, which is consistent, so not wrong | Low |
| 10 | **Signed out, /profile says "This profile is private."** | AllTrails and Instagram send a signed-out visitor who opens "your profile" to sign in (from memory) | profile.astro:48 shows the private line for every unreadable case | Low, but it reads as a broken page |

## Hidde's answers (2026-11-22)

1 yes (built), 2 later, 3 not answered yet, 4 yes (built), 5 yes (built on profiles and Activity; My trees left out, see CONVENTIONS.md). Rows 6 to 10 not asked yet.

## Questions for Hidde (top five, in Dutch)

```text
- Moet de terugknop van de telefoon op de website eerst de open foto of het open blad sluiten, zoals bij Instagram en Google Maps, in plaats van de pagina te verlaten?
- Willen we pushmeldingen sturen als iemand je foto een hartje geeft, je volgt of je boom live gaat, zoals Strava en komoot, met een keuze per soort?
- Zullen we Blokkeren en Melden in het ...-menu op iemands profiel zetten, zoals AllTrails, en niet alleen in Mensen zoeken?
- Mogen de aantallen volgers en volgend op andermans profiel aantikbaar worden, zodat je die lijst ziet, zoals bij AllTrails en Strava?
- Willen we omlaag trekken om te verversen ook op Mijn bomen, profielen en Activiteit, zoals Instagram dat overal doet?
```
