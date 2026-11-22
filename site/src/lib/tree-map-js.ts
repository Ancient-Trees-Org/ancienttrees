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
import { ui } from "./i18n";

const LANGS = ["en", "es", "it", "nl", "de", "pt", "fr", "ja"];

export function treeMapJs(): string {
  const dropWords: Record<string, string[]> = {};
  for (const l of LANGS) { const u = ui(l); dropWords[l] = [u.droppedPin, u.droppedAdd, u.droppedDirections]; }
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
  // A DROPPED PIN (Hidde, 2026-11-22: "build it exactly as them"; CONVENTIONS.md
  // "A dropped pin"; the apps' DroppedPin.swift). Google Maps on a computer:
  // "right-click the place or area. A pop-up window appears", the coordinates
  // at its top; on a phone "touch and hold an area of the map that isn't
  // labeled". So: right-click, or a half-second hold (Android's browser sends
  // the hold as a contextmenu too, iPhone's does not, hence the timer). On a
  // tree, nothing. One pin at a time: MapLibre's own marker in red, above the
  // trees, and a small card at it. A click on open map, the cross or Escape
  // takes it away.
  if (!o.embedded) {
    var DW = ${JSON.stringify(dropWords)};
    var dw = DW[(document.documentElement.lang || 'en').slice(0, 2)] || DW.en;
    var dropMarker = null, dropPopup = null, lastDrop = 0;
    var treeLayers = function() {
      var src = o.source || 'trees';
      return (map.getStyle().layers || []).map(function(l) { return l.id; })
        .filter(function(id) { return id.indexOf(src + '-') === 0; });
    };
    var onTree = function(pt, target) {
      if (target && target.closest && target.closest('.maplibregl-marker')) { return true; }
      var r = 22, ids = treeLayers();
      return ids.length > 0 && map.queryRenderedFeatures([[pt.x - r, pt.y - r], [pt.x + r, pt.y + r]], { layers: ids }).length > 0;
    };
    var clearDrop = function() {
      if (dropPopup) { var p = dropPopup; dropPopup = null; p.remove(); }
      if (dropMarker) { dropMarker.remove(); dropMarker = null; }
    };
    var dropAt = function(ll) {
      if (Date.now() - lastDrop < 700) { return; }
      lastDrop = Date.now();
      clearDrop();
      if (navigator.vibrate) { try { navigator.vibrate(15); } catch (e) {} }
      var lat = ll.lat.toFixed(5), lng = ll.lng.toFixed(5);
      dropMarker = new maplibregl.Marker({ color: '#E53935' }).setLngLat(ll).addTo(map);
      var box = document.createElement('div');
      box.className = 'drop-card';
      var head = document.createElement('div'); head.className = 'drop-head';
      var h = document.createElement('strong'); h.textContent = dw[0];
      var x = document.createElement('button'); x.type = 'button'; x.className = 'drop-x'; x.setAttribute('aria-label', 'Close'); x.innerHTML = '&times;';
      head.appendChild(h); head.appendChild(x);
      var c = document.createElement('p'); c.className = 'drop-coords'; c.textContent = lat + ', ' + lng;
      var add = document.createElement('a'); add.className = 'drop-add';
      add.href = '/contribute?kind=tree&where=' + encodeURIComponent(lat + ', ' + lng); add.textContent = dw[1];
      var go = document.createElement('a'); go.className = 'drop-go'; go.target = '_blank'; go.rel = 'noopener';
      go.href = 'https://www.google.com/maps/dir/?api=1&destination=' + lat + ',' + lng + '&travelmode=walking'; go.textContent = dw[2];
      box.appendChild(head); box.appendChild(c); box.appendChild(add); box.appendChild(go);
      x.addEventListener('click', clearDrop);
      dropPopup = new maplibregl.Popup({ closeButton: false, closeOnClick: false, offset: [0, -38], maxWidth: '260px', className: 'drop-pop' })
        .setLngLat(ll).setDOMContent(box).addTo(map);
    };
    map.on('contextmenu', function(e) {
      if (e.originalEvent) { e.originalEvent.preventDefault(); }
      if (onTree(e.point, e.originalEvent && e.originalEvent.target)) { return; }
      dropAt(e.lngLat);
    });
    var holdT = null, holdAt = null;
    var cancelHold = function() { if (holdT) { clearTimeout(holdT); holdT = null; } };
    map.on('touchstart', function(e) {
      cancelHold();
      if (!e.originalEvent || e.originalEvent.touches.length !== 1) { return; }
      holdAt = e.point;
      var ll = e.lngLat, target = e.originalEvent.target;
      holdT = setTimeout(function() { holdT = null; if (!onTree(holdAt, target)) { dropAt(ll); } }, 500);
    });
    map.on('touchmove', function(e) { if (holdAt && e.point && Math.abs(e.point.x - holdAt.x) + Math.abs(e.point.y - holdAt.y) > 10) { cancelHold(); } });
    map.on('touchend', cancelHold);
    map.on('touchcancel', cancelHold);
    map.on('movestart', cancelHold);
    map.on('click', function(e) {
      if (!dropMarker || Date.now() - lastDrop < 700) { return; }
      if (!onTree(e.point, e.originalEvent && e.originalEvent.target)) { clearDrop(); }
    });
    document.addEventListener('keydown', function(e) { if (e.key === 'Escape' && dropMarker) { clearDrop(); } });
  }

  map.on('style.load', init);
  if (map.isStyleLoaded()) { init(); }
  return { map: map, geo: geo, fromAddress: fromAddress,
           pins: function() { return pins; }, card: function() { return card; } };
}
`;
}
