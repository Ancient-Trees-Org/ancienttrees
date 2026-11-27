// OUR OWN PHOTOGRAPHS, TOLD TO SEARCH ENGINES (Hidde, 2026-11-27: "Ja, bouw 1
// en 2"). A photograph a visitor took at the tree exists nowhere else on the
// web, and it is the strongest thing a tree page has, but until today a
// crawler saw it only as one more <img>. Each one now travels in the tree
// page's structured data as an ImageObject (when, by whom in words, never a
// name), and the sitemap lists it under its page as an image:image
// (sitemap-integration.ts reads the contentUrls back out of the built page,
// so the rule lives here once).
//
// Whose counts: the same three sources thin_pages.unique_photo() calls ours,
// a reader's through the app ("contributor"), our own ("mine"), and one a
// person mailed us with their yes ("mail"). A Commons or Flickr photograph is
// on other sites too, so it stays a plain image url.

type Shot = {
  url?: string | null;
  source?: string | null;
  note?: string | null;
  taken_month?: number | null;
  sighting_id?: string | null;
};

const OURS = new Set(["contributor", "mine", "mail"]);

export function isOwnPhoto(p: Shot | null | undefined): boolean {
  return !!p?.url && OURS.has(p.source ?? "");
}

/** The day the photograph reached us, from the note every publishing script
 *  writes ("sent through the app (2026-11-16)"); null when it does not say. */
export function ownPhotoDay(p: Shot): string | null {
  const m = /\((20\d\d-\d\d-\d\d)\)/.exec(p.note ?? "");
  return m ? m[1] : null;
}

function byWhom(p: Shot): string {
  if (p.source === "mine") return "Ancient Trees";
  return "a visitor to the tree";
}

/** ImageObjects for the tree page's structured data, our own photographs
 *  only, in the order the page shows them. */
export function ownImageObjects(shots: Shot[], treeName: string, place: string): Record<string, unknown>[] {
  return shots.filter(isOwnPhoto).map((p) => {
    const day = ownPhotoDay(p);
    return {
      "@type": "ImageObject",
      contentUrl: p.url,
      caption: `${treeName}, ${place}, photographed at the tree by ${byWhom(p)}`,
      creditText: p.source === "mine" ? "Ancient Trees" : "A visitor, via Ancient Trees",
      copyrightNotice: "Ancient Trees",
      ...(day ? { dateCreated: day, uploadDate: day } : {}),
    };
  });
}
