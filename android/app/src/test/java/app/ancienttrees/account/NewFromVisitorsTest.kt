package app.ancienttrees.account

import app.ancienttrees.feed.Photo
import app.ancienttrees.feed.Precision
import app.ancienttrees.feed.Tree
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

/**
 * Discover's New from visitors row picks what this feed can show (2026-11-22, Hidde: "the
 * feed should always stay available"). The ios NewFromVisitorsTests, case for case.
 */
class NewFromVisitorsTest {

    private fun shot(s: String) = Photo("u/$s", null, null, null, null, null, null, null, null, null, sighting = s)

    private fun tree(id: String, vararg sightings: String) = Tree(
        id = id, name = id, species = "Oak (Quercus sp.)", age = null, ageShort = null, ageMin = null,
        lat = 52.0, lng = 5.0, city = "Utrecht", citySlug = "utrecht", country = "Netherlands",
        neighbourhood = "", access = "", paidEntry = false, transport = "", story = "s",
        storyLatin = emptyList(), howToRecognise = "", url = "/utrecht/$id", precision = Precision.CONFIRMED,
        photo = sightings.firstOrNull()?.let(::shot), photos = sightings.map(::shot),
        saves = 0, mini = false, bestMonths = emptyList(),
    )

    private fun row(s: String, tree: String) = NewFromVisitors.Row(s, tree, "2026-11-22T10:00:00Z", null, null, null)

    @Test fun anUnknownNewerPhotoDoesNotHideAKnownOlderOne() {
        val a = tree("a", "s2")
        val tiles = NewFromVisitors.tiles(listOf(row("s1", "a"), row("s2", "a"))) { if (it == "a") a else null }
        assertEquals(listOf("s2"), tiles.map { it.first.sightingId })
    }

    @Test fun oneTilePerTree() {
        val trees = mapOf("a" to tree("a", "s1", "s2"), "b" to tree("b", "s3"))
        val tiles = NewFromVisitors.tiles(listOf(row("s1", "a"), row("s3", "b"), row("s2", "a"))) { trees[it] }
        assertEquals(listOf("a", "b"), tiles.map { it.second.id })
        assertEquals("s1", tiles.first().first.sightingId)
    }

    @Test fun knownNeedsTheFeedsCopy() {
        val a = tree("a", "s1")
        assertTrue(NewFromVisitors.known(row("s1", "a")) { if (it == "a") a else null })
        assertFalse(NewFromVisitors.known(row("s2", "a")) { if (it == "a") a else null })
        assertFalse(NewFromVisitors.known(row("s1", "zz")) { null })
    }

    @Test fun twelveAtMost() {
        val trees = (1..20).associate { "t$it" to tree("t$it", "s$it") }
        val rows = (1..20).map { row("s$it", "t$it") }
        assertEquals(12, NewFromVisitors.tiles(rows) { trees[it] }.size)
    }
}
