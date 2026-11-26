// THE FEED, FROM THE SERVER ONLY (Hidde, 2026-11-26: "dit blijft maar fout
// gaan ... hoe gaan we zorgen dat die feed niet elke keer afhankelijk is van
// zon lange deploy"; the Feed tab, approved the same day: "niet slecht").
//
// Every post comes whole from public.feed() (supabase/feed.sql): the tree's
// name, place, pin and a picture in the public `feed` bucket, written by
// scripts/feed_publish.py right after the reader judge looked. Nothing here
// waits on a deploy or on this phone's catalogue: the catalogue only adds the
// story's first sentence when it already knows the tree. The name and avatar
// only of a public profile, else nil ("A visitor"); the account id only to a
// signed-in caller. Nothing kept on the device (hard rule 11).
import Foundation

public enum FeedPosts {
    public struct Post: Decodable, Identifiable, Hashable {
        let key: String
        let kind: String
        let tree_id: String
        let tree_name: String
        let place: String
        let url: String
        let latitude: Double?
        let longitude: Double?
        let photo_url: String?
        let photo_w: Int?
        let photo_h: Int?
        let published_at: String
        let author_name: String?
        let author_avatar: String?
        let author_id: String?
        public var id: String { key }

        /// A tree somebody added, against a photograph on one of ours.
        var isNewTree: Bool { kind == "tree" }

        /// The heart is the like on a visitor's photograph (PhotoLikes), keyed
        /// by its sightings uuid; only a photo post carries one (a tip's key is
        /// "tree:<id>" and has no photograph row to like).
        var likeId: String? {
            guard kind == "photo", UUID(uuidString: key) != nil else { return nil }
            return key.lowercased()
        }

        var photo: URL? { photo_url.flatMap(URL.init(string:)) }
    }

    enum Filter: String, CaseIterable {
        case everyone, following, near
        var label: String {
            switch self {
            case .everyone: "Everyone"
            case .following: "Following"
            case .near: "Near you"
            }
        }
    }

    /// Near you is a day out: within 100 km of where the phone is, the
    /// distance AllTrails' Nearby and komoot's "around you" draw around a
    /// person. The server pages by time only, so the filter reads page after
    /// page until it has something to show (FeedView.more).
    static let nearKm = 100.0

    static let pageSize = 24

    /// The posts after `after`, newest first, by the server's keyset paging:
    /// a post that goes live while somebody scrolls never repeats one. Nil
    /// when the server did not answer.
    static func page(after: Post?, n: Int = pageSize, token: String?) async -> [Post]? {
        var body: [String: Any] = ["n": n]
        if let after {
            body["before_at"] = after.published_at
            body["before_key"] = after.key
        }
        let r = Supa.request("/rest/v1/rpc/feed", token: token, body: body)
        guard let (data, resp) = try? await Net.data(for: r),
              let http = resp as? HTTPURLResponse, (200..<300).contains(http.statusCode),
              let rows = try? JSONDecoder().decode([Post].self, from: data) else { return nil }
        return rows
    }

    /// Whose post this is, asked again as a signed-in caller after the sign-in
    /// a tap on the name asked for: the post before it is the cursor that
    /// returns exactly this one.
    static func author(of post: Post, after prev: Post?, token: String?) async -> String? {
        await page(after: prev, n: 1, token: token)?.first { $0.key == post.key }?.author_id
    }

    /// "added a new tree" or "photographed a tree".
    static func deed(_ p: Post) -> String { p.isNewTree ? "added a new tree" : "photographed a tree" }

    /// The story's first sentence, for the two lines under the name. Cut at the
    /// first full stop that ends a sentence (followed by a space and a
    /// capital, or a quote), so "St. Peter" and "c. 1650" do not cut it short.
    static func firstSentence(_ story: String) -> String {
        let s = story.trimmingCharacters(in: .whitespacesAndNewlines)
        let chars = Array(s)
        var i = 0
        while i < chars.count {
            let c = chars[i]
            if c == "." || c == "!" || c == "?" {
                var j = i + 1
                while j < chars.count, chars[j] == "\"" || chars[j] == "”" || chars[j] == "’" { j += 1 }
                if j >= chars.count { return s }
                if chars[j] == " ", j + 1 < chars.count {
                    let next = chars[j + 1]
                    let prevWord = String(chars[..<i]).split(separator: " ").last.map(String.init) ?? ""
                    let abbreviation = prevWord.count <= 2 && prevWord.first?.isUppercase == true
                        || ["c", "ca", "St", "Mt", "Dr", "Mr", "Mrs", "approx"].contains(prevWord)
                    if (next.isUppercase || next == "\"" || next == "“") && !abbreviation {
                        return String(chars[...min(j - 1, chars.count - 1)])
                    }
                }
            }
            i += 1
        }
        return s
    }

    /// Kilometres between two points (haversine), for Near you.
    static func km(_ lat1: Double, _ lng1: Double, _ lat2: Double, _ lng2: Double) -> Double {
        let r = 6371.0
        let dLat = (lat2 - lat1) * .pi / 180, dLng = (lng2 - lng1) * .pi / 180
        let a = sin(dLat / 2) * sin(dLat / 2)
            + cos(lat1 * .pi / 180) * cos(lat2 * .pi / 180) * sin(dLng / 2) * sin(dLng / 2)
        return 2 * r * asin(min(1, sqrt(a)))
    }

    /// Whether a post passes the filter.
    static func passes(_ p: Post, _ f: Filter, following: Set<String>,
                       origin: (lat: Double, lng: Double)?) -> Bool {
        switch f {
        case .everyone: return true
        case .following:
            guard let a = p.author_id?.lowercased() else { return false }
            return following.contains(a)
        case .near:
            guard let o = origin, let lat = p.latitude, let lng = p.longitude else { return false }
            return km(o.lat, o.lng, lat, lng) <= nearKm
        }
    }

    /// A tree the server has and this phone's catalogue does not yet (the
    /// judge put it live after the last deploy): its page from the post
    /// itself, the name, place, picture and pin. The full page comes with the
    /// next catalogue.
    static func stub(_ p: Post) -> Tree {
        let slug = p.url.split(separator: "/").first.map(String.init) ?? ""
        let photo = p.photo_url.map {
            Photo(url: $0, license: nil, attribution: nil, width: p.photo_w, height: p.photo_h,
                  thumbRaw: $0, heroRaw: $0, creditRequiredRaw: false, attributionShort: nil,
                  creditLine: nil, creditURL: nil, frameRaw: nil, takenMonth: nil, season: nil,
                  sighting: nil, by: nil)
        }
        return Tree(id: p.tree_id, name: p.tree_name, species: "", age: nil, ageMin: nil, ageMax: nil,
                    lat: p.latitude ?? 0, lng: p.longitude ?? 0,
                    city: p.place, citySlug: slug, country: "", neighbourhoodRaw: nil,
                    access: "", paidEntryRaw: nil, transportRaw: nil, story: "",
                    recogniseRaw: nil, url: p.url, precision: .approximate, photo: photo,
                    bestTime: nil, peak: nil)
    }
}
