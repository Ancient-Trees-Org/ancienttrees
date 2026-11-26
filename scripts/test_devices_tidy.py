"""Tests for scripts/devices_tidy.py's simulator plan, on a made-up device list.
python3 scripts/test_devices_tidy.py"""
import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import devices_tidy as dt

UTC = datetime.timezone.utc
NOW = datetime.datetime(2026, 11, 26, 15, 0, tzinfo=UTC)
GB = 1024 ** 3
fails = []


def dev(udid, name, state="Shutdown", hours_ago=48, gb=0.02):
    d = {"udid": udid, "name": name, "state": state, "isAvailable": True,
         "dataPathSize": int(gb * GB)}
    if hours_ago is not None:
        d["lastBootedAt"] = (NOW - datetime.timedelta(hours=hours_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")
    return d


def expect(name, got, want):
    ok = got == want
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f": got {got!r}, want {want!r}"))
    if not ok:
        fails.append(name)


def plan(devs):
    return sorted((a, u) for a, u, _, _ in dt.plan_simulators({"iOS-26-5": devs}, NOW))


expect("a session's own simulator that is idle and big goes",
       plan([dev("a", "AT dark hertz", gb=2.1)]), [("delete", "a")])
expect("a booted simulator is never touched, whatever its name",
       plan([dev("a", "AT dark hertz", state="Booted", gb=2.1)]), [])
expect("a simulator used in the last hours is left for its session",
       plan([dev("a", "AT dark hertz", hours_ago=2, gb=2.1)]), [])
expect("Xcode's own empty default is left alone",
       plan([dev("a", "iPhone Air", hours_ago=None)]), [])
expect("a fixed phone that grew is erased, not deleted",
       plan([dev("a", "iPhone SE (sweep) iOS 18.6", gb=2.9)]), [("erase", "a")])
expect("a fixed phone that is small stays as it is",
       plan([dev("a", "iPhone 17 Pro", gb=0.5)]), [])
expect("the second copy of a name goes, the newest boot stays",
       plan([dev("old", "iPhone SE (sweep)", hours_ago=200),
             dev("new", "iPhone SE (sweep)", hours_ago=30)]), [("delete", "old")])
expect("the version suffix keeps a fixed name fixed",
       dt.base_name("iPhone 16 Pro Max iOS 18.6"), "iPhone 16 Pro Max")

print(f"\n{len(fails)} failed" if fails else "\nall passed")
sys.exit(1 if fails else 0)
