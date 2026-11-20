package app.ancienttrees.account

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

// The crash note (ExitWatch.note): the types, our own code lines, no addresses,
// one bounded line (Hidde, 2026-11-20, after five crashes arrived with no line).
class ExitWatchTest {
    private fun frame(cls: String, fn: String, line: Int) = StackTraceElement(cls, fn, "SourceFile", line)

    @Test
    fun namesTheTypesAndOurOwnLines() {
        val cause = OutOfMemoryError("Failed to allocate 48000000 byte allocation")
        cause.stackTrace = arrayOf(
            frame("android.graphics.BitmapFactory", "nativeDecodeByteArray", 0),
            frame("android.graphics.BitmapFactory", "decodeByteArray", 1),
            frame("app.ancienttrees.ui.MyTreesKt", "photo", 950),
            frame("androidx.compose.runtime.Composer", "apply", 10),
        )
        val e = IllegalStateException("wrapped", cause)
        e.stackTrace = arrayOf(frame("app.ancienttrees.ui.MyTreesKt", "MyTrees", 120))
        val n = ExitWatch.note(e, mainThread = true)
        assertTrue(n, n.startsWith("IllegalStateException < OutOfMemoryError"))
        assertTrue(n, n.contains("MyTreesKt.photo:950"))
        assertTrue(n, n.contains("MyTreesKt.MyTrees:120"))
        assertFalse(n, n.contains("48000000"))
        assertFalse(n, n.contains("[bg]"))
        assertTrue(n.length <= 600)
    }

    @Test
    fun aBackgroundThreadIsMarked() {
        val e = RuntimeException("x")
        e.stackTrace = arrayOf(frame("app.ancienttrees.feed.Feed", "load", 3))
        assertTrue(ExitWatch.note(e, mainThread = false).contains("[bg]"))
    }

    @Test
    fun scrubTakesOutAddressesAndMail() {
        assertEquals(
            "open <address> for <mail> failed",
            ExitWatch.scrub("open https://x.supabase.co/a?token=abc for someone@example.com failed"),
        )
        assertEquals(80, ExitWatch.scrub("a".repeat(200)).length)
    }

    @Test
    fun theFirstLookSetsTheMarkEvenWithNoExits() {
        // A clean install has no exits on record: the mark must still move off 0,
        // or the first real crash afterwards is taken for "first look" and dropped.
        assertEquals(1_000L, ExitWatch.nextMark(seen = 0L, newestExit = 0L, now = 1_000L))
        assertEquals(2_000L, ExitWatch.nextMark(seen = 0L, newestExit = 2_000L, now = 1_000L))
    }

    @Test
    fun laterLooksFollowTheExitsNotTheClock() {
        assertEquals(1_000L, ExitWatch.nextMark(seen = 1_000L, newestExit = 900L, now = 5_000L))
        assertEquals(3_000L, ExitWatch.nextMark(seen = 1_000L, newestExit = 3_000L, now = 5_000L))
    }

    @Test
    fun aCauseLoopEnds() {
        val a = RuntimeException("a")
        val b = RuntimeException("b", a)
        a.initCause(b)
        assertTrue(ExitWatch.note(b, true).length <= 600)
    }
}
