package app.ancienttrees.map

/**
 * A TAPPED PIN STAYS WHERE THE FINGER PUT IT (Hidde, 2026-11-27: "dan verspringt
 * de hele kaart"), the same rule as TreeMap.pinNeedsMove / pinHidden on iOS
 * (CONVENTIONS.md "Tapping a pin on a map that has a list in a sheet"): the map
 * moves only for a pin out of sight or under the card. Points in pixels, 40 dp
 * of air given in the same unit. Pure, for PinTapTest.
 */
object PinTap {
    /** Before the card is up: the card will cover the lower 45% of the map. */
    fun needsMove(x: Float, y: Float, width: Float, height: Float, top: Float, air: Float): Boolean {
        val bottom = height * 0.55f
        return x < air || x > width - air || y < top + air || y > bottom
    }

    /** Once the card is up: outside the strip between the controls and the card. */
    fun hidden(x: Float, y: Float, width: Float, height: Float, top: Float, bottom: Float, air: Float): Boolean =
        x < air || x > width - air || y < top + air || y > height - bottom - air
}
