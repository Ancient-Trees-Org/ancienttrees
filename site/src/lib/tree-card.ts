// THE TREE CARD, ONE FUNCTION FOR THE SERVER AND THE BROWSER (Hidde,
// 2026-11-20: "pak volgende component ook op", after the pin and the save
// button). TreeCard.astro was the card, and the scripts that draw cards in
// the browser wrote its markup again by hand: the card catalogue (map cards,
// the profile grid, /account), the explore list's highlights and rows. Each
// had drifted: no credit links, English words, a third kind of "seen" badge,
// no tile for a tree without a photograph.
//
// Now the markup has one author, treeCardHtml(). TreeCard.astro works out
// the card's answers (which photograph at which widths, the meta line, the
// credit with its links, the season chip) and calls it; a script carries the
// same function as text (treeCardJs()) and feeds it the same answers from
// /api/cards.json. Nothing in here decides anything: it only writes what it
// is handed, in the shape TreeCard always had.
//
// Like saveButtonHtml() it reads nothing outside its arguments and stays
// plain ES5, because it ships as its own source.
import { saveButtonHtml, saveButtonJs, SAVE_ICONS } from "./save-button";

/** One <img>: the src, and the srcset and sizes when there are widths. */
export interface CardImg { src: string; srcset?: string; sizes?: string }

export interface CardModel {
  id: string;
  name: string;
  /** The tree's page; "" for a tree without one (an app-only tree). */
  href: string;
  variant: "full" | "compact" | "row" | "highlight";
  /** The city page's card number (#tree-N), else null. */
  index?: number | null;
  /** The name's heading level on full, compact and row cards. */
  h?: 2 | 3;
  /** A label after the name (TreeCard tree.label), already in words. */
  label?: string;
  /** Common name and short age, plain text; joined with a middot. */
  metaParts: string[];
  /** The story text, as HTML (latin.ts italics), or "". */
  storyHtml?: string;
  /** The photograph at card width; null for a tree without one. */
  photo: CardImg | null;
  /** The highlight's photograph and the row's 64px thumbnail. */
  hl?: CardImg | null;
  thumb?: CardImg | null;
  /** What the save button stores for /saved: the photograph at 500. */
  savePhoto?: string;
  /** The species silhouette (species-icons.ts) for the no-photo tile. */
  tileIcon?: string;
  commonName?: string;
  /** The season chip's HTML (phenology.ts seasonChipHtml), or "". */
  chipHtml?: string;
  /** Draw the "seen" badge for the paint script to show (canTick). */
  canTick?: boolean;
  /** Draw it shown already (the account knows the tree is collected). */
  seen?: boolean;
  /** The photo credit's HTML (creditLineHtml), or "". */
  creditHtml?: string;
  /** "Read its story in the app" for a tree without a page, as HTML, or "". */
  appHtml?: string;
}

export interface CardWords {
  save: string;
  saved: string;
  noPhoto: string;
  seen: string;
  seenMark: string;
  /** The one save button, bound to its icons. */
  button: (o: object) => string;
}

export function treeCardHtml(m: CardModel, w: CardWords): string {
  function esc(s: unknown): string {
    return String(s === undefined || s === null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function img(i: CardImg, alt: string): string {
    return '<img src="' + esc(i.src) + '"' + (i.srcset ? ' srcset="' + esc(i.srcset) + '"' : "") +
      (i.sizes ? ' sizes="' + esc(i.sizes) + '"' : "") + ' alt="' + esc(alt) + '" loading="lazy">';
  }
  var parts: string[] = [];
  for (var k = 0; k < m.metaParts.length; k++) { if (m.metaParts[k]) { parts.push(m.metaParts[k]); } }
  var metaHtml = parts.map(esc).join(" &middot; ");
  var nameLink = m.href ? '<a href="' + esc(m.href) + '">' + esc(m.name) + "</a>" : esc(m.name);
  function button(photo: string | undefined): string {
    return w.button({ id: m.id, name: m.name, save: w.save, saved: w.saved, url: m.href || undefined,
      photo: photo || undefined, meta: parts.join(" · ") || undefined, look: "card" });
  }
  var seen = '<span class="tree-card-seen" data-tree="' + esc(m.id) + '"' + (m.seen ? "" : " hidden") + ">" +
    w.seenMark + "<span>" + esc(w.seen) + "</span></span>";
  var showSeen = m.canTick || m.seen;
  var tags = (m.chipHtml || showSeen) ? '<div class="tag-row">' + (m.chipHtml || "") + (showSeen ? seen : "") + "</div>" : "";
  var meta = metaHtml ? '<p class="tree-meta">' + metaHtml + "</p>" : "";
  var credit = m.creditHtml ? '<p class="tree-card-credit">' + m.creditHtml + "</p>" : "";
  var app = m.appHtml || "";

  if (m.variant === "highlight") {
    var hl = m.hl || m.photo;
    if (!hl) { return ""; }
    return '<article class="tree-hl tree-card-link" data-tree-id="' + esc(m.id) + '"><div class="tree-hl-photo">' +
      img(hl, m.name) + button(m.savePhoto) + tags + "</div>" +
      '<p class="tree-name tree-hl-name">' + nameLink + "</p>" + meta + app + credit + "</article>";
  }

  var row = m.variant === "row";
  var h = m.h === 2 ? "h2" : "h3";
  var heading = "<" + h + ' class="tree-name">' + nameLink +
    (m.label ? '<span class="tree-label">' + esc(m.label) + "</span>" : "") + "</" + h + ">";
  var story = m.storyHtml ? '<p class="tree-story">' + m.storyHtml + "</p>" : "";
  var out = '<article class="tree-card tree-card-link tree-card-nonum' + (m.photo ? "" : " tree-card-hastile") +
    (row ? " tree-card-row" : "") + '"' +
    (m.index === undefined || m.index === null ? "" : ' id="tree-' + m.index + '"') +
    ' data-tree-id="' + esc(m.id) + '">';
  if (m.photo) {
    out += '<div class="tree-card-photo">' + img(m.photo, m.name) + button(m.savePhoto) + tags + "</div>";
  } else {
    out += '<div class="tree-card-photo tree-card-tile"><div class="tree-card-tile-art" aria-hidden="true">' +
      '<svg viewBox="0 0 40 40">' + (m.tileIcon || "") + "</svg>" +
      (m.commonName ? '<span class="tree-card-tile-name">' + esc(m.commonName) + "</span>" : "") +
      '<span class="tree-card-tile-none">' + esc(w.noPhoto) + "</span></div>" + button(undefined) + tags + "</div>";
  }
  if (row) {
    var th = m.thumb || m.photo;
    out += '<div class="tree-row-thumb' + (th ? "" : " tree-row-thumb-none") + '" aria-hidden="true">' +
      (th ? img(th, "") : '<svg viewBox="0 0 40 40">' + (m.tileIcon || "") + "</svg>") + "</div>";
    out += '<div class="tree-row-text"><div class="tree-card-top">' + heading + "</div>" + meta + story + app + credit +
      (showSeen ? '<div class="tag-row tree-row-tags">' + seen + "</div>" : "") + "</div>";
    out += '<div class="tree-row-save">' + button(m.savePhoto) + "</div>";
  } else {
    out += '<div class="tree-card-top">' + heading + "</div>" + meta + story + app + credit;
  }
  return out + "</article>";
}

// The "seen" badge's mark: a green disc with a white tick, the app's
// checkmark.seal drawn flat.
export const SEEN_MARK = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="#4A6B2A"/><path d="M7.5 12.5l3 3 6-6.5" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>';

/** The words for the server, in the page's language. */
export function cardWords(U: { cardSave: string; cardSaved: string; noPhotoYet: string; seenChip: string }): CardWords {
  return { save: U.cardSave, saved: U.cardSaved, noPhoto: U.noPhotoYet, seen: U.seenChip, seenMark: SEEN_MARK,
           button: (o) => saveButtonHtml(o as Parameters<typeof saveButtonHtml>[0], SAVE_ICONS) };
}

/** The same function for a page's script: atTreeCard(model, words) in the
 *  browser, with words as cardWords() gives them minus the button, which the
 *  browser binds to the one save button. Carries saveButtonJs(). */
export function treeCardJs(): string {
  const src = treeCardHtml.toString();
  if (/__\w+\(|\?\?|\?\.|=>/.test(src)) {
    throw new Error("treeCardHtml() no longer ships as plain ES5 text: " + src.slice(0, 120));
  }
  return `${saveButtonJs()}
var AT_SEEN_MARK = ${JSON.stringify(SEEN_MARK)};
var atTreeCardHtml = ${src};
function atTreeCard(m, w) {
  return atTreeCardHtml(m, { save: w.save, saved: w.saved, noPhoto: w.noPhoto, seen: w.seen,
    seenMark: AT_SEEN_MARK, button: atSaveButton });
}
`;
}
