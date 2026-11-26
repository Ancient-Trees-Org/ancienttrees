// ONE MAP ON THE WEBSITE (Hidde, 2026-11-26: "I really prefer 1 and all
// competitors do it"; CONVENTIONS.md "One map or two"). A city page is the map
// opened on its city: leave the city, or close its panel with the cross, and
// the panel becomes the map's trees in view (lib/view-list-js.ts), the address
// /explore#map=..., without loading a page; Back brings the city back.
//
// It goes live city by city, so a fault reaches a few pages that Google sends
// people to, never all of them (pagecheck's map walk stops a broken deploy).
// "all" turns it on everywhere; an English city page first, the languages
// after.
export const ONE_MAP_CITIES: "all" | string[] = ["tokyo"];

export function oneMapOn(slug: string, lang: string): boolean {
  if (lang !== "en") return false;
  return ONE_MAP_CITIES === "all" || ONE_MAP_CITIES.includes(slug);
}
