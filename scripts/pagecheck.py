#!/usr/bin/env python3
"""Do the pages RUN? A real Chrome opens a fixed set of pages and waits.

Hidde, 2026-11-06 ("ons platform wordt steeds groter, dit soort fouten worden
steeds duurder", then "dit lijkt me een goed systeem doe het"): that afternoon
/explore crashed every visitor's tab a few seconds after loading (Chrome
"Error code 5"). The trees list painted its hearts with a function that
refiltered the map, the refilter redrew the list, forever. Every check in the
deploy passed, because qa.py and preflight read the HTML and the data and
never run a line of the JavaScript; the smoke test runs Chrome, but after the
site is live, and its hang was read as a fault of the test.

So this opens each page in Chrome at desktop and phone width, waits long
enough for the late work to happen (the card catalogue arrives after a few
seconds, which is exactly when that loop started), and fails when:
  - the tab crashed (the renderer died: Chrome's "Aw, Snap" / error code 5),
  - the page stopped answering (the main thread is stuck in a loop),
  - an uncaught JavaScript error came from our own scripts.
A failing page is opened once more before it counts, so one slow start is not
a blocked deploy; a broken page fails both times.

Two uses, one page set:
  python3 scripts/pagecheck.py                 the built site in site/dist,
                                               served locally (deploy.yml,
                                               BEFORE the upload: a failure
                                               keeps the old site live)
  python3 scripts/pagecheck.py --live          https://ancienttrees.app
                                               (pages-live.yml, every hour)
  python3 scripts/pagecheck.py --base URL      any other origin

Needs Python Playwright (pip install playwright==1.60.0). It drives the Chrome
the machine already has (channel "chrome", as GitHub's ubuntu runners carry
google-chrome), else Playwright's own Chromium if one is installed.

Exit 0 when every page ran, 1 when one did not, 2 when no browser could start.
"""
import argparse
import functools
import os
import sys
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "site" / "dist"
LIVE = "https://ancienttrees.app"

# The pages people land on, and every kind of map: the explore map over the
# United Kingdom is the 2026-11-06 crash, kept as its own line. The tree is the
# one uptime.yml fetches (lon_001); if it is ever retired, change both.
PAGES = [
    ("/", "home"),
    ("/explore", "explore map"),
    ("/explore#map=5.5/54.5/-3", "explore map over the United Kingdom"),
    ("/london", "city page"),
    ("/london/totteridge-yew", "tree page"),
    ("/united-kingdom", "country page"),
    ("/cities", "cities index"),
    ("/contribute", "contribute"),
    ("/visitors", "New from visitors, See all"),
    ("/nl/amsterdam", "translated city page"),
]
WIDTHS = [(1280, 800, "desktop"), (390, 844, "phone")]

# How long a page gets to do its late work before it is judged, and how long a
# stuck main thread is given to answer before it counts as hung.
SETTLE_S = 8
ANSWER_MS = 5000
LOAD_MS = 30000


class Pages(SimpleHTTPRequestHandler):
    """site/dist the way GitHub Pages serves it: /london is london.html
    FIRST, and london/index.html only when there is no london.html. The
    first deploy with this check (2026-11-06) served the folder's index
    first, and /london never finished loading, while the live /london was
    fine (GitHub answers it with london.html, 708 KB, checked with curl)."""

    def log_message(self, *a):
        pass

    def translate_path(self, path):
        clean = path.split("?", 1)[0].split("#", 1)[0]
        p = Path(super().translate_path(clean))
        if not p.suffix and not clean.endswith("/") and p.with_suffix(".html").is_file():
            return str(p.with_suffix(".html"))
        if p.is_dir() and (p / "index.html").is_file():
            return str(p / "index.html")
        return str(p)


def serve(dist):
    handler = functools.partial(Pages, directory=str(dist))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, "http://127.0.0.1:%d" % server.server_address[1]


def launch(pw):
    args = ["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--no-sandbox"]
    for kw in ({"channel": "chrome"}, {}):
        try:
            return pw.chromium.launch(args=args, **kw)
        except Exception as e:
            last = e
    raise last


def check(browser, base, path, size):
    """One page at one width: None when it ran, else what went wrong."""
    w, h, _ = size
    ctx = browser.new_context(viewport={"width": w, "height": h})
    page = ctx.new_page()
    origin = base.split("://", 1)[-1]
    crashed, errors = [], []
    page.on("crash", lambda *a: crashed.append(True))

    def on_error(e):
        stack = (getattr(e, "stack", "") or "") + " " + str(e)
        # Ours only: a page's own inline script, or a file served from it.
        # A failure inside the map library's WebGL start on a headless machine
        # is the machine, not the page (web_errors.py sees those as well).
        if origin in stack and "Failed to initialize WebGL" not in stack:
            errors.append(str(e).splitlines()[0][:200])
    page.on("pageerror", on_error)
    try:
        try:
            page.goto(base + path, wait_until="domcontentloaded", timeout=LOAD_MS)
        except Exception as e:
            if crashed:
                return "the tab crashed while loading"
            return "did not load (%s)" % str(e).splitlines()[0][:120]
        deadline = time.time() + SETTLE_S
        while time.time() < deadline:
            if crashed:
                return "the tab crashed (Chrome error code 5)"
            try:
                page.wait_for_function("true", timeout=ANSWER_MS)
            except Exception:
                if crashed:
                    return "the tab crashed (Chrome error code 5)"
                return "the page stopped answering (a script is stuck in a loop)"
            time.sleep(1)
        if crashed:
            return "the tab crashed (Chrome error code 5)"
        if errors:
            return "JavaScript error: " + errors[0]
        return None
    finally:
        try:
            ctx.close()
        except Exception:
            pass


# THE MAP WALK (Hidde, 2026-11-20: "welke vraag moet ik jou stellen dat je
# overal dezelfde kaart ervaring goed fixed ... binnen web niet [afwijken]").
# Every website map is one component (tree-map-js.ts, tree-pins-js.ts,
# map-card-js.ts), but that day a CSS line broke the city map's pins on Kyoto
# while every source check stayed green. So the same steps run on every kind of
# map, at a desktop and a laptop width, and any map that answers differently
# stops the deploy:
#   - every pin is a MapLibre marker standing absolute (the Kyoto fault);
#   - the map's buttons are the same: zoom, one find-me (not on a map inside a
#     page), no full screen;
#   - pointing at a pin lights it, and no other pin moves;
#   - pointing at a row in the list lights its pin, and no pin moves;
#   - a click on a pin opens the tree card beside it, never over the pin, and
#     its photograph loads;
#   - a full map keeps its place in the address (#map=).
# (path, label, inside a page: no find-me, no scroll zoom, no address)
MAP_WALK = [
    ("/kyoto", "city map", False),
    ("/explore#map=12/35.01/135.76", "explore map", False),
    ("/japan", "country map", False),
    ("/united-states/california", "state map", True),
]
WALK_WIDTHS = [(1440, 900, "desktop"), (1024, 768, "laptop")]

WALK_JS = r"""
() => {
  const box = document.querySelector('.maplibregl-map');
  const marks = Array.from(document.querySelectorAll('.maplibregl-marker.pin-tree'));
  marks.forEach((m, i) => { if (!m.dataset.walk) m.dataset.walk = 'w' + i + '_' + Math.random().toString(36).slice(2, 6); });
  const r = box ? box.getBoundingClientRect() : null;
  const pins = marks.map(m => {
    const b = m.getBoundingClientRect();
    return {k: m.dataset.walk, x: b.left + b.width / 2, y: b.top + b.height / 2,
            w: b.width, h: b.height, pos: getComputedStyle(m).position,
            active: m.classList.contains('active'), name: m.getAttribute('aria-label') || ''};
  });
  return {
    map: r ? {l: r.left, t: r.top, r: r.right, b: r.bottom} : null,
    pins: pins,
    zoom: document.querySelectorAll('.maplibregl-ctrl-zoom-in').length,
    geo: document.querySelectorAll('.maplibregl-ctrl-geolocate').length,
    full: document.querySelectorAll('.maplibregl-ctrl-fullscreen').length,
    hash: location.hash,
  };
}
"""


def _inside(p, m, pad=60):
    return m["l"] + pad < p["x"] < m["r"] - pad and m["t"] + pad < p["y"] < m["b"] - pad


def _moved(before, after, skip=()):
    """Pins present both times that moved more than 2 px."""
    now = {p["k"]: p for p in after["pins"]}
    out = []
    for p in before["pins"]:
        q = now.get(p["k"])
        if q and p["k"] not in skip and (abs(q["x"] - p["x"]) > 2 or abs(q["y"] - p["y"]) > 2):
            out.append(p["name"] or p["k"])
    return out


def walk(browser, base, path, embedded, size):
    """The map walk on one map at one width: a list of what went wrong."""
    w, h, _ = size
    ctx = browser.new_context(viewport={"width": w, "height": h})
    page = ctx.new_page()
    bad = []
    try:
        page.goto(base + path, wait_until="domcontentloaded", timeout=LOAD_MS)
        if not page.evaluate("() => { try { return !!document.createElement('canvas').getContext('webgl'); } catch (e) { return false; } }"):
            return None  # no WebGL on this machine: the walk cannot see a map
        try:
            page.wait_for_function(
                "() => document.querySelectorAll('.maplibregl-marker.pin-tree').length >= 3",
                timeout=25000)
        except Exception:
            return ["no pins appeared on the map within 25 seconds"]
        time.sleep(2.5)
        s0 = page.evaluate(WALK_JS)
        m = s0["map"]
        loose = [p["name"] or p["k"] for p in s0["pins"] if p["pos"] != "absolute"]
        if loose:
            bad.append("%d pin(s) are not position:absolute (%s), so they stack and jump" % (len(loose), loose[0]))
        if s0["zoom"] != 1:
            bad.append("%d zoom buttons, not 1" % s0["zoom"])
        want_geo = 0 if embedded else 1
        if s0["geo"] != want_geo:
            bad.append("%d find-me buttons, not %d" % (s0["geo"], want_geo))
        if s0["full"]:
            bad.append("a full-screen button, which no other map has")

        # Pointing at a pin.
        seen = [p for p in s0["pins"] if _inside(p, m)]
        if not seen:
            bad.append("no pin stands inside the map to point at")
            return bad
        target = seen[len(seen) // 2]
        page.mouse.move(target["x"], target["y"])
        time.sleep(0.8)
        s1 = page.evaluate(WALK_JS)
        lit = [p for p in s1["pins"] if p["k"] == target["k"]]
        if not lit or not lit[0]["active"]:
            bad.append("pointing at a pin does not light it (%s)" % target["name"])
        moved = _moved(s0, s1, skip=(target["k"],))
        if moved:
            bad.append("pointing at a pin moved %d other pin(s) (%s)" % (len(moved), moved[0]))
        page.mouse.move(m["l"] + 8, m["b"] - 8)
        time.sleep(0.8)

        # Pointing at a row in the list beside the map.
        rows = page.evaluate("""(m) => Array.from(document.querySelectorAll('[data-tree-id]'))
          .filter(e => { const b = e.getBoundingClientRect();
            return b.width > 40 && b.height > 20 && b.top >= 0 && b.bottom <= innerHeight
              && !(b.left >= m.l && b.right <= m.r && b.top >= m.t && b.bottom <= m.b)
              && !e.closest('.maplibregl-map'); })
          .slice(0, 1).map(e => { const b = e.getBoundingClientRect();
            return {x: b.left + b.width / 2, y: b.top + Math.min(b.height / 2, 30), text: e.textContent}; })""", m)
        if rows:
            s2 = page.evaluate(WALK_JS)
            page.mouse.move(rows[0]["x"], rows[0]["y"])
            time.sleep(0.8)
            s3 = page.evaluate(WALK_JS)
            moved = _moved(s2, s3)
            if moved:
                bad.append("pointing at a row in the list moved %d pin(s) (%s)" % (len(moved), moved[0]))
            act = [p for p in s3["pins"] if p["active"]]
            if len(act) > 1:
                bad.append("pointing at one row lit %d pins" % len(act))
            elif act and act[0]["name"] and act[0]["name"] not in rows[0]["text"]:
                bad.append("pointing at a row lit another tree's pin (%s)" % act[0]["name"])
            page.mouse.move(m["l"] + 8, m["b"] - 8)
            time.sleep(0.8)

        # A click on a pin opens the card beside it.
        s4 = page.evaluate(WALK_JS)
        live = [p for p in s4["pins"] if _inside(p, m)]
        if live:
            t = live[len(live) // 2]
            page.mouse.click(t["x"], t["y"])
            try:
                page.wait_for_selector(".map-pop", timeout=5000)
            except Exception:
                bad.append("a click on a pin opened no tree card (%s)" % t["name"])
            else:
                time.sleep(1.0)
                pop = page.evaluate("""(k) => {
                  const c = document.querySelector('.map-pop').getBoundingClientRect();
                  const pin = document.querySelector('[data-walk="' + k + '"]');
                  const p = pin ? pin.getBoundingClientRect() : null;
                  const img = document.querySelector('.map-pop .tree-card-photo img');
                  return {c: {l: c.left, t: c.top, r: c.right, b: c.bottom},
                          p: p ? {x: p.left + p.width / 2, y: p.top + p.height / 2} : null,
                          img: img ? {src: img.currentSrc || img.src} : null};
                }""", t["k"])
                if pop["p"]:
                    c, p = pop["c"], pop["p"]
                    if c["l"] < p["x"] < c["r"] and c["t"] < p["y"] < c["b"]:
                        bad.append("the tree card covers its own pin (%s)" % t["name"])
                if pop["img"]:
                    try:
                        page.wait_for_function(
                            "() => { const i = document.querySelector('.map-pop .tree-card-photo img'); return i && i.complete && i.naturalWidth > 0; }",
                            timeout=8000)
                    except Exception:
                        bad.append("the tree card's photograph did not load (%s)" % t["name"])
            page.keyboard.press("Escape")
            time.sleep(0.5)

        # A full map keeps its place in the address.
        if not embedded:
            page.mouse.move((m["l"] + m["r"]) / 2, (m["t"] + m["b"]) / 2 + 40)
            page.mouse.wheel(0, -300)
            time.sleep(2.0)
            if not page.evaluate("() => location.hash").startswith("#map="):
                bad.append("the map does not keep its place in the address (#map=)")
        return bad
    except Exception as e:
        return bad + ["the walk stopped: %s" % str(e).splitlines()[0][:160]]
    finally:
        try:
            ctx.close()
        except Exception:
            pass


def run_walk(browser, pw, base, failures):
    for path, label, embedded in MAP_WALK:
        for size in WALK_WIDTHS:
            what = walk(browser, base, path, embedded, size)
            if what is None:
                print("  skip  map walk %-30s %-7s no WebGL on this machine" % (path, size[2]))
                continue
            if what:
                if not browser.is_connected():
                    browser = launch(pw)
                again = walk(browser, base, path, embedded, size)
                if again:
                    for one in again:
                        failures.append((path, label + ", map walk", size[2], one))
                        print("  FAIL  map walk %-30s %-7s %s" % (path, size[2], one))
                    continue
            print("  ok    map walk %-30s %s" % (path, size[2]))
    return browser


def run(base, only_walk=False):
    from playwright.sync_api import sync_playwright
    failures = []
    with sync_playwright() as pw:
        try:
            browser = launch(pw)
        except Exception as e:
            print("pagecheck: no browser could start (%s)" % str(e).splitlines()[0][:160])
            return 2
        for path, label in ([] if only_walk else PAGES):
            for size in WIDTHS:
                what = check(browser, base, path, size)
                if what:
                    # A crashed renderer can take the browser down with it.
                    if not browser.is_connected():
                        browser = launch(pw)
                    again = check(browser, base, path, size)
                    if again:
                        failures.append((path, label, size[2], again))
                        print("  FAIL  %-34s %-7s %s" % (path, size[2], again))
                        if not browser.is_connected():
                            browser = launch(pw)
                        continue
                print("  ok    %-34s %s" % (path, size[2]))
        browser = run_walk(browser, pw, base, failures)
        browser.close()
    if failures:
        print("\npagecheck: %d failure(s) on %s:" % (len(failures), base))
        for path, label, width, what in failures:
            print("  %s (%s, %s): %s" % (path, label, width, what))
        return 1
    print("\npagecheck: all %d pages ran at both widths, and every map walked the same, on %s"
          % (len(PAGES), base))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--live", action="store_true", help="check %s" % LIVE)
    ap.add_argument("--base", help="check this origin instead of site/dist")
    ap.add_argument("--dist", default=str(DIST), help="the built site to serve")
    ap.add_argument("--walk", action="store_true", help="only the map walk")
    a = ap.parse_args()
    if a.live or a.base:
        return run((a.base or LIVE).rstrip("/"), a.walk)
    dist = Path(a.dist)
    if not (dist / "index.html").exists():
        print("pagecheck: no built site at %s (run astro build first)" % dist)
        return 1
    server, base = serve(dist)
    try:
        return run(base, a.walk)
    finally:
        server.shutdown()


if __name__ == "__main__":
    sys.exit(main())
