// "DID YOU MEAN ...?" UNDER THE EMAIL FIELD (Hidde, 2026-11-16: "can we give a
// warning before sending", then "check conventions how to tackle this more
// thoroughly"; CONVENTIONS.md "A mistyped email address").
//
// The Guardian weekend's sign-up mails bounced on addresses like
// outlook.co for outlook.com: the person typed the provider one letter wrong,
// waited for a mail that could never come, and only some signed up again. The
// convention is mailcheck.js's, used on sign-up forms for a decade: when the
// part after the @ is one or two letters off a provider people actually use,
// a line under the field offers the corrected address, and a tap puts it in.
//
// It never refuses an address. The first Send with a suggestion showing holds
// the send once so the line is seen (on a phone, tapping Send is what blurs the
// field, so a hint shown only on blur would flash and be gone with the sheet);
// the second Send goes out exactly as typed. A typo before the @ no list can
// catch; the "check your inbox" step shows the whole address with "Use a
// different address" beside it for that.
//
// One list, data/email-domains.json, read here at build time and copied into
// the iPhone and Android apps (qa's check_one_email_domain_list()). The rule
// is the same on all three: unknown domain, the nearest listed one by edit
// distance, at most 2 apart (1 for a domain of six letters or fewer), and only
// when that nearest one is the only one that near.
import fs from "node:fs";
import path from "node:path";
import { DATA } from "./data-dir";

const DOMAINS: string[] = JSON.parse(
  fs.readFileSync(path.join(DATA, "email-domains.json"), "utf-8"),
).domains;

export const EMAIL_SUGGEST_JS = `
<script>
(function() {
  var D = ${JSON.stringify(DOMAINS)};
  function dist(a, b) {
    var m = a.length, n = b.length, prev = [], cur, i, j;
    for (j = 0; j <= n; j++) prev[j] = j;
    for (i = 1; i <= m; i++) {
      cur = [i];
      for (j = 1; j <= n; j++) {
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a.charAt(i - 1) === b.charAt(j - 1) ? 0 : 1));
      }
      prev = cur;
    }
    return prev[n];
  }
  // The corrected address, or null.
  window.atEmailSuggest = function(addr) {
    addr = (addr || '').trim();
    var at = addr.lastIndexOf('@');
    if (at < 1 || at === addr.length - 1) return null;
    var local = addr.slice(0, at), dom = addr.slice(at + 1).toLowerCase();
    if (D.indexOf(dom) > -1) return null;
    var best = null, bestD = 99, tie = false;
    for (var k = 0; k < D.length; k++) {
      var d = dist(dom, D[k]);
      if (d < bestD) { bestD = d; best = D[k]; tie = false; }
      else if (d === bestD) { tie = true; }
    }
    var limit = dom.length <= 6 ? 1 : 2;
    if (!best || tie || bestD > limit) return null;
    return local + '@' + best;
  };
  // Wire one form: <prefix>-email, <prefix>-suggest (its data-tpl holds
  // "Did you mean %s?" in the page's language). Returns hold(): true when the
  // send should wait because a suggestion was just shown for this exact value.
  window.atWireEmailSuggest = function(prefix) {
    var input = document.getElementById(prefix + '-email');
    var box = document.getElementById(prefix + '-suggest');
    if (!input || !box) return function() { return false; };
    var shownFor = null;
    function show() {
      var s = window.atEmailSuggest(input.value);
      if (!s) { box.hidden = true; box.textContent = ''; return false; }
      var parts = (box.getAttribute('data-tpl') || 'Did you mean %s?').split('%s');
      box.textContent = '';
      box.appendChild(document.createTextNode(parts[0]));
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'signin-suggest-pick';
      b.textContent = s;
      b.addEventListener('click', function() {
        input.value = s;
        // A refusal from the server ("That address can't receive mail") was
        // about the address just replaced.
        input.setCustomValidity('');
        box.hidden = true;
        shownFor = null;
        try { at.track('email-suggest-taken'); } catch (e) {}
        input.focus();
      });
      // The address and what follows it ("?") stay on one line together.
      var glue = document.createElement('span');
      glue.className = 'signin-suggest-glue';
      glue.appendChild(b);
      glue.appendChild(document.createTextNode(parts[1] || ''));
      box.appendChild(glue);
      box.hidden = false;
      return true;
    }
    // Shown on blur, but only a Send counts as having seen it: on a phone the
    // tap on Send is itself the blur, so the hint and the send arrive together.
    input.addEventListener('blur', show);
    input.addEventListener('input', function() { if (!box.hidden && !window.atEmailSuggest(input.value)) box.hidden = true; });
    return function hold() {
      var v = input.value.trim();
      if (!window.atEmailSuggest(v)) { box.hidden = true; return false; }
      if (shownFor === v) return false; // held once already: send as typed
      show();
      shownFor = v;
      return true;
    };
  };
})();
</script>
`;
