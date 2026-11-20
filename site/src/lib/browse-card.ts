// The one card used by every browse index (cities, species, collections,
// countries, parks). Ported from browse_card()/collection_face(),
// build_site.py:3865-3892.
import { usablePhoto, thumbUrl, NO_PHOTO_CARD, type TreeLike } from "./images";
import { BASE_URL } from "./schema";

// THE PLACE CARD, ONE FUNCTION FOR THE SERVER AND THE BROWSER (Hidde,
// 2026-11-20, "werk daarna volgende component uit", after the pin, the save
// button and the tree card). The photograph, the name and one line under it:
// a city, a species, a collection, a country, a park. The browse indexes
// wrote it through browseCard(), and four more places wrote it by hand (the
// /cities pages in English and translated, the city map's "cities in view",
// /explore's nearest tree), each a little different: the translated index
// printed a bare number, the city map said "trees" in English on every page.
// Now placeCardHtml() writes it everywhere, and scripts carry its own source
// (placeCardJs()), as saveButtonHtml() and treeCardHtml() are carried.
export interface PlaceCard {
  href: string;
  name: string;
  /** The line under the name, as HTML (it may carry a .dist span). */
  sub: string;
  /** The photograph, or null for the no-photo drawing. */
  face: string | null;
}

export function placeCardHtml(o: PlaceCard, noPhoto: string): string {
  function esc(s: unknown): string {
    return String(s === undefined || s === null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  var ph = o.face ? '<span class="exc-ph"><img src="' + esc(o.face) + '" alt="" loading="lazy"></span>' : noPhoto;
  return '<a class="exc-card" href="' + esc(o.href) + '">' + ph + '<span class="exc-body"><b>' + esc(o.name) +
    "</b><span>" + o.sub + "</span></span></a>";
}

export function browseCard(href: string, name: string, sub: string, face: string | null): string {
  return placeCardHtml({ href, name, sub, face }, NO_PHOTO_CARD);
}

/** The same function for a page's script: atPlaceCard(o) in the browser. */
export function placeCardJs(): string {
  const src = placeCardHtml.toString();
  if (/__\w+\(|\?\?|\?\.|=>/.test(src)) {
    throw new Error("placeCardHtml() no longer ships as plain ES5 text: " + src.slice(0, 120));
  }
  return `
var AT_NO_PHOTO_CARD = ${JSON.stringify(NO_PHOTO_CARD)};
var atPlaceCardHtml = ${src};
function atPlaceCard(o) { return atPlaceCardHtml(o, AT_NO_PHOTO_CARD); }
`;
}

interface CollectionEntryLike {
  city_slug: string;
  tree_id: string;
}
interface CityLike {
  data: { trees: TreeLike[] };
}

/** First entry in the collection that has a usable photo. */
export function collectionFace(
  entries: CollectionEntryLike[],
  citiesBySlug: Map<string, CityLike>,
): string | null {
  for (const e of entries) {
    const entry = citiesBySlug.get(e.city_slug);
    if (!entry) continue;
    for (const t of entry.data.trees) {
      if (t.id === e.tree_id) {
        const p = usablePhoto(t);
        if (p?.url) {
          // /api/browse.json is read by the app, which has no page to resolve
          // a relative path against, and thumbUrl now returns "/photos/..."
          // for the photographs we host ourselves.
          const u = thumbUrl(p.url, 400);
          return u.startsWith("/") ? `${BASE_URL}${u}` : u;
        }
      }
    }
  }
  return null;
}
