// The feed's credit_line is the answer for both surfaces. An empty line means
// "no name to print" (a reader's photograph, whose name the server gives under
// the photo), and the website then prints nothing. The app treated "" as a
// missing field and joined an empty name with the licence sentence, so the
// tree page read "Photo:  · Provided by a reader through the Ancient Trees
// app, all rights reserved" (walk before build 42, 2026-11-25).
import XCTest
@testable import AncientTrees

final class CreditLineTests: XCTestCase {
    private func photo(_ extra: String) -> Photo {
        let json = """
        {"url":"https://example.org/a.jpg","license":"Provided by a reader through the Ancient Trees app, all rights reserved",
         "attribution":"","attribution_short":"","credit_required":true\(extra)}
        """
        return try! JSONDecoder().decode(Photo.self, from: Data(json.utf8))
    }

    func testAnEmptyLineFromTheFeedPrintsNoCredit() {
        XCTAssertNil(Photos.credit(photo(#","credit_line":"""#)))
    }

    func testTheFeedsLineIsPrintedAsItIs() {
        XCTAssertEqual(Photos.credit(photo(#","credit_line":"Nikolau (CC BY-SA 3.0)""#)), "Nikolau (CC BY-SA 3.0)")
    }

    func testAnOlderSnapshotNeverStartsWithAnEmptyName() {
        let line = Photos.credit(photo(""))
        XCTAssertEqual(line, "Provided by a reader through the Ancient Trees app, all rights reserved")
        XCTAssertFalse(line?.hasPrefix(" ") ?? false)
    }
}
