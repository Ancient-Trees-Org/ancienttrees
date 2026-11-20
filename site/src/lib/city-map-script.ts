// Ported from city_map_script(), build_site.py:1532-2058. The city page's
// map: tree pins, walk switching (redraw, not navigation), the passport (account-only since 2026-09-02, read through
// visited-sync-js.ts; the ancienttrees_seen key it used to write is gone),
// and "where am I" GPS.
//
// The tick button exists now (2026-09-12): components/SeenButton.astro emits
// .seen-btn into every tree card, and tree-actions-js.ts handles the click by
// delegation, the same way the heart is handled. This file kept the only two
// jobs that are the MAP's: the moss tick on a pin, and the passport counter.
// The click handler and the label painting that used to live here went with
// the change, along with the proximity check they carried, which contradicted
// DECISIONS.md 2026-08-20 ("GPS proximity is a BONUS, never a gate").
//
// Below, cityMapScript() returns its whole body as a template literal that
// ships verbatim as an inline <script> (see mapScript() in ./map): no
// bundler or module graph reaches that text, so nothing in there can import
// from ./walks the way this file's own build-time code does above. That cost
// us a hand-kept copy of the haversine formula until 2026-09-12, when the
// proximity check that needed it went; there is no duplicate of it left here.
import {MAP_STYLE, MAP_CREDIT} from "./site-config";
import { mapScript, pinPriority, PILES_JS, ONE_WORLD } from "./map";
import { treePinsJs } from "./tree-pins-js";
import { distSpan } from "./trees";
import type { WalkMarker, Walk } from "./walks";
import { mapCardJs } from "./map-card-js";
import { mapFiltersJs } from "./map-filters-js";

export interface OtherCity {
  slug: string;
  city: string;
  country: string;
  n: number;
  ph: string | null;
  rank: number;
  lat: number;
  lng: number;
}

/** Where the map opens: the trees that actually cluster, not every outlier
 * (Hidde, 2026-09-24: Singapore opened zoomed far out because one tree, the
 * mangrove apples at Chek Jawa on Pulau Ubin, stands 24 km from the other
 * 33). Every pin still goes on the map and every card stays in the list; only
 * the opening frame ignores a tree that stands far from the rest.
 *
 * The rule, deliberately conservative so a small city is never cropped to
 * three trees: measure each tree's distance from the median point, keep the
 * ones within four times the median of those distances or 10 km, whichever is
 * larger, and only use that core when it drops no more than a quarter of the
 * trees. 10 km is the floor because anything that close already fits a city
 * map at zoom 11. Measured over every published city on the day it was
 * written, it changes the opening frame of 39 of them (Singapore, Hobart,
 * Osaka, London among them) and crops none to fewer
 * than three quarters of its trees.
 *
 * Computed at build time and shipped as two corners, so the inline script
 * does no arithmetic and the city page and the translated city page open on
 * the same frame. Returns null when there is nothing to fit. */
export function homeBounds(markers: { lat: number; lng: number }[]): [[number, number], [number, number]] | null {
  if (markers.length < 2) return null;
  const median = (xs: number[]): number => {
    const s = [...xs].sort((a, b) => a - b);
    const m = Math.floor(s.length / 2);
    return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2;
  };
  const mLat = median(markers.map((m) => m.lat));
  const mLng = median(markers.map((m) => m.lng));
  const km = (m: { lat: number; lng: number }): number => {
    const x = (m.lng - mLng) * Math.cos(((m.lat + mLat) / 2) * Math.PI / 180);
    return 111.32 * Math.hypot(x, m.lat - mLat);
  };
  const dists = markers.map(km);
  const limit = Math.max(4 * median(dists), 10);
  let core = markers.filter((_, i) => dists[i] <= limit);
  if (core.length < 2 || markers.length - core.length > markers.length * 0.25) core = markers;
  const lats = core.map((m) => m.lat);
  const lngs = core.map((m) => m.lng);
  return [[Math.min(...lngs), Math.min(...lats)], [Math.max(...lngs), Math.max(...lats)]];
}

export function cityMapScript(
  markers: WalkMarker[],
  center: [number, number],
  route: Walk | null,
  otherCities: OtherCity[],
  walks: Walk[],
  /** The city's own trees, without its day trips (lib/day-trips.ts). The
   *  opening frame is drawn round these, so Copenhagen opens on Copenhagen
   *  and not on Dyrehaven as well (Hidde, 2026-10-06). */
  inTown?: { lat: number; lng: number }[],
  lang = "en"
): string {
  const data = JSON.stringify(markers);
  // TREES ON ONE SPOT (Hidde, 2026-10-15, the Ajuda dragon tree hidden under
  // the jacarandas' pin) are found in the browser now, by PILES_JS in the one
  // pin set (tree-pins-js.ts), the same as on every map. CONVENTIONS.md, "Two
  // trees on exactly the same spot".
  const routeCoords = JSON.stringify(route && markers.length > 1 ? route.order.map((i) => [markers[i].lng, markers[i].lat]) : []);
  const walksJson = JSON.stringify(
    walks.map((w) => ({
      coords: w.shape ?? w.order.map((i) => [markers[i].lng, markers[i].lat]),
      members: w.order,
      url: w.url ?? "",
      label: w.label ?? "",
      name: w.name ?? "",
      // The distance carries its own kilometres so units-js.ts can say it in
      // miles for a reader whose region reads in miles (2026-09-12).
      meta: `about ${distSpan(w.km)}, ${w.duration ?? ""} on foot`,
      combined: Boolean(w.combined),
    }))
  );
  // Which tree gets its full pin where two would collide: a photograph
  // first, then readers' saves, then our own order (lib/map.ts pinPriority).
  const pinOrderJson = JSON.stringify(
    markers.map((m, i) => i).sort((a, b) =>
      pinPriority(markers[a].shot, markers[a].saves ?? 0) - pinPriority(markers[b].shot, markers[b].saves ?? 0) || a - b)
  );
  void otherCities;

  const home = homeBounds(inTown && inTown.length >= 2 ? inTown : markers);

  return mapScript(`${PILES_JS}${mapCardJs(lang)}${treePinsJs()}${mapFiltersJs()}
var markers = ${data};
// THE FILTER ROW (lib/map-filters-js.ts), the explore map's, wired here before
// the map for the reason given there (Hidde, 2026-11-01: "put the filters also
// on city map"). A tree the filter leaves out loses its pin, its dot and its
// card in the list; the other places' trees go the same way. The species list
// comes from /api/map-species.json when the chip is first opened.
var SPECIES = null, SPECIES_L = null;
var OFF = markers.map(function() { return false; });
var NEARBY = [];
// The species' pin drawings for the other places' trees, by the index
// /api/pins.json carries (/api/map-species.json icons).
var SP_IC = null;
// THE ONE TREE PIN (tree-pins-js.ts) for this city's trees and every other
// place's, since 2026-11-20 (Hidde: "ik wil gewoon 1 goede"). It replaced this
// map's own DOM pins and the second, circle-pin layer for the neighbours.
var pins = null;
// This city's trees first wherever two collide: pinPriority order inside the
// city, before any neighbour.
function homeFeatures() {
  var out = [];
  markers.forEach(function(m, i) {
    if (OFF[i]) { return; }
    out.push({type: 'Feature', geometry: {type: 'Point', coordinates: [m.lng, m.lat]},
              properties: {id: m.id, ix: i, name: m.name, paid: m.paid ? 1 : 0, home: 1,
                           pr: -1000000 + PIN_ORDER.indexOf(i)}});
  });
  return out;
}
function allFeatures() {
  var near = filtersOn() ? NEARBY.filter(function(f) { return keepsTree(f.properties); }) : NEARBY;
  return homeFeatures().concat(near);
}
function applyCityFilters() {
  var on = filtersOn(), n = 0;
  markers.forEach(function(m, i) {
    var keep = !on || keepsTree({id: m.id, paid: m.paid ? 1 : 0, sp: m.sp});
    OFF[i] = !keep;
    if (keep) { n++; }
    var card = document.getElementById('tree-' + (i + 1));
    if (card) { card.style.display = keep ? '' : 'none'; }
  });
  if (!pins) { atFilterCount(n); return; }
  pins.setData(allFeatures());
  if (pins.selected() === null && typeof mapCard !== 'undefined' && mapCard && mapCard.isOpen()) { mapCard.close(); }
  atFilterCount(n);
}
atMapFilters({
  apply: applyCityFilters,
  items: function() {
    return markers.map(function(m) { return {sp: m.sp, c: [m.lng, m.lat]}; })
      .concat(NEARBY.map(function(f) { return {sp: f.properties.sp, c: f.geometry.coordinates}; }));
  },
  ready: function(cb) {
    if (SPECIES) { cb(); return; }
    fetch('/api/map-species.json').then(function(r) { return r.json(); }).then(function(j) {
      SPECIES = j.names || []; SPECIES_L = j.latin || [];
      cb();
    }).catch(function() {});
  },
  map: function() { return typeof map !== 'undefined' ? map : null; }
});
// The opening frame: the cluster, not every outlier. See homeBounds().
var HOME = ${JSON.stringify(home)};
if (!atCanMap()) return;
var map = new maplibregl.Map({
  container: 'map',
  style: '${MAP_STYLE}',
  center: [${center[1]}, ${center[0]}],
  zoom: 10.5, ${ONE_WORLD},
  scrollZoom: true,
  attributionControl: false
});
map.addControl(new maplibregl.AttributionControl({compact: true, customAttribution: ${JSON.stringify(MAP_CREDIT)}}), 'top-left');
map.addControl(new maplibregl.NavigationControl());
map.addControl(new maplibregl.FullscreenControl());
map.on('load', function() { map.resize(); });
new ResizeObserver(function() { map.resize(); }).observe(document.getElementById('map'));
// EVERY TREE IN VIEW, the explore map's way (Hidde, 2026-11-01, zooming out
// from Amsterdam: the neighbours' trees were missing, then every dot was a
// whole city that opened another page). The city map is the explore map
// pointed at this city: other places' trees are drawn as /explore draws them,
// at every zoom, and a tap opens the tree's card, never another page. Since
// 2026-11-20 all of them are one pin set (tree-pins-js.ts) with this city's
// trees ahead where two collide, so a map zoomed out looks the same from every
// page. The other places' rows come from /api/pins.json, fetched once and
// cached.
var HOME_IDS = {};
markers.forEach(function(m) { HOME_IDS[m.id] = 1; });
var PIN_ORDER = ${pinOrderJson};
// The pins go on as soon as the style is there, not at 'load', which waits for
// every tile: the smoke test and a slow phone both see the trees first.
function initPins() {
  if (pins) { return; }
  pins = atTreePins(map, {
    source: 'trees',
    // This city's markers carry their drawing; a neighbour's is looked up by
    // its species index once /api/map-species.json has answered.
    iconOf: function(p) {
      if (p.home) { var m = markers[p.ix]; return m ? m.icon : 'broadleaf'; }
      return (SP_IC && p.sp !== undefined && p.sp !== null && p.sp >= 0 && SP_IC[p.sp]) || 'broadleaf';
    },
    seen: function(p) { return readSeen().indexOf(p.id) !== -1; },
    open: function(p, c) {
      if (p.home) { selectTree(p.ix); return; }
      openTreeCard(p, c);
    }
  });
  openTreeCard = atTreePinCard(map, pins, function(p) {
    if (!p.home) { return null; }
    var card = cardOf(p.ix);
    return card ? { el: card, href: hrefOf(card) } : null;
  });
  mapCard = openTreeCard;
  atPinsFollowList(pins, openTreeCard, null);
  pins.setData(allFeatures());
  Promise.all([
    fetch('/api/pins.json').then(function(r) { return r.json(); }),
    fetch('/api/map-species.json').then(function(r) { return r.json(); }).catch(function() { return null; })
  ]).then(function(got) {
    var rows = got[0], sp = got[1];
    if (sp) {
      SP_IC = sp.icons || null;
      if (!SPECIES) { SPECIES = sp.names || []; SPECIES_L = sp.latin || []; }
    }
    NEARBY = [];
    rows.forEach(function(r) {
      if (HOME_IDS[r[0]]) { return; }
      NEARBY.push({type: 'Feature', geometry: {type: 'Point', coordinates: [r[1], r[2]]},
                   properties: {id: r[0], cs: r[3], pr: r[4], sp: r[5], paid: r[6], mn: r[7]}});
    });
    applyCityFilters();
  }).catch(function() {});
  if (wantTree !== null) { openOnTree(wantTree); }
}
map.on('style.load', initPins);
if (map.isStyleLoaded()) { initPins(); }
// NO "CITIES IN VIEW" ANY MORE (Hidde, 2026-11-20, shown the city map and
// /explore zoomed out side by side: "B, bomen in beeld"). Zoomed out, the
// city map's list turned into a list of other cities, which no other map and
// neither app does; the list now stays this city's trees at every zoom, and
// the other places stay on the map as pins (data/map-parity.json).
if (markers.length > 1) {
  var _b = new maplibregl.LngLatBounds(HOME[0], HOME[1]);
  var _el = document.getElementById('map');
  var _pad = Math.max(30, Math.min(90, Math.floor(Math.min(_el.clientWidth, _el.clientHeight) * 0.16)));
  map.fitBounds(_b, { padding: _pad, maxZoom: 14.5, duration: 0 });
}

// The opened tree, as an index into markers (a neighbour's tree is -1).
var activeIdx = -1;
function setActive(idx, fly, scroll, noSheet) {
  // Selecting a tree OUTSIDE the chosen walk releases the walk instead of
  // leaving the tree dimmed under it (Hidde, 2026-08-14: "the tree stays in
  // opacity mode instead of jumping out of the hike and towards the tree").
  // The person's intent moved from the route to the tree; the filter follows.
  if (typeof activeWalk !== 'undefined' && activeWalk >= 0 && WALKS[activeWalk] &&
      WALKS[activeWalk].members.indexOf(idx) === -1) {
    showWholeCity();
  }
  activeIdx = idx;
  var m = markers[idx];
  if (pins) { pins.select(m.id); }
  var card = cardOf(idx);
  // On a phone the cards live inside the bottom sheet, and picking a tree
  // means opening THAT tree rather than scrolling a list behind a map. The
  // sheet publishes this hook; on desktop it is undefined and nothing changes.
  if (card && window.atSheetFocus && !noSheet) { window.atSheetFocus(card.dataset.treeId); }
  if (card && scroll) { card.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }
  // A tree centred in the map element is a tree hidden behind the sheet, since
  // the sheet covers the lower half of it. Maps recentres on the part of the
  // map you can still see, so this does too: the offset moves the target up by
  // half the difference between the element's centre and the visible centre.
  var flyOffset = [0, 0];
  if (fly && window.atSheetTop) {
    var sheetTop = window.atSheetTop();
    var mapEl = document.getElementById('map');
    if (sheetTop !== null && mapEl) {
      var mr = mapEl.getBoundingClientRect();
      var visibleMid = (mr.top + Math.min(mr.bottom, sheetTop)) / 2;
      flyOffset = [0, Math.round(visibleMid - (mr.top + mr.bottom) / 2)];
    }
  }
  if (fly === 'keep') { map.easeTo({ center: [m.lng, m.lat], duration: 600, offset: flyOffset }); }
  else if (fly) { map.flyTo({ center: [m.lng, m.lat], zoom: 14.5, duration: 1200, offset: flyOffset }); }
}

// --- a tapped pin -------------------------------------------------------------
var phoneMq = window.matchMedia('(max-width: 800px)');
function cardOf(idx) { return document.getElementById('tree-' + (idx + 1)); }
function hrefOf(card) { var a = card && card.querySelector('.tree-name a'); return a ? a.href : null; }
function clearPin() {
  activeIdx = -1;
  if (pins) { pins.select(null); }
}
// THE CARD OF A TAPPED PIN is the one every map shows (map-card-js.ts, through
// tree-pins-js.ts atTreePinCard): this page hands it the tree's own card from
// the list, and the card lets the pin go when it closes.
var openTreeCard = null;
var mapCard = null;
// A tap on the map with no card open still lets a phone's pin go (the sheet's
// own listener drops the sheet back to the list).
map.on('click', function() { if (!(mapCard && mapCard.isOpen()) && phoneMq.matches) clearPin(); });

// A PIN SHOWS AIRBNB'S CARD on a phone and on a desktop (Hidde, 2026-10-24:
// "de nieuwe preview pinnen a la airbnb zijn er niet op mobile web"),
// replacing 10-20's sheet that became the tree (Apple Maps; the app keeps
// that). On a phone the sheet drops to its peek first (inside the card's open).
function selectTree(idx) {
  var m = markers[idx];
  setActive(idx, false, false, true);
  if (openTreeCard) { openTreeCard({ id: m.id, ix: idx, home: 1, name: m.name }, [m.lng, m.lat]); }
}
// On a phone the open card's photograph is the way into the tree page, and
// the cross (.sheet-back, which sheet-js.ts closes the tree on) lets the pin go.
document.addEventListener('click', function(e) {
  if (!phoneMq.matches) return;
  if (e.target.closest('.sheet-back')) { clearPin(); return; }
  var photo = e.target.closest('.panel.is-detail .tree-card.is-open .tree-card-photo');
  if (photo && !e.target.closest('.heart-card')) {
    var href = hrefOf(photo.closest('.tree-card')); if (href) window.location.href = href;
  }
});

// TREES ON ONE SPOT: ZOOM IN, THEN SPREAD (Hidde, 2026-10-15) is the one
// pin set's now (PILES_JS through tree-pins-js.ts), the same on every map.
if (markers.length > 1) { map.fitBounds(HOME, { padding: 70, maxZoom: 13 }); }
// The map keeps its place in the address (#map=zoom/lat/lng), as /explore
// does, so back from a tree page lands where you were (Hidde, 2026-11-01).
var _view = /^#map=([0-9.]+)\\/(-?[0-9.]+)\\/(-?[0-9.]+)$/.exec(location.hash);
if (_view) { map.jumpTo({zoom: +_view[1], center: [+_view[3], +_view[2]]}); }
map.on('moveend', function() {
  if (location.hash && location.hash.indexOf('#map=') !== 0) { return; }
  var c = map.getCenter();
  try { history.replaceState(null, '', location.pathname + location.search + '#map=' +
    map.getZoom().toFixed(2) + '/' + c.lat.toFixed(5) + '/' + c.lng.toFixed(5)); } catch (e) {}
});
// A tap on a card OPENS the tree since 2026-10-04 (TreeCard.astro: the whole
// card is one link, as in the app and on AllTrails and Airbnb). What the list
// still does for the map is AllTrails' and Airbnb's web half: on a desktop,
// pointing at a card or a Highlights photograph lights its pin, without flying
// anywhere (Hidde, 2026-11-10). atPinsFollowList, wired on load.

var routeCoords = ${routeCoords};
// OPEN ON ONE TREE (2026-09-24). A tree page's map, expanded, lands here with
// #tree=<id>, the web's version of the app's full-map button on its tree page:
// the whole city around it, with this tree selected rather than a map that
// forgets which tree you came from. Read now, acted on once the pins exist.
var wantTree = location.hash.indexOf('#tree=') === 0 ? decodeURIComponent(location.hash.slice(6)) : null;
function addWalkLayer() {
  if (routeCoords.length < 2 || map.getSource('walk')) { return; }
  map.addSource('walk', {
    type: 'geojson',
    data: { type: 'Feature', geometry: { type: 'LineString', coordinates: routeCoords } }
  });
  map.addLayer({
    id: 'walk-casing', type: 'line', source: 'walk',
    layout: { 'line-cap': 'round', 'line-join': 'round' },
    paint: { 'line-color': '#fff', 'line-width': 8, 'line-opacity': 0.85 }
  });
  map.addLayer({
    id: 'walk', type: 'line', source: 'walk',
    layout: { 'line-cap': 'round', 'line-join': 'round' },
    paint: { 'line-color': '#3D5C1E', 'line-width': 4.5, 'line-opacity': 0.95,
              'line-dasharray': [1.4, 1.1] }
  });
}
if (map.isStyleLoaded()) { addWalkLayer(); } else { map.on('styledata', addWalkLayer); }

function addAllWalksLayer() {
  if (WALKS.length < 2 || map.getSource('walks-all')) { return; }
  map.addSource('walks-all', {
    type: 'geojson',
    // The combined option is the sum of lines already on the map: drawing it
    // grey as well would double every segment, so only the real walks show.
    data: { type: 'FeatureCollection', features: WALKS.map(function(w, i) {
      return { type: 'Feature', properties: { idx: i },
               geometry: { type: 'LineString', coordinates: w.coords } };
    }).filter(function(f) { return !WALKS[f.properties.idx].combined; }) }
  });
  map.addLayer({
    id: 'walks-all-hit', type: 'line', source: 'walks-all',
    layout: { 'line-cap': 'round', 'line-join': 'round' },
    paint: { 'line-color': '#000', 'line-width': 16, 'line-opacity': 0.001 }
  });
  map.addLayer({
    id: 'walks-all-casing', type: 'line', source: 'walks-all',
    layout: { 'line-cap': 'round', 'line-join': 'round' },
    paint: { 'line-color': '#fff', 'line-width': 7, 'line-opacity': 0.7 }
  });
  map.addLayer({
    id: 'walks-all', type: 'line', source: 'walks-all',
    layout: { 'line-cap': 'round', 'line-join': 'round' },
    paint: { 'line-color': '#4b5563', 'line-width': 3, 'line-opacity': 0.3,
              'line-dasharray': [1.4, 1.1] }
  });
  map.on('click', 'walks-all-hit', function(e) {
    if (e.features && e.features.length) { selectWalk(e.features[0].properties.idx); }
  });
  map.on('mouseenter', 'walks-all-hit', function() { map.getCanvas().style.cursor = 'pointer'; });
  map.on('mouseleave', 'walks-all-hit', function() { map.getCanvas().style.cursor = ''; });
}
function setAllWalksFilter(activeIdx) {
  // Hide the grey copy of whatever is selected, so the chosen walk shows once
  // in green rather than twice in two colours.
  if (!map.getLayer('walks-all')) { return; }
  // Selecting the combined option hides every grey copy: its green line
  // covers all of them, and grey under green reads as a third walk.
  var f = activeIdx < 0 ? null
        : (WALKS[activeIdx] && WALKS[activeIdx].combined) ? ['==', ['get', 'idx'], -1]
        : ['!=', ['get', 'idx'], activeIdx];
  map.setFilter('walks-all', f);
  map.setFilter('walks-all-hit', f);
  if (map.getLayer('walks-all-casing')) { map.setFilter('walks-all-casing', f); }
}
if (map.isStyleLoaded()) { addAllWalksLayer(); } else { map.on('styledata', addAllWalksLayer); }

var WALKS = ${walksJson};
var wantCoords = [];
function drawWalk(coords) {
  wantCoords = coords;
  var src = null;
  try { src = map.getSource('walk'); } catch (e) { src = null; }
  if (src) {
    src.setData({ type: 'Feature', geometry: { type: 'LineString', coordinates: coords } });
    return;
  }
  if (!map.isStyleLoaded()) {
    map.once('styledata', function() { drawWalk(wantCoords); });
    return;
  }
  addWalkLayer();
}
function selectWalk(idx) {
  var w = WALKS[idx];
  if (!w) { return; }
  activeWalk = idx;
  setAllWalksFilter(idx);
  routeCoords = w.coords;
  drawWalk(w.coords);
  var go = document.getElementById('route-go');
  if (go) { go.href = w.url; }
  var lab = document.getElementById('route-label');
  if (lab) { lab.textContent = w.label; }
  var meta = document.getElementById('route-meta');
  // innerHTML rather than textContent: the line carries a .dist span so a
  // reader in miles gets miles (2026-09-12). Everything in it is ours,
  // generated from the walk itself.
  if (meta) { meta.innerHTML = w.meta; if (window.atPaintUnits) window.atPaintUnits(); }
  var nm = document.querySelector('.route-name');
  if (nm) { nm.textContent = w.name; nm.hidden = !w.name; }
  var on = {};
  w.members.forEach(function(i) { on[i] = true; });
  if (pins) { pins.dim(markers.filter(function(m, i) { return !on[i]; }).map(function(m) { return m.id; })); }
  document.querySelectorAll('.tree-card').forEach(function(card, i) {
    card.classList.toggle('card-off', !on[i]);
  });
  document.querySelectorAll('.walk-pick').forEach(function(b, i) {
    b.classList.toggle('is-on', i === idx);
    b.setAttribute('aria-pressed', i === idx ? 'true' : 'false');
  });
  if (w.coords.length > 1) {
    var bb = new maplibregl.LngLatBounds();
    w.coords.forEach(function(c) { bb.extend(c); });
    map.fitBounds(bb, { padding: 70, maxZoom: 15 });
  }
}
var activeWalk = -1;
function showWholeCity() {
  activeWalk = -1;
  setAllWalksFilter(-1);
  drawWalk([]);
  if (pins) { pins.dim(null); }
  document.querySelectorAll('.tree-card').forEach(function(card) {
    card.classList.remove('card-off');
  });
  document.querySelectorAll('.walk-pick').forEach(function(b) {
    b.classList.remove('is-on');
    b.setAttribute('aria-pressed', 'false');
  });
  // The bar goes back to the lead walk too, or deselecting leaves it naming a
  // walk no chip shows as chosen ("Both walks" with nothing selected).
  var w0 = WALKS[0];
  if (w0) {
    routeCoords = w0.coords;
    var go = document.getElementById('route-go');
    if (go) { go.href = w0.url; }
    var lab = document.getElementById('route-label');
    if (lab) { lab.textContent = w0.label; }
    var meta = document.getElementById('route-meta');
    if (meta) { meta.innerHTML = w0.meta; if (window.atPaintUnits) window.atPaintUnits(); }
    var nm = document.querySelector('.route-name');
    if (nm) { nm.textContent = w0.name; nm.hidden = !w0.name; }
  }
  if (markers.length > 1) { map.fitBounds(HOME, { padding: 70, maxZoom: 13 }); }
}
document.querySelectorAll('.walk-pick').forEach(function(btn) {
  btn.addEventListener('click', function() {
    var idx = parseInt(btn.getAttribute('data-walk'), 10);
    if (idx === activeWalk) { showWholeCity(); } else { selectWalk(idx); }
  });
});
if (WALKS.length === 1 && WALKS[0].coords.length > 1) {
  drawWalk(WALKS[0].coords);
} else if (WALKS.length > 1) {
  drawWalk([]);
}

// THE LOG LIVES IN THE ACCOUNT (2026-09-02). It used to live in
// localStorage under ancienttrees_seen, with the account as a copy merged as
// a union; Hidde ended that: "alles wat wordt opgeslagen, moet op je account
// zijn." visited-sync-js.ts holds this page's copy of the answer in memory
// and writes every tick straight through.
function readSeen() {
  return (window.atVisited ? window.atVisited() : []);
}
function writeSeen(changed, on) {
  if (changed && window.atPushVisited) { window.atPushVisited(changed, on); }
}
window.atPaintPassport = function() { try { paintPassport(); } catch (e) {} };

// The bookmark and the tick on a pin are the one pin set's (tree-pins-js.ts):
// a save or a tick repaints them through atPaintPinFaves and atPaintSeen.
function paintPassport() {
  var seen = readSeen();
  var here = 0;
  markers.forEach(function(m, idx) {
    var got = seen.indexOf(m.id) !== -1;
    if (got) { here++; }
  });
  if (pins) { pins.marks(); }
  var box = document.getElementById('passport');
  if (box) {
    document.getElementById('passport-count').textContent = here;
    box.hidden = here === 0;
    box.classList.toggle('complete', here === markers.length);
    // The line under the count is a link to the collection, in the page's
    // language (Hidde, 2026-10-19). It used to say "N trees in total, across
    // every city" in English on every language.
  }
}

// THE #trees= TRANSFER LINK IS GONE (2026-09-02), along with the button that
// made one. It existed to move a log between devices while the log lived in a
// browser and nothing else; the account does that now, and better. Keeping it
// would mean an unauthenticated url could write into somebody's collection,
// which is the opposite of "everything behind an account". An old link simply
// does nothing, which is the right failure: nobody loses anything, because
// whatever it carried is already in the account it was signed into.
if (location.hash.indexOf('#trees=') === 0) {
  history.replaceState(null, '', location.pathname + location.search);
}

paintPassport();

// The #tree=<id> arrival (wantTree, above), once the pins exist.
function openOnTree(want) {
  for (var ti = 0; ti < markers.length; ti++) {
    if (markers[ti].id === want) { setActive(ti, true, false); return; }
  }
}
var gpsBtn = document.getElementById('gps-btn');
var meMarker = null, watchId = null;
if (gpsBtn && navigator.geolocation) {
  gpsBtn.addEventListener('click', function() {
    if (watchId !== null) {
      navigator.geolocation.clearWatch(watchId);
      watchId = null;
      if (meMarker) { meMarker.remove(); meMarker = null; }
      gpsBtn.setAttribute('aria-pressed', 'false');
      gpsBtn.textContent = 'Where am I';
      return;
    }
    gpsBtn.textContent = 'Finding you...';
    watchId = navigator.geolocation.watchPosition(function(pos) {
      var here = [pos.coords.longitude, pos.coords.latitude];
      if (!meMarker) {
        var dot = document.createElement('div');
        dot.className = 'pin-me';
        meMarker = new maplibregl.Marker({ element: dot }).setLngLat(here).addTo(map);
        map.flyTo({ center: here, zoom: 15, duration: 1000 });
      } else {
        meMarker.setLngLat(here);
      }
      gpsBtn.setAttribute('aria-pressed', 'true');
      gpsBtn.textContent = 'Hide me';
    }, function(err) {
      gpsBtn.textContent = err.code === 1 ? 'Location blocked' : 'Location unavailable';
      watchId = null;
      setTimeout(function() { gpsBtn.textContent = 'Where am I'; }, 3000);
    }, { enableHighAccuracy: true, maximumAge: 10000, timeout: 10000 });
  });
} else if (gpsBtn) {
  gpsBtn.hidden = true;
}
`);
}
