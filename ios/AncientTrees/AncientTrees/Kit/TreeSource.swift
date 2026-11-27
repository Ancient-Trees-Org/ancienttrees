// WHERE A TREE WAS OPENED FROM (Hidde, 2026-11-27: "kunnen we dit uberhaupt
// toevoegen op alle paginas dat we zien waar mensen klikken op bomen wat werkt
// en niet?").
//
// `tree_opened` carries `from`: the tab, then the page the tree was opened on
// ("discover", "map", "feed", "my-trees", "map/city", "discover/collection",
// "feed/person", "discover/tree" for a tree reached from another tree's page).
// On a page made of shelves the shelf is added where the tile says so
// ("discover/best", "discover/trending", "discover/visitors"), and a few doors
// that are not a page say what they are ("search", "link", "nearby").
//
// Two halves. The page comes from the navigation stack itself (ContentView's
// destination for `.tree`), so every screen is covered without each one
// remembering to say so. The finer name comes from the tap: `.opensTree(from:)`
// on a link counts the tap without taking it, exactly as `.countsShare` does,
// and the tree page takes that name if the tap was a moment ago.
//
// Nothing is kept on the device: one string in memory, cleared when read.

import SwiftUI

@MainActor
enum TreeSource {
    private static var pending: (name: String, at: Date)?

    /// A tap that is about to open a tree, named.
    static func mark(_ name: String) { pending = (name, Date()) }

    /// The name of the tap that opened this tree, if there was one in the last
    /// two seconds, else the page; cleared either way, so a later tree opened
    /// some other way never inherits it.
    static func take(page: String) -> String {
        defer { pending = nil }
        if let p = pending, Date().timeIntervalSince(p.at) < 2 { return p.name }
        return page
    }

    /// A route's kind as a word: "city", "collection", "person", "tree".
    static func kind(_ route: Route) -> String {
        let s = String(describing: route)
        return String(s.prefix { $0 != "(" })
    }

    /// The page a tree opened on: the tab, plus the screen under it when the
    /// tree was not opened from the tab's own first screen.
    static func page(tab: String, path: [Route], route: Route) -> String {
        guard let i = path.lastIndex(of: route), i > 0 else { return tab }
        return tab + "/" + kind(path[i - 1])
    }
}

private struct TreeFromKey: EnvironmentKey {
    static let defaultValue = "unknown"
}

extension EnvironmentValues {
    /// The page a tree page was opened on (TreeSource.page), set by the stack.
    var treeFrom: String {
        get { self[TreeFromKey.self] }
        set { self[TreeFromKey.self] = newValue }
    }
}

extension View {
    /// Names the tap that opens a tree, without taking the tap from the link.
    func opensTree(from name: String) -> some View {
        simultaneousGesture(TapGesture().onEnded { TreeSource.mark(name) })
    }
}
