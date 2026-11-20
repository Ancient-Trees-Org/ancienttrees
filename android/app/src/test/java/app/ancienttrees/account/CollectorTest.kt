package app.ancienttrees.account

import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.Date

class CollectorTest {

    private val noon = Date(1_762_776_000_000) // 2025-11-10 12:00 UTC

    @Test fun theRowCarriesTheIphonesKeysAndWhereThePhoneStood() {
        val r = Collector.row("u1", "ID-1", "lis_001", "The Ajuda Dragon Tree", 38.7, -9.2, "u1/ID-1.jpg", noon)
        assertEquals(
            setOf("user_id", "id", "tree_id", "name", "note", "lat", "lng", "taken_at", "status", "updated_at", "shared", "photo", "client"),
            r.keys().asSequence().toSet(),
        )
        assertEquals("android", r.getString("client"))
        assertEquals("mine", r.getString("status"))
        assertEquals(true, r.getBoolean("shared"))
        assertEquals(38.7, r.getDouble("lat"), 0.0)
        assertEquals("u1/ID-1.jpg", r.getString("photo"))
        assertEquals("2025-11-10T12:00:00Z", r.getString("taken_at"))
    }

    // Audit, 2026-11-20: a library photo without a date was filed at the moment it
    // was picked, unmarked, so a summer photo picked in November read as autumn.
    @Test fun aPickedMomentIsMarkedAsAFallback() {
        val july = Date(1_752_500_000_000)
        assertEquals(Collector.FALLBACK_DATE, Collector.dated(null, fromCamera = false, now = noon).basis)
        assertEquals(noon, Collector.dated(null, fromCamera = false, now = noon).date)
        assertEquals(Collector.PHOTO_DATE, Collector.dated(null, fromCamera = true, now = noon).basis)
        assertEquals(Collector.PHOTO_DATE, Collector.dated(july, fromCamera = false, now = noon).basis)
        assertEquals(july, Collector.dated(july, fromCamera = false, now = noon).date)
    }

    @Test fun theRowSaysWhatItsDateRestsOnAndEachExtrasMonth() {
        val r = Collector.row("u1", "ID-1", null, "A tree", 38.7, -9.2, "u1/ID-1.jpg", noon,
            extras = listOf("u1/ID-1-extra-1.jpg", "u1/ID-1-extra-2.jpg"),
            takenBasis = Collector.FALLBACK_DATE, extraMonths = listOf(7, null))
        assertEquals("fallback", r.getString("taken_basis"))
        val months = r.getJSONArray("extra_photo_months")
        assertEquals(2, months.length())
        assertEquals(7, months.getInt(0))
        assertEquals(true, months.isNull(1))
        // No months known: the key stays off, so an older database takes the row.
        val bare = Collector.row("u1", "ID-2", null, "A tree", 38.7, -9.2, null, noon,
            extras = listOf("u1/ID-2-extra-1.jpg"), extraMonths = listOf(null))
        assertEquals(false, bare.has("extra_photo_months"))
        assertEquals(false, bare.has("taken_basis"))
    }

    @Test fun aMonthIsOneToTwelve() {
        assertEquals(11, Collector.month(noon))
        assertEquals(null, Collector.month(null))
    }

    @Test fun theVisitIsADay() {
        assertEquals(10, Collector.day(noon).length)
    }
}
