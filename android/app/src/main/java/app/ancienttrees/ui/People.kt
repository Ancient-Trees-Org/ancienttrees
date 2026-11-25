// Finding somebody and following them, and somebody else's public profile:
// ported from ios Screens/People.swift, Screens/PersonProfile.swift and
// Kit/SuggestedPeople.swift.
//
// Find people is a pushed page: the field on top, Share your profile, then
// Suggested (ambassadors of your places, people who photographed trees there,
// the other ambassadors). Followers and Following are the same page with
// another source. Every row: picture and name open the profile, a Follow pill,
// and the ellipsis for report and block (App Store 1.2's control, kept the same
// on Android).
//
// Blocks: the iPhone keeps its blocked list on the phone as well; here it lives
// only in memory and is read back from the server's blocks table (hard rule 11).

package app.ancienttrees.ui

import android.content.Intent
import androidx.activity.compose.BackHandler
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.layout.widthIn
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.pulltorefresh.PullToRefreshBox
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.BasicTextField
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.SpanStyle
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.buildAnnotatedString
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.text.withStyle
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import app.ancienttrees.R
import app.ancienttrees.feed.Photo
import app.ancienttrees.account.Account
import app.ancienttrees.account.DemoPeople
import app.ancienttrees.account.EarlyAdopter
import app.ancienttrees.account.Profiles
import app.ancienttrees.account.Supa
import app.ancienttrees.feed.Catalogue
import app.ancienttrees.feed.Tree
import kotlinx.coroutines.async
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import org.json.JSONArray
import org.json.JSONObject

/** Report and block (Moderation.swift), over supabase/reports.sql's tables. */
class Moderation {
    val blocked = mutableStateListOf<String>()
    fun hides(id: String) = id in blocked

    suspend fun load(me: String?, token: String?) {
        if (me == null || token == null) return
        val rows = Supa.rows("/rest/v1/blocks?select=blocked&blocker=eq.$me", token)
        blocked.clear()
        blocked.addAll(rows.map { it.optString("blocked") })
    }

    suspend fun report(subject: String, reason: String, reporter: String, token: String): Boolean =
        Supa.send("/rest/v1/reports", token = token, prefer = "return=minimal",
            body = JSONArray().put(JSONObject().put("reporter", reporter).put("subject", subject).put("reason", reason)).toString()).ok

    suspend fun block(id: String, me: String, token: String?) {
        if (id !in blocked) blocked.add(id)
        token ?: return
        Supa.send("/rest/v1/blocks?on_conflict=blocker,blocked", token = token, prefer = "resolution=merge-duplicates,return=minimal",
            body = JSONArray().put(JSONObject().put("blocker", me).put("blocked", id)).toString())
    }

    suspend fun unblock(id: String, me: String, token: String?) {
        blocked.remove(id)
        token ?: return
        Supa.delete("/rest/v1/blocks?blocker=eq.$me&blocked=eq.$id", token)
    }
}

enum class PeopleSource { SEARCH, FOLLOWERS, FOLLOWING }

/** What the people pages need from around them. */
class PeopleHost(
    val account: Account,
    val profiles: Profiles,
    val moderation: Moderation,
    val catalogue: Catalogue?,
    /** Your saved and collected trees, for "your places" in Suggested. */
    val yourTrees: List<String>,
    val userId: String?,
    val args: List<String>,
    val signIn: (SignInReason) -> Unit,
    val editName: () -> Unit,
    val openPerson: (String) -> Unit,
    /** Somebody else's followers (true) or following, from the counts on their profile. */
    val openFollowList: (String, Boolean) -> Unit = { _, _ -> },
    val openTree: (Tree) -> Unit,
    /** Somebody's own tree: its shared page (SightingSync.url(for:)). */
    val openShared: (String) -> Unit = {},
)

private data class Suggestion(val profile: Profiles.Profile, val reason: String, val ambassador: Boolean)

// THE LAST SUGGESTIONS STAY FOR THE NEXT VISIT (Hidde on his Samsung, 2026-11-17:
// "het duurde best even voordat de gesuggereerde gebruikers vertoonden"): memory only,
// for this account, refreshed behind the list as Discover's shelves are.
private var lastSuggestions: Pair<String, List<Suggestion>>? = null

@Composable
fun FindPeopleScreen(host: PeopleHost, source: PeopleSource, owner: String? = null, onBack: () -> Unit) = PlainText { FindPeopleInner(host, source, owner, onBack) }

@Composable
private fun FindPeopleInner(host: PeopleHost, source: PeopleSource, owner: String?, onBack: () -> Unit) {
    val brand = Brand.colors
    val context = LocalContext.current
    val scope = rememberCoroutineScope()
    val demo = DemoPeople.on(host.args)
    val me = host.userId
    // Whose list (People.swift owner): yours, or somebody else's from their profile.
    val isMine = owner == null || owner == me
    var query by remember { mutableStateOf("") }
    var results by remember { mutableStateOf<List<Profiles.Profile>>(emptyList()) }
    var suggestions by remember { mutableStateOf(lastSuggestions?.takeIf { it.first == me && source == PeopleSource.SEARCH }?.second.orEmpty()) }
    val followingIds = remember { mutableStateListOf<String>() }
    var searching by remember { mutableStateOf(false) }
    var acting by remember { mutableStateOf<Profiles.Profile?>(null) }
    var askingPublic by remember { mutableStateOf(false) }
    var refreshing by remember { mutableStateOf(false) }

    suspend fun token() = if (demo) null else host.account.fresh()?.accessToken
    suspend fun loadFollowing() {
        if (me == null || demo) return
        val ids = host.profiles.followingIds(me, token())
        followingIds.clear(); followingIds.addAll(ids)
    }
    val ambassadorWord = stringResource(R.string.people_ambassador_of)
    val photographedOne = stringResource(R.string.people_photographed_1)
    val photographedMany = stringResource(R.string.people_photographed_n)
    fun reasonAmbassador(place: String) = ambassadorWord.format(place)
    fun reasonPhoto(n: Int, place: String) = if (n == 1) photographedOne.format(place) else photographedMany.format(n, place)
    val anywhereOne = stringResource(R.string.people_photographed_any_1)
    val anywhereMany = stringResource(R.string.people_photographed_any_n)
    var loadingMore by remember { mutableStateOf(false) }
    var noMore by remember { mutableStateOf(false) }

    /** THE NEXT PAGE OF SUGGESTED (Hidde, 2026-11-25; People.swift loadMore): when
     *  the foot of the list comes into view, the most active public photographers
     *  anywhere, 20 at a time, never somebody shown or followed; stops after the
     *  last one or when the server cannot answer. */
    suspend fun loadMore() {
        if (source != PeopleSource.SEARCH || me == null || demo || loadingMore || noMore) return
        loadingMore = true
        try {
            val shown = suggestions
            val rows = host.profiles.morePhotographers(shown.map { it.profile.userId }, 20, token())
            if (rows == null) { noMore = true; return }
            if (rows.size < 20) noMore = true
            val seen = shown.map { it.profile.userId }.toHashSet()
            val next = rows.filter {
                it.userId != me && !host.moderation.hides(it.userId) && it.displayName.isNotEmpty() && seen.add(it.userId)
            }.map {
                Suggestion(Profiles.Profile(it.userId, it.displayName, it.avatarUrl),
                    if (it.trees == 1) anywhereOne else anywhereMany.format(it.trees), false)
            }
            if (next.isEmpty()) { noMore = true; return }
            host.profiles.loadAmbassadors(next.map { it.profile.userId }, token())
            suggestions = shown + next
        } finally { loadingMore = false }
    }

    suspend fun loadSuggestions() {
        if (source != PeopleSource.SEARCH || me == null) { suggestions = emptyList(); loadFollowing(); return }
        if (demo) {
            suggestions = DemoPeople.suggestions.map {
                Suggestion(it.profile, if (it.ambassador) reasonAmbassador(it.place) else reasonPhoto(it.count ?: 0, it.place), it.ambassador)
            }
            return
        }
        val cat = host.catalogue ?: run { loadFollowing(); return }
        // Your places, most trees first.
        val places = host.yourTrees.mapNotNull { cat.tree(it)?.citySlug }.groupingBy { it }.eachCount()
            .entries.sortedWith(compareBy({ -it.value }, { it.key })).map { it.key }
        val rank = places.withIndex().associate { it.value to it.index }
        val t = token()
        // Who you follow and who photographed your places, at the same time.
        val shots = kotlinx.coroutines.coroutineScope {
            val following = async { loadFollowing() }
            val photographers = async { host.profiles.photographers(places.take(6).associateWith { s -> cat.trees(s).map { it.id } }, t) }
            following.await()
            photographers.await()
        }
        val names = cat.browse?.cities.orEmpty().filter { it.slug != null }.associate { it.slug!! to it.name }
        val ambassadors = cat.browse?.cities.orEmpty().flatMap { c ->
            val slug = c.slug ?: return@flatMap emptyList()
            c.ambassadors.mapNotNull { a -> a.profile?.let { Triple(it, a.name, slug) } }
        }
        fun amb(a: Triple<String, String, String>) = Suggestion(Profiles.Profile(a.first, a.second, null), reasonAmbassador(names[a.third] ?: a.third), true)
        val mine = ambassadors.filter { it.third in rank }.sortedBy { rank[it.third] }.map(::amb)
        val others = ambassadors.filter { it.third !in rank }.map(::amb)
        val photo = shots.sortedWith(compareBy({ rank[it.place] ?: Int.MAX_VALUE }, { -it.trees })).map {
            Suggestion(Profiles.Profile(it.userId, it.displayName, it.avatarUrl), reasonPhoto(it.trees, names[it.place] ?: it.place), false)
        }
        val seen = HashSet<String>()
        var list = (mine + photo + others).filter {
            val id = it.profile.userId
            id != me && !host.moderation.hides(id) && it.profile.displayName.isNotEmpty() && seen.add(id)
        }.filter { it.profile.userId !in followingIds }.take(12)
        // On screen now; the names and badges below follow a moment later.
        if (suggestions.isEmpty()) suggestions = list
        // The name and picture as their owner set them today.
        val fresh = host.profiles.byIds(list.map { it.profile.userId }, t).associateBy { it.userId }
        list = list.map { s -> fresh[s.profile.userId]?.let { p -> s.copy(profile = s.profile.copy(displayName = p.displayName.ifEmpty { s.profile.displayName }, avatarUrl = p.avatarUrl)) } ?: s }
        host.profiles.loadAmbassadors(list.map { it.profile.userId }, t)
        suggestions = list
        noMore = false
        me?.let { lastSuggestions = it to list }
    }

    LaunchedEffect(me) {
        if (demo && source != PeopleSource.SEARCH) results = DemoPeople.all
        // Suggestions load who you follow alongside (and the demo's stand-ins); the
        // follower lists only need the follow state.
        if (source == PeopleSource.SEARCH) loadSuggestions() else loadFollowing()
    }
    LaunchedEffect(source, me) {
        if (source == PeopleSource.SEARCH || me == null || demo) return@LaunchedEffect
        searching = true
        val t = token()
        val whose = if (isMine) me else owner ?: me
        val ids = if (source == PeopleSource.FOLLOWERS) host.profiles.followerIds(whose, t) else host.profiles.followingIds(whose, t)
        val known = host.profiles.byIds(ids, t).associateBy { it.userId }
        host.profiles.loadAmbassadors(ids, t)
        // A count and a list that disagree is worse than either: a follower with no name yet still gets a row.
        results = ids.map { known[it] ?: Profiles.Profile(it, "", null) }
        searching = false
    }
    LaunchedEffect(query) {
        if (source != PeopleSource.SEARCH) return@LaunchedEffect
        if (demo) { results = if (query.isBlank()) emptyList() else DemoPeople.all; return@LaunchedEffect }
        if (me == null) { results = emptyList(); return@LaunchedEffect }
        searching = true
        delay(300)
        results = host.profiles.search(query, token())
        host.profiles.loadAmbassadors(results.map { it.userId }, token())
        searching = false
    }

    // On somebody else's list you are a row too, so it agrees with the count.
    val visible = results.filter { !isMine || it.userId != me }.let { o -> o.filter { !host.moderation.hides(it.userId) } + o.filter { host.moderation.hides(it.userId) } }
    val showsSuggestions = source == PeopleSource.SEARCH && me != null && query.isBlank() && suggestions.isNotEmpty()
    val emptyLine = when (source) {
        PeopleSource.SEARCH -> if (me == null) stringResource(R.string.people_sign_in) else if (query.isEmpty()) null else stringResource(R.string.people_none)
        PeopleSource.FOLLOWERS -> stringResource(if (isMine) R.string.people_no_followers else R.string.people_no_followers_them)
        PeopleSource.FOLLOWING -> stringResource(if (isMine) R.string.people_no_following else R.string.people_no_following_them)
    }

    fun toggle(p: Profiles.Profile) {
        if (me == null) { host.signIn(SignInReason.General); return }
        val was = p.userId in followingIds
        if (was) followingIds.remove(p.userId) else followingIds.add(p.userId)
        if (demo) return
        scope.launch {
            val t = host.account.fresh()?.accessToken
            if (t == null) {
                if (was) followingIds.add(p.userId) else followingIds.remove(p.userId)
                host.signIn(SignInReason.General); return@launch
            }
            val ok = if (was) host.profiles.unfollow(p.userId, me, t) else host.profiles.follow(p.userId, me, t)
            if (!ok) { if (was) followingIds.add(p.userId) else followingIds.remove(p.userId) }
            loadFollowing()
        }
    }

    fun shareProfile(uid: String) {
        app.ancienttrees.account.Measure.event("share_tapped", mapOf("where" to "profile"))
        val url = "https://ancienttrees.app/profile?u=$uid&utm_source=share&utm_medium=app&utm_campaign=profile"
        val send = Intent(Intent.ACTION_SEND).apply {
            type = "text/plain"
            putExtra(Intent.EXTRA_TEXT, context.getString(R.string.people_share_line) + " " + url)
        }
        runCatching { context.startActivity(Intent.createChooser(send, null)) }
    }

    Column(Modifier.fillMaxSize().background(brand.ground).testTag("people-sheet")) {
        PushedBar(
            stringResource(
                when (source) {
                    PeopleSource.SEARCH -> R.string.people_find
                    PeopleSource.FOLLOWERS -> R.string.people_followers
                    PeopleSource.FOLLOWING -> R.string.people_following
                },
            ),
            onBack,
        )
        if (source == PeopleSource.SEARCH) SearchField(query) { query = it }
        // PULL TO REFRESH on Find people (People.swift RefreshableWhen; Hidde,
        // 2026-11-04, "dat doen ze toch ook bij insta"): who you follow and
        // Suggested load again. Followers and Following keep still.
        RefreshableWhen(on = source == PeopleSource.SEARCH, refreshing = refreshing, onRefresh = {
            scope.launch {
                refreshing = true
                loadFollowing()
                loadSuggestions()
                refreshing = false
            }
        }) {
        LazyColumn(contentPadding = PaddingValues(bottom = 90.dp), modifier = Modifier.fillMaxSize()) {
            if (visible.isEmpty() && !searching && !showsSuggestions && emptyLine != null) {
                item {
                    Text(emptyLine, fontSize = 15.sp, color = brand.inkSoft, modifier = Modifier.padding(start = 20.dp, end = 20.dp, top = 4.dp, bottom = 12.dp))
                }
            }
            if (source == PeopleSource.SEARCH && me != null) {
                item {
                    Row(
                        horizontalArrangement = Arrangement.spacedBy(12.dp),
                        verticalAlignment = Alignment.CenterVertically,
                        // The iPhone's list cell: 74 tall, its icon from 16 (SweepFrames people).
                        modifier = Modifier.fillMaxWidth().heightIn(min = 74.dp)
                            .clickable(role = Role.Button) {
                                when {
                                    host.profiles.myPublic == true -> shareProfile(me)
                                    host.profiles.me?.displayName.isNullOrEmpty() -> host.editName()
                                    else -> askingPublic = true
                                }
                            }
                            .padding(horizontal = 16.dp, vertical = 6.dp).testTag("people-share"),
                    ) {
                        Box(Modifier.size(32.dp), contentAlignment = Alignment.Center) {
                            Icon(Sym.Share, null, tint = brand.moss, modifier = Modifier.size(20.dp))
                        }
                        Text(stringResource(R.string.people_share), fontSize = 16.sp, color = brand.ink)
                    }
                    // From the words to 16 short of the edge, as iOS 26's list separator.
                    HorizontalDivider(Modifier.padding(start = 60.dp, end = 16.dp), thickness = 0.5.dp, color = brand.hairline)
                }
            }
            if (showsSuggestions) {
                item {
                    // iOS 26's section header: 22 below the share cell, 33 tall, the
                    // word on its foot (SweepFrames: 272 to 305 under a cell ending at 250).
                    Box(Modifier.fillMaxWidth().padding(top = 22.dp).height(33.dp), contentAlignment = Alignment.BottomStart) {
                        Eyebrow(stringResource(R.string.people_suggested), Modifier.padding(start = 16.dp, bottom = 7.dp).testTag("people-suggested"))
                    }
                }
                items(suggestions, key = { "s" + it.profile.userId }) { s ->
                    PersonRow(host, s.profile, s.reason, s.ambassador || host.profiles.placesByUser[s.profile.userId].orEmpty().isNotEmpty(),
                        following = s.profile.userId in followingIds, source = source, onFollow = { toggle(s.profile) }, onMore = { acting = s.profile })
                }
                // The foot of Suggested: in view, it asks for the next page.
                if (!noMore) item(key = "s-more") {
                    LaunchedEffect(suggestions.size) { loadMore() }
                    Box(Modifier.fillMaxWidth().height(56.dp).testTag("people-suggested-more"), contentAlignment = Alignment.Center) {
                        if (loadingMore) androidx.compose.material3.CircularProgressIndicator(Modifier.size(22.dp), color = brand.inkSoft, strokeWidth = 2.dp)
                    }
                }
            } else {
                items(visible, key = { it.userId }) { p ->
                    PersonRow(host, p, null, false, following = p.userId in followingIds, source = source,
                        onFollow = { toggle(p) }, onMore = { acting = p }, mineList = isMine)
                }
            }
        }
        }
    }

    if (askingPublic && me != null) {
        MakePublicSheet(
            onYes = {
                scope.launch {
                    val t = host.account.fresh()?.accessToken
                    val ok = t != null && host.profiles.savePublic(true, me, t)
                    askingPublic = false
                    if (ok) { delay(450); shareProfile(me) }
                }
            },
            onNo = { askingPublic = false },
        )
    }
    PersonActions(host, acting, onClose = { acting = null })
}

/**
 * THE PERSON MENU (Report, Block or Unblock), its reasons and its thanks: one
 * version for Find people's rows and the more button on a person's profile
 * (Hidde, 2026-11-22, "Ja, bouw het"; People.swift PersonActions; AllTrails'
 * "..." on a profile, "Block user"). onChange runs after a block or unblock.
 */
@Composable
fun PersonActions(host: PeopleHost, acting: Profiles.Profile?, onClose: () -> Unit, onChange: () -> Unit = {}) {
    val scope = rememberCoroutineScope()
    var reporting by remember { mutableStateOf<Profiles.Profile?>(null) }
    var reported by remember { mutableStateOf(false) }
    acting?.let { p ->
        val hidden = host.moderation.hides(p.userId)
        BrandSheet(
            title = p.displayName,
            message = stringResource(R.string.people_block_body),
            onDismiss = onClose,
            buttons = listOf(
                SheetButton(stringResource(R.string.people_report), SheetKind.SECONDARY) { onClose(); reported = false; reporting = p },
                if (hidden) {
                    SheetButton(stringResource(R.string.people_unblock_person), SheetKind.SECONDARY) { block(host, p, scope, onChange); onClose() }
                } else {
                    SheetButton(stringResource(R.string.people_block_person), SheetKind.DESTRUCTIVE) { block(host, p, scope, onChange); onClose() }
                },
            ),
        )
    }
    reporting?.let { p ->
        if (reported) {
            BrandSheet(
                title = stringResource(R.string.people_thanks),
                message = stringResource(R.string.people_thanks_body),
                icon = Sym.Check,
                onDismiss = { reporting = null },
                buttons = listOf(SheetButton(stringResource(R.string.done), SheetKind.PRIMARY, tag = "report-thanks-done") { reporting = null }),
            )
        } else {
            val reasons = listOf(R.string.report_offensive, R.string.report_impersonation, R.string.report_spam, R.string.report_other)
            // The reason goes to the server in the iPhone's English words, so one queue reads one language.
            val english = listOf("An offensive name or picture", "Pretending to be somebody else", "Spam or advertising", "Something else")
            BrandSheet(
                title = stringResource(R.string.people_why_report),
                onDismiss = { reporting = null },
                buttons = reasons.mapIndexed { i, r ->
                    SheetButton(stringResource(r), SheetKind.SECONDARY) {
                        scope.launch {
                            val s = host.userId
                            val t = host.account.fresh()?.accessToken
                            if (s != null && t != null) host.moderation.report(p.userId, english[i], s, t)
                            reported = true
                        }
                    }
                },
            )
        }
    }
}

private fun block(host: PeopleHost, p: Profiles.Profile, scope: kotlinx.coroutines.CoroutineScope, onChange: () -> Unit = {}) {
    val me = host.userId ?: return
    scope.launch {
        val t = host.account.fresh()?.accessToken ?: return@launch
        if (host.moderation.hides(p.userId)) host.moderation.unblock(p.userId, me, t) else host.moderation.block(p.userId, me, t)
        onChange()
    }
}

/** Pull to refresh on Find people only (People.swift RefreshableWhen); the two lists keep still. */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun RefreshableWhen(on: Boolean, refreshing: Boolean, onRefresh: () -> Unit, content: @Composable () -> Unit) {
    if (on) {
        PullToRefreshBox(isRefreshing = refreshing, onRefresh = onRefresh, modifier = Modifier.fillMaxSize()) { content() }
    } else {
        content()
    }
}

/** The search field on top of Find people, drawn under the bar always. */
@Composable
private fun SearchField(query: String, onChange: (String) -> Unit) {
    val brand = Brand.colors
    val keyboard = androidx.compose.ui.platform.LocalSoftwareKeyboardController.current
    BasicTextField(
        value = query,
        onValueChange = onChange,
        singleLine = true,
        textStyle = sfStyle(fontSize = 17.sp, color = brand.ink),
        // .searchable's Search key puts the keyboard away (MapSearch.kt's field).
        keyboardOptions = KeyboardOptions(autoCorrectEnabled = false, imeAction = androidx.compose.ui.text.input.ImeAction.Search),
        keyboardActions = androidx.compose.foundation.text.KeyboardActions(onSearch = { keyboard?.hide() }),
        // The iPhone's bar carries its search field in 60 under the 54 (SweepFrames
        // people: the first cell at 114 below the safe area): iOS 26's white capsule,
        // 44 tall with a soft shadow, right under the bar, then 16 (its shot: 117 to
        // 160; the field here was 40 and grey, 2026-11-12).
        modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp).padding(bottom = 16.dp),
        decorationBox = { inner ->
            Row(
                verticalAlignment = Alignment.CenterVertically,
                modifier = Modifier.fillMaxWidth().height(44.dp)
                    .shadow(10.dp, RoundedCornerShape(50), ambientColor = Color.Black.copy(alpha = 0.12f), spotColor = Color.Black.copy(alpha = 0.12f))
                    .background(brand.surface, RoundedCornerShape(50)).padding(horizontal = 14.dp),
            ) {
                Icon(Sym.Search, null, tint = brand.ink, modifier = Modifier.size(20.dp))
                Spacer(Modifier.size(6.dp))
                Box(Modifier.weight(1f)) {
                    if (query.isEmpty()) Text(stringResource(R.string.people_search), fontSize = 17.sp, color = brand.inkSoft.copy(alpha = 0.8f))
                    inner()
                }
                // .searchable's clear button once there is text (MapSearch.kt's).
                if (query.isNotEmpty()) {
                    Box(
                        contentAlignment = Alignment.Center,
                        modifier = Modifier.size(44.dp).clickable { onChange("") }
                            .semantics { contentDescription = "Clear" },
                    ) { Icon(Sym.CancelFill, null, tint = brand.inkSoft, modifier = Modifier.size(20.dp)) }
                }
            }
        },
    )
}

/** One person: picture, name, a badge or the reason they are suggested, Follow, and the ellipsis. */
@Composable
private fun PersonRow(
    host: PeopleHost,
    p: Profiles.Profile,
    reason: String?,
    seal: Boolean,
    following: Boolean,
    source: PeopleSource,
    onFollow: () -> Unit,
    onMore: () -> Unit,
    mineList: Boolean = true,
) {
    val brand = Brand.colors
    val keyboardNow = androidx.compose.ui.platform.LocalSoftwareKeyboardController.current
    val hidden = host.moderation.hides(p.userId)
    val scope = rememberCoroutineScope()
    Row(
        verticalAlignment = Alignment.CenterVertically,
        // The iPhone's list row: 17 above and below a 44 row (78 apart), the avatar
        // at 16, the more button ending 16 from the edge (SweepFrames people).
        modifier = Modifier.fillMaxWidth().padding(start = 16.dp, end = 16.dp, top = 17.dp, bottom = 17.dp),
    ) {
        // People.swift: HStack(spacing: 12) of the name button, which hugs what it
        // holds, a Spacer(minLength: 8), Follow and the ellipsis. The flexible room
        // is this Box; the tap area inside it is only as wide as the name.
        Box(Modifier.weight(1f)) { Row(
            horizontalArrangement = Arrangement.spacedBy(12.dp),
            verticalAlignment = Alignment.CenterVertically,
            // The keyboard goes as a profile opens (it stayed up over the profile and
            // the first back only closed it; the test-account walk, 2026-11-17).
            modifier = Modifier.clickable(role = Role.Button) { keyboardNow?.hide(); host.openPerson(p.userId) }.testTag("person-open"),
        ) {
            Box {
                Avatar(p.avatarUrl, p.displayName, 40, initialSize = 16)
                if (seal) {
                    Box(Modifier.align(Alignment.BottomEnd).offset(3.dp, 3.dp).background(brand.ground, CircleShape)) {
                        Icon(Sym.VerifiedFill, stringResource(R.string.people_ambassador), tint = brand.moss, modifier = Modifier.size(15.dp))
                    }
                }
            }
            Column(verticalArrangement = Arrangement.spacedBy(3.dp)) {
                Text(
                    p.displayName.ifEmpty { stringResource(R.string.people_no_name) }, fontSize = 16.sp,
                    color = if (p.displayName.isEmpty() || hidden) brand.inkSoft else brand.ink, maxLines = 1, overflow = TextOverflow.Ellipsis,
                )
                if (reason != null) {
                    // Ends in "…" rather than breaking inside a word ("am / bassador")
                    // where big text leaves the column narrow (the small-phone walk).
                    Text(reason, fontSize = 12.sp, color = brand.inkSoft, maxLines = 2, overflow = androidx.compose.ui.text.style.TextOverflow.Ellipsis,
                        )
                } else {
                    AmbassadorBadge(host.profiles.placesByUser[p.userId].orEmpty(), compact = true)
                }
            }
        } }
        Spacer(Modifier.size(32.dp))
        // Yourself, on somebody else's list: no Follow, no more button.
        if (p.userId != host.userId) {
        if (hidden) {
            Text(
                stringResource(R.string.people_unblock), fontSize = 15.sp, fontWeight = FontWeight.SemiBold, color = brand.moss, textAlign = TextAlign.End,
                modifier = Modifier.widthIn(min = 78.dp).heightIn(min = 44.dp).clickable(role = Role.Button) {
                    val me = host.userId ?: return@clickable
                    scope.launch { host.moderation.unblock(p.userId, me, host.account.fresh()?.accessToken) }
                }.padding(vertical = 12.dp).testTag("person-unblock"),
            )
        } else {
            FollowPill(
                if (following) stringResource(R.string.people_following_state)
                else if (source == PeopleSource.FOLLOWERS && mineList) stringResource(R.string.people_follow_back) else stringResource(R.string.people_follow),
                following, "person-follow", onFollow,
            )
        }
        val more = stringResource(R.string.people_more, p.displayName)
        Spacer(Modifier.size(12.dp))
        Box(
            Modifier.size(44.dp).clickable(role = Role.Button, onClick = onMore).semantics { contentDescription = more }.testTag("person-more"),
            contentAlignment = Alignment.Center,
        ) { Icon(Sym.MoreVert, null, tint = brand.inkSoft, modifier = Modifier.size(20.dp)) }
        }
    }
}

/** The pill Strava and Instagram draw: filled while it says Follow, outlined once you do. */
@Composable
fun FollowPill(label: String, on: Boolean, tag: String, onClick: () -> Unit) {
    val brand = Brand.colors
    Box(Modifier.heightIn(min = 44.dp).clickable(role = Role.Button, onClick = onClick).testTag(tag), contentAlignment = Alignment.Center) {
        Box(
            Modifier
                .widthIn(min = 96.dp)
                .height(34.dp)
                .clip(RoundedCornerShape(50))
                .background(if (on) Color.Transparent else brand.moss)
                .let { if (on) it.border(1.dp, brand.hairline, RoundedCornerShape(50)) else it }
                .padding(horizontal = 14.dp),
            contentAlignment = Alignment.Center,
        ) {
            Text(label, fontSize = 15.sp, fontWeight = FontWeight.SemiBold, color = if (on) brand.ink else Color.White)
        }
    }
}

/** A round face: the picture, else the first letter in moss on the moss tint, else the person mark. */
@Composable
fun Avatar(url: String?, name: String?, size: Int, initialSize: Int) {
    val brand = Brand.colors
    Box(Modifier.size(size.dp).clip(CircleShape).background(brand.moss.copy(alpha = 0.12f)), contentAlignment = Alignment.Center) {
        val first = name?.trim()?.firstOrNull()
        when {
            url != null -> RemoteImage(url, null, Modifier.fillMaxSize(), placeholder = false)
            first != null -> Text(first.uppercase(), fontFamily = BrandFace, fontWeight = FontWeight.Black, fontSize = initialSize.sp, color = brand.moss)
            else -> Icon(Sym.PersonFill, null, tint = brand.moss.copy(alpha = 0.6f), modifier = Modifier.size((size * 0.4).dp))
        }
    }
}

/**
 * PersonProfile.swift: My trees as a visitor sees it. Picture, name and flag,
 * the follow line, Follow where your own gear sits, the badges, then Collected
 * and Want to visit over the three-across grid. Private, unknown and unreachable
 * all read the same: "This profile is private."
 */
@Composable
fun PersonProfileScreen(host: PeopleHost, userId: String, onBack: () -> Unit) = PlainText { PersonInner(host, userId, onBack) }

@Composable
private fun PersonInner(host: PeopleHost, userId: String, onBack: () -> Unit) {
    val brand = Brand.colors
    val scope = rememberCoroutineScope()
    val demo = DemoPeople.on(host.args)
    var profile by remember { mutableStateOf<Profiles.PublicProfile?>(null) }
    var loaded by remember { mutableStateOf(false) }
    var following by remember { mutableStateOf(false) }
    var followers by remember { mutableStateOf(0) }
    var early by remember { mutableStateOf(false) }
    var knownName by remember { mutableStateOf<String?>(null) }
    var lane by remember { mutableStateOf(0) }
    var viewingAvatar by remember { mutableStateOf(false) }
    var acting by remember { mutableStateOf<Profiles.Profile?>(null) }

    suspend fun reload() {
        val token = if (demo) null else host.account.fresh()?.accessToken
        val p = host.profiles.publicProfile(userId, token)
        profile = p
        followers = p?.followers ?: 0
        if (p == null) {
            knownName = host.profiles.byIds(listOf(userId), token).firstOrNull()?.displayName
                ?: DemoPeople.all.firstOrNull { it.userId == userId }?.displayName
        }
        loaded = true
        if (p != null) early = EarlyAdopter.has(p.createdAt)
        val me = host.userId
        if (me != null && me != userId && !demo) following = userId in host.profiles.followingIds(me, token)
    }
    LaunchedEffect(userId) { reload() }

    fun toggle() {
        val me = host.userId ?: run { host.signIn(profile?.let { SignInReason.Follow(it.displayName) } ?: SignInReason.General); return }
        val was = following
        following = !was
        followers = maxOf(0, followers + if (was) -1 else 1)
        if (demo) return
        scope.launch {
            val t = host.account.fresh()?.accessToken
            val ok = t != null && (if (was) host.profiles.unfollow(userId, me, t) else host.profiles.follow(userId, me, t))
            if (!ok) { following = was; followers = maxOf(0, followers + if (was) 1 else -1) }
            if (t == null) host.signIn(SignInReason.General)
        }
    }

    Box(Modifier.fillMaxSize()) {
    Column(Modifier.fillMaxSize().background(brand.ground).testTag("person-profile")) {
        // THE MORE BUTTON top right: Report and Block, as AllTrails' and
        // Instagram's "..." on a profile (Hidde, 2026-11-22; PersonProfile.swift).
        // Not on your own profile; signed out, it asks you to sign in.
        val moreLabel = stringResource(R.string.people_more, profile?.displayName ?: knownName ?: "")
        PushedBar("", onBack, trailing = if (loaded && host.userId != userId) ({
            BarIcon(Sym.MoreVert, moreLabel, {
                if (host.userId == null) host.signIn(SignInReason.General)
                else acting = Profiles.Profile(userId, profile?.displayName ?: knownName ?: "", null)
            }, Modifier.testTag("person-profile-more"))
        }) else null)
        // Pull to refresh, as every profile in Instagram, Strava and AllTrails
        // (Hidde, 2026-11-22, "5 ja"; PersonProfile.swift .refreshable).
        PullRefresh({ reload() }) {
        Column(
            verticalArrangement = Arrangement.spacedBy(16.dp),
            modifier = Modifier.fillMaxWidth().verticalScroll(rememberScrollState()).padding(horizontal = 16.dp).padding(top = 8.dp, bottom = 40.dp),
        ) {
            Row(horizontalArrangement = Arrangement.spacedBy(14.dp), verticalAlignment = Alignment.CenterVertically) {
                // A tap on their picture shows it full screen (Hidde, 2026-11-16;
                // PersonProfile.swift viewingAvatar). A letter opens nothing.
                val avatarUrl = profile?.avatarUrl
                val openLabel = stringResource(R.string.photo_open)
                Box(
                    if (avatarUrl == null) Modifier else Modifier.clip(CircleShape)
                        .clickable(role = Role.Button) { viewingAvatar = true }
                        .semantics { contentDescription = openLabel }
                        .testTag("person-avatar"),
                ) { Avatar(avatarUrl, profile?.displayName ?: knownName, 60, initialSize = 24) }
                Column(Modifier.weight(1f), verticalArrangement = Arrangement.spacedBy(2.dp)) {
                    Row(horizontalArrangement = Arrangement.spacedBy(8.dp), verticalAlignment = Alignment.CenterVertically) {
                        Text(profile?.displayName ?: knownName ?: "", fontFamily = BrandFace, fontWeight = FontWeight.Bold, fontSize = 22.sp,
                            color = brand.ink, maxLines = 2, overflow = TextOverflow.Ellipsis, modifier = Modifier.weight(1f, fill = false))
                        CountryFlag(profile?.country)
                    }
                    // Each number opens its list (Hidde, 2026-11-22, "4 ja"; AllTrails,
                    // PersonProfile.swift openList). Signed out, it asks first.
                    profile?.let { p -> FollowLine(followers, p.following,
                        onFollowers = { if (host.userId == null) host.signIn(SignInReason.General) else host.openFollowList(userId, true) },
                        onFollowing = { if (host.userId == null) host.signIn(SignInReason.General) else host.openFollowList(userId, false) }) }
                }
                if (profile != null && host.userId != userId) {
                    FollowPill(stringResource(if (following) R.string.people_following_state else R.string.people_follow), following, "person-profile-follow") { toggle() }
                }
            }
            val p = profile
            if (p != null) {
                if (p.ambassador.isNotEmpty() || early) {
                    Row(horizontalArrangement = Arrangement.spacedBy(6.dp), verticalAlignment = Alignment.CenterVertically) {
                        AmbassadorBadge(p.ambassador.map { Profiles.Ambassador(p.userId, it.lowercase(), it, true) }, size = 13)
                        if (early) EarlyAdopterBadge(13)
                    }
                }
                LaneTabs(lane) { lane = it }
                val trees = (if (lane == 0) p.visited else p.saves).mapNotNull { host.catalogue?.tree(it) }
                // Collected: our trees, Approved on the ones they added, then their own
                // trees (Hidde, 2026-11-12; PersonProfile.swift grid(_:)).
                val own = if (lane == 0) p.own.filter { it.opens } else emptyList()
                val approved = p.approved.toSet()
                if (trees.isEmpty() && own.isEmpty()) {
                    Text(stringResource(if (lane == 0) R.string.person_none_collected else R.string.person_none_saved), fontSize = 15.sp, color = brand.inkSoft)
                } else {
                    Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
                        val tiles: List<@Composable (Modifier) -> Unit> =
                            trees.map { t -> @Composable { m: Modifier -> GridTile(t, t.id in approved, m) { host.openTree(t) } } } +
                                own.map { o -> @Composable { m: Modifier -> OwnTile(o, m) { host.openShared(o.id.lowercase()) } } }
                        for (row in tiles.chunked(3)) {
                            Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                                for (tile in row) tile(Modifier.weight(1f))
                                repeat(3 - row.size) { Spacer(Modifier.weight(1f)) }
                            }
                        }
                    }
                }
            } else if (loaded) {
                Row(horizontalArrangement = Arrangement.spacedBy(8.dp), verticalAlignment = Alignment.CenterVertically, modifier = Modifier.testTag("person-private")) {
                    Icon(Sym.Lock, null, tint = brand.inkSoft, modifier = Modifier.size(18.dp))
                    Text(stringResource(R.string.person_private), fontSize = 16.sp, color = brand.inkSoft)
                }
            }
        }
        }
    }
    // Their own picture: no licence, so no credit line (creditRequired false).
    val face = profile?.avatarUrl
    if (viewingAvatar && face != null) {
        PhotoViewer(listOf(Photo(url = face, license = null, attribution = null, attributionShort = null, thumb = null,
            hero = null, creditRequired = false, creditLine = null, creditUrl = null, frame = null)), 0) { viewingAvatar = false }
    }
    // Report and Block, the same menu Find people's rows open; a block reads the profile again.
    PersonActions(host, acting, onClose = { acting = null }, onChange = { scope.launch { reload() } })
    }
}

/** "12 followers   4 following", the numbers bold. */
@Composable
fun FollowLine(followers: Int, following: Int, onFollowers: (() -> Unit)? = null, onFollowing: (() -> Unit)? = null) {
    val brand = Brand.colors
    val f1 = stringResource(R.string.people_followers_word)
    val f2 = stringResource(R.string.people_following_word)
    if (onFollowers != null && onFollowing != null) {
        // Two taps, each 44 tall to hit, as the iPhone's countButton.
        Row(horizontalArrangement = Arrangement.spacedBy(14.dp), verticalAlignment = Alignment.CenterVertically) {
            FollowCount(followers, f1, "person-followers", onFollowers)
            FollowCount(following, f2, "person-following", onFollowing)
        }
        return
    }
    Text(
        buildAnnotatedString {
            withStyle(SpanStyle(fontWeight = FontWeight.Bold)) { append("$followers") }
            append(" $f1   ")
            withStyle(SpanStyle(fontWeight = FontWeight.Bold)) { append("$following") }
            append(" $f2")
        },
        fontSize = 13.sp, color = brand.inkSoft, maxLines = 1,
    )
}

@Composable
private fun FollowCount(n: Int, word: String, tag: String, onClick: () -> Unit) {
    val brand = Brand.colors
    Box(Modifier.heightIn(min = 44.dp).clickable(role = Role.Button, onClick = onClick).testTag(tag), contentAlignment = Alignment.CenterStart) {
        Text(
            buildAnnotatedString {
                withStyle(SpanStyle(fontWeight = FontWeight.Bold)) { append("$n") }
                append(" $word")
            },
            fontSize = 13.sp, color = brand.inkSoft, maxLines = 1,
        )
    }
}

/** Collect.swift's two lanes, plain underlined tabs on a hairline. */
@Composable
private fun LaneTabs(lane: Int, select: (Int) -> Unit) {
    val brand = Brand.colors
    Box {
        HorizontalDivider(Modifier.align(Alignment.BottomStart), thickness = 1.dp, color = brand.hairline)
        Row(horizontalArrangement = Arrangement.spacedBy(24.dp)) {
            for ((i, label) in listOf(R.string.person_lane_collected, R.string.want_to_visit).withIndex()) {
                val on = lane == i
                Column(
                    Modifier.width(androidx.compose.foundation.layout.IntrinsicSize.Max).clickable(interactionSource = remember { MutableInteractionSource() }, indication = androidx.compose.foundation.LocalIndication.current) { select(i) }
                        .testTag(if (i == 0) "person-lane-collected" else "person-lane-want"),
                ) {
                    Text(stringResource(label), fontSize = 16.sp, fontWeight = FontWeight.SemiBold, color = if (on) brand.ink else brand.inkSoft,
                        modifier = Modifier.padding(vertical = 12.dp))
                    Box(Modifier.fillMaxWidth().height(2.dp).background(if (on) brand.moss else Color.Transparent))
                }
            }
        }
    }
}

/** CollectedTile (.ours): the photograph in a 3:4 tile and the city's tag. */
@Composable
private fun GridTile(t: Tree, approved: Boolean, modifier: Modifier, onOpen: () -> Unit) {
    val brand = Brand.colors
    Box(
        modifier.aspectRatio(3f / 4f).clip(RoundedCornerShape(12.dp)).background(brand.surfaceMuted)
            .clickable(onClick = onOpen).testTag("tree-card"),
    ) {
        val photo = t.photo
        if (photo != null) RemoteImage(photo.card, null, Modifier.fillMaxSize())
        else Text(t.name, fontFamily = BrandFace, fontWeight = FontWeight.Bold, fontSize = 12.sp, color = brand.inkSoft,
            textAlign = TextAlign.Center, maxLines = 4, modifier = Modifier.align(Alignment.Center).padding(8.dp))
        if (t.city.isNotEmpty()) TagPill(t.city, Modifier.align(Alignment.BottomStart).padding(6.dp))
        if (approved) ApprovedPill(Modifier.align(Alignment.TopStart).padding(6.dp))
    }
}

/** CollectedTile (.shared): somebody's own tree, its shared photograph, else its name. */
@Composable
private fun OwnTile(o: Profiles.OwnTree, modifier: Modifier, onOpen: () -> Unit) {
    val brand = Brand.colors
    Box(
        modifier.aspectRatio(3f / 4f).clip(RoundedCornerShape(12.dp)).background(brand.surfaceMuted)
            .clickable(onClick = onOpen).testTag("own-tree-card"),
    ) {
        val named = @Composable {
            Text(o.title, fontFamily = BrandFace, fontWeight = FontWeight.Bold, fontSize = 12.sp, color = brand.inkSoft,
                textAlign = TextAlign.Center, maxLines = 4, modifier = Modifier.align(Alignment.Center).padding(8.dp))
        }
        val url = o.photoUrl
        if (url != null) RemoteImage(o.thumbUrl ?: url, o.title, Modifier.fillMaxSize(), orElse = url,
            fallback = { Box(Modifier.fillMaxSize()) { named() } })
        else named()
    }
}
