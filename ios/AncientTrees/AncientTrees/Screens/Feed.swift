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
    /// Discover's sliding header: away while reading down, back on scroll up.
    @State private var headerHidden = false
    @State private var headerHeight: CGFloat = 160
    /// The signed-in state the list was loaded for (see the `.task` below).
    @State private var loadedFor: Bool?
    /// The accounts you follow, asked once per sign-in for Following.
    @State private var following: Set<String> = []

    private static let edge: CGFloat = 16

    private var shown: [(post: FeedPosts.Post, prev: FeedPosts.Post?)] {
        let o: (lat: Double, lng: Double)? = located ? origin : nil
        // CHECKED ONLY (Hidde, 2026-11-26: "eerst bomen een pagina laten maken
        // voordat we ze laten zien ... de helft heeft wel een bookmark, de
        // andere niet"): a share the judge has not looked at yet waits, 10 to
        // 30 minutes, until it is a tree with its page, save and heart.
        return posts.filter { $0.post.isChecked && FeedPosts.passes($0.post, filter, following: following, origin: o) }
    }

    var body: some View {
        GeometryReader { geo in
            let width = geo.size.width - Self.edge * 2
            ScrollViewReader { proxy in
                ScrollView {
                    LazyVStack(alignment: .leading, spacing: 28) {
                        // WHAT THE FILTER NEEDS, ON TOP (Hidde, 2026-11-26):
                        // Following with nobody followed yet shows People you
                        // may know first; Near you without a location asks
                        // for it first.
                        if filter == .following && account.isSignedIn && following.isEmpty {
                            FeedPeopleRow(following: following)
                        }
                        if filter == .near && !located { NearYouCard() }
                        let list = shown
                        if grid {
                            // People you may know between the photographs,
                            // never opening the page (Hidde, 2026-11-26: "niet
                            // de pagina mee openen ... ergens tussendoor"), as
                            // Instagram's "Suggested for you" comes mid-feed.
                            // Where both columns end level (FeedPosts.evenCut).
                            let colW = (geo.size.width - Self.edge * 2 - 12) / 2
                            let cut = FeedPosts.evenCut(list.map { Double(colW * Self.ratio($0.post) + 70) })
                            tiles(Array(list.prefix(cut)), width: geo.size.width, offset: 0, total: list.count)
                                .padding(.horizontal, -Self.edge)
                                .padding(.top, 4)
                            if account.isSignedIn && filter == .everyone && list.count > cut {
                                FeedPeopleRow(following: following).id("feed-people")
                            }
                            if list.count > cut {
                                tiles(Array(list.dropFirst(cut)), width: geo.size.width, offset: cut, total: list.count)
                                    .padding(.horizontal, -Self.edge)
                            }
                        } else {
                            ForEach(Array(list.enumerated()), id: \.element.post.key) { i, it in
                                post(it.post, prev: it.prev, width: width)
                                    .id("feed-\(i)")
                                    .onAppear { if i >= list.count - 6 { Task { await more() } } }
                                if i == 2 && account.isSignedIn && filter == .everyone {
                                    FeedPeopleRow(following: following)
                                }
                            }
                        }
                        footer(list.isEmpty)
                    }
                    .padding(.horizontal, Self.edge)
                    .padding(.top, 6)
                    .padding(.bottom, 100)        // clear of the floating tab bar
                    // The top, for a tap on the Feed tab; the header itself is
                    // pinned above the list (safeAreaInset below), 16 above
                    // the first post as before.
                    .background(alignment: .top) { Color.clear.frame(height: 1).id("feed-top") }
                }
                .refreshable { await restart() }
                // On the list itself, never around the pinned header: there it
                // took the header's buttons' own names away (SignedOutWalk).
                .accessibilityIdentifier("feed")
                // DISCOVER'S HEADER (Hidde, 2026-11-26: "als je naar beneden
                // scrolt en weer omhooggaat, komt die titel naar beneden ...
                // datzelfde bij feed"): reading down slides it away, any
                // scroll back up brings it back, near the top it always shows.
                .onScrollGeometryChange(for: CGFloat.self) { $0.contentOffset.y + $0.contentInsets.top } action: { old, new in
                    let hide: Bool
                    if new < headerHeight { hide = false }
                    else if new > old + 1 { hide = true }
                    else if new < old - 1 { hide = false }
                    else { return }
                    if hide != headerHidden {
                        withAnimation(.snappy(duration: 0.25)) { headerHidden = hide }
                    }
                }
                .safeAreaInset(edge: .top, spacing: 0) {
                    header
                        .padding(.horizontal, Self.edge)
                        .padding(.top, 6)
                        .padding(.bottom, 6)
                        .background(Brand.ground.ignoresSafeArea(edges: .top))
                        .onGeometryChange(for: CGFloat.self) { $0.size.height } action: { headerHeight = $0 }
                        .offset(y: headerHidden ? -(headerHeight + 80) : 0)
                }
                // While the header is away the clock keeps a solid strip.
                .overlay(alignment: .top) {
                    GeometryReader { g in
                        Brand.ground
                            .frame(height: g.safeAreaInsets.top)
                            .offset(y: -g.safeAreaInsets.top)
                    }
                    .frame(height: 0)
                    .opacity(headerHidden ? 1 : 0)
                    .allowsHitTesting(false)
                }
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
                    headerHidden = false
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
        }
        .brandGround()
        .task(id: account.isSignedIn) {
            // ONLY WHEN SIGNING IN OR OUT, never because the tab came back
            // into view. A `.task` runs again each time its view reappears, so
            // Back from a tree or a profile emptied the list and loaded it
            // again, and the Feed came back scrolled somewhere else (Hidde,
            // 2026-11-26: "niet op het juiste punt in de feed terug";
            // BackKeepsPlaceWalk). Pull to refresh still starts it over.
            // Back keeps the Feed exactly as it was: nothing is read again here
            // (reading who you follow on return moved and dropped the tiles,
            // BackKeepsPlaceWalk, 2026-11-27). Following reads it when chosen.
            if loadedFor == account.isSignedIn, !posts.isEmpty { return }
            loadedFor = account.isSignedIn
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
                // Signed out it asks for a sign-in first, then goes on to
                // Find people (Hidde, 2026-11-26: "uitgelogd ... gewoon naar
                // een loginscherm"), as every account control does.
                Button {
                    if account.isSignedIn { navigator.push = .findPeople }
                    else { nudge.require(.general) { navigator.push = .findPeople } }
                } label: {
                    HeaderDisc(symbol: "person.badge.plus")
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
    /// A tile's photograph shape: its own, at most 1.6 tall, 4:5 without a size.
    static func ratio(_ p: FeedPosts.Post) -> CGFloat {
        guard let w = p.photo_w, let h = p.photo_h, w > 0, h > 0 else { return 5.0 / 4.0 }
        return min(CGFloat(h) / CGFloat(w), 1.6)
    }

    private func tiles(_ list: [(post: FeedPosts.Post, prev: FeedPosts.Post?)], width: CGFloat,
                       offset: Int = 0, total: Int = 0) -> some View {
        let gap: CGFloat = 12
        let colWidth = (width - Self.edge * 2 - gap) / 2
        func ratio(_ p: FeedPosts.Post) -> CGFloat { Self.ratio(p) }
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
                            .onAppear { if offset + entry.0 >= max(total, list.count) - 8 { Task { await more() } } }
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
            // The website's /visitors tile (Hidde, 2026-11-19 and 11-20): the
            // save on the photograph's top right, over the link and not in it,
            // and the heart at the end of the byline. Saving is the tree's,
            // the heart the person's photograph; a share not checked yet has
            // neither (no tree of ours, no published photograph).
            .overlay(alignment: .topTrailing) {
                if p.isChecked { SaveHeart(tree: known ?? FeedPosts.stub(p), look: .onPhoto).padding(6) }
            }
            Text(p.tree_name)
                .font(.brand(14, .bold, relativeTo: .subheadline))
                .foregroundStyle(Brand.ink)
                .lineLimit(2)
                .fixedSize(horizontal: false, vertical: true)
            // TOP, not centre (Hidde, 2026-11-26: "de hartjes bij de tiles een
            // beetje raar uitgelijnd"): the name line hangs at the top of its
            // 44 tap room, so a centred heart stood 13 points under it.
            HStack(alignment: .top, spacing: 2) {
                // The name opens the profile (signed out it asks first), a
                // button of its own beside the heart, never around it.
                let who = HStack(spacing: 5) {
                    VisitorFace(name: name, avatar: p.author_avatar, size: 18)
                    Text(name).font(.system(size: 13, weight: .medium)).foregroundStyle(Brand.inkSoft).lineLimit(1)
                    if let when = SentAgo.short(p.published_at) {
                        Text("· \(when)").font(.system(size: 13)).foregroundStyle(Brand.inkSoft.opacity(0.75))
                            .lineLimit(1).fixedSize()
                    }
                }
                // Apple's 44 to tap, the room hanging below the line as
                // VisitorLine's does, so nothing moves on screen.
                .frame(minHeight: 44, alignment: .top)
                .contentShape(.rect)
                if p.author_name != nil {
                    Button { openAuthor(p, prev: prev) } label: { who }
                        .buttonStyle(.plain)
                        .accessibilityLabel("\(name), open profile")
                        .accessibilityIdentifier("feed-author")
                } else {
                    who.accessibilityElement(children: .combine)
                }
                Spacer(minLength: 0)
                if let like = p.likeId { PhotoHeart(photoId: like, size: 16).frame(height: 18) }
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
        // Following asks again who you follow, so somebody followed a moment
        // ago is in it (release walk 2026-11-26, pass 1).
        Task { if f == .following { await loadFollowing() }; await fill() }
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
            // ONE CARD IN TWO SIZES (Hidde, 2026-11-26: "de bookmark ... rechtsboven
            // ... laten staan", "nu lijkt het overal maar een beetje random
            // geplaatst"): the save top right on the photograph as on every
            // tree card and on the grid's tiles, over the link and not in it;
            // the heart at the end of the person's line; share on the tree's
            // own page, top right, as everywhere (Airbnb's listing card: save
            // on the card, share on the page).
            .overlay(alignment: .topTrailing) {
                if p.isChecked { SaveHeart(tree: tree, look: .onPhoto).padding(6) }
            }
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
        return HStack(spacing: 4) {
            if p.author_name == nil {
                line.accessibilityElement(children: .combine)
            } else {
                Button { openAuthor(p, prev: prev) } label: { line }
                    .buttonStyle(.plain)
                    .accessibilityLabel("\(name), open profile")
                    .accessibilityIdentifier("feed-author")
            }
            // The heart, the person's photograph, at the end of their line as
            // on the grid's tiles and the website's (beside the name, never in it).
            if let like = p.likeId { PhotoHeart(photoId: like, size: 17) }
        }
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
        case .near: return located ? "Nothing new within 100 km of you yet." : ""
        }
    }

    // MARK: - loading

    /// PULL TO REFRESH (Hidde, 2026-11-26: "the feed did not load. Pull down
    /// again"; FeedRefreshWalk). Emptying the list first made SwiftUI end the
    /// refresh's own task, which cut the request off, and a cut-off request
    /// read as a failure. So the request runs in a task of its own, and the
    /// posts on screen stay until the new first page is in, as Instagram's
    /// refresh does; a refresh that fails keeps what was there.
    private func restart() async {
        // Who you follow comes again too: pull to refresh after following
        // somebody left Following empty (release walk 2026-11-26, pass 1).
        await Task { @MainActor in await loadFollowing(); await reload() }.value
    }

    private func reload() async {
        generation += 1
        let gen = generation
        busy = true
        let token = await account.freshToken()
        let n = filter == .everyone ? FeedPosts.pageSize : 48
        let answer = await FeedPosts.page(after: nil, n: n, token: token)
        guard gen == generation else { return }
        busy = false
        guard let page = answer else {
            if posts.isEmpty { failed = true }
            return
        }
        posts = []; last = nil; done = false; failed = false
        take(page, n: n)
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
        take(page, n: n)
    }

    private func take(_ page: [FeedPosts.Post], n: Int) {
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
        // Only when it changed: the same set written again redrew the people
        // row and moved the Feed on Back from a tree (BackKeepsPlaceWalk,
        // run 45904954877, after the reload on return was added).
        let now = Set(ids.map { $0.lowercased() })
        if now != following { following = now }
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

/// Near you without a location: the card that asks for it, EmptyPlaceCard's
/// shape, with the map's own Location off control as its action.
private struct NearYouCard: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 14) {
            VStack(alignment: .leading, spacing: 8) {
                Image(systemName: "location")
                    .font(.system(size: 22, weight: .medium))
                    .foregroundStyle(Brand.inkSoft.opacity(0.6))
                    .accessibilityHidden(true)
                Text("See what is new near you")
                    .font(.system(size: 16, weight: .semibold))
                    .foregroundStyle(Brand.ink)
                Text("Turn on your location to see the trees people added within 100 km.")
                    .font(.system(size: 14))
                    .foregroundStyle(Brand.inkSoft)
                    .fixedSize(horizontal: false, vertical: true)
            }
            LocationOffChip()
        }
        .padding(16)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(Brand.surfaceMuted, in: .rect(cornerRadius: 14))
        .accessibilityElement(children: .contain)
        .accessibilityIdentifier("feed-near-card")
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
