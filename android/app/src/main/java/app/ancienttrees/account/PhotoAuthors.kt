// Kit/PhotoAuthors.swift: who sent each reader's photograph on a tree, a public
// profile only (rpc photo_authors). Signed out the server names no account id.

package app.ancienttrees.account

import org.json.JSONArray
import org.json.JSONObject

object PhotoAuthors {
    data class Row(val photoId: String, val authorName: String?, val authorAvatar: String?, val authorId: String?)

    suspend fun load(ids: List<String>, token: String?): Map<String, Row> {
        val wanted = ids.toSet().sorted()
        if (wanted.isEmpty()) return emptyMap()
        val r = Supa.send("/rest/v1/rpc/photo_authors", token = token, body = JSONObject().put("ids", JSONArray(wanted)).toString())
        if (!r.ok) return emptyMap()
        return runCatching {
            val a = JSONArray(r.body)
            (0 until a.length()).mapNotNull { i ->
                val o = a.getJSONObject(i)
                fun s(k: String) = o.optString(k).takeIf { it.isNotEmpty() && it != "null" }
                val name = s("author_name") ?: return@mapNotNull null
                Row(o.getString("photo_id"), name, s("author_avatar"), s("author_id"))
            }.associateBy { it.photoId }
        }.getOrDefault(emptyMap())
    }
}
