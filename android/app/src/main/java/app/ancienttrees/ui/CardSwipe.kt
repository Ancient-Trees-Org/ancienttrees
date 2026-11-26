package app.ancienttrees.ui

/**
 * When a downward swipe on a tapped tree's card closes it (Hidde, 2026-11-24:
 * the card sprang back unless dragged half its height, "zowel ios als android
 * overal"). Material 3's sheet lets go after 56 dp of drag or a 125 dp/s flick
 * (BottomSheetDefaults); BottomSheet.swift's CardSwipe carries the same numbers.
 * Its own object so CardSwipeTest holds it.
 */
object CardSwipe {
    const val DRAG_TO_CLOSE_DP = 56f
    const val FLICK_TO_CLOSE_DP = 125f

    fun closes(dragDp: Float, velocityDp: Float): Boolean =
        dragDp > DRAG_TO_CLOSE_DP || velocityDp > FLICK_TO_CLOSE_DP
}
