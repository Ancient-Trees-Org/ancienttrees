// Ported from map_head()/country_map_script()/single_pin_script(),
// build_site.py:1199-1230ish, 4045-4101. Raw <script>/<link> tags loading
// MapLibre from a CDN, matching the current site exactly rather than going
// through the bundled npm package (see site-config.ts's note on MAPLIBRE_JS).
import {MAPLIBRE_JS, MAPLIBRE_CSS, MAP_STYLE, MAP_CREDIT} from "./site-config";
import { NO_PHOTO_CARD } from "./images";
import { mapCardJs } from "./map-card-js";
import { mapFiltersJs } from "./map-filters-js";
import { ui } from "./i18n";
import { icon } from "./icons";
import { treePinsJs } from "./tree-pins-js";
import { treeCardJs } from "./tree-card";

/** MapLibre, loaded without blocking the page.
 *
 * Until 2026-08-09 every page with a map carried a plain
 * `<script src="unpkg.com/maplibre-gl...">`, which stops the parser dead
 * while a few hundred kilobytes come down from a host that is not ours, on a
 * fresh DNS lookup and TLS handshake. Our own server answers in 33 to 158
 * milliseconds, so that download was most of what a visitor waited for, and
 * 72 percent of our search clicks arrive on a phone.
 *
 * `defer` fixes it without changing behaviour: the browser fetches in
 * parallel, executes after parsing, and deferred external scripts run in
 * document order strictly before DOMContentLoaded. So the init below, moved
 * into a DOMContentLoaded listener, is guaranteed to find `maplibregl`
 * defined. That guarantee is the whole reason this is a wrapper rather than
 * an IntersectionObserver: lazy-until-visible would be faster still and
 * would also stop the map ever building in a headless render, which is what
 * the smoke test checks. */
/** The five seconds (2026-09-12, Hidde: "does it need to be visible, is rather
 * not show it"). It does need to be reachable and it does not need to be read.
 * The OSMF attribution guideline of 2021-06-25 allows a credit to collapse
 * "automatically on map interaction such as panning, clicking, or zooming" or
 * "automatically after five seconds", on one condition: "If the attribution has
 * been collapsed, the user must still be able to find the licence information
 * if they look for it, for example from an '(i)' button in the corner of the
 * map." MapLibre already does the first half on a touch; a visitor who never
 * touches the map was left reading a band across the top forever.
 *
 * So: five seconds, then it is a 24 point (i) and nothing else. That is the
 * floor rather than a preference. OpenFreeMap's own terms say plainly
 * "Attribution is required", and the guideline's collapsed state still wants
 * the (i) there, so it cannot go altogether. */
const COLLAPSE_ATTRIBUTION = `
setTimeout(function () {
  var list = document.querySelectorAll('.maplibregl-ctrl-attrib');
  for (var i = 0; i < list.length; i++) {
    list[i].classList.remove('maplibregl-compact-show');
    if (list[i].tagName === 'DETAILS') { list[i].open = false; }
  }
}, 5000);`;


/** WHICH PINS SHOW: THE AIRBNB WAY, ON EVERY MAP (Hidde, 2026-10-24: "doe de
 *  Airbnb-manier overal: volledige pins voor wat past, kleine stippen voor de
 *  rest, nooit bubbels, een tik opent altijd de boom. Web en app.").
 *
 *  Looked at the same day (CONVENTIONS.md, "How close two pins have to be"):
 *  Airbnb never piles listings into a counted bubble at any zoom. It draws
 *  a ranked handful of full pins, small unlabelled dots for the rest, and
 *  zooming in draws more; a tap always opens a listing and nothing zooms for
 *  you. Google Maps draws every result pin, overlapping where it must, no
 *  counts. The counted bubbles this replaced (2026-10-04 to 10-24) were
 *  MapKit's and the web clustering libraries' default, and Hidde's verdict on
 *  them: "je wil ook niet nodeloos bubbels openklikken en je wil trouwens ook
 *  niet dat je altijd inzoomt bij bubbels klikken."
 *
 *  So every map draws every tree, and the only question is which get the
 *  full pin: a tree with a photograph before one without, then the one more
 *  readers saved (`pr` on the feature, pinPriority(); Airbnb ranks by what
 *  you are likely to book, we rank by what is worth the walk), then our own
 *  order, and a pin that would collide
 *  with one already placed is drawn as a dot instead. PIN_DISTANCE is the
 *  collision rule, centre to centre, the same 40 the app uses (TreeMap.swift,
 *  pinDistance) and supercluster's own default. Every map places them the
 *  same way since 2026-11-20 (tree-pins-js.ts, the one tree pin); until then
 *  the circle-pin maps used MapLibre's symbol collision and the city map its
 *  own pass over DOM pins. The one bubble left is a same-spot stack, below.
 *  qa: check_every_map_shows_pins_the_same_way(). */
export const PIN_DISTANCE = 40;

/** WHICH TREE GETS THE FULL PIN where two collide, as a sort key, lower
 *  first: a photograph before none, and among equals the tree more readers
 *  saved to Want to go (Hidde, 2026-10-24: "i think photo and likes are the
 *  best way"; saves from data/tree-saves.json, lib/saves.ts). The app's
 *  TreeMap.swift pinPriority is the same arithmetic; qa holds the two equal.
 *  Kept small so a feature carries one short number. */
export function pinPriority(hasPhoto: boolean, saves: number): number {
  return (hasPhoto ? 0 : 100000) - Math.min(Math.max(0, Math.round(saves)), 99999);
}

/** ZOOMED OUT, THE AIRBNB SPLIT (Hidde, 2026-11-03, design B, after "dit
 *  voelt gewoon incompleet" about an even spread of dots). Airbnb's map shows
 *  a few full pins for the listings most likely to be booked and "smaller
 *  ovals without price" (mini-pins) for the next tier, each at its real
 *  place, and nothing for the rest (airbnb.tech, "Improving Search Ranking
 *  for Maps"). Below FAR_ZOOM ours does the same: full pins at least
 *  FAR_PIN_DISTANCE apart, a mini pin for half the photographed trees, the
 *  rest left out; from FAR_ZOOM in, every tree as before. The half is fixed
 *  per tree (its id), so the same trees stand there every visit. Decided here
 *  only: the web maps read `mn` off each point, the app reads `mini` from the
 *  feed (app-feed.ts). */
export const FAR_ZOOM = 6.5;
export const FAR_PIN_DISTANCE = 90;
export const MINI_RADIUS = 3;
export function miniPin(id: string, hasPhoto: boolean): boolean {
  if (!hasPhoto) return false;
  let sum = 0;
  for (const ch of id) sum += ch.codePointAt(0) ?? 0;
  return sum % 2 === 0;
}
/** ONE WORLD ON EVERY MAP (Hidde, 2026-07-29: "ik hoef niet 2 werelden te
 *  zien"; again 2026-11-03, after the city map could be zoomed out to several
 *  worlds). Every maplibregl.Map on the site takes ONE_WORLD: no world copies,
 *  and a zoom floor at which one world still fills a phone. The app's
 *  TreeMap.swift worldMinZoom is the same number; qa holds the two equal
 *  (check_every_map_shows_one_world()). */
export const WORLD_MIN_ZOOM = 1.5;
export const ONE_WORLD = `renderWorldCopies: false, minZoom: ${WORLD_MIN_ZOOM}`;

/** THE ONE PIN, WEB AND APP (Hidde, 2026-11-20: "B, de app-pin", then
 *  "maken we hier gelijk ook 1 component van?"). Two codebases cannot share
 *  one drawing, so they share its numbers: the website draws the pin from
 *  these (tree-pins-js.ts writes its CSS from them) and qa
 *  check_every_map_shows_pins_the_same_way() refuses a push where
 *  TreeMap.swift draws a different one. The app's pin, measured that day: a
 *  moss disc (UIColor 0.20/0.35/0.20) 34 across in a 3pt white ring, the
 *  species in white at 20, 1.5 times the size when chosen; a dot is a moss
 *  disc of radius 4 in a 1.5 white ring. */
export const PIN_SPEC = {
  fill: "#335933",
  ring: "#ffffff",
  size: 34,
  ringWidth: 3,
  glyph: 20,
  chosenScale: 1.5,
  dotRadius: 4,
  dotRing: 1.5,
} as const;

/** The same-spot stack's bubble (CONVENTIONS.md 2026-10-15), 26px plus ring,
 *  the app's stackPin at 32 points. */
export const STACK_RADIUS = 13;
/** From this zoom a same-spot stack is its bubble; below it the stack is one
 *  ordinary pin, because below it two pins a street apart would overlap
 *  anyway and the bubble would read as the clustering we no longer do. The
 *  same number as the app's stackZoom (TreeMap.swift). */
export const STACK_ZOOM = 14;

/** TREES ON ONE SPOT, on every map (Hidde, 2026-10-15: "map interaction need
 *  to stay consistent so do everywhere"). The city map and the app do it
 *  first (spreadStack() in city-map-script.ts, MapLayers.spread in
 *  TreeMap.swift); this is the same behaviour for maps that draw trees as
 *  circles in a GeoJSON source: /explore, the country maps, My trees.
 *
 *  Trees on one coordinate drew one dot over the other with only the top one
 *  reachable, and no zoom parts them.
 *  So before the data goes in, atMarkPiles() gives every feature a `pile`:
 *  0 alone, n on the one feature that stands for a pile of n, -1 on the rest.
 *  The tree layer draws pile 0 only; atPileLayers() adds a bubble (the
 *  cluster's own) for the rest. A tap flies to zoom 17 on the spot and the
 *  dots spring apart round it on thin legs, Leaflet's spiderfy; a dot opens
 *  its tree through `open`; a tap on the map or your own zoom folds them.
 *  Clusters still count every tree, hidden ones included.
 *  CONVENTIONS.md, "Two trees on exactly the same spot". */
export const PILES_JS = `
// The piles as the DATA has them. Never read back from the map: a feature
// from the map's tiles has its coordinate rounded to the tile grid, so it no
// longer matches its own spot (the app's first tap only zoomed because of
// this, 2026-10-15).
var atPiles = [];
function atPileKey(c) { return c[1].toFixed(5) + ',' + c[0].toFixed(5); }
function atMarkPiles(features) {
  var by = {};
  features.forEach(function(f) {
    var c = f.geometry && f.geometry.coordinates;
    if (!c || c[0] == null || c[1] == null) { return; }
    var k = atPileKey(c);
    (by[k] = by[k] || []).push(f);
  });
  atPiles = [];
  Object.keys(by).forEach(function(k) {
    var g = by[k];
    g.forEach(function(f, i) { f.properties.pile = g.length < 2 ? 0 : (i === 0 ? g.length : -1); f.properties.pk = k; });
    if (g.length > 1) { atPiles.push({c: g[0].geometry.coordinates.slice(), fs: g}); }
  });
  return features;
}
// pinEl(feature), when given, makes the full pin a spread stack fans out
// (tree-pins-js.ts: the one tree pin), on legs that stop at the pin's edge;
// without it the fan is of dots.
function atPileLayers(map, source, treeLayer, open, hollow, pinEl) {
  var pileOnly = ['all', ['!', ['has', 'point_count']], ['>=', ['coalesce', ['get', 'pile'], 0], 2]];
  if (map.getLayer(treeLayer)) {
    map.setFilter(treeLayer, ['all', ['!', ['has', 'point_count']], ['==', ['coalesce', ['get', 'pile'], 0], 0]]);
  }
  // The bubble only from STACK_ZOOM; below it the stack is one ordinary pin
  // (tree-pins-js.ts draws the pile's first tree there).
  map.addLayer({id: treeLayer + '-pile', type: 'circle', source: source, filter: pileOnly, minzoom: ${STACK_ZOOM},
    paint: {'circle-color': '#4A6B2A', 'circle-opacity': 0.92, 'circle-radius': ${STACK_RADIUS},
            'circle-stroke-width': 2, 'circle-stroke-color': '#F6F2E9'}});
  map.addLayer({id: treeLayer + '-pile-n', type: 'symbol', source: source, filter: pileOnly, minzoom: ${STACK_ZOOM},
    layout: {'text-field': ['to-string', ['get', 'pile']], 'text-font': ['Noto Sans Regular'],
             'text-size': 12, 'text-allow-overlap': true},
    paint: {'text-color': '#F6F2E9'}});
  var spread = [], tapAt = 0;
  // The bubble is a map layer, so while its pile is spread it is filtered out.
  function showBubbles(except) {
    var f = except ? ['all', pileOnly, ['!=', ['get', 'pk'], except]] : pileOnly;
    map.setFilter(treeLayer + '-pile', f);
    map.setFilter(treeLayer + '-pile-n', f);
  }
  function fold() {
    if (!spread.length) { return; }
    spread.forEach(function(m) { m.remove(); });
    spread = [];
    showBubbles(null);
  }
  function fan(pile) {
    fold();
    var c = pile.c, g = pile.fs, n = g.length;
    // Full pins stand further out than dots, and their legs stop at the pin's
    // edge (17 is half a pin), as the city map's spread always did.
    var R = pinEl ? (n <= 2 ? 36 : 44) : (n <= 2 ? 24 : 30), edge = pinEl ? 17 : 9;
    showBubbles(atPileKey(c));
    var legs = document.createElement('div');
    legs.className = 'stack-legs-host';
    var html = '<i class="stack-dot"></i>';
    var made = [];
    g.forEach(function(f, i) {
      var a = n === 2 ? Math.PI * i : -Math.PI / 2 + i * 2 * Math.PI / n;
      html += '<i class="stack-leg" style="width:' + (R - edge) + 'px;transform:rotate(' + (a * 180 / Math.PI) + 'deg)"></i>';
      var d;
      if (pinEl) {
        d = pinEl(f);
        d.setAttribute('role', 'button');
        d.tabIndex = 0;
      } else {
        d = document.createElement('button');
        d.type = 'button';
        d.className = 'pile-dot' + (hollow && hollow(f.properties) ? ' pile-dot--hollow' : '');
      }
      made.push(d);
      if (f.properties.name) { d.setAttribute('aria-label', f.properties.name); d.title = f.properties.name; }
      d.addEventListener('click', function(e) {
        e.stopPropagation(); tapAt = Date.now();
        if (pinEl) { made.forEach(function(x) { x.classList.toggle('active', x === d); }); }
        open(f.properties, c);
      });
      spread.push(new maplibregl.Marker({element: d, offset: [Math.round(R * Math.cos(a)), Math.round(R * Math.sin(a))]})
        .setLngLat(c).addTo(map));
    });
    legs.innerHTML = html;
    spread.unshift(new maplibregl.Marker({element: legs}).setLngLat(c).addTo(map));
  }
  map.on('click', treeLayer + '-pile', function(e) {
    tapAt = Date.now();
    // The nearest pile on screen to the tap: the bubble was drawn there.
    var best = null, bestD = 30 * 30;
    atPiles.forEach(function(p) {
      var q = map.project(p.c), dx = q.x - e.point.x, dy = q.y - e.point.y;
      if (dx * dx + dy * dy < bestD) { bestD = dx * dx + dy * dy; best = p; }
    });
    if (!best) { return; }
    if (map.getZoom() >= 16.5) { fan(best); return; }
    map.easeTo({center: best.c, zoom: 17, duration: 900});
    setTimeout(function() { fan(best); }, 950);
  });
  map.on('click', function() { if (Date.now() - tapAt > 400) { fold(); } });
  map.on('zoomstart', function(e) { if (e.originalEvent) { fold(); } });
  map.on('mouseenter', treeLayer + '-pile', function() { map.getCanvas().style.cursor = 'pointer'; });
  map.on('mouseleave', treeLayer + '-pile', function() { map.getCanvas().style.cursor = ''; });
}`;

export function mapScript(body: string): string {
  return `\n<script defer src="${MAPLIBRE_JS}"></script>\n<script>\n` +
    `document.addEventListener("DOMContentLoaded", function () {\n${CAN_MAP_JS}\n${body}\n${COLLAPSE_ATTRIBUTION}\n});\n</script>\n`;
}

/** Whether this browser can draw a MapLibre map at all. Without WebGL the
 * Map constructor throws "Failed to initialize WebGL", which stopped every
 * line after it: on a tree page, Back, Take me there and Show us where it is
 * (web_errors, 2026-11-04, Chrome 149 on a tree page). Every map is created
 * behind atCanMap(); a page without one keeps everything else working and
 * its map box simply stays empty, as it did before. Asked once per page.
 * The library itself is asked first: a script that never arrived (a dropped
 * connection) or that the browser cannot parse (Chrome 75) leaves no
 * maplibregl, and the first use of it stopped the page the same way
 * (web_errors, 2026-11-10 and 11-11, /hong-kong, /assen, a Waremme tree). */
export const CAN_MAP_JS = `
function atCanMap() {
  if (atCanMap.v === undefined) {
    try {
      var c = document.createElement('canvas');
      atCanMap.v = !!(window.maplibregl && window.WebGLRenderingContext &&
        (c.getContext('webgl2') || c.getContext('webgl') || c.getContext('experimental-webgl')));
    } catch (e) { atCanMap.v = false; }
  }
  return atCanMap.v;
}
`;

/** MapLibre's stylesheet. The `preconnect` to unpkg.com that used to sit here
 * went with the vendoring on 2026-08-16 (see site-config.ts): warming a
 * connection to a host we no longer call is a wasted DNS lookup, and our own
 * origin is already connected.
 * The street tiles come from tiles.openfreemap.org three hops into the load
 * (our style, then its TileJSON, then the tiles), so that connection is warmed
 * here, once, for every map page (2026-11-04: about 100 ms on a cold visit on
 * broadband, more on a phone). `crossorigin` because MapLibre fetches in CORS
 * mode without credentials; a preconnect of the other kind is not reused. */
export function mapHead(): string {
  return `<link rel="preconnect" href="https://tiles.openfreemap.org" crossorigin>`
    + `<link rel="stylesheet" href="${MAPLIBRE_CSS}">`;
}

/** A single-pin map: the tree page's own map, ported from
 * single_pin_script(), build_site.py:1203-1219. */
export function singlePinScript(lat: number, lng: number): string {
  return mapScript(`
if (!atCanMap()) return;
var map = new maplibregl.Map({
  container: 'map', style: '${MAP_STYLE}',
  center: [${lng}, ${lat}], zoom: 14.5, scrollZoom: false, ${ONE_WORLD},
  attributionControl: false
});
map.addControl(new maplibregl.AttributionControl({compact: true, customAttribution: ${JSON.stringify(MAP_CREDIT)}}), 'top-left');
map.addControl(new maplibregl.NavigationControl());
map.on('load', function() { map.resize(); });
var el = document.createElement('div');
// A dot, not a numbered pill. There is exactly one pin on this map, so a "1"
// on it was never telling anybody anything.
el.className = 'pin pin-dot';
new maplibregl.Marker({ element: el }).setLngLat([${lng}, ${lat}]).addTo(map);
`);
}

export interface CountryMapCity {
  slug: string;
  city: string;
  count: number;
  /** pinPriority(): which tree gets the full pin first. sp: index into
   *  /api/map-species.json (mapSpecies()), paid: behind a ticket; both only
   *  for the filter row. */
  markers: { lat: number; lng: number; url?: string; pr?: number; id?: string; sp?: number; paid?: boolean;
             /** The drawing on its pin (species-icons.ts speciesIconKey). */
             ic?: string }[];
}

/** Every tree in the country, drawn the way /explore and the app draw them
 *  (tree-pins-js.ts): a pin or a dot per tree, and either opens its tree.
 *
 *  `sheet`: the map is the page, the city page's split with the bottom sheet
 *  (the country page since 2026-11-04, Hidde: the website country page a map,
 *  as the app's one map screen for every place). It then scrolls to zoom like
 *  the city map, carries the filter row (MapFilters.astro) and frames the
 *  country above the sheet's peek instead of behind it. Without it the map is
 *  the embedded box it always was (the state pages). */
export function countryMapScript(cities: CountryMapCity[],
                                 frame?: [[number, number], [number, number]],
                                 focus?: [[number, number], [number, number]],
                                 opts: { sheet?: boolean } = {}): string {
  // THE APP'S COUNTRY MAP (Hidde, 2026-10-04, on Italy: "deze stad preview is
  // niet echt mooi trek dit ook gelijk met app"). It was one dot per CITY with
  // its count and its name printed beside it, and in a country with forty
  // cities the names and numbers piled over each other. The app's country
  // page draws its TreeMap instead: every tree, no labels of our own over
  // the base map's. So this is the explore map's pin style and its one rule:
  // a pin or a dot opens its tree.
  const sheet = Boolean(opts.sheet);
  const data = {
    type: "FeatureCollection",
    features: cities.flatMap((c) => c.markers.map((m) => ({
      type: "Feature",
      geometry: { type: "Point", coordinates: [m.lng, m.lat] },
      properties: { id: m.id ?? "", cs: "/" + c.slug, url: m.url ?? "/" + c.slug, pr: m.pr ?? 1,
                    // pinPriority puts a tree with a photograph at 0 or below.
                    mn: miniPin(m.id ?? "", (m.pr ?? 1) <= 0) ? 1 : 0,
                    ...(m.ic && m.ic !== "broadleaf" ? { ic: m.ic } : {}),
                    ...(m.paid ? { paid: 1 } : {}),
                    ...(sheet ? { sp: m.sp ?? -1, paid: m.paid ? 1 : 0 } : {}) },
    }))),
  };
  // The filter row, the city map's wiring (city-map-script.ts): set up before
  // the map for the reason map-filters-js.ts gives, re-sourcing the data
  // rather than hiding a layer, species list fetched when the chip opens.
  const filters = sheet ? `${mapFiltersJs()}
var SPECIES = null, SPECIES_L = null;
function applyCountryFilters() {
  var kept = filtersOn() ? ALL.filter(function(f) { return keepsTree(f.properties); }) : ALL;
  if (typeof pins !== 'undefined' && pins) { pins.setData(kept); }
  atFilterCount(kept.length);
}
atMapFilters({
  apply: applyCountryFilters,
  items: function() { return ALL.map(function(f) { return { sp: f.properties.sp, c: f.geometry.coordinates }; }); },
  ready: function(cb) {
    if (SPECIES) { cb(); return; }
    fetch('/api/map-species.json').then(function(r) { return r.json(); }).then(function(j) {
      SPECIES = j.names || []; SPECIES_L = j.latin || [];
      cb();
    }).catch(function() {});
  },
  map: function() { return typeof map !== 'undefined' ? map : null; }
});
` : "";
  return mapScript(`${PILES_JS}${mapCardJs()}${treePinsJs()}
var ALL = ${JSON.stringify(data)}.features;
var pins = null;
${filters}
var SHEET = ${sheet ? "true" : "false"};
if (!atCanMap()) return;
var map = new maplibregl.Map({
  container: 'map', style: '${MAP_STYLE}',
  center: [0, 0], zoom: 3, ${ONE_WORLD},
  scrollZoom: SHEET, attributionControl: false
});
map.addControl(new maplibregl.AttributionControl({compact: true, customAttribution: ${JSON.stringify(MAP_CREDIT)}}), 'top-left');
map.addControl(new maplibregl.NavigationControl({showCompass: false}));
var b = new maplibregl.LngLatBounds();
ALL.forEach(function(f) { b.extend(f.geometry.coordinates); });
// A country whose cities all hug one border names extra ground to show
// (map_frame in data/countries), so Canada's map is not centred on the US.
var FRAME = ${JSON.stringify(frame ?? null)};
if (FRAME) { b.extend(FRAME[0]); b.extend(FRAME[1]); }
// A country with trees overseas opens on its mainland instead (map_focus):
// Martinique, Tenerife and Hawaii stay on the map, one zoom out away.
var FOCUS = ${JSON.stringify(focus ?? null)};
if (FOCUS) { b = new maplibregl.LngLatBounds(FOCUS[0], FOCUS[1]); }
var touched = false;
// On a phone the sheet's peek covers the bottom of a full-bleed map, so the
// country is framed in the part that shows: above the peek and below the
// filter row (sheet-js.ts says where the sheet comes to rest).
function pad() {
  var p = { top: 36, bottom: 36, left: 36, right: 36 };
  if (!SHEET) { return p; }
  var el = map.getContainer(), h = el.clientHeight;
  p.top = 64;
  var st = window.atSheetTop ? window.atSheetTop() : null;
  if (st !== null && st !== undefined) {
    var top = el.getBoundingClientRect().top;
    p.bottom = Math.max(36, Math.round(top + h - st) + 16);
  }
  // A padding taller than the map makes MapLibre refuse the frame.
  if (p.top + p.bottom > h - 40) { p.top = 36; p.bottom = Math.max(36, h - 120); }
  return p;
}
function fit() {
  if (touched) return;
  var p = pad();
  map.fitBounds(b, { padding: p, maxZoom: 9, duration: 0 });
  // On a phone held upright the width decides the zoom, so the frame sits in
  // the middle with a band of neighbour above and below it: for Canada that
  // lower band was the US and Mexico (Hidde, 2026-09-24). Slide the view north
  // until the frame's southern edge meets the bottom, so the spare height
  // shows more of the country instead of its neighbour.
  if (FRAME) {
    var h = map.getContainer().clientHeight;
    var y = map.project([FRAME[0][0], Math.min(FRAME[0][1], FRAME[1][1])]).y;
    var dy = y - (h - p.bottom - 12);
    if (dy < 0) { map.panBy([0, dy], { duration: 0 }); }
  }
}
map.on('dragstart', function() { touched = true; });
map.on('zoomstart', function(e) { if (e.originalEvent) { touched = true; } });
new ResizeObserver(function() { map.resize(); fit(); }).observe(document.getElementById('map'));
map.on('load', fit);
// The pins go on as soon as the style is there, not at 'load', which waits
// for every tile (as on the city map).
function initPins() {
  if (pins) { return; }
  fit();
  // THE ONE TREE PIN (tree-pins-js.ts), the city map's, since 2026-11-20
  // (Hidde: "ik wil gewoon 1 goede"). A pin or a dot shows the tree's card,
  // the same as on every map (map-card-js.ts).
  var openCard = null;
  pins = atTreePins(map, {
    source: 'trees',
    iconOf: function(p) { return p.ic || 'broadleaf'; },
    open: function(p, c) { if (openCard) openCard(p, c); }
  });
  pins.setData(ALL);
  openCard = atTreePinCard(map, pins, null);
  atPinsFollowList(pins, openCard, null);
  if (SHEET && typeof applyCountryFilters === 'function') { applyCountryFilters(); }
}
map.on('style.load', initPins);
if (map.isStyleLoaded()) { initPins(); }
`);
}

export interface ExploreTreeFeature {
  type: "Feature";
  // Nullable to match Python: a tree with no recorded location still
  // serializes ([None, None] -> [null, null]) rather than crashing the
  // build, exactly like the unfiltered-trees quirk in search-index.json.
  geometry: { type: "Point"; coordinates: [number | null, number | null] };
  properties: {
    id: string; name: string; url: string; cs: string; city: string; age: string; now: 0 | 1;
    /** Behind a ticket. The filter hides these; 241 of 3,055 trees. */
    paid?: 0 | 1;
    /** pinPriority(): which tree gets the full pin where two collide. */
    pr?: number;
    /** miniPin(): drawn as a mini pin when zoomed out. */
    mn: 0 | 1;
    /** Index into the species list the page ships beside the features. An
     *  index rather than the name, because 3,055 copies of "Pedunculate Oak"
     *  is 45KB of the same twelve words. */
    sp?: number;
    /** Its place in its own city's Highlights (lib/highlights.ts), 0 first:
     *  the feed's highlight_rank, so the list under the map orders them the
     *  way the city page and the app do. Only on a highlight. */
    hl?: number;
    /** The short age (age-short.ts), the second half of the row's meta line. */
    as?: string;
  };
}

/** How many rows the list under the explore map draws before it says to
 *  zoom in. The ten city cards it replaced were a cap of the same kind. */
export const EXPLORE_LIST_MAX = 30;

/** What the explore list needs beside the features: per city its name in the
 *  page's language, country and page (empty when it has none), per country
 *  its page, the species silhouettes once and a key per species index, and
 *  the words. */
export interface ExploreListData {
  /** a: somebody already looks after the place (placeHasAmbassador), so its
   *  box asks for "an" ambassador rather than "the". */
  places: Record<string, { n: string; k: string; h: string; a?: number }>;
  countries: Record<string, string>;
  icons: Record<string, string>;
  speciesIcon: string[];
}
export interface ExploreCityRow {
  city: string;
  url: string;
  country: string;
  n: number;
  lat: number;
  lng: number;
  ph: string | null;
  rank: number;
}

/** The /explore world map: every tree as a pin or a dot (tree-pins-js.ts), plus the
 * register layer fetched separately. Ported from the
 * inline `script` string in build_explore_page(), build_site.py:4641-4805. */
export function exploreMapScript(features: ExploreTreeFeature[], cities: ExploreCityRow[],
                                 species: string[] = [], lang = "en", speciesLatin: string[] = [],
                                 list: ExploreListData = { places: {}, countries: {}, icons: {}, speciesIcon: [] }): string {
  const geojson = JSON.stringify({ type: "FeatureCollection", features });
  // A counted string travels as its one-tree form and a template with {n},
  // so the browser fills the number without a rule of its own.
  const U = ui(lang);
  const counted = (fn: (n: number) => string) => ({ one: fn(1), many: fn(98765).replace("98765", "{n}") });
  const words = {
    inView: counted(U.treesInView), all: counted(U.allTrees), highlights: U.highlights,
    more: U.zoomForMore, app: U.readInApp, save: U.cardSave, saved: U.cardSaved,
    credit: U.photoCredit("{c}"),
    collected: U.mapFilterMine, seen: U.seenChip, noPhoto: U.noPhotoYet,
    ambThe: U.ambassadorBecomeThe("{p}"), ambA: U.ambassadorBecomeA("{p}"), plus: U.plusRow,
  };
  const citiesJson = JSON.stringify(cities);
  const speciesJson = JSON.stringify(species);
  const speciesLatinJson = JSON.stringify(speciesLatin);
  return (
    mapScript(
    `${PILES_JS}${mapCardJs(lang)}${treePinsJs()}${treeCardJs()}${mapFiltersJs()}
var DATA = ${geojson};
var CITIES = ${citiesJson};
// The empty map's ask (Hidde, 2026-10-25): the grey card of an empty notes
// section, then the nearest tree. Words in the page's language.
var EMPTY = ${JSON.stringify({ title: ui(lang).emptyPlaceTitle, here: ui(lang).emptyHereTitle,
  ask: ui(lang).emptyPlaceAsk, add: ui(lang).addTree, nearest: ui(lang).nearestTree,
  ic: icon("tree", "regular"), plus: icon("plus", "bold") })};
var SPECIES = ${speciesJson};
var SPECIES_L = ${speciesLatinJson};
// The list under the map (renderPanel, below).
var PLACES = ${JSON.stringify(list.places)};
var COUNTRIES = ${JSON.stringify(list.countries)};
var SP_ICONS = ${JSON.stringify(list.icons)};
var SP_IC = ${JSON.stringify(list.speciesIcon)};
var WORDS = ${JSON.stringify(words)};
var CHEVRON = ${JSON.stringify(icon("caret-right", "bold", "ic city-box-chev"))};
var BOX_IC = ${JSON.stringify({ amb: icon("seal-check", "bold", "ic city-box-ic"), plus: icon("sparkle", "fill", "ic city-box-ic") })};
// The trees the filter row keeps; the list counts only those.
var SHOWN = DATA.features;
// THE FILTER ROW is lib/map-filters-js.ts, shared with the city map; it is
// wired up here, before the map, for the reason it gives.
// FILTERING RE-SOURCES, it does not hide a layer: the same-spot piles are
// marked on the data (atMarkPiles), so what is hidden must leave the data.
function applyFilters() {
  if (typeof pins === 'undefined' || !pins) return;
  var kept = filtersOn() ? DATA.features.filter(function(f) { return keepsTree(f.properties); }) : DATA.features;
  // WHILE A SEARCH HOLDS, ONLY THAT PLACE (Hidde, 2026-11-06, Airbnb's map:
  // the searched place's pins, count and list until you move the map).
  if (typeof FOCUS !== 'undefined' && FOCUS) { kept = kept.filter(_inFocus); }
  pins.setData(kept);
  atFilterCount(kept.length);
  SHOWN = kept;
  renderPanel();
}
atMapFilters({
  apply: applyFilters,
  items: function() { return DATA.features.map(function(f) { return { sp: f.properties.sp, c: f.geometry.coordinates }; }); },
  ready: function(cb) { cb(); },
  map: function() { return typeof map !== 'undefined' ? map : null; }
});

// One world only (Hidde, 2026-07-29: "ik hoef niet 2 werelden te zien").
if (!atCanMap()) return;
var map = new maplibregl.Map({
  container: 'map', style: '${MAP_STYLE}',
  center: [8, 48], zoom: 3.4, ${ONE_WORLD},
  attributionControl: false
});
map.addControl(new maplibregl.AttributionControl({compact: true, customAttribution: ${JSON.stringify(MAP_CREDIT)}}), 'top-left');
map.addControl(new maplibregl.NavigationControl());
new ResizeObserver(function() { map.resize(); }).observe(document.getElementById('map'));
// Location is asked HERE, in map context, never on the homepage.
var _geo = new maplibregl.GeolocateControl({
  positionOptions: { enableHighAccuracy: true },
  showUserLocation: true, fitBoundsOptions: { maxZoom: 13.5 }
});
map.addControl(_geo);
// Arriving from the search field's "Trees near me" row (#near) triggers the
// locate control once the map is ready, so that row does what it says
// instead of merely opening the map. The permission prompt still belongs to
// the browser and only appears because the visitor asked for it.
// On /explore itself the row only changes the hash and the page does not
// reload, so a hashchange has to trigger it too (Hidde, 2026-10-12: "er
// gebeurt niks").
function _nearFromHash() {
  if (location.hash !== '#near') { return; }
  if (map.loaded()) { _geo.trigger(); }
  else { map.once('load', function() { setTimeout(function() { _geo.trigger(); }, 300); }); }
  try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
}
_nearFromHash();
window.addEventListener('hashchange', _nearFromHash);
// Open where the visitor is, without asking for anything (Hidde,
// 2026-07-30). The browser's own timezone gives a region for free: no
// permission prompt, no IP lookup, no third-party service, nothing stored.
// The Geolocate button above is still there for an exact fix.
var REGIONS = {
  'Europe/Amsterdam': [4.9, 52.37], 'Europe/Brussels': [4.35, 50.85],
  'Europe/London': [-0.13, 51.51], 'Europe/Dublin': [-6.26, 53.35],
  'Europe/Lisbon': [-9.14, 38.72], 'Europe/Madrid': [-3.7, 40.42],
  'Europe/Paris': [2.35, 48.86], 'Europe/Berlin': [13.4, 52.52],
  'Europe/Rome': [12.5, 41.9], 'Europe/Vienna': [16.37, 48.21],
  'Europe/Prague': [14.42, 50.09], 'Europe/Athens': [23.73, 37.98],
  'Europe/Warsaw': [21.01, 52.23], 'Europe/Istanbul': [28.98, 41.01],
  'Asia/Tokyo': [139.69, 35.69], 'Asia/Singapore': [103.82, 1.35],
  'Asia/Bangkok': [100.5, 13.75], 'America/New_York': [-74.0, 40.71],
  'Atlantic/Reykjavik': [-21.9, 64.15]
};
try {
  var tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
  if (REGIONS[tz]) { map.jumpTo({center: REGIONS[tz], zoom: 9}); }
  else if (tz && tz.indexOf('Europe/') === 0) { map.jumpTo({center: [10, 50], zoom: 4}); }
} catch (e) {}
// The map keeps its place in the address (#map=zoom/lat/lng, the
// OpenStreetMap form; Google Maps and Airbnb do the same), so back from a tree
// page lands where you were, not on the timezone guess (Hidde, 2026-11-01:
// "fix the back button thing"). replaceState, so panning adds no history.
var _view = /^#map=([0-9.]+)\\/(-?[0-9.]+)\\/(-?[0-9.]+)$/.exec(location.hash);
if (_view) { map.jumpTo({zoom: +_view[1], center: [+_view[3], +_view[2]]}); }
map.on('moveend', function() {
  if (location.hash && location.hash.indexOf('#map=') !== 0) { return; }
  var c = map.getCenter();
  try { history.replaceState(null, '', location.pathname + location.search + '#map=' +
    map.getZoom().toFixed(2) + '/' + c.lat.toFixed(5) + '/' + c.lng.toFixed(5)); } catch (e) {}
});
// Arriving from a town in the search that we hold no tree for
// (#@lat,lng,Name, search-form.ts): the map opens on that town, at the zoom a
// town fills, and the sheet asks for its first tree under its name. Read after
// the timezone guess above so the town wins.
var PLACE = null;
var FOCUS = null;
// On a phone the sheet covers the lower map: the town goes in the middle of
// what is still visible, measured the way the tree card measures it.
function _goPlace() {
  var lift = 0;
  try {
    var mr = map.getContainer().getBoundingClientRect();
    var st = window.atSheetTop ? window.atSheetTop() : null;
    if (st !== null && st < mr.bottom) { lift = (mr.bottom - st) / 2; }
  } catch (e) {}
  map.easeTo({center: [PLACE.lng, PLACE.lat], zoom: 11, offset: [0, -lift], duration: 0});
}
function _placeFromHash() {
  var m = /^#@(-?[0-9.]+),(-?[0-9.]+),?(.*)$/.exec(location.hash);
  if (!m) { return; }
  var name = '';
  try { name = decodeURIComponent(m[3] || ''); } catch (e) {}
  PLACE = {lat: parseFloat(m[1]), lng: parseFloat(m[2]), name: name};
  _goPlace();
  // Once more on the next frame: the sheet's script may only now have said
  // where its top is.
  requestAnimationFrame(_goPlace);
  try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
}
_placeFromHash();
window.addEventListener('hashchange', _placeFromHash);
// A place picked in the search on this map moves this map (Hidde, 2026-11-01:
// "als je op de kaart naar griekenland zoekt ... niet in de kaart blijft").
// Airbnb's search on its map, and our app's (MapTab.swift, case .country):
// the whole spread of the country or city in view, never its page. Returns
// false for a place this map holds no tree of, and the search then navigates.
window.atMapPlace = function(kind, key) {
  // The place searched for leads the list under the map until the search
  // field changes (Hidde, 2026-11-06: searching United Kingdom fitted the
  // Benelux in too; then the Airbnb rule, the search holds while you drag).
  FOCUS = {kind: kind, key: key};
  applyFilters();
  var slugs = {};
  CITIES.forEach(function(c) {
    if (kind === 'country' ? c.country === key : c.url === key) { slugs[c.url] = 1; }
  });
  var lngs = [], lats = [];
  DATA.features.forEach(function(f) {
    var c = f.geometry.coordinates;
    if (slugs[f.properties.cs] && c[0] !== null && c[1] !== null) { lngs.push(c[0]); lats.push(c[1]); }
  });
  var n = lngs.length;
  if (!n) { return false; }
  // The middle 96 percent of its trees, as the app frames a place, so one
  // tree overseas does not pull the view across an ocean (France's in the
  // Caribbean framed the whole Atlantic, 2026-11-06).
  lngs.sort(function(a, z) { return a - z; }); lats.sort(function(a, z) { return a - z; });
  var lo = Math.floor((n - 1) * 0.02), hi = Math.ceil((n - 1) * 0.98);
  var b = new maplibregl.LngLatBounds([lngs[lo], lats[lo]], [lngs[hi], lats[hi]]);
  var lift = 0;
  try {
    var mr = map.getContainer().getBoundingClientRect();
    var st = window.atSheetTop ? window.atSheetTop() : null;
    if (st !== null && st < mr.bottom) { lift = Math.min(mr.bottom - st, mr.height * 0.6); }
  } catch (e) {}
  // The top clears the filter chips that sit over the map.
  map.fitBounds(b, { padding: {top: 100, left: 40, right: 40, bottom: 40 + lift},
                     maxZoom: kind === 'country' ? 9 : 13, duration: 900 });
  return true;
};
// A country picked in the search anywhere else lands here (#country=Greece,
// search-form.ts), Airbnb's search, which always lands on its map (Hidde,
// 2026-11-01). Read after the timezone guess so the country wins.
function _countryFromHash() {
  var m = /^#country=(.+)$/.exec(location.hash);
  if (!m) { return; }
  var name = '';
  try { name = decodeURIComponent(m[1]); } catch (e) { return; }
  window.atMapPlace('country', name);
  // Once more on the next frame, when the sheet has said where its top is,
  // and once the map has loaded, when its container has its final size.
  requestAnimationFrame(function() { window.atMapPlace('country', name); });
  if (!map.loaded()) { map.once('load', function() { window.atMapPlace('country', name); }); }
  try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
}
_countryFromHash();
window.addEventListener('hashchange', _countryFromHash);
var pins = null;
function initTreeLayers() {
  if (pins) { return; }
  // THE ONE TREE PIN (tree-pins-js.ts), the city map's, since 2026-11-20
  // (Hidde: "ik wil gewoon 1 goede"); it was a moss circle here.
  var openCard = null;
  pins = atTreePins(map, {
    source: 'trees',
    iconOf: function(p) { return (p.sp !== undefined && p.sp !== null && SP_IC[p.sp]) || 'broadleaf'; },
    open: function(p, c) { if (openCard) openCard(p, c); }
  });
  pins.setData(DATA.features);
  // A search that arrived before the map had its source (#country=...).
  if (FOCUS) { applyFilters(); }
  // The season heartbeat (a pulse and a gold dot behind trees at their peak)
  // is switched off: Hidde, 2026-10-03, "its not good enough lets look at it
  // later". The 'now' property still travels in DATA, so bringing it back is
  // a halo layer, its requestAnimationFrame loop and the two gold cases on
  // the tree layer (git history has all three).
  // A pin or a dot shows its tree's card, the one every map shows
  // (map-card-js.ts, Hidde 2026-10-24: the city map and this one are one
  // thing). It replaced 10-04's jump straight to the tree page.
  openCard = atTreePinCard(map, pins, null);
  // Pointing at a tree in the list lights its pin (Airbnb's list).
  atPinsFollowList(pins, openCard, null);
  // The register layer: officially designated trees from a government
  // register, not our own research. Visually quieter than the curated
  // trees on purpose (small, hollow, grey) so the two layers read as
  // different kinds of thing, not competing dots. No clustering (small
  // pilot count); no click-through URL, since these carry no own page.
  // Fetched rather than inlined: there are thousands of these and they would
  // otherwise be the heaviest thing on the page, loaded before the map the
  // visitor actually came for. They also only appear from zoom 8, because a
  // grey haze over Europe at world zoom tells nobody anything.
  if (!map.getSource('registers')) {
    fetch('assets/registers.json').then(function(r) { return r.json(); }).then(function(data) {
      if (!data.features.length || map.getSource('registers')) { return; }
      map.addSource('registers', {type: 'geojson', data: data});
      map.addLayer({id: 'register', type: 'circle', source: 'registers', minzoom: 8,
        paint: {'circle-color': 'rgba(0,0,0,0)', 'circle-radius': 5,
                'circle-stroke-width': 1.5, 'circle-stroke-color': '#8A8578'}});
      map.on('click', 'register', function(e) {
        var p = e.features[0].properties;
        new maplibregl.Popup({offset: 10})
          .setLngLat(e.features[0].geometry.coordinates)
          .setHTML('<strong>' + p.name + '</strong><br>' + p.designation +
                   (p.area ? ' &middot; ' + p.area : '') +
                   '<br><em>From the official register, not yet verified by us.</em>')
          .addTo(map);
      });
      map.on('mouseenter', 'register', function() { map.getCanvas().style.cursor = 'pointer'; });
      map.on('mouseleave', 'register', function() { map.getCanvas().style.cursor = ''; });
    }).catch(function() { /* the map works without this layer */ });
  }
}
map.on('style.load', initTreeLayers);
if (map.isStyleLoaded()) { initTreeLayers(); }

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
var CARDS = null;
// The trees this account collected, from the server (atCollection.visited),
// as a set; null signed out or until it answers.
var VISITED = null;
var LIST_MAX = ${EXPLORE_LIST_MAX};
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
  if (!panel || typeof map === 'undefined' || !map) return;
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
  // The ambassador box UNDER the Highlights (Hidde, 2026-11-06: "doe de
  // ambasadeur knop onder highlight"), as in the app.
  html += _boxHtml(trees);
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
      '<a class="exc-card" href="/' + best.properties.url + '">${NO_PHOTO_CARD}' +
      '<span class="exc-body"><b>' + _esc(best.properties.name) + '</b>' +
      '<span>' + Math.round(bd) + ' km &middot; ' + _esc(best.properties.city) + '</span></span></a>';
  }
  return html;
}
if (panel) panel.addEventListener('click', function(e) {
  var a = e.target.closest ? e.target.closest('[data-ev]') : null;
  if (a) at.track(a.getAttribute('data-ev'), 'map');
});
// THE SEARCH HOLDS UNTIL YOU MOVE THE MAP (Airbnb's map, Hidde 2026-11-06:
// "alleen degene in frankrijk tellen tot kruisje of scrollen"): a drag or a
// zoom by the visitor, or typing in or clearing the field, ends it, and the
// map area is everything again. The search's own fit carries no
// originalEvent, so it keeps it. The app does the same (MapTab onUserMove).
function _endSearch(clearField) {
  if (!FOCUS) { return; }
  FOCUS = null;
  var q = document.getElementById('ex-q');
  if (clearField && q) { q.value = ''; }
  applyFilters();
}
map.on('dragstart', function() { _endSearch(true); });
map.on('zoomstart', function(e) { if (e && e.originalEvent) { _endSearch(true); } });
(function() {
  var q = document.getElementById('ex-q');
  if (q) { q.addEventListener('input', function() { _endSearch(false); }); }
})();
map.on('moveend', renderPanel);
// The photographs, from the catalogue the pins' cards share. Not behind the
// map's load, which waits for every street tile: on a slow phone, or with the
// tile host busy, the list stood as grey tiles until the streets had come in.
var _cardsAsked = false;
function _askCards() {
  var C = window.atCollection;
  if (_cardsAsked || !C || !C.catalogue) { return; }
  _cardsAsked = true;
  C.catalogue().then(function(c) { CARDS = c || {}; renderPanel(); });
}
_askCards();
map.on('load', function() {
  renderPanel();
  _askCards();
  var C = window.atCollection;
  if (C && C.verify && C.visited) {
    C.verify().then(function(ok) {
      if (!ok) { return; }
      C.visited().then(function(ids) {
        if (!ids || !ids.length) { return; }
        VISITED = {}; ids.forEach(function(id) { VISITED[id] = 1; }); renderPanel();
      });
    });
  }
});
renderPanel();

`)
  );
}

/** "the Netherlands" in a sentence, "The Netherlands" at its start. */
/** YOUR OWN MAP, on your own profile.
 *
 * Hidde, 2026-09-02, having put the Polarsteps profile beside ours: "kun je
 * het helemaal gelijk trekken met polarsteps - dat je dus ook een persoonlijke
 * kaart naast je account krijgt met jouw bomen - zoals op de app account
 * pagina." Polarsteps gives half the profile to a world map of where you have
 * been; our own app puts the map above the profile sheet with your trees
 * pinned on it. Both make the same point, which is that a collection is a
 * shape rather than a list.
 *
 * It is the SAME map as everywhere else: the same style, the same wrapper, the
 * same .split skeleton the city and explore pages share, because the one thing
 * this project has learned twice about maps is that a second implementation
 * drifts (CLAUDE.md, one layout for map pages).
 *
 * What differs is where the pins come from. Every other map bakes its features
 * at build time; this one cannot, because whose trees they are is only known
 * once somebody signs in. So it starts empty and profile-js hands it the
 * features through atSetMyTrees() once the account has answered. An empty map
 * is the honest first frame: it is what a collection with nothing in it looks
 * like.
 */
export function myTreesMapScript(): string {
  return mapScript(`${PILES_JS}${mapCardJs()}${treePinsJs()}
// An empty collection opens on the whole world, as Polarsteps' empty map
// does, not on Europe: an Australian with no trees yet saw an empty Europe
// (Hidde, 2026-11-01). The trees, once there, frame themselves (paint()).
if (!atCanMap()) return;
var map = new maplibregl.Map({
  container: 'map', style: '${MAP_STYLE}',
  bounds: [[-165, -50], [180, 70]], ${ONE_WORLD},
  attributionControl: false
});
map.addControl(new maplibregl.AttributionControl({compact: true, customAttribution: ${JSON.stringify(MAP_CREDIT)}}), 'top-left');
map.addControl(new maplibregl.NavigationControl());
new ResizeObserver(function() { map.resize(); }).observe(document.getElementById('map'));

var EMPTY = { type: 'FeatureCollection', features: [] };
var pending = null;

var pins = null;
function initMine() {
  if (pins) { return; }
  // THE ONE TREE PIN (tree-pins-js.ts), the city map's: the species drawn on
  // it, the tick in the corner on a tree you collected, the bookmark on one
  // you saved. Until 2026-11-20 this map had its own filled-versus-hollow
  // circles for the same two facts (Hidde: "ik wil gewoon 1 goede").
  // A pin or a dot shows the tree's card, the one every map shows
  // (map-card-js.ts), and the card is the tile's own when the grid has it, so
  // your photograph of the tree comes with it. A tree only you have may have
  // no page at all: sharing is what gives it one, so its card carries the
  // name and place and opens nothing.
  var openCard = null;
  pins = atTreePins(map, {
    source: 'mine',
    iconOf: function(p) { return p.ic || 'broadleaf'; },
    seen: function(p) { return p.got === 1 || Boolean(window.atHasVisited && window.atHasVisited(p.id)); },
    open: function(p, c) { if (openCard) openCard(p, c); }
  });
  openCard = atTreePinCard(map, pins, function(p) {
    // The grid's own card for this tree, in the lane you are looking at first.
    var id = String(p.id || '').replace(/[^A-Za-z0-9_-]/g, '');
    var q = id.indexOf('own-') === 0
      ? '.saved-list [data-pin-id="' + id + '"], .saved-list [data-id="' + id.slice(4) + '"]'
      : '.saved-list [data-tree-id="' + id + '"]';
    var all = Array.prototype.slice.call(document.querySelectorAll(q));
    var shown = all.filter(function(el) { return el.offsetParent !== null; });
    var el = (shown[0] || all[0]);
    if (!el) { return null; }
    var card = el.closest('.tree-card') || el;
    var a = card.querySelector('a[href]');
    return { el: card, href: a ? a.href : (p.url || null) };
  });
  // Pointing at a tile lights its pin (Airbnb's list).
  atPinsFollowList(pins, openCard, function(el) {
    if (!el.closest('.saved-list')) { return null; }
    if (el.hasAttribute('data-pin-id')) { return el.getAttribute('data-pin-id'); }
    if (el.hasAttribute('data-tree-id')) { return el.getAttribute('data-tree-id'); }
    var own = el.getAttribute('data-id');
    return own ? 'own-' + own : null;
  });
  if (pending) { paint(pending); pending = null; }
}

function paint(features) {
  pins.setData(features);
  if (!features.length) { return; }
  // Frame the whole collection. One tree gets a city-level zoom rather than
  // a bounding box of nothing.
  var b = new maplibregl.LngLatBounds();
  features.forEach(function(f) { b.extend(f.geometry.coordinates); });
  if (features.length === 1) { map.easeTo({ center: features[0].geometry.coordinates, zoom: 12 }); }
  else { map.fitBounds(b, { padding: 70, maxZoom: 12, duration: 700 }); }
}

// Called by profile-js once the account has said which trees are yours. It
// may arrive before or after the style loads, so both orders work.
window.atSetMyTrees = function(features) {
  if (pins) { paint(features); } else { pending = features; }
};

map.on('style.load', initMine);
if (map.isStyleLoaded()) { initMine(); }
`);
}

export function countryName(intro: { country: string; article?: string }, capital = false): string {
  const art = intro.article;
  if (!art) return intro.country;
  const displayArt = capital ? art.charAt(0).toUpperCase() + art.slice(1) : art;
  return `${displayArt} ${intro.country}`;
}
