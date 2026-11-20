// Your collection, read from your account and from nowhere else.
//
// WHAT THIS REPLACES, and why it is one file instead of the two it grew from
// (Hidde, 2026-09-02): "ik wil dat je ervoor zorgt dat er niets meer lokaal
// wordt opgeslagen. Alles wat wordt opgeslagen, moet op je account zijn. Dus
// zodra je iets liket of wat dan ook, moet dat achter een account staan."
//
// Saving was already account-gated (2026-08-30), but the SAVE ITSELF was still
// written to localStorage as a cache, and a cache with its own history is a
// second source of truth. Three faults came out of that one decision, and he
// found all three in a morning:
//
//   * Saves made in one browser before the gate existed were unioned INTO his
//     account on the next sign-in, so his account page filled up with trees he
//     had never deliberately kept ("ik zie nog steeds heel veel saved trees").
//   * A card rendered from the snapshot taken when the heart was tapped, so a
//     tree that has a photograph today showed none if it had none then, and a
//     save made in the app carried no name at all ("ik weet zeker dat hier
//     bomen tussen staan die wel een foto hebben die we nu niet tonen").
//   * That snapshot was drawn by hand-written markup instead of the one tree
//     card, so the saved list was the only place on the site where a tree does
//     not look like a tree ("een soort van boomkaart die ik helemaal niet zie
//     terugkomen op saved trees").
//
// So: the account holds WHICH trees, /api/cards.json holds WHAT THEY ARE, and
// this file joins the two. Nothing is remembered on the device. The only thing
// still in localStorage anywhere is the session token, which is not a saved
// tree, it is the account.
//
// Convention: Strava, AllTrails and Google Maps all keep the saved list inside
// the account and all render a saved item with the same card the rest of the
// product uses. See CONVENTIONS.md, "What signing out takes with it": signing
// out takes the list off the screen and the next sign-in brings it all back,
// because it lives in the account rather than on the glass.
import { SUPABASE_URL, SUPABASE_KEY } from "./site-config";
import { treeCardJs } from "./tree-card";
import { seasonChipHtml } from "./phenology";
import { ui } from "./i18n";

const EN = ui("en");
// The season chips the card can show, by key, as the server writes them.
const CHIPS = Object.fromEntries(["bloom", "autumn", "fruit", "leaves", "catkins", "winter"].map((k) => [k, seasonChipHtml(k, EN)]));
// The card's save control is the app's bookmark (2026-10-09), the same pair
// SaveHeart.astro renders, shown one at a time by aria-pressed.

export const COLLECTION_JS = `
<script>
// Included by a page's own scripts AND by Base.astro (for the search field's
// recent searches, 2026-11-04), so the first copy wins and a second is a no-op:
// one session check per page, never two doors.
window.atCollection = window.atCollection || (function() {
${treeCardJs()}
var CARD_WORDS = ${JSON.stringify({ save: EN.cardSave, saved: EN.cardSaved, noPhoto: EN.noPhotoYet, seen: EN.seenChip })};
var CARD_CHIPS = ${JSON.stringify(CHIPS)};
  var SB = '${SUPABASE_URL}', KEY = '${SUPABASE_KEY}';
  // In memory for the life of this page only. Deliberately not sessionStorage:
  // that is storage too, and the rule is the rule.
  var cardsWait = null;

  // The server's verdict on the stored session: null until it answers, then
  // true or false. A session the server refused is no session, whatever the
  // browser still holds (2026-10-05, the sixth time Hidde saw a heart work
  // signed out).
  var confirmed = null;
  function session() {
    if (confirmed === false) return null;
    try {
      var s = JSON.parse(localStorage.getItem('ancienttrees_session'));
      return (s && s.access_token && s.expires_at > Date.now() / 1000) ? s : null;
    } catch (e) { return null; }
  }
  // THE SERVER DECIDES WHO IS SIGNED IN, NEVER THE BROWSER (Hidde, 2026-10-02:
  // "I can still do thumbs up save and collect tree without being logged in
  // on the website ... close this gap forever! No local storage!"). Until
  // tonight every script here trusted a session object in localStorage by its
  // own expires_at: a token revoked elsewhere, a deleted account or a hand
  // edited value painted the whole site signed in, hearts lit on tap, and the
  // refused write was swallowed. So: a stored session is CHECKED with Supabase
  // once per page load, any write the server refuses forgets it, and
  // forgetting repaints every control and the bar and opens the sign-in
  // dialog. The smoke test plants a fake session and clicks Save to prove it.
  function forget() {
    try { localStorage.removeItem('ancienttrees_session'); } catch (e) {}
    try { delete document.documentElement.dataset.signedIn; } catch (e) {}
    if (window.atPaintNav) { try { window.atPaintNav(false); } catch (e) {} }
    try { document.dispatchEvent(new CustomEvent('at:signedout')); } catch (e) {}
  }
  function refused(r) {
    if (r && (r.status === 401 || r.status === 403)) {
      forget();
      if (window.atOpenSignIn) { try { window.atOpenSignIn(); } catch (e) {} }
      return true;
    }
    return false;
  }
  var verified = null;
  // WHO the server says this is, kept from the same answer: the address a
  // gated act will be answered at. A control that commits somebody to
  // something (the ambassador request, 2026-10-07) prints it, so "signed in"
  // is never a guess on either side of the screen.
  var who = null;
  var waitedForRenewal = false;
  function renewable() {
    try {
      var s = JSON.parse(localStorage.getItem('ancienttrees_session'));
      return !!(s && s.refresh_token && !(s.expires_at > Date.now() / 1000));
    } catch (e) { return false; }
  }
  function parsed() {
    return new Promise(function(done) {
      if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function() { done(); });
      else done();
    });
  }
  function verify() {
    if (verified) return verified;
    // A spent token with a refresh token beside it is renewed by signin-js
    // (window.atRefreshing), and who is signed in is decided after that answer,
    // never before it (2026-11-17). This script can run BEFORE signin-js (a
    // page that includes it itself: the first copy wins), so it waits for the
    // page to be parsed, then for the renewal. Once only: a second pass decides.
    if (!waitedForRenewal && !session() && renewable()) {
      waitedForRenewal = true;
      return (verified = parsed().then(function() {
        return Promise.resolve(window.atRefreshing).catch(function() {});
      }).then(function() {
        verified = null;
        return verify();
      }));
    }
    var s = session();
    if (!s) return (verified = Promise.resolve(false));
    verified = fetch(SB + '/auth/v1/user', { headers: { 'apikey': KEY, 'Authorization': 'Bearer ' + s.access_token } })
      .then(function(r) {
        if (r.status === 401 || r.status === 403) { confirmed = false; forget(); return false; }
        confirmed = r.ok;
        if (!r.ok) return false;
        return r.json().then(function(u) { who = (u && u.email) || null; return true; }, function() { return true; });
      })
      .catch(function() { confirmed = true; return true; });   // offline: keep the session, the next write decides
    return verified;
  }
  // EVERY GATED TAP GOES THROUGH HERE: save, seen, vote, photo, report. It
  // acts only once the server has said this session is real; otherwise it
  // opens sign-in and does nothing else. One door, so no control can trust the
  // browser on its own again.
  function gate(onIn, onOut) {
    verify().then(function(ok) {
      var s = ok && session();
      if (s) onIn(s); else onOut();
    });
  }
  window.atGate = gate;
  function api(path, s, opts) {
    opts = opts || {};
    var h = { 'apikey': KEY, 'Authorization': 'Bearer ' + s.access_token };
    if (opts.body) { h['Content-Type'] = 'application/json'; h['Prefer'] = 'resolution=merge-duplicates'; }
    return fetch(SB + path, { method: opts.method || 'GET', headers: h,
                              body: opts.body ? JSON.stringify(opts.body) : undefined })
      .then(function(r) { refused(r); return r; });
  }
  verify();
  // What a tree IS, answered by the website rather than remembered by the
  // browser. One request, held for this page, shared by every caller.
  function catalogue() {
    if (cardsWait) return cardsWait;
    cardsWait = fetch('/api/cards.json')
      .then(function(r) { return r.ok ? r.json() : {}; })
      .catch(function() { return {}; });
    return cardsWait;
  }
  function esc(t) { return String(t == null ? '' : t)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;'); }

  // THE SAME CARD AS EVERYWHERE ELSE. It cannot literally be TreeCard.astro,
  // which renders at build time, so it emits that component's markup from the
  // component's own data: the meta line arrives composed, the photograph
  // arrives at the two widths TreeCard asks for, and the credit arrives only
  // when the licence obliges one. Nothing here decides any of that.
  // "visited" adds the "Seen" badge over the photo, the same per-tree signal
  // TreeCard.swift's own "ticked" view draws (a filled checkmark-seal capsule,
  // top left) whenever saved.isVisited(tree.id) is true, regardless of
  // which list the card happens to render in. Web had no such badge and
  // "hearted" used to be one blanket value for a WHOLE list rather than each
  // card's own true state, so My trees and Favourites read as the same
  // unmarked card everywhere (Hidde, 2026-09-03).
  function card(id, c, hearted, visited) {
    var common = String(c.sp || '').replace(/\\s*\\(.*\\)\\s*$/, '').trim();
    var month = new Date().getMonth() + 1;
    var icons = window.AT_PIN_ICONS || null;
    return atTreeCard({
      id: id, name: c.n || '', href: c.u || '', variant: 'compact', index: null, h: 3,
      metaParts: [common, c.ag || ''],
      photo: c.p ? { src: c.p, srcset: c.p + ' 500w, ' + (c.p9 || c.p) + ' 900w', sizes: '(max-width: 800px) 100vw, 560px' } : null,
      savePhoto: c.p || '',
      // The species drawing for a tree without a photograph, where the page
      // carries the pins' drawings (every map does); else the broadleaf crown.
      tileIcon: c.p ? '' : (icons ? (icons[c.ic || 'broadleaf'] || icons.broadleaf) : ''),
      commonName: common,
      chipHtml: c.bt && c.sk && CARD_CHIPS[c.sk] && c.bt.indexOf(month) !== -1 ? CARD_CHIPS[c.sk] : '',
      seen: Boolean(visited),
      creditHtml: c.ch || '',
      // An app-only tree (cards.json "a") has no page: the name is no link,
      // and the card says where its story is.
      appHtml: c.a ? '<p class="tree-meta tree-app-only"><a href="/app" data-app-download>Read its story in the app</a></p>' : ''
    }, CARD_WORDS);
  }

  function ids(path) {
    var s = session();
    if (!s) return Promise.resolve([]);
    return api(path, s)
      .then(function(r) { return r.ok ? r.json() : []; })
      .then(function(rows) { return (rows || []).map(function(r) { return r.tree_id; }); })
      .catch(function() { return []; });
  }

  return {
    session: session,
    who: function() { return who; },
    forget: forget,
    verify: verify,
    gate: gate,
    catalogue: catalogue,
    card: card,
    esc: esc,
    /** Tree ids this account wants to visit, newest first. Signed out: nothing, and no request.
        Read from the server's wishes view, which drops a save made before the tree was collected
        (supabase/wishes.sql, Hidde 2026-11-02); the saves table answers until that view exists. */
    saves: function() {
      var s = session();
      if (!s) return Promise.resolve([]);
      return api('/rest/v1/wishes?select=tree_id&order=created_at.desc', s)
        .then(function(r) {
          if (!r.ok) return ids('/rest/v1/saves?select=tree_id&order=created_at.desc');
          return r.json().then(function(rows) { return (rows || []).map(function(x) { return x.tree_id; }); });
        })
        .catch(function() { return []; });
    },
    /** Tree ids this account has checked in at, newest first. */
    visited: function() { return ids('/rest/v1/visited?select=tree_id&order=created_at.desc'); },
    save: function(id, on) {
      var s = session();
      if (!s) return Promise.resolve(false);
      var p = on
        // A fresh created_at: a heart put on a collected tree is a new wish (wishes.sql).
        ? api('/rest/v1/saves?on_conflict=user_id,tree_id', s, { method: 'POST', body: [{ tree_id: id, created_at: new Date().toISOString() }] })
        : api('/rest/v1/saves?tree_id=eq.' + encodeURIComponent(id), s, { method: 'DELETE' });
      return p.then(function(r) { return r.ok; }).catch(function() { return false; });
    },
    /** The day this account collected one tree, "YYYY-MM-DD", or null. */
    visitedOn: function(id) {
      var s = session();
      if (!s) return Promise.resolve(null);
      return api('/rest/v1/visited?select=visited_at&tree_id=eq.' + encodeURIComponent(id), s)
        .then(function(r) { return r.ok ? r.json() : []; })
        .then(function(rows) { return rows && rows[0] ? rows[0].visited_at : null; })
        .catch(function() { return null; });
    },
    visit: function(id, on, day) {
      var s = session();
      if (!s) return Promise.resolve(false);
      // day: Undo puts a tick back on the day it was first made (2026-10-10).
      var row = day ? { tree_id: id, visited_at: day } : { tree_id: id };
      var p = on
        ? api('/rest/v1/visited?on_conflict=user_id,tree_id', s, { method: 'POST', body: [row] })
        : api('/rest/v1/visited?tree_id=eq.' + encodeURIComponent(id), s, { method: 'DELETE' });
      return p.then(function(r) { return r.ok; }).catch(function() { return false; });
    }
  };
})();
</script>
`;
