import XCTest

/// BACK LANDS WHERE YOU WERE (Hidde, 2026-11-26, on his phone: from the Feed
/// to a profile and back "kom ik niet op het juiste punt in de feed terug.
/// Iets te laag gescrolld", and the same after a See all: "zorgen dat, als
/// mensen op Vorige klikken, ze ook daadwerkelijk op de plek komen waar ze net
/// waren"). Scroll, open something, go back, and the same tile must stand where
/// it stood, to within two points.
final class BackKeepsPlaceWalk: XCTestCase {
    override func setUpWithError() throws {
        continueAfterFailure = false
        XCUIDevice.shared.orientation = .portrait
    }

    private func launch(_ args: [String]) -> XCUIApplication {
        let app = XCUIApplication()
        app.launchArguments = ["-no-location-ask", "-no-cover", "-at=52.0907,5.1214"] + args
        app.launch()
        return app
    }

    /// The first tile fully on screen, below the header area.
    private func anchor(_ app: XCUIApplication, _ id: String) -> XCUIElement? {
        let screen = app.windows.firstMatch.frame
        let tiles = app.descendants(matching: .any).matching(identifier: id).allElementsBoundByIndex
        // A tile whose top is in view, below the header and above the bar
        // (a big post is taller than half the screen, so its bottom may not be).
        return tiles.first { $0.exists && $0.frame.minY > 100 && $0.frame.minY < screen.maxY - 90 }
    }

    private func back(_ app: XCUIApplication) {
        let bar = app.navigationBars.buttons.firstMatch
        if bar.waitForExistence(timeout: 5) { bar.tap() } else {
            // A page with our own back button.
            app.buttons["Back"].firstMatch.tap()
        }
    }

    func testBackFromATreeKeepsTheFeedWhereItWas() { walk([], "feed-tile") }

    func testBackFromATreeKeepsTheBigFeedWhereItWas() { walk(["-feedbig"], "feed-name") }

    private func walk(_ extra: [String], _ id: String) {
        let app = launch(["-tab=4"] + extra)
        XCTAssertTrue(app.descendants(matching: .any)[id].firstMatch.waitForExistence(timeout: 30))
        let list = app.descendants(matching: .any)["feed"].firstMatch
        list.swipeUp(); list.swipeUp()
        sleep(2)
        guard let a = anchor(app, id) else {
            let frames = app.descendants(matching: .any).matching(identifier: id).allElementsBoundByIndex
                .prefix(8).map { "\(Int($0.frame.minY))" }.joined(separator: ",")
            return XCTFail("no tile in view after scrolling; tops: \(frames)")
        }
        let label = a.label, before = a.frame.minY
        XCTAssertFalse(label.isEmpty, "the tile has no label to find it again by")
        a.tap()
        sleep(2)
        back(app)
        sleep(2)
        let again = app.descendants(matching: .any).matching(identifier: id)
            .matching(NSPredicate(format: "label == %@", label)).firstMatch
        XCTAssertTrue(again.waitForExistence(timeout: 5), "the tile is gone after Back")
        XCTAssertEqual(again.frame.minY, before, accuracy: 2,
                       "Back moved the Feed: the tile stood at \(before), now at \(again.frame.minY)")
    }
}
