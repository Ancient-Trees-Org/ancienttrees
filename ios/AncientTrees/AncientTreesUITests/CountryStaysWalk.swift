import XCTest

/// A COUNTRY YOU PICK STAYS PICKED (2026-11-22, a reader: "helaas wil het land
/// bij mij nog niet blijven staan", after the server took the flag again).
/// The editor filled its name and country in a .task on the Form, and the
/// Country picker pushes its list over that Form, so coming back ran the task
/// again and put the old country back before Save. This picks "Don't show"
/// over a profile that has NL and checks the row still says so on return.
final class CountryStaysWalk: XCTestCase {
    override func setUpWithError() throws {
        continueAfterFailure = false
    }

    func testAPickedCountryStaysOnTheRow() {
        let app = XCUIApplication()
        app.launchArguments = ["-no-location-ask", "-signed-in", "-tab=2", "-profile-edit", "-country=NL"]
        app.launch()

        let row = app.buttons["profile-country"].firstMatch
        XCTAssertTrue(row.waitForExistence(timeout: 30), "the editor shows no Country row")
        XCTAssertTrue(Self.says(row, "Netherlands"), "the row does not start on the saved country")
        row.tapWhenSettled()

        // The list opens on the chosen country (2026-11-26, iOS Settings'
        // Region list), so "Don't show" at its top is a scroll away.
        XCTAssertTrue(app.searchFields["Search countries"].waitForExistence(timeout: 10), "the country list did not open")
        let none = app.buttons.containing(NSPredicate(format: "label CONTAINS %@", "Don't show")).firstMatch
        for _ in 0..<12 where !none.exists { app.swipeDown() }
        XCTAssertTrue(none.waitForExistence(timeout: 5), "the list has no Don't show at its top")
        none.tap()

        XCTAssertTrue(row.waitForExistence(timeout: 10), "the list did not go back to the editor")
        // Long enough for an appearance task to have run again.
        sleep(3)
        XCTAssertTrue(Self.says(row, "Don't show"),
                      "coming back from the list put the old country back: \(row.label) / \(String(describing: row.value))")
    }

    static func says(_ e: XCUIElement, _ text: String) -> Bool {
        e.label.contains(text) || ((e.value as? String)?.contains(text) ?? false)
    }
}
