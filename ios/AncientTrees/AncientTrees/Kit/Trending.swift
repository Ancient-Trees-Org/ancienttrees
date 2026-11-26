// TRENDING THIS MONTH, Discover's numbered shelf (DESIGN, 2026-11-26, after
// Hidde's look at Polarsteps' Verkennen tab: "Trending deze maand").
//
// What trends: the PLACES where the most different visitors shared a
// photograph of one of our trees in the last 30 days. People, not
// photographs, so one keen visitor with eleven shots of Gdansk does not
// outrank London's eighteen visitors; photographs break a tie. Read from the
// public visitor_photos RPC the "New from visitors" row already pages
// (supabase/visitor-photos.sql), so it needs no deploy. Saves were the other
// candidate, but data/tree-saves.json counts every save ever, not this month.
//
// For the design the app pages the RPC back 30 days itself (about fifteen
// calls of 48). Before release this becomes one server function returning
// the nine places, so a phone asks once. Nothing is kept on the device.
import Foundation

enum Trending {
    struct Place: Identifiable, Equatable {
        let slug: String
        let name: String
        let country: String
        let people: Int
        let photos: Int
        /// The newest visitor photograph there this feed can show, else nil
        /// and the place's own face.
        let tree: Tree
        let shot: Photo?
        var id: String { slug }
        static func == (a: Place, b: Place) -> Bool { a.slug == b.slug && a.people == b.people }
    }

    /// Three columns of three, Polarsteps' shelf.
    static let count = 9
    static let days = 30

    static func load(token: String?, tree: (String) -> Tree?) async -> [Place] {
        let since = ISO8601DateFormatter().string(from: Date().addingTimeInterval(-Double(days) * 86_400))
        var rows: [NewFromVisitors.Row] = []
        var cursor: NewFromVisitors.Row? = nil
        for _ in 0..<24 {
            guard let page = await NewFromVisitors.page(after: cursor, n: 48, token: token) else { break }
            rows += page.filter { $0.published_at >= since }
            guard page.count == 48, let last = page.last, last.published_at >= since else { break }
            cursor = last
        }
        return rank(rows, tree: tree)
    }

    static func rank(_ rows: [NewFromVisitors.Row], tree: (String) -> Tree?) -> [Place] {
        struct Tally { var people = Set<String>(); var photos = 0; var newest: (Tree, Photo?)? }
        var by: [String: Tally] = [:]
        for r in rows {                                   // newest first, as served
            guard let t = tree(r.tree_id) else { continue }
            var x = by[t.citySlug] ?? Tally()
            // A visitor without a public profile counts once per photograph's
            // sighting, never by name: nothing else identifies them here.
            x.people.insert(r.author_name ?? r.sighting_id.uuidString)
            x.photos += 1
            if x.newest == nil || x.newest?.1 == nil {
                let s = NewFromVisitors.shot(r, in: t)
                if x.newest == nil || s != nil { x.newest = (t, s) }
            }
            by[t.citySlug] = x
        }
        return by.compactMap { slug, x -> Place? in
            guard let (t, s) = x.newest, s != nil || t.photo != nil else { return nil }
            return Place(slug: slug, name: t.city, country: t.country,
                         people: x.people.count, photos: x.photos, tree: t, shot: s)
        }
        .sorted { ($0.people, $0.photos, $1.name) > ($1.people, $1.photos, $0.name) }
        .prefix(count).map { $0 }
    }
}
