package app.ancienttrees.feed

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Test

/** A tree you added is labelled with a place only when one of ours stands close by (report 1488); the iPhone's CollectView.placeOfYourTree uses the same 3 km. */
class MyTreesPlaceTest {
    @Test fun fifteenKilometresOffIsNoPlace() = assertNull(CollectRules.placeLabel("Westonbirt Arboretum", 15.0))

    @Test fun aTreeOfOursCloseByNamesThePlace() = assertEquals("Tortworth", CollectRules.placeLabel("Tortworth", 0.03))

    @Test fun aTreeOfOursByIdIsAlwaysItsOwnPlace() = assertEquals("Tortworth", CollectRules.placeLabel("Tortworth", null))

    @Test fun theSameNumberAsTheIphone() = assertEquals(3.0, CollectRules.PLACE_LABEL_KM, 0.0)
}
