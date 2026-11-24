#!/usr/bin/env python3
"""android_prelaunch.py - every machine check on the Android app, in one go, before Hidde tests a build.

Hidde, 2026-11-18: "voeg deze strategie aan ons algehele testplan toe zodat de
volgende keer in een keer deze hele chain kan starten". The machine half of
RELEASE_CHECKLIST.md "Every build"; the three walks by a session follow it.

    python3 scripts/android_prelaunch.py            # everything, on emulator-5554
    python3 scripts/android_prelaunch.py --skip-walks

In order, stopping at nothing (each step reports; the summary says what failed):
  1. unit tests (testDebugUnitTest)
  2. the Play build: signed aab and apk (scripts/android_release.py --apk)
  3. every instrumented test (FlowWalk, SignedInRoundTrip, ButtonWalk) against the
     "minified" build type: the Play build's own R8 with the test door open
     (build.gradle.kts), so a class R8 strips wrongly fails here, not on a phone
  4. the Play apk itself, opened by finger (scripts/android_release_walk.py)
  5. spacing against the iPhone (scripts/android_spacing.py)
Needs a running emulator (ANDROID_SERIAL, default emulator-5554) and, for the
signed-in round trip, SUPABASE_SERVICE_KEY (from ~/.ancienttrees-supabase.env).
Never runs on a physical phone.
"""
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
SDK = pathlib.Path.home() / "Library" / "Android" / "sdk"
JBR = "/Applications/Android Studio.app/Contents/jbr/Contents/Home"
SERIAL = os.environ.get("ANDROID_SERIAL", "emulator-5554")
if not SERIAL.startswith("emulator-"):
    sys.exit("android_prelaunch.py runs on an emulator only (ANDROID_SERIAL=emulator-...)")

ENV = dict(os.environ, ANDROID_HOME=str(SDK), JAVA_HOME=JBR, ANDROID_SERIAL=SERIAL)
results = []


def step(name, cmd, cwd=ROOT, env=None, limit=1800):
    """One step, killed after `limit` seconds: a hung emulator or a waiting lock
    otherwise stalls the whole chain with nobody to notice (2026-11-18, spacing
    sat for an hour behind a stale copy of itself)."""
    started = time.time()
    print(f"\n== {name}", flush=True)
    try:
        ok = subprocess.run(cmd, cwd=cwd, env=env or ENV, timeout=limit).returncode == 0
        note = ""
    except subprocess.TimeoutExpired:
        ok, note = False, f", HUNG: killed after {limit // 60} min"
    took = int(time.time() - started)
    results.append((name + note, ok, took))
    print(f"== {name}: {'ok' if ok else 'FAILED'} ({took} s{note})", flush=True)


def test_session():
    """The test account's session for SignedInRoundTrip, as CI makes it (scripts/test_session.py)."""
    env = dict(ENV)
    f = pathlib.Path.home() / ".ancienttrees-supabase.env"
    if f.exists():
        for line in f.read_text().splitlines():
            if line.startswith("SUPABASE_SERVICE_KEY="):
                env["SUPABASE_SERVICE_KEY"] = line.split("=", 1)[1].strip().strip('"')
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "test_session.py")], capture_output=True, text=True, env=env)
    return r.stdout.strip() if r.returncode == 0 else ""


gradle = ["./gradlew", "--no-daemon", "-q"]
android = ROOT / "android"
step("unit tests", gradle + ["testDebugUnitTest"], cwd=android)
step("Play build (aab + apk)", [sys.executable, "scripts/android_release.py", "--apk"])
if "--skip-walks" not in sys.argv:
    session = test_session()
    # A Play-signed install left by an earlier walk refuses the debug-signed test apk.
    subprocess.run([str(SDK / "platform-tools" / "adb"), "-s", SERIAL, "uninstall", "app.ancienttrees.map"], capture_output=True)
    step("every instrumented test on the Play build's R8 (minified)",
         gradle + ["-PtestMinified", "connectedMinifiedAndroidTest",
                   f"-Pandroid.testInstrumentationRunnerArguments.AT_SESSION={session}"], cwd=android)
    # The test run uninstalls the app; the Play apk goes on fresh for the finger walk.
    subprocess.run([str(SDK / "platform-tools" / "adb"), "-s", SERIAL, "uninstall", "app.ancienttrees.map"], capture_output=True)
    step("the Play apk opened by finger", [sys.executable, "scripts/android_release_walk.py"])
    step("spacing against the iPhone", [sys.executable, "scripts/android_spacing.py"])

print("\n== summary")
for name, ok, took in results:
    print(f"  {'ok    ' if ok else 'FAILED'}  {name} ({took} s)")
print("  results: android/app/build/outputs/androidTest-results/connected/, frames in /data/local/tmp/walk on the emulator, out/play/walk/")
sys.exit(0 if all(ok for _, ok, _ in results) else 1)
