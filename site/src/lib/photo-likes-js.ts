// THE HEART ON A VISITOR'S PHOTOGRAPH (Hidde, 2026-11-20: "dat gebruikers de
// fotos kunnen hartje geven om elkaar aan te moedigen voor de foto zelf", then
// "Ja, bouw het hartje"). Convention: CONVENTIONS.md "A heart for a visitor's
// photograph, beside save and Worth the visit; who and when on it": the
// bookmark saves the TREE in the photograph's corner, the thumb says the tree
// is worth the visit, and this heart thanks the PHOTOGRAPHER, at the end of
// their line (face, name, when).
//
// TWO TAPS, Instagram's and Strava's (2026-11-22, Hidde: "kun je ook zien ...
// wie je dat heeft gegeven?"): the heart gives or takes back; the count beside
// it opens who gave one (PhotoLikers.astro's sheet, signed in only, from
// photo_likers() in supabase/photo-hearts-who.sql).
//
// One script for every place the byline stands (the home row, /visitors, the
// tree page under the hero and in the opened photograph). A slot is
// <span data-photo-like="<photo id>"></span>; this fills it with the two
// buttons, asks the server for the counts of every slot on the page in one
// call, and keeps them in step. Signed out, a tap opens the sign-in sheet
// through the one door (atCollection.gate) and changes nothing. Nothing kept
// on the device.
import { SUPABASE_URL, SUPABASE_KEY } from "./site-config";
import { ui } from "./i18n";
import { icon } from "./icons";

const LANGS = ["en", "es", "it", "nl", "de", "pt", "fr", "ja"];

export function photoLikesJs(): string {
  const words: Record<string, string[]> = {};
  for (const l of LANGS) {
    const u = ui(l);
    words[l] = [u.photoLike, u.photoLiked, u.photoHeartsOne, u.photoHeartsMany, u.photoHeartsWho];
  }
  const off = icon("heart", "bold", "pl-off");
  const on = icon("heart", "fill", "pl-on");
  return `
<script>
(function () {
  if (window.atPhotoLikes) return;
  var SB = ${JSON.stringify(SUPABASE_URL)}, KEY = ${JSON.stringify(SUPABASE_KEY)};
  var WORDS = ${JSON.stringify(words)};
  var OFF = ${JSON.stringify(off)}, ON = ${JSON.stringify(on)};
  var lang = (document.documentElement.lang || 'en').slice(0, 2);
  var W = WORDS[lang] || WORDS.en;
  var state = {};
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return '&#' + c.charCodeAt(0) + ';'; }); }
  function hearts(n) { return n === 1 ? W[2] : W[3].replace('{n}', String(n)); }
  function call(name, body, token) {
    return fetch(SB + '/rest/v1/rpc/' + name, {
      method: 'POST',
      headers: { 'apikey': KEY, 'Authorization': 'Bearer ' + (token || KEY), 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    }).then(function (r) { return r.ok ? r.json() : []; }).catch(function () { return []; });
  }
  function show(id) {
    var s = state[id] || { n: 0, mine: false };
    document.querySelectorAll('[data-photo-like]').forEach(function (slot) {
      if (slot.getAttribute('data-photo-like') !== id) return;
      var b = slot.querySelector('.photo-like');
      if (!b) {
        b = document.createElement('button');
        b.type = 'button';
        b.className = 'photo-like';
        b.setAttribute('data-photo', id);
        b.innerHTML = OFF + ON;
        slot.appendChild(b);
        var c = document.createElement('button');
        c.type = 'button';
        c.className = 'pl-count';
        c.setAttribute('data-photo', id);
        c.hidden = true;
        slot.appendChild(c);
      }
      b.setAttribute('aria-pressed', s.mine ? 'true' : 'false');
      b.setAttribute('aria-label', s.mine ? W[1] : W[0]);
      // From one, never a zero (Hidde, 2026-08-26: "pas van 1 tellen").
      var cnt = slot.querySelector('.pl-count');
      cnt.textContent = s.n ? String(s.n) : '';
      cnt.hidden = !s.n;
      cnt.classList.toggle('on', !!s.mine);
      cnt.setAttribute('aria-label', s.n ? hearts(s.n) + '. ' + W[4] : W[4]);
    });
  }
  function load() {
    var ids = [];
    document.querySelectorAll('[data-photo-like]').forEach(function (slot) {
      var id = slot.getAttribute('data-photo-like');
      if (id && ids.indexOf(id) < 0) ids.push(id);
      if (!slot.querySelector('.photo-like')) show(id);
    });
    if (!ids.length) return;
    var go = function (token) {
      call('photo_like_counts', { ids: ids }, token).then(function (rows) {
        (rows || []).forEach(function (r) { state[r.photo_id] = { n: Number(r.likes) || 0, mine: !!r.mine }; });
        ids.forEach(show);
      });
    };
    var C = window.atCollection;
    if (C && C.gate) C.gate(function (s) { go(s.access_token); }, function () { go(null); });
    else go(null);
  }
  function write(id, give, s) {
    var h = { 'apikey': KEY, 'Authorization': 'Bearer ' + s.access_token };
    var req = give
      ? fetch(SB + '/rest/v1/photo_likes?on_conflict=user_id,photo_id', { method: 'POST',
          headers: Object.assign({ 'Content-Type': 'application/json', 'Prefer': 'resolution=ignore-duplicates' }, h),
          body: JSON.stringify([{ photo_id: id }]) })
      : fetch(SB + '/rest/v1/photo_likes?photo_id=eq.' + encodeURIComponent(id), { method: 'DELETE', headers: h });
    return req.then(function (r) { return r.ok; }).catch(function () { return false; });
  }
  // Who gave one: the followers list's rows (people-js.ts), a private
  // profile as "A visitor" without a link.
  function openLikers(id, s) {
    var dlg = document.getElementById('pl-sheet');
    var list = document.getElementById('pl-list');
    if (!dlg || !list) return;
    var n = (state[id] || {}).n || 0;
    document.getElementById('pl-title').textContent = hearts(n);
    list.innerHTML = '';
    if (dlg.showModal && !dlg.open) dlg.showModal();
    call('photo_likers', { photo: id }, s.access_token).then(function (rows) {
      var anon = list.getAttribute('data-anon') || '';
      if (rows && rows.length) document.getElementById('pl-title').textContent = hearts(rows.length);
      list.innerHTML = (rows || []).map(function (p) {
        var name = p.display_name || anon;
        var av = p.avatar_url && /^https:/.test(p.avatar_url)
          ? '<span class="people-av" style="background-image:url(' + esc(String(p.avatar_url).replace(/[()'"]/g, '')) + ')"></span>'
          : '<span class="people-av">' + esc(name.charAt(0).toUpperCase()) + '</span>';
        var inner = av + '<span class="people-name' + (p.display_name ? '' : ' none') + '">' + esc(name) + '</span>';
        return '<li>' + (p.user_id
          ? '<a class="people-who" href="/profile?u=' + encodeURIComponent(p.user_id) + '">' + inner + '</a>'
          : '<span class="people-who">' + inner + '</span>') + '</li>';
      }).join('');
    });
  }
  document.addEventListener('click', function (e) {
    var cnt = e.target.closest && e.target.closest('.pl-count');
    var b = !cnt && e.target.closest && e.target.closest('.photo-like');
    if (!cnt && !b) return;
    e.preventDefault();
    e.stopPropagation();
    var id = (cnt || b).getAttribute('data-photo');
    var ask = function () { if (window.atOpenSignIn) window.atOpenSignIn(); };
    var C = window.atCollection;
    if (!C || !C.gate) { ask(); return; }
    if (cnt) { C.gate(function (s) { openLikers(id, s); }, ask); return; }
    C.gate(function (s) {
      var was = state[id] || { n: 0, mine: false };
      var give = !was.mine;
      state[id] = { n: Math.max(0, was.n + (give ? 1 : -1)), mine: give };
      show(id);
      // A write the server refuses puts the heart back (People.swift's rule
      // for Follow: the button never lies about what is stored).
      write(id, give, s).then(function (ok) { if (!ok) { state[id] = was; show(id); } });
    }, ask);
  }, true);
  // DOUBLE TAP A PHOTOGRAPH FOR A HEART (Hidde, 2026-11-22, "2 sounds good";
  // Instagram; the apps' DoubleTapHeart): on a visitor's photo in a feed, the
  // first click waits a quarter second for a second one, then opens as it did;
  // a second click gives a heart (never takes one back) and a white heart pops
  // over the photo. Signed out it asks. A click with a modifier key opens at once.
  var dblWait = null;
  function burst(ph) {
    var b = document.createElement('span');
    b.className = 'dbl-burst';
    b.innerHTML = ON;
    ph.appendChild(b);
    setTimeout(function () { if (b.parentNode) b.parentNode.removeChild(b); }, 900);
  }
  document.addEventListener('click', function (e) {
    var ph = e.target.closest && e.target.closest('[data-dbl-heart]');
    if (!ph || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
    var a = ph.closest('a');
    e.preventDefault();
    if (dblWait && dblWait.ph === ph) {
      clearTimeout(dblWait.t); dblWait = null;
      var id = ph.getAttribute('data-dbl-heart');
      var ask = function () { if (window.atOpenSignIn) window.atOpenSignIn(); };
      var C = window.atCollection;
      if (!C || !C.gate) { ask(); return; }
      C.gate(function (s) {
        burst(ph);
        var was = state[id] || { n: 0, mine: false };
        if (was.mine) return;
        state[id] = { n: was.n + 1, mine: true };
        show(id);
        write(id, true, s).then(function (ok) { if (!ok) { state[id] = was; show(id); } });
      }, ask);
      return;
    }
    if (dblWait) clearTimeout(dblWait.t);
    dblWait = { ph: ph, t: setTimeout(function () { dblWait = null; if (a && a.href) location.href = a.href; }, 250) };
  });
  window.atPhotoLikes = { load: load };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', load); else load();
})();
</script>`;
}
