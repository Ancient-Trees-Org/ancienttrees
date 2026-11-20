// EVERY PHOTOGRAPH VISITORS SENT, the See all behind Discover's "New from
// visitors" (Hidde, 2026-11-18: "bouw in nieuw gesprek beide", the website's
// /visitors in the app).
//
// Convention: Unsplash's and Pinterest's photo feed (CONVENTIONS.md "A feed of
// visitors' photographs: whole photographs, masonry, endless", 2026-11-18): a
// masonry of WHOLE photographs, each at its own shape, newest sent first, each
// tile into the shorter column so the order reads across, 24 more as the end
// comes near, one line when there is nothing more. Endless because the items
// are endless and similar (CONVENTIONS.md 2026-10-10).
//
// Each tile is the row's own card: the visitor's photograph with the city tag
// on it (CollectedTile's TagPill, 6 points in), and under it the same line,
// the same 7 points apart, from VisitorLine below, which the row uses too.
// The row crops to 3:4; here a portrait phone photograph keeps its crown and
// its foot. Two columns 12 apart, the shelf's own gap, 16 from the edges.
//
// From the server (NewFromVisitors.page), read each time the page opens;
// nothing kept on the device (hard rule 11). A photograph whose tree or whose
// picture the feed does not carry yet is skipped, as the row skips it.
import SwiftUI

struct VisitorPhotosView: View {
    let catalogue: Catalogue
    @Environment(Account.self) private var account
    @Environment(Navigator.self) private var navigator
    @Environment(Nudge.self) private var nudge

    /// A tile: the server's row, the one the server sent before it (the
    /// cursor that returns exactly this row, for the name after a sign-in),
    /// and what the feed knows of its tree and photograph.
    struct Item: Identifiable {
        let row: NewFromVisitors.Row
        let prev: NewFromVisitors.Row?
        let tree: Tree
        let shot: Photo
        var id: UUID { row.sighting_id }
        /// Height over width; the website's 3:4 when the feed has no size.
        var ratio: CGFloat {
            guard let w = shot.width, let h = shot.height, w > 0, h > 0 else { return 4.0 / 3.0 }
            return CGFloat(h) / CGFloat(w)
        }
    }

    /// Every row the server sent, each with the one before it. Which of them
    /// are tiles is asked of the catalogue as the page draws, as the row on
    /// Discover does, so a photograph the feed did not carry yet (a fresh
    /// install, before the new feed) appears the moment the feed does.
    @State private var rows: [(row: NewFromVisitors.Row, prev: NewFromVisitors.Row?)] = []
    private var items: [Item] {
        var seen = Set<UUID>()
        return rows.compactMap { r in
            guard seen.insert(r.row.id).inserted, let t = catalogue.tree(r.row.tree_id),
                  let s = NewFromVisitors.shot(r.row, in: t) else { return nil }
            return Item(row: r.row, prev: r.prev, tree: t, shot: s)
        }
    }
    /// The last row the server sent, tile or not: the next page starts after it.
    @State private var last: NewFromVisitors.Row?
    @State private var busy = false
    @State private var done = false
    /// Which start of the page a load belongs to: a load still on its way
    /// when the page starts again (a sign-in) is dropped, never counted as
    /// the end.
    @State private var generation = 0

    private static let gap: CGFloat = 12
    private static let edge: CGFloat = 16
    private static let tileShape = RoundedRectangle(cornerRadius: 12, style: .continuous)

    var body: some View {
        GeometryReader { geo in
            let width = (geo.size.width - Self.edge * 2 - Self.gap) / 2
            ScrollView {
                VStack(alignment: .leading, spacing: 0) {
                    Text("Photographs people took at the trees, newest first.")
                        .font(.subheadline).foregroundStyle(Brand.inkSoft)
                        .fixedSize(horizontal: false, vertical: true)
                        .padding(.bottom, 16)
                    let shown = items
                    let cols = columns(shown, width)
                    HStack(alignment: .top, spacing: Self.gap) {
                        ForEach(0..<2, id: \.self) { c in
                            LazyVStack(alignment: .leading, spacing: 0) {
                                ForEach(cols[c]) { tile($0, of: shown, width: width) }
                            }
                            .frame(width: width, alignment: .top)
                        }
                    }
                    footer(shown.isEmpty)
                }
                .padding(.horizontal, Self.edge).padding(.top, 6)
                .padding(.bottom, 80)
            }
            .accessibilityIdentifier("visitor-photos")
        }
        .brandGround()
        .navigationTitle("New from visitors")
        .navigationBarTitleDisplayMode(.inline)
        // Signed in, the names come with the account id and open the profile
        // at once; the page starts again when that changes.
        .task(id: account.isSignedIn) {
            generation += 1
            rows = []; last = nil; done = false; busy = false
            await more()
        }
    }

    /// Each tile into the shorter column, in order (Pinterest), measured by
    /// the photograph's own shape plus the line under it.
    private func columns(_ items: [Item], _ width: CGFloat) -> [[Item]] {
        var cols: [[Item]] = [[], []]
        var heights: [CGFloat] = [0, 0]
        for it in items {
            let c = heights[1] < heights[0] ? 1 : 0
            cols[c].append(it)
            heights[c] += width * it.ratio + 7 + VisitorTitle.height + 2 + VisitorLine.height
        }
        return cols
    }

    private func tile(_ it: Item, of shown: [Item], width: CGFloat) -> some View {
        VStack(alignment: .leading, spacing: 7) {
            NavigationLink(value: Route.tree(it.tree.id)) {
                TreePhoto(url: it.shot.card) { Brand.surfaceMuted }
                    .frame(width: width, height: width * it.ratio)
                    .overlay(alignment: .bottomLeading) { TagPill(text: it.tree.city).padding(6) }
                    .clipShape(Self.tileShape)
                    .contentShape(.rect)
                    .accessibilityElement(children: .ignore)
                    .accessibilityLabel("\(it.tree.name), \(it.tree.city)")
            }
            .buttonStyle(.plain)
            .accessibilityIdentifier("visitor-tile")
            // The save on the photograph's top right, as on every card
            // (Hidde, 2026-11-19: "een bookmark icontje bij elke boom"; the
            // web's /visitors tile carries the same). Over the link, not in
            // it, so a tap saves and does not open the tree.
            .overlay(alignment: .topTrailing) { SaveHeart(tree: it.tree, look: .onPhoto).padding(6) }
            VStack(alignment: .leading, spacing: 2) {
                NavigationLink(value: Route.tree(it.tree.id)) { VisitorTitle(name: it.tree.name, width: width) }
                    .buttonStyle(.plain)
                VisitorLine(row: it.row, width: width) { _ in open(it) }
            }
        }
        .onAppear {
            // More as the end comes near: eight tiles before the last.
            if let i = shown.firstIndex(where: { $0.id == it.id }), i >= shown.count - 8 {
                Task { await more() }
            }
        }
    }

    @ViewBuilder private func footer(_ empty: Bool) -> some View {
        if done {
            if !empty {
                Text("You have seen every photograph so far.")
                    .font(.subheadline).foregroundStyle(Brand.inkSoft)
                    .frame(maxWidth: .infinity)
                    .padding(.top, 20)
            }
        } else {
            ProgressView()
                .frame(maxWidth: .infinity, minHeight: 60)
                .padding(.top, 12)
                .onAppear { Task { await more() } }
        }
    }

    private func more() async {
        guard !busy, !done else { return }
        let gen = generation
        busy = true
        let token = await account.freshToken()
        let answer = await NewFromVisitors.page(after: last, token: token)
        guard gen == generation else { return }
        busy = false
        // No answer: the page stops where it is, as the website's does.
        guard let page = answer else { done = true; return }
        let before = items.count
        var prev = last
        for r in page {
            rows.append((row: r, prev: prev))
            prev = r
        }
        if let l = page.last { last = l }
        if page.count < NewFromVisitors.pageSize { done = true }
        // A page whose photographs the feed does not carry yet added no tile,
        // and nothing on screen moved to ask again: ask for the next one now.
        if !done && items.count == before { await more() }
    }

    /// A visitor's name, tapped: Home's openVisitor. Signed out the server
    /// hands no account id, so after the sign-in the photograph's own row is
    /// asked again and the tap finishes on the profile it was for.
    private func open(_ it: Item) {
        if let id = it.row.author_id, account.isSignedIn { navigator.push = .person(id); return }
        nudge.require(.general) {
            Task { @MainActor in
                let token = await account.freshToken()
                if let id = await NewFromVisitors.author(of: it.row, after: it.prev, token: token) {
                    navigator.push = .person(id)
                }
            }
        }
    }
}

/// A visitor's face in a byline: their picture, else their initial on moss,
/// 16 points round. One view for the tiles and the tree page (2026-11-20).
struct VisitorFace: View {
    let name: String
    let avatar: String?

    var body: some View {
        Group {
            if let a = avatar, let u = URL(string: a) {
                AsyncImage(url: u) { $0.resizable().scaledToFill() } placeholder: { Brand.moss.opacity(0.15) }
            } else {
                Text(String(name.prefix(1)))
                    .font(.system(size: 9, weight: .bold))
                    .foregroundStyle(Brand.moss)
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                    .background(Brand.moss.opacity(0.15))
            }
        }
        .frame(width: 16, height: 16)
        .clipShape(.circle)
    }
}

/// The tree's name under a visitor's photograph, at most two lines, the
/// website's tile (Hidde, 2026-11-20: "A, met boomnaam"; CONVENTIONS.md "A
/// heart for a visitor's photograph ... who and when on it"): the city is the
/// tag on the photograph, the name says which tree, the line under it who.
struct VisitorTitle: View {
    let name: String
    let width: CGFloat
    /// Two lines of 14 point bold, what the masonry reserves for it.
    static let height: CGFloat = 38

    var body: some View {
        Text(name)
            .font(.brand(14, .bold, relativeTo: .subheadline))
            .foregroundStyle(Brand.ink)
            .lineLimit(2)
            .multilineTextAlignment(.leading)
            .fixedSize(horizontal: false, vertical: true)
            .frame(width: width, alignment: .leading)
    }
}

/// Who sent it: a small avatar and the name, one line, under a visitor's
/// photograph on Discover's row and on its See all page. The name of a public
/// profile shows to everyone; a tap opens the profile, and signed out it asks
/// for a sign-in first (Hidde, 2026-11-06, the Instagram and Pinterest way).
/// A generated name ("Green Fig 1965") prints and links like any other (Hidde,
/// 2026-11-07: "a visitor is weird that its unclickable just give the link to
/// their made up name"). Only a private profile has no name: "A visitor".
struct VisitorLine: View {
    let row: NewFromVisitors.Row
    let width: CGFloat
    let open: (NewFromVisitors.Row) -> Void

    /// Apple's 44 points to tap, on a 16 point line: the room hangs below
    /// the name, so nothing moves on screen and a tap on the photograph above
    /// still opens the tree.
    static let height: CGFloat = 44

    var body: some View {
        let real = row.author_name
        let name = real ?? "A visitor"
        let line = HStack(spacing: 5) {
            VisitorFace(name: name, avatar: row.author_avatar)
            Text(name)
                .font(.system(size: 12, weight: .medium))
                .foregroundStyle(Brand.inkSoft)
                .lineLimit(1)
            // When it was sent, the website's ".nfv-when" (Hidde, 2026-11-20):
            // never squeezed, so a long name gives way to it.
            if let when = SentAgo.short(row.published_at) {
                Text("· \(when)")
                    .font(.system(size: 12))
                    .foregroundStyle(Brand.inkSoft.opacity(0.75))
                    .lineLimit(1)
                    .fixedSize()
            }
        }
        .frame(width: width, alignment: .leading)
        // Under the label's own element, or the system measures only the
        // avatar and the name (appfit SMALL on iOS 18, 2026-11-07).
        .frame(minHeight: Self.height, alignment: .top)
        .contentShape(Rectangle())
        .accessibilityElement(children: .ignore)
        if real == nil {
            line.accessibilityLabel(name)
        } else {
            Button {
                open(row)
            } label: { line }
            .buttonStyle(.plain)
            .accessibilityLabel("\(name), open profile")
            .accessibilityIdentifier("visitor-name")
        }
    }
}
