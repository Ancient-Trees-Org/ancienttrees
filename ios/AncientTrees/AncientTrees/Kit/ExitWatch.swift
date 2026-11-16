// Did the app last end while somebody was looking at it?
//
// WHY THIS EXISTS (Hidde, 2026-11-16, the Monday after the Guardian piece:
// "die app crashes klinkt bijna te goed om waar te zijn", then "Ja,
// uitzoeken"). MetricKit (Kit/Diagnostics.swift) reported ONE crash from about
// 4,000 new phones. It only reports from phones whose owner shares analytics
// with app developers, and it never reports the commonest way an app dies on
// a phone: iOS ending it for using too much memory, which is not a "crash"
// at all. Meanwhile 58 phones reopened the app within two minutes, 53 of
// those right after opening a tree. So the count we had was a sample with a
// hole in it, and the hole sat exactly where the suspicion was.
//
// THE CONVENTION. This is the "unclean shutdown" check Firebase Crashlytics,
// Bugsnag and Embrace use to count out-of-memory and watchdog terminations:
// write a flag when the app comes to the front, clear it when it goes to the
// back. A process that ends normally always passes through the background
// first (even a swipe-up from the app switcher), so a flag still there at the
// next launch means the app ended while it was on screen: a crash, the memory
// killer, or the watchdog. It counts every phone, needs no permission and no
// third party, and costs one small value in UserDefaults.
//
// WHAT IS SENT: one PostHog event, `app_exit_abnormal`, with the version that
// ended and the last thing measured before it (an event name and, on a tree
// page, the tree's id). Nothing about the person.
//
// ON THE DEVICE (hard rule 11): the flag is the app's own state, not
// something a person did; data/cross-device.json lists it as `device`.
//
// Known false alarm: a phone that switches off with the app open (a flat
// battery). Rare enough that a jump in this number still means the app.

import Foundation

enum ExitWatch {
    private static let key = "exit.foreground.v1"
    /// Fields inside that one value (named, so the store scanner reads them
    /// as parts of exit.foreground.v1 rather than stores of their own).
    private static let buildField = "version", lastField = "last", treeField = "tree"

    /// What the previous process left behind, read once before this launch
    /// writes anything. Set in AncientTreesApp.init, the earliest moment.
    private static var previous: [String: String]?

    /// Called first thing in AncientTreesApp.init.
    static func capture() {
        let d = UserDefaults.standard
        previous = d.dictionary(forKey: key) as? [String: String]
        d.removeObject(forKey: key)
    }

    /// Called once per launch, after Measure knows who is signed in.
    static func report() {
        guard var p = previous else { return }
        previous = nil
        let ended = p.removeValue(forKey: buildField)
        Measure.event("app_exit_abnormal", p.merging(["ended_build": ended ?? "?"]) { a, _ in a })
    }

    /// The app is on screen.
    static func foreground() {
        var p = UserDefaults.standard.dictionary(forKey: key) as? [String: String] ?? [:]
        p[buildField] = Bundle.main.infoDictionary?["CFBundleVersion"] as? String ?? "?"
        UserDefaults.standard.set(p, forKey: key)
    }

    /// The app left the screen normally.
    static func background() {
        UserDefaults.standard.removeObject(forKey: key)
    }

    /// The last thing measured while on screen, so a bad exit says where.
    static func note(_ event: String, tree: String?) {
        let d = UserDefaults.standard
        guard var p = d.dictionary(forKey: key) as? [String: String] else { return }
        p[lastField] = event
        if let tree { p[treeField] = tree } else { p.removeValue(forKey: treeField) }
        d.set(p, forKey: key)
    }
}
