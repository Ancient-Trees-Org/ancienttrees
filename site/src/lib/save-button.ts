// THE SAVE BUTTON, ONE FUNCTION FOR THE SERVER AND THE BROWSER (Hidde,
// 2026-11-20: "we zijn nu de hele tijd verschillende versies aan het
// onderhouden ik wil gewoon 1 goede", then "pak volgende component ook op").
// SaveHeart.astro was the button, and four scripts wrote its markup again by
// hand (the explore list, the card catalogue, the visitors row, the home
// shelf), each a little different. Now SaveHeart.astro renders through
// saveButtonHtml() and every script carries the very same function as text
// (saveButtonJs(), its own source), so there is one button.
//
// saveButtonHtml() is written to survive being shipped as text: it reads
// nothing outside its own arguments, and it stays plain ES5 (no ?? or ?.),
// because the browsers we still serve include old ones (web_errors 2026-11,
// Chrome 75).
//
// Painted and handled by TREE_ACTIONS_JS via delegation, so a page that
// renders it must also ship TREE_ACTIONS_JS. Labels ride on data attributes
// so a Spanish page stays Spanish; the button also carries what /saved needs
// to draw the same card it was saved from (url, photograph, meta line).
import { icon } from "./icons";

/** Phosphor's bookmark, outline and filled, the app's SaveHeart glyph since
 *  2026-10-09. CSS shows one or the other on aria-pressed. */
export const SAVE_ICONS = icon("bookmark-simple", "bold", "heart hi-off") + icon("bookmark-simple", "fill", "heart hi-on");

export interface SaveButton {
  id: string;
  name: string;
  /** The words, in the page's language. */
  save: string;
  saved: string;
  url?: string;
  photo?: string;
  meta?: string;
  /** "card": the white circle on a list card's photograph; "round": the app's
   *  bar circle; "pill" (default): the word beside the glyph. */
  look?: "pill" | "round" | "card";
  compact?: boolean;
  /** Paint it saved from the start (the paint script corrects it anyway). */
  pressed?: boolean;
}

export function saveButtonHtml(o: SaveButton, icons: string): string {
  function esc(s: unknown): string {
    return String(s === undefined || s === null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  var look = o.look || "pill";
  var cls = "save-btn heart-btn" + (o.compact ? " heart-compact" : "") +
    (look === "round" ? " heart-round" : "") + (look === "card" ? " heart-card" : "");
  return '<button class="' + cls + '" type="button" data-tree="' + esc(o.id) + '" data-name="' + esc(o.name) + '"' +
    ' data-l-save="' + esc(o.save) + '" data-l-saved="' + esc(o.saved) + '"' +
    (o.url ? ' data-url="' + esc(o.url) + '"' : "") +
    (o.photo ? ' data-photo="' + esc(o.photo) + '"' : "") +
    (o.meta ? ' data-meta="' + esc(o.meta) + '"' : "") +
    ' aria-pressed="' + (o.pressed ? "true" : "false") + '"' +
    ' aria-label="' + esc(o.save + " " + o.name) + '">' + icons +
    '<span' + (look === "round" || look === "card" ? ' class="sr-only"' : "") + '>' + esc(o.save) + '</span></button>';
}

/** The same function for a page's script: atSaveButton(o) in the browser is
 *  saveButtonHtml(o) on the server. */
export function saveButtonJs(): string {
  // The build's compiler must hand the function over untouched: a helper it
  // injects (esbuild's __name, a spread or optional-chaining shim) would not
  // exist in the browser, so the build stops here rather than ship it.
  const src = saveButtonHtml.toString();
  if (/__\w+\(|\?\?|\?\.|=>/.test(src)) {
    throw new Error("saveButtonHtml() no longer ships as plain ES5 text: " + src.slice(0, 120));
  }
  return `
var AT_SAVE_ICONS = ${JSON.stringify(SAVE_ICONS)};
var atSaveButtonHtml = ${src};
function atSaveButton(o) { return atSaveButtonHtml(o, AT_SAVE_ICONS); }
`;
}
