import XCTest
@testable import AncientTrees

/// The Feed tab's posts from public.feed() (Kit/FeedPosts.swift). Since
/// 2026-11-26 the server also hands posts a reader shared before the judge
/// looked (checked = false, supabase/feed-live.sql): no tree id, no place, no
/// position, the share page as link. One such row in a page must never stop
/// the page from decoding, and it must never show a place, a save or a heart.
final class FeedPostsTests: XCTestCase {

    private let page = """
    [
     {"key":"a4d1c500-1664-48c1-bc8e-7d9d6ee2ad3f","kind":"photo","tree_id":"bhm_001",
      "tree_name":"The Preston Twin","place":"Brighton","url":"/brighton/preston-twin",
      "latitude":50.84,"longitude":-0.15,"photo_url":"https://x/feed/a.jpg","photo_w":800,"photo_h":1067,
      "published_at":"2026-11-26T09:19:14.045353+00:00","author_name":"Milo S.","author_avatar":null,
      "author_id":null,"checked":true},
     {"key":"af38a0d5-0114-4c0e-8b25-336a957b89a8","kind":"tree","tree_id":null,
      "tree_name":"American Sycamore","place":"","url":"/t/?id=af38a0d5-0114-4c0e-8b25-336a957b89a8",
      "latitude":null,"longitude":null,"photo_url":"https://x/shared-sightings/b.jpg","photo_w":null,"photo_h":null,
      "published_at":"2026-11-25T15:06:55.864564+00:00","author_name":"Leafy Linden 4134","author_avatar":null,
      "author_id":null,"checked":false},
     {"key":"tree:ulv_002","kind":"tree","tree_id":"ulv_002","tree_name":"The Conishead Priory Douglas Fir",
      "place":"Ulverston","url":"/ulverston/conishead-priory-douglas-fir","latitude":54.17,"longitude":-3.07,
      "photo_url":"https://x/feed/c.jpg","photo_w":800,"photo_h":1419,
      "published_at":"2026-11-26T08:46:00Z","author_name":null,"author_avatar":null,"author_id":null}
    ]
    """

    private func posts() throws -> [FeedPosts.Post] {
        try JSONDecoder().decode([FeedPosts.Post].self, from: Data(page.utf8))
    }

    func testAPageWithAnUncheckedPostDecodes() throws {
        XCTAssertEqual(try posts().count, 3)
    }

    func testACheckedPhotoKeepsEverything() throws {
        let p = try posts()[0]
        XCTAssertTrue(p.isChecked)
        XCTAssertEqual(p.likeId, "a4d1c500-1664-48c1-bc8e-7d9d6ee2ad3f")
        XCTAssertNil(p.sharedId)
        XCTAssertEqual(FeedPosts.deed(p), "photographed a tree")
    }

    func testAnUncheckedPostShowsNoPlaceNoHeartAndOpensTheSharePage() throws {
        let p = try posts()[1]
        XCTAssertFalse(p.isChecked)
        XCTAssertFalse(p.isNewTree, "no New on the map before the judge looked")
        XCTAssertNil(p.likeId, "no heart on a photograph that is not published")
        XCTAssertEqual(p.sharedId, UUID(uuidString: "af38a0d5-0114-4c0e-8b25-336a957b89a8"))
        XCTAssertEqual(FeedPosts.deed(p), "just shared a tree")
        XCTAssertFalse(FeedPosts.passes(p, .near, following: [], origin: (lat: 52.0, lng: 5.0)),
                       "no position, so never near anybody")
    }

    func testAnOlderAnswerWithoutTheColumnCountsAsChecked() throws {
        let p = try posts()[2]
        XCTAssertNil(p.checked)
        XCTAssertTrue(p.isChecked)
        XCTAssertTrue(p.isNewTree)
        XCTAssertNil(p.likeId, "a tip has no photograph row to like")
    }

    /// Andrea's Varese trees, 2026-11-26: a reader's own new tree, checked,
    /// keyed by its sightings uuid, carries a heart like any photo post.
    func testAReadersOwnNewTreeCarriesAHeart() throws {
        let one = """
        [{"key":"5B0E2C1A-7D7E-4F7A-9C1E-2D3B4A5C6D7E","kind":"tree","tree_id":"vrs_009",
          "tree_name":"The Picnic-Table Cedars","place":"Varese","url":"/varese/picnic-table-cedars",
          "latitude":45.8,"longitude":8.8,"photo_url":"https://x/feed/d.jpg","photo_w":800,"photo_h":600,
          "published_at":"2026-11-26T08:00:00Z","author_name":"Andrea C.","author_avatar":null,
          "author_id":null,"checked":true}]
        """
        let p = try JSONDecoder().decode([FeedPosts.Post].self, from: Data(one.utf8))[0]
        XCTAssertTrue(p.isNewTree)
        XCTAssertEqual(p.likeId, "5b0e2c1a-7d7e-4f7a-9c1e-2d3b4a5c6d7e")
    }

    /// The grid breaks where both columns end level (Hidde, 2026-11-26: "hier
    /// zit een raar gat"), never after a fixed six.
    func testTheGridBreaksWhereTheColumnsAreLevel() {
        // Six tiles: after six the columns differ by 300, after four by 0.
        let h: [Double] = [400, 400, 300, 300, 200, 500, 300, 300]
        XCTAssertEqual(FeedPosts.evenCut(h), 4)
        XCTAssertEqual(FeedPosts.evenCut([300, 300, 300]), 3)
    }
}
