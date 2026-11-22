// NEW FROM VISITORS and the ambassador ask: the server calls Discover makes,
// the Android twin of ios Kit/NewFromVisitors.swift and the ambassador half of
// Kit/Submissions.swift. Nothing is kept on the device: the rows are read each
// time Discover opens, and whether you asked is read from your account.

package app.ancienttrees.account

import org.json.JSONArray
import org.json.JSONObject
import java.net.URLEncoder

object NewFromVisitors {
    /** One photograph a visitor sent that went live; the name and avatar only from a public profile. */
    data class Row(
        val sightingId: String,
        val treeId: String,
        val publishedAt: String,
        val authorName: String?,
        val authorAvatar: String?,
        /** Only to a signed-in caller (supabase/new-from-visitors.sql). */
        val authorId: String?,
    )

    /** The row shows from this many tiles, so it never stands half empty. */
    const val MINIMUM = 4

    private fun JSONObject.text(k: String): String? = if (isNull(k)) null else (opt(k) as? String)

    fun parse(body: String): List<Row> = runCatching {
        val a = JSONArray(body)
        val rows = (0 until a.length()).mapNotNull { i ->
            val o = a.optJSONObject(i) ?: return@mapNotNull null
            Row(
                sightingId = o.text("sighting_id") ?: return@mapNotNull null,
                treeId = o.text("tree_id") ?: return@mapNotNull null,
                publishedAt = o.text("published_at").orEmpty(),
                authorName = o.text("author_name"),
                authorAvatar = o.text("author_avatar"),
                authorId = o.text("author_id"),
            )
        }
        // Every row, in the server's order: tiles() picks one per tree from
        // what this feed can show (NewFromVisitors.load in ios).
        rows
    }.getOrDefault(emptyList())

    /**
     * The photograph this visitor sent, among the tree's own by the sightings row the feed
     * names (Photo.sighting), so the tile shows their picture and not the lead (Hidde,
     * 2026-11-15). Null until the feed carries it; the tile then shows the lead.
     * NewFromVisitors.shot in ios Kit/NewFromVisitors.swift.
     */
    fun shot(row: Row, tree: app.ancienttrees.feed.Tree): app.ancienttrees.feed.Photo? {
        val id = row.sightingId.lowercase()
        return tree.shots.firstOrNull { it.sighting == id }
    }

    /**
     * The tiles the row shows: only a tree whose feed already carries this visitor's
     * photograph, the website's rule (Hidde, 2026-11-16: the newest tiles stood empty until
     * the next deploy). NewFromVisitors.tiles in ios Kit/NewFromVisitors.swift.
     */
    fun tiles(rows: List<Row>, tree: (String) -> app.ancienttrees.feed.Tree?): List<Triple<Row, app.ancienttrees.feed.Tree, app.ancienttrees.feed.Photo>> {
        // One tile per tree, its newest photograph this feed carries, so an unknown newer one
        // never hides an older one that can show; twelve at most (2026-11-22).
        val seen = HashSet<String>()
        return rows.mapNotNull { r ->
            val t = tree(r.treeId) ?: return@mapNotNull null
            val s = shot(r, t) ?: return@mapNotNull null
            if (!seen.add(r.treeId)) return@mapNotNull null
            Triple(r, t, s)
        }.take(12)
    }

    /** Whether this feed can show the row's photograph (load's test). NewFromVisitors.known in ios. */
    fun known(row: Row, tree: (String) -> app.ancienttrees.feed.Tree?): Boolean =
        tree(row.treeId)?.let { shot(row, it) } != null

    /**
     * THE SEE ALL PAGE'S PAGES (Hidde, 2026-11-18): every photograph, not one per tree,
     * newest sent first, by the server's keyset paging (supabase/visitor-photos.sql), the
     * rows after [after]. Null when the server did not answer; the page stops there.
     * NewFromVisitors.page in ios Kit/NewFromVisitors.swift.
     */
    const val PAGE_SIZE = 24

    suspend fun page(after: Row?, token: String?, n: Int = PAGE_SIZE): List<Row>? {
        val body = JSONObject().put("n", n)
        if (after != null) body.put("before_at", after.publishedAt).put("before_id", after.sightingId.lowercase())
        val r = Supa.send("/rest/v1/rpc/visitor_photos", token = token, body = body.toString())
        if (!r.ok) return null
        return runCatching {
            val a = JSONArray(r.body)
            (0 until a.length()).mapNotNull { i ->
                val o = a.optJSONObject(i) ?: return@mapNotNull null
                Row(
                    sightingId = o.text("sighting_id") ?: return@mapNotNull null,
                    treeId = o.text("tree_id") ?: return@mapNotNull null,
                    publishedAt = o.text("published_at").orEmpty(),
                    authorName = o.text("author_name"),
                    authorAvatar = o.text("author_avatar"),
                    authorId = o.text("author_id"),
                )
            }
        }.getOrNull()
    }

    /** Whose photograph this is, asked again signed in: the row before it is the cursor that returns exactly it. */
    suspend fun author(row: Row, prev: Row?, token: String?): String? =
        page(prev, token, n = 1)?.firstOrNull { it.sightingId == row.sightingId }?.authorId

    /**
     * THE ROW NEVER WAITS ON A FRESH FEED (2026-11-22, Hidde: "the feed should always stay
     * available"). The newest 24 first; when fewer than [MINIMUM] trees of them are in this
     * feed ([known]), older photographs from the See all pages fill the row, four pages back
     * at most. Every row is kept (once), so a feed that arrives later shows the newer ones.
     * NewFromVisitors.load in ios Kit/NewFromVisitors.swift.
     */
    suspend fun load(token: String?, known: (Row) -> Boolean): List<Row> {
        val r = Supa.send("/rest/v1/rpc/new_from_visitors", token = token, body = JSONObject().put("n", 24).toString())
        val rows = (if (r.ok) parse(r.body) else emptyList()).toMutableList()
        fun knownTrees() = rows.filter(known).map { it.treeId }.toSet().size
        if (knownTrees() < MINIMUM) {
            var cursor: Row? = null
            for (i in 0 until 4) {
                val list = page(cursor, token, n = 48) ?: break
                rows += list
                if (knownTrees() >= MINIMUM * 2 || list.size < 48) break
                cursor = list.last()
            }
        }
        return rows.distinctBy { it.sightingId }
    }
}

object AmbassadorAsk {
    private const val PATH = "/rest/v1/submissions"

    suspend fun request(city: String, token: String): Boolean {
        val body = JSONObject()
            .put("kind", "ambassador")
            .put("city", city)
            .put("tree", "")
            .put("why", "ambassador request")
            .put("page", "app")
        return Supa.send(PATH, token = token, body = body.toString(), prefer = "return=minimal").ok
    }

    /** Whether this account already asked for this city, read from the account, never remembered here. */
    suspend fun asked(city: String, token: String?): Boolean {
        if (token == null) return false
        val q = URLEncoder.encode(city, "UTF-8").replace("+", "%20")
        return Supa.rows("$PATH?select=id&kind=eq.ambassador&city=eq.$q&limit=1", token).isNotEmpty()
    }
}
