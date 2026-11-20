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
//
// THE CRASH NOTE (Hidde, 2026-11-20: "yes to this", after five crashes on three
// collectors' phones on build 3 came in as a reason and nothing more, while
// PostHog's own crash handler, in that build since 11-16, delivered none of
// them). install() puts a small handler in front of PostHog's: at an uncaught
// exception it writes one line to the device preferences, synchronously, before
// anything else can fail (an out-of-memory crash leaves too little to build and
// queue an event; a short string still fits): the exception types and the top
// code lines, our own classes first (R8 keeps their names, proguard-rules.pro).
// The next launch sends it beside the crash's app_exit_abnormal as `trace`,
// then deletes it. Messages are cut short and stripped of addresses; nothing
// about the person (data/cross-device.json, android:device/exit.crash.note).
// scripts/app_crashes.py reads it, and health.py makes a new one rung-2 work.
object ExitWatch {
    private const val PREFS = "device"
    private const val SEEN = "exit.reported.at"
    private const val NOTE = "exit.crash.note"

    /** After CrashReporter.start, so this runs first and then hands on to PostHog's handler. */
    private var installed = false

    fun install(context: Context) {
        // onCreate runs again when the activity is recreated: one handler, not a chain of them.
        if (installed) return
        installed = true
        val prefs = context.applicationContext.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
        val next = Thread.getDefaultUncaughtExceptionHandler()
        Thread.setDefaultUncaughtExceptionHandler { thread, e ->
            try {
                prefs.edit().putString(NOTE, note(e, thread.name == "main")).commit()
            } catch (_: Throwable) {
            }
            next?.uncaughtException(thread, e)
        }
    }

    /** The line that is kept: pure, so a unit test holds it to its shape and length. */
    internal fun note(e: Throwable, mainThread: Boolean): String {
        val chain = generateSequence(e) { t -> t.cause?.takeIf { it !== t } }.take(5).toList()
        val types = chain.joinToString(" < ") { it.javaClass.name.substringAfterLast('.') }
        val msg = scrub(chain.last().message ?: chain.first().message ?: "")
        val frames = chain.flatMap { it.stackTrace.asList() }
        val ours = frames.filter { it.className.startsWith("app.ancienttrees") }.take(5)
        val lines = (frames.take(2) + ours).distinct().joinToString(" | ") {
            it.className.substringAfterLast('.') + "." + it.methodName + ":" + it.lineNumber
        }
        val head = types + (if (msg.isNotEmpty()) " ($msg)" else "") + (if (mainThread) "" else " [bg]")
        return "$head @ $lines".take(600)
    }

    private val MAIL = Regex("\\S+@\\S+")
    private val ADDRESS = Regex("(https?|content|file)://\\S+")
    private val LONG_NUMBER = Regex("\\d{6,}")

    /** No web or mail addresses, no long numbers, one line; at most 80 characters. */
    internal fun scrub(s: String): String =
        s.replace(MAIL, "<mail>").replace(ADDRESS, "<address>").replace(LONG_NUMBER, "<n>")
            .replace('\n', ' ').trim().take(80)

    fun report(context: Context) {
        val prefs = context.applicationContext.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
        val crashNote = prefs.getString(NOTE, null)
        if (crashNote != null) prefs.edit().remove(NOTE).apply()
        val sent = exits(context, prefs, crashNote)
        // A note with no exit to sit beside (Android 10, or the first launch with
        // this code) still says where it crashed.
        if (crashNote != null && !sent) Measure.event("app_crash_note", mapOf("trace" to crashNote))
    }

    /** Reports the bad exits since the last look; true when the crash note went with one. */
    private fun exits(context: Context, prefs: android.content.SharedPreferences, crashNote: String?): Boolean {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.R) return false
        val am = context.getSystemService(ActivityManager::class.java) ?: return false
        val exits = try {
            am.getHistoricalProcessExitReasons(context.packageName, 0, 10)
        } catch (e: Exception) {
            return false
        }
        val seen = prefs.getLong(SEEN, 0L)
        val first = seen == 0L
        var newest = seen
        var noteSent = false
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
            val props = mutableMapOf("reason" to why, "on_screen" to if (onScreen) "yes" else "no")
            e.description?.takeIf { it.isNotBlank() }?.let { props["detail"] = scrub(it) }
            // The exits come newest first: the note belongs to the newest crash.
            if (crashNote != null && !noteSent && why == "crash") {
                props["trace"] = crashNote
                noteSent = true
            }
            Measure.event("app_exit_abnormal", props)
        }
        val mark = nextMark(seen, newest, System.currentTimeMillis())
        if (mark != seen) prefs.edit().putLong(SEEN, mark).apply()
        return noteSent
    }

    /**
     * The mark after a look. The first look sets it to now even when the phone has
     * no exits on record: left at 0, the next look counted as "first" again and
     * swallowed the first real crash, freeze or map crash after a clean install
     * (found 2026-11-20 on build 4's own crash proof, which arrived as a loose
     * app_crash_note instead of beside its app_exit_abnormal).
     */
    internal fun nextMark(seen: Long, newestExit: Long, now: Long): Long =
        if (seen == 0L) maxOf(newestExit, now) else maxOf(seen, newestExit)
}
