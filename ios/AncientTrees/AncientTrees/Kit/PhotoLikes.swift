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

/// The heart right after a photographer's line: outlined, filled moss once
/// you gave one, the count beside it from one (Hidde, 2026-08-26: "pas van 1
/// tellen"). TWO TAPS since 2026-11-22, Instagram's and Strava's (Hidde: "kun
/// je ook zien ... wie je dat heeft gegeven?"): the heart gives or takes back,
/// the count opens who gave one (PhotoLikersSheet). Signed out either asks
/// for a sign-in first and gives nothing.
struct PhotoHeart: View {
    let photoId: String
    var onDark = false
    @Environment(Account.self) private var account
    @Environment(Nudge.self) private var nudge
    @State private var showingLikers = false
    private var store: PhotoLikes { PhotoLikes.shared }

    var body: some View {
        let s = store.state(photoId)
        let tint = s.mine ? (onDark ? Color.white : Brand.moss) : (onDark ? Color.white.opacity(0.85) : Brand.inkSoft)
        HStack(spacing: 0) {
            Button {
                if account.isSignedIn {
                    Task { if let t = await account.freshToken() { await store.toggle(photoId, token: t) } }
                } else {
                    nudge.require(.general) {}
                }
            } label: {
                Image(systemName: s.mine ? "heart.fill" : "heart")
                    .font(.system(size: 14, weight: .semibold))
                    .foregroundStyle(tint)
                    .frame(minWidth: 26, minHeight: 44)
                    .contentShape(Rectangle())
            }
            .buttonStyle(.plain)
            .accessibilityLabel(s.mine ? "You liked this photo" : "Like this photo")
            .accessibilityIdentifier("photo-like")
            if s.count > 0 {
                Button {
                    if account.isSignedIn { showingLikers = true } else { nudge.require(.general) {} }
                } label: {
                    Text("\(s.count)").font(.system(size: 12, weight: .semibold)).monospacedDigit()
                        .foregroundStyle(tint)
                        .frame(minWidth: 22, minHeight: 44, alignment: .leading)
                        .contentShape(Rectangle())
                }
                .buttonStyle(.plain)
                .accessibilityLabel(s.count == 1 ? "1 heart. See who gave a heart" : "\(s.count) hearts. See who gave a heart")
                .accessibilityIdentifier("photo-like-count")
            }
        }
        .task(id: photoId + (account.session?.userId ?? "")) {
            store.want(photoId, token: await account.freshToken())
        }
        .sheet(isPresented: $showingLikers) {
            PhotoLikersSheet(photoId: photoId)
                .presentationDetents([.medium, .large])
                .presentationDragIndicator(.visible)
        }
    }
}

/// Who gave a photograph a heart, oldest first (photo_likers in
/// supabase/photo-hearts-who.sql, signed in only): the followers list's row,
/// a face and a name that opens the profile; a private profile is "A visitor"
/// and opens nothing.
struct PhotoLikersSheet: View {
    let photoId: String
    @Environment(Account.self) private var account
    @Environment(Navigator.self) private var navigator
    @Environment(\.dismiss) private var dismiss

    struct Row: Decodable, Identifiable {
        let user_id: String?
        let display_name: String?
        let avatar_url: String?
        let created_at: String
        var id: String { (user_id ?? "") + created_at }
    }
    @State private var rows: [Row] = []

    var body: some View {
        VStack(spacing: 0) {
            Text(rows.count == 1 ? "1 heart" : "\(max(rows.count, PhotoLikes.shared.state(photoId).count)) hearts")
                .font(.brand(26, .black, relativeTo: .title2))
                .foregroundStyle(Brand.ink)
                .padding(.top, 24).padding(.bottom, 12)
            ScrollView {
                LazyVStack(spacing: 0) {
                    ForEach(rows) { r in
                        Button {
                            guard let id = r.user_id else { return }
                            dismiss()
                            Task { @MainActor in
                                try? await Task.sleep(for: .milliseconds(300))
                                navigator.push = .person(id)
                            }
                        } label: {
                            HStack(spacing: 12) {
                                let name = r.display_name ?? "A visitor"
                                ZStack {
                                    Circle().fill(Brand.moss.opacity(0.12))
                                    if let a = r.avatar_url, let u = URL(string: a) {
                                        TreePhoto(url: u) { Color.clear }.clipShape(.circle)
                                    } else {
                                        Text(String(name.prefix(1)).uppercased())
                                            .font(.brand(16, .black, relativeTo: .body))
                                            .foregroundStyle(Brand.moss)
                                    }
                                }
                                .frame(width: 40, height: 40)
                                Text(name)
                                    .font(.callout.weight(r.display_name == nil ? .regular : .semibold))
                                    .foregroundStyle(r.display_name == nil ? Brand.inkSoft : Brand.ink)
                                Spacer()
                            }
                            .padding(.vertical, 8)
                            .contentShape(.rect)
                        }
                        .buttonStyle(.plain)
                        .disabled(r.user_id == nil)
                        Divider()
                    }
                }
                .padding(.horizontal, 20)
            }
        }
        .brandGround()
        .accessibilityIdentifier("photo-likers")
        .task {
            let r = Supa.request("/rest/v1/rpc/photo_likers", token: await account.freshToken(), body: ["photo": photoId])
            guard let (data, resp) = try? await Net.data(for: r),
                  let http = resp as? HTTPURLResponse, (200..<300).contains(http.statusCode),
                  let got = try? JSONDecoder().decode([Row].self, from: data) else { return }
            rows = got
        }
    }
}
