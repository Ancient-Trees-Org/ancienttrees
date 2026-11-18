package app.ancienttrees.map

import app.ancienttrees.feed.ViewBox
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

/**
 * Signing in crashed the app on Hidde's Samsung (2026-11-17): My trees framed
 * collected trees from Lisbon to Japan and asked MapLibre for a box past the pole.
 */
class SafeBoundsTest {
    @Test fun aBoxPastThePoleIsClampedNotThrown() {
        val b = safeBox(ViewBox(south = -60.0, west = -20.0, north = 130.0, east = 160.0))
        assertEquals(85.0, b.north, 0.0)
        assertEquals(-60.0, b.south, 0.0)
    }

    @Test fun aBoxWiderThanTheWorldIsTheWorld() {
        val b = safeBox(ViewBox(south = 10.0, west = -250.0, north = 40.0, east = 200.0))
        assertEquals(-180.0, b.west, 0.0)
        assertEquals(180.0, b.east, 0.0)
    }

    @Test fun anOrdinaryBoxIsUntouched() {
        val b = safeBox(ViewBox(south = 52.3, west = 4.8, north = 52.4, east = 4.95))
        assertEquals(52.4, b.north, 0.0)
        assertEquals(4.8, b.west, 0.0)
        assertTrue(b.south < b.north)
    }
}
