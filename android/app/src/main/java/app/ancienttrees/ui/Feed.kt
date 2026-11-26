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
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateListOf
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
) {
    val brand = Brand.colors
    val scope = rememberCoroutineScope()
    var filter by remember { mutableStateOf(FeedPosts.Filter.EVERYONE) }
    val posts = remember { mutableStateListOf<Pair<FeedPosts.Post, FeedPosts.Post?>>() }
    var last by remember { mutableStateOf<FeedPosts.Post?>(null) }
    var busy by remember { mutableStateOf(false) }
    var done by remember { mutableStateOf(false) }
    var failed by remember { mutableStateOf(false) }
    var generation by remember { mutableIntStateOf(0) }
    var following by remember { mutableStateOf(emptySet<String>()) }
    val here by rememberUpdatedState(if (located) origin else null)
    val shown by remember {
        derivedStateOf { posts.filter { FeedPosts.passes(it.first, filter, following, here) } }
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
        var prev = last
        val seen = posts.map { it.first.key }.toHashSet()
        for (p in page) if (seen.add(p.key)) { posts.add(p to prev); prev = p }
        page.lastOrNull()?.let { last = it }
        if (page.size < n) done = true
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

    suspend fun restart() {
        generation++
        posts.clear(); last = null; done = false; failed = false; busy = false
        more()
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
        else -> stringResource(R.string.feed_empty_near_off)
    }

    PullRefresh(onRefresh = { restart() }) {
        LazyColumn(
            state = list,
            contentPadding = PaddingValues(start = 16.dp, end = 16.dp, top = 6.dp, bottom = 100.dp),
            verticalArrangement = Arrangement.spacedBy(28.dp),
            // Under the status bar, never behind it (Discover's opaque top).
            modifier = Modifier.fillMaxSize().background(brand.ground).statusBarsPadding().testTag("feed"),
        ) {
            item(key = "head") {
                Column(Modifier.padding(bottom = 0.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
                    Text(
                        stringResource(R.string.tab_feed),
                        fontFamily = BrandFace,
                        fontWeight = FontWeight.Bold,
                        fontSize = 32.sp,
                        color = brand.ink,
                        modifier = Modifier.semantics { heading() },
                    )
                    Row(horizontalArrangement = Arrangement.spacedBy(8.dp), modifier = Modifier.padding(bottom = 0.dp)) {
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
                }
            }
            itemsIndexed(shown, key = { _, it -> it.first.key }) { i, (p, prev) ->
                // 16 from the chips to the first post (the design), 28 between posts.
                Box(if (i == 0) Modifier.offsetTop(-12) else Modifier) {
                    FeedPost(p, p.treeId?.let { catalogue.tree(it) }, host, onAuthor = { openAuthor(p, prev) })
                }
            }
            item(key = "end") {
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
        }
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
        Row(
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(10.dp),
            modifier = Modifier
                .fillMaxWidth()
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
        // Heart (a visitor's photograph only), save, share; the glyphs line up with the text.
        Row(
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(4.dp),
            modifier = Modifier.offsetTop(-6).offsetStart(if (p.likeId == null) -11 else 0),
        ) {
            p.likeId?.let {
                PhotoHeart(it, size = 25.dp)
                Spacer(Modifier.width(6.dp))
            }
            // Nothing to save before the check: no tree of ours exists yet.
            if (p.checked) SaveMark(tree, onPhoto = false)
            val shareLabel = stringResource(R.string.share_tree)
            Box(
                contentAlignment = Alignment.Center,
                modifier = Modifier
                    .size(44.dp)
                    .clickable(role = Role.Button) { host.share(tree) }
                    .semantics { contentDescription = shareLabel }
                    .testTag("feed-share"),
            ) {
                Icon(Sym.Share, null, tint = brand.inkSoft, modifier = Modifier.size(22.dp))
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
