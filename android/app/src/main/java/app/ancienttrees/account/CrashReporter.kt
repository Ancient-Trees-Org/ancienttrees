package app.ancienttrees.account

import android.content.Context
import com.posthog.android.PostHogAndroid
import com.posthog.android.PostHogAndroidConfig

// The Android twin of Kit/CrashReporter.swift (Hidde, 2026-11-16: "laten we dat
// pad volgen zet het in de volgende build en ook android"). PostHog's own SDK,
// used for its crash handler only: an uncaught exception becomes a `$exception`
// event in the PostHog project the app already measures into. Screen views,
// lifecycle events, session replay, feature flags and person profiles stay off;
// our own events still go through Measure.kt. An emulator sends nothing, the
// same line Measure draws. Stack traces read as source lines once the R8
// mapping is uploaded (needs a personal API key from Hidde).
object CrashReporter {
    fun start(context: Context) {
        if (Measure.isEmulator()) return
        val config = PostHogAndroidConfig(apiKey = Measure.KEY, host = Measure.PROJECT_HOST).apply {
            errorTrackingConfig.autoCapture = true
            captureApplicationLifecycleEvents = false
            captureScreenViews = false
            captureDeepLinks = false
            sessionReplay = false
            preloadFeatureFlags = false
            personProfiles = com.posthog.PersonProfiles.NEVER
        }
        PostHogAndroid.setup(context.applicationContext, config)
    }
}
