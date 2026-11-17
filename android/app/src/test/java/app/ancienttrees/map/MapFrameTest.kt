package app.ancienttrees.map

import org.junit.Assert.assertEquals
import org.junit.Test

class MapFrameTest {
    @Test fun treesThatFitAreAllKept() {
        val nl = listOf(52.2 to 5.3, 52.4 to 4.9, 51.9 to 4.5)
        assertEquals(nl, MapFrame.densest(nl))
    }

    @Test fun aCollectionAcrossContinentsOpensWhereMostTreesAre() {
        val japan = List(5) { 35.0 + it * 0.1 to 139.0 + it * 0.1 }
        val europe = listOf(52.2 to 5.3, 40.4 to -3.7)
        assertEquals(japan.toSet(), MapFrame.densest(europe + japan).toSet())
    }
}
