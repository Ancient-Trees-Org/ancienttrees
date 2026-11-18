#!/usr/bin/env python3
"""Do the photographs LOOK right on a real screen? Chrome opens the pages the
way a phone (3x screen) and a laptop (2x) do and measures every photograph it
shows.

Hidde, 2026-11-18, after the New from visitors row and a tree's strip looked
off: "can you make some sort of test for photo quality i have to find it out
always". The fault that day was a 1600 pixel original shrunk seven times into
a tile; in September it was a 960 pixel hero stretched over a phone, and
before that a 428 pixel Commons file blown up to full width. All three are
one measurement: how many of the file's pixels land on one pixel of the
screen. So for every photograph shown, at its real size on the page and the
screen's real density, after the browser picked from the srcset:

  SOFT   the file is stretched: one of its pixels covers more than SOFT_AT
         screen pixels across (blurry, the 428 px Roth-Linde, the 960 cap).
  HEAVY  the file is shrunk more than HEAVY_AT times (leaves shimmer, and a
         tile weighs what a hero should: the 2026-11-18 readers' photos).
         A photograph under 500 points that weighs over HEAVY_BYTES is only
         a note: slow, but not something anybody sees.
  BROKEN the file did not load.

A photograph only fails when it is above THUMB points wide (avatars and
icons are not photographs) and when it actually loaded. Lazy rows are
scrolled into view first, so the shelves and the strip are measured too.

The pages: home, New from visitors' See all page, a city, a country, the
cities index, and the tree pages of
the three newest photographs in New from visitors, taken from the home page
itself, so the check always looks at what readers sent last.

  python3 scripts/photocheck.py                 site/dist, served locally
  python3 scripts/photocheck.py --live          https://ancienttrees.app
  python3 scripts/photocheck.py --live --notes  also print the near misses

Exit 0 when every photograph passes, 1 when one does not, 2 when no browser
could start. Needs Playwright, as pagecheck.py does (pip install
playwright==1.60.0). Run by photos-live.yml every day into quality.py's Web
"Photos" light, so a soft or heavy photograph reaches the digest and the runs
before anybody sees it. Removing this check needs Hidde.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pagecheck import DIST, LIVE, launch, serve  # noqa: E402

# Real devices, not the 1x of a headless default: an iPhone is 3x, a laptop 2x.
SCREENS = [(390, 844, 3, "phone"), (1280, 800, 2, "desktop")]
PAGES = ["/", "/visitors", "/london", "/united-kingdom", "/cities"]
NEWEST_TREES = 3

SOFT_AT = 2.0        # one file pixel over more than 2 screen pixels: blurry
SOFT_NOTE = 1.6      # a near miss, printed with --notes
HEAVY_AT = 3.5       # a file over 3.5 times the screen pixels it fills
HEAVY_BYTES = 450_000
THUMB = 60           # points; anything narrower is an avatar or an icon

MEASURE = """async (dpr) => {
  // An <img> chosen from a srcset reports naturalWidth divided by the density
  // the browser assumed, not the file's pixels (a 500 file read as 175). So
  // each file is opened once more on its own and measured there.
  const real = {};
  const trueSize = async (src) => {
    if (!(src in real)) {
      real[src] = await new Promise((ok) => {
        const i = new Image();
        i.onload = () => ok([i.naturalWidth, i.naturalHeight]);
        i.onerror = () => ok([0, 0]);
        i.src = src;
      });
    }
    return real[src];
  };
  const out = [];
  for (const img of document.images) {
    const r = img.getBoundingClientRect();
    if (r.width < %d || r.height < 20) continue;
    const st = getComputedStyle(img);
    if (st.visibility === 'hidden' || st.display === 'none') continue;
    const src = img.currentSrc || img.src;
    if (!src || src.startsWith('data:')) continue;
    if (!img.complete) continue;
    if (!img.naturalWidth) { out.push({src, broken: true, w: r.width}); continue; }
    const [nw, nh] = await trueSize(src);
    if (!nw) { out.push({src, broken: true, w: r.width}); continue; }
    const fit = st.objectFit;
    // How many screen pixels one file pixel covers, across.
    const scale = (fit === 'cover' ? Math.max(r.width / nw, r.height / nh)
                 : fit === 'contain' ? Math.min(r.width / nw, r.height / nh)
                 : r.width / nw) * dpr;
    const e = performance.getEntriesByName(src)[0];
    out.push({src, nw, nh, w: Math.round(r.width), h: Math.round(r.height), scale,
              bytes: e ? (e.encodedBodySize || e.transferSize || 0) : 0});
  }
  return out;
}""" % THUMB

SCROLL = """async () => {
  const step = innerHeight * 0.8;
  for (let y = 0; y < document.body.scrollHeight; y += step) {
    scrollTo(0, y);
    // Lazy rows that slide sideways: bring every tile into view once.
    for (const row of document.querySelectorAll('.shelf-row, .photo-strip')) {
      const r = row.getBoundingClientRect();
      if (r.bottom > 0 && r.top < innerHeight) row.scrollLeft = row.scrollWidth;
    }
    await new Promise(r => setTimeout(r, 250));
  }
  for (const row of document.querySelectorAll('.shelf-row, .photo-strip')) row.scrollLeft = 0;
  scrollTo(0, 0);
}"""


def judge(m):
    if m.get("broken"):
        return "BROKEN", "did not load"
    s = m["scale"]
    if s > SOFT_AT:
        return "SOFT", "%dx%d file over %dx%d pt: each file pixel is %.1f screen pixels (stretched)" % (
            m["nw"], m["nh"], m["w"], m["h"], s)
    if s and 1 / s > HEAVY_AT:
        return "HEAVY", "%dx%d file over %dx%d pt: %.1f times more pixels across than the screen shows" % (
            m["nw"], m["nh"], m["w"], m["h"], 1 / s)
    # Weight alone looks fine and only slows the page (a Commons 960 card of
    # 600 KB, measured 2026-11-18), so it is a note, never the red light.
    if m["bytes"] > HEAVY_BYTES and m["w"] < 500:
        return "note", "%d KB for a photograph %d pt wide (slow, not blurry)" % (m["bytes"] // 1000, m["w"])
    if s > SOFT_NOTE:
        return "note", "%dx%d file over %dx%d pt: %.1f (near soft)" % (m["nw"], m["nh"], m["w"], m["h"], s)
    return None, ""


def measure(browser, base, path, screen):
    w, h, dpr, _ = screen
    ctx = browser.new_context(viewport={"width": w, "height": h}, device_scale_factor=dpr)
    page = ctx.new_page()
    try:
        page.goto(base + path, wait_until="load", timeout=45000)
        page.wait_for_timeout(2500)          # the visitors row comes from the server
        page.evaluate(SCROLL)
        page.wait_for_timeout(1500)
        page.evaluate(SCROLL)
        links = []
        if path == "/":
            links = page.eval_on_selector_all(
                "#nfv a.nfv-tree", "els => els.map(e => e.getAttribute('href'))")
        return page.evaluate(MEASURE, dpr), links
    finally:
        ctx.close()


def run(base, notes):
    from playwright.sync_api import sync_playwright
    fails, near, seen = [], [], set()
    with sync_playwright() as pw:
        try:
            browser = launch(pw)
        except Exception as e:
            print("photocheck: no browser could start (%s)" % str(e).splitlines()[0][:160])
            return 2
        pages = list(PAGES)
        counted = 0
        while pages:
            path = pages.pop(0)
            for screen in SCREENS:
                try:
                    found, links = measure(browser, base, path, screen)
                except Exception as e:
                    print("  skip  %-48s %-7s %s" % (path, screen[3], str(e).splitlines()[0][:100]))
                    continue
                for href in [l for l in links if l and l.startswith("/") and "#" not in l][:NEWEST_TREES]:
                    if href not in pages and href not in PAGES:
                        pages.append(href)
                bad = 0
                for m in found:
                    counted += 1
                    kind, why = judge(m)
                    if not kind:
                        continue
                    key = (kind, m["src"].split("?")[0], screen[3])
                    if key in seen:
                        continue
                    seen.add(key)
                    row = (path, screen[3], kind, m["src"].replace(base, ""), why)
                    if kind == "note":
                        near.append(row)
                    else:
                        fails.append(row)
                        bad += 1
                print("  %-5s %-48s %-7s %d photographs" % ("FAIL" if bad else "ok", path, screen[3], len(found)))
        browser.close()
    if notes and near:
        print("\nNear misses (stretched 1.6 to 2 times, or heavy in bytes only):")
        for path, scr, kind, src, why in near:
            print("  %-7s %s\n          %s\n          %s" % (scr, path, src, why))
    if fails:
        print("\nphotocheck: %d photograph(s) would look wrong on %s:" % (len(fails), base))
        for path, scr, kind, src, why in fails:
            print("  %-6s %-7s %s\n                 %s\n                 %s" % (kind, scr, path, src, why))
        return 1
    print("\nphotocheck: %d photographs measured, all sharp and right-sized on %s" % (counted, base))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--live", action="store_true", help="check %s" % LIVE)
    ap.add_argument("--base", help="check this origin instead of site/dist")
    ap.add_argument("--dist", default=str(DIST))
    ap.add_argument("--notes", action="store_true", help="also print near misses")
    a = ap.parse_args()
    if a.live or a.base:
        return run((a.base or LIVE).rstrip("/"), a.notes)
    dist = Path(a.dist)
    if not (dist / "index.html").exists():
        print("photocheck: no built site at %s (run astro build first)" % dist)
        return 1
    server, base = serve(dist)
    try:
        return run(base, a.notes)
    finally:
        server.shutdown()


if __name__ == "__main__":
    sys.exit(main())
