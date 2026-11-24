// ONE ACTIVITY ROW, for the /activity page (ActivityPage.astro) and the bell's
// dropdown in the bar (Base.astro), so the two cannot drift (2026-11-22, Hidde:
// "oke laten we a doen", the Strava and Instagram bell that drops down a short
// list with See all). Instagram's Activity row: faces, the words with the names
// bold, the time, the photograph at the end; New above Earlier.
//
// The string defines, inside whatever script includes it:
//   atActRows(rows, cards, W) -> HTML for the <li> rows, with the New and
//   Earlier headings; W is { one, two, more, fresh, earlier, empty, anon }.
// It needs AGO_FN (lib/time-ago-js.ts) in the same script for atAgo().
import { ui } from "./i18n";

export function activityWords(lang: string) {
  const u = ui(lang);
  return {
    one: u.activityOne, two: u.activityTwo, more: u.activityMore,
    fresh: u.activityNew, earlier: u.activityEarlier, empty: u.activityEmpty, anon: u.noteVisitor,
    follow: u.activityFollow, back: u.activityFollowBack, following: u.activityFollowing,
  };
}

/** THE BELL'S DROPDOWN (Base.astro, 2026-11-22, Hidde: "oke laten we a doen"):
 *  a click on the bell beside your face opens a short list under it, the six
 *  newest, with See all to /activity; a click outside or Escape closes it;
 *  opening it marks Activity seen, so the dot goes on every device. Strava's,
 *  Facebook's and Instagram's (2016) web bell. Without script the bell is a
 *  plain link to /activity. */
export function bellDropJs(lang: string, sb: string, key: string, agoFn: string): string {
  const W = activityWords(lang);
  return `<script>
(function () {
  ${agoFn}
  ${ACTIVITY_ROWS_FN}
  var SB = ${JSON.stringify(sb)}, KEY = ${JSON.stringify(key)}, W = ${JSON.stringify(W)};
  var bell = document.getElementById('bar-bell'), drop = document.getElementById('bell-drop');
  if (!bell || !drop) return;
  var list = drop.querySelector('.act-list'), cards = null;
  atActFollowBind(drop, SB, KEY);
  function close() { drop.hidden = true; bell.setAttribute('aria-expanded', 'false'); }
  function open(s) {
    drop.hidden = false; bell.setAttribute('aria-expanded', 'true');
    list.innerHTML = '<li class="act-wait"><span class="vp-spin" role="status"></span></li>';
    var h = { 'apikey': KEY, 'Authorization': 'Bearer ' + s.access_token, 'Content-Type': 'application/json' };
    var rows = fetch(SB + '/rest/v1/rpc/my_activity', { method: 'POST', headers: h, body: '{"n":6}' })
      .then(function (r) { return r.ok ? r.json() : []; }).catch(function () { return []; });
    var cs = cards ? Promise.resolve(cards) : fetch('/api/visitor-cards.json')
      .then(function (r) { return r.ok ? r.json() : {}; }).catch(function () { return {}; });
    Promise.all([rows, cs]).then(function (v) {
      cards = v[1];
      list.innerHTML = atActRows(v[0] || [], cards, W);
      fetch(SB + '/rest/v1/rpc/activity_seen', { method: 'POST', headers: h, body: '{}' }).then(function () {
        document.querySelectorAll('header.bar .bell-dot').forEach(function (d) { d.hidden = true; });
      }).catch(function () {});
    });
  }
  bell.addEventListener('click', function (e) {
    e.preventDefault();
    if (!drop.hidden) { close(); return; }
    var C = window.atCollection;
    if (C && C.gate) C.gate(open, function () { location.href = bell.getAttribute('href'); });
    else location.href = bell.getAttribute('href');
  });
  document.addEventListener('click', function (e) {
    if (!drop.hidden && !drop.contains(e.target) && !bell.contains(e.target)) close();
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !drop.hidden) { close(); bell.focus(); } });
})();
</script>`;
}

export const ACTIVITY_ROWS_FN = `
  function atActRows(rows, cards, W) {
    function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return '&#' + c.charCodeAt(0) + ';'; }); }
    function line(r, tree) {
      var names = r.names || [], n = Number(r.hearts) || 0;
      var a = '<b>' + esc(names[0] || W.anon) + '</b>';
      var t = '<b>' + esc(tree) + '</b>';
      if (n <= 1) return W.one.replace('{a}', a).replace('{t}', t);
      if (n === 2 && names[1]) return W.two.replace('{a}', a).replace('{b}', '<b>' + esc(names[1]) + '</b>').replace('{t}', t);
      return W.more.replace('{a}', a).replace('{n}', '<b>' + (n - 1) + '</b>').replace('{t}', t);
    }
    function faces(r) {
      var names = r.names || [], avs = r.avatars || [], out = '';
      for (var i = 0; i < Math.max(1, Math.min(2, names.length)); i++) {
        var nm = names[i] || W.anon, av = avs[i];
        out += av && /^https:/.test(av)
          ? '<span class="act-face" style="background-image:url(' + esc(av.replace(/[()'"]/g, '')) + ')"></span>'
          : '<span class="act-face">' + esc(nm.charAt(0).toUpperCase()) + '</span>';
      }
      return out;
    }
    // A NEW FOLLOWER (Hidde, 2026-11-24, "Ja, bouw het"; Instagram's Activity
    // row: their face, "X started following you.", Follow back or Following at
    // the end). The face and name open their profile; the pill follows back.
    function followRow(r) {
      var names = r.names || [], id = String(r.user_id || '');
      var a = '<b>' + esc(names[0] || W.anon) + '</b>';
      var on = !!r.following;
      return '<li class="act-li-follow"><a class="act-row act-follow' + (r.is_new ? ' is-new' : '') + '" href="/profile?u=' + encodeURIComponent(id) + '">'
        + '<span class="act-faces is-one">' + faces(r) + '</span>'
        + '<span class="act-text">' + W.follow.replace('{a}', a) + ' <span class="act-when">' + esc(atAgo(r.latest_at, false)) + '</span></span>'
        + '</a><button type="button" class="act-pill' + (on ? ' on' : '') + '" data-id="' + esc(id) + '" data-back="' + esc(W.back) + '" data-following="' + esc(W.following) + '" aria-pressed="' + (on ? 'true' : 'false') + '">'
        + esc(on ? W.following : W.back) + '</button></li>';
    }
    function row(r) {
      if (r.kind === 'follow') return followRow(r);
      var c = cards[r.tree_id] || null;
      var img = c ? (c.s[String(r.photo_id).toLowerCase()] || c.p) : '';
      return '<li><a class="act-row' + (r.is_new ? ' is-new' : '') + '" href="' + esc(c ? c.u : '#') + '">'
        + '<span class="act-faces">' + faces(r) + '</span>'
        + '<span class="act-text">' + line(r, c ? c.n : '') + ' <span class="act-when">' + esc(atAgo(r.latest_at, false)) + '</span></span>'
        + (img ? '<img class="act-ph" src="' + esc(img) + '" alt="" loading="lazy">' : '')
        + '</a></li>';
    }
    var fresh = rows.filter(function (r) { return r.is_new; });
    var old = rows.filter(function (r) { return !r.is_new; });
    var html = '';
    if (fresh.length) html += '<li class="act-day">' + esc(W.fresh) + '</li>' + fresh.map(row).join('');
    if (old.length) html += '<li class="act-day">' + esc(W.earlier) + '</li>' + old.map(row).join('');
    return html || '<li class="act-empty">' + esc(W.empty) + '</li>';
  }
  // Follow back and Following on a follower's row, the people sheet's write
  // (people-js.ts): the pill moves at once, and goes back if the account
  // refuses. Bound once on the list's container; rows are repainted freely.
  function atActFollowBind(root, SB, KEY) {
    root.addEventListener('click', function (e) {
      var b = e.target.closest && e.target.closest('.act-pill');
      if (!b) return;
      e.preventDefault();
      var C = window.atCollection, id = b.getAttribute('data-id');
      if (!C || !C.gate || !id) return;
      C.gate(function (s) {
        var me = s.user && s.user.id;
        if (!me) return;
        var on = b.classList.contains('on');
        var h = { 'apikey': KEY, 'Authorization': 'Bearer ' + s.access_token, 'Content-Type': 'application/json', 'Prefer': 'return=minimal' };
        function set(v) {
          b.classList.toggle('on', v); b.setAttribute('aria-pressed', v ? 'true' : 'false');
          b.textContent = b.getAttribute(v ? 'data-following' : 'data-back');
        }
        set(!on); b.disabled = true;
        var req = on
          ? fetch(SB + '/rest/v1/follows?follower=eq.' + me + '&followee=eq.' + id, { method: 'DELETE', headers: h })
          : fetch(SB + '/rest/v1/follows', { method: 'POST', headers: h, body: JSON.stringify({ follower: me, followee: id }) });
        req.then(function (r) { b.disabled = false; if (!r.ok) set(on); })
          .catch(function () { b.disabled = false; set(on); });
      }, function () { if (window.atOpenSignIn) window.atOpenSignIn(); });
    });
  }
`;
