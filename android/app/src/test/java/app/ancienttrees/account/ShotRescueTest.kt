package app.ancienttrees.account

import org.junit.Assert.assertArrayEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test
import java.nio.file.Files

// Report 1686 (2026-11-25, "Not able to add trees"): Android ended the app
// behind the system camera for memory, the photograph stayed in the cache and
// nothing ever read it. A shot left there is handed back once, when recent.
class ShotRescueTest {

    private val now = 1_764_100_000_000L

    @Test fun aRecentShotLeftInTheCacheIsHandedBackOnce() {
        val dir = Files.createTempDirectory("rescue").toFile()
        val f = Collector.shotFile(dir)
        f.writeBytes(byteArrayOf(1, 2, 3))
        f.setLastModified(now - 5 * 60 * 1000)
        assertArrayEquals(byteArrayOf(1, 2, 3), Collector.rescueShot(f, now))
        assertFalse(f.exists())
        assertNull(Collector.rescueShot(f, now))
    }

    @Test fun anOldOrEmptyShotIsThrownAwayNotHandedBack() {
        val dir = Files.createTempDirectory("rescue").toFile()
        val f = Collector.shotFile(dir)
        f.writeBytes(byteArrayOf(1))
        f.setLastModified(now - Collector.RESCUE_MS - 1000)
        assertNull(Collector.rescueShot(f, now))
        assertFalse(f.exists())
        f.writeBytes(ByteArray(0))
        f.setLastModified(now)
        assertNull(Collector.rescueShot(f, now))
    }

    @Test fun nothingInTheCacheIsNothingToHandBack() {
        val dir = Files.createTempDirectory("rescue").toFile()
        assertNull(Collector.rescueShot(Collector.shotFile(dir), now))
    }

    @Test fun onlyWrittenRecentShotsCount() {
        assertTrue(Collector.rescuable(10, now - 1000, now))
        assertFalse(Collector.rescuable(0, now, now))
        assertFalse(Collector.rescuable(10, now - Collector.RESCUE_MS, now))
        assertFalse(Collector.rescuable(10, now + 10 * 60 * 1000, now))
    }
}
