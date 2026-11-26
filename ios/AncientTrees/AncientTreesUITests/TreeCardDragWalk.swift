import XCTest

/// A TREE CARD DRAGGED DOWN CLOSES AND THE MENU STAYS (Hidde, 2026-11-26: "als
/// ik naar de map ga, ik klik op een boom en ik scroll die weg naar beneden,
/// dan gaat het hele menu weg"; "ja, bouw dat"). The bar stop, where the tab
/// bar steps away, is the results list's own (Airbnb); a chosen tree dragged
/// down goes back to the list, as Google Maps and Airbnb do.
final class TreeCardDragWalk: XCTestCase {
    override func setUpWithError() throws {
        continueAfterFailure = false
        XCUIDevice.shared.orientation = .portrait
    }

    func testDraggingATreeCardDownKeepsTheTabBar() {
        let app = XCUIApplication()
        app.launchArguments = ["-no-location-ask", "-no-cover", "-at=52.3676,4.9041", "-tab=0", "-select=ams_001"]
        app.launch()
        let card = app.buttons["place-card"]
        XCTAssertTrue(card.waitForExistence(timeout: 30), "no tree card on the map")
        let map = app.descendants(matching: .any)["tab-map"].firstMatch
        XCTAssertTrue(map.waitForExistence(timeout: 5))
        // Drag the card all the way down, past its lowest stop.
        let w = app.windows.firstMatch
        let from = card.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0.05))
        from.press(forDuration: 0.1, thenDragTo: w.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0.99)))
        sleep(2)
        XCTAssertFalse(card.exists && card.isHittable, "the tree card is still open after dragging it down")
        XCTAssertTrue(map.exists && map.isHittable, "dragging a tree card down took the tab bar away")
    }
}
