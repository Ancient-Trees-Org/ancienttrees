// Where a tree was opened from, for tree_opened (Kit/TreeSource.swift).

import XCTest
@testable import AncientTrees

@MainActor
final class TreeSourceTests: XCTestCase {

    func testAPageIsTheTabPlusTheScreenUnderTheTree() {
        let path: [Route] = [.city("london"), .tree("lon_001")]
        XCTAssertEqual(TreeSource.page(tab: "map", path: path, route: .tree("lon_001")), "map/city")
        // Straight from the tab's own first screen: the tab alone.
        XCTAssertEqual(TreeSource.page(tab: "discover", path: [.tree("lon_001")], route: .tree("lon_001")), "discover")
        // From another tree's page.
        let deeper: [Route] = [.collection("kings"), .tree("a"), .tree("b")]
        XCTAssertEqual(TreeSource.page(tab: "discover", path: deeper, route: .tree("b")), "discover/tree")
    }

    func testATapNamesTheTreeOnceAndOnlyJustAfter() {
        TreeSource.mark("discover/best")
        XCTAssertEqual(TreeSource.take(page: "discover"), "discover/best")
        // Read once: the next tree opened some other way keeps its page.
        XCTAssertEqual(TreeSource.take(page: "map"), "map")
    }

    func testARouteKindIsAWord() {
        XCTAssertEqual(TreeSource.kind(.species("Pedunculate Oak")), "species")
        XCTAssertEqual(TreeSource.kind(.index(.islands)), "index")
    }
}
