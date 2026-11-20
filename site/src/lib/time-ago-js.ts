// WHEN A VISITOR'S PHOTOGRAPH WAS SENT, in the visitor's own language (Hidde,
// 2026-11-20: "aangeven hoelaat iets is gepost, om het platform meer actueel
// te maken"; CONVENTIONS.md "A heart for a visitor's photograph ... who and
// when on it").
//
// Short on a tile ("2h", "3d", Instagram's way), written out under the hero
// and in the opened photograph ("2 hours ago"), and month and year after four
// weeks ("Oct 2026"), the way Google Maps dates a photograph. The browser's
// own Intl does the words, so all eight languages come for free and nothing is
// typed into a component. The time is the server's published_at (when it was
// sent, never when it was taken); without one the line simply has no time.
export const AGO_FN = `
  function atAgo(iso, long) {
    var t = Date.parse(iso || '');
    if (!t) return '';
    var lang = document.documentElement.lang || 'en';
    var s = Math.max(0, (Date.now() - t) / 1000);
    try {
      if (s >= 28 * 86400) return new Date(t).toLocaleDateString(lang, { month: 'short', year: 'numeric' });
      var u = s < 3600 ? ['minute', Math.max(1, Math.floor(s / 60))]
        : s < 86400 ? ['hour', Math.floor(s / 3600)]
        : s < 7 * 86400 ? ['day', Math.floor(s / 86400)]
        : ['week', Math.floor(s / (7 * 86400))];
      if (long) return new Intl.RelativeTimeFormat(lang, { numeric: 'always' }).format(-u[1], u[0]);
      return new Intl.NumberFormat(lang, { style: 'unit', unit: u[0], unitDisplay: 'narrow' }).format(u[1]);
    } catch (e) { return ''; }
  }`;
