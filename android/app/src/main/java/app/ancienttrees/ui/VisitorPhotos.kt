// EVERY PHOTOGRAPH VISITORS SENT, the See all behind Discover's "New from
// visitors" (Hidde, 2026-11-18: "bouw in nieuw gesprek beide"). The Android twin
// of ios Screens/VisitorPhotos.swift, read from that source.
//
// Convention: Unsplash's and Pinterest's photo feed (CONVENTIONS.md "A feed of
// visitors' photographs: whole photographs, masonry, endless", 2026-11-18): a
// masonry of WHOLE photographs, each at its own shape, newest sent first, each
// tile into the shorter column so the order reads across, 24 more as the end
// comes near, one line when there is nothing more.
//
// Each tile is the row's own card: the visitor's photograph with the city tag on
// it (TagPill, 6 in), and 7 under it the same VisitorLine the row uses. Two
// columns 12 apart, 16 from the edges, the intro 6 under the bar and 16 above the
// photographs, the end line 20 under them, the spinner 60 tall (iOS's numbers).
// From the server each time the page opens; nothing kept on the device.

package app.ancienttrees.ui

import androidx.compose.ui.platform.testTag
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.staggeredgrid.LazyVerticalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridCells
import androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridItemSpan
import androidx.compose.foundation.lazy.staggeredgrid.items
import androidx.compose.foundation.lazy.staggeredgrid.rememberLazyStaggeredGridState
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.CircularProgressIndicator

import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.derivedStateOf
import androidx.compose.runtime.rememberUpdatedState
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.runtime.snapshotFlow
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import app.ancienttrees.R
import app.ancienttrees.account.NewFromVisitors
import app.ancienttrees.feed.Catalogue
import app.ancienttrees.feed.Photo
import app.ancienttrees.feed.Tree
import kotlinx.coroutines.launch

/** A tile: the server's row, the row it sent before (the cursor for the name after a sign-in), the tree and photograph. */
private class VisitorItem(val row: NewFromVisitors.Row, val prev: NewFromVisitors.Row?, val tree: Tree, val shot: Photo) {
    /** Width over height; the website's 3:4 when the feed has no size. */
    val ratio: Float
        get() {
            val w = shot.width ?: 0
            val h = shot.height ?: 0
            return if (w > 0 && h > 0) w.toFloat() / h else 3f / 4f
        }
}

private val VP_SHAPE = RoundedCornerShape(12.dp)

@Composable
fun VisitorPhotosPage(catalogue: Catalogue, act: DiscoverActions, onBack: () -> Unit) {
    val brand = Brand.colors
    val scope = rememberCoroutineScope()
    // Every row the server sent, each with the one before it. Which are tiles is
    // asked of the catalogue as the page draws (VisitorPhotos.swift `items`), so a
    // photograph the feed did not carry yet appears the moment the feed does.
    val rows = remember { mutableStateListOf<Pair<NewFromVisitors.Row, NewFromVisitors.Row?>>() }
    val cat by rememberUpdatedState(catalogue)
    val items by remember {
        derivedStateOf {
            val seen = HashSet<String>()
            rows.mapNotNull { (r, prev) ->
                if (!seen.add(r.sightingId)) return@mapNotNull null
                val t = cat.tree(r.treeId) ?: return@mapNotNull null
                val s = NewFromVisitors.shot(r, t) ?: return@mapNotNull null
                VisitorItem(r, prev, t, s)
            }
        }
    }
    var last by remember { mutableStateOf<NewFromVisitors.Row?>(null) }
    var busy by remember { mutableStateOf(false) }
    var done by remember { mutableStateOf(false) }
    // Which start of the page a load belongs to: one still on its way when the
    // page starts again (a sign-in) is dropped, never counted as the end.
    var generation by remember { mutableIntStateOf(0) }
    val signedIn = act.signedIn()

    suspend fun more() {
        if (busy || done) return
        val before = items.size
        val gen = generation
        busy = true
        val token = act.token()
        val answer = NewFromVisitors.page(last, token)
        if (gen != generation) return
        busy = false
        // No answer: the page stops where it is, as the website's does.
        val page = answer ?: run { done = true; return }
        var prev = last
        for (r in page) {
            rows.add(r to prev)
            prev = r
        }
        page.lastOrNull()?.let { last = it }
        if (page.size < NewFromVisitors.PAGE_SIZE) done = true
        // A page whose photographs the feed does not carry yet added nothing, and
        // nothing on screen moved to ask again: ask for the next one now.
        if (!done && items.size == before) more()
    }

    // Signed in, the names come with the account id; the page starts again when that changes.
    LaunchedEffect(signedIn) {
        generation++
        rows.clear(); last = null; done = false; busy = false
        more()
    }

    val grid = rememberLazyStaggeredGridState()
    // More as the end comes near: eight tiles before the last.
    LaunchedEffect(grid) {
        snapshotFlow { grid.layoutInfo.visibleItemsInfo.lastOrNull()?.index ?: 0 }
            .collect { i -> if (i >= items.size - 8) more() }
    }

    // A visitor's name, tapped (Home.swift openVisitor): signed out, after the
    // sign-in the photograph's own row is asked again and the tap finishes on
    // the profile it was for.
    fun open(it: VisitorItem) {
        val id = it.row.authorId
        if (id != null && act.signedIn()) { act.openPerson(id); return }
        act.signIn {
            scope.launch {
                NewFromVisitors.author(it.row, it.prev, act.token())?.let(act.openPerson)
            }
        }
    }

    Column(Modifier.fillMaxSize().background(brand.ground)) {
        PushedBar(stringResource(R.string.discover_visitors), onBack)
        LazyVerticalStaggeredGrid(
            columns = StaggeredGridCells.Fixed(2),
            state = grid,
            horizontalArrangement = Arrangement.spacedBy(12.dp),
            contentPadding = PaddingValues(start = 16.dp, end = 16.dp, top = 6.dp, bottom = 80.dp),
            modifier = Modifier.fillMaxSize().semantics { contentDescription = "visitor-photos" },
        ) {
            item(key = "intro", span = StaggeredGridItemSpan.FullLine) {
                Text(
                    stringResource(R.string.visitors_intro),
                    fontSize = 15.sp,
                    color = brand.inkSoft,
                    modifier = Modifier.padding(bottom = 16.dp),
                )
            }
            items(items, key = { it.row.sightingId }) { it ->
                Column(verticalArrangement = Arrangement.spacedBy(7.dp)) {
                    Box(
                        Modifier
                            .fillMaxWidth()
                            .aspectRatio(it.ratio)
                            .clip(VP_SHAPE)
                            .background(brand.surfaceMuted)
                            .doubleTapHeart(it.row.sightingId.lowercase()) { act.openTree(it.tree) }
                            .semantics { contentDescription = "visitor-tile" }
                            // The iPhone's identifier as a resource id too, so the spacing run pairs
                            // tiles by kind, not by the day's tree names (2026-11-26).
                            .testTag("visitor-tile"),
                    ) {
                        RemoteImage(it.shot.card, null, Modifier.fillMaxSize())
                        TagPill(it.tree.city, Modifier.align(Alignment.BottomStart).padding(6.dp))
                        // The card save, as VisitorPhotos.swift (Hidde, 2026-11-19).
                        Box(Modifier.align(Alignment.TopEnd).padding(6.dp)) { SaveMark(it.tree, onPhoto = true) }
                    }
                    androidx.compose.foundation.layout.BoxWithConstraints(Modifier.fillMaxWidth()) {
                        // The tree's name, then who and when (VisitorPhotos.swift, 2026-11-20).
                        val w = maxWidth
                        Column(verticalArrangement = Arrangement.spacedBy(2.dp)) {
                            VisitorTitle(it.tree.name, w, Modifier.clickable { act.openTree(it.tree) })
                            VisitorLine(it.row, w) { _ -> open(it) }
                        }
                    }
                }
            }
            item(key = "end", span = StaggeredGridItemSpan.FullLine) {
                if (done) {
                    if (items.isNotEmpty()) {
                        Text(
                            stringResource(R.string.visitors_end),
                            fontSize = 15.sp,
                            color = brand.inkSoft,
                            textAlign = TextAlign.Center,
                            modifier = Modifier.fillMaxWidth().padding(top = 20.dp),
                        )
                    }
                } else {
                    Box(Modifier.fillMaxWidth().padding(top = 12.dp).heightIn(min = 60.dp), contentAlignment = Alignment.Center) {
                        CircularProgressIndicator(color = brand.inkSoft, strokeWidth = 2.dp, modifier = Modifier.size(22.dp))
                    }
                    LaunchedEffect(Unit) { more() }
                }
            }
        }
    }
}
