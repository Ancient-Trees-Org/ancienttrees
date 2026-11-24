// THE HEARTS OTHER PEOPLE GAVE YOUR PHOTOGRAPHS (Hidde, 2026-11-22: "kun je
// ook zien als je een hartje krijgt wie je dat heeft gegeven?", the bell on
// Discover "voor nu is het ok"; he expects a feed with the people you follow
// later, with its own place). The website's /activity (ActivityPage.astro).
//
// Convention: Instagram's Activity and Strava's notifications (CONVENTIONS.md
// "A heart for a visitor's photograph ... Who gave it"): one row per
// photograph, bundled ("Miguel P. and 2 others gave your photograph of ... a
// heart"), New above Earlier, the photograph at the row's end; a tap opens the
// tree. Design: drafts/design-2026-11-22-heart-who/product.html.
//
// Since 2026-11-24 a new follower too (Hidde: "Ja, bouw het"): "X started
// following you." with Follow back, one row per person, never bundled
// (drafts/design-2026-11-24-follow-activity).
//
// From the server (supabase/follow-activity.sql my_activity), read
// each time the screen opens; opening it calls activity_seen(), which takes
// the bell's dot away on every device. Nothing kept on the phone (hard rule 11).
import SwiftUI

@MainActor @Observable
final class ActivityStore {
    static let shared = ActivityStore()

    /// One row of my_activity (supabase/follow-activity.sql): kind "heart"
    /// (one per photograph, bundled) or "follow" (one per person who follows
    /// you, with whether you follow them back; Hidde, 2026-11-24).
    struct Row: Decodable, Identifiable {
        let kind: String?
        let photo_id: String?
        let tree_id: String?
        let hearts: Int
        let latest_at: String
        let names: [String]?
        let avatars: [String]?
        let is_new: Bool
        let user_id: String?
        let following: Bool?
        var isFollow: Bool { kind == "follow" }
        var id: String { isFollow ? "f-" + (user_id ?? latest_at) : (photo_id ?? latest_at) }
    }

    private(set) var rows: [Row] = []
    private(set) var loaded = false
    /// Something came after you last opened Activity: the bell's dot.
    private(set) var fresh = false

    func load(token: String?, n: Int = 60) async {
        guard let token else { rows = []; fresh = false; return }
        let r = Supa.request("/rest/v1/rpc/my_activity", token: token, body: ["n": n])
        guard let (data, resp) = try? await Net.data(for: r),
              let http = resp as? HTTPURLResponse, (200..<300).contains(http.statusCode),
              let got = try? JSONDecoder().decode([Row].self, from: data) else { return }
        rows = got
        loaded = true
        fresh = got.contains { $0.is_new }
    }

    /// Follow back, or take it back, from a follower's row: the pill moves at
    /// once and goes back if the account refuses (People.swift toggle).
    func setFollowing(_ on: Bool, for userId: String) {
        rows = rows.map { r in
            guard r.isFollow, r.user_id == userId else { return r }
            return Row(kind: r.kind, photo_id: r.photo_id, tree_id: r.tree_id, hearts: r.hearts,
                       latest_at: r.latest_at, names: r.names, avatars: r.avatars,
                       is_new: r.is_new, user_id: r.user_id, following: on)
        }
    }

    func seen(token: String?) async {
        guard let token else { return }
        if await Supa.post("/rest/v1/rpc/activity_seen", token: token, body: [String: String]()) { fresh = false }
    }
}

/// The bell top right of Discover: signed in only, a dot while something is new.
struct ActivityBell: View {
    @Environment(Account.self) private var account
    @Environment(Navigator.self) private var navigator
    private var store: ActivityStore { ActivityStore.shared }

    var body: some View {
        if account.isSignedIn {
            Button { navigator.push = .activity } label: {
                Image(systemName: "bell")
                    .font(.system(size: 17, weight: .semibold))
                    .foregroundStyle(Brand.ink)
                    .frame(width: 40, height: 40)
                    .background(Brand.surface, in: .circle)
                    .overlay(alignment: .topTrailing) {
                        if store.fresh {
                            Circle().fill(Color(red: 0.85, green: 0.34, blue: 0.25))
                                .frame(width: 9, height: 9)
                                .overlay(Circle().strokeBorder(Brand.ground, lineWidth: 2))
                                .offset(x: -7, y: 7)
                        }
                    }
                    .frame(minWidth: 44, minHeight: 44)
                    .contentShape(.rect)
            }
            .buttonStyle(.plain)
            .accessibilityLabel(store.fresh ? "Activity, new" : "Activity")
            .accessibilityIdentifier("activity-bell")
            .task(id: account.session?.userId ?? "") {
                await store.load(token: await account.freshToken(), n: 5)
            }
        }
    }
}

struct ActivityView: View {
    let catalogue: Catalogue
    @Environment(Account.self) private var account
    @Environment(Navigator.self) private var navigator
    @Environment(Profiles.self) private var profiles
    private var store: ActivityStore { ActivityStore.shared }

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 0) {
                Text("Hearts on your photographs, and new followers.")
                    .font(.subheadline).foregroundStyle(Brand.inkSoft)
                    .padding(.horizontal, 16).padding(.bottom, 8)
                let fresh = store.rows.filter(\.is_new)
                let old = store.rows.filter { !$0.is_new }
                if !fresh.isEmpty { section("New", fresh) }
                if !old.isEmpty { section("Earlier", old) }
                if store.loaded && store.rows.isEmpty {
                    Text("Nothing yet. When someone gives one of your photographs a heart or follows you, it shows here.")
                        .font(.callout).foregroundStyle(Brand.inkSoft)
                        .padding(16)
                        .accessibilityIdentifier("activity-empty")
                }
            }
            .padding(.top, 6).padding(.bottom, 80)
        }
        // Pull to refresh, as Instagram's Activity (Hidde, 2026-11-22, "5 ja").
        .refreshable {
            let t = await account.freshToken()
            await store.load(token: t)
            await store.seen(token: t)
        }
        .brandGround()
        .navigationTitle("Activity")
        .navigationBarTitleDisplayMode(.inline)
        .accessibilityIdentifier("activity")
        .task(id: account.session?.userId ?? "") {
            let t = await account.freshToken()
            await store.load(token: t)
            await store.seen(token: t)
        }
    }

    @ViewBuilder private func section(_ title: String, _ rows: [ActivityStore.Row]) -> some View {
        Text(title).font(.brand(15, .black, relativeTo: .headline))
            .padding(.horizontal, 16).padding(.top, 14).padding(.bottom, 4)
        ForEach(rows) { row($0) }
    }

    /// A NEW FOLLOWER (Hidde, 2026-11-24, "Ja, bouw het"; Instagram's
    /// Activity, design drafts/design-2026-11-24-follow-activity): their face,
    /// "X started following you.", and Follow back or Following at the end,
    /// the pill Find people draws. The face and words open their profile.
    @ViewBuilder private func followRow(_ r: ActivityStore.Row) -> some View {
        let name = r.names?.first ?? "A visitor"
        let on = r.following ?? false
        HStack(spacing: 12) {
            Button {
                if let u = r.user_id { navigator.push = .person(u) }
            } label: {
                HStack(spacing: 12) {
                    ActivityFace(name: name, avatar: r.avatars?.first.flatMap { $0.isEmpty ? nil : $0 })
                        .frame(width: 44, height: 40)
                    (Text((try? AttributedString(markdown: "**\(name)** started following you.")) ?? AttributedString(name))
                     + Text("  " + (SentAgo.short(r.latest_at) ?? "")).foregroundColor(Brand.inkSoft))
                        .font(.system(size: 14))
                        .foregroundStyle(Brand.ink)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .multilineTextAlignment(.leading)
                }
                .contentShape(.rect)
            }
            .buttonStyle(.plain)
            .accessibilityIdentifier("activity-follow-open")
            Button { toggle(r) } label: {
                Text(on ? "Following" : "Follow back")
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(on ? Brand.ink : .white)
                    .padding(.horizontal, 14)
                    .frame(minWidth: 96, minHeight: 34)
                    .background(on ? Color.clear : Brand.moss, in: .capsule)
                    .overlay { if on { Capsule().strokeBorder(Brand.hairline, lineWidth: 1) } }
                    .frame(minHeight: 44)
                    .contentShape(.rect)
            }
            .buttonStyle(.plain)
            .accessibilityIdentifier("activity-follow")
        }
        .padding(.horizontal, 16).padding(.vertical, 6)
        .background(r.is_new ? Brand.moss.opacity(0.08) : .clear)
        .accessibilityIdentifier("activity-row")
    }

    private func toggle(_ r: ActivityStore.Row) {
        guard let other = r.user_id, let me = account.session?.userId else { return }
        let was = r.following ?? false
        store.setFollowing(!was, for: other)
        Task {
            guard let t = await account.freshToken() else { store.setFollowing(was, for: other); return }
            let ok = was
                ? await profiles.unfollow(other, me: me, token: t)
                : await profiles.follow(other, me: me, token: t)
            if !ok { store.setFollowing(was, for: other) }
        }
    }

    @ViewBuilder private func row(_ r: ActivityStore.Row) -> some View {
        if r.isFollow { followRow(r) } else { heartRow(r) }
    }

    @ViewBuilder private func heartRow(_ r: ActivityStore.Row) -> some View {
        let tree = r.tree_id.flatMap { catalogue.tree($0) }
        let shot = tree?.shots.first { $0.sighting == r.photo_id?.lowercased() }
        Button {
            if let t = tree { navigator.push = .tree(t.id) }
        } label: {
            HStack(spacing: 12) {
                faces(r)
                (Text(words(r, tree?.name ?? "a tree")) + Text("  " + (SentAgo.short(r.latest_at) ?? "")).foregroundColor(Brand.inkSoft))
                    .font(.system(size: 14))
                    .foregroundStyle(Brand.ink)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .multilineTextAlignment(.leading)
                if let s = shot ?? tree?.photo {
                    TreePhoto(url: s.card) { Brand.surfaceMuted }
                        .frame(width: 48, height: 48)
                        .clipShape(.rect(cornerRadius: 8))
                }
            }
            .padding(.horizontal, 16).padding(.vertical, 10)
            .background(r.is_new ? Brand.moss.opacity(0.08) : .clear)
            .contentShape(.rect)
        }
        .buttonStyle(.plain)
        .accessibilityIdentifier("activity-row")
    }

    private func words(_ r: ActivityStore.Row, _ tree: String) -> AttributedString {
        let names = r.names ?? []
        let a = names.first ?? "A visitor"
        var s: String
        if r.hearts <= 1 { s = "**\(a)** gave your photograph of **\(tree)** a heart." }
        else if r.hearts == 2, names.count > 1 { s = "**\(a)** and **\(names[1])** gave your photograph of **\(tree)** a heart." }
        else { s = "**\(a)** and **\(r.hearts - 1) others** gave your photograph of **\(tree)** a heart." }
        return (try? AttributedString(markdown: s)) ?? AttributedString(s)
    }

    private func faces(_ r: ActivityStore.Row) -> some View {
        let names = r.names ?? []
        let avs = r.avatars ?? []
        let n = max(1, min(2, names.count))
        return ZStack(alignment: .topLeading) {
            ForEach(0..<n, id: \.self) { i in
                let name = i < names.count ? names[i] : "A visitor"
                let av = i < avs.count && !avs[i].isEmpty ? avs[i] : nil
                ActivityFace(name: name, avatar: av)
                    .offset(x: CGFloat(i) * 14, y: n == 1 ? 5 : CGFloat(i) * 10)
            }
        }
        .frame(width: 44, height: 40, alignment: .topLeading)
    }
}

private struct ActivityFace: View {
    let name: String
    let avatar: String?
    var body: some View {
        Group {
            if let a = avatar, let u = URL(string: a) {
                AsyncImage(url: u) { $0.resizable().scaledToFill() } placeholder: { Brand.moss.opacity(0.15) }
            } else {
                Text(String(name.prefix(1)).uppercased())
                    .font(.system(size: 12, weight: .bold))
                    .foregroundStyle(Brand.moss)
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                    .background(Color(red: 0.89, green: 0.92, blue: 0.84))
            }
        }
        .frame(width: 30, height: 30)
        .clipShape(.circle)
        .overlay(Circle().strokeBorder(Brand.ground, lineWidth: 2))
    }
}
