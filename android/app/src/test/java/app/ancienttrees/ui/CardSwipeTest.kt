package app.ancienttrees.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

/** A tapped tree's card closes with a short swipe down; the iPhone's CardSwipeTests hold the same numbers. */
class CardSwipeTest {
    @Test fun aSlowSixtyDpDragCloses() = assertTrue(CardSwipe.closes(dragDp = 60f, velocityDp = 20f))

    @Test fun aLightFlickCloses() = assertTrue(CardSwipe.closes(dragDp = 12f, velocityDp = 300f))

    @Test fun aNudgeStays() = assertFalse(CardSwipe.closes(dragDp = 30f, velocityDp = 50f))

    @Test fun anUpwardDragNeverCloses() = assertFalse(CardSwipe.closes(dragDp = -200f, velocityDp = -900f))

    @Test fun sameNumbersAsTheIphone() {
        assertEquals(56f, CardSwipe.DRAG_TO_CLOSE_DP)
        assertEquals(125f, CardSwipe.FLICK_TO_CLOSE_DP)
    }
}
