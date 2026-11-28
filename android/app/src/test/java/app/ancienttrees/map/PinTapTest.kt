package app.ancienttrees.map

import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

/** The Android twin of TreeMapPinTapTests (iOS). */
class PinTapTest {
    private val w = 402f
    private val h = 874f

    @Test fun aPinInTheOpenUpperMapStaysPut() {
        assertFalse(PinTap.needsMove(200f, 300f, w, h, 120f, 40f))
    }

    @Test fun aPinTheCardWouldCoverIsBroughtUp() {
        assertTrue(PinTap.needsMove(200f, 700f, w, h, 120f, 40f))
    }

    @Test fun aPinUnderTheFieldOrOffTheEdgeIsBroughtIn() {
        assertTrue(PinTap.needsMove(200f, 100f, w, h, 120f, 40f))
        assertTrue(PinTap.needsMove(10f, 300f, w, h, 120f, 40f))
    }

    @Test fun onceTheCardIsUpOnlyACoveredPinIsHidden() {
        assertFalse(PinTap.hidden(200f, 300f, w, h, 150f, 380f, 40f))
        assertTrue(PinTap.hidden(200f, 600f, w, h, 150f, 380f, 40f))
    }
}
