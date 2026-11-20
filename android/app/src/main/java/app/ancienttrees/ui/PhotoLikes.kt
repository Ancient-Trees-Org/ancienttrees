// Kit/PhotoLikes.swift: the heart on a visitor's photograph (Hidde, 2026-11-20:
// "Ja, bouw het hartje"). One store for the app, counts asked in one call for
// every heart that appeared within a moment of each other, a write the server
// refuses puts the heart back, nothing kept on the device (hard rule 11).
// supabase/photo-likes.sql: the count is public, who gave it is not.

package app.ancienttrees.ui

import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.widthIn
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
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

    /** Give or take back, shown at once; refused, it goes back. */
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

/** PhotoHeart (Kit/PhotoLikes.swift): outlined, filled moss once given, the count from one; signed out it asks for a sign-in. */
@Composable
fun PhotoHeart(photoId: String, onDark: Boolean = false) {
    val marks = LocalTreeMarks.current
    val brand = Brand.colors
    val scope = rememberCoroutineScope()
    val s = PhotoLikes.state(photoId)
    LaunchedEffect(photoId, marks.signedIn) { PhotoLikes.want(photoId, marks.token()) }
    val tint = when {
        s.mine -> if (onDark) Color.White else brand.moss
        else -> if (onDark) Color.White.copy(alpha = 0.85f) else brand.inkSoft
    }
    Row(
        horizontalArrangement = Arrangement.spacedBy(3.dp, Alignment.End),
        verticalAlignment = Alignment.CenterVertically,
        modifier = Modifier
            .widthIn(min = 44.dp)
            .heightIn(min = 44.dp)
            .clickable(interactionSource = remember { MutableInteractionSource() }, indication = null, role = Role.Button) {
                if (marks.signedIn) {
                    scope.launch { marks.token()?.let { PhotoLikes.toggle(photoId, it) } }
                } else {
                    marks.signIn()
                }
            }
            .semantics { contentDescription = "photo-like" },
    ) {
        Icon(if (s.mine) Sym.HeartFill else Sym.Heart, null, tint = tint, modifier = Modifier.size(15.dp))
        if (s.count > 0) Text("${s.count}", fontSize = 12.sp, fontWeight = FontWeight.SemiBold, color = tint)
    }
}
