// Every crash, on every phone, with the line it happened on.
//
// Hidde, 2026-11-16, after the Guardian weekend: MetricKit (Kit/Diagnostics.swift)
// had reported one crash from about 4,000 new phones, because it only hears
// from phones that share analytics with developers and never says what ended
// the app. He wanted one tool rather than another ("kan het niet gewoon met
// posthog, geen zin in weer de volgende tool", then "laten we dat pad volgen
// zet het in de volgende build en ook android"). So crashes go to the PostHog
// project the app already measures into, through PostHog's own SDK, used here
// for exactly one thing: its crash handler (Mach exceptions, POSIX signals,
// uncaught NSExceptions), written to disk at the crash and sent as a
// `$exception` event of level "fatal" at the next launch. PostHog's own
// convention, docs "Error tracking for iOS".
//
// EVERYTHING ELSE THE SDK CAN DO IS OFF: no screen views, no app-lifecycle
// events, no taps, no session replay, no feature flags, no person profiles.
// Our own events still go through Kit/Measure.swift, unchanged. The SDK keeps
// its own anonymous id; `install_id` beside every crash is Measure's, so a
// crash can be read next to what that phone did before it.
//
// THE SAME LINE AS MEASURE: a simulator sends nothing (Measure.isOn), so no
// test, sweep or CI run is ever counted.
//
// STACK TRACES read as file and line once the build's dSYMs are uploaded to
// PostHog (release step, needs a personal API key from Hidde); until then
// they arrive as addresses, which scripts/crash_symbols.py's map can still read.

import Foundation
import PostHog

enum CrashReporter {
    static func start() {
        guard Measure.isOn else { return }
        let config = PostHogConfig(projectToken: Measure.key, host: Measure.projectHost)
        config.errorTrackingConfig.autoCapture = true
        config.captureApplicationLifecycleEvents = false
        config.captureScreenViews = false
        config.captureElementInteractions = false
        config.sessionReplay = false
        config.preloadFeatureFlags = false
        config.personProfiles = .never
        PostHogSDK.shared.setup(config)
        PostHogSDK.shared.register(["install_id": Measure.install])
    }
}
