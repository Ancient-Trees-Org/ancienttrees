// NEW FROM VISITORS on the web homepage, the app's Discover row of the same
// name (Kit/NewFromVisitors.swift, Screens/Home.swift; Hidde, 2026-11-06).
//
// Convention: the app's row, which is Unsplash's and Pinterest's creator line
// under a tile. The tile is this page's own shelf card; nothing new is drawn.
//
// The newest things readers put live, a tree they added or a photograph on
// one of ours, from the server (feed(), anon-readable): one tile
// per tree, newest first, the row only from four tiles so it never stands half
// empty. Under each tile one line: a 16px avatar and the name of a public
// profile (a generated "Green Fig 1965" too, linked like any other; Hidde,
// 2026-11-07), else "A visitor". The name shows to everyone; a tap opens the profile, and signed
// out it asks for a sign-in first, the Instagram and Pinterest way (CLAUDE.md,
// Privacy and accounts). The account id only comes to a signed-in caller, so
// a signed-out page could not link the profile even if it wanted to.
//
// Since 2026-11-26 everything a tile shows comes from public.feed()
// (supabase/feed.sql), never from the build: a tree the reader judge put live
// a minute ago shows at once, with its picture from the public feed bucket.
// Nothing is kept on the device.
import { SUPABASE_URL, SUPABASE_KEY } from "./site-config";
import { visitorSaveFn, visitorTileFn } from "./visitors-page-js";

/** The row shows from this many tiles (NewFromVisitors.minimum). */
export const VISITORS_MIN = 4;

export function visitorsRowJs(visitorWord: string, saveWord: string, savedWord: string, justShared: string): string {
  return `
<script>
(function () {
  var SB = ${JSON.stringify(SUPABASE_URL)}, KEY = ${JSON.stringify(SUPABASE_KEY)};
  var A_VISITOR = ${JSON.stringify(visitorWord)};
  var JUST_SHARED = ${JSON.stringify(justShared)};
  var MIN = ${VISITORS_MIN};
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
  // FROM THE SERVER ONLY (2026-11-26): feed() hands every row whole, the
  // tree's name, link, place and a picture in the public feed bucket, so the
  // row never waits on a deploy and never stands empty because the build
  // fell behind (it vanished once when one was eleven hours late).
  function load(token, ask) {
    return (ask || rpc('feed', { n: 24 }, token)).then(function (list) {
      // Checked posts only (Hidde, 2026-11-26): a share waits, 10 to 30
      // minutes, until it is a tree with its page, save and heart.
      return (Array.isArray(list) ? list : []).filter(function (f) { return f.checked !== false; }).map(nfvFrom);
    });
  }
  function paint(rows) {
    var box = document.getElementById('nfv');
    var row = box && box.querySelector('.shelf-row');
    if (!row || !Array.isArray(rows)) return;
    var seen = {}, html = [];
    rows.forEach(function (x) {
      var r = x.r, c = x.c;
      if (html.length >= 12 || seen[r.tree_id] || !c.p) return;
      seen[r.tree_id] = 1;
      // A generated name prints and links like any other (Hidde, 2026-11-07:
      // "a visitor is weird that its unclickable just give the link to their
      // made up name"); only a private profile, which has no name to give,
      // stays "A visitor". The tile is /visitors' own (nfvTile).
      html.push('<div class="shelf-card nfv-card">' +
        nfvTile(r, c, '<img src="' + esc(c.p) + '" alt="" loading="lazy">', 'home-visitors', 'nfv-ask', '') +
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
      load(s.access_token).then(function (rows) {
        var hit = (rows || []).map(function (x) { return x.r; }).filter(function (r) { return r.sighting_id === b.dataset.sighting; })[0];
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
        var hit = (rows || []).map(function (x) { return x.r; }).filter(function (r) { return r.sighting_id === id; })[0];
        if (hit && hit.author_id) location.href = '/profile?u=' + encodeURIComponent(hit.author_id);
      });
    }, function () {});
  };
  if (window.atPendingVisitor) window.atGoVisitor();
  function start() {
    if (window.atPendingVisitor) window.atGoVisitor();
    // FIRST PAINT WAITS FOR NOTHING BUT THE PHOTOS (2026-11-22, Hidde: "it
    // takes quite a time to load ... shows up later than the rest"). It used
    // to wait for the page to finish and then for the server's sign-in answer
    // before it even asked. Names show to everyone, so the public answer
    // paints the row; a tap on a name resolves the profile itself (the click
    // handler above). The server still decides who is signed in
    // (atCollection.gate): for them the row is painted again with the names as
    // direct links, the same tiles in the same order.
    var signed = false;
    load(null, EARLY).then(function (r) { if (!signed) paint(r); });
    var C = window.atCollection;
    if (C && C.gate) {
      C.gate(function (s) { load(s.access_token).then(function (r) { signed = true; paint(r); }); },
             function () {});
    }
  }
  // The first question leaves as soon as this script runs, before the page has
  // finished, so the answer is usually there by the time the row can be drawn.
  var EARLY = rpc('feed', { n: 24 }, null);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
</script>`;
}
