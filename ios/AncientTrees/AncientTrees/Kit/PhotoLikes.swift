// THE HEART ON A VISITOR'S PHOTOGRAPH (Hidde, 2026-11-20: "dat gebruikers de
// fotos kunnen hartje geven om elkaar aan te moedigen voor de foto zelf";
// "Ja, bouw het hartje"). The website's lib/photo-likes-js.ts in Swift.
// Convention: CONVENTIONS.md "A heart for a visitor's photograph, beside save
// and Worth the visit": the bookmark saves the tree, the thumb says the tree
// is worth it, this heart thanks the photographer and sits at the end of
// their line. Strava's kudos: the count is the button. Google Maps' "Helpful":
// the count is public, who gave it is not (supabase/photo-likes.sql).
//
// One store for the app, so a heart given on Discover's row is given on the
// tree page too. Counts are asked of the server in one call for every heart
// that appeared within a moment of each other; nothing is kept on the device
// (hard rule 11): a fresh launch asks again.
import SwiftUI

@MainActor @Observable
final class PhotoLikes {
    static let shared = PhotoLikes()

    struct State: Equatable { var count = 0; var mine = false }
    private(set) var states: [String: State] = [:]
    private var asked = Set<String>()
    private var waiting = Set<String>()
    private var token: String?
    private var scheduled = false

    func state(_ id: String) -> State { states[id] ?? State() }

    /// A heart appeared: its count joins the next call, ~150 ms later.
    /// A new session asks again (whether "mine" depends on who asks).
    func want(_ id: String, token: String?) {
        if token != self.token { self.token = token; asked.removeAll() }
        guard !asked.contains(id) else { return }
        waiting.insert(id)
        guard !scheduled else { return }
        scheduled = true
        Task {
            try? await Task.sleep(for: .milliseconds(150))
            let ids = Array(waiting)
            waiting.removeAll(); scheduled = false
            ids.forEach { asked.insert($0) }
            await load(ids, token: self.token)
        }
    }

    private func load(_ ids: [String], token: String?) async {
        guard !ids.isEmpty else { return }
        struct Row: Decodable { let photo_id: String; let likes: Int; let mine: Bool }
        let r = Supa.request("/rest/v1/rpc/photo_like_counts", token: token, body: ["ids": ids])
        guard let (data, resp) = try? await Net.data(for: r),
              let http = resp as? HTTPURLResponse, (200..<300).contains(http.statusCode),
              let rows = try? JSONDecoder().decode([Row].self, from: data) else { return }
        for id in ids where states[id] == nil { states[id] = State() }
        for row in rows { states[row.photo_id] = State(count: row.likes, mine: row.mine) }
    }

    /// Give or take back, shown at once; a write the server refuses puts the
    /// heart back (People.swift's rule for Follow).
    func toggle(_ id: String, token: String) async {
        let was = state(id)
        let give = !was.mine
        states[id] = State(count: max(0, was.count + (give ? 1 : -1)), mine: give)
        let ok = give
            // ignore-duplicates: the table grants no UPDATE, so a second
            // heart on a phone that missed the first is a no-op, not a refusal.
            ? await Supa.post("/rest/v1/photo_likes?on_conflict=user_id,photo_id", token: token, body: [["photo_id": id]],
                              prefer: "resolution=ignore-duplicates,return=minimal")
            : await Supa.delete("/rest/v1/photo_likes?photo_id=eq.\(id)", token: token)
        if !ok { states[id] = was }
    }
}

/// The heart at the end of a photographer's line: outlined, filled moss once
/// you gave one, the count beside it from one (Hidde, 2026-08-26: "pas van 1
/// tellen"). Signed out a tap asks for a sign-in first and gives nothing.
struct PhotoHeart: View {
    let photoId: String
    var onDark = false
    @Environment(Account.self) private var account
    @Environment(Nudge.self) private var nudge
    private var store: PhotoLikes { PhotoLikes.shared }

    var body: some View {
        let s = store.state(photoId)
        Button {
            if account.isSignedIn {
                Task { if let t = await account.freshToken() { await store.toggle(photoId, token: t) } }
            } else {
                nudge.require(.general) {}
            }
        } label: {
            HStack(spacing: 3) {
                Image(systemName: s.mine ? "heart.fill" : "heart")
                    .font(.system(size: 14, weight: .semibold))
                if s.count > 0 {
                    Text("\(s.count)").font(.system(size: 12, weight: .semibold)).monospacedDigit()
                }
            }
            .foregroundStyle(s.mine ? (onDark ? Color.white : Brand.moss) : (onDark ? Color.white.opacity(0.85) : Brand.inkSoft))
            .frame(minWidth: 44, minHeight: 44, alignment: .trailing)
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
        .accessibilityLabel(s.mine ? "You liked this photo" : "Like this photo")
        .accessibilityValue(s.count > 0 ? "\(s.count)" : "")
        .accessibilityIdentifier("photo-like")
        .task(id: photoId + (account.session?.userId ?? "")) {
            store.want(photoId, token: await account.freshToken())
        }
    }
}
