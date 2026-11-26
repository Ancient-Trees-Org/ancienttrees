import XCTest

/// Somebody's profile, the two things Hidde found on his phone (2026-11-26):
/// a tap on the NAME opened their followers (the count's tap area lay over it),
/// and the AMBASSADOR badge opened nothing instead of their place.
final class PersonProfileWalk: XCTestCase {
    override func setUpWithError() throws { continueAfterFailure = false }

    private func launch() -> XCUIApplication {
        let app = XCUIApplication()
        app.launchArguments = ["-no-location-ask", "-no-cover", "-signed-in", "-people-demo", "-tab=1",
                               "-open=person:00000000-0000-0000-0000-0000000000a1"]
        app.launch()
        return app
    }

    func testTheNameOpensNothing() {
        let app = launch()
        let name = app.staticTexts["person-name"].firstMatch
        XCTAssertTrue(name.waitForExistence(timeout: 30), "no name on the profile")
        name.tap()
        sleep(2)
        XCTAssertFalse(app.navigationBars["Followers"].exists, "a tap on the name opened the followers")
        XCTAssertTrue(name.exists, "a tap on the name left the profile")
    }

    func testTheAmbassadorBadgeOpensThePlace() {
        let app = launch()
        let badge = app.descendants(matching: .any)["ambassador-badge"].firstMatch
        XCTAssertTrue(badge.waitForExistence(timeout: 30), "no ambassador badge on the demo profile")
        badge.tap()
        // The place opens on the map tab: the profile is no longer on screen.
        let name = app.staticTexts["person-name"].firstMatch
        let gone = NSPredicate(format: "exists == false")
        expectation(for: gone, evaluatedWith: name)
        waitForExpectations(timeout: 10)
    }
}
