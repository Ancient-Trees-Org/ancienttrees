// Kit/PhotoLikes.swift: the heart on a visitor's photograph (Hidde, 2026-11-20:
// "Ja, bouw het hartje"). One store for the app, counts asked in one call for
// every heart that appeared within a moment of each other, a write the server
// refuses puts the heart back, nothing kept on the device (hard rule 11).
// supabase/photo-likes.sql: the count is public, who gave it is not.

package app.ancienttrees.ui

import androidx.compose.ui.platform.testTag
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.compose.ui.draw.clip
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.ui.graphics.drawscope.translate
import androidx.compose.ui.draw.drawWithContent
import androidx.compose.foundation.combinedClickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.widthIn
import androidx.compose.material3.Icon
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.mutableStateMapOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import app.ancienttrees.account.Supa
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import org.json.JSONArray
import org.json.JSONObject

object PhotoLikes {
    data class State(val count: Int = 0, val mine: Boolean = false)

    val states = mutableStateMapOf<String, State>()
    private val asked = mutableSetOf<String>()
    private val waiting = mutableSetOf<String>()
    private var token: String? = null
    private var scheduled = false

    fun state(id: String): State = states[id] ?: State()

    /** A heart appeared: its count joins the next call, ~150 ms later. A new session asks again. */
    suspend fun want(id: String, token: String?) {
        if (token != this.token) { this.token = token; asked.clear() }
        if (id in asked) return
        waiting.add(id)
        if (scheduled) return
        scheduled = true
        delay(150)
        val ids = waiting.toList()
        waiting.clear(); scheduled = false
        asked.addAll(ids)
        load(ids, this.token)
    }

    private suspend fun load(ids: List<String>, token: String?) {
        if (ids.isEmpty()) return
        val r = Supa.send("/rest/v1/rpc/photo_like_counts", token = token, body = JSONObject().put("ids", JSONArray(ids)).toString())
        if (!r.ok) return
        runCatching {
            ids.forEach { if (states[it] == null) states[it] = State() }
            val a = JSONArray(r.body)
            for (i in 0 until a.length()) {
                val o = a.getJSONObject(i)
                states[o.getString("photo_id")] = State(o.optInt("likes"), o.optBoolean("mine"))
            }
        }
    }

    /**
     * The heart tapped signed out, given once the account is in (PhotoLikes.swift
     * giveAfterSignIn, 2026-11-27). The count is asked again with the new session first,
     * so a heart this account already gave on another phone is not given twice.
     */
    private val afterSignIn = kotlinx.coroutines.MainScope()
    fun giveAfterSignIn(id: String, token: suspend () -> String?) {
        afterSignIn.launch {
            val t = token() ?: return@launch
            load(listOf(id), t)
            give(id, t)
        }
    }

    /** Give or take back, shown at once; refused, it goes back. */
    /** A double tap only ever gives (Instagram); a heart already given stays. */
    suspend fun give(id: String, token: String) {
        if (state(id).mine) return
        toggle(id, token)
    }

    suspend fun toggle(id: String, token: String) {
        val was = state(id)
        val give = !was.mine
        states[id] = State(maxOf(0, was.count + if (give) 1 else -1), give)
        // ignore-duplicates: the table grants no UPDATE (PhotoLikes.swift).
        val r = if (give) {
            Supa.send("/rest/v1/photo_likes?on_conflict=user_id,photo_id", token = token,
                body = JSONArray().put(JSONObject().put("photo_id", id)).toString(),
                prefer = "resolution=ignore-duplicates,return=minimal")
        } else {
            Supa.send("/rest/v1/photo_likes?photo_id=eq.$id", method = "DELETE", token = token, prefer = "return=minimal")
        }
        if (!r.ok) states[id] = was
    }
}

/**
 * PhotoHeart (Kit/PhotoLikes.swift): outlined, filled moss once given, the count from one.
 * Two taps since 2026-11-22: the heart gives or takes back, the count opens who gave one
 * (PhotoLikersSheet). Signed out either asks for a sign-in.
 */
/**
 * DOUBLE TAP A PHOTOGRAPH FOR A HEART (PhotoLikes.swift DoubleTapHeart; Hidde,
 * 2026-11-22, "2 sounds good"; Instagram): a big white heart pops over the photo
 * and the heart under it fills. Gives only; signed out it asks. The single tap
 * still opens, a moment later, as on Instagram.
 */
@OptIn(androidx.compose.foundation.ExperimentalFoundationApi::class)
@Composable
fun Modifier.doubleTapHeart(photoId: String, onTap: () -> Unit): Modifier {
    val marks = LocalTreeMarks.current
    val scope = rememberCoroutineScope()
    val haptic = androidx.compose.ui.platform.LocalHapticFeedback.current
    var burst by remember { mutableStateOf(false) }
    val scale by androidx.compose.animation.core.animateFloatAsState(if (burst) 1f else 0.4f, label = "heart-scale")
    val alpha by androidx.compose.animation.core.animateFloatAsState(if (burst) 1f else 0f, label = "heart-alpha")
    return this
        .combinedClickable(
            interactionSource = remember { MutableInteractionSource() },
            indication = androidx.compose.foundation.LocalIndication.current,
            onClick = onTap,
            onDoubleClick = {
                if (!marks.signedIn) {
                    val then = marks.signInThen
                    if (then != null) then { PhotoLikes.giveAfterSignIn(photoId, marks.token) } else marks.signIn()
                    return@combinedClickable
                }
                haptic.performHapticFeedback(androidx.compose.ui.hapticfeedback.HapticFeedbackType.LongPress)
                burst = true
                scope.launch {
                    marks.token()?.let { PhotoLikes.give(photoId, it) }
                    kotlinx.coroutines.delay(650)
                    burst = false
                }
            },
        )
        .wrapHeart(scale, alpha)
}

@Composable
private fun Modifier.wrapHeart(scale: Float, alpha: Float): Modifier {
    val heart = androidx.compose.ui.graphics.vector.rememberVectorPainter(Sym.HeartFill)
    return this.drawWithContent {
        drawContent()
        if (alpha > 0f) {
            val s = 72.dp.toPx() * scale
            translate(left = (size.width - s) / 2f, top = (size.height - s) / 2f) {
                with(heart) { draw(androidx.compose.ui.geometry.Size(s, s), alpha = alpha, colorFilter = androidx.compose.ui.graphics.ColorFilter.tint(Color.White)) }
            }
        }
    }
}

@Composable
fun PhotoHeart(photoId: String, onDark: Boolean = false, size: androidx.compose.ui.unit.Dp = 15.dp) {
    val marks = LocalTreeMarks.current
    val brand = Brand.colors
    val scope = rememberCoroutineScope()
    val s = PhotoLikes.state(photoId)
    var likers by remember { mutableStateOf(false) }
    LaunchedEffect(photoId, marks.signedIn) { PhotoLikes.want(photoId, marks.token()) }
    val tint = when {
        s.mine -> if (onDark) Color.White else brand.moss
        else -> if (onDark) Color.White.copy(alpha = 0.85f) else brand.inkSoft
    }
    Row(verticalAlignment = Alignment.CenterVertically) {
        Box(
            contentAlignment = Alignment.Center,
            modifier = Modifier
                .widthIn(min = 26.dp)
                .heightIn(min = 44.dp)
                .clickable(interactionSource = remember { MutableInteractionSource() }, indication = null, role = Role.Button) {
                    if (marks.signedIn) {
                        scope.launch { marks.token()?.let { PhotoLikes.toggle(photoId, it) } }
                    } else {
                        // The heart lands after the sign-in (Hidde, 2026-11-27): given, never
                        // toggled, as the save does (PhotoLikes.swift).
                        val then = marks.signInThen
                        if (then != null) then { PhotoLikes.giveAfterSignIn(photoId, marks.token) } else marks.signIn()
                    }
                }
                .semantics { contentDescription = "photo-like" }
                .testTag("photo-like"),
        ) {
            Icon(if (s.mine) Sym.HeartFill else Sym.Heart, null, tint = tint, modifier = Modifier.size(size))
        }
        if (s.count > 0) {
            Box(
                contentAlignment = Alignment.CenterStart,
                modifier = Modifier
                    .widthIn(min = 22.dp)
                    .heightIn(min = 44.dp)
                    .clickable(interactionSource = remember { MutableInteractionSource() }, indication = null, role = Role.Button) {
                        if (marks.signedIn) likers = true else marks.signIn()
                    }
                    .semantics { contentDescription = "photo-like-count" },
            ) {
                Text("${s.count}", fontSize = 12.sp, fontWeight = FontWeight.SemiBold, color = tint)
            }
        }
    }
    if (likers) PhotoLikersSheet(photoId) { likers = false }
}

/** One row of photo_likers: the account only for a public profile or your own. */
data class Liker(val userId: String?, val name: String?, val avatar: String?)

/**
 * The name on a row (PhotoLikersList.label): "You" for your own heart (the server
 * sends your own account back even when your profile is private), the public name
 * for anyone else, else "A visitor". The iOS walk of 2026-11-25 saw a private test
 * account as "A visitor" in its own list; Instagram's likers list says "You".
 */
fun likerLabel(r: Liker, me: String?): String =
    if (r.userId != null && me != null && r.userId.equals(me, ignoreCase = true)) "You" else r.name ?: "A visitor"

/** Kit/PhotoLikes.swift PhotoLikersSheet: who gave one, oldest first; a private profile is "A visitor". */
@Composable
fun PhotoLikersSheet(photoId: String, onDismiss: () -> Unit) {
    val marks = LocalTreeMarks.current
    val brand = Brand.colors
    val rows = remember { mutableStateListOf<Liker>() }
    var me by remember { mutableStateOf<String?>(null) }
    LaunchedEffect(Unit) { me = marks.myId() }
    LaunchedEffect(photoId) {
        val r = Supa.send("/rest/v1/rpc/photo_likers", token = marks.token(), body = JSONObject().put("photo", photoId).toString())
        if (r.ok) runCatching {
            val a = JSONArray(r.body)
            rows.clear()
            for (i in 0 until a.length()) {
                val o = a.getJSONObject(i)
                rows.add(Liker(o.optString("user_id").ifEmpty { null }.takeIf { !o.isNull("user_id") },
                    o.optString("display_name").takeIf { !o.isNull("display_name") },
                    o.optString("avatar_url").takeIf { !o.isNull("avatar_url") && it.isNotEmpty() }))
            }
        }
    }
    val n = maxOf(rows.size, PhotoLikes.state(photoId).count)
    BrandSheet(
        title = if (n == 1) "1 heart" else "$n hearts",
        onDismiss = onDismiss,
        buttons = emptyList(),
    ) {
        rows.forEach { p ->
            val name = likerLabel(p, me)
            Row(
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.spacedBy(12.dp),
                modifier = Modifier
                    .fillMaxWidth()
                    .heightIn(min = 56.dp)
                    .clickable(enabled = p.userId != null) { p.userId?.let { onDismiss(); marks.openPerson(it) } },
            ) {
                Box(
                    Modifier.size(40.dp).clip(CircleShape).background(brand.moss.copy(alpha = 0.12f)),
                    contentAlignment = Alignment.Center,
                ) {
                    if (p.avatar != null) RemoteImage(p.avatar, null, Modifier.fillMaxSize())
                    else Text((p.name ?: name).take(1).uppercase(), fontSize = 16.sp, fontWeight = FontWeight.Black, color = brand.moss)
                }
                Text(name, fontSize = 16.sp, fontWeight = if (p.userId == null) FontWeight.Normal else FontWeight.SemiBold,
                    color = if (p.userId == null) brand.inkSoft else brand.ink)
            }
        }
    }
}
