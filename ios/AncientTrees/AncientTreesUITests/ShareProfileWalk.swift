import XCTest

/// SHARE YOUR PROFILE ANSWERS (Hidde, 2026-11-26, on his phone: "als ik bij
/// Find People op Share Your Profile klik, die knop helemaal niet werkt").
/// A public profile: the row opens the system share sheet.
final class ShareProfileWalk: XCTestCase {
    override func setUpWithError() throws { continueAfterFailure = false }

    func testShareYourProfileOpensTheShareSheet() {
        let app = XCUIApplication()
        app.launchArguments = ["-no-location-ask", "-no-cover", "-signed-in", "-public=on", "-tab=4", "-open=people:all"]
        app.launch()
        let row = app.descendants(matching: .any)["people-share"].firstMatch
        XCTAssertTrue(row.waitForExistence(timeout: 30), "no Share your profile row")
        row.tap()
        let sheet = app.otherElements["ActivityListView"].firstMatch
        let copy = app.buttons["Copy"].firstMatch
        XCTAssertTrue(sheet.waitForExistence(timeout: 8) || copy.waitForExistence(timeout: 2),
                      "tapping Share your profile opened nothing")
    }
}
