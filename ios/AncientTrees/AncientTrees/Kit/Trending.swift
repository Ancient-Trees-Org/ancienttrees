// TRENDING THIS MONTH, Discover's numbered shelf (DESIGN, 2026-11-26, after
// Hidde's look at Polarsteps' Verkennen tab: "Trending deze maand").
//
// TREES, not places (Hidde, on the first design: "is het niet veel logischer
// om bomen trending te maken: bomen die veel worden gefotografeerd, geliked,
// worth a visit"). The trees the most different people did something with in
// the last 30 days: shared a photograph, gave one a heart, voted it Worth
// the visit, saved it. Each person counts once per tree. Counted on the
// server, supabase/trending-trees.sql (`trending_trees`), ids and counts
// only, one call. Nothing kept on the device.
import Foundation

enum Trending {
    struct Row: Decodable { let tree_id: String; let people: Int; let actions: Int }

    /// Three columns of three, Polarsteps' shelf.
    static let count = 9
    static let days = 30

    static func load(token: String?, tree: (String) -> Tree?) async -> [Tree] {
        // Design scaffolding: -trendingids=a,b,c stands in for the server
        // until trending-trees.sql is pasted (the sweep's screenshots).
        if let a = ProcessInfo.processInfo.arguments.first(where: { $0.hasPrefix("-trendingids=") }) {
            return pick(a.dropFirst(13).split(separator: ",").map(String.init), tree: tree)
        }
        let r = Supa.request("/rest/v1/rpc/trending_trees", token: token,
                             body: ["days": days, "n": count * 2])
        guard let (data, resp) = try? await Net.data(for: r),
              let http = resp as? HTTPURLResponse, (200..<300).contains(http.statusCode),
              let rows = try? JSONDecoder().decode([Row].self, from: data) else { return [] }
        return pick(rows.map(\.tree_id), tree: tree)
    }

    /// Trees this feed knows and can show with a photograph, in rank order.
    static func pick(_ ids: [String], tree: (String) -> Tree?) -> [Tree] {
        Array(ids.compactMap(tree).filter { $0.photo != nil }.prefix(count))
    }
}
