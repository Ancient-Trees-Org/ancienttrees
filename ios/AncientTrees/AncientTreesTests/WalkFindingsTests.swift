// The release walk before build 42 (2026-11-25, out/tmp/walk-ios.md) found
// these; each test was red before its fix.
import XCTest
import MapKit
@testable import AncientTrees

final class WalkFindingsTests: XCTestCase {
    private func tree(_ id: String, lat: Double = 51.5, lng: Double = -0.1) -> Tree {
        let json = """
        {"id":"\(id)","name":"\(id)","species":"Pedunculate Oak (Quercus robur)","age":null,
         "age_min":null,"age_max":null,"lat":\(lat),"lng":\(lng),
         "city":"London","city_slug":"london","country":"United Kingdom","neighbourhood":null,
         "access":"","transport":null,"precision":"confirmed","best_time":null,
         "peak":null,"story":"","how_to_recognise":null,"url":"","photo":null}
        """
        return try! JSONDecoder().decode(Tree.self, from: Data(json.utf8))
    }

    // F3: a private account saw its own heart as "A visitor".
    func testYourOwnHeartSaysYou() {
        let mine = PhotoLikersList.Row(user_id: "ABC-1", display_name: "Leafy Maple", avatar_url: nil, created_at: "t")
        XCTAssertEqual(PhotoLikersList.label(mine, me: "abc-1"), "You")
        let other = PhotoLikersList.Row(user_id: nil, display_name: nil, avatar_url: nil, created_at: "u")
        XCTAssertEqual(PhotoLikersList.label(other, me: "abc-1"), "A visitor")
    }

    // F11: Settings drew the address's letter, My trees the name's.
    func testOneInitialForYourAvatar() {
        XCTAssertEqual(Profiles.myInitial(displayName: "Leafy Maple", email: "apptest@x.org"), "L")
        XCTAssertEqual(Profiles.myInitial(displayName: nil, email: "apptest@x.org"), "A")
        XCTAssertEqual(Profiles.myInitial(displayName: "", email: "apptest@x.org"), "A")
    }

    // F4: Want to visit took the pin away and left the card.
    func testWantToVisitDropsTheCardOfAnUnsavedTree() {
        var f = MapFilters()
        f.favouritesOnly = true
        let t = tree("lon_001")
        XCTAssertFalse(f.keepsCard(t, month: 5, collected: [], favourites: [], distanceKm: 1))
        XCTAssertTrue(f.keepsCard(t, month: 5, collected: [], favourites: ["lon_001"], distanceKm: 1))
    }

    // F6: switching to Collected left the map on the other lane's trees.
    func testALaneFramesItsOwnTrees() {
        let r = CollectView.laneRegion([(lat: 52.36, lng: 4.88), (lat: 52.38, lng: 4.90)])
        XCTAssertEqual(r?.center.latitude ?? 0, 52.37, accuracy: 0.001)
        XCTAssertEqual(r?.center.longitude ?? 0, 4.89, accuracy: 0.001)
        XCTAssertNil(CollectView.laneRegion([]))
    }

    // F8: 250 countries with no search.
    func testTheCountryListAnswersATypedName() {
        let hits = CountryList.matching("zeal").map(\.code)
        XCTAssertTrue(hits.contains("NZ"))
        XCTAssertFalse(hits.contains("NC"))
        XCTAssertEqual(CountryList.matching("nl").first?.code, "NL")
    }

    // Release walk 2026-11-26, pass 2: offline the tree page said "No notes
    // yet" about notes it never received.
    func testNotesThatDidNotArriveAreNotNone() {
        XCTAssertTrue(TreeNotes.failedAnswer(status: nil))
        XCTAssertTrue(TreeNotes.failedAnswer(status: 503))
        XCTAssertFalse(TreeNotes.failedAnswer(status: 200))
        XCTAssertFalse(TreeNotes.failedAnswer(status: 404))
    }

    // Release walk 2026-11-26, pass 3: "You found The Wilhelminalinde".
    func testATreesNameReadsRightInsideASentence() {
        XCTAssertEqual(CollectSheet.midSentence("The Wilhelminalinde"), "the Wilhelminalinde")
        XCTAssertEqual(CollectSheet.midSentence("Old Tjikko"), "Old Tjikko")
        XCTAssertEqual(CollectSheet.midSentence("Theodore's Oak"), "Theodore's Oak")
    }

    // Report 1488: the Tortworth chestnut showed under Westonbirt, 13 km off.
    func testATreeYouAddedIsNotFiledUnderAFarPlace() {
        XCTAssertNil(CollectView.placeOfYourTree(place: nil, linked: false, nearest: "Westonbirt", nearestKm: 13))
        XCTAssertEqual(CollectView.placeOfYourTree(place: "near Tortworth", linked: false, nearest: "Westonbirt", nearestKm: 13),
                       "Tortworth")
        XCTAssertEqual(CollectView.placeOfYourTree(place: nil, linked: false, nearest: "Baarn", nearestKm: 0.4), "Baarn")
        XCTAssertEqual(CollectView.placeOfYourTree(place: "in Nara", linked: true, nearest: "Kyoto", nearestKm: 30), "Kyoto")
    }
}
