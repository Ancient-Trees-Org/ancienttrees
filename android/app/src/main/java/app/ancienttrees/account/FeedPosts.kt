// THE FEED, FROM THE SERVER ONLY (Hidde, 2026-11-26), the Android twin of ios
// Kit/FeedPosts.swift, read from that source. Every post comes whole from
// public.feed() (supabase/feed.sql): name, place, pin and a picture in the public
// `feed` bucket, so the Feed tab never waits on a deploy. Nothing kept on the device.

package app.ancienttrees.account

import app.ancienttrees.feed.Geo
import app.ancienttrees.feed.Photo
import app.ancienttrees.feed.Precision
import app.ancienttrees.feed.Tree
import org.json.JSONArray
import org.json.JSONObject

object FeedPosts {
    data class Post(
        val key: String,
        val kind: String,
        /** Null on a post not checked yet: no tree of ours exists. */
        val treeId: String?,
        val treeName: String,
        val place: String,
        val url: String,
        val latitude: Double?,
        val longitude: Double?,
        val photoUrl: String?,
        val photoW: Int?,
        val photoH: Int?,
        val publishedAt: String,
        val authorName: String?,
        val authorAvatar: String?,
        /** Only to a signed-in caller, only for a public profile. */
        val authorId: String?,
        /**
         * LIVE FIRST, THEN CHECKED (supabase/feed-live.sql, 2026-11-26): false on a post a
         * reader shared that the judge has not looked at yet. The reader's own name, no place,
         * no position (hard rule 10), the share page as link, nothing to save or like. Missing
         * in an older answer means checked. FeedPosts.Post.checked in ios.
         */
        val checked: Boolean = true,
    ) {
        /** A tree somebody added, against a photograph on one of ours; only once checked. */
        val isNewTree: Boolean get() = kind == "tree" && checked

        /** The like on a visitor's photograph, keyed by its sightings uuid: a checked photo post and a reader's own new tree (Hidde, 2026-11-26); a tip ("tree:<id>") has none. */
        val likeId: String?
            get() = if (checked && UUID_RE.matches(key)) key.lowercase() else null

        /** The shared sighting behind an unchecked post (its key). */
        val sharedId: String? get() = if (!checked && UUID_RE.matches(key)) key.lowercase() else null
    }

    enum class Filter { EVERYONE, FOLLOWING, NEAR }

    /** Near you is a day out: within 100 km (FeedPosts.nearKm in ios). */
    const val NEAR_KM = 100.0
    const val PAGE_SIZE = 24

    private val UUID_RE = Regex("^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")

    private fun JSONObject.text(k: String): String? = if (isNull(k)) null else (opt(k) as? String)
    private fun JSONObject.num(k: String): Double? = if (isNull(k) || !has(k)) null else optDouble(k).takeIf { !it.isNaN() }

    fun parse(body: String): List<Post>? = runCatching {
        val a = JSONArray(body)
        (0 until a.length()).mapNotNull { i ->
            val o = a.optJSONObject(i) ?: return@mapNotNull null
            Post(
                key = o.text("key") ?: return@mapNotNull null,
                kind = o.text("kind") ?: "photo",
                treeId = o.text("tree_id"),
                treeName = o.text("tree_name").orEmpty(),
                place = o.text("place").orEmpty(),
                url = o.text("url").orEmpty(),
                latitude = o.num("latitude"),
                longitude = o.num("longitude"),
                photoUrl = o.text("photo_url"),
                photoW = o.num("photo_w")?.toInt(),
                photoH = o.num("photo_h")?.toInt(),
                publishedAt = o.text("published_at").orEmpty(),
                authorName = o.text("author_name"),
                authorAvatar = o.text("author_avatar"),
                authorId = o.text("author_id"),
                checked = if (o.has("checked") && !o.isNull("checked")) o.optBoolean("checked", true) else true,
            )
        }
    }.getOrNull()

    /** The posts after [after], newest first, by the server's keyset paging. Null when it did not answer. */
    suspend fun page(after: Post?, token: String?, n: Int = PAGE_SIZE): List<Post>? {
        val body = JSONObject().put("n", n)
        if (after != null) body.put("before_at", after.publishedAt).put("before_key", after.key)
        val r = Supa.send("/rest/v1/rpc/feed", token = token, body = body.toString())
        if (!r.ok) return null
        return parse(r.body)
    }

    /** Whose post this is, asked again signed in: the post before it is the cursor that returns exactly it. */
    suspend fun author(post: Post, prev: Post?, token: String?): String? =
        page(prev, token, n = 1)?.firstOrNull { it.key == post.key }?.authorId

    /**
     * The story's first sentence: cut at a full stop followed by a space and a capital or a
     * quote, never after a short abbreviation ("St.", "c."). FeedPosts.firstSentence in ios.
     */
    fun firstSentence(story: String): String {
        val s = story.trim()
        var i = 0
        while (i < s.length) {
            val c = s[i]
            if (c == '.' || c == '!' || c == '?') {
                var j = i + 1
                while (j < s.length && (s[j] == '"' || s[j] == '”' || s[j] == '’')) j++
                if (j >= s.length) return s
                if (s[j] == ' ' && j + 1 < s.length) {
                    val next = s[j + 1]
                    val prevWord = s.substring(0, i).split(' ').lastOrNull().orEmpty()
                    val abbreviation = (prevWord.length <= 2 && prevWord.firstOrNull()?.isUpperCase() == true) ||
                        prevWord in setOf("c", "ca", "St", "Mt", "Dr", "Mr", "Mrs", "approx")
                    if ((next.isUpperCase() || next == '"' || next == '“') && !abbreviation) return s.substring(0, j)
                }
            }
            i++
        }
        return s
    }

    fun passes(p: Post, f: Filter, following: Set<String>, origin: Pair<Double, Double>?): Boolean = when (f) {
        Filter.EVERYONE -> true
        Filter.FOLLOWING -> p.authorId?.lowercase()?.let { it in following } == true
        Filter.NEAR -> {
            val lat = p.latitude
            val lng = p.longitude
            origin != null && lat != null && lng != null && Geo.km(origin.first, origin.second, lat, lng) <= NEAR_KM
        }
    }

    /** A tree the server has and this phone's catalogue does not yet: its page from the post. */
    fun stub(p: Post): Tree {
        val slug = p.url.trim('/').substringBefore('/')
        val photo = p.photoUrl?.let {
            Photo(url = it, license = null, attribution = null, attributionShort = null, thumb = it, hero = it,
                creditRequired = false, creditLine = null, creditUrl = null, frame = null,
                width = p.photoW, height = p.photoH)
        }
        return Tree(
            id = p.treeId ?: "shared:${p.key}", name = p.treeName, species = "", age = null, ageShort = null,
            lat = p.latitude ?: 0.0, lng = p.longitude ?: 0.0, city = p.place, citySlug = slug, country = "",
            neighbourhood = "", access = "", paidEntry = false, transport = "", story = "", storyLatin = emptyList(),
            howToRecognise = "", url = p.url, precision = Precision.APPROXIMATE, photo = photo, saves = 0, mini = false,
        )
    }
}
