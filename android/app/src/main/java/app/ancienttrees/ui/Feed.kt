// THE FEED TAB (Hidde, 2026-11-26: the feed "een eigen tab", design approved: "niet
// slecht"). The Android twin of ios Screens/Feed.swift, read from that source:
// AllTrails' Community, Strava's Home, iNaturalist, Polarsteps' steps (CONVENTIONS.md
// "A feed tab"). One post per thing a reader put live, newest first: face, name, what
// and when; the whole photograph at 4:5 with the place on it ("New on the map" on a
// tree somebody added); the tree's name and its story's first sentence; heart (a
// visitor's photograph only), save, share. Chips Everyone, Following, Near you.
// Endless by the server's keyset paging, pull to refresh. Every post from
// public.feed() (account/FeedPosts.kt), never from the catalogue: a tree the catalogue
// does not know yet still shows and opens.
//
// iOS's numbers: 16 edges, the screen title, chips 8 apart, 28 between posts, 16 from
// the chips to the first post, 10 inside a post, a 36 face, 14 corners, pills 10 in.

package app.ancienttrees.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.lazy.items
import androidx.compose.ui.semantics.selected
import androidx.compose.ui.graphics.Color
import androidx.compose.foundation.layout.wrapContentHeight
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.Icon
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.derivedStateOf
import androidx.compose.ui.input.nestedscroll.nestedScroll
import androidx.compose.ui.layout.onSizeChanged
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.windowInsetsTopHeight
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.statusBars
import androidx.compose.ui.draw.alpha
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.rememberUpdatedState
import androidx.compose.runtime.setValue
import androidx.compose.runtime.snapshotFlow
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.layout.layout
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.heading
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import app.ancienttrees.R
import app.ancienttrees.account.FeedPosts
import app.ancienttrees.feed.Catalogue
import app.ancienttrees.feed.Tree
import kotlinx.coroutines.launch

/** What the Feed asks of the app around it (ContentView's environment on the iPhone). */
class FeedHost(
    val signedIn: () -> Boolean,
    val token: suspend () -> String?,
    val myId: () -> String?,
    val followingIds: suspend (me: String, token: String?) -> List<String>,
    /** Sign in, then [then] once the account is in (nudge.require). */
    val signIn: (then: (() -> Unit)?) -> Unit,
    val openPerson: (String) -> Unit,
    /** A tree the catalogue knows (Route.tree) or the post itself (Route.feedPost). */
    val openTree: (Tree) -> Unit,
    val openPost: (FeedPosts.Post) -> Unit,
    /** A post not checked yet: the share page (SharedTree.kt), never a tree page. */
    val openShared: (String) -> Unit,
    val share: (Tree) -> Unit,
    val askLocation: () -> Unit,
    /** Find people (People.kt, Route.findPeople): the person with a plus, and See all. */
    val findPeople: () -> Unit = {},
    /** People you may know, signed in only (FeedPeople.swift): who and one line why. */
    val suggestions: suspend (following: Set<String>) -> List<Pair<app.ancienttrees.account.Profiles.Profile, String>> = { emptyList() },
    /** The Activity bell (Activity.kt), drawn by the app around the Feed. */
    val bell: @Composable () -> Unit = {},
    /** Follow (true) or unfollow; true when the account took it. */
    val follow: suspend (userId: String, on: Boolean) -> Boolean = { _, _ -> false },
)

object Feed {
    /** The Feed's tab, 4 as on the iPhone (FeedView.tag): My trees stays 2, the camera 3. */
    const val TAB = 4
}

private val POST_SHAPE = RoundedCornerShape(14.dp)

@Composable
fun FeedScreen(
    catalogue: Catalogue,
    origin: Pair<Double, Double>,
    located: Boolean,
    signedIn: Boolean,
    scrollTop: Int,
    feedTo: Int?,
    host: FeedHost,
    /** `-feedbig` opens on one post at a time, for the sweep. */
    startBig: Boolean = false,
) {
    val brand = Brand.colors
    val scope = rememberCoroutineScope()
    var filter by remember { mutableStateOf(FeedPosts.Filter.EVERYONE) }
    // ONE IMMUTABLE LIST, REPLACED WHOLE (ButtonWalk, 2026-11-27: a
    // ConcurrentModificationException in `shown` while a page was added one post
    // at a time). A list that is swapped, never changed, cannot change under a read.
    var posts by remember { mutableStateOf<List<Pair<FeedPosts.Post, FeedPosts.Post?>>>(emptyList()) }
    var last by remember { mutableStateOf<FeedPosts.Post?>(null) }
    var busy by remember { mutableStateOf(false) }
    var done by remember { mutableStateOf(false) }
    var failed by remember { mutableStateOf(false) }
    var generation by remember { mutableIntStateOf(0) }
    var following by remember { mutableStateOf(emptySet<String>()) }
    // ZOOMED OUT FIRST (Hidde, 2026-11-26: "standaard juist op de uitgezoomde
    // versie", "zoals bij de feed op web"): the website's masonry; one big post
    // at a time is the other tab. In memory only (hard rule 11).
    var grid by remember { mutableStateOf(!startBig) }
    val here by rememberUpdatedState(if (located) origin else null)
    val shown by remember {
        // Checked posts only (FeedView.shown, Hidde 2026-11-26): a share waits until it is a tree.
        derivedStateOf { posts.filter { it.first.checked && FeedPosts.passes(it.first, filter, following, here) } }
    }

    fun take(page: List<FeedPosts.Post>, n: Int) {
        var prev = last
        val seen = posts.map { it.first.key }.toHashSet()
        val added = ArrayList<Pair<FeedPosts.Post, FeedPosts.Post?>>()
        for (p in page) if (seen.add(p.key)) { added.add(p to prev); prev = p }
        if (added.isNotEmpty()) posts = posts + added
        page.lastOrNull()?.let { last = it }
        if (page.size < n) done = true
    }

    suspend fun more() {
        if (busy || done || failed) return
        val gen = generation
        busy = true
        val n = if (filter == FeedPosts.Filter.EVERYONE) FeedPosts.PAGE_SIZE else 48
        val answer = FeedPosts.page(last, host.token(), n)
        if (gen != generation) return
        busy = false
        val page = answer ?: run { failed = true; return }
        take(page, n)
    }


    // A filter shows only part of each page: read on until a screen of posts or the end.
    suspend fun fill() {
        var rounds = 0
        while (shown.size < 6 && !done && !failed && rounds < 30) {
            val before = posts.size
            more()
            if (posts.size == before) break
            rounds++
        }
    }

    // Pull to refresh keeps the posts on screen until the new first page is
    // in, and a refresh that fails keeps them (FeedView.reload, Hidde
    // 2026-11-26: "the feed did not load. Pull down again").
    suspend fun restart() {
        generation++
        val gen = generation
        busy = true
        val n = if (filter == FeedPosts.Filter.EVERYONE) FeedPosts.PAGE_SIZE else 48
        val answer = FeedPosts.page(null, host.token(), n)
        if (gen != generation) return
        busy = false
        if (answer == null) { if (posts.isEmpty()) failed = true; return }
        posts = emptyList(); last = null; done = false; failed = false
        take(answer, n)
        fill()
    }

    LaunchedEffect(signedIn) {
        val me = host.myId()
        following = if (me != null) host.followingIds(me, host.token()).map { it.lowercase() }.toSet() else emptySet()
        restart()
    }

    val list = rememberLazyListState()
    LaunchedEffect(scrollTop) { if (scrollTop > 0) list.animateScrollToItem(0) }
    LaunchedEffect(feedTo) {
        if (feedTo != null) { kotlinx.coroutines.delay(4000); list.scrollToItem(feedTo + 1) }
    }
    LaunchedEffect(list) {
        snapshotFlow { list.layoutInfo.visibleItemsInfo.lastOrNull()?.index ?: 0 }
            .collect { i -> if (i >= shown.size - 6) more() }
    }

    fun choose(f: FeedPosts.Filter) {
        if (f == FeedPosts.Filter.FOLLOWING && !host.signedIn()) {
            host.signIn { filter = FeedPosts.Filter.FOLLOWING }
            return
        }
        if (f == FeedPosts.Filter.NEAR && !located) host.askLocation()
        filter = f
        app.ancienttrees.account.Measure.event("feed_filter", mapOf("filter" to f.name.lowercase()))
        scope.launch { fill() }
    }

    fun openAuthor(p: FeedPosts.Post, prev: FeedPosts.Post?) {
        val id = p.authorId
        if (id != null && host.signedIn()) { host.openPerson(id); return }
        host.signIn {
            scope.launch { FeedPosts.author(p, prev, host.token())?.let(host.openPerson) }
        }
    }

    val emptyLine = when {
        failed -> stringResource(R.string.feed_failed)
        filter == FeedPosts.Filter.EVERYONE -> stringResource(R.string.feed_empty)
        filter == FeedPosts.Filter.FOLLOWING ->
            if (following.isEmpty()) stringResource(R.string.feed_empty_following_none) else stringResource(R.string.feed_empty_following)
        located -> stringResource(R.string.feed_empty_near)
        else -> ""
    }

    val header: @Composable () -> Unit = {
        Column(verticalArrangement = Arrangement.spacedBy(12.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text(
                    stringResource(R.string.tab_feed),
                    fontFamily = BrandFace,
                    fontWeight = FontWeight.Bold,
                    fontSize = 32.sp,
                    color = brand.ink,
                    modifier = Modifier.weight(1f).semantics { heading() },
                )
                // Polarsteps' person with a plus, the same disc on every tab
                // (FeedView, 2026-11-26); the bell moved on to My trees.
                val findLabel = stringResource(R.string.people_find)
                HeaderDisc(Sym.PersonAdd, "feed-find-people", label = findLabel) {
                    // Signed out: sign in first, then Find people.
                    if (host.signedIn()) host.findPeople() else host.signIn { host.findPeople() }
                }
            }
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                FeedPosts.Filter.entries.forEach { f ->
                    val label = when (f) {
                        FeedPosts.Filter.EVERYONE -> stringResource(R.string.feed_everyone)
                        FeedPosts.Filter.FOLLOWING -> stringResource(R.string.feed_following)
                        FeedPosts.Filter.NEAR -> stringResource(R.string.feed_near)
                    }
                    Box(Modifier.testTag("feed-filter-" + when (f) {
                        FeedPosts.Filter.EVERYONE -> "everyone"
                        FeedPosts.Filter.FOLLOWING -> "following"
                        FeedPosts.Filter.NEAR -> "near"
                    })) { FilterChip(label, null, filter == f) { choose(f) } }
                }
            }
            LayoutTabs(grid) { g ->
                grid = g
                app.ancienttrees.account.Measure.event("feed_layout", mapOf("layout" to if (g) "grid" else "big"))
            }
        }
    }
    val endItem: @Composable () -> Unit = {
        if (done || failed) {
            Text(
                if (shown.isEmpty()) emptyLine else stringResource(R.string.feed_end),
                fontSize = 15.sp,
                color = brand.inkSoft,
                textAlign = TextAlign.Center,
                modifier = Modifier.fillMaxWidth().padding(top = 8.dp),
            )
        } else {
            Box(Modifier.fillMaxWidth().heightIn(min = 60.dp), contentAlignment = Alignment.Center) {
                CircularProgressIndicator(color = brand.inkSoft, strokeWidth = 2.dp, modifier = Modifier.size(22.dp))
            }
            LaunchedEffect(Unit) { more() }
        }
    }
    val showPeople = signedIn && filter == FeedPosts.Filter.EVERYONE
    // What the filter needs, on top (FeedView, 2026-11-26): Following with nobody
    // followed shows People you may know first; Near you without a location asks for it.
    val topPeople = signedIn && filter == FeedPosts.Filter.FOLLOWING && following.isEmpty()
    val nearCard = filter == FeedPosts.Filter.NEAR && !located

    // DISCOVER'S HEADER (Hidde, 2026-11-26: "als je naar beneden scrolt en weer
    // omhooggaat, komt die titel naar beneden ... datzelfde bij feed"; Discover.kt's
    // quick return): pinned over the list, away reading down, back on any scroll up.
    val density = androidx.compose.ui.platform.LocalDensity.current
    val staggered = androidx.compose.foundation.lazy.staggeredgrid.rememberLazyStaggeredGridState()
    var headerHidden by remember { mutableStateOf(false) }
    // 0 until the header has measured: the lists wait for it, or the grid lays
    // out under a guessed top and starts with its first photograph behind the header.
    var headerPx by remember { mutableStateOf(0) }
    val nearTop by remember {
        derivedStateOf {
            if (grid) staggered.firstVisibleItemIndex == 0 && staggered.firstVisibleItemScrollOffset < headerPx
            else list.firstVisibleItemIndex == 0 && list.firstVisibleItemScrollOffset < headerPx
        }
    }
    LaunchedEffect(nearTop) { if (nearTop) headerHidden = false }
    val quickReturn = remember {
        object : androidx.compose.ui.input.nestedscroll.NestedScrollConnection {
            override fun onPostScroll(
                consumed: androidx.compose.ui.geometry.Offset,
                available: androidx.compose.ui.geometry.Offset,
                source: androidx.compose.ui.input.nestedscroll.NestedScrollSource,
            ): androidx.compose.ui.geometry.Offset {
                if (consumed.y < -1f && !nearTop) headerHidden = true
                else if (consumed.y > 1f) headerHidden = false
                return androidx.compose.ui.geometry.Offset.Zero
            }
        }
    }
    val headerShift by androidx.compose.animation.core.animateIntAsState(
        if (headerHidden) -(headerPx + with(density) { 80.dp.roundToPx() }) else 0,
        Motion.snappy(0.25f),
        label = "feed-header",
    )
    LaunchedEffect(scrollTop) { if (scrollTop > 0) headerHidden = false }
    // 16 from the layout row to the first post, as before.
    val listTop = with(density) { headerPx.toDp() } + 10.dp
    // A grid column's width, for where the grid breaks (FeedPosts.evenCut).
    val colDp = (androidx.compose.ui.platform.LocalConfiguration.current.screenWidthDp - 44) / 2f

    Box(Modifier.fillMaxSize().background(brand.ground)) {
    if (headerPx == 0) Spacer(Modifier.fillMaxSize())
    else if (grid) PullRefresh(onRefresh = { restart() }) {
        // The website's /visitors masonry (ios FeedView.tiles): two columns 12
        // apart, each photograph whole at its own shape, the place on it, the
        // save top right, the name and the byline with the heart under it.
        // People you may know after the first six, never opening the page.
        LaunchedEffect(staggered) {
            snapshotFlow { staggered.layoutInfo.visibleItemsInfo.lastOrNull()?.index ?: 0 }
                .collect { i -> if (i >= shown.size - 8) more() }
        }
        LaunchedEffect(scrollTop) { if (scrollTop > 0) staggered.animateScrollToItem(0) }
        androidx.compose.foundation.lazy.staggeredgrid.LazyVerticalStaggeredGrid(
            columns = androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridCells.Fixed(2),
            state = staggered,
            horizontalArrangement = Arrangement.spacedBy(12.dp),
            verticalItemSpacing = 16.dp,
            contentPadding = PaddingValues(start = 16.dp, end = 16.dp, top = listTop - 16.dp, bottom = 100.dp),
            modifier = Modifier.fillMaxSize().nestedScroll(quickReturn).testTag("feed"),
        ) {
            val full = androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridItemSpan.FullLine
            // The list's anchor at the top, where the header item stood: without it
            // the grid kept the spinner in place as the posts arrived and opened
            // a few posts down.
            item(key = "top", span = full) { Spacer(Modifier.height(0.dp)) }
            if (topPeople) item(key = "people-top", span = full) { FeedPeopleRow(host, following) }
            if (nearCard) item(key = "near-card", span = full) { NearYouCard(host) }
            // Where both columns end level (FeedPosts.evenCut), never a fixed six.
            val cut = FeedPosts.evenCut(shown.map { (p, _) ->
                val w = p.photoW ?: 0
                val h = p.photoH ?: 0
                val r = if (w > 0 && h > 0) minOf(h.toFloat() / w, 1.6f) else 5f / 4f
                colDp * r + 70f
            })
            items(cut, key = { shown[it].first.key }) { i ->
                val (p, prev) = shown[i]
                FeedTile(p, p.treeId?.let { catalogue.tree(it) }, host, onAuthor = { openAuthor(p, prev) })
            }
            if (showPeople && shown.size > cut) item(key = "people", span = full) { FeedPeopleRow(host, following) }
            items(shown.size - cut, key = { shown[cut + it].first.key }) { i ->
                val (p, prev) = shown[cut + i]
                FeedTile(p, p.treeId?.let { catalogue.tree(it) }, host, onAuthor = { openAuthor(p, prev) })
            }
            item(key = "end", span = full) { endItem() }
        }
    } else PullRefresh(onRefresh = { restart() }) {
        LazyColumn(
            state = list,
            contentPadding = PaddingValues(start = 16.dp, end = 16.dp, top = listTop - 28.dp, bottom = 100.dp),
            verticalArrangement = Arrangement.spacedBy(28.dp),
            modifier = Modifier.fillMaxSize().nestedScroll(quickReturn).testTag("feed"),
        ) {
            item(key = "top") { Spacer(Modifier.height(0.dp)) } // the anchor; its 28 is taken off the top
            if (topPeople) item(key = "people-top") { FeedPeopleRow(host, following) }
            if (nearCard) item(key = "near-card") { NearYouCard(host) }
            itemsIndexed(shown, key = { _, it -> it.first.key }) { i, (p, prev) ->
                FeedPost(p, p.treeId?.let { catalogue.tree(it) }, host, onAuthor = { openAuthor(p, prev) })
                if (i == 2 && showPeople) FeedPeopleRow(host, following)
            }
            item(key = "end") { endItem() }
        }
    }
        // PINNED, sliding away and back (Discover.kt's header).
        Box(
            Modifier
                .offset { androidx.compose.ui.unit.IntOffset(0, headerShift) }
                .onSizeChanged { headerPx = it.height }
                .fillMaxWidth()
                .background(brand.ground)
                .statusBarsPadding()
                .padding(horizontal = 16.dp)
                .padding(top = 6.dp, bottom = 6.dp),
        ) { header() }
        // While the header is away, the status bar keeps a solid strip.
        Box(
            Modifier
                .fillMaxWidth()
                .windowInsetsTopHeight(WindowInsets.statusBars)
                .alpha(if (headerHidden) 1f else 0f)
                .background(brand.ground),
        )
    }
}

/** Pulls an item up by [dp] without changing what it measures (the chips' 16 instead of 28). */
private fun Modifier.offsetTop(dp: Int): Modifier = this.layout { m, c ->
    val p = m.measure(c)
    val d = dp.dp.roundToPx()
    layout(p.width, (p.height + d).coerceAtLeast(0)) { p.place(0, d) }
}

@Composable
private fun FeedPost(p: FeedPosts.Post, known: Tree?, host: FeedHost, onAuthor: () -> Unit) {
    val brand = Brand.colors
    val tree = known ?: FeedPosts.stub(p)
    val open = {
        val shared = p.sharedId
        // A photograph of a tree we have opens that tree, checked or not
        // (Feed.swift, 2026-11-26); a tree they added and nobody checked yet
        // opens its share page.
        when {
            known != null -> host.openTree(known)
            shared != null -> host.openShared(shared)
            else -> host.openPost(p)
        }
    }
    Column(verticalArrangement = Arrangement.spacedBy(10.dp)) {
        // Who, what and when (FeedView.byline): a public profile's name opens it, "A visitor" nothing.
        val name = p.authorName ?: stringResource(R.string.discover_a_visitor)
        val deed = stringResource(
            when {
                !p.checked -> R.string.feed_just_shared
                p.isNewTree -> R.string.feed_added
                else -> R.string.feed_photographed
            },
        )
        val whenText = SentAgo.short(p.publishedAt)
        Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.fillMaxWidth()) {
            Row(
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.spacedBy(10.dp),
                modifier = Modifier
                    .weight(1f)
                    .heightIn(min = 44.dp)
                    .then(if (p.authorName != null) Modifier.clickable(role = Role.Button, onClick = onAuthor).testTag("feed-author") else Modifier),
            ) {
                if (p.authorName != null) Avatar(p.authorAvatar, name, 36, 15)
                else Box(Modifier.size(36.dp).clip(CircleShape).background(brand.surfaceMuted))
                Column(verticalArrangement = Arrangement.spacedBy(1.dp)) {
                    Text(name, fontSize = 15.sp, fontWeight = FontWeight.SemiBold, color = brand.ink, maxLines = 1, overflow = TextOverflow.Ellipsis)
                    Text(listOfNotNull(deed, whenText).joinToString(" · "), fontSize = 13.sp, color = brand.inkSoft, maxLines = 1)
                }
            }
            // The heart at the end of the person's line, as on the tiles (FeedView.byline).
            p.likeId?.let { PhotoHeart(it, size = 22.dp) }
        }
        // The whole photograph at 4:5, the place on it, "New on the map" on a tree somebody added.
        val photoMod = Modifier
            .fillMaxWidth()
            .aspectRatio(4f / 5f)
            .clip(POST_SHAPE)
            .background(brand.surfaceMuted)
            .semantics { contentDescription = if (p.place.isEmpty()) p.treeName else "${p.treeName}, ${p.place}" }
            .testTag("feed-photo")
        Box(if (p.likeId != null) photoMod.doubleTapHeart(p.likeId!!) { open() } else photoMod.clickable(role = Role.Button) { open() }) {
            p.photoUrl?.let { RemoteImage(it, null, Modifier.fillMaxSize()) }
            if (p.isNewTree) FeedPill(stringResource(R.string.feed_new_on_map), Modifier.align(Alignment.TopStart).padding(10.dp))
            if (p.place.isNotEmpty()) FeedPill(p.place, Modifier.align(Alignment.BottomStart).padding(10.dp))
            // One card in two sizes (2026-11-26): the save top right on the photograph, as on every tree card.
            if (p.checked) Box(Modifier.align(Alignment.TopEnd).padding(6.dp)) { SaveMark(tree, onPhoto = true) }
        }
        Column(
            verticalArrangement = Arrangement.spacedBy(4.dp),
            modifier = Modifier.fillMaxWidth().clickable(role = Role.Button) { open() }.testTag("feed-name"),
        ) {
            Text(p.treeName, fontFamily = BrandFace, fontWeight = FontWeight.Bold, fontSize = 20.sp, color = brand.ink, maxLines = 2, overflow = TextOverflow.Ellipsis)
            val story = known?.story.orEmpty()
            if (story.isNotEmpty()) {
                Text(FeedPosts.firstSentence(story), fontSize = 15.sp, color = brand.inkSoft, maxLines = 2, overflow = TextOverflow.Ellipsis)
            }
        }
    }
}

private fun Modifier.offsetStart(dp: Int): Modifier = this.layout { m, c ->
    val p = m.measure(c)
    layout(p.width, p.height) { p.place(dp.dp.roundToPx(), 0) }
}

/** A label on the photograph (FeedPill on the iPhone): 12 semibold, moss on white, a capsule. */
@Composable
private fun FeedPill(text: String, modifier: Modifier = Modifier) {
    val brand = Brand.colors
    Text(
        text,
        fontSize = 12.sp,
        fontWeight = FontWeight.SemiBold,
        color = brand.moss,
        maxLines = 1,
        overflow = TextOverflow.Ellipsis,
        modifier = modifier.background(brand.surface, RoundedCornerShape(50)).padding(horizontal = 9.dp, vertical = 5.dp),
    )
}


/** Zoomed out or one by one: Instagram's profile tabs (FeedView.layoutToggle), full width, a line under the chosen half. */
@Composable
private fun LayoutTabs(grid: Boolean, choose: (Boolean) -> Unit) {
    val brand = Brand.colors
    Box(Modifier.fillMaxWidth().padding(horizontal = 0.dp)) {
        Row(Modifier.fillMaxWidth()) {
            listOf(true, false).forEach { g ->
                val on = grid == g
                val label = stringResource(if (g) R.string.feed_layout_grid else R.string.feed_layout_big)
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier
                        .weight(1f)
                        .heightIn(min = 44.dp)
                        .clickable(role = Role.Tab) { choose(g) }
                        .semantics { contentDescription = label; selected = on }
                        .testTag(if (g) "feed-layout-grid" else "feed-layout-big"),
                ) {
                    Icon(if (g) Sym.GridView else Sym.ViewAgenda, null,
                        tint = if (on) brand.ink else brand.inkSoft.copy(alpha = 0.6f), modifier = Modifier.size(26.dp))
                    if (on) Box(Modifier.align(Alignment.BottomCenter).fillMaxWidth().height(1.5.dp).background(brand.ink))
                }
            }
        }
        Box(Modifier.align(Alignment.BottomCenter).fillMaxWidth().height(0.5.dp).background(brand.hairline))
    }
}

/** One tile of the masonry (FeedView.tile on the iPhone, the website's /visitors tile). */
@Composable
private fun FeedTile(p: FeedPosts.Post, known: Tree?, host: FeedHost, onAuthor: () -> Unit) {
    val brand = Brand.colors
    val open = {
        val shared = p.sharedId
        when {
            shared != null -> host.openShared(shared)
            known != null -> host.openTree(known)
            else -> host.openPost(p)
        }
    }
    val ratio = run {
        val w = p.photoW ?: 0
        val h = p.photoH ?: 0
        if (w > 0 && h > 0) maxOf(w.toFloat() / h, 1f / 1.6f) else 4f / 5f
    }
    val name = p.authorName ?: stringResource(R.string.discover_a_visitor)
    Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
        val photoMod = Modifier
            .fillMaxWidth()
            .aspectRatio(ratio)
            .clip(RoundedCornerShape(12.dp))
            .background(brand.surfaceMuted)
            .semantics { contentDescription = if (p.place.isEmpty()) p.treeName else "${p.treeName}, ${p.place}" }
            .testTag("feed-tile")
        Box(if (p.likeId != null) photoMod.doubleTapHeart(p.likeId!!) { open() } else photoMod.clickable(role = Role.Button) { open() }) {
            p.photoUrl?.let { RemoteImage(it, null, Modifier.fillMaxSize()) }
            if (p.place.isNotEmpty()) TagPill(p.place, Modifier.align(Alignment.BottomStart).padding(6.dp))
            // The save, as on every card: the tree's (not before the check).
            if (p.checked) Box(Modifier.align(Alignment.TopEnd).padding(6.dp)) { SaveMark(known ?: FeedPosts.stub(p), onPhoto = true) }
        }
        Text(p.treeName, fontFamily = BrandFace, fontWeight = FontWeight.Bold, fontSize = 14.sp, color = brand.ink,
            maxLines = 2, overflow = TextOverflow.Ellipsis, modifier = Modifier.clickable { open() })
        Row(verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.spacedBy(5.dp),
            modifier = Modifier.fillMaxWidth().then(if (p.authorName != null) Modifier.clickable(onClick = onAuthor) else Modifier)) {
            VisitorFace(name, p.authorAvatar, size = 18)
            // The name takes what it needs, the time keeps its room, the heart
            // stays at the end (FeedView.tile): a long name gives way first.
            Row(Modifier.weight(1f), verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.spacedBy(5.dp)) {
                Text(name, fontSize = 13.sp, fontWeight = FontWeight.Medium, color = brand.inkSoft, maxLines = 1,
                    overflow = TextOverflow.Ellipsis, modifier = Modifier.weight(1f, fill = false))
                SentAgo.short(p.publishedAt)?.let { Text("· $it", fontSize = 13.sp, color = brand.inkSoft.copy(alpha = 0.75f), maxLines = 1, softWrap = false) }
            }
            // The heart, the person's photograph (only one published on a tree of ours).
            p.likeId?.let { PhotoHeart(it, size = 21.dp) }
        }
    }
}

/**
 * PEOPLE YOU MAY KNOW (FeedPeople.swift; Polarsteps' Activity row): cards that scroll
 * sideways, a round face, the name, one line why, Follow, an X; See all is Find people.
 * Signed in only. A card taken away is gone for this opening only (hard rule 11).
 */
@Composable
private fun FeedPeopleRow(host: FeedHost, following: Set<String>) {
    val brand = Brand.colors
    val scope = rememberCoroutineScope()
    var people by remember { mutableStateOf(emptyList<Pair<app.ancienttrees.account.Profiles.Profile, String>>()) }
    var gone by remember { mutableStateOf(emptySet<String>()) }
    var followed by remember { mutableStateOf(emptySet<String>()) }
    LaunchedEffect(following) { people = host.suggestions(following) }
    val shown = people.filter { it.first.userId !in gone }
    if (shown.isEmpty()) return
    Column(verticalArrangement = Arrangement.spacedBy(12.dp), modifier = Modifier.testTag("feed-people")) {
        Box(Modifier.fullBleed()) { ShelfHeader(stringResource(R.string.feed_people_title)) { host.findPeople() } }
        androidx.compose.foundation.lazy.LazyRow(
            horizontalArrangement = Arrangement.spacedBy(12.dp),
            contentPadding = PaddingValues(horizontal = 16.dp),
            modifier = Modifier.fullBleed(),
        ) {
            items(shown, key = { it.first.userId }) { (prof, reason) ->
                val on = prof.userId in followed
                Box(Modifier.width(132.dp).clip(RoundedCornerShape(20.dp)).background(brand.surfaceMuted)) {
                    Column(
                        horizontalAlignment = Alignment.CenterHorizontally,
                        verticalArrangement = Arrangement.spacedBy(6.dp),
                        modifier = Modifier.fillMaxWidth().padding(start = 10.dp, end = 10.dp, top = 14.dp, bottom = 6.dp),
                    ) {
                        Column(
                            horizontalAlignment = Alignment.CenterHorizontally,
                            verticalArrangement = Arrangement.spacedBy(8.dp),
                            modifier = Modifier.clickable { host.openPerson(prof.userId) }.testTag("feed-person"),
                        ) {
                            Avatar(prof.avatarUrl, prof.displayName, 60, 24)
                            Column(horizontalAlignment = Alignment.CenterHorizontally, verticalArrangement = Arrangement.spacedBy(3.dp)) {
                                Text(prof.displayName, fontSize = 14.sp, fontWeight = FontWeight.SemiBold, color = brand.ink, maxLines = 1)
                                Text(reason, fontSize = 12.sp, color = brand.inkSoft, textAlign = TextAlign.Center, maxLines = 2, minLines = 2)
                            }
                        }
                        Box(
                            contentAlignment = Alignment.Center,
                            modifier = Modifier
                                .heightIn(min = 44.dp)
                                .clickable(role = Role.Button) {
                                    scope.launch { if (host.follow(prof.userId, !on)) followed = if (on) followed - prof.userId else followed + prof.userId }
                                }
                                .testTag("feed-person-follow"),
                        ) {
                            Text(
                                stringResource(if (on) R.string.people_following else R.string.people_follow),
                                fontSize = 14.sp, fontWeight = FontWeight.SemiBold,
                                color = if (on) brand.ink else Color.White,
                                modifier = Modifier
                                    .height(32.dp)
                                    .then(if (on) Modifier.border(1.dp, brand.hairline, RoundedCornerShape(50)) else Modifier.background(brand.ink, RoundedCornerShape(50)))
                                    .padding(horizontal = 18.dp)
                                    .wrapContentHeight(Alignment.CenterVertically),
                            )
                        }
                    }
                    val notNow = stringResource(R.string.feed_people_not_now, prof.displayName)
                    Box(
                        contentAlignment = Alignment.Center,
                        modifier = Modifier
                            .align(Alignment.TopEnd)
                            .size(44.dp)
                            .clickable(role = Role.Button) { gone = gone + prof.userId }
                            .semantics { contentDescription = notNow }
                            .testTag("feed-person-dismiss"),
                    ) {
                        Box(Modifier.size(20.dp).clip(CircleShape).background(brand.ink), contentAlignment = Alignment.Center) {
                            Icon(Sym.CloseBold, null, tint = Color.White, modifier = Modifier.size(12.dp))
                        }
                    }
                }
            }
        }
    }
}

/** Out to the screen's edges, past the list's 16 (ShelfHeader and the row bring their own). */
private fun Modifier.fullBleed(): Modifier = this.layout { m, c ->
    val extra = 32.dp.roundToPx()
    val pl = m.measure(c.copy(maxWidth = c.maxWidth + extra, minWidth = minOf(c.minWidth + extra, c.maxWidth + extra)))
    layout(c.maxWidth, pl.height) { pl.place(-16.dp.roundToPx(), 0) }
}


/** Near you without a location (FeedView's NearYouCard): EmptyPlaceCard's shape, Use my location. */
@Composable
private fun NearYouCard(host: FeedHost) {
    val brand = Brand.colors
    Column(
        verticalArrangement = Arrangement.spacedBy(14.dp),
        modifier = Modifier.fillMaxWidth().clip(RoundedCornerShape(14.dp)).background(brand.surfaceMuted).padding(16.dp).testTag("feed-near-card"),
    ) {
        Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Icon(Sym.NearMe, null, tint = brand.inkSoft.copy(alpha = 0.6f), modifier = Modifier.size(26.dp))
            Text(stringResource(R.string.feed_near_title), fontSize = 16.sp, fontWeight = FontWeight.SemiBold, color = brand.ink)
            Text(stringResource(R.string.feed_near_body), fontSize = 14.sp, color = brand.inkSoft)
        }
        SecondaryButton(stringResource(R.string.feed_near_button), Sym.NearMeSemibold) { host.askLocation() }
    }
}
