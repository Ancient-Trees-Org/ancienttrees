// Switching light and dark with the map open left it without a single pin until
// a pan (walk before build 42, 2026-11-25; seen twice on iOS 18.6). The new
// style carries none of our layers; the reload branch cleared only the drawn
// keys, so the same tree array still looked drawn and nothing was set again.
// TreeMap.DrawnTrees.forget() now clears everything that decides a redraw.

import Testing
import Foundation
@testable import AncientTrees

@MainActor
struct AStyleReloadDrawsTheTreesAgain {

    private static func tree(_ id: String) -> Tree {
        let json = """
        {"id":"\(id)","name":"The Oak",
         "species":"Pedunculate Oak (Quercus robur)","age":null,
         "age_min":null,"age_max":null,"lat":52.37,"lng":4.89,
         "city":"Amsterdam","city_slug":"amsterdam","country":"Netherlands",
         "neighbourhood":null,"access":"","transport":null,
         "precision":"confirmed","best_time":null,"peak":null,"story":"",
         "how_to_recognise":null,"url":"","photo":null}
        """
        return try! JSONDecoder().decode(Tree.self, from: Data(json.utf8))
    }

    @Test func theSameArrayAfterAReloadIsDrawnAgain() {
        let trees = [Self.tree("a"), Self.tree("b")]
        var drawn = TreeMap.DrawnTrees()
        let first = drawn.update(trees, collected: [], favourites: [])
        // The sheet's 80 updates a pin tap: nothing to do.
        let again = drawn.update(trees, collected: [], favourites: [])
        // Light to dark: the style reloads and our layers are gone.
        drawn.forget()
        let afterReload = drawn.update(trees, collected: [], favourites: [])
        #expect(first)
        #expect(!again)
        #expect(afterReload)
    }

    @Test func aNewButIdenticalArrayDoesNotRedraw() {
        var drawn = TreeMap.DrawnTrees()
        let first = drawn.update([Self.tree("a")], collected: [], favourites: [])
        let second = drawn.update([Self.tree("a")], collected: [], favourites: [])
        #expect(first)
        #expect(!second)
    }

    @Test func collectingATreeRedraws() {
        let trees = [Self.tree("a")]
        var drawn = TreeMap.DrawnTrees()
        let first = drawn.update(trees, collected: [], favourites: [])
        let collected = drawn.update(trees, collected: ["a"], favourites: [])
        #expect(first)
        #expect(collected)
    }
}
