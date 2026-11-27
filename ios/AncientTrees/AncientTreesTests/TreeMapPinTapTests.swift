// A tapped pin stays where the finger put it (Hidde, 2026-11-27: "dan verspringt
// de hele kaart"); the map moves only for a pin out of sight or under the card
// (CONVENTIONS.md, "Tapping a pin on a map that has a list in a sheet").
import XCTest
@testable import AncientTrees

final class TreeMapPinTapTests: XCTestCase {
    private let phone = CGSize(width: 402, height: 874)

    func testAPinInTheOpenUpperMapStaysPut() {
        XCTAssertFalse(TreeMap.pinNeedsMove(CGPoint(x: 200, y: 300), in: phone, topCover: 120))
    }

    func testAPinTheCardWouldCoverIsBroughtUp() {
        XCTAssertTrue(TreeMap.pinNeedsMove(CGPoint(x: 200, y: 700), in: phone, topCover: 120))
    }

    func testAPinUnderTheSearchFieldOrOffTheEdgeIsBroughtIn() {
        XCTAssertTrue(TreeMap.pinNeedsMove(CGPoint(x: 200, y: 100), in: phone, topCover: 120))
        XCTAssertTrue(TreeMap.pinNeedsMove(CGPoint(x: 10, y: 300), in: phone, topCover: 120))
        XCTAssertTrue(TreeMap.pinNeedsMove(CGPoint(x: 200, y: -50), in: phone, topCover: 120))
    }

    /// Once the card is up: only a pin in the strip between the controls and
    /// the card counts as seen.
    func testOnceTheCardIsUpOnlyACoveredPinIsHidden() {
        XCTAssertFalse(TreeMap.pinHidden(CGPoint(x: 200, y: 300), in: phone, top: 150, bottom: 380))
        XCTAssertTrue(TreeMap.pinHidden(CGPoint(x: 200, y: 600), in: phone, top: 150, bottom: 380))
        XCTAssertTrue(TreeMap.pinHidden(CGPoint(x: 200, y: 160), in: phone, top: 150, bottom: 380))
    }
}
