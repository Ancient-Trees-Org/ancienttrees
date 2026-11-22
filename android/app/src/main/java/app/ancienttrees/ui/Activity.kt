// Screens/Activity.swift: the hearts other people gave your photographs,
// behind the bell top right of Discover (Hidde, 2026-11-22: the bell "voor nu
// is het ok"). Instagram's Activity: one row per photograph, bundled, New above
// Earlier, the photograph at the row's end, a tap opens the tree. From
// my_photo_activity() (supabase/photo-hearts-who.sql); opening it calls
// activity_seen(), so the dot goes on every device. Nothing kept on the phone.

package app.ancienttrees.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
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
    data class Row(
        val photoId: String,
        val treeId: String?,
        val hearts: Int,
        val latestAt: String,
        val names: List<String>,
        val avatars: List<String>,
        val isNew: Boolean,
    )

    val rows = mutableStateListOf<Row>()
    var loaded by mutableStateOf(false)
    /** Something came after you last opened Activity: the bell's dot. */
    var fresh by mutableStateOf(false)

    suspend fun load(token: String?, n: Int = 60) {
        if (token == null) { rows.clear(); fresh = false; return }
        val r = Supa.send("/rest/v1/rpc/my_photo_activity", token = token, body = JSONObject().put("n", n).toString())
        if (!r.ok) return
        runCatching {
            val a = JSONArray(r.body)
            val got = (0 until a.length()).map { i ->
                val o = a.getJSONObject(i)
                fun list(k: String): List<String> = o.optJSONArray(k)?.let { arr -> (0 until arr.length()).map { arr.optString(it) } } ?: emptyList()
                Row(o.getString("photo_id"), o.optString("tree_id").ifEmpty { null }, o.optInt("hearts"),
                    o.optString("latest_at"), list("names"), list("avatars"), o.optBoolean("is_new"))
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

/** The bell top right of Discover (Activity.swift ActivityBell): a dot while something is new. */
@Composable
fun ActivityBell(act: DiscoverActions, open: () -> Unit) {
    val brand = Brand.colors
    LaunchedEffect(Unit) { ActivityStore.load(act.token(), 5) }
    Box(
        Modifier
            .size(44.dp)
            .clickable(onClick = open)
            .semantics { contentDescription = "activity-bell" },
        contentAlignment = Alignment.Center,
    ) {
        Box(Modifier.size(40.dp).background(brand.surface, CircleShape), contentAlignment = Alignment.Center) {
            Icon(Sym.Bell, null, tint = brand.ink, modifier = Modifier.size(20.dp))
        }
        if (ActivityStore.fresh) {
            Box(
                Modifier.align(Alignment.TopEnd).offset(x = (-7).dp, y = 7.dp).size(9.dp)
                    .background(Color(0xFFD8573F), CircleShape).border(2.dp, brand.ground, CircleShape),
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
        LazyColumn(Modifier.fillMaxSize()) {
            item {
                Text("Hearts on your photographs.", fontSize = 15.sp, color = brand.inkSoft,
                    modifier = Modifier.padding(horizontal = 16.dp).padding(bottom = 8.dp))
            }
            val fresh = ActivityStore.rows.filter { it.isNew }
            val old = ActivityStore.rows.filter { !it.isNew }
            if (fresh.isNotEmpty()) {
                item { Day("New") }
                items(fresh, key = { "n" + it.photoId }) { ActivityRow(it, catalogue, act) }
            }
            if (old.isNotEmpty()) {
                item { Day("Earlier") }
                items(old, key = { "o" + it.photoId }) { ActivityRow(it, catalogue, act) }
            }
            if (ActivityStore.loaded && ActivityStore.rows.isEmpty()) {
                item {
                    Text("No hearts yet. When someone gives one of your photographs a heart, it shows here.",
                        fontSize = 15.sp, color = brand.inkSoft, modifier = Modifier.padding(16.dp))
                }
            }
        }
    }
}

@Composable
private fun Day(title: String) {
    Text(title, fontFamily = BrandFace, fontWeight = FontWeight.Black, fontSize = 15.sp, color = Brand.colors.ink,
        modifier = Modifier.padding(start = 16.dp, top = 14.dp, bottom = 4.dp))
}

@Composable
private fun ActivityRow(r: ActivityStore.Row, catalogue: Catalogue, act: DiscoverActions) {
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
