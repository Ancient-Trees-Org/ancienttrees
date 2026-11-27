// ONE MAP, NO RELOAD (Hidde, 2026-11-27: "ok bouw optie 2", after the fly and
// fade from London to Lisbon showed Lisbon twice: "very cringe"). Airbnb's
// map keeps standing when you search another city; its list and its address
// change without a page load. Ours does the same: a city picked in the search
// on any map flies there (fly-to-city-js.ts), then this fetches that city's
// page, swaps the page's part (the .split: sheet, filter row, map tools) and
// runs that page's own scripts, while the map you were looking at stays on
// top as a picture until the new one has drawn underneath it. The address
// becomes the city's own (/lisbon#map=...). Google never sees any of this:
// /lisbon is still the whole page from the server, and every link is still a
// link.
//
// What makes a page's scripts runnable twice: every listener a page script
// adds while it runs (the scripts slot, the page's own inline scripts and
// their DOMContentLoaded bodies) is written down here, and removed before the
// next page's scripts run, so the old page stops answering. The page scripts
// are each one closure (IIFEs and mapScript's DOMContentLoaded function), so
// running them again declares nothing twice. Back to an entry of an earlier
// page loads that page for real (history entries carry the page's number).
//
// Anything unexpected (another language, no map on either side, a failed
// fetch or an error while swapping) falls back to the ordinary load.
//
// Inline in Base.astro's head, before any page script, so the listener
// recorder is in place when they run.
export const SOFT_NAV_JS = `
(function() {
  if (!window.EventTarget || !window.history || !history.pushState || !window.fetch || !window.DOMParser) { return; }
  var P = { id: 0, rec: 0, ls: [], cache: {} };
  window.atPage = P;
  var add = EventTarget.prototype.addEventListener;
  EventTarget.prototype.addEventListener = function(t, f, o) {
    if (P.rec > 0 && f) {
      if (this === document && t === 'DOMContentLoaded') {
        var g = f;
        f = function(e) {
          P.rec++;
          try { return typeof g === 'function' ? g.call(document, e) : g.handleEvent(e); }
          finally { P.rec--; }
        };
        // A page swapped in after the document loaded runs its body now.
        if (document.readyState !== 'loading') { f(new Event('DOMContentLoaded')); return; }
      }
      P.ls.push([this, t, f, o]);
    }
    return add.call(this, t, f, o);
  };
  // Every history entry says which page made it.
  function tag(s) {
    if (s === null || s === undefined) { return { atPg: P.id }; }
    if (typeof s === 'object' && s.atPg === undefined) {
      var c = {};
      for (var k in s) { c[k] = s[k]; }
      c.atPg = P.id;
      return c;
    }
    return s;
  }
  var push = history.pushState, rep = history.replaceState;
  history.pushState = function(s, t, u) { return push.call(history, tag(s), t, u); };
  history.replaceState = function(s, t, u) { return rep.call(history, tag(s), t, u); };
  window.addEventListener('popstate', function(e) {
    var pg = e.state && e.state.atPg !== undefined ? e.state.atPg : 0;
    if (pg !== P.id) { location.reload(); }
  });

  P.prefetch = function(path) {
    if (!P.cache[path]) {
      P.cache[path] = fetch(path, { credentials: 'same-origin' }).then(function(r) {
        if (!r.ok) { throw new Error('status ' + r.status); }
        return r.text();
      });
      P.cache[path].catch(function() { delete P.cache[path]; });
    }
    return P.cache[path];
  };

  P.go = function(path, hash) {
    var url = path + (hash || '');
    function hard() { location.href = url; }
    P.prefetch(path).then(function(html) {
      delete P.cache[path];
      try { swap(html, url); } catch (e) { hard(); }
    }, hard);
  };

  function pageScripts(doc) {
    var out = [], on = false;
    Array.prototype.forEach.call(doc.querySelectorAll('script'), function(s) {
      var m = s.getAttribute('data-at-page');
      if (m === 'scripts-start') { on = true; return; }
      if (m === 'scripts-end') { on = false; return; }
      if (on) { out.push(s); }
    });
    return out;
  }
  function run(s) {
    var type = (s.getAttribute('type') || '').toLowerCase();
    if (type && type !== 'text/javascript' && type !== 'module') { return; }
    var src = s.getAttribute('src');
    if (src) {
      if (document.querySelector('script[src="' + src.replace(/"/g, '') + '"]')) { return; }
      var e = document.createElement('script');
      e.src = src; e.async = false;
      document.head.appendChild(e);
      return;
    }
    var n = document.createElement('script');
    n.text = s.text;
    document.body.appendChild(n);
    n.remove();
  }
  function setHead(doc) {
    document.title = doc.title;
    [['link[rel="canonical"]', 'href'], ['meta[name="description"]', 'content'],
     ['meta[property="og:title"]', 'content'], ['meta[property="og:url"]', 'content'],
     ['meta[property="og:description"]', 'content'], ['meta[property="og:image"]', 'content']].forEach(function(q) {
      var a = document.querySelector(q[0]), b = doc.querySelector(q[0]);
      if (a && b) { a.setAttribute(q[1], b.getAttribute(q[1]) || ''); }
    });
  }

  function swap(html, url) {
    var doc = new DOMParser().parseFromString(html, 'text/html');
    var nSplit = doc.querySelector('.split'), oSplit = document.querySelector('.split');
    var oMapEl = document.getElementById('map'), nMapEl = nSplit ? nSplit.querySelector('#map') : null;
    var scripts = pageScripts(doc);
    if (!nSplit || !oSplit || !oMapEl || !nMapEl || !scripts.length ||
        (doc.documentElement.lang || '') !== (document.documentElement.lang || '')) {
      throw new Error('not swappable');
    }
    // The old page stops answering.
    P.ls.forEach(function(l) { try { l[0].removeEventListener(l[1], l[2], l[3]); } catch (e) {} });
    P.ls = [];
    var oldMap = window.atMainMap || null;
    window.atMainMap = null;
    P.id++;
    history.pushState(null, '', url);
    setHead(doc);
    // The map you were looking at stays on top, as a picture, until the new
    // one has drawn underneath it.
    oMapEl.id = 'map-old';
    oMapEl.style.pointerEvents = 'none';
    nMapEl.parentNode.insertBefore(oMapEl, nMapEl.nextSibling);
    var root = document.documentElement;
    root.classList.remove('sheet-away');
    root.style.removeProperty('--map-pop-lift');
    var adopted = document.adoptNode(nSplit);
    oSplit.parentNode.replaceChild(adopted, oSplit);
    P.rec++;
    try {
      // The page part's own scripts (the ambassador and Plus rows), then the
      // page's scripts, in the order the page has them.
      Array.prototype.forEach.call(adopted.querySelectorAll('script'), function(s) { s.remove(); run(s); });
      scripts.forEach(run);
    } finally { P.rec--; }
    if (window.atPaintUnits) { try { window.atPaintUnits(); } catch (e) {} }
    var nm = window.atMainMap;
    var gone = false;
    function drop() {
      if (gone) { return; }
      gone = true;
      oMapEl.style.transition = 'opacity .2s';
      oMapEl.style.opacity = '0';
      setTimeout(function() {
        try { if (oldMap) { oldMap.remove(); } } catch (e) {}
        if (oMapEl.parentNode) { oMapEl.parentNode.removeChild(oMapEl); }
      }, 220);
    }
    if (nm && nm !== oldMap) {
      nm.once('idle', function() { setTimeout(drop, 120); });
      setTimeout(drop, 3500);
    } else { drop(); }
  }
})();
`;
