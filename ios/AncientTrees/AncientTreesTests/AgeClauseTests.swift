import XCTest
@testable import AncientTrees

/// The tree page's Age field shows the age sentence's first clause. A reader
/// saw "about 1" for a plane of about 1,000 years (report 1000138,
/// 2026-11-24): a thousands separator was taken for a clause break.
final class AgeClauseTests: XCTestCase {

    func testAThousandsSeparatorIsNotAClauseBreak() {
        XCTAssertEqual(Tree.firstAgeClause(of: "about 1,000 years, by a reader's estimate"), "about 1,000 years")
        XCTAssertEqual(Tree.firstAgeClause(of: "roughly 2,600 years (temple tradition)"), "roughly 2,600 years")
        XCTAssertEqual(Tree.firstAgeClause(of: "over 1,000 years"), "over 1,000 years")
    }

    func testTheClauseStillEndsWhereItDid() {
        XCTAssertEqual(Tree.firstAgeClause(of: "roughly 135 years, planted around 1889"), "roughly 135 years")
        XCTAssertEqual(Tree.firstAgeClause(of: "disputed, 1,300 to 5,000 years"), "disputed")
        XCTAssertEqual(Tree.firstAgeClause(of: "over 2,000 years by one source; not dated"), "over 2,000 years by one source")
        XCTAssertEqual(Tree.firstAgeClause(of: "about 300 years"), "about 300 years")
    }
}
