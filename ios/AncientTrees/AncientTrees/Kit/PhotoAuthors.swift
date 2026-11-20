// WHO TOOK THE PHOTOGRAPH, on a tree page (Hidde, 2026-11-17: "bij foto's wel
// namen gaan noemen van degene die het heeft opgeloot. Als die een account
// hebben, dan worden die accounts ook klikbaar"). The website's
// reader-names-js.ts in Swift, the rule of New from visitors: the server
// (supabase/reader-names.sql, photo_authors) names a reader's photograph by
// the id the feed carries (Photo.by), with a name and picture only from a
// public profile and the account id only to a signed-in caller. A private
// profile, our own photograph, any licensed one: no row, no name.
import Foundation

enum PhotoAuthors {
    struct Row: Decodable, Equatable {
        let photo_id: String
        let author_name: String?
        let author_avatar: String?
        let author_id: String?
        /// When it was sent (supabase/photo-authors-time.sql, 2026-11-20);
        /// nil until that is pasted, and the byline then has no time.
        let published_at: String?
    }

    static func load(ids: [String], token: String?) async -> [String: Row] {
        let ids = Array(Set(ids)).sorted()
        guard !ids.isEmpty else { return [:] }
        let r = Supa.request("/rest/v1/rpc/photo_authors", token: token, body: ["ids": ids])
        guard let (data, resp) = try? await Net.data(for: r),
              let http = resp as? HTTPURLResponse, (200..<300).contains(http.statusCode),
              let rows = try? JSONDecoder().decode([Row].self, from: data) else { return [:] }
        var out: [String: Row] = [:]
        for row in rows where row.author_name != nil { out[row.photo_id] = row }
        return out
    }
}
