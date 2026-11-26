package app.ancienttrees.account

import app.ancienttrees.feed.Tree
import org.json.JSONArray
import org.json.JSONObject

/**
 * TRENDING THIS MONTH, Discover's numbered shelf (Hidde, 2026-11-26: "bouw
 * maar gewoon", after Polarsteps' Verkennen tab). The trees the most different
 * people photographed, hearted, voted Worth the visit or saved in the last 30
 * days, counted on the server (supabase/trending-trees.sql), ids only.
 * Nothing kept on the device. ios Kit/Trending.swift.
 */
object Trending {
    /** Three columns of three, Polarsteps' shelf. */
    const val COUNT = 9
    const val DAYS = 30

    suspend fun load(token: String?, tree: (String) -> Tree?): List<Tree> {
        val body = JSONObject().put("days", DAYS).put("n", COUNT * 2).toString()
        val r = Supa.send("/rest/v1/rpc/trending_trees", token = token, body = body)
        if (!r.ok) return emptyList()
        val ids = runCatching {
            val a = JSONArray(r.body)
            (0 until a.length()).mapNotNull { a.optJSONObject(it)?.optString("tree_id")?.takeIf(String::isNotEmpty) }
        }.getOrDefault(emptyList())
        return pick(ids, tree)
    }

    /** Trees this feed knows and can show with a photograph, in rank order. */
    fun pick(ids: List<String>, tree: (String) -> Tree?): List<Tree> =
        ids.mapNotNull(tree).filter { it.photo != null }.take(COUNT)
}
