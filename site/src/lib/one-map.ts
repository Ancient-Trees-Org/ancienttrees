// ONE MAP ON THE WEBSITE (Hidde, 2026-11-26: "I really prefer 1 and all
// competitors do it"; CONVENTIONS.md "One map or two"). A city page is the map
// opened on its city: drag or zoom it yourself (Airbnb's way, 2026-11-27) and
// the panel becomes the map's trees in view (lib/view-list-js.ts), the address
// /explore#map=..., without loading a page; Back brings the city back.
//
// It goes live city by city, so a fault reaches a few pages that Google sends
// people to, never all of them (pagecheck's map walk stops a broken deploy).
// "all" turns it on everywhere, every language's city page included (the
// languages since 2026-11-27).
// Tokyo alone from 2026-11-26; every English city page from 2026-11-27
// (Hidde: "Ja, alle steden").
export const ONE_MAP_CITIES: "all" | string[] = "all";

export function oneMapOn(slug: string, lang: string): boolean {
  const on = ONE_MAP_CITIES as "all" | string[];
  return on === "all" || on.includes(slug);
}
