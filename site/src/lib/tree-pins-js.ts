// THE ONE TREE PIN, on every map of the website (Hidde, 2026-11-20: "we zijn
// nu de hele tijd verschillende versies aan het onderhouden ik wil gewoon 1
// goede"). Until today the city map drew its own trees as DOM pins with the
// species drawn on them, and every other map (explore, country, state, the
// profile, and the other places' trees on the city map itself) drew moss
// circles as a MapLibre symbol layer. Two looks, two hover states, two ways
// of marking the chosen tree. Now every map hands its trees to atTreePins()
// and gets the city pin, its hover, its chosen state and its three corners.
//
// How it draws, the Airbnb way (lib/map.ts PIN_DISTANCE has the benchmark):
// every tree is a dot in a GL circle layer, which costs nothing at 5,000
// trees, and the trees that get a FULL pin are DOM elements made only for
// what is in view: in pinPriority order (a photograph first, then readers'
// saves), a saved tree before the rest, a pin where no full pin stands within
// PIN_DISTANCE, a dot otherwise. Below FAR_ZOOM the Airbnb split (FAR_PIN_
// DISTANCE apart, a mini dot for the `mn` trees, nothing for the rest). The
// same-spot stacks are PILES_JS, whose spread now fans full pins.
//
// The states, measured on Airbnb's map on 2026-11-20 (Kyoto, desktop):
// pointing at a listing in the list turns its pin to the chosen look; a tap on
// a pin turns it to the chosen look and opens the card over the map; the list
// itself is not marked. So: hover() and select() both give the pin its
// .active look (style.css .pin-tree.active), and a hovered or chosen tree is
// always a full pin, never a dot.
//
// Ships as text inside mapScript()'s body, like PILES_JS: nothing in it can
// import, so the build-time pieces are interpolated here.
import { icon } from "./icons";
import { SPECIES_ICONS } from "./species-icons";
import { PIN_DISTANCE, FAR_ZOOM, FAR_PIN_DISTANCE, MINI_RADIUS, STACK_ZOOM, PIN_SPEC } from "./map";

// The saved corner: the cards' own bookmark, filled. The collected corner: a
// filled tick. The ticket corner: Phosphor's ticket fill. All three as the
// city pin has worn them since 2026-11-12 (CONVENTIONS.md "A tree you saved,
// on every map").
const PIN_BOOKMARK = icon("bookmark-simple", "fill", "pin-fav-ic");
const PIN_TICK = icon("check-circle", "fill", "pin-got-ic");
const PIN_TICKET = icon("ticket", "fill", "pin-ticket-ic");

// THE PIN ITSELF, written from PIN_SPEC (lib/map.ts), the app's numbers, so
// the drawing has one source on the website and qa holds it to the app's. The
// corners (.pin-got, .pin-fav, .pin-ticket) stay in style.css. The hover is a
// deeper shadow only: MapLibre places a marker with an inline transform, so a
// scale on :hover never applied.
//
// READ AT CALL TIME, NEVER AT LOAD: map.ts imports this file and this file
// imports PIN_SPEC from map.ts, so at load PIN_SPEC is still undefined. A
// module-level `const S = PIN_SPEC` broke every deploy on 2026-11-20 ("Cannot
// read properties of undefined (reading 'size')" while generating routes).
function pinCss(S: typeof PIN_SPEC): string {
  const CHOSEN = Math.round(S.size * S.chosenScale);
  const CHOSEN_GLYPH = Math.round(S.glyph * S.chosenScale);
  return `.pin-tree{position:relative;width:${S.size}px;height:${S.size}px;box-sizing:border-box;border-radius:50%;` +
  `background:${S.fill};border:${S.ringWidth}px solid ${S.ring};box-shadow:0 3px 10px rgba(26,26,20,0.28);` +
  `cursor:pointer;display:flex;align-items:center;justify-content:center;transition:box-shadow .18s ease}` +
  `.pin-tree>svg{width:${S.glyph}px;height:${S.glyph}px;color:${S.ring}}` +
  `.pin-tree:hover{box-shadow:0 5px 16px rgba(26,26,20,0.4)}` +
  `.pin-tree.active{width:${CHOSEN}px;height:${CHOSEN}px;z-index:5;box-shadow:0 5px 16px rgba(26,26,20,0.4)}` +
  `.pin-tree.active>svg{width:${CHOSEN_GLYPH}px;height:${CHOSEN_GLYPH}px}`;
}

export function treePinsJs(): string {
  const S = PIN_SPEC;
  const PIN_CSS = pinCss(S);
  return `
(function() {
  if (document.getElementById('at-pin-css')) { return; }
  var st = document.createElement('style');
  st.id = 'at-pin-css';
  st.textContent = ${JSON.stringify(PIN_CSS)};
  document.head.appendChild(st);
})();
var AT_PIN_ICONS = ${JSON.stringify(SPECIES_ICONS)};
var AT_PIN_MARKS = ${JSON.stringify({ got: PIN_TICK, fav: PIN_BOOKMARK, paid: PIN_TICKET })};
// Every map on a page that draws trees, so one save or tick repaints them all.
var AT_PIN_SETS = [];
// The pin's markup, the one place it is written. Exposed for the city map's
// list, which needs nothing else from it.
// iconKey: a key of AT_PIN_ICONS, or the drawing itself (the city map's
// markers carry theirs, species-icons.ts speciesIcon()).
function atPinMarkup(iconKey, paid) {
  var art = AT_PIN_ICONS[iconKey] || (iconKey && String(iconKey).charAt(0) === '<' ? iconKey : AT_PIN_ICONS.broadleaf);
  return '<svg viewBox="0 0 40 40" fill="currentColor" aria-hidden="true">' + art + '</svg>' +
    '<span class="pin-got" aria-hidden="true">' + AT_PIN_MARKS.got + '</span>' +
    '<span class="pin-fav" aria-hidden="true">' + AT_PIN_MARKS.fav + '</span>' +
    (paid ? '<span class="pin-ticket" aria-hidden="true">' + AT_PIN_MARKS.paid + '</span>' : '');
}
// o: { source: id of the GeoJSON source to make,
//      iconOf(props) -> a key of AT_PIN_ICONS,
//      open(props, [lng, lat]): a pin or a dot was tapped,
//      seen(props) -> true when the tree is collected (optional; else the account's answer),
//      far: false to leave the zoomed-out split off (a map that never zooms out) }
function atTreePins(map, o) {
  var src = o.source;
  var EMPTY = {type: 'FeatureCollection', features: []};
  var order = [];          // features in pin order
  var els = {};            // id -> {el, marker, f}
  var sel = null, hov = null, raf = 0, tapAt = 0;
  var loose = ['all', ['!', ['has', 'point_count']], ['==', ['coalesce', ['get', 'pile'], 0], 0]];
  var pileHead = ['all', ['!', ['has', 'point_count']], ['>=', ['coalesce', ['get', 'pile'], 0], 2]];
  var mini = ['all', loose, ['==', ['coalesce', ['get', 'mn'], 1], 1]];
  var thin = o.far !== false;
  map.addSource(src, {type: 'geojson', data: EMPTY});
  // THE DOT, the app's: a moss disc in a white ring (PIN_SPEC), with the
  // pin's soft shadow under it.
  var dotPaint = {'circle-color': '${S.fill}', 'circle-radius': ${S.dotRadius}, 'circle-stroke-width': ${S.dotRing}, 'circle-stroke-color': '${S.ring}'};
  var shadow = {'circle-color': 'rgba(26,26,20,0.25)', 'circle-radius': ${S.dotRadius + S.dotRing + 2}, 'circle-blur': 0.8, 'circle-translate': [0, 1]};
  var dotsAt = thin ? ${FAR_ZOOM} : 0;
  map.addLayer({id: src + '-mini', type: 'circle', source: src, filter: mini, maxzoom: thin ? ${FAR_ZOOM} : 0,
    paint: {'circle-color': '${S.fill}', 'circle-radius': ${MINI_RADIUS}, 'circle-stroke-width': 1, 'circle-stroke-color': '${S.ring}'}});
  map.addLayer({id: src + '-shadow', type: 'circle', source: src, filter: loose, minzoom: dotsAt, paint: shadow});
  map.addLayer({id: src + '-dot', type: 'circle', source: src, filter: loose, minzoom: dotsAt, paint: dotPaint});
  map.addLayer({id: src + '-head-shadow', type: 'circle', source: src, filter: pileHead, minzoom: dotsAt, maxzoom: ${STACK_ZOOM}, paint: shadow});
  map.addLayer({id: src + '-head-dot', type: 'circle', source: src, filter: pileHead, minzoom: dotsAt, maxzoom: ${STACK_ZOOM}, paint: dotPaint});
  [src + '-dot', src + '-head-dot', src + '-mini'].forEach(function(l) {
    map.on('click', l, function(e) {
      // A full pin over the dot already answered this tap.
      if (Date.now() - tapAt < 300) { return; }
      var f = e.features[0];
      o.open(f.properties, f.geometry.coordinates);
    });
    map.on('mouseenter', l, function() { map.getCanvas().style.cursor = 'pointer'; });
    map.on('mouseleave', l, function() { map.getCanvas().style.cursor = ''; });
  });

  function idOf(f) { return String(f.properties.id); }
  function seenOf(p) {
    if (o.seen) { return Boolean(o.seen(p)); }
    return Boolean(window.atHasVisited && window.atHasVisited(p.id));
  }
  function keptOf(p) { return Boolean(window.atHasSaved && window.atHasSaved(p.id)); }
  var dimmed = null;       // ids to dim (a chosen walk's others), or null
  function paint(rec) {
    var p = rec.f.properties, id = idOf(rec.f);
    rec.el.classList.toggle('active', id === sel || id === hov);
    rec.el.classList.toggle('pin-off', Boolean(dimmed && dimmed[id]));
    rec.el.classList.toggle('kept', keptOf(p));
    rec.el.classList.toggle('seen', seenOf(p));
  }
  function make(f) {
    var p = f.properties, el = document.createElement('div');
    el.className = 'pin-tree';
    if (p.name) { el.title = p.name; }
    el.innerHTML = atPinMarkup(o.iconOf(p), p.paid === 1 || p.paid === true);
    el.addEventListener('click', function(e) {
      e.stopPropagation();
      tapAt = Date.now();
      o.open(p, f.geometry.coordinates);
    });
    var marker = new maplibregl.Marker({element: el}).setLngLat(f.geometry.coordinates).addTo(map);
    // After addTo: MapLibre labels every marker "Map marker".
    if (p.name) { el.setAttribute('aria-label', p.name); }
    return {el: el, marker: marker, f: f};
  }
  // A full pin for this tree, made for the fan of a same-spot stack.
  function fanPin(f) {
    var el = document.createElement('div');
    el.className = 'pin-tree';
    el.innerHTML = atPinMarkup(o.iconOf(f.properties), f.properties.paid === 1 || f.properties.paid === true);
    if (idOf(f) === sel) { el.classList.add('active'); }
    el.classList.toggle('kept', keptOf(f.properties));
    el.classList.toggle('seen', seenOf(f.properties));
    return el;
  }

  // WHICH TREES GET A FULL PIN, worked out again on every move (a frame at a
  // time). A grid of PIN_DISTANCE cells keeps it cheap with thousands of trees.
  function place() {
    raf = 0;
    var z = map.getZoom(), far = thin && z < ${FAR_ZOOM};
    var D = far ? ${FAR_PIN_DISTANCE} : ${PIN_DISTANCE}, D2 = D * D;
    var box = map.getContainer(), W = box.clientWidth, H = box.clientHeight;
    var b = map.getBounds();
    var west = b.getWest(), east = b.getEast(), south = b.getSouth(), north = b.getNorth();
    var near = z >= ${STACK_ZOOM};
    var grid = {}, want = {}, n = 0;
    function cell(x, y) { return Math.floor(x / D) + ':' + Math.floor(y / D); }
    function fits(q) {
      var cx = Math.floor(q.x / D), cy = Math.floor(q.y / D);
      for (var i = -1; i <= 1; i++) { for (var j = -1; j <= 1; j++) {
        var c = grid[(cx + i) + ':' + (cy + j)];
        if (!c) { continue; }
        for (var k = 0; k < c.length; k++) {
          var dx = c[k].x - q.x, dy = c[k].y - q.y;
          if (dx * dx + dy * dy < D2) { return false; }
        }
      } }
      return true;
    }
    function put(f, q) {
      var k = cell(q.x, q.y);
      (grid[k] = grid[k] || []).push(q);
      want[idOf(f)] = f;
      n++;
    }
    function candidate(f) {
      var pile = f.properties.pile || 0;
      if (pile < 0) { return false; }
      if (pile >= 2 && near) { return false; }
      var c = f.geometry.coordinates;
      return c[0] >= west && c[0] <= east && c[1] >= south && c[1] <= north;
    }
    // The chosen and the pointed-at tree first: always full.
    [sel, hov].forEach(function(id) {
      if (id === null) { return; }
      var f = byId[id];
      if (!f || !candidate(f)) { return; }
      put(f, map.project(f.geometry.coordinates));
    });
    // A TREE YOU SAVED IS PLACED FIRST, so it is never the dot under a
    // neighbour (Hidde, 2026-11-12; CONVENTIONS.md "A tree you saved, on every
    // map"), then the rest in pin order.
    var saved = [], rest = [];
    order.forEach(function(f) { (keptOf(f.properties) ? saved : rest).push(f); });
    var left = [];
    [saved, rest].forEach(function(list) {
      for (var i = 0; i < list.length; i++) {
        var f = list[i], id = idOf(f);
        if (want[id] || !candidate(f)) { continue; }
        var q = map.project(f.geometry.coordinates);
        if (q.x < -20 || q.y < -20 || q.x > W + 20 || q.y > H + 20) { continue; }
        if (n < 600 && fits(q)) { put(f, q); } else { left.push([f, q]); }
      }
    });
    // THE DOTS, AIRBNB'S MINI-PINS: a tree whose pin did not fit is a dot only
    // where the dot stands clear of every full pin and of the other dots;
    // anything else is not drawn until a zoom makes room (Hidde, 2026-11-20,
    // on Baarn: "je sommige pins niet ziet omdat andere eroverheen gaat";
    // CONVENTIONS.md "How close two pins have to be": Airbnb draws full pins,
    // then mini-pins, "the rest are simply not drawn"). Zoomed out the dots
    // are the mini pins of the trees the feed marks (mn).
    var CLEAR = ${S.size / 2 + S.dotRadius + S.dotRing + 3}, GAP = ${2 * (S.dotRadius + S.dotRing) + 2};
    function clearOf(q) {
      var cx = Math.floor(q.x / D), cy = Math.floor(q.y / D);
      for (var i = -1; i <= 1; i++) { for (var j = -1; j <= 1; j++) {
        var c = grid[(cx + i) + ':' + (cy + j)];
        if (!c) { continue; }
        for (var k = 0; k < c.length; k++) {
          var dx = c[k].x - q.x, dy = c[k].y - q.y;
          if (dx * dx + dy * dy < CLEAR * CLEAR) { return false; }
        }
      } }
      return true;
    }
    var dgrid = {}, dots = [];
    function dotFits(q) {
      var cx = Math.floor(q.x / GAP), cy = Math.floor(q.y / GAP);
      for (var i = -1; i <= 1; i++) { for (var j = -1; j <= 1; j++) {
        var c = dgrid[(cx + i) + ':' + (cy + j)];
        if (!c) { continue; }
        for (var k = 0; k < c.length; k++) {
          var dx = c[k].x - q.x, dy = c[k].y - q.y;
          if (dx * dx + dy * dy < GAP * GAP) { return false; }
        }
      } }
      return true;
    }
    for (var li = 0; li < left.length && dots.length < 1500; li++) {
      var lf = left[li][0], lq = left[li][1];
      if (far && (lf.properties.mn === 0 || lf.properties.mn === '0')) { continue; }
      if (!clearOf(lq) || !dotFits(lq)) { continue; }
      var dk = Math.floor(lq.x / GAP) + ':' + Math.floor(lq.y / GAP);
      (dgrid[dk] = dgrid[dk] || []).push(lq);
      dots.push(idOf(lf));
    }
    showDots(dots);
    Object.keys(els).forEach(function(id) {
      if (!want[id]) { els[id].marker.remove(); delete els[id]; }
    });
    Object.keys(want).forEach(function(id) {
      if (!els[id]) { els[id] = make(want[id]); }
      paint(els[id]);
    });
  }
  // Which dots the GL layers draw: only the ids the placement let through.
  var dotKey = null;
  function showDots(ids) {
    var key = ids.join('|');
    if (key === dotKey) { return; }
    dotKey = key;
    var only = ['in', ['to-string', ['get', 'id']], ['literal', ids]];
    [[src + '-dot', loose], [src + '-shadow', loose], [src + '-head-dot', pileHead],
     [src + '-head-shadow', pileHead], [src + '-mini', mini]].forEach(function(l) {
      if (map.getLayer(l[0])) { map.setFilter(l[0], ['all', l[1], only]); }
    });
  }
  function soon() { if (!raf) { raf = requestAnimationFrame(place); } }
  map.on('move', soon);
  map.on('resize', soon);

  var byId = {};
  var api = {
    setData: function(features) {
      var piled = atMarkPiles(features);
      map.getSource(src).setData({type: 'FeatureCollection', features: piled});
      byId = {};
      piled.forEach(function(f) { byId[idOf(f)] = f; });
      order = piled.slice().sort(function(a, z) {
        var pa = a.properties.pr, pz = z.properties.pr;
        return (pa === undefined || pa === null ? 1 : pa) - (pz === undefined || pz === null ? 1 : pz);
      });
      // A tree that left the data takes its pin with it.
      Object.keys(els).forEach(function(id) {
        if (!byId[id]) { els[id].marker.remove(); delete els[id]; }
        else { els[id].f = byId[id]; }
      });
      if (sel !== null && !byId[sel]) { sel = null; }
      if (hov !== null && !byId[hov]) { hov = null; }
      place();
    },
    // The chosen tree: the pin grows and turns moss. null lets it go.
    select: function(id) { sel = id === null || id === undefined ? null : String(id); place(); },
    // The tree the list is pointing at, Airbnb's hover. null lets it go.
    hover: function(id) {
      var next = id === null || id === undefined ? null : String(id);
      if (next === hov) { return; }
      hov = next; place();
    },
    has: function(id) { return Boolean(byId[String(id)]); },
    selected: function() { return sel; },
    feature: function(id) { return byId[String(id)] || null; },
    // Saves and ticks changed: the corners, and the saved-first order.
    marks: function() { place(); },
    // A chosen walk dims every tree not on it (ids: an array), null undims.
    dim: function(ids) {
      dimmed = null;
      if (ids && ids.length) { dimmed = {}; ids.forEach(function(id) { dimmed[String(id)] = true; }); }
      var op = dimmed ? ['case', ['in', ['to-string', ['get', 'id']], ['literal', Object.keys(dimmed)]], 0.3, 1] : 1;
      [src + '-dot', src + '-head-dot'].forEach(function(l) {
        map.setPaintProperty(l, 'circle-opacity', op);
        map.setPaintProperty(l, 'circle-stroke-opacity', op);
      });
      [src + '-shadow', src + '-head-shadow'].forEach(function(l) {
        map.setPaintProperty(l, 'circle-opacity', dimmed ? ['case', ['in', ['to-string', ['get', 'id']], ['literal', Object.keys(dimmed)]], 0.3, 1] : 1);
      });
      place();
    },
    fanPin: fanPin
  };
  atPileLayers(map, src, src, function(p, c) { tapAt = Date.now(); o.open(p, c); }, null, fanPin);
  AT_PIN_SETS.push(api);
  return api;
}
// One save or tick repaints every map's pins. tree-actions-js.ts calls
// atPaintPinFaves after every save; atMapCard calls atPaintSeen after a card
// opens; both may already be taken by the page, so they are chained.
(function() {
  var faves = window.atPaintPinFaves, seen = window.atPaintSeen;
  window.atPaintPinFaves = function() {
    if (faves) { try { faves(); } catch (e) {} }
    AT_PIN_SETS.forEach(function(s) { s.marks(); });
  };
  window.atPaintSeen = function() {
    if (seen) { try { seen(); } catch (e) {} }
    AT_PIN_SETS.forEach(function(s) { s.marks(); });
  };
})();

// THE TAPPED TREE'S CARD on a map of tree pins: the pin is chosen, the one
// card opens beside it (map-card-js.ts), and the card letting go lets the pin
// go. cardFor(props) may hand over the page's own card for the tree (the city
// list, the profile grid); otherwise the card comes from /api/cards.json, and
// a tree the catalogue does not know gets one from what the pin carries.
function atTreePinCard(map, pins, cardFor) {
  var ctl = atMapCard(map, { gap: 36, onClose: function() { pins.select(null); } });
  var C = window.atCollection;
  map.once('idle', function() { if (C && C.catalogue) C.catalogue(); });
  var asked = 0;
  var openOne = function(p, c) {
    var mine = ++asked;
    var id = p.id || '';
    pins.hover(null);
    pins.select(id);
    var own = cardFor ? cardFor(p) : null;
    if (own) { ctl.open(own.el || own, c, own.href || null); return; }
    var known = C && C.catalogue ? C.catalogue() : Promise.resolve({});
    known.then(function(cards) {
      if (mine !== asked) return;
      var k = (id && cards[id]) || { n: p.name || '', c: p.city || '' };
      var rec = {};
      for (var key in k) { rec[key] = k[key]; }
      if (p.url) { rec.u = p.url; }
      var saved = Boolean(window.atHasSaved && window.atHasSaved(id));
      var seen = Boolean(window.atHasVisited && window.atHasVisited(id));
      var html = C && C.card ? C.card(id, rec, saved, seen) : '';
      if (html) { ctl.open(html, c, rec.u || null); }
    });
  };
  openOne.close = ctl.close;
  openOne.isOpen = ctl.isOpen;
  return openOne;
}

// POINTING AT A TREE IN THE LIST LIGHTS ITS PIN, on a computer (Airbnb's list,
// AllTrails' web map; Hidde, 2026-11-10: "als ik hover over de afbeeldingen in
// de lijst dat de pin dan duidelijk wordt"). Any element carrying the tree's
// id (data-tree-id, or data-pin-id where the pin's id differs) lights it,
// except while a pin's card is open. idOf maps an element to the pin's id.
function atPinsFollowList(pins, card, idOf) {
  if (!(window.matchMedia && window.matchMedia('(hover: hover) and (min-width: 800px)').matches)) { return; }
  // data-id: the profile's own-tree tiles (my-trees-js.ts), which idOf maps.
  var sel = '[data-pin-id], [data-tree-id], .saved-list [data-id]';
  function idFor(el) {
    if (idOf) { return idOf(el); }
    return el.getAttribute('data-pin-id') || el.getAttribute('data-tree-id');
  }
  document.addEventListener('mouseover', function(e) {
    var el = e.target.closest && e.target.closest(sel);
    if (!el || el.closest('.maplibregl-map')) { return; }
    if (card && card.isOpen && card.isOpen()) { return; }
    var id = idFor(el);
    if (id && pins.has(id)) { pins.hover(id); }
  });
  document.addEventListener('mouseout', function(e) {
    var el = e.target.closest && e.target.closest(sel);
    if (!el) { return; }
    var to = e.relatedTarget && e.relatedTarget.closest && e.relatedTarget.closest(sel);
    if (to === el) { return; }
    pins.hover(null);
  });
}
`;
}
