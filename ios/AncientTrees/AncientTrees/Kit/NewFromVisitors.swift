// NEW FROM VISITORS, Discover's second row (Hidde, 2026-11-06: "Ja,
// goedgekeurd"; "New from visitors" so it moves every week, "deze week waren
// wel gewoon 3 uploads").
//
// The newest photographs visitors sent that went live on one of our trees,
// from the server (supabase/new-from-visitors.sql, anon-readable): the tree,
// when, and the name and avatar only from a public profile, else nil, which
// the row prints as "A visitor". The account id comes only to a signed-in
// caller, so a tap on the name opens the profile; signed out it asks for a
// sign-in first (CLAUDE.md, Privacy and accounts). Nothing kept on the device.
import Foundation

enum NewFromVisitors {
    struct Row: Decodable, Identifiable, Equatable {
        let sighting_id: UUID
        let tree_id: String
        let published_at: String
        let author_name: String?
        let author_avatar: String?
        let author_id: String?
        var id: UUID { sighting_id }
    }

    /// The row shows from this many tiles, so it never stands half empty.
    static let minimum = 4

    static func load(token: String?) async -> [Row] {
        let r = Supa.request("/rest/v1/rpc/new_from_visitors", token: token, body: ["n": 12])
        guard let (data, resp) = try? await Net.data(for: r),
              let http = resp as? HTTPURLResponse, (200..<300).contains(http.statusCode),
              let rows = try? JSONDecoder().decode([Row].self, from: data) else { return [] }
        // One tile per tree, its newest photograph.
        var seen = Set<String>()
        return rows.filter { seen.insert($0.tree_id).inserted }
    }

    /// The photograph this visitor sent, found among the tree's own by the
    /// sightings row the feed names (Photo.sighting), so the tile shows their
    /// picture and not the tree's lead (Hidde, 2026-11-15: "waarom toont hij
    /// niet altijd de gebruikers foto"). Nil until the feed carries it, and the
    /// tile then shows the lead as before.
    static func shot(_ row: Row, in tree: Tree) -> Photo? {
        let id = row.sighting_id.uuidString.lowercased()
        return tree.shots.first { $0.sighting == id }
    }

    /// The tiles the row shows: only a tree whose feed already carries this
    /// visitor's photograph. The server names a photograph the moment it is
    /// published, the feed only after the next deploy; in between the tile
    /// stood empty, or showed somebody else's picture over this visitor's name
    /// (Hidde, 2026-11-16: "bij ios missen de eerste 4 een foto, bij web
    /// allemaal wel"). The website's rule (visitors-row-js.ts skips a tree its
    /// build does not know); the tile appears with the next feed.
    static func tiles(_ rows: [Row], tree: (String) -> Tree?) -> [(row: Row, tree: Tree, shot: Photo)] {
        rows.compactMap { r in
            guard let t = tree(r.tree_id), let s = shot(r, in: t) else { return nil }
            return (row: r, tree: t, shot: s)
        }
    }
}
