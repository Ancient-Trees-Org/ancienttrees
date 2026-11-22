// THE SEE ALL PAGE OF NEW FROM VISITORS (/visitors; Hidde, 2026-11-18: "a
// see all button from new from visitors that leads to a page that has
// infinite scroll on it", then "ok build the see all page").
//
// Convention: Unsplash's and Pinterest's photo feed, a masonry of WHOLE
// photographs, newest first, more loading as you near the end (CONVENTIONS.md
// 2026-10-10: endless scroll is for endless similar items). The home row
// crops each photograph to 4:3; here a portrait phone photograph keeps its
// crown and its foot. Each tile is the row's own card (VisitorsPage.astro
// reuses its classes), and a name behaves as it does in the row: a public
// profile's name opens it, signed out it asks for a sign-in first.
//
// The server pages by the last row seen (supabase/visitor-photos.sql), so a
// photograph that goes live while somebody scrolls never repeats a tile.
// Until that function exists it shows the home row's 24 and stops. What each
// tree looks like is baked into the page (#vp-data, lib/visitor-cards.ts),
// with each photograph's size, so a tile takes its place before it loads.
// Nothing is kept on the device.
import { SUPABASE_URL, SUPABASE_KEY } from "./site-config";
import { saveButtonJs } from "./save-button";
import { AGO_FN } from "./time-ago-js";

// The save on each tile (Hidde, 2026-11-19: "het zou heel logisch zijn als er
// een bookmark icontje is bij elke boom", then "Yes, both" for the home row
// too): the card heart every list carries, SaveHeart.astro look "card" and
// map.ts _heart(), painted and handled by TREE_ACTIONS_JS, which the page
// including this must ship. A sibling of the tile's link, never inside it, so
// a tap saves and does not open the tree. One function for the home row and
// /visitors, so the two tiles cannot drift.
// The button is the one save button (lib/save-button.ts), SaveHeart's own
// function; this only says what goes in it. The meta is the city here.
export function visitorSaveFn(saveWord: string, savedWord: string): string {
  return `${saveButtonJs()}
  function nfvSave(id, c, esc) {
    return atSaveButton({ id: id, name: c.n, save: ${JSON.stringify(saveWord)}, saved: ${JSON.stringify(savedWord)},
      url: c.u, photo: c.p, meta: c.c, look: 'card',
      pressed: Boolean(window.atHasSaved && window.atHasSaved(id)) });
  }`;
}

// THE TILE ITSELF, one function for the home row and /visitors, matching the
// apps' tile (Hidde, 2026-11-20: "A, met boomnaam"; CONVENTIONS.md "A heart for
// a visitor's photograph ... who and when on it"): the photograph with the
// city as a tag on it (the apps' TagPill), the save top right, the tree's name
// under it, then the byline: face, name, when it was sent. The script that
// includes this defines esc(), A_VISITOR and nfvSave(). `ask` is the class a
// signed-out name carries (each script answers its own), `extra` its data.
export function visitorTileFn(): string {
  return `${AGO_FN}
  function nfvTile(r, c, img, ev, ask, extra) {
    var real = r.author_name || null;
    var name = real || A_VISITOR;
    var av = r.author_avatar && real
      ? '<img src="' + esc(r.author_avatar) + '" alt="" loading="lazy">'
      : '<span>' + esc(name.charAt(0)) + '</span>';
    var when = atAgo(r.published_at, false);
    var line = '<span class="nfv-av" aria-hidden="true">' + av + '</span><span class="nfv-name">' + esc(name) + '</span>' +
      (when ? '<span class="nfv-when">' + esc(when) + '</span>' : '');
    var who = real
      ? (r.author_id
          ? '<a class="nfv-who" href="/profile?u=' + encodeURIComponent(r.author_id) + '">' + line + '</a>'
          : '<button type="button" class="nfv-who ' + ask + '" data-sighting="' + esc(r.sighting_id) + '"' + (extra || '') + '>' + line + '</button>')
      : '<span class="nfv-who">' + line + '</span>';
    // The heart at the line's end, beside the name and never inside its link
    // (lib/photo-likes-js.ts fills the slot; Hidde, 2026-11-20).
    var like = '<span class="nfv-like" data-photo-like="' + esc(String(r.sighting_id).toLowerCase()) + '"></span>';
    return '<a class="nfv-tree" href="' + esc(c.u) + '" data-ev="' + ev + '" data-detail="' + esc(r.tree_id) + '">' +
      '<span class="shelf-ph" data-dbl-heart="' + esc(String(r.sighting_id).toLowerCase()) + '">' + img + '<span class="nfv-tag">' + esc(c.c) + '</span></span>' +
      '<b>' + esc(c.n) + '</b></a>' + nfvSave(r.tree_id, c, esc) + '<div class="nfv-by">' + who + like + '</div>';
  }`;
}

/** Tiles per request: two screens on a laptop, four on a phone. */
export const VISITORS_PAGE = 24;

export function visitorsPageJs(visitorWord: string, saveWord: string, savedWord: string): string {
  return `
<script>
(function () {
  var SB = ${JSON.stringify(SUPABASE_URL)}, KEY = ${JSON.stringify(SUPABASE_KEY)};
  var A_VISITOR = ${JSON.stringify(visitorWord)};
  ${visitorSaveFn(saveWord, savedWord)}
  ${visitorTileFn()}
  var N = ${VISITORS_PAGE};
  var cards = {}, rows = [], cursor = null, done = false, busy = false, token = null, paged = true;
  var grid, more, end, cols = [], ncols = 0;
  function esc(t) { return String(t == null ? '' : t)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function rpc(name, body, tok) {
    return fetch(SB + '/rest/v1/rpc/' + name, {
      method: 'POST',
      headers: { 'apikey': KEY, 'Authorization': 'Bearer ' + (tok || KEY), 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    }).then(function (r) { if (!r.ok) throw r.status; return r.json(); });
  }
  // One page after the cursor; the home row's 24 while visitor_photos is not
  // there yet (and then nothing more).
  function page(tok) {
    if (!paged) return Promise.resolve([]);
    var body = { n: N };
    if (cursor) { body.before_at = cursor.at; body.before_id = cursor.id; }
    return rpc('visitor_photos', body, tok).catch(function (e) {
      if (cursor) throw e;
      paged = false;
      return rpc('new_from_visitors', { n: 24 }, tok);
    });
  }
  function columns() {
    var w = grid.clientWidth;
    return w >= 1100 ? 5 : w >= 860 ? 4 : w >= 560 ? 3 : 2;
  }
  function tile(r, prev) {
    var c = cards[r.tree_id];
    var src = c.s[r.sighting_id];
    var d = c.d && c.d[r.sighting_id];
    var img = d
      ? '<img src="' + esc(src) + '" width="' + d[0] + '" height="' + d[1] + '" alt="" loading="lazy">'
      : '<img class="vp-noratio" src="' + esc(src) + '" alt="" loading="lazy">';
    var extra = prev ? ' data-prev-at="' + esc(prev.published_at) + '" data-prev-id="' + esc(prev.sighting_id) + '"' : '';
    var el = document.createElement('div');
    el.className = 'shelf-card nfv-card';
    el.innerHTML = nfvTile(r, c, img, 'visitors-page', 'vp-ask', extra);
    return el;
  }
  // Each tile into the shortest column, in order, so the newest stand at the
  // top left and the order reads across, as Pinterest places its pins.
  function place(el) {
    var low = cols[0];
    for (var i = 1; i < cols.length; i++) if (cols[i].offsetHeight < low.offsetHeight) low = cols[i];
    low.appendChild(el);
  }
  function layout() {
    var n = columns();
    if (n === ncols) return;
    ncols = n;
    grid.innerHTML = '';
    cols = [];
    for (var i = 0; i < n; i++) { var c = document.createElement('div'); c.className = 'vp-col'; grid.appendChild(c); cols.push(c); }
    rows.forEach(function (r) { place(tile(r, r.prev)); });
    if (window.atPaintSaveButtons) window.atPaintSaveButtons();
    if (window.atPhotoLikes) window.atPhotoLikes.load();
  }
  // r.prev is the row the SERVER sent before it (a tile with no card is
  // skipped on the page but still counts as the cursor for the next one).
  var prevRaw = null;
  function add(list) {
    list = Array.isArray(list) ? list : [];
    list.forEach(function (r) {
      r.prev = prevRaw;
      prevRaw = r;
      // Only a photograph this build carries as THAT visitor's: one that went
      // live after the build used to show the tree's lead in its place, the
      // same picture as another tile (Hidde, 2026-11-19: "i see a lot of
      // duplicates here"). It appears with the next deploy, as in the apps.
      var c = cards[r.tree_id];
      if (!c || !(c.s && c.s[r.sighting_id])) return;
      rows.push(r);
      place(tile(r, r.prev));
    });
    var last = list[list.length - 1];
    if (last) cursor = { at: last.published_at, id: last.sighting_id };
    if (window.atPaintSaveButtons) window.atPaintSaveButtons();
    if (window.atPhotoLikes) window.atPhotoLikes.load();
    if (!paged || list.length < N) finish();
  }
  function finish() {
    done = true;
    more.hidden = true;
    if (rows.length) end.hidden = false;
  }
  function next() {
    if (busy || done) return;
    busy = true;
    page(token).then(add, function () { finish(); }).then(function () {
      busy = false;
      if (!done && more.getBoundingClientRect().top < innerHeight + 1200) next();
      if (window.atPendingVisitor) window.atGoVisitor();
    });
  }
  // Whose photograph this is, asked as a signed-in caller: the row just
  // before it in the feed is the cursor that returns exactly this one.
  function author(b, tok) {
    var body = { n: 1 };
    if (b.dataset.prevAt) { body.before_at = b.dataset.prevAt; body.before_id = b.dataset.prevId; }
    var ask = paged ? rpc('visitor_photos', body, tok) : rpc('new_from_visitors', { n: 24 }, tok);
    return ask.then(function (list) {
      var hit = (list || []).filter(function (r) { return r.sighting_id === b.dataset.sighting; })[0];
      return hit && hit.author_id;
    }).catch(function () { return null; });
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('.vp-ask');
    if (!b) return;
    var ask = function () { if (window.atOpenSignIn) window.atOpenSignIn(null, null, { kind: 'visitor', sighting: b.dataset.sighting }); };
    var C = window.atCollection;
    if (!C || !C.gate) { ask(); return; }
    C.gate(function (s) {
      author(b, s.access_token).then(function (id) { if (id) location.href = '/profile?u=' + encodeURIComponent(id); });
    }, ask);
  });
  // After the sign-in a name asked for (signin-js hands the photograph over
  // as atPendingVisitor): finish the tap once its tile is on the page.
  window.atGoVisitor = function () {
    var id = window.atPendingVisitor, C = window.atCollection;
    if (!id || !C || !C.gate) return;
    var b = document.querySelector('.vp-ask[data-sighting="' + id + '"]');
    if (!b) return;
    window.atPendingVisitor = null;
    C.gate(function (s) {
      author(b, s.access_token).then(function (uid) { if (uid) location.href = '/profile?u=' + encodeURIComponent(uid); });
    }, function () {});
  };
  function start() {
    grid = document.getElementById('vp-grid');
    more = document.getElementById('vp-more');
    end = document.getElementById('vp-end');
    var el = document.getElementById('vp-data');
    if (!grid || !el) return;
    try { cards = JSON.parse(el.textContent || '{}'); } catch (e) { return; }
    layout();
    var resized;
    addEventListener('resize', function () { clearTimeout(resized); resized = setTimeout(layout, 150); });
    var go = function () {
      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (es) { if (es[0].isIntersecting) next(); }, { rootMargin: '1200px 0px' }).observe(more);
      }
      next();
    };
    // The server decides who is signed in (atCollection.gate); signed in, the
    // names come with the account id and open the profile directly.
    var C = window.atCollection;
    if (C && C.gate) C.gate(function (s) { token = s.access_token; go(); }, go);
    else go();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
</script>`;
}
