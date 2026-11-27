// WHERE A TREE WAS OPENED FROM (Kit/TreeSource.swift, Hidde 2026-11-27:
// "kunnen we dit uberhaupt toevoegen op alle paginas dat we zien waar mensen
// klikken op bomen wat werkt en niet?").
//
// `tree_opened` carries `from`, in the iPhone's words: the tab, then the page
// under the tree ("map", "discover/collection", "feed/person", "discover/tree"),
// or the name of the tap that opened it ("discover/best", "search", "link").
// The page comes from the stack; the finer name from the tap, read once and
// only just after. Nothing is kept on the device: one string in memory.

package app.ancienttrees.ui

object TreeSource {
    private var pending: Pair<String, Long>? = null

    /** A tap that is about to open a tree, named. */
    fun mark(name: String) {
        pending = name to System.currentTimeMillis()
    }

    /** The tap's name if it came in the last two seconds, else the page; cleared either way. */
    fun take(page: String): String {
        val p = pending
        pending = null
        return if (p != null && System.currentTimeMillis() - p.second < 2000) p.first else page
    }

    /** A page's kind in the iPhone's Route words ("collection", "person", "tree"). */
    fun kind(p: Page): String = when (p) {
        is Page.TreePage -> "tree"
        is Page.FeedTree -> "feedPost"
        is Page.Mine -> "mine"
        is Page.Shared -> "shared"
        is Page.Species -> "species"
        is Page.TreeMap -> "treeMap"
        is Page.Person -> "person"
        is Page.People -> "people"
        is Page.Discover -> when (p.page) {
            is DiscoverPage.Collection -> "collection"
            is DiscoverPage.Index -> "index"
            DiscoverPage.Visitors -> "visitors"
            DiscoverPage.Activity -> "activity"
        }
        Page.Settings -> "settings"
        Page.Privacy -> "privacy"
    }

    /** The tab's name as the iPhone writes it (ContentView.treePage). */
    fun tabName(tab: Int): String = when (tab) {
        0 -> "map"
        1 -> "discover"
        2 -> "my-trees"
        4 -> "feed"
        else -> "tab$tab"
    }

    /** The tab, plus the page under the tree when it was not opened from the tab's first screen. */
    fun page(tab: Int, stack: List<Page>): String =
        if (stack.size < 2) tabName(tab) else tabName(tab) + "/" + kind(stack[stack.size - 2])
}
