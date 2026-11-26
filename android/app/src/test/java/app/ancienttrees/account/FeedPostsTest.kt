package app.ancienttrees.account

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

/** The Feed's posts from feed(), checked and not yet checked (supabase/feed-live.sql). FeedPostsTests in ios. */
class FeedPostsTest {
    private val page = """
    [
     {"key":"a4d1c500-1664-48c1-bc8e-7d9d6ee2ad3f","kind":"photo","tree_id":"bhm_001",
      "tree_name":"The Preston Twin","place":"Brighton","url":"/brighton/preston-twin",
      "latitude":50.84,"longitude":-0.15,"photo_url":"https://x/feed/a.jpg","photo_w":800,"photo_h":1067,
      "published_at":"2026-11-26T09:19:14Z","author_name":"Milo S.","author_avatar":null,
      "author_id":null,"checked":true},
     {"key":"af38a0d5-0114-4c0e-8b25-336a957b89a8","kind":"tree","tree_id":null,
      "tree_name":"American Sycamore","place":"","url":"/t/?id=af38a0d5-0114-4c0e-8b25-336a957b89a8",
      "latitude":null,"longitude":null,"photo_url":"https://x/shared-sightings/b.jpg","photo_w":null,"photo_h":null,
      "published_at":"2026-11-25T15:06:55Z","author_name":"Leafy Linden 4134","author_avatar":null,
      "author_id":null,"checked":false},
     {"key":"tree:ulv_002","kind":"tree","tree_id":"ulv_002","tree_name":"Fir","place":"Ulverston",
      "url":"/ulverston/fir","latitude":54.17,"longitude":-3.07,"photo_url":"https://x/feed/c.jpg",
      "photo_w":800,"photo_h":1419,"published_at":"2026-11-26T08:46:00Z","author_name":null,
      "author_avatar":null,"author_id":null}
    ]
    """

    @Test fun anUncheckedPostNeverDropsFromThePage() {
        assertEquals(3, FeedPosts.parse(page)!!.size)
    }

    @Test fun aCheckedPhotoKeepsItsHeart() {
        val p = FeedPosts.parse(page)!![0]
        assertTrue(p.checked)
        assertEquals("a4d1c500-1664-48c1-bc8e-7d9d6ee2ad3f", p.likeId)
        assertNull(p.sharedId)
    }

    @Test fun anUncheckedPostHasNoPlaceNoHeartAndOpensTheSharePage() {
        val p = FeedPosts.parse(page)!![1]
        assertFalse(p.checked)
        assertNull(p.treeId)
        assertFalse(p.isNewTree)
        assertNull(p.likeId)
        assertEquals("af38a0d5-0114-4c0e-8b25-336a957b89a8", p.sharedId)
        assertFalse(FeedPosts.passes(p, FeedPosts.Filter.NEAR, emptySet(), 52.0 to 5.0))
    }

    @Test fun anOlderAnswerWithoutTheColumnIsChecked() {
        val p = FeedPosts.parse(page)!![2]
        assertTrue(p.checked)
        assertTrue(p.isNewTree)
        assertNull(p.likeId)
    }

    /** Andrea's Varese trees, 2026-11-26: a reader's own new tree, checked, carries a heart. */
    @Test fun aReadersOwnNewTreeCarriesAHeart() {
        val one = """
        [{"key":"5B0E2C1A-7D7E-4F7A-9C1E-2D3B4A5C6D7E","kind":"tree","tree_id":"vrs_009",
          "tree_name":"The Picnic-Table Cedars","place":"Varese","url":"/varese/picnic-table-cedars",
          "latitude":45.8,"longitude":8.8,"photo_url":"https://x/feed/d.jpg","photo_w":800,"photo_h":600,
          "published_at":"2026-11-26T08:00:00Z","author_name":"Andrea C.","author_avatar":null,
          "author_id":null,"checked":true}]
        """
        val p = FeedPosts.parse(one)!![0]
        assertTrue(p.isNewTree)
        assertEquals("5b0e2c1a-7d7e-4f7a-9c1e-2d3b4a5c6d7e", p.likeId)
    }
}
