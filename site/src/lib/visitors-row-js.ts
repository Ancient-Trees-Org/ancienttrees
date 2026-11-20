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
  ${visitorSaveFn(saveWord, savedWord)}
  ${visitorTileFn()}
  function esc(t) { return String(t == null ? '' : t)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function load(token) {
    return fetch(SB + '/rest/v1/rpc/new_from_visitors', {
      method: 'POST',
      headers: { 'apikey': KEY, 'Authorization': 'Bearer ' + (token || KEY), 'Content-Type': 'application/json' },
      body: JSON.stringify({ n: 12 })
    }).then(function (r) { return r.ok ? r.json() : []; }).catch(function () { return []; });
  }
  function paint(rows, cards) {
    var box = document.getElementById('nfv');
    var row = box && box.querySelector('.shelf-row');
    if (!row || !Array.isArray(rows)) return;
    var seen = {}, html = [];
    rows.forEach(function (r) {
      var c = cards[r.tree_id];
      // Only a photograph this build carries as THAT visitor's: one that went
      // live after the build used to show the tree's lead in its place, the
      // same picture as another tile (Hidde, 2026-11-19: "i see a lot of
      // duplicates here"). It appears with the next deploy, as in the apps.
      if (!c || seen[r.tree_id] || !(c.s && c.s[r.sighting_id])) return;
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
      load(s.access_token).then(function (rows) {
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
      load(s.access_token).then(function (rows) {
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
    // The server decides who is signed in (atCollection.gate), never the browser.
    var C = window.atCollection;
    if (C && C.gate) {
      C.gate(function (s) { load(s.access_token).then(function (r) { paint(r, cards); }); },
                    function () { load(null).then(function (r) { paint(r, cards); }); });
    } else {
      load(null).then(function (r) { paint(r, cards); });
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
</script>`;
}
