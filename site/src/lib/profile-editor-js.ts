// The script behind components/ProfileEditor.astro: your picture, name and
// country, in the one sheet, on whichever page opens it (/account from your
// photo, name or flag; Settings from your card). Lifted out of
// account/settings.astro on 2026-11-22 (Hidde: "dat je op je profielfoto of
// naam kan klikken, of de vlag"), unchanged in what it does, so the app's
// ProfileEditor.swift and this stay one decision: the same upsert, the same
// 512-pixel JPEG, the same country write.
//
// Needs COUNTRY_JS (window.atSettleCountry) and DOWNSIZE_JS (window.atDownsize)
// on the page. window.atProfileEditor.open(msg?) opens it, msg shown under
// Save; a save fires "at-profile" on document with { name, avatar, country }.
import { SUPABASE_URL, SUPABASE_KEY } from "./site-config";

export const PROFILE_EDITOR_JS = `
<script>
(function() {
  var SB = '${SUPABASE_URL}', KEY = '${SUPABASE_KEY}';
  var sheet = document.getElementById('me-sheet');
  if (!sheet) return;
  function el(id) { return document.getElementById(id); }
  function session() {
    try {
      var s = JSON.parse(localStorage.getItem('ancienttrees_session'));
      return (s && s.access_token && s.expires_at > Date.now() / 1000) ? s : null;
    } catch (e) { return null; }
  }

  var myId = null, myAvatar = null, myCountry = '', myHidden = false, picked = null;
  var picBtn = el('pic-pick'), picFile = el('in-pic'), picPrev = el('pic-preview');
  var nameBtn = el('save-name'), nameBox = el('in-name'), countryBox = el('in-country');

  function initial(name) {
    if (!picPrev.style.backgroundImage) picPrev.textContent = (name || '?').charAt(0).toUpperCase();
  }
  function showPicture(url) {
    picPrev.textContent = '';
    picPrev.style.backgroundImage = 'url(' + String(url).replace(/[()'"]/g, '') + ')';
    picBtn.textContent = 'Change photo';
  }
  function say(msg) { var n = el('name-status'); n.textContent = msg; n.hidden = false; }
  function quiet() { var n = el('name-status'); n.textContent = ''; n.hidden = true; }

  // What the account already holds, read once when a page with the sheet
  // loads signed in, so the sheet opens filled rather than empty: an empty box
  // on a page that knows the answer reads as data lost.
  // Read at load and again on open while it has not landed: a sign-in being
  // renewed as the page loads (signin-js atRefreshing) left the first open
  // empty (seen live 2026-11-22).
  var loading = false;
  function load() {
    var s = session();
    if (!s || loading || myId) return;
    loading = true;
    fetch(SB + '/auth/v1/user', { headers: { 'apikey': KEY, 'Authorization': 'Bearer ' + s.access_token } })
      .then(function(r) { return r.ok ? r.json() : null; })
      .then(function(u) {
        if (!u || !u.id) return;
        myId = u.id;
        if (u.email) initial(u.email);
        fetch(SB + '/rest/v1/profiles?select=display_name,avatar_url&user_id=eq.' + encodeURIComponent(u.id),
              { headers: { 'apikey': KEY, 'Authorization': 'Bearer ' + s.access_token } })
          .then(function(r) { return r.ok ? r.json() : null; })
          .then(function(rows) {
            var p = rows && rows[0];
            if (!p) return;
            if (p.display_name) { nameBox.value = p.display_name; nameBtn.disabled = false; initial(p.display_name); }
            if (p.avatar_url) { myAvatar = p.avatar_url; showPicture(myAvatar); }
          }).catch(function() {});
        if (window.atSettleCountry) window.atSettleCountry(SB, KEY, s.access_token, u.id)
          .then(function(c) {
            myCountry = c.country; myHidden = c.hidden;
            countryBox.value = c.country || (c.hidden ? '' : c.guess);
          }).catch(function() {});
      }).catch(function() {}).then(function() { loading = false; });
  }
  load();
  window.addEventListener('load', function() {
    if (window.atRefreshing) Promise.resolve(window.atRefreshing).catch(function() {}).then(load);
  });

  window.atProfileEditor = {
    open: function(msg) {
      load();
      if (msg) say(msg); else quiet();
      if (sheet.showModal && !sheet.open) sheet.showModal();
    }
  };

  // Nothing is uploaded on picking: the app's editor stages the picture and
  // sends it on Save, so somebody who changes their mind simply leaves.
  picBtn.addEventListener('click', function() { picFile.click(); });
  picFile.addEventListener('change', function() {
    var f = picFile.files && picFile.files[0];
    if (!f) return;
    window.atDownsize(f, 512, function(blob) {
      if (!blob) { say('That picture could not be read. Try another one.'); return; }
      picked = blob;
      showPicture(URL.createObjectURL(blob));
      say('Press Save to keep it.');
    });
  });

  // The upload runs before the row is written, so a failed picture never
  // leaves a url in the database pointing at nothing (supabase/profiles.sql:
  // avatars/<user-id>/avatar.jpg with x-upsert, one file per person).
  function sendPicture(token, cb) {
    if (!picked) { cb(true, myAvatar); return; }
    fetch(SB + '/storage/v1/object/avatars/' + encodeURIComponent(myId) + '/avatar.jpg', {
      method: 'POST',
      headers: { 'apikey': KEY, 'Authorization': 'Bearer ' + token,
                 'Content-Type': 'image/jpeg', 'x-upsert': 'true' },
      body: picked
    }).then(function(r) {
      cb(r.ok, r.ok ? SB + '/storage/v1/object/public/avatars/' + encodeURIComponent(myId) + '/avatar.jpg' : null);
    }).catch(function() { cb(false, null); });
  }

  // Save is dead while the box is empty, as the app's editor is.
  nameBtn.disabled = true;
  nameBox.addEventListener('input', function() { nameBtn.disabled = nameBox.value.trim().length < 1; });

  // ONE SAVE for picture, name and country, the app's editor's one button.
  // The same upsert the app makes (profiles?on_conflict=user_id, merge).
  nameBtn.addEventListener('click', function() {
    var v = nameBox.value.trim();
    var cur = session();
    if (!cur || !myId) { say('That did not save. Your sign-in has expired.'); return; }
    if (v.length < 1) return;
    nameBtn.disabled = true;
    say('Saving.');
    function put(row) {
      return fetch(SB + '/rest/v1/profiles?on_conflict=user_id', {
        method: 'POST',
        headers: { 'apikey': KEY, 'Authorization': 'Bearer ' + cur.access_token,
                   'Content-Type': 'application/json', 'Prefer': 'resolution=merge-duplicates' },
        body: JSON.stringify([row])
      });
    }
    sendPicture(cur.access_token, function(ok, url) {
      if (!ok) { nameBtn.disabled = false; say('That did not save. The picture would not upload.'); return; }
      // avatar_url only travels when we KNOW one: a null we merely failed to
      // read would take somebody's picture off on a save about a name.
      var row = { user_id: myId, display_name: v };
      if (url) row.avatar_url = url;
      put(row).then(function(r) {
        if (!r.ok) { nameBtn.disabled = false; say('That did not save. Try again in a moment.'); return; }
        if (url) { myAvatar = url; picked = null; }
        var want = countryBox.value;
        var done = function(ok2) {
          nameBtn.disabled = false;
          say(ok2 ? 'Saved.' : 'That did not save. Your country would not save.');
          if (ok2) { myCountry = want; myHidden = !want; }
          document.dispatchEvent(new CustomEvent('at-profile', { detail: {
            name: v, avatar: myAvatar, country: ok2 ? (want || '') : myCountry } }));
          if (ok2) setTimeout(function() { if (sheet.open) sheet.close(); }, 700);
        };
        // The country on its own write, like the app's saveCountry, only when
        // it changed. "Don't show" stores flag_hidden; a database without that
        // column yet takes the country alone.
        if (want === myCountry && (want || myHidden)) { done(true); return; }
        put({ user_id: myId, country: want || null, flag_hidden: !want })
          .then(function(r2) { return r2.ok ? r2 : put({ user_id: myId, country: want || null }); })
          .then(function(r3) { done(r3.ok); }).catch(function() { done(false); });
      }).catch(function() { nameBtn.disabled = false; say('That did not save. Try again in a moment.'); });
    });
  });
})();
</script>
`;
