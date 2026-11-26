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
    /// ZOOMED OUT OR ONE BIG (Hidde, 2026-11-26: "heel weinig boom per pixel",
    /// then "de boomfeed sws standaard juist op de uitgezoomde versie", "zoals
    /// bij de feed op web nu met de verschillende grote plaatjes"): the
    /// website's /visitors masonry, two columns of whole photographs each at
    /// its own shape (Pinterest's and Unsplash's, CONVENTIONS.md "A feed of
    /// visitors' photographs"), is where the tab opens; one big post at a time
    /// is the other half of the switch. In memory only (hard rule 11).
    @State private var grid = !ProcessInfo.processInfo.arguments.contains("-feedbig")
    /// The post the big view scrolls to after a tile was tapped.
    @State private var jumpTo: String?
    @Namespace private var layoutLine
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
                        if grid {
                            // People you may know above the photographs,
                            // where Polarsteps puts its row on Activity.
                            if account.isSignedIn && filter == .everyone {
                                FeedPeopleRow(following: following)
                            }
                            tiles(list, width: geo.size.width)
                                .padding(.horizontal, -Self.edge)
                                .padding(.top, 4)
                        } else {
                            ForEach(Array(list.enumerated()), id: \.element.post.key) { i, it in
                                post(it.post, prev: it.prev, width: width)
                                    .id("feed-\(i)")
                                    .onAppear { if i >= list.count - 6 { Task { await more() } } }
                                // People you may know after the second post,
                                // where Instagram's "Suggested for you" sits.
                                if i == 1 && account.isSignedIn && filter == .everyone {
                                    FeedPeopleRow(following: following).id("feed-people")
                                }
                            }
                        }
                        footer(list.isEmpty)
                    }
                    .padding(.horizontal, Self.edge)
                    .padding(.top, 6)
                    .padding(.bottom, 100)        // clear of the floating tab bar
                }
                .refreshable { await restart() }
                .onChange(of: jumpTo) { _, id in
                    guard let id else { return }
                    Task { @MainActor in
                        try? await Task.sleep(for: .milliseconds(50))
                        proxy.scrollTo(id, anchor: .top)
                        jumpTo = nil
                    }
                }
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
            HStack(alignment: .firstTextBaseline) {
                Text("Feed")
                    .font(.screenTitle)
                    .foregroundStyle(Brand.ink)
                Spacer(minLength: 8)
                // ADD FRIENDS, Polarsteps' person with a plus top right of
                // Activity: Find people, which asks a signed-out person to
                // sign in (People.swift).
                Button { navigator.push = .findPeople } label: {
                    Image(systemName: "person.badge.plus")
                        .font(.system(size: 19, weight: .medium))
                        .foregroundStyle(Brand.ink)
                        .frame(width: 44, height: 44)
                        .background(Brand.surface, in: .circle)
                        .overlay { Circle().strokeBorder(Brand.hairline, lineWidth: 1) }
                }
                .buttonStyle(.plain)
                .accessibilityLabel("Find people")
                .accessibilityIdentifier("feed-find-people")
                .alignmentGuide(.firstTextBaseline) { d in d[VerticalAlignment.center] + 12 }
            }
            HStack(spacing: 8) {
                ForEach(FeedPosts.Filter.allCases, id: \.self) { f in
                    FilterChip(label: f.label, icon: nil, on: filter == f) { choose(f) }
                        .accessibilityIdentifier("feed-filter-\(f.rawValue)")
                }
            }
            layoutToggle
                .padding(.horizontal, -Self.edge)
        }
    }

    /// Big or three across: Instagram's profile tabs, read off its page on
    /// 2026-11-26 (CONVENTIONS.md "A feed shown big or as a grid"): a row
    /// across the full width, one glyph per half, the one on screen in ink
    /// with a line under its half, the other soft, a hairline under the row.
    /// The grid glyph is Instagram's, a square split three by three; the big
    /// view's is two stacked cards, a feed of posts.
    private var layoutToggle: some View {
        HStack(spacing: 0) {
            ForEach([true, false], id: \.self) { g in
                Button {
                    withAnimation(.snappy(duration: 0.2)) { grid = g }
                    Measure.event("feed_layout", ["layout": g ? "grid" : "big"])
                } label: {
                    Image(systemName: g ? "square.grid.2x2" : "rectangle.grid.1x2")
                        .font(.system(size: 20, weight: .regular))
                        .foregroundStyle(grid == g ? Brand.ink : Brand.inkSoft.opacity(0.6))
                        .frame(maxWidth: .infinity, minHeight: 44)
                        .overlay(alignment: .bottom) {
                            if grid == g {
                                Rectangle().fill(Brand.ink).frame(height: 1.5)
                                    .matchedGeometryEffect(id: "feed-layout-line", in: layoutLine)
                            }
                        }
                        .contentShape(.rect)
                }
                .buttonStyle(.plain)
                .accessibilityLabel(g ? "Show as a grid" : "Show one by one")
                .accessibilityAddTraits(grid == g ? .isSelected : [])
                .accessibilityIdentifier(g ? "feed-layout-grid" : "feed-layout-big")
            }
        }
        .overlay(alignment: .bottom) { Rectangle().fill(Brand.hairline).frame(height: 0.5) }
    }

    /// The masonry: two columns 12 apart, each tile into the shorter column
    /// so the order reads across, the photograph whole at its own shape (4:5
    /// when the server has no size), the place on it, the tree's name and who
    /// under it, the website's tile (VisitorPhotos.swift's numbers). A tap
    /// opens the tree, as a tile on the website does.
    private func tiles(_ list: [(post: FeedPosts.Post, prev: FeedPosts.Post?)], width: CGFloat) -> some View {
        let gap: CGFloat = 12
        let colWidth = (width - Self.edge * 2 - gap) / 2
        func ratio(_ p: FeedPosts.Post) -> CGFloat {
            guard let w = p.photo_w, let h = p.photo_h, w > 0, h > 0 else { return 5.0 / 4.0 }
            return min(CGFloat(h) / CGFloat(w), 1.6)
        }
        var cols: [[(Int, FeedPosts.Post, FeedPosts.Post?)]] = [[], []]
        var heights: [CGFloat] = [0, 0]
        for (i, it) in list.enumerated() {
            let c = heights[1] < heights[0] ? 1 : 0
            cols[c].append((i, it.post, it.prev))
            heights[c] += colWidth * ratio(it.post) + 70
        }
        return HStack(alignment: .top, spacing: gap) {
            ForEach(0..<2, id: \.self) { c in
                LazyVStack(alignment: .leading, spacing: 16) {
                    ForEach(cols[c], id: \.1.key) { entry in
                        tile(entry.1, prev: entry.2, width: colWidth, ratio: ratio(entry.1))
                            .onAppear { if entry.0 >= list.count - 8 { Task { await more() } } }
                    }
                }
                .frame(width: colWidth, alignment: .top)
            }
        }
        .padding(.horizontal, Self.edge)
    }

    private func tile(_ p: FeedPosts.Post, prev: FeedPosts.Post?, width: CGFloat, ratio: CGFloat) -> some View {
        let known = p.tree_id.flatMap { catalogue.tree($0) }
        let route: Route = if let shared = p.sharedId { .shared(shared) }
            else if let k = known { .tree(k.id) } else { .feedPost(p) }
        let name = p.author_name ?? "A visitor"
        return VStack(alignment: .leading, spacing: 6) {
            NavigationLink(value: route) {
                TreePhoto(url: p.photo) { Brand.surfaceMuted }
                    .frame(width: width, height: width * ratio)
                    .overlay(alignment: .bottomLeading) {
                        if !p.place.isEmpty { TagPill(text: p.place).padding(6) }
                    }
                    .clipShape(.rect(cornerRadius: 12, style: .continuous))
                    .contentShape(.rect)
            }
            .buttonStyle(.plain)
            .modifier(DoubleTapLike(id: p.likeId))
            .accessibilityLabel(p.place.isEmpty ? p.tree_name : "\(p.tree_name), \(p.place)")
            .accessibilityIdentifier("feed-tile")
            Text(p.tree_name)
                .font(.brand(14, .bold, relativeTo: .subheadline))
                .foregroundStyle(Brand.ink)
                .lineLimit(2)
                .fixedSize(horizontal: false, vertical: true)
            HStack(spacing: 5) {
                VisitorFace(name: name, avatar: p.author_avatar)
                Text(name).font(.system(size: 12, weight: .medium)).foregroundStyle(Brand.inkSoft).lineLimit(1)
                if let when = SentAgo.short(p.published_at) {
                    Text("· \(when)").font(.system(size: 12)).foregroundStyle(Brand.inkSoft.opacity(0.75))
                        .lineLimit(1).fixedSize()
                }
            }
            .contentShape(.rect)
            .onTapGesture { if p.author_name != nil { openAuthor(p, prev: prev) } }
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
        let known = p.tree_id.flatMap { catalogue.tree($0) }
        let tree = known ?? FeedPosts.stub(p)
        // A photograph of a tree we have opens that tree, checked or not (Hidde,
        // 2026-11-26: "Yes, fix both"); a tree they added and nobody has
        // checked yet opens its share page (SharedTreeView).
        let route: Route = if let k = known { .tree(k.id) }
            else if let shared = p.sharedId { .shared(shared) } else { .feedPost(p) }
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
                    .accessibilityLabel(p.place.isEmpty ? p.tree_name : "\(p.tree_name), \(p.place)")
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
                // 44 to hit, its own height to lay out (the ambassador tag's
                // way in Collect.swift): a one-line name was a 24 point target
                // (appfit SMALL, run 45810490360).
                .padding(.vertical, 10)
                .contentShape(.rect)
            }
            .buttonStyle(.plain)
            .padding(.vertical, -10)
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
            // Nothing to save before the check: no tree of ours exists yet.
            if p.isChecked { SaveHeart(tree: tree, look: .plain) }
            if let url = Shared.page(p.url, from: "feed") {
                ShareLink(item: url, subject: Text(p.tree_name),
                          message: Text(p.place.isEmpty ? "\(p.tree_name)." : "\(p.tree_name), \(p.place).")) {
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
