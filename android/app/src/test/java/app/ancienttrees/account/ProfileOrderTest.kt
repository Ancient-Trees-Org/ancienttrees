package app.ancienttrees.account

import org.junit.Assert.assertEquals
import org.junit.Test

/** A profile runs newest first (Hidde, 2026-11-26); ProfileOrderTests.swift on the iPhone. */
class ProfileOrderTest {
    @Test fun ourTreesAndTheirOwnMixNewestFirst() {
        val keys = listOf("t:lon_001", "t:par_002", "o:aaaa")
        assertEquals(listOf(2, 1, 0), Profiles.collectedOrder(keys, listOf("o:AAAA", "t:par_002", "t:lon_001")))
    }

    @Test fun withoutAnOrderTheyStayAsGiven() {
        assertEquals(listOf(0, 1), Profiles.collectedOrder(listOf("t:a", "o:b"), null))
    }

    @Test fun aTileTheOrderDoesNotNameGoesLast() {
        assertEquals(listOf(1, 0), Profiles.collectedOrder(listOf("t:a", "t:b"), listOf("t:b")))
    }
}
