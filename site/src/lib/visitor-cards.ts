// What each tree looks like on a visitor's tile, for the trees that carry a
// visitor's photograph: shared by the home row (HomePage.astro,
// lib/visitors-row-js.ts) and the See all page (VisitorsPage.astro,
// lib/visitors-page-js.ts), so the two cannot drift. Moved out of
// HomePage.astro on 2026-11-18, unchanged, plus each photograph's size.
//
// A tree without a page of its own (app-first.ts) opens its place's map on
// its card, or the explore map where the place has no page. `s` maps each
// visitor's photograph (by its sightings row) to its own small copy, so the
// tile shows the picture that visitor sent and not the tree's lead (Hidde,
// 2026-11-15: "waarom toont hij niet altijd de gebruikers foto"). `d` holds
// that photograph's width and height, so the See all page can place a whole
// photograph in its column before it has loaded (no jump while scrolling).
import { getCollection } from "astro:content";
import { renderableTrees, mapTrees, cityIsOnMap, treeHasPage, treeSlugsForCity } from "./trees";
import { usablePhoto, thumbUrl } from "./images";
import { placeHasPage, exploreAt } from "./place-page";
import { cityHref, languagesForCity } from "./i18n";

export type VisitorCard = {
  n: string;
  c: string;
  u: string;
  p: string;
  s: Record<string, string>;
  d: Record<string, [number, number]>;
};

export async function visitorCards(lang: string): Promise<Record<string, VisitorCard>> {
  const treeHref = (citySlug: string, treeSlug: string) =>
    lang !== "en" && languagesForCity(citySlug).includes(lang)
      ? `/${lang}/${citySlug}/${treeSlug}`
      : `/${citySlug}/${treeSlug}`;
  const out: Record<string, VisitorCard> = {};
  for (const c of (await getCollection("cities")).filter(cityIsOnMap)) {
    const slugs = treeSlugsForCity(c);
    const placePage = placeHasPage(c.id, renderableTrees(c).length);
    for (const t of mapTrees(c)) {
      const all = [t.photo, ...((t as any).photos ?? [])];
      if (!all.some((p: any) => p?.source === "contributor")) continue;
      const ph = usablePhoto(t);
      if (!ph?.url) continue;
      const href = treeHasPage(t)
        ? treeHref(c.id, slugs[t.id])
        : placePage
          ? `${cityHref(lang, c.id)}#tree=${encodeURIComponent(t.id)}`
          : exploreAt(t.location.latitude, t.location.longitude);
      const s: Record<string, string> = {};
      const d: Record<string, [number, number]> = {};
      for (const p of all as any[]) {
        const sid = String(p?.sighting_id ?? "").toLowerCase().match(/^[0-9a-f-]{36}/)?.[0];
        if (p?.source === "contributor" && p?.url && sid && !s[sid]) {
          s[sid] = thumbUrl(p.url, 500);
          if (p.width > 0 && p.height > 0) d[sid] = [p.width, p.height];
        }
      }
      out[t.id] = { n: t.name, c: c.data.city, u: href, p: thumbUrl(ph.url, 500), s, d };
    }
  }
  return out;
}

/** The cards as a JSON script body, safe inside a <script> element. */
export function cardsJson(cards: Record<string, VisitorCard>): string {
  return JSON.stringify(cards).replace(/</g, "\\u003c");
}
