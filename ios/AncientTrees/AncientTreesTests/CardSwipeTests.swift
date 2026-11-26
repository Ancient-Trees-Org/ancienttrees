// A tapped tree's card closes with a short swipe down (Hidde, 2026-11-24:
// people swiped it and it sprang back, it needed half the card's height).
// The rule is Material 3's: 56 points of drag or a flick of 125 a second.
// Android's MapSheetTest holds the same numbers.

import Testing
import CoreGraphics
@testable import AncientTrees

struct CardSwipeTests {
    @Test func aSlowSixtyPointDragCloses() {
        // The hand check of 2026-11-24: sprang back before, closes now.
        #expect(CardSwipe.closes(drag: 60, velocity: 20))
    }

    @Test func aLightFlickCloses() {
        #expect(CardSwipe.closes(drag: 12, velocity: 300))
    }

    @Test func aNudgeStays() {
        #expect(!CardSwipe.closes(drag: 30, velocity: 50))
    }

    @Test func halfACardIsNoLongerTheBar() {
        // The old rule: the nearest stop, about half a 340 point card.
        #expect(CardSwipe.dragToClose < 100)
    }

    @Test func anUpwardDragNeverCloses() {
        #expect(!CardSwipe.closes(drag: -200, velocity: -900))
    }
}
