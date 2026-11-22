import XCTest
@testable import AncientTrees

/// Discover's New from visitors row picks what this feed can show
/// (2026-11-22, Hidde: "the feed should always stay available"). On the
/// website, a deploy eleven hours behind left the twelve newest photographs
/// unknown and the row vanished; load() now pages further back, and tiles()
/// must take a tree's newest KNOWN photograph rather than give the tree up
/// because a newer, unknown one came first.
final class NewFromVisitorsTests: XCTestCase {

    private func tree(_ id: String, sightings: [String]) throws -> Tree {
        let shots = sightings.map { s in
            """
            {"url":"https://ancienttrees.app/photos/\(s).jpg","license":"x","attribution":null,
             "width":1600,"height":1200,"thumb":"https://ancienttrees.app/photos/\(s)-500.jpg",
             "hero":"https://ancienttrees.app/photos/\(s).jpg","credit_required":false,
             "attribution_short":null,"credit_line":null,"sighting":"\(s)"}
            """
        }
        let lead = shots.first ?? "null"
        // The feed's `photos` is the whole set, lead included (Tree.shots).
        let rest = shots.count > 1 ? ",\"photos\":[\(shots.joined(separator: ","))]" : ""
        let json = """
        {"id":"\(id)","name":"Tree \(id)","species":"Oak (Quercus sp.)","age":null,
         "age_min":null,"age_max":null,"lat":52.0,"lng":5.0,"city":"Utrecht","city_slug":"utrecht",
         "country":"Netherlands","neighbourhood":null,"access":"","transport":null,
         "precision":"confirmed","best_time":null,"peak":null,"story":"","how_to_recognise":null,
         "url":"","photo":\(lead)\(rest)}
        """
        return try JSONDecoder().decode(Tree.self, from: Data(json.utf8))
    }

    private func row(_ sighting: String, _ tree: String) throws -> NewFromVisitors.Row {
        let json = """
        {"sighting_id":"\(sighting)","tree_id":"\(tree)","published_at":"2026-11-22T10:00:00Z",
         "author_name":null,"author_avatar":null,"author_id":null}
        """
        return try JSONDecoder().decode(NewFromVisitors.Row.self, from: Data(json.utf8))
    }

    private let s1 = "00000000-0000-0000-0000-000000000001"
    private let s2 = "00000000-0000-0000-0000-000000000002"
    private let s3 = "00000000-0000-0000-0000-000000000003"

    /// A newer photograph the feed does not carry yet must not hide the
    /// tree's older one that it does.
    func testAnUnknownNewerPhotoDoesNotHideAKnownOlderOne() throws {
        let a = try tree("a", sightings: [s2])
        let rows = [try row(s1, "a"), try row(s2, "a")]
        let tiles = NewFromVisitors.tiles(rows) { $0 == "a" ? a : nil }
        XCTAssertEqual(tiles.map { $0.row.sighting_id.uuidString.lowercased() }, [s2])
    }

    /// One tile per tree, the newest known first.
    func testOneTilePerTree() throws {
        let a = try tree("a", sightings: [s1, s2])
        let b = try tree("b", sightings: [s3])
        let rows = [try row(s1, "a"), try row(s3, "b"), try row(s2, "a")]
        let tiles = NewFromVisitors.tiles(rows) { ["a": a, "b": b][$0] }
        XCTAssertEqual(tiles.map { $0.tree.id }, ["a", "b"])
        XCTAssertEqual(tiles.first?.row.sighting_id.uuidString.lowercased(), s1)
    }

    /// load()'s test: a photograph counts only when the feed carries it.
    func testKnownNeedsTheFeedsCopy() throws {
        let a = try tree("a", sightings: [s1])
        XCTAssertTrue(NewFromVisitors.known(try row(s1, "a")) { $0 == "a" ? a : nil })
        XCTAssertFalse(NewFromVisitors.known(try row(s2, "a")) { $0 == "a" ? a : nil })
        XCTAssertFalse(NewFromVisitors.known(try row(s1, "zz")) { _ in nil })
    }

    /// Twelve tiles at most, now that load() asks for more rows.
    func testTwelveAtMost() throws {
        var trees: [String: Tree] = [:]
        var rows: [NewFromVisitors.Row] = []
        for i in 1...20 {
            let s = String(format: "00000000-0000-0000-0000-%012d", i)
            trees["t\(i)"] = try tree("t\(i)", sightings: [s])
            rows.append(try row(s, "t\(i)"))
        }
        XCTAssertEqual(NewFromVisitors.tiles(rows) { trees[$0] }.count, 12)
    }
}
