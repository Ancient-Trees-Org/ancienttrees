// NEW FROM VISITORS on the web homepage, the app's Discover row of the same
// name (Kit/NewFromVisitors.swift, Screens/Home.swift; Hidde, 2026-11-06).
//
// Convention: the app's row, which is Unsplash's and Pinterest's creator line
// under a tile. The tile is this page's own shelf card; nothing new is drawn.
//
// The newest photographs visitors sent that went live on one of our trees,
// from the server (supabase/new-from-visitors.sql, anon-readable): one tile
// per tree, newest first, the row only from four tiles so it never stands half
// empty. Under each tile one line: a 16px avatar and the name of a public
// profile (a generated "Green Fig 1965" too, linked like any other; Hidde,
// 2026-11-07), else "A visitor". The name shows to everyone; a tap opens the profile, and signed
// out it asks for a sign-in first, the Instagram and Pinterest way (CLAUDE.md,
// Privacy and accounts). The account id only comes to a signed-in caller, so
// a signed-out page could not link the profile even if it wanted to.
//
// What a tree looks like is baked into the page at build time (#nfv-data),
// only for trees that carry a visitor's photograph: a few dozen, where
// /api/cards.json is 700 KB. A photograph newer than the last build waits for
// the next one, as its place on the tree's own page does. Nothing is kept on
// the device.
import { SUPABASE_URL, SUPABASE_KEY } from "./site-config";
import { visitorSaveFn, visitorTileFn } from "./visitors-page-js";

/** The row shows from this many tiles (NewFromVisitors.minimum). */
export const VISITORS_MIN = 4;

export function visitorsRowJs(visitorWord: string, saveWord: string, savedWord: string): string {
  return `
<script>
(function () {
  var SB = ${JSON.stringify(SUPABASE_URL)}, KEY = ${JSON.stringify(SUPABASE_KEY)};
  var A_VISITOR = ${JSON.stringify(visitorWord)};
  var MIN = ${VISITORS_MIN};
  var CARDS = {};
  ${visitorSaveFn(saveWord, savedWord)}
  ${visitorTileFn()}
  function esc(t) { return String(t == null ? '' : t)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function rpc(name, body, token) {
    return fetch(SB + '/rest/v1/rpc/' + name, {
      method: 'POST',
      headers: { 'apikey': KEY, 'Authorization': 'Bearer ' + (token || KEY), 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    }).then(function (r) { return r.ok ? r.json() : []; }).catch(function () { return []; });
  }
  // Only a photograph this build carries as THAT visitor's: one that went
  // live after the build used to show the tree's lead in its place, the
  // same picture as another tile (Hidde, 2026-11-19: "i see a lot of
  // duplicates here"). It appears with the next deploy, as in the apps.
  function usable(r, cards) { var c = cards[r.tree_id]; return !!(c && c.s && c.s[r.sighting_id]); }
  // THE ROW NEVER DEPENDS ON A FRESH DEPLOY (2026-11-22). The newest 24 first
  // (each person once before anyone twice); when fewer than MIN of them are in
  // this build, older photographs from the See all page's feed (visitor_photos,
  // newest first) fill it, a few pages back at most. A deploy that fell eleven
  // hours behind once left all twelve newest unknown and the row vanished.
  function load(token, cards, ask) {
    return (ask || rpc('new_from_visitors', { n: 24 }, token)).then(function (first) {
      first = Array.isArray(first) ? first : [];
      var out = first.slice(), trees = {}, pages = 0;
      first.forEach(function (r) { if (usable(r, cards)) trees[r.tree_id] = 1; });
      function more(cursor) {
        if (Object.keys(trees).length >= MIN * 2 || pages >= 4) return out;
        pages++;
        var body = { n: 48 };
        if (cursor) { body.before_at = cursor.published_at; body.before_id = cursor.sighting_id; }
        return rpc('visitor_photos', body, token).then(function (list) {
          list = Array.isArray(list) ? list : [];
          list.forEach(function (r) { out.push(r); if (usable(r, cards)) trees[r.tree_id] = 1; });
          return list.length < 48 ? out : more(list[list.length - 1]);
        });
      }
      return Object.keys(trees).length >= MIN ? out : more(null);
    });
  }
  function paint(rows, cards) {
    var box = document.getElementById('nfv');
    var row = box && box.querySelector('.shelf-row');
    if (!row || !Array.isArray(rows)) return;
    var seen = {}, html = [];
    rows.forEach(function (r) {
      var c = cards[r.tree_id];
      if (html.length >= 12 || seen[r.tree_id] || !usable(r, cards)) return;
      seen[r.tree_id] = 1;
      // A generated name prints and links like any other (Hidde, 2026-11-07:
      // "a visitor is weird that its unclickable just give the link to their
      // made up name"); only a private profile, which has no name to give,
      // stays "A visitor". The tile is /visitors' own (nfvTile).
      html.push('<div class="shelf-card nfv-card">' +
        nfvTile(r, c, '<img src="' + esc(c.s[r.sighting_id]) + '" alt="" loading="lazy">', 'home-visitors', 'nfv-ask', '') +
        '</div>');
    });
    if (html.length < MIN) return;
    row.innerHTML = html.join('');
    box.hidden = false;
    if (window.atPaintSaveButtons) window.atPaintSaveButtons();
    if (window.atPhotoLikes) window.atPhotoLikes.load();
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('.nfv-ask');
    if (!b) return;
    // The one door (atCollection.gate): a session the server accepts gets the
    // profile (the page may have painted before it answered); otherwise sign
    // in first, the app's nudge.require(.general).
    // The sheet keeps which name was tapped, so the sign-in ends on that
    // profile and not back here (Hidde, 2026-11-12, Isabelle R.).
    var ask = function () { if (window.atOpenSignIn) window.atOpenSignIn(null, null, { kind: 'visitor', sighting: b.dataset.sighting }); };
    var C = window.atCollection;
    if (!C || !C.gate) { ask(); return; }
    C.gate(function (s) {
      load(s.access_token, CARDS).then(function (rows) {
        var hit = (rows || []).filter(function (r) { return r.sighting_id === b.dataset.sighting; })[0];
        if (hit && hit.author_id) location.href = '/profile?u=' + encodeURIComponent(hit.author_id);
      });
    }, ask);
  });
  // AFTER THE SIGN-IN THAT A NAME ASKED FOR (2026-11-12): signin-js hands the
  // tapped photograph's id over as atPendingVisitor; the server, asked with
  // the new session, says whose it is, and the tap finishes on that profile.
  window.atGoVisitor = function () {
    var id = window.atPendingVisitor;
    var C = window.atCollection;
    if (!id) return;
    // Signin-js lands before collection-js is on the page (Base.astro puts it
    // after), so the first call can come before the one door exists; start()
    // below calls again once the page is parsed (found 2026-11-12, live test).
    if (!C || !C.gate) return;
    window.atPendingVisitor = null;
    C.gate(function (s) {
      load(s.access_token, CARDS).then(function (rows) {
        var hit = (rows || []).filter(function (r) { return r.sighting_id === id; })[0];
        if (hit && hit.author_id) location.href = '/profile?u=' + encodeURIComponent(hit.author_id);
      });
    }, function () {});
  };
  if (window.atPendingVisitor) window.atGoVisitor();
  function start() {
    if (window.atPendingVisitor) window.atGoVisitor();
    var el = document.getElementById('nfv-data');
    if (!el) return;
    var cards = {};
    try { cards = JSON.parse(el.textContent || '{}'); } catch (e) { return; }
    CARDS = cards;
    // FIRST PAINT WAITS FOR NOTHING BUT THE PHOTOS (2026-11-22, Hidde: "it
    // takes quite a time to load ... shows up later than the rest"). It used
    // to wait for the page to finish and then for the server's sign-in answer
    // before it even asked. Names show to everyone, so the public answer
    // paints the row; a tap on a name resolves the profile itself (the click
    // handler above). The server still decides who is signed in
    // (atCollection.gate): for them the row is painted again with the names as
    // direct links, the same tiles in the same order.
    var signed = false;
    load(null, cards, EARLY).then(function (r) { if (!signed) paint(r, cards); });
    var C = window.atCollection;
    if (C && C.gate) {
      C.gate(function (s) { load(s.access_token, cards).then(function (r) { signed = true; paint(r, cards); }); },
             function () {});
    }
  }
  // The first question leaves as soon as this script runs, before the page has
  // finished, so the answer is usually there by the time the row can be drawn.
  var EARLY = rpc('new_from_visitors', { n: 24 }, null);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
</script>`;
}
