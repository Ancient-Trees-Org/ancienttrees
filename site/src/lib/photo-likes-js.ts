// THE HEART ON A VISITOR'S PHOTOGRAPH (Hidde, 2026-11-20: "dat gebruikers de
// fotos kunnen hartje geven om elkaar aan te moedigen voor de foto zelf", then
// "Ja, bouw het hartje"). Convention: CONVENTIONS.md "A heart for a visitor's
// photograph, beside save and Worth the visit; who and when on it": the
// bookmark saves the TREE in the photograph's corner, the thumb says the tree
// is worth the visit, and this heart thanks the PHOTOGRAPHER, at the end of
// their line (face, name, when). Strava's kudos and Instagram's like: the
// count is the button, one tap gives, a second takes it back. Google Maps'
// "Helpful": the count is public, who gave it is not (supabase/photo-likes.sql).
//
// One script for every place the byline stands (the home row, /visitors, the
// tree page under the hero and in the opened photograph). A slot is
// <span data-photo-like="<photo id>"></span>; this fills it with the button,
// asks the server for the counts of every slot on the page in one call, and
// keeps them in step. Signed out, a tap opens the sign-in sheet through the
// one door (atCollection.gate) and changes nothing. Nothing kept on the device.
import { SUPABASE_URL, SUPABASE_KEY } from "./site-config";
import { ui } from "./i18n";
import { icon } from "./icons";

const LANGS = ["en", "es", "it", "nl", "de", "pt", "fr", "ja"];

export function photoLikesJs(): string {
  const words: Record<string, [string, string]> = {};
  for (const l of LANGS) words[l] = [ui(l).photoLike, ui(l).photoLiked];
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
  function rpc(ids, token) {
    return fetch(SB + '/rest/v1/rpc/photo_like_counts', {
      method: 'POST',
      headers: { 'apikey': KEY, 'Authorization': 'Bearer ' + (token || KEY), 'Content-Type': 'application/json' },
      body: JSON.stringify({ ids: ids })
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
        b.innerHTML = OFF + ON + '<span class="pl-n"></span>';
        slot.appendChild(b);
      }
      b.setAttribute('aria-pressed', s.mine ? 'true' : 'false');
      b.setAttribute('aria-label', (s.mine ? W[1] : W[0]) + (s.n ? ', ' + s.n : ''));
      // From one, never a zero (Hidde, 2026-08-26: "pas van 1 tellen").
      b.querySelector('.pl-n').textContent = s.n ? String(s.n) : '';
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
      rpc(ids, token).then(function (rows) {
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
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('.photo-like');
    if (!b) return;
    e.preventDefault();
    e.stopPropagation();
    var id = b.getAttribute('data-photo');
    var ask = function () { if (window.atOpenSignIn) window.atOpenSignIn(); };
    var C = window.atCollection;
    if (!C || !C.gate) { ask(); return; }
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
  window.atPhotoLikes = { load: load };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', load); else load();
})();
</script>`;
}
