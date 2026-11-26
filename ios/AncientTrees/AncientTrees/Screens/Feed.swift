// THE FEED TAB (Hidde, 2026-11-26: the feed "een eigen tab", the design
// drafts/design-2026-11-26-feed/feed.png approved: "niet slecht").
//
// Convention (CONVENTIONS.md "A feed tab"): AllTrails' Community tab, Strava's
// Home, iNaturalist's observations and Polarsteps' steps. One post per thing a
// reader put live, newest first: who (avatar, name) and what and when on top,
// the WHOLE photograph under it at 4:5 with the place on it, then the tree's
// name, a line of its story, and the actions row (Instagram's and Strava's
// place for them, under the picture). Filters as chips under the title
// (AllTrails' Nearby chip, Strava's Following). Endless, by the server's
// keyset paging, pull to refresh.
//
// Data from public.feed() only (Kit/FeedPosts.swift): a post never waits on a
// deploy. A tree this phone's catalogue already knows adds its story's first
// sentence; one it does not know yet still shows and opens, from the post.
//
// Spacing from the existing parts: the 16 page edge and screen title of
// Discover, the FilterChip row 8 apart, 28 between posts (BrandSheet's gap
// between sections), 10 inside a post's group, CollectedTile's pill shape.
import SwiftUI

struct FeedView: View {
    let catalogue: Catalogue
    let origin: (lat: Double, lng: Double)
    let located: Bool
    var onUseMyLocation: () -> Void = {}

    @Environment(Account.self) private var account
    @Environment(Navigator.self) private var navigator
    @Environment(Nudge.self) private var nudge
    @Environment(Profiles.self) private var profiles

    /// The tag the Feed tab carries in ContentView's TabView.
    static let tag = 4

    @State private var filter: FeedPosts.Filter = .everyone
    /// Every post the server sent, each with the one before it (the cursor
    /// that returns exactly this post, for the name after a sign-in).
    @State private var posts: [(post: FeedPosts.Post, prev: FeedPosts.Post?)] = []
    @State private var last: FeedPosts.Post?
    @State private var busy = false
    @State private var done = false
    @State private var failed = false
    @State private var generation = 0
    /// The accounts you follow, asked once per sign-in for Following.
    @State private var following: Set<String> = []

    private static let edge: CGFloat = 16

    private var shown: [(post: FeedPosts.Post, prev: FeedPosts.Post?)] {
        let o: (lat: Double, lng: Double)? = located ? origin : nil
        return posts.filter { FeedPosts.passes($0.post, filter, following: following, origin: o) }
    }

    var body: some View {
        GeometryReader { geo in
            let width = geo.size.width - Self.edge * 2
            ScrollViewReader { proxy in
                ScrollView {
                    LazyVStack(alignment: .leading, spacing: 28) {
                        // 16 from the chips to the first post, the design's
                        // gap, not the 28 between posts.
                        header.id("feed-top").padding(.bottom, -12)
                        let list = shown
                        ForEach(Array(list.enumerated()), id: \.element.post.key) { i, it in
                            post(it.post, prev: it.prev, width: width)
                                .id("feed-\(i)")
                                .onAppear { if i >= list.count - 6 { Task { await more() } } }
                        }
                        footer(list.isEmpty)
                    }
                    .padding(.horizontal, Self.edge)
                    .padding(.top, 6)
                    .padding(.bottom, 100)        // clear of the floating tab bar
                }
                .refreshable { await restart() }
                .onChange(of: navigator.scrollToTop?.token) { _, _ in
                    guard navigator.scrollToTop?.tab == Self.tag else { return }
                    withAnimation(.snappy) { proxy.scrollTo("feed-top", anchor: .top) }
                }
                // -feedto=N scrolls to the Nth post for the sweep, which
                // cannot swipe (Discover's -discoverto, 2026-10-10).
                .task {
                    if let a = ProcessInfo.processInfo.arguments.first(where: { $0.hasPrefix("-feedto=") }) {
                        try? await Task.sleep(for: .seconds(4))
                        proxy.scrollTo("feed-" + a.dropFirst(8), anchor: .top)
                    }
                }
            }
            .accessibilityIdentifier("feed")
        }
        .brandGround()
        .task(id: account.isSignedIn) {
            await loadFollowing()
            await restart()
        }
    }

    // MARK: - header

    private var header: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("Feed")
                .font(.screenTitle)
                .foregroundStyle(Brand.ink)
            HStack(spacing: 8) {
                ForEach(FeedPosts.Filter.allCases, id: \.self) { f in
                    FilterChip(label: f.label, icon: nil, on: filter == f) { choose(f) }
                        .accessibilityIdentifier("feed-filter-\(f.rawValue)")
                }
            }
        }
    }

    private func choose(_ f: FeedPosts.Filter) {
        if f == .following && !account.isSignedIn {
            nudge.require(.general) { filter = .following }
            return
        }
        if f == .near && !located { onUseMyLocation() }
        filter = f
        Measure.event("feed_filter", ["filter": f.rawValue])
        Task { await fill() }
    }

    // MARK: - a post

    private func post(_ p: FeedPosts.Post, prev: FeedPosts.Post?, width: CGFloat) -> some View {
        let known = catalogue.tree(p.tree_id)
        let tree = known ?? FeedPosts.stub(p)
        let route: Route = known != nil ? .tree(p.tree_id) : .feedPost(p)
        return VStack(alignment: .leading, spacing: 10) {
            byline(p, prev: prev)
            NavigationLink(value: route) {
                TreePhoto(url: p.photo) { Brand.surfaceMuted }
                    .frame(width: width, height: width * 5 / 4)
                    .overlay(alignment: .topLeading) {
                        if p.isNewTree { FeedPill(text: "New on the map").padding(10) }
                    }
                    .overlay(alignment: .bottomLeading) {
                        if !p.place.isEmpty { FeedPill(text: p.place).padding(10) }
                    }
                    .clipShape(.rect(cornerRadius: 14, style: .continuous))
                    .contentShape(.rect)
                    .accessibilityElement(children: .ignore)
                    .accessibilityLabel("\(p.tree_name), \(p.place)")
            }
            .buttonStyle(.plain)
            .accessibilityIdentifier("feed-photo")
            .modifier(DoubleTapLike(id: p.likeId))
            NavigationLink(value: route) {
                VStack(alignment: .leading, spacing: 4) {
                    Text(p.tree_name)
                        .font(.brand(20, .bold, relativeTo: .title3))
                        .foregroundStyle(Brand.ink)
                        .multilineTextAlignment(.leading)
                        .lineLimit(2)
                        .fixedSize(horizontal: false, vertical: true)
                    if let story = known?.story, !story.isEmpty {
                        Text(FeedPosts.firstSentence(story))
                            .font(.system(size: 15))
                            .foregroundStyle(Brand.inkSoft)
                            .multilineTextAlignment(.leading)
                            .lineLimit(2)
                    }
                }
                .frame(maxWidth: .infinity, alignment: .leading)
                .contentShape(.rect)
            }
            .buttonStyle(.plain)
            .accessibilityIdentifier("feed-name")
            actions(p, tree: tree)
        }
    }

    /// Who, what and when: the face, the name (a public profile's, tappable
    /// signed in, asking for a sign-in signed out), "A visitor" for a private
    /// one, which opens nothing (VisitorLine's rules, 2026-11-06/07).
    private func byline(_ p: FeedPosts.Post, prev: FeedPosts.Post?) -> some View {
        let name = p.author_name ?? "A visitor"
        let when = SentAgo.short(p.published_at)
        let line = HStack(spacing: 10) {
            FeedFace(name: name, avatar: p.author_avatar, known: p.author_name != nil)
            VStack(alignment: .leading, spacing: 1) {
                Text(name)
                    .font(.system(size: 15, weight: .semibold))
                    .foregroundStyle(Brand.ink)
                    .lineLimit(1)
                Text([FeedPosts.deed(p), when].compactMap { $0 }.joined(separator: " · "))
                    .font(.system(size: 13))
                    .foregroundStyle(Brand.inkSoft)
                    .lineLimit(1)
            }
            Spacer(minLength: 0)
        }
        .frame(minHeight: 44)
        .contentShape(.rect)
        return Group {
            if p.author_name == nil {
                line.accessibilityElement(children: .combine)
            } else {
                Button { openAuthor(p, prev: prev) } label: { line }
                    .buttonStyle(.plain)
                    .accessibilityLabel("\(name), open profile")
                    .accessibilityIdentifier("feed-author")
            }
        }
    }

    private func actions(_ p: FeedPosts.Post, tree: Tree) -> some View {
        HStack(spacing: 4) {
            if let like = p.likeId {
                PhotoHeart(photoId: like, size: 19)
                    .padding(.trailing, 6)
            }
            SaveHeart(tree: tree, look: .plain)
            if let url = Shared.page(p.url, from: "feed") {
                ShareLink(item: url, subject: Text(p.tree_name),
                          message: Text("\(p.tree_name), \(p.place).")) {
                    Image(systemName: "square.and.arrow.up")
                        .font(.system(size: 17, weight: .medium))
                        .foregroundStyle(Brand.inkSoft)
                        .frame(width: 44, height: 44)
                        .contentShape(.rect)
                }
                .countsShare("feed")
                .accessibilityLabel("Share \(p.tree_name)")
                .accessibilityIdentifier("feed-share")
            }
            Spacer(minLength: 0)
        }
        // The glyphs line up with the text above, not their 44 point boxes
        // (PhotoHeart already reaches 9 points out of its own).
        .padding(.leading, p.likeId == nil ? -12 : -3)
        .padding(.top, -6)
    }

    @ViewBuilder private func footer(_ empty: Bool) -> some View {
        if done || failed {
            Text(empty ? emptyLine : "You have seen everything so far.")
                .font(.subheadline).foregroundStyle(Brand.inkSoft)
                .multilineTextAlignment(.center)
                .frame(maxWidth: .infinity)
                .padding(.top, 8)
        } else {
            ProgressView()
                .frame(maxWidth: .infinity, minHeight: 60)
                .onAppear { Task { await more() } }
        }
    }

    private var emptyLine: String {
        if failed { return "The feed did not load. Pull down to try again." }
        switch filter {
        case .everyone: return "Nothing new yet."
        case .following: return following.isEmpty
            ? "Follow people to see the trees they add here."
            : "Nobody you follow has added anything yet."
        case .near: return located
            ? "Nothing new within 100 km of you yet."
            : "Turn on your location to see what is new near you."
        }
    }

    // MARK: - loading

    private func restart() async {
        generation += 1
        posts = []; last = nil; done = false; failed = false; busy = false
        await more()
        await fill()
    }

    /// A filter shows only part of each page; read on until it has a screen
    /// of posts or the server has no more (the feed is a few hundred rows).
    private func fill() async {
        var rounds = 0
        while shown.count < 6 && !done && !failed && rounds < 30 {
            let before = posts.count
            await more()
            if posts.count == before { break }
            rounds += 1
        }
    }

    private func more() async {
        guard !busy, !done, !failed else { return }
        let gen = generation
        busy = true
        let token = await account.freshToken()
        let n = filter == .everyone ? FeedPosts.pageSize : 48
        let answer = await FeedPosts.page(after: last, n: n, token: token)
        guard gen == generation else { return }
        busy = false
        guard let page = answer else { failed = true; return }
        var prev = last
        var seen = Set(posts.map(\.post.key))
        for p in page where seen.insert(p.key).inserted {
            posts.append((post: p, prev: prev))
            prev = p
        }
        if let l = page.last { last = l }
        if page.count < n { done = true }
    }

    private func loadFollowing() async {
        guard let me = account.session?.userId else { following = []; return }
        let ids = await profiles.followingIds(of: me, token: await account.freshToken())
        following = Set(ids.map { $0.lowercased() })
    }

    private func openAuthor(_ p: FeedPosts.Post, prev: FeedPosts.Post?) {
        if let id = p.author_id, account.isSignedIn { navigator.push = .person(id); return }
        nudge.require(.general) {
            Task { @MainActor in
                let token = await account.freshToken()
                if let id = await FeedPosts.author(of: p, after: prev, token: token) {
                    navigator.push = .person(id)
                }
            }
        }
    }
}

/// The double tap that hearts a visitor's photograph (Instagram's), only on a
/// post that has one to like.
private struct DoubleTapLike: ViewModifier {
    let id: String?
    func body(content: Content) -> some View {
        if let id { content.doubleTapHeart(id) } else { content }
    }
}

/// A label on the photograph: CollectedTile's TagPill a size up for a
/// full-width picture (12 semibold, moss on white, a capsule 10 in).
struct FeedPill: View {
    let text: String
    var body: some View {
        Text(text)
            .font(.system(size: 12, weight: .semibold))
            .foregroundStyle(Brand.moss)
            .lineLimit(1)
            .padding(.horizontal, 9).padding(.vertical, 5)
            .background(Brand.surface, in: .capsule)
    }
}

/// The face in a post's byline: their picture, else their initial on moss,
/// 36 round; a private profile gets the plain circle.
struct FeedFace: View {
    let name: String
    let avatar: String?
    let known: Bool
    var body: some View {
        Group {
            if let a = avatar, let u = URL(string: a) {
                AsyncImage(url: u) { $0.resizable().scaledToFill() } placeholder: { Brand.moss.opacity(0.15) }
            } else if known {
                Text(String(name.prefix(1)))
                    .font(.system(size: 15, weight: .bold))
                    .foregroundStyle(Brand.moss)
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                    .background(Brand.mossTint)
            } else {
                Brand.surfaceMuted
            }
        }
        .frame(width: 36, height: 36)
        .clipShape(.circle)
        .accessibilityHidden(true)
    }
}
