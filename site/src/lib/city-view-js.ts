// ONE MAP: THE CITY'S PANEL, THEN THE MAP'S TREES IN VIEW (Hidde,
// 2026-11-26: "I really prefer 1 and all competitors do it"; lib/one-map.ts,
// CONVENTIONS.md "One map or two"). The city page is the map opened on its
// city. Google Maps keeps a place's panel while you look around and closes it
// with its cross; Airbnb's list turns into "within map area" once the map is
// moved off the place, and its address follows the view without a page load.
// So: the panel is the city's, as the server wrote it, until you move the
// map yourself. Then, Airbnb's way (Hidde, 2026-11-27: "ja maak gewoon airbnb
// na", after finding the cross odd and zooming out doing nothing), the panel
// becomes /explore's list of trees in view (lib/view-list-js.ts, the
// same code), the head says the map's own title and the address becomes
// /explore#map=..., which loads exactly this view on its own. Back brings the
// city's panel back. Nothing names a place from what happens to be in view
// (CONVENTIONS.md, 2026-11-06): zooming into another city leaves the list.
//
// Text inside cityMapScript's body, after `var map`. It reads markers, HOME,
// SPECIES, SPECIES_L, SP_IC, filtersOn, keepsTree, clearPin and mapCard from
// that script and builds the list's own names from /api/map-view/<lang>.json,
// fetched the first time you leave the city. The page's HTML does not change:
// the list, its note and its head are made here, in the browser.
import { viewListJs } from "./view-list-js";
import { EXPLORE_LIST_MAX } from "./map";
import { flyToCityJs } from "./fly-to-city-js";

export interface CityViewWords {
  /** The map's own title ("The ancient tree map"). */
  title: string;
  /** Its one line under the title. */
  note: string;
  /** The crumb after Home ("Map"). */
  map: string;
  /** The document title /explore has. */
  docTitle: string;
}

export function cityViewJs(lang: string, explorePath: string, words: CityViewWords): string {
  return `
// ---- ONE MAP (city-view-js.ts) ----
var VIEW = false;
var PLACE_PATH = location.pathname;
var VIEW_PATH = ${JSON.stringify(explorePath)};
var VIEW_WORDS = ${JSON.stringify(words)};
var DATA = null, SHOWN = [], FOCUS = null, PLACE = null, PLACES = {}, COUNTRIES = {}, INTROS = {};
var SP_ICONS = {}, WORDS = null, EMPTY = null, CHEVRON = '', BOX_IC = {};
var _sheet = document.getElementById('sheet');
var _sheetBody = _sheet ? _sheet.querySelector('.sheet-body') : null;
var _viewBody = null, _hiddenByView = [], _headSaved = null, _viewAsked = false, _viewWaiting = [];
// The list's place, hidden until you leave the city: the map's one line in
// the city intro's own block (PlaceIntro.astro), then the list.
if (_sheetBody) {
  _viewBody = document.createElement('div');
  _viewBody.id = 'view-body';
  _viewBody.hidden = true;
  var _ciLede = _sheetBody.querySelector('.lede');
  var _ci = _ciLede ? _ciLede.parentNode : null;
  if (_ci && _ci.classList.contains('city-intro')) {
    var _note = _ci.cloneNode(false);
    _note.removeAttribute('id');
    _note.classList.add('is-open');
    var _lede = document.createElement('p');
    _lede.className = 'lede';
    _lede.textContent = VIEW_WORDS.note;
    _note.appendChild(_lede);
    _viewBody.appendChild(_note);
  }
  var _ep = document.createElement('div');
  _ep.id = 'ex-panel';
  _ep.setAttribute('aria-live', 'polite');
  _viewBody.appendChild(_ep);
  _sheetBody.insertBefore(_viewBody, _sheetBody.firstChild);
}
${viewListJs(EXPLORE_LIST_MAX)}
${flyToCityJs()}
// A city picked in the search (search-form.ts go()): another city is flown to
// and opened there (fly-to-city-js.ts); this city brings its own panel back
// and frames its trees, with Back returning to the list. A country still
// opens /explore on it.
window.atMapPlace = function(kind, key) {
  if (kind !== 'city') { return false; }
  if ('/' + key !== PLACE_PATH) { atFlyToCity(map, key); return true; }
  if (VIEW) {
    toPlace();
    try { history.pushState(null, '', PLACE_PATH + _viewHash()); } catch (e) {}
  }
  if (HOME) { map.fitBounds(HOME, { padding: 70, maxZoom: 13, duration: 900 }); }
  return true;
};
function _viewData(cb) {
  if (DATA) { cb(); return; }
  _viewWaiting.push(cb);
  if (_viewAsked) { return; }
  _viewAsked = true;
  fetch('/api/map-view/${lang}.json').then(function(r) { return r.json(); }).then(function(j) {
    DATA = { type: 'FeatureCollection', features: j.features || [] };
    PLACES = j.places || {}; COUNTRIES = j.countries || {}; INTROS = j.intros || {};
    SP_ICONS = j.icons || {}; WORDS = j.words; EMPTY = j.empty; CHEVRON = j.chevron || ''; BOX_IC = j.boxIc || {};
    if (!SPECIES) { SPECIES = j.species || []; SPECIES_L = j.speciesLatin || []; }
    if (!SP_IC) { SP_IC = j.speciesIcon || null; }
    _viewFilter();
    var w = _viewWaiting; _viewWaiting = [];
    w.forEach(function(f) { f(); });
  }).catch(function() { _viewAsked = false; _viewWaiting = []; });
}
// The filter row keeps the same trees in the list as on the map.
function _viewFilter() {
  if (!DATA) { return; }
  SHOWN = filtersOn() ? DATA.features.filter(function(f) { return keepsTree(f.properties); }) : DATA.features;
}
// Every child of the sheet's body steps aside for the list, the city's foot
// too (its "Know one in Tokyo we missed?" and Plus row are the city's).
function _viewHide(on) {
  if (!_sheetBody || !_viewBody) { return; }
  if (on) {
    _hiddenByView = [];
    Array.prototype.forEach.call(_sheetBody.children, function(el) {
      if (el === _viewBody || el.hidden) { return; }
      el.hidden = true;
      _hiddenByView.push(el);
    });
    _viewBody.hidden = false;
  } else {
    _hiddenByView.forEach(function(el) { el.hidden = false; });
    _hiddenByView = [];
    _viewBody.hidden = true;
  }
}
// The head (PlaceHead.astro) says the map's title while the list shows, and
// the city's again when it goes.
function _viewHead(on) {
  var head = _sheet ? _sheet.querySelector('.place-head') : null;
  if (!head) { return; }
  var h1 = head.querySelector('h1'), nav = head.querySelector('nav'), eb = head.querySelector('.eyebrow');
  var share = head.querySelector('.page-head [data-share]');
  if (on) {
    if (!_headSaved) {
      _headSaved = { h1: h1 ? h1.innerHTML : '', nav: nav ? nav.innerHTML : '', eb: eb ? eb.hidden : true,
        url: share ? share.getAttribute('data-share-url') : '', title: share ? share.getAttribute('data-share-title') : '',
        doc: document.title };
    }
    if (h1) { h1.textContent = VIEW_WORDS.title; }
    var first = nav ? nav.querySelector('a') : null;
    if (nav && first) { nav.innerHTML = first.outerHTML + ' › <span>' + _esc(VIEW_WORDS.map) + '</span>'; }
    if (eb) { eb.hidden = true; }
    if (share) { share.setAttribute('data-share-url', location.origin + VIEW_PATH); share.setAttribute('data-share-title', VIEW_WORDS.title); }
    document.title = VIEW_WORDS.docTitle;
  } else if (_headSaved) {
    if (h1) { h1.innerHTML = _headSaved.h1; }
    if (nav) { nav.innerHTML = _headSaved.nav; }
    if (eb) { eb.hidden = _headSaved.eb; }
    if (share) { share.setAttribute('data-share-url', _headSaved.url); share.setAttribute('data-share-title', _headSaved.title); }
    document.title = _headSaved.doc;
  }
}
function _viewHash() {
  var c = map.getCenter();
  return '#map=' + map.getZoom().toFixed(2) + '/' + c.lat.toFixed(5) + '/' + c.lng.toFixed(5);
}
function toView(push) {
  if (VIEW) { return; }
  _viewData(function() {
    if (VIEW) { return; }
    VIEW = true;
    if (mapCard && mapCard.isOpen && mapCard.isOpen()) { mapCard.close(); }
    clearPin();
    _viewHide(true);
    _viewHead(true);
    if (_sheet) { _sheet.classList.add('is-view'); _sheet.scrollTop = 0; }
    try {
      if (push) { history.pushState(null, '', VIEW_PATH + _viewHash()); }
      else { history.replaceState(null, '', VIEW_PATH + _viewHash()); }
    } catch (e) {}
    window.atViewListShow();
  });
}
function toPlace() {
  if (!VIEW) { return; }
  VIEW = false;
  if (mapCard && mapCard.isOpen && mapCard.isOpen()) { mapCard.close(); }
  _viewHide(false);
  _viewHead(false);
  if (_sheet) { _sheet.classList.remove('is-view'); _sheet.scrollTop = 0; }
}
// Leaving the city: any drag or zoom of your own, as on Airbnb, where a move
// of the map turns the list into "within map area" at once. The page's own
// fits, a tapped pin's card and a flight carry no originalEvent and never
// leave it.
// A zoom by wheel, pinch, double click or the + and - buttons does not
// always carry an originalEvent on its zoomstart (a wheel zoom never did,
// found live 2026-11-27), so those inputs are read on the map itself and
// count for the move that ends within a second and a half.
var _viewUserMove = false, _viewZoomAt = 0;
function _viewZoomed() { _viewZoomAt = Date.now(); }
map.on('dragstart', function() { _viewUserMove = true; });
map.on('zoomstart', function(e) { if (e && e.originalEvent) { _viewUserMove = true; } });
(function() {
  var box = map.getContainer();
  box.addEventListener('wheel', _viewZoomed, { passive: true });
  box.addEventListener('dblclick', _viewZoomed);
  box.addEventListener('touchmove', function(e) { if (e.touches && e.touches.length > 1) { _viewZoomed(); } }, { passive: true });
  box.addEventListener('click', function(e) {
    if (e.target.closest && e.target.closest('.maplibregl-ctrl-zoom-in, .maplibregl-ctrl-zoom-out')) { _viewZoomed(); }
  });
})();
map.on('moveend', function() {
  var user = _viewUserMove || Date.now() - _viewZoomAt < 1500;
  _viewUserMove = false;
  if (VIEW || !user) { return; }
  _viewZoomAt = 0;
  toView(true);
});
// Back to the city's address brings its panel back, where you were on it.
window.addEventListener('popstate', function() {
  if (location.pathname === PLACE_PATH && VIEW) {
    toPlace();
    var v = /^#map=([0-9.]+)\\/(-?[0-9.]+)\\/(-?[0-9.]+)$/.exec(location.hash);
    if (v) { map.jumpTo({ zoom: +v[1], center: [+v[3], +v[2]] }); }
    else if (HOME) { map.fitBounds(HOME, { padding: 70, maxZoom: 13 }); }
  } else if (location.pathname === VIEW_PATH && !VIEW) {
    toView(false);
  }
});
`;
}
