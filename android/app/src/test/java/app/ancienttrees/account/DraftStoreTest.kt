package app.ancienttrees.account

import org.junit.Assert.assertArrayEquals
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Rule
import org.junit.Test
import org.junit.rules.TemporaryFolder
import java.util.Date

/** A draft open when Android ends the app comes back at the next start (DraftStore). */
class DraftStoreTest {
    @get:Rule val tmp = TemporaryFolder()

    private val now = 1_800_000_000_000L
    private fun draft() = Collector.Draft(
        id = "d1", name = "The big lime", lat = 52.1, lng = 5.3,
        jpeg = byteArrayOf(1, 2, 3), extras = listOf(byteArrayOf(4), byteArrayOf(5, 6)),
        taken = Date(now - 5_000), fixNote = "GPS 8 m", place = "Baarn",
        note = "Planted by my grandfather", species = "Lime (Tilia sp.)", age = "200",
        girthCm = 420, takenBasis = Collector.PHOTO_DATE, extraMonths = listOf(5, null),
    )

    @Test fun aDraftSurvivesTheApp() {
        val dir = tmp.root
        DraftStore.save(dir, draft(), now)
        val back = DraftStore.load(dir, now + 60_000)!!
        val d = draft()
        assertEquals(d.copy(jpeg = null, extras = emptyList()), back.copy(jpeg = null, extras = emptyList()))
        assertArrayEquals(d.jpeg, back.jpeg)
        assertEquals(2, back.extras.size)
        assertArrayEquals(byteArrayOf(5, 6), back.extras[1])
        assertEquals(listOf(5, null), back.extraMonths)
    }

    @Test fun fewerExtrasLeaveNoOldPhotograph() {
        val dir = tmp.root
        DraftStore.save(dir, draft(), now)
        DraftStore.save(dir, draft().copy(extras = listOf(byteArrayOf(9)), extraMonths = listOf(1)), now)
        val back = DraftStore.load(dir, now)!!
        assertEquals(1, back.extras.size)
        assertFalse(java.io.File(DraftStore.dir(dir), "extra-1.jpg").exists())
    }

    @Test fun aDayOldDraftIsThrownAway() {
        val dir = tmp.root
        DraftStore.save(dir, draft(), now)
        assertNull(DraftStore.load(dir, now + DraftStore.KEEP_MS))
        assertFalse(DraftStore.dir(dir).exists())
    }

    @Test fun clearedMeansGone() {
        val dir = tmp.root
        DraftStore.save(dir, draft(), now)
        DraftStore.clear(dir)
        assertNull(DraftStore.load(dir, now))
    }
}
