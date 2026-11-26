// Screens/Activity.swift: the hearts other people gave your photographs,
// behind the bell top right of Discover (Hidde, 2026-11-22: the bell "voor nu
// is het ok"). Instagram's Activity: one row per photograph, bundled, New above
// Earlier, the photograph at the row's end, a tap opens the tree. From
// my_activity() (supabase/follow-activity.sql; since 2026-11-24 a new follower
// too, "X started following you." with Follow back); opening it calls
// activity_seen(), so the dot goes on every device. Nothing kept on the phone.

package app.ancienttrees.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.platform.testTag
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Icon
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import kotlinx.coroutines.launch
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.SpanStyle
import androidx.compose.ui.text.buildAnnotatedString
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.withStyle
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import app.ancienttrees.account.Supa
import app.ancienttrees.feed.Catalogue
import org.json.JSONArray
import org.json.JSONObject

object ActivityStore {
    /** One row of my_activity (supabase/follow-activity.sql): a heart (one per
     *  photograph, bundled) or a new follower (Hidde, 2026-11-24), Activity.swift's Row. */
    data class Row(
        val photoId: String,
        val treeId: String?,
        val hearts: Int,
        val latestAt: String,
        val names: List<String>,
        val avatars: List<String>,
        val isNew: Boolean,
        val kind: String = "heart",
        val userId: String? = null,
        val following: Boolean = false,
    ) {
        val isFollow: Boolean get() = kind == "follow"
        val key: String get() = if (isFollow) "f" + (userId ?: latestAt) else photoId
    }

    /** Follow back, or take it back: the pill moves at once (Activity.swift setFollowing). */
    fun setFollowing(userId: String, on: Boolean) {
        val i = rows.indexOfFirst { it.isFollow && it.userId == userId }
        if (i >= 0) rows[i] = rows[i].copy(following = on)
    }

    val rows = mutableStateListOf<Row>()
    var loaded by mutableStateOf(false)
    /** Something came after you last opened Activity: the bell's dot. */
    var fresh by mutableStateOf(false)

    suspend fun load(token: String?, n: Int = 60) {
        if (token == null) { rows.clear(); fresh = false; return }
        val r = Supa.send("/rest/v1/rpc/my_activity", token = token, body = JSONObject().put("n", n).toString())
        if (!r.ok) return
        runCatching {
            val a = JSONArray(r.body)
            val got = (0 until a.length()).map { i ->
                val o = a.getJSONObject(i)
                fun list(k: String): List<String> = o.optJSONArray(k)?.let { arr -> (0 until arr.length()).map { arr.optString(it) } } ?: emptyList()
                fun str(k: String): String? = if (o.isNull(k)) null else o.optString(k).ifEmpty { null }
                Row(str("photo_id") ?: "", str("tree_id"), o.optInt("hearts"),
                    o.optString("latest_at"), list("names"), list("avatars"), o.optBoolean("is_new"),
                    kind = str("kind") ?: "heart", userId = str("user_id"), following = o.optBoolean("following"))
            }
            rows.clear(); rows.addAll(got)
            loaded = true
            fresh = got.any { it.isNew }
        }
    }

    suspend fun seen(token: String?) {
        if (token == null) return
        if (Supa.send("/rest/v1/rpc/activity_seen", token = token, body = "{}").ok) fresh = false
    }
}

/** The bell top right of the Feed since 2026-11-26 (Activity.swift ActivityBell): a dot while something is new. */
@Composable
fun ActivityBell(token: suspend () -> String?, open: () -> Unit) {
    LaunchedEffect(Unit) { ActivityStore.load(token(), 5) }
    HeaderDisc(Sym.Bell, "activity-bell", dot = ActivityStore.fresh, onClick = open)
}

/**
 * ONE ROUND BUTTON FOR EVERY TAB'S HEADER (Style.swift HeaderDisc, Hidde 2026-11-26):
 * a 44 dp white disc with a hairline and a soft shadow, a 24 dp glyph in ink, the
 * red dot for something new.
 */
@Composable
fun HeaderDisc(glyph: androidx.compose.ui.graphics.vector.ImageVector, tag: String, dot: Boolean = false, label: String = tag, onClick: () -> Unit) {
    val brand = Brand.colors
    Box(
        contentAlignment = Alignment.Center,
        modifier = Modifier
            .size(44.dp)
            .shadow(2.dp, CircleShape, ambientColor = Color.Black.copy(alpha = 0.06f), spotColor = Color.Black.copy(alpha = 0.06f))
            .clip(CircleShape)
            .background(brand.surface)
            .border(1.dp, brand.hairline, CircleShape)
            .clickable(role = androidx.compose.ui.semantics.Role.Button, onClick = onClick)
            .semantics { contentDescription = label }
            .testTag(tag),
    ) {
        Icon(glyph, null, tint = brand.ink, modifier = Modifier.size(24.dp))
        if (dot) {
            Box(
                Modifier.align(Alignment.TopEnd).offset(x = (-6).dp, y = 6.dp).size(10.dp)
                    .background(Color(0xFFD8573F), CircleShape).border(2.dp, brand.surface, CircleShape),
            )
        }
    }
}

@Composable
fun ActivityPage(catalogue: Catalogue, act: DiscoverActions, onBack: () -> Unit) {
    val brand = Brand.colors
    LaunchedEffect(Unit) {
        val t = act.token()
        ActivityStore.load(t)
        ActivityStore.seen(t)
    }
    Column(Modifier.fillMaxSize().background(brand.ground)) {
        PushedBar("Activity", onBack)
        // Pull to refresh, as Instagram's Activity (Hidde, 2026-11-22, "5 ja"; Activity.swift).
        PullRefresh({ val t = act.token(); ActivityStore.load(t); ActivityStore.seen(t) }) {
        LazyColumn(Modifier.fillMaxSize()) {
            item {
                Text("Hearts on your photographs, and new followers.", fontSize = 15.sp, color = brand.inkSoft,
                    modifier = Modifier.padding(horizontal = 16.dp).padding(bottom = 8.dp))
            }
            val fresh = ActivityStore.rows.filter { it.isNew }
            val old = ActivityStore.rows.filter { !it.isNew }
            if (fresh.isNotEmpty()) {
                item { Day("New") }
                items(fresh, key = { "n" + it.key }) { ActivityRow(it, catalogue, act) }
            }
            if (old.isNotEmpty()) {
                item { Day("Earlier") }
                items(old, key = { "o" + it.key }) { ActivityRow(it, catalogue, act) }
            }
            if (ActivityStore.loaded && ActivityStore.rows.isEmpty()) {
                item {
                    Text("Nothing yet. When someone gives one of your photographs a heart or follows you, it shows here.",
                        fontSize = 15.sp, color = brand.inkSoft, modifier = Modifier.padding(16.dp))
                }
            }
        }
        }
    }
}

@Composable
private fun Day(title: String) {
    // Instagram's notification headings, plain 17 semibold, never the brand's black (2026-11-26).
    Text(title, fontWeight = FontWeight.SemiBold, fontSize = 17.sp, color = Brand.colors.ink,
        modifier = Modifier.padding(start = 16.dp, top = 14.dp, bottom = 4.dp))
}

/** One face, the hearts row's 30 dp circle (Activity.swift ActivityFace). */
@Composable
private fun Face(name: String, avatar: String?) {
    val brand = Brand.colors
    Box(
        Modifier.size(30.dp).clip(CircleShape).background(Color(0xFFE4EBD6)).border(2.dp, brand.ground, CircleShape),
        contentAlignment = Alignment.Center,
    ) {
        if (avatar != null) RemoteImage(avatar, null, Modifier.fillMaxSize())
        else Text(name.take(1).uppercase(), fontSize = 12.sp, fontWeight = FontWeight.Bold, color = brand.moss)
    }
}

/** A NEW FOLLOWER (Hidde, 2026-11-24; Activity.swift followRow): their face,
 *  "X started following you.", Follow back or Following, Find people's pill. */
@Composable
private fun FollowRow(r: ActivityStore.Row, act: DiscoverActions) {
    val brand = Brand.colors
    val scope = androidx.compose.runtime.rememberCoroutineScope()
    val name = r.names.firstOrNull() ?: "A visitor"
    val words = buildAnnotatedString {
        withStyle(SpanStyle(fontWeight = FontWeight.Bold)) { append(name) }
        append(" started following you.  ")
        withStyle(SpanStyle(color = brand.inkSoft)) { append(SentAgo.short(r.latestAt) ?: "") }
    }
    Row(
        Modifier
            .fillMaxWidth()
            .background(if (r.isNew) brand.moss.copy(alpha = 0.08f) else Color.Transparent)
            .padding(horizontal = 16.dp, vertical = 6.dp)
            .semantics { contentDescription = "activity-row" },
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(12.dp),
    ) {
        Row(
            Modifier.weight(1f).clickable { r.userId?.let { act.openPerson(it) } }.padding(vertical = 4.dp)
                .semantics { contentDescription = "activity-follow-open" },
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(12.dp),
        ) {
            Box(Modifier.size(44.dp, 40.dp), contentAlignment = Alignment.Center) {
                Face(name, r.avatars.firstOrNull()?.ifEmpty { null })
            }
            Text(words, fontSize = 14.sp, color = brand.ink, modifier = Modifier.weight(1f))
        }
        val on = r.following
        FollowPill(
            if (on) androidx.compose.ui.res.stringResource(app.ancienttrees.R.string.people_following_state)
            else androidx.compose.ui.res.stringResource(app.ancienttrees.R.string.people_follow_back),
            on, "activity-follow",
        ) {
            val id = r.userId ?: return@FollowPill
            ActivityStore.setFollowing(id, !on)
            scope.launch { if (!act.follow(id, !on)) ActivityStore.setFollowing(id, on) }
        }
    }
}

@Composable
private fun ActivityRow(r: ActivityStore.Row, catalogue: Catalogue, act: DiscoverActions) {
    if (r.isFollow) { FollowRow(r, act); return }
    val brand = Brand.colors
    val tree = r.treeId?.let { catalogue.tree(it) }
    val shot = tree?.shots?.firstOrNull { it.sighting == r.photoId.lowercase() } ?: tree?.photo
    val a = r.names.firstOrNull() ?: "A visitor"
    val t = tree?.name ?: "a tree"
    val words = buildAnnotatedString {
        val bold = SpanStyle(fontWeight = FontWeight.Bold)
        withStyle(bold) { append(a) }
        when {
            r.hearts <= 1 -> {}
            r.hearts == 2 && r.names.size > 1 -> { append(" and "); withStyle(bold) { append(r.names[1]) } }
            else -> { append(" and "); withStyle(bold) { append("${r.hearts - 1} others") } }
        }
        append(" gave your photograph of "); withStyle(bold) { append(t) }; append(" a heart.  ")
        withStyle(SpanStyle(color = brand.inkSoft)) { append(SentAgo.short(r.latestAt) ?: "") }
    }
    Row(
        Modifier
            .fillMaxWidth()
            .background(if (r.isNew) brand.moss.copy(alpha = 0.08f) else Color.Transparent)
            .clickable { tree?.let { act.openTree(it) } }
            .padding(horizontal = 16.dp, vertical = 10.dp)
            .semantics { contentDescription = "activity-row" },
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(12.dp),
    ) {
        Box(Modifier.size(44.dp, 40.dp)) {
            val n = maxOf(1, minOf(2, r.names.size))
            for (i in 0 until n) {
                val name = r.names.getOrNull(i) ?: "A visitor"
                val av = r.avatars.getOrNull(i)?.ifEmpty { null }
                Box(Modifier.offset(x = (i * 14).dp, y = if (n == 1) 5.dp else (i * 10).dp)) {
                    Box(
                        Modifier.size(30.dp).clip(CircleShape).background(Color(0xFFE4EBD6)).border(2.dp, brand.ground, CircleShape),
                        contentAlignment = Alignment.Center,
                    ) {
                        if (av != null) RemoteImage(av, null, Modifier.fillMaxSize())
                        else Text(name.take(1).uppercase(), fontSize = 12.sp, fontWeight = FontWeight.Bold, color = brand.moss)
                    }
                }
            }
        }
        Text(words, fontSize = 14.sp, color = brand.ink, modifier = Modifier.weight(1f))
        shot?.let {
            RemoteImage(it.card, null, Modifier.size(48.dp).clip(RoundedCornerShape(8.dp)))
        }
    }
}

/** Pull to refresh on a pushed page (Material's PullToRefreshBox), the iPhone's .refreshable. */
@OptIn(androidx.compose.material3.ExperimentalMaterial3Api::class)
@Composable
fun PullRefresh(onRefresh: suspend () -> Unit, content: @Composable () -> Unit) {
    val scope = androidx.compose.runtime.rememberCoroutineScope()
    var refreshing by androidx.compose.runtime.remember { mutableStateOf(false) }
    androidx.compose.material3.pulltorefresh.PullToRefreshBox(
        isRefreshing = refreshing,
        onRefresh = { scope.launch { refreshing = true; try { onRefresh() } finally { refreshing = false } } },
        modifier = Modifier.fillMaxSize(),
    ) { content() }
}
