package app.ancienttrees.ui

import android.content.ComponentCallbacks2
import org.junit.Assert.assertEquals
import org.junit.Test

/** The photographs give memory back, so Android has less reason to end the app (RemoteImage.kt). */
class ImageMemoryTest {
    private val mb = 1024L * 1024

    @Test fun anEighthOfTheHeapAtMost64() {
        assertEquals((24 * mb).toInt(), memoryBudget(192 * mb))
        assertEquals((64 * mb).toInt(), memoryBudget(512 * mb))
        assertEquals((8 * mb).toInt(), memoryBudget(32 * mb))
    }

    @Test fun outOfSightNothingIsKept() {
        assertEquals(0, keepAfterTrim(ComponentCallbacks2.TRIM_MEMORY_UI_HIDDEN, 1000))
        assertEquals(0, keepAfterTrim(ComponentCallbacks2.TRIM_MEMORY_BACKGROUND, 1000))
        assertEquals(500, keepAfterTrim(ComponentCallbacks2.TRIM_MEMORY_RUNNING_LOW, 1000))
        assertEquals(1000, keepAfterTrim(ComponentCallbacks2.TRIM_MEMORY_RUNNING_MODERATE, 1000))
    }
}
