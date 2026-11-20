#!/usr/bin/env python3
"""A map change crosses every platform, or says why it does not.

Hidde, 2026-11-20, after the one tree pin, the clear-dot rule and the card
reached the website and not the phones: "wees zelf kritisch als we dingen in
een kaart aanpakken moeten we altijd over platformen heen denken. niet alles
moet hetzelfde maar als het kan wel". The both-surfaces rule had said so in
prose since 2026-08-21; crosscheck.py holds the FEED to it, and nothing held
the map's own behaviour, which lives in code on three surfaces.

So: a push that changes how a website map draws or behaves (the files in WEB)
and touches no phone map (APP) must also change data/map-parity.json, the
ledger where every such difference stands with what each platform does, and
either the phones' open debt or the reason it stays web only. A push that
changes the phones' map alone is held the same way. Run by scripts/hooks/
pre-push on the files being pushed; qa's check_map_parity_ledger() holds the
ledger's shape.

    python3 scripts/mapparity.py FILE...   # exit 1 when the ledger is owed
    python3 scripts/mapparity.py           # the push's files against origin/main
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = "data/map-parity.json"

# What a website map draws and does: the pins, the dots, the card, the
# filters, the map scripts themselves.
WEB = re.compile(r"^site/src/lib/(tree-pins-js|map-card-js|map|city-map-script|tree-page-js|map-filters-js|map-spread)\.ts$"
                 r"|^site/src/components/ExploreMap\.astro$")
# The phones' maps.
APP = re.compile(r"^ios/AncientTrees/AncientTrees/Screens/(TreeMap|MapTab|MapLayers|MapSheet)[A-Za-z]*\.swift$"
                 r"|^android/app/src/main/java/app/ancienttrees/(map/[A-Za-z]+\.kt|ui/(Map[A-Za-z]*|TreeMapPage)\.kt)$")


def owed(files):
    files = [f.strip() for f in files if f.strip()]
    web = [f for f in files if WEB.search(f)]
    app = [f for f in files if APP.search(f)]
    if (web and not app) or (app and not web):
        if LEDGER not in files:
            side = web or app
            return ("%s changes a map on %s only (%s) and %s is not in the push. "
                    "Bring the other platforms along, or add or update the ledger's row: what each "
                    "platform does, and the phones' open debt or why it stays one-sided."
                    % ("This push", "the website" if web else "the phones", ", ".join(side[:3]), LEDGER))
    return None


def main(argv):
    if argv:
        files = argv
    else:
        out = subprocess.run(["git", "diff", "--name-only", "origin/main", "HEAD"], cwd=ROOT,
                             capture_output=True, text=True).stdout
        files = out.splitlines()
    msg = owed(files)
    if msg:
        print(msg)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
