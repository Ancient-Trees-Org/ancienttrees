import XCTest

/// PULL TO REFRESH LOADS (Hidde, 2026-11-26, on his phone: "Refreshing the
/// feed on feed: the feed did not load. Pull down again to try again"). The
/// refresh emptied the list first, SwiftUI then ended the refresh's own task,
/// the request was cut off, and a cut-off request counted as a failure. Pull
/// down twice, as he did, and the posts must still be there with no error line.
final class FeedRefreshWalk: XCTestCase {
    override func setUpWithError() throws {
        continueAfterFailure = false
        XCUIDevice.shared.orientation = .portrait
    }

    private func pull(_ app: XCUIApplication) {
        let w = app.windows.firstMatch
        let from = w.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0.3))
        let to = w.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0.85))
        from.press(forDuration: 0.05, thenDragTo: to)
    }

    private func walk(_ extra: [String], _ id: String) {
        let app = XCUIApplication()
        app.launchArguments = ["-no-location-ask", "-no-cover", "-at=52.0907,5.1214", "-tab=4"] + extra
        app.launch()
        let tile = app.descendants(matching: .any)[id].firstMatch
        XCTAssertTrue(tile.waitForExistence(timeout: 30), "the Feed shows no posts")
        for round in 1...2 {
            pull(app)
            sleep(6)
            let failed = app.staticTexts.containing(NSPredicate(format: "label CONTAINS %@", "did not load")).firstMatch
            XCTAssertFalse(failed.exists, "refresh \(round) said the feed did not load")
            XCTAssertTrue(tile.waitForExistence(timeout: 15), "refresh \(round) left the Feed empty")
        }
    }

    func testPullToRefreshLoadsTheGrid() { walk([], "feed-tile") }

    func testPullToRefreshLoadsTheBigFeed() { walk(["-feedbig"], "feed-name") }
}
