// FLY, THEN THE CITY (Hidde, 2026-11-26: "A, fly and fade"; step 3 of the one
// map, lib/one-map.ts, CONVENTIONS.md "One map or two"). A city picked in the
// search on the map does not leave the map: the map flies to the city's trees,
// and when it lands the city's page takes the panel's place at exactly that
// view (#map=, which every map reads, tree-map-js.ts), without a page load
// since 2026-11-27 (soft-nav-js.ts). The cross-page fade of 2026-11-26 showed
// the city twice (Hidde: "very cringe").
//
// Text inside a map script: needs maplibregl and atSheetTop (sheet-js.ts) when
// there is a sheet. The trees' places come from /api/pins.json
// ([id, lng, lat, city slug, ...]), the file every map already fetches.
export function flyToCityJs(): string {
  return `
function atFlyToCity(map, slug) {
  var page = '/' + slug;
  // The city's page is fetched while the map flies, and swapped in where it
  // lands, without a page load (soft-nav-js.ts, Hidde 2026-11-27: "ok bouw
  // optie 2"); a browser without that loads the page as before.
  if (window.atPage && window.atPage.prefetch) { window.atPage.prefetch(page); }
  // Where you were before the flight: Back returns there, not to the city
  // the flight passed on its way (the map keeps its place in the address).
  var c0 = map.getCenter(), was = '#map=' + map.getZoom().toFixed(2) + '/' + c0.lat.toFixed(5) + '/' + c0.lng.toFixed(5);
  function go() {
    var c = map.getCenter();
    var hash = '#map=' + map.getZoom().toFixed(2) + '/' + c.lat.toFixed(5) + '/' + c.lng.toFixed(5);
    try { if (/^#map=|^$/.test(location.hash)) { history.replaceState(history.state, '', location.pathname + location.search + was); } } catch (e) {}
    if (window.atPage && window.atPage.go) { window.atPage.go(page, hash); return; }
    location.href = page + hash;
  }
  function fly(rows) {
    var lngs = [], lats = [];
    rows.forEach(function(r) {
      if (r[3] === slug && r[1] !== null && r[2] !== null) { lngs.push(r[1]); lats.push(r[2]); }
    });
    var n = lngs.length;
    if (!n) { location.href = page; return; }
    // The middle 96 percent of its trees, as the search frames a country, so
    // one day trip far out does not pull the view away from the city.
    lngs.sort(function(a, z) { return a - z; }); lats.sort(function(a, z) { return a - z; });
    var lo = Math.floor((n - 1) * 0.02), hi = Math.ceil((n - 1) * 0.98);
    var b = new maplibregl.LngLatBounds([lngs[lo], lats[lo]], [lngs[hi], lats[hi]]);
    var lift = 0;
    try {
      var mr = map.getContainer().getBoundingClientRect();
      var st = window.atSheetTop ? window.atSheetTop() : null;
      if (st !== null && st < mr.bottom) { lift = Math.min(mr.bottom - st, mr.height * 0.6); }
    } catch (e) {}
    var done = false;
    function land() { if (done) { return; } done = true; go(); }
    map.once('moveend', land);
    setTimeout(land, 3000);
    map.fitBounds(b, { padding: {top: 100, left: 40, right: 40, bottom: 40 + lift}, maxZoom: 13, duration: 1400 });
  }
  if (atFlyToCity.rows) { fly(atFlyToCity.rows); return; }
  fetch('/api/pins.json').then(function(r) { return r.json(); })
    .then(function(j) { atFlyToCity.rows = j; fly(j); })
    .catch(function() { location.href = page; });
}
`;
}
