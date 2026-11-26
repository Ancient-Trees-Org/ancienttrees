import { ui } from "./i18n";
import { icon } from "./icons";

// THE TREES IN VIEW, one list for every map that shows them (2026-11-26,
// Hidde: "I really prefer 1 and all competitors do it"). Moved word for word
// out of exploreMapScript (map.ts), step 1 of making the city map and /explore
// one map: the city page uses this same list once you leave its city.
//
// Like PILES_JS and the other pieces, it is text that runs inside one map
// script, so it reads the names that script defines before it: map, pins
// (via applyFilters), SHOWN, DATA, FOCUS, PLACE, PLACES, SPECIES, SP_ICONS,
// SP_IC, WORDS, EMPTY, CHEVRON, BOX_IC, and atTreeCard / atPlaceCard from
// treeCardJs() and placeCardJs(). It defines renderPanel(), _esc(), _km(),
// _inFocus() and the panel's listeners on #ex-panel.
export function viewListJs(listMax: number): string {
  return `
// ---- THE TREES IN VIEW, AIRBNB'S WAY (Hidde, 2026-11-06: "zullen de airbnb
// interactie maar gewoon als standaard aan houden ... zowel voor app als
// web"), the app's list too (MapTab.swift): the count of trees in view, then
// for a searched city its box (the ambassador and Plus rows, until the search
// field changes, as Google Maps keeps a searched place's card), the
// photographed trees as Highlights, then every tree as a row, the searched
// place's own first. Nothing guesses a place name from the view any more. It replaced the list of cities in view
// (2026-07-31): the pins and the heading lead to the cities now. Photographs
// come from the one card catalogue the pins' cards already read
// (/api/cards.json, atCollection.catalogue), so the list draws first with the
// species tiles and again once it has answered.
var panel = document.getElementById('ex-panel');
// Hidden, or inside something hidden (the city page's list until you leave
// its city): the list then draws and fetches nothing.
function _listHidden() { return !panel || Boolean(panel.closest('[hidden]')); }
var CARDS = null;
// The trees this account collected, from the server (atCollection.visited),
// as a set; null signed out or until it answers.
var VISITED = null;
var LIST_MAX = ${listMax};
// pinPriority as the pins read it: a missing one counts as no photograph.
function _pr(f) { var r = f.properties.pr; return r === undefined || r === null ? 1 : r; }
function _n(w, n) { return n === 1 ? w.one : w.many.replace('{n}', String(n)); }
function _inFocus(f) {
  if (!FOCUS) { return false; }
  var pl = PLACES[f.properties.cs];
  return FOCUS.kind === 'country' ? Boolean(pl && pl.k === FOCUS.key) : f.properties.cs === FOCUS.key;
}
// The searched city's box: the ambassador row to its page's request. Nothing
// for a country or a city without a page.
// Only while the city's own trees are in view (Hidde, 2026-11-06: alone over
// an empty map it "staat nu zielig in zn eentje"); the field keeps the search.
function _focusCity(trees) {
  if (!FOCUS || FOCUS.kind === 'country' || !trees.some(_inFocus)) { return null; }
  var pl = PLACES[FOCUS.key];
  return pl && pl.h ? pl : null;
}
function _boxHtml(trees) {
  var pl = _focusCity(trees);
  if (!pl) { return ''; }
  var amb = (pl.a ? WORDS.ambA : WORDS.ambThe).replace('{p}', pl.n);
  return '<div class="city-box exc-box"><a class="city-box-row" href="' + _esc(pl.h) + '#ambassador">' + BOX_IC.amb +
    '<span class="city-box-label">' + _esc(amb) + '</span>' + CHEVRON + '</a></div>';
}
// The Plus row stands alone UNDER the trees (Hidde, 2026-11-06, before the
// Guardian piece: the first screen is the city and its trees, the ask comes
// after them; "dan kunnen we altijd nog meer op de voorgrond zetten"). It opens
// the one Plus sheet (PlusAsk.astro, on this page without a row of its own).
function _plusHtml(trees) {
  var pl = _focusCity(trees);
  if (!pl || !document.getElementById('plus-dialog')) { return ''; }
  var answered = false;
  try { answered = localStorage.getItem('at_plus_answered') === '1'; } catch (e) {}
  if (answered) { return ''; }
  return '<div class="city-box exc-box plus-under"><div class="plus-bar"><button type="button" class="plus-row city-box-row" data-from="explore" data-city="' + _esc(pl.n) + '">' +
    BOX_IC.plus + '<span class="city-box-label">' + _esc(WORDS.plus) + '</span>' + CHEVRON + '</button></div></div>';
}
// THE ONE CARD (lib/tree-card.ts, 2026-11-20): the highlight and the row
// are TreeCard's own, written by the same function, fed what the pin and the
// card catalogue know. Before, this list wrote both by hand.
function _cardModel(f, variant) {
  var p = f.properties, k = (CARDS && p.id && CARDS[p.id]) || {};
  var common = (p.sp !== undefined && p.sp !== null && SPECIES[p.sp]) || String(k.sp || '').replace(/\s*\(.*\)\s*$/, '');
  var ic = SP_ICONS[(p.sp !== undefined && p.sp !== null && SP_IC[p.sp]) || 'broadleaf'] || '';
  var img = k.p ? { src: k.p } : null;
  return { id: p.id || '', name: p.name || k.n || '', href: p.url ? '/' + p.url : '', variant: variant, h: 3,
    metaParts: [common, p.as || ''], photo: img, hl: img, thumb: img, savePhoto: k.p || '',
    tileIcon: ic, commonName: common, seen: Boolean(VISITED && VISITED[p.id]), creditHtml: k.ch || '',
    // An app-only tree (lib/app-first.ts APP_ONLY_PINS) has no page: its name
    // is no link and the card says where its story is, as its pin's card does.
    appHtml: p.url ? '' : '<p class="tree-meta tree-app-only"><a href="/app" data-app-download>' + _esc(WORDS.app) + '</a></p>' };
}
var _CARD_WORDS = { save: WORDS.save, saved: WORDS.saved, noPhoto: WORDS.noPhoto, seen: WORDS.seen };
function _hlHtml(f) { return atTreeCard(_cardModel(f, 'highlight'), _CARD_WORDS); }
function _rowHtml(f) { return atTreeCard(_cardModel(f, 'row'), _CARD_WORDS); }
function renderPanel() {
  // A hidden panel draws nothing: on a city page the list waits until you
  // leave the city (window.atViewListShow, below).
  if (_listHidden() || typeof map === 'undefined' || !map) return;
  var b = map.getBounds();
  var trees = SHOWN.filter(function(f) { var g = f.geometry.coordinates; return g[0] !== null && g[1] !== null && b.contains(g); });
  if (!trees.length) { panel.classList.remove('ex-trees'); panel.innerHTML = emptyHere(); return; }
  // Rows: the searched place first, then photograph first and readers' saves
  // (pinPriority, the pins' own order); sort is stable, so ties keep the
  // site's city order.
  trees = trees.slice().sort(function(a, z) {
    return (_inFocus(a) ? 0 : 1) - (_inFocus(z) ? 0 : 1) || _pr(a) - _pr(z);
  });
  // The count small and centred under the grip, Airbnb's "Over 1,000 homes"
  // (Hidde, 2026-11-06: "die 32 trees staat los"); the app's countStrip.
  var head = '<p class="exc-count">' + _esc(_n(WORDS.inView, trees.length)) + '</p>';
  // Highlights: photographed trees (pinPriority puts them at 0 or below),
  // each city's own Highlights first in their rank, at most ten.
  var hls = trees.filter(function(f) { return _pr(f) <= 0; }).sort(function(a, z) {
    var ha = a.properties.hl, hz = z.properties.hl;
    var na = ha === undefined || ha === null, nz = hz === undefined || hz === null;
    return (_inFocus(a) ? 0 : 1) - (_inFocus(z) ? 0 : 1) || (na ? 1 : 0) - (nz ? 1 : 0) ||
      (na || nz ? 0 : ha - hz) || _pr(a) - _pr(z);
  }).slice(0, 10);
  var html = head;
  if (hls.length) {
    html += '<section class="city-highlights"><h3 class="city-section-head">' + _esc(WORDS.highlights) + '</h3>' +
      '<div class="tree-hl-list">' + hls.map(_hlHtml).join('') + '</div></section>';
  }
  // COLLECTED, A SHELF LIKE THE HIGHLIGHTS (Hidde, 2026-11-06: "a section
  // like highlights ... same tiles as highlight but then collected"), the
  // app's too (MapTab placeList): the trees in view you collected, at most
  // ten. They stay in the rows below as well.
  if (VISITED) {
    var col = trees.filter(function(f) { return VISITED[f.properties.id]; }).slice(0, 10);
    if (col.length) {
      html += '<section class="city-highlights"><h3 class="city-section-head">' + _esc(WORDS.collected) + '</h3>' +
        '<div class="tree-hl-list">' + col.map(_hlHtml).join('') + '</div></section>';
    }
  }
  // The ambassador box sits in the place head's intro, above the
  // Highlights, as on the city page (Hidde, 2026-11-22: the city page is the
  // design; this reverses "onder highlight" of 2026-11-06).
  var boxEl = document.getElementById('ex-box');
  if (boxEl) { boxEl.innerHTML = _boxHtml(trees); }
  else { html += _boxHtml(trees); }
  html += '<h3 class="city-section-head">' + _esc(_n(WORDS.all, trees.length)) + '</h3>' +
    '<div class="tree-rows">' + trees.slice(0, LIST_MAX).map(_rowHtml).join('') + '</div>' +
    (trees.length > LIST_MAX ? '<p class="ex-more">' + _esc(WORDS.more) + '</p>' : '') + _plusHtml(trees);
  panel.classList.add('ex-trees');
  panel.innerHTML = html;
  // The hearts only: atPaintSaves refilters the map, which calls this again
  // (the 2026-11-06 crash, tree-actions-js.ts paintButtons).
  if (window.atPaintSaveButtons) { window.atPaintSaveButtons(); }
}
function _km(a, b) {
  var R = Math.PI / 180, h = Math.pow(Math.sin((b[1] - a[1]) * R / 2), 2) +
    Math.cos(a[1] * R) * Math.cos(b[1] * R) * Math.pow(Math.sin((b[0] - a[0]) * R / 2), 2);
  return 12742 * Math.asin(Math.sqrt(h));
}
function _esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;'); }
// No tree in view: the ask, named after the town while the map is still on
// it, then the tree nearest the middle of the map.
function emptyHere() {
  var c = map.getCenter(), here = [c.lng, c.lat];
  var named = PLACE && PLACE.name && _km(here, [PLACE.lng, PLACE.lat]) < 15;
  var title = named ? EMPTY.title.replace('{place}', PLACE.name) : EMPTY.here;
  var html = '<div class="td-notes-empty exc-ask">' +
    '<span class="td-notes-empty-ic" aria-hidden="true">' + EMPTY.ic + '</span>' +
    '<p class="td-notes-empty-t">' + _esc(title) + '</p>' +
    '<p class="td-notes-empty-s">' + _esc(EMPTY.ask) + '</p>' +
    '<div class="td-notes-empty-act"><a class="addphoto-btn quiet td-note-ask" href="/contribute?kind=tree' +
    (named ? '&city=' + encodeURIComponent(PLACE.name) : '') +
    '" data-ev="empty-place-add">' + EMPTY.plus + '<span>' + _esc(EMPTY.add) + '</span></a></div></div>';
  var best = null, bd = Infinity;
  DATA.features.forEach(function(f) {
    var g = f.geometry.coordinates;
    // An app-only tree has a pin but no page (APP_ONLY_PINS), so it is never
    // the "nearest tree" link here.
    if (g[0] === null || !f.properties.url) { return; }
    var d = _km(here, g);
    if (d < bd) { bd = d; best = f; }
  });
  if (best) {
    html += '<div class="exc-cityhead"><h2>' + _esc(EMPTY.nearest) + '</h2></div>' +
      // The one place card (lib/browse-card.ts). No photograph, as the app's
      // nearest row has none (MapTab.swift emptyHere; data/map-parity.json).
      atPlaceCard({ href: '/' + best.properties.url, name: best.properties.name, face: null,
        sub: Math.round(bd) + ' km &middot; ' + _esc(best.properties.city) });
  }
  return html;
}
if (panel) panel.addEventListener('click', function(e) {
  var a = e.target.closest ? e.target.closest('[data-ev]') : null;
  if (a) at.track(a.getAttribute('data-ev'), 'map');
});
map.on('moveend', renderPanel);
// The photographs, from the catalogue the pins' cards share. Not behind the
// map's load, which waits for every street tile: on a slow phone, or with the
// tile host busy, the list stood as grey tiles until the streets had come in.
var _cardsAsked = false;
function _askCards() {
  var C = window.atCollection;
  if (_cardsAsked || !C || !C.catalogue || _listHidden()) { return; }
  _cardsAsked = true;
  C.catalogue().then(function(c) { CARDS = c || {}; renderPanel(); });
}
// The trees this account collected, asked once, and only while the list shows.
var _visitedAsked = false;
function _askVisited() {
  var C = window.atCollection;
  if (_visitedAsked || !C || !C.verify || !C.visited || _listHidden()) { return; }
  _visitedAsked = true;
  C.verify().then(function(ok) {
    if (!ok) { return; }
    C.visited().then(function(ids) {
      if (!ids || !ids.length) { return; }
      VISITED = {}; ids.forEach(function(id) { VISITED[id] = 1; }); renderPanel();
    });
  });
}
_askCards();
map.on('load', function() {
  renderPanel();
  _askCards();
  _askVisited();
});
// A city page shows the list once you leave its city (city-map-script.ts).
window.atViewListShow = function() {
  _askCards();
  if (map.loaded()) { _askVisited(); }
  renderPanel();
};
renderPanel();
`;
}

/** The list's words and drawings in the page's language: the names
 *  view-list-js.ts reads (WORDS, EMPTY, CHEVRON, BOX_IC). exploreMapScript
 *  writes them into /explore; /api/map-view/<lang>.json carries them for the
 *  city map. */
export function viewListWords(lang: string) {
  const U = ui(lang);
  // A counted string travels as its one-tree form and a template with {n},
  // so the browser fills the number without a rule of its own.
  const counted = (fn: (n: number) => string) => ({ one: fn(1), many: fn(98765).replace("98765", "{n}") });
  return {
    words: {
      inView: counted(U.treesInView), all: counted(U.allTrees), highlights: U.highlights,
      more: U.zoomForMore, app: U.readInApp, save: U.cardSave, saved: U.cardSaved,
      credit: U.photoCredit("{c}"),
      collected: U.mapFilterMine, seen: U.seenChip, noPhoto: U.noPhotoYet,
      ambThe: U.ambassadorBecomeThe("{p}"), ambA: U.ambassadorBecomeA("{p}"), plus: U.plusRow,
      headIn: U.heading("{c}"),
    },
    // The empty map's ask (Hidde, 2026-10-25): the grey card of an empty notes
    // section, then the nearest tree. Words in the page's language.
    empty: { title: U.emptyPlaceTitle, here: U.emptyHereTitle,
      ask: U.emptyPlaceAsk, add: U.addTree, nearest: U.nearestTree,
      ic: icon("tree", "regular"), plus: icon("plus", "bold") },
    chevron: icon("caret-right", "bold", "ic city-box-chev"),
    boxIc: { amb: icon("seal-check", "bold", "ic city-box-ic"), plus: icon("sparkle", "fill", "ic city-box-ic") },
  };
}
