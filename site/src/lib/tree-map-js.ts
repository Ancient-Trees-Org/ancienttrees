// THE ONE MAP (Hidde, 2026-11-20: "maar zijn de explore kaart de stadskaart en
// de kaart op profiel nu een en hetzelfde product?", then "oke maak het").
// The pin, the dots, the tapped tree's card and the filter row were already
// one each; the map around them was still built five times, each page with
// its own controls (a fullscreen button on the city map only, a locate button
// of its own on the city map and MapLibre's on /explore, none on the profile)
// and its own memory of where you were (the city map and /explore kept it in
// the address, the profile and the country maps did not).
//
// atTreeMap() is that map: the style, one world, the credit, the zoom
// buttons, the one locate button (MapLibre's own, as /explore always had),
// the resize, the place kept in the address (#map=zoom/lat/lng, so back from
// a tree page lands where you were), and the trees: atTreePins, the one card
// and the list that lights a pin. A page hands over its trees, its opening
// frame and what is its own (the city map's walks, /explore's list), and
// nothing else. data/map-parity.json.
//
// Ships as text inside mapScript()'s body; it needs PILES_JS, mapCardJs()
// and treePinsJs() beside it.
import { MAP_STYLE, MAP_CREDIT } from "./site-config";
import { ONE_WORLD } from "./map";
import { droppedPinJs } from "./dropped-pin-js";

export function treeMapJs(): string {
  return `
// o: { container, center/zoom or bounds+padding, embedded (no scroll zoom, no
//      locate, no address: a map inside a page rather than the page),
//      source, iconOf, seen, open(p, c) (return true when the page handled
//      the tap), cardFor(p), listIdOf(el), ready(pins, card) }
// The opening frame: a box to fit, or a centre and a zoom.
function atMapFrame(o, opts) {
  if (o.bounds) { opts.bounds = o.bounds; opts.fitBoundsOptions = { padding: o.padding || 40, maxZoom: o.maxZoom || 14.5 }; }
  else { opts.center = o.center || [8, 48]; opts.zoom = o.zoom === undefined ? 3.4 : o.zoom; }
  return opts;
}
function atTreeMap(o) {
  // The page asks first and stops without a map; asked again here so this
  // one place never builds what the browser cannot draw (CAN_MAP_JS).
  if (!atCanMap()) { return null; }
  var opts = { container: o.container || 'map' };
  var map = new maplibregl.Map(atMapFrame(o, { container: o.container || 'map', style: '${MAP_STYLE}', ${ONE_WORLD},
    scrollZoom: !o.embedded, attributionControl: false }));
  // The page's own map, which a city swapped in without a page load hands
  // over to and removes (soft-nav-js.ts).
  if (!o.embedded) { window.atMainMap = map; }
  map.addControl(new maplibregl.AttributionControl({compact: true, customAttribution: ${JSON.stringify(MAP_CREDIT)}}), 'top-left');
  map.addControl(new maplibregl.NavigationControl());
  var geo = null;
  if (!o.embedded) {
    // Location is asked HERE, in map context, never on the homepage.
    geo = new maplibregl.GeolocateControl({
      positionOptions: { enableHighAccuracy: true },
      showUserLocation: true, fitBoundsOptions: { maxZoom: 13.5 }
    });
    map.addControl(geo);
  }
  var box = typeof opts.container === 'string' ? document.getElementById(opts.container) : opts.container;
  if (box && window.ResizeObserver) { new ResizeObserver(function() { map.resize(); }).observe(box); }

  // THE PLACE IN THE ADDRESS (#map=zoom/lat/lng, the OpenStreetMap form;
  // Google Maps and Airbnb do the same), so back from a tree page lands where
  // you were (Hidde, 2026-11-01: "fix the back button thing"). replaceState,
  // so panning adds no history. A hash that means something else (#tree=,
  // #near, #@...) is left alone.
  var fromAddress = false;
  if (!o.embedded) {
    var view = /^#map=([0-9.]+)\\/(-?[0-9.]+)\\/(-?[0-9.]+)$/.exec(location.hash);
    if (view) { map.jumpTo({zoom: +view[1], center: [+view[3], +view[2]]}); fromAddress = true; }
    map.on('moveend', function() {
      if (location.hash && location.hash.indexOf('#map=') !== 0) { return; }
      var c = map.getCenter();
      try { history.replaceState(null, '', location.pathname + location.search + '#map=' +
        map.getZoom().toFixed(2) + '/' + c.lat.toFixed(5) + '/' + c.lng.toFixed(5)); } catch (e) {}
    });
  }

  // THE TREES, as soon as the style is there (not at 'load', which waits for
  // every tile).
  var pins = null, card = null;
  function init() {
    if (pins) { return; }
    pins = atTreePins(map, {
      source: o.source || 'trees',
      iconOf: o.iconOf,
      seen: o.seen,
      open: function(p, c) {
        if (o.open && o.open(p, c) === true) { return; }
        if (card) { card(p, c); }
      }
    });
    card = atTreePinCard(map, pins, o.cardFor || null);
    atPinsFollowList(pins, card, o.listIdOf || null);
    if (o.ready) { o.ready(pins, card); }
  }
  ${droppedPinJs()}

  map.on('style.load', init);
  if (map.isStyleLoaded()) { init(); }
  return { map: map, geo: geo, fromAddress: fromAddress,
           pins: function() { return pins; }, card: function() { return card; } };
}
`;
}
