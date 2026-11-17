// WHO WROTE THE NOTE, WHO TOOK THE PHOTOGRAPH, ON THE TREE PAGE (Hidde,
// 2026-11-17: "bij foto's wel namen gaan noemen van degene die het heeft
// opgeloot. Als die een account hebben, dan worden die accounts ook
// klikbaar"). The rule of the home page's New from visitors row
// (visitors-row-js.ts), now under a note and under a reader's photograph:
//
// * The server says whose it is (supabase/reader-names.sql): a name and
//   picture only from a public profile, the account id only to a signed-in
//   caller. Private: no name under a photograph, "A visitor" under a note.
// * A name with an id is a link to /profile?u=<id>. Without one (signed out)
//   it is a button: the one door (atCollection.gate) asks the server again
//   with the session it accepts, else opens the sign-in sheet, which keeps
//   which name was tapped so the sign-in ends on that profile
//   (signin-js 'visitor', atGoVisitor below).
//
// THE BUG THIS REPLACES (2026-11-17, the Arbour Oak of Wollaton Park): the
// notes section carried its "Sign in first" sentence as data-signin, the
// attribute signin-js reads as "this opens the sign-in sheet", so every tap
// anywhere in the notes, a name included, opened sign-in, signed in or not.
// qa's check_data_signin_only_on_controls() keeps that attribute on links
// and buttons.
import { SUPABASE_URL, SUPABASE_KEY } from "./site-config";

export const READER_NAMES_JS = `
<script>
(function() {
  var SB = "${SUPABASE_URL}", KEY = "${SUPABASE_KEY}";
  function rpc(fn, body, token) {
    return fetch(SB + '/rest/v1/rpc/' + fn, {
      method: 'POST',
      headers: { 'apikey': KEY, 'Authorization': 'Bearer ' + (token || KEY), 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    }).then(function(r) { return r.ok ? r.json() : []; }).catch(function() { return []; });
  }
  function treeId() {
    var s = document.getElementById('td-notes');
    return s ? s.getAttribute('data-tree') : null;
  }
  // The account behind a tapped name, asked with a session the server took.
  // n:<created_at> is a note on this tree, p:<photo id> a photograph.
  function resolve(key, token) {
    if (key.indexOf('n:') === 0) {
      var t = treeId();
      if (!t) return Promise.resolve(null);
      return rpc('tree_notes_for', { ids: [t] }, token).then(function(rows) {
        var hit = (rows || []).filter(function(r) { return r.created_at === key.slice(2); })[0];
        return hit && hit.author_id || null;
      });
    }
    if (key.indexOf('p:') === 0) {
      return rpc('photo_authors', { ids: [key.slice(2)] }, token).then(function(rows) {
        return rows && rows[0] && rows[0].author_id || null;
      });
    }
    return Promise.resolve(null);
  }
  function go(id) { if (id) location.href = '/profile?u=' + encodeURIComponent(id); }

  // A name as a control: a link when the server gave the account, else a
  // button that asks. inner is the face and name, already built.
  window.atNameLink = function(inner, authorId, key, cls) {
    var e;
    if (authorId) {
      e = document.createElement('a');
      e.href = '/profile?u=' + encodeURIComponent(authorId);
    } else {
      e = document.createElement('button');
      e.type = 'button';
      e.setAttribute('data-name-key', key);
    }
    e.className = (cls || '') + ' rn-link';
    e.appendChild(inner);
    return e;
  };

  document.addEventListener('click', function(ev) {
    var b = ev.target.closest && ev.target.closest('[data-name-key]');
    if (!b) return;
    ev.preventDefault();
    var key = b.getAttribute('data-name-key');
    var ask = function() {
      if (window.atOpenSignIn) window.atOpenSignIn(null, null, { kind: 'visitor', sighting: key });
    };
    var C = window.atCollection;
    if (!C || !C.gate) { ask(); return; }
    C.gate(function(s) { resolve(key, s.access_token).then(go); }, ask);
  });

  // After the sign-in a name asked for: signin-js hands the key over as
  // atPendingVisitor and calls this; the server, asked with the new session,
  // says whose it is.
  window.atGoVisitor = function() {
    var key = window.atPendingVisitor;
    var C = window.atCollection;
    if (!key || !C || !C.gate) return;
    window.atPendingVisitor = null;
    C.gate(function(s) { resolve(String(key), s.access_token).then(go); }, function() {});
  };

  // THE PHOTOGRAPHS. Every credit slot of a reader's photograph names its
  // photo id; one call fills them all. data-tpl is "Photo: {name}" in the
  // page's language.
  function paintPhotos(rows) {
    var by = {};
    (rows || []).forEach(function(r) { if (r && r.photo_id && r.author_name) by[r.photo_id] = r; });
    document.querySelectorAll('[data-photo-by]').forEach(function(slot) {
      var r = by[slot.getAttribute('data-photo-by')];
      if (!r) return;
      var tpl = slot.getAttribute('data-tpl') || '{name}';
      var parts = tpl.split('{name}');
      var name = document.createElement('span');
      name.className = 'rn-name';
      name.textContent = r.author_name;
      var link = window.atNameLink(name, r.author_id, 'p:' + r.photo_id, 'rn-photo');
      slot.textContent = '';
      if (parts[0]) slot.appendChild(document.createTextNode(parts[0]));
      slot.appendChild(link);
      if (parts[1]) slot.appendChild(document.createTextNode(parts[1]));
    });
  }
  function start() {
    if (window.atPendingVisitor) window.atGoVisitor();
    var ids = [];
    document.querySelectorAll('[data-photo-by]').forEach(function(s) {
      var id = s.getAttribute('data-photo-by');
      if (id && ids.indexOf(id) < 0) ids.push(id);
    });
    if (!ids.length) return;
    var C = window.atCollection;
    if (C && C.gate) {
      C.gate(function(s) { rpc('photo_authors', { ids: ids }, s.access_token).then(paintPhotos); },
             function() { rpc('photo_authors', { ids: ids }, null).then(paintPhotos); });
    } else {
      rpc('photo_authors', { ids: ids }, null).then(paintPhotos);
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
</script>
`;
