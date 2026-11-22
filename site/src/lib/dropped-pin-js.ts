// A DROPPED PIN on every full website map (Hidde, 2026-11-22: "build it
// exactly as them"; CONVENTIONS.md "A dropped pin"; the apps' DroppedPin.swift).
// Text that atTreeMap() in tree-map-js.ts carries inside its body, where `map`
// and `o` are that map and its options.
//
// Its own file because the card it opens is NOT a tree's card: a dropped pin is
// a spot with no tree and no page, like the register dots, so the one tapped-
// tree card (map-card-js.ts, qa check_one_tree_card_on_every_map) does not fit
// it. Google's own form on a computer is a small pop-up at the spot.
import { ui } from "./i18n";

const LANGS = ["en", "es", "it", "nl", "de", "pt", "fr", "ja"];

export function droppedPinJs(): string {
  const dropWords: Record<string, string[]> = {};
  for (const l of LANGS) { const u = ui(l); dropWords[l] = [u.droppedPin, u.droppedAdd, u.droppedDirections]; }
  return `
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
`;
}
