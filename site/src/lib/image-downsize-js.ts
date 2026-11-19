// Turning a phone's photograph into something we can send, once.
//
// Extracted from account/settings.astro on 2026-09-23, when a second place
// needed it: a reader adding a photograph of a tree. A second copy of this
// would have drifted inside a fortnight, and the corpus has the scar to prove
// it (a Wikimedia bucket table hand-ported into Swift, asking for a width the
// server does not serve).
//
// UPRIGHT, asked for rather than hoped for. A phone writes the orientation in
// an EXIF tag and leaves the pixels sideways, which is the same trap
// sightings_publish.py rotates out of reader photographs on the other end.
// createImageBitmap is told to apply it; the <img> fallback exists only for a
// browser with no createImageBitmap at all.
//
// The re-encode drops every other EXIF tag with it, including where the
// photograph was taken. That is a real loss and it is the right trade here:
// stripping a stranger's location out of a file they hand us is what a site
// should do by default, and the one place a geotag would have been useful,
// deciding which of two trunks a picture shows, is answered by which page the
// person was standing on when they pressed the button.
export const DOWNSIZE_JS = `
<script>
window.atDownsize = function(file, maxEdge, done) {
  function draw(src, w, h, release) {
    var side = Math.max(w, h), scale = side > maxEdge ? maxEdge / side : 1;
    var c = document.createElement("canvas");
    c.width = Math.round(w * scale);
    c.height = Math.round(h * scale);
    c.getContext("2d").drawImage(src, 0, 0, c.width, c.height);
    if (release) release();
    c.toBlob(function(b) { done(b); }, "image/jpeg", 0.8);
  }
  if (window.createImageBitmap) {
    createImageBitmap(file, { imageOrientation: "from-image" })
      .then(function(bm) { draw(bm, bm.width, bm.height, function() { bm.close(); }); })
      .catch(function() { done(null); });
    return;
  }
  var img = new Image(), url = URL.createObjectURL(file);
  img.onload = function() {
    draw(img, img.naturalWidth, img.naturalHeight, function() { URL.revokeObjectURL(url); });
  };
  img.onerror = function() { URL.revokeObjectURL(url); done(null); };
  img.src = url;
};
// THE DAY IT WAS TAKEN, read before the re-encode above throws the EXIF away
// (Hidde, 2026-11-19: "het gat dat de tijd niet wordt opgeslagen van input").
// The apps send the photograph's own date; the website sent none, so a summer
// picture uploaded in November was filed under autumn on the tree page. Only
// DateTimeOriginal (or the camera's DateTime) is read, never the GPS block,
// and a file without one gives null: the server then keeps the upload moment
// and the row's note says so. done(iso or null), never throws.
window.atPhotoDate = function(file, done) {
  function fin(v) { try { done(v); } catch (e) {} }
  if (!file || !file.slice || !window.DataView) return fin(null);
  var reader = new FileReader();
  reader.onerror = function() { fin(null); };
  reader.onload = function() {
    try {
      var v = new DataView(reader.result), n = v.byteLength, o = 2;
      if (n < 4 || v.getUint16(0) !== 0xFFD8) return fin(null);
      while (o + 4 < n) {
        var mark = v.getUint16(o), size = v.getUint16(o + 2);
        if (mark === 0xFFE1 && v.getUint32(o + 4) === 0x45786966) {
          var t = o + 10, le = v.getUint16(t) === 0x4949;
          var u16 = function(p) { return v.getUint16(p, le); };
          var u32 = function(p) { return v.getUint32(p, le); };
          var text = function(p) { var s = ''; for (var k = 0; k < 19 && p + k < n; k++) s += String.fromCharCode(v.getUint8(p + k)); return s; };
          var scan = function(ifd, want) {
            var found = {}, c = u16(ifd);
            for (var i = 0; i < c; i++) {
              var e = ifd + 2 + i * 12, tag = u16(e);
              if (want.indexOf(tag) >= 0) found[tag] = u32(e + 8);
            }
            return found;
          };
          var top = scan(t + u32(t + 4), [0x8769, 0x0132]);
          var raw = null;
          if (top[0x8769]) { var ex = scan(t + top[0x8769], [0x9003]); if (ex[0x9003]) raw = text(t + ex[0x9003]); }
          if (!raw && top[0x0132]) raw = text(t + top[0x0132]);
          var m = raw && raw.match(/^(\\d{4}):(\\d{2}):(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2})/);
          if (!m) return fin(null);
          var y = +m[1], mo = +m[2];
          if (y < 1990 || mo < 1 || mo > 12) return fin(null);
          var iso = m[1] + '-' + m[2] + '-' + m[3] + 'T' + m[4] + ':' + m[5] + ':' + m[6];
          if (Date.parse(iso) > Date.now() + 86400000) return fin(null);
          return fin(iso);
        }
        if ((mark & 0xFF00) !== 0xFF00 || mark === 0xFFDA) break;
        o += 2 + size;
      }
      fin(null);
    } catch (e) { fin(null); }
  };
  reader.readAsArrayBuffer(file.slice(0, 262144));
};
</script>
`;
