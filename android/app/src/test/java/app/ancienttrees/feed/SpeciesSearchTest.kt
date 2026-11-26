package app.ancienttrees.feed

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class SpeciesSearchTest {
    @Test fun accentsAndCaseFold() {
        assertEquals("liskiava", SpeciesSearch.fold(" Liškiava "))
    }

    @Test fun theKindsOfHitInOrder() {
        assertEquals(SpeciesHit.Name, SpeciesSearch.hit("European White Elm", "Ulmus laevis", emptyList(), "elm"))
        assertEquals(SpeciesHit.Latin, SpeciesSearch.hit("European White Elm", "Ulmus laevis", emptyList(), "ulm"))
        val other = SpeciesSearch.hit("European White Elm", "Ulmus laevis", listOf("Orme lisse"), "lis")
        assertTrue(other is SpeciesHit.Other && other.via == "Orme lisse")
        assertEquals(SpeciesHit.Nearly, SpeciesSearch.hit("Sycamore", null, emptyList(), "sycamre"))
        assertNull(SpeciesSearch.hit("Sycamore", null, emptyList(), "oak"))
    }

    // iOS walk 2026-11-25 F9: "oak" left Pedunculate Oak (426 trees) out of Top results.
    @Test fun theSpeciesWithMoreTreesLeadsATie() {
        val counts = mapOf("Adriatic Oak" to 2, "Aleppo Oak" to 4, "Pedunculate Oak" to 426, "Cork Oak" to 30)
        val names = counts.keys.sorted()
        val ranked = rankSpecies(names, "oak", { null }, { emptyList() }, { counts[it] ?: 0 }).map { it.first }
        assertEquals(listOf("Pedunculate Oak", "Cork Oak", "Aleppo Oak", "Adriatic Oak"), ranked)
    }
}
