package app.ancienttrees.account

import android.app.ActivityManager
import android.app.ApplicationExitInfo
import android.content.Context
import android.os.Build

// The Android twin of Kit/ExitWatch.swift (Hidde, 2026-11-16, "Ja, uitzoeken",
// after the iPhone's crash count turned out to miss memory kills). Android
// does what iOS makes us build by hand: since Android 11 the system keeps the
// reasons the last processes ended (ApplicationExitInfo, the platform's own
// convention for this, used by Crashlytics and Play vitals). At launch the
// ones since the last look that ended badly (a crash, a native crash, an
// ANR, the low-memory killer, excessive resource use) each become one
// `app_exit_abnormal` event, the same name the iPhone sends, with the reason
// and whether the app was on screen. Nothing about the person.
//
// ON THE DEVICE: one timestamp in the "device" preferences, the newest exit
// already reported, so none is sent twice (data/cross-device.json,
// android:device/exit.reported.at).
object ExitWatch {
    private const val PREFS = "device"
    private const val SEEN = "exit.reported.at"

    fun report(context: Context) {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.R) return
        val prefs = context.applicationContext.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
        val am = context.getSystemService(ActivityManager::class.java) ?: return
        val exits = try {
            am.getHistoricalProcessExitReasons(context.packageName, 0, 10)
        } catch (e: Exception) {
            return
        }
        val seen = prefs.getLong(SEEN, 0L)
        val first = seen == 0L
        var newest = seen
        for (e in exits) {
            if (e.timestamp <= seen) continue
            newest = maxOf(newest, e.timestamp)
            // The first launch with this code only sets the mark: exits from
            // before it was installed say nothing about this version.
            if (first) continue
            val why = when (e.reason) {
                ApplicationExitInfo.REASON_CRASH -> "crash"
                ApplicationExitInfo.REASON_CRASH_NATIVE -> "crash_native"
                ApplicationExitInfo.REASON_ANR -> "anr"
                ApplicationExitInfo.REASON_LOW_MEMORY -> "memory"
                ApplicationExitInfo.REASON_EXCESSIVE_RESOURCE_USAGE -> "resources"
                ApplicationExitInfo.REASON_INITIALIZATION_FAILURE -> "init_failure"
                else -> null
            } ?: continue
            val onScreen = e.importance <= ActivityManager.RunningAppProcessInfo.IMPORTANCE_FOREGROUND
            Measure.event("app_exit_abnormal", mapOf("reason" to why, "on_screen" to if (onScreen) "yes" else "no"))
        }
        if (newest != seen) prefs.edit().putLong(SEEN, newest).apply()
    }
}
