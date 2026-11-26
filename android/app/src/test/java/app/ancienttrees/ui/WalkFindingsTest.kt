package app.ancienttrees.ui

import app.ancienttrees.account.Profiles
import app.ancienttrees.feed.Photo
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

/** The iPhone walk of 2026-11-25, its findings that were in Android too (WalkFindingsTests.swift). */
class WalkFindingsTest {
    // F3: your own heart on a private profile says You.
    @Test fun yourOwnHeartSaysYou() {
        assertEquals("You", likerLabel(Liker("ABC-1", null, null), "abc-1"))
        assertEquals("Leafy M.", likerLabel(Liker("x", "Leafy M.", null), "abc-1"))
        assertEquals("A visitor", likerLabel(Liker(null, null, null), "abc-1"))
        assertEquals("A visitor", likerLabel(Liker(null, null, null), null))
    }

    // F11: one letter in your avatar, the name's, on My trees and Settings alike.
    @Test fun oneAvatarLetter() {
        assertEquals("L", Profiles.myInitial("Leafy Maple 2525", "apptest@example.com"))
        assertEquals("A", Profiles.myInitial(null, "apptest@example.com"))
        assertEquals("A", Profiles.myInitial("", "apptest@example.com"))
        assertNull(Profiles.myInitial(null, null))
    }

    // F4: Want to visit hides an unsaved tree, so its card closes (MapFilters.keeps).
    @Test fun wantToVisitHidesAnUnsavedTree() {
        val t = app.ancienttrees.feed.Tree(
            id = "ams_001", name = "The plane", species = "London Plane (Platanus x hispanica)", age = null, ageShort = null,
            lat = 52.37, lng = 4.89, city = "Amsterdam", citySlug = "amsterdam", country = "Netherlands",
            neighbourhood = "", access = "", paidEntry = false, transport = "", story = "s",
            storyLatin = emptyList(), howToRecognise = "", url = "/amsterdam/ams_001",
            precision = app.ancienttrees.feed.Precision.APPROXIMATE, photo = null, saves = 0, mini = false,
        )
        assertFalse(MapFilters(favouritesOnly = true).keeps(t, emptySet(), emptySet()))
        assertTrue(MapFilters(favouritesOnly = true).keeps(t, emptySet(), setOf("ams_001")))
    }

    // F6: a lane switch frames that lane's trees; an empty lane leaves the map be.
    @Test fun aLaneFramesItsTrees() {
        assertNull(laneBox(emptyList()))
        val b = laneBox(listOf(52.36 to 4.88, 52.38 to 4.90))!!
        assertTrue(b.south < 52.36 && b.north > 52.38 && b.west < 4.88 && b.east > 4.90)
        val one = laneBox(listOf(52.37 to 4.89))!!
        assertEquals(0.02, one.north - one.south, 1e-9)
    }

    // F8: the country list answers what is typed.
    @Test fun theCountryListSearches() {
        val all = listOf("NL" to "Netherlands", "NZ" to "New Zealand", "NC" to "New Caledonia", "PT" to "Portugal")
        assertEquals(listOf("NZ" to "New Zealand"), matchingCountries(all, "zeal"))
        assertEquals(3, matchingCountries(all, "ne").size)
        assertEquals(listOf("PT" to "Portugal"), matchingCountries(all, "pt"))
        assertEquals(all, matchingCountries(all, ""))
    }

    // F2: an empty credit line from the feed prints no credit at all.
    @Test fun anEmptyCreditLineIsNoCredit() {
        fun photo(line: String?, name: String?, lic: String?) = Photo(
            url = "u", license = lic, attribution = name, attributionShort = null, thumb = null, hero = null,
            creditRequired = true, creditLine = line, creditUrl = null, frame = null,
        )
        assertNull(photo("", "", "Provided by a reader through the Ancient Trees app, all rights reserved").credit)
        assertEquals("Jan · CC BY 4.0", photo(null, "Jan", "CC BY 4.0").credit)
        assertEquals("CC BY 4.0", photo(null, "", "CC BY 4.0").credit)
        assertNotNull(photo("Jan, CC BY", null, null).credit)
    }
}
