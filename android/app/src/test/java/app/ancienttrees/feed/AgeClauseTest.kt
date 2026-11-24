package app.ancienttrees.feed

import org.junit.Assert.assertEquals
import org.junit.Test

/** AgeClauseTests.swift: a thousands separator is not a clause break (report 1000138, 2026-11-24). */
class AgeClauseTest {
    @Test
    fun aThousandsSeparatorIsNotAClauseBreak() {
        assertEquals("about 1,000 years", Tree.firstAgeClause("about 1,000 years, by a reader's estimate"))
        assertEquals("roughly 2,600 years", Tree.firstAgeClause("roughly 2,600 years (temple tradition)"))
        assertEquals("over 1,000 years", Tree.firstAgeClause("over 1,000 years"))
    }

    @Test
    fun theClauseStillEndsWhereItDid() {
        assertEquals("roughly 135 years", Tree.firstAgeClause("roughly 135 years, planted around 1889"))
        assertEquals("disputed", Tree.firstAgeClause("disputed, 1,300 to 5,000 years"))
        assertEquals("over 2,000 years by one source", Tree.firstAgeClause("over 2,000 years by one source; not dated"))
        assertEquals("about 300 years", Tree.firstAgeClause("about 300 years"))
    }
}
