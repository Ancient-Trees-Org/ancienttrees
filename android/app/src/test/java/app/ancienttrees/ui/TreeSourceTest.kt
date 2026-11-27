package app.ancienttrees.ui

import org.junit.Assert.assertEquals
import org.junit.Test

/** Where a tree was opened from, in the iPhone's words (TreeSourceTests.swift). */
class TreeSourceTest {

    @Test fun aPageIsTheTabPlusThePageUnderTheTree() {
        val path = listOf(Page.Discover(DiscoverPage.Collection("kings")), Page.TreePage("a"))
        assertEquals("discover/collection", TreeSource.page(1, path))
        // Straight from the tab's own first screen: the tab alone.
        assertEquals("feed", TreeSource.page(4, listOf(Page.TreePage("a"))))
        assertEquals("my-trees/tree", TreeSource.page(2, listOf(Page.TreePage("a"), Page.TreePage("b"))))
    }

    @Test fun aTapNamesTheTreeOnceAndOnlyJustAfter() {
        TreeSource.mark("discover/best")
        assertEquals("discover/best", TreeSource.take("discover"))
        // Read once: the next tree opened some other way keeps its page.
        assertEquals("map", TreeSource.take("map"))
    }
}
