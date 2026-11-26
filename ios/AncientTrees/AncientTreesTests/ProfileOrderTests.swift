import XCTest
@testable import AncientTrees

/// A PROFILE RUNS NEWEST FIRST (Hidde, 2026-11-26: "je laatstgenomen foto als
/// eerste getoond wordt en dat die dan terug in de tijd loopt"): our trees and
/// their own trees in one order, the server's, with no dates on the phone.
@MainActor
final class ProfileOrderTests: XCTestCase {
    private func own(_ id: String) -> Profiles.OwnTree {
        try! JSONDecoder().decode(Profiles.OwnTree.self, from: Data("{\"id\":\"\(id)\"}".utf8))
    }

    func testOurTreesAndTheirOwnMixNewestFirst() {
        let a = "AAAAAAAA-0000-0000-0000-000000000001"
        let items = Profiles.collected(trees: ["lon_001", "par_002"], own: [own(a)],
                                       recent: ["o:" + a.lowercased(), "t:par_002", "t:lon_001"])
        XCTAssertEqual(items.map(\.id), ["o:" + a.lowercased(), "t:par_002", "t:lon_001"])
    }

    func testWithoutAnOrderOurTreesComeFirstAsBefore() {
        let a = "AAAAAAAA-0000-0000-0000-000000000001"
        let items = Profiles.collected(trees: ["lon_001"], own: [own(a)], recent: nil)
        XCTAssertEqual(items.map(\.id), ["t:lon_001", "o:" + a.lowercased()])
    }

    func testATileTheOrderDoesNotNameGoesLast() {
        let items = Profiles.collected(trees: ["lon_001", "par_002"], own: [], recent: ["t:par_002"])
        XCTAssertEqual(items.map(\.id), ["t:par_002", "t:lon_001"])
    }
}
