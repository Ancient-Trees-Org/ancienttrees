// A FEED TILE OPENS ITS TREE (2026-11-27): ButtonWalk read every control on the
// Feed as dead while a finger on the same build opened the tree. The photo likes
// on a double tap, so its single tap fires after the 300 ms wait for a second one,
// and under the test clock that wait only moves when the clock is moved: a click,
// then the clock past the window, then the tree page. The title, a plain click,
// opens it straight away. Frames go to /data/local/tmp/walk/.

package app.ancienttrees

import android.content.Intent
import androidx.compose.ui.test.ExperimentalTestApi
import androidx.compose.ui.test.click
import androidx.compose.ui.test.hasTestTag
import androidx.compose.ui.test.isRoot
import androidx.compose.ui.test.junit4.createEmptyComposeRule
import androidx.compose.ui.test.onAllNodesWithTag
import androidx.compose.ui.test.onFirst
import androidx.compose.ui.test.performClick
import androidx.compose.ui.test.performTouchInput
import androidx.test.core.app.ActivityScenario
import androidx.test.core.app.ApplicationProvider
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import org.junit.After
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@OptIn(ExperimentalTestApi::class)
@RunWith(AndroidJUnit4::class)
class FeedTileWalk {
    @get:Rule val rule = createEmptyComposeRule()
    private var scenario: ActivityScenario<MainActivity>? = null

    @After fun close() { scenario?.close() }

    private fun start(extra: List<String>) {
        val intent = Intent(ApplicationProvider.getApplicationContext(), MainActivity::class.java)
            .putExtra("args", (listOf("-at=52.3731,4.8922", "-AppleLocale=en_NL", "-no-location-ask", "-no-cover", "-no-review-prompt", "-tab=4") + extra).toTypedArray())
        scenario = ActivityScenario.launch(intent)
        rule.waitUntil(60_000) { rule.onAllNodesWithTag("feed-tile").fetchSemanticsNodes().isNotEmpty() }
        rule.waitForIdle()
    }

    private fun shoot(name: String) {
        val ui = InstrumentationRegistry.getInstrumentation().uiAutomation
        ui.executeShellCommand("mkdir -p /data/local/tmp/walk").close()
        ui.executeShellCommand("screencap -p /data/local/tmp/walk/feedtile-$name.png").close()
        Thread.sleep(500)
    }

    private fun opened(): Boolean {
        val end = System.currentTimeMillis() + 8_000
        while (System.currentTimeMillis() < end) {
            rule.waitForIdle()
            if (rule.onAllNodes(hasTestTag("tree-page")).fetchSemanticsNodes().isNotEmpty()) return true
            Thread.sleep(250)
        }
        return false
    }

    @Test fun aClickOnATileOpensItsTree() {
        start(emptyList())
        shoot("click-before")
        rule.onAllNodesWithTag("feed-tile").onFirst().performClick()
        rule.mainClock.advanceTimeBy(500)
        val ok = opened()
        shoot("click-after")
        org.junit.Assert.assertTrue("a click on the first Feed tile opened no tree page", ok)
    }

    @Test fun aClickOnATitleOpensItsTree() {
        start(emptyList())
        val tile = rule.onAllNodesWithTag("feed-tile").onFirst().fetchSemanticsNode()
        var name = ""
        InstrumentationRegistry.getInstrumentation().runOnMainSync {
            name = tile.config[androidx.compose.ui.semantics.SemanticsProperties.ContentDescription].first().substringBefore(", ")
        }
        rule.onAllNodes(androidx.compose.ui.test.hasText(name)).onFirst().performClick()
        val ok = opened()
        shoot("title-after")
        org.junit.Assert.assertTrue("a click on the first Feed title ($name) opened no tree page", ok)
    }

    @Test fun aFingerOnATileOpensItsTree() {
        start(emptyList())
        shoot("finger-before")
        val tile = rule.onAllNodesWithTag("feed-tile").onFirst().fetchSemanticsNode()
        val root = rule.onAllNodes(isRoot()).onFirst()
        val rootBox = root.fetchSemanticsNode()
        var at = androidx.compose.ui.geometry.Offset.Zero
        InstrumentationRegistry.getInstrumentation().runOnMainSync {
            at = tile.boundsInWindow.center - rootBox.boundsInWindow.topLeft
        }
        root.performTouchInput { click(at) }
        rule.mainClock.advanceTimeBy(500)
        val ok = opened()
        shoot("finger-after")
        org.junit.Assert.assertTrue("a finger on the first Feed tile opened no tree page", ok)
    }
}
