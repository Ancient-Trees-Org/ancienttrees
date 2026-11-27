// EVERY BUTTON ANSWERS A FINGER: the Android twin of ios AncientTreesUITests/
// ButtonWalk.swift (2026-11-08; review 2026-11-11: Android had none).
//
// Opens each of the iPhone's 14 screens, signed out and signed in, finds every
// control a finger can reach on it (scrolling down a few times), and for each
// one: launches the screen fresh, waits for it to stand still, taps the
// control's centre as a finger does, and asserts that SOMETHING CHANGED: a new
// screen, a sheet, a different label, a snackbar, or the app handing over to
// the browser, a maps app or the share sheet. A control after which the screen
// reads exactly as before is a dead button, and every dead button on a screen
// is named in one failure.
//
// What is compared is the semantics tree's text, tags, states and bounds,
// rounded, once the screen has stood still (two equal readings a second
// apart), so a sheet that lowers counts as an answer and a map still drawing
// (MapLibre is not in the tree) does not. A control that rightly changes
// nothing goes in `quiet` with its reason; one that would do harm with the
// stand-in session (delete, sign out, block) is never tapped (`neverTap`).
//
// Slow (a fresh launch per control), so android.yml runs it in its own job,
// daily and on dispatch, as buttonwalk.yml does for the iPhone. A new screen
// joins `screens` here, as it joins the iPhone's list.
//
//   python3 scripts/android_walk.py --only ButtonWalk

package app.ancienttrees

import android.content.Intent
import androidx.compose.ui.geometry.Rect
import androidx.compose.ui.semantics.SemanticsActions
import androidx.compose.ui.semantics.SemanticsNode
import androidx.compose.ui.semantics.SemanticsProperties
import androidx.compose.ui.semantics.getOrNull
import androidx.compose.ui.test.ExperimentalTestApi
import androidx.compose.ui.test.SemanticsMatcher
import androidx.compose.ui.test.click
import androidx.compose.ui.test.isRoot
import androidx.compose.ui.test.junit4.createEmptyComposeRule
import androidx.compose.ui.test.onFirst
import androidx.compose.ui.test.performTouchInput
import androidx.compose.ui.test.swipeUp
import androidx.test.core.app.ActivityScenario
import androidx.test.core.app.ApplicationProvider
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import androidx.test.runner.lifecycle.ActivityLifecycleMonitorRegistry
import androidx.test.runner.lifecycle.Stage
import org.junit.After
import org.junit.Assert.assertTrue
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@OptIn(ExperimentalTestApi::class)
@RunWith(AndroidJUnit4::class)
class ButtonWalk {
    @get:Rule val rule = createEmptyComposeRule()
    private var scenario: ActivityScenario<MainActivity>? = null

    @After fun close() { watchdog?.interrupt(); scenario?.close() }

    // A STEP THAT STANDS STILL IS NAMED, NEVER WAITED ON (2026-11-26: a local run
    // sat at 0 of 29 for two and a half hours on the launch screen, where CI's
    // walk takes 26 minutes). Every launch, tap and reading beats; when nothing
    // beats for STALL_MS the watchdog logs every thread's stack under the tag
    // ButtonWalkStall and interrupts the test thread, so the screen's step throws,
    // walkAll records it as a problem with the screen's name, and the walk goes on.
    @Volatile private var beat = System.currentTimeMillis()
    @Volatile private var step = "start"
    private var watchdog: Thread? = null

    private fun beat(what: String) { step = what; beat = System.currentTimeMillis() }

    private fun startWatchdog() {
        val test = Thread.currentThread()
        watchdog = Thread {
            try {
                while (true) {
                    Thread.sleep(5_000)
                    if (System.currentTimeMillis() - beat > STALL_MS) {
                        val dump = StringBuilder("stalled ${STALL_MS / 1000}s at: $step\n")
                        for ((t, st) in Thread.getAllStackTraces()) {
                            dump.append("\"").append(t.name).append("\" ").append(t.state).append('\n')
                            for (f in st.take(30)) dump.append("    at ").append(f).append('\n')
                        }
                        dump.lines().chunked(40).forEach { android.util.Log.e("ButtonWalkStall", it.joinToString("\n")) }
                        stalls.add(step)
                        beat = System.currentTimeMillis()
                        test.interrupt()
                    }
                }
            } catch (_: InterruptedException) {}
        }.apply { isDaemon = true; name = "ButtonWalk watchdog"; start() }
    }

    private val stalls = java.util.Collections.synchronizedList(ArrayList<String>())

    companion object {
        private val base = listOf("-AppleLocale=en_NL", "-no-location-ask", "-reset-collection", "-reset-blocks", "-no-cover", "-no-review-prompt")
        private const val ORIGIN = "-at=52.3731,4.8922"
        /**
         * No beat for this long is a hang. Every reading of the screen beats, and a
         * reading needs the app's main thread, so a main thread stuck this long is
         * caught with its stack before Android's own 60 s ANR ends the run unexplained.
         */
        private const val STALL_MS = 30_000L

        /** name, launch arguments: ButtonWalk.swift's screens, each walked signed out and signed in. */
        val screens = listOf(
            "map" to listOf("-tab=0"),
            "map-full" to listOf("-tab=0", "-sheet=full"),
            "map-bar" to listOf("-tab=0", "-sheet=bar"),
            "map-pin" to listOf("-tab=0", "-select=ath_004"),
            "discover" to listOf("-tab=1"),
            "discover-cadiz" to listOf("-tab=1", "-at=36.5297,-6.2925"),
            "my-trees" to listOf("-tab=2"),
            // The Feed tab (ButtonWalk.swift "feed", missing here until 2026-11-26).
            "feed" to listOf("-tab=4"),
            "profile" to listOf("-tab=2", "-settings"),
            "tree" to listOf("-tab=0", "-open=tree:ath_004"),
            "tree-nophoto" to listOf("-tab=0", "-open=tree:vln_010"),
            "city" to listOf("-tab=0", "-open=city:cadiz"),
            "city-full" to listOf("-tab=0", "-open=city:cadiz", "-sheet=full"),
            "species" to listOf("-tab=0", "-open=species:Aleppo Pine"),
            "collection" to listOf("-tab=0", "-open=collection:ancient-oaks-of-europe"),
            // Every photograph visitors sent, Discover's See all (2026-11-18).
            "visitors" to listOf("-tab=1", "-open=visitors:all"),
        )

        /** Words that mean a machine must not tap it, even with the stand-in session. */
        val neverTap = listOf("delete", "sign out", "signout", "log out", "logout", "block", "remove", "unfollow")

        /** "<screen>|<tag or label>": controls that rightly change nothing this walk can read, with why. */
        val quiet = mapOf(
            "map|tab-map" to "already on the map tab",
            "map-full|tab-map" to "already on the map tab",
            "map-pin|tab-map" to "already on the map tab",
            "map-bar|tab-map" to "already on the map tab",
            "city|tab-map" to "already on the map tab",
            "city-full|tab-map" to "already on the map tab",
            "discover|tab-discover" to "already on Discover, at the top",
            "discover-cadiz|tab-discover" to "already on Discover, at the top",
            "my-trees|tab-my-trees" to "already on My trees",
            "feed|tab-feed" to "already on the Feed, at the top",
            "feed|feed-filter-everyone" to "Everyone is the filter already on",
            "feed|Everyone" to "Everyone is the filter already on (the tag sits on the chip's box)",
            "feed|feed-layout-grid" to "the grid is the layout already on",
            "map|map-recentre" to "the camera already stands on the test's location",
            "map-bar|map-recentre" to "the camera already stands on the test's location",
            "my-trees|map-recentre" to "the camera already stands on the test's location",
            "my-trees|Collected" to "already on Collected, the lane My trees opens on",
        )
    }

    private fun launch(args: List<String>) {
        beat("launch ${args.joinToString(" ")}")
        scenario?.close()
        // THE OLD SCREEN GONE BEFORE THE NEXT (2026-11-27): launched straight after a
        // close, Android's window manager on API 37 sometimes never gave the new screen
        // its focus ("Duplicate finish request"), the app's main thread idle the whole
        // time, and the launch waited for ever. Wait until no MainActivity is alive.
        val gone = System.currentTimeMillis() + 10_000
        while (System.currentTimeMillis() < gone) {
            var alive = false
            InstrumentationRegistry.getInstrumentation().runOnMainSync {
                val m = ActivityLifecycleMonitorRegistry.getInstance()
                alive = listOf(Stage.PRE_ON_CREATE, Stage.CREATED, Stage.STARTED, Stage.RESUMED, Stage.PAUSED, Stage.STOPPED)
                    .any { st -> m.getActivitiesInStage(st).any { it is MainActivity } }
            }
            if (!alive) break
            Thread.sleep(100)
        }
        Thread.sleep(300)
        val at = if (args.any { it.startsWith("-at=") }) emptyList() else listOf(ORIGIN)
        val intent = Intent(ApplicationProvider.getApplicationContext(), MainActivity::class.java)
            .putExtra("args", (base + at + args).toTypedArray())
        scenario = ActivityScenario.launch(intent)
        // The catalogue is read before anything stands; a tab bar or a page means it has.
        rule.waitUntil(45_000) { buttons().isNotEmpty() }
    }

    /** Our activity is no longer in front: a browser tab, a maps app or the share sheet took over. */
    private fun leftTheApp(): Boolean {
        var resumed = false
        InstrumentationRegistry.getInstrumentation().runOnMainSync {
            resumed = ActivityLifecycleMonitorRegistry.getInstance().getActivitiesInStage(Stage.RESUMED)
                .any { it is MainActivity }
        }
        return !resumed
    }

    private fun locationAllowed(): Boolean {
        val c = InstrumentationRegistry.getInstrumentation().targetContext
        return c.checkSelfPermission(android.Manifest.permission.ACCESS_FINE_LOCATION) == android.content.pm.PackageManager.PERMISSION_GRANTED ||
            c.checkSelfPermission(android.Manifest.permission.ACCESS_COARSE_LOCATION) == android.content.pm.PackageManager.PERMISSION_GRANTED
    }

    /**
     * READ THE TREE ON THE APP'S OWN THREAD (2026-11-27). A SemanticsNode's config,
     * bounds and children are read from the live layout; read from the test thread
     * while the app laid out the same tree, they threw "performMeasureAndLayout called
     * during measure layout" and a ConcurrentModificationException in the Feed, and
     * could leave the app's main thread stuck. Fetch as before, read here.
     */
    private fun <T> onMain(block: () -> T): T {
        var out: Result<T>? = null
        InstrumentationRegistry.getInstrumentation().runOnMainSync { out = runCatching(block) }
        return out!!.getOrThrow()
    }

    private fun roots(): List<SemanticsNode> =
        runCatching { rule.onAllNodes(isRoot(), useUnmergedTree = true).fetchSemanticsNodes() }.getOrDefault(emptyList())

    /** The screen as text: every node's tag, words, state and bounds (rounded to 4 px). */
    private fun signature(): String {
        if (leftTheApp()) return "<left the app>"
        val sb = StringBuilder()
        fun walk(n: SemanticsNode, depth: Int) {
            val c = n.config
            val b = n.boundsInRoot
            sb.append(depth).append(' ')
                .append(c.getOrNull(SemanticsProperties.TestTag) ?: "").append('|')
                .append(c.getOrNull(SemanticsProperties.Text)?.joinToString { it.text } ?: "").append('|')
                .append(c.getOrNull(SemanticsProperties.ContentDescription)?.joinToString() ?: "").append('|')
                .append(c.getOrNull(SemanticsProperties.EditableText)?.text ?: "").append('|')
                .append(c.getOrNull(SemanticsProperties.Selected) ?: "").append('|')
                .append(c.getOrNull(SemanticsProperties.ToggleableState) ?: "").append('|')
                .append((b.left / 4).toInt()).append(',').append((b.top / 4).toInt()).append(',')
                .append((b.right / 4).toInt()).append(',').append((b.bottom / 4).toInt()).append('\n')
            for (k in n.children) walk(k, depth + 1)
        }
        val rs = roots()
        onMain { for (r in rs) walk(r, 0) }
        return sb.toString()
    }

    /** Until two readings a second apart agree, at most eight seconds. */
    private fun settled(): String {
        beat("$step, settling")
        rule.waitForIdle()
        var last = signature()
        repeat(8) {
            Thread.sleep(1000)
            rule.waitForIdle()
            val now = signature()
            beat = System.currentTimeMillis()
            if (now == last) return now
            last = now
        }
        return last
    }

    data class Target(val tag: String, val label: String) {
        val key get() = tag.ifEmpty { label }
    }

    private fun target(n: SemanticsNode): Target {
        val c = n.config
        val tag = c.getOrNull(SemanticsProperties.TestTag).orEmpty()
        val label = c.getOrNull(SemanticsProperties.ContentDescription)?.firstOrNull()
            ?: c.getOrNull(SemanticsProperties.Text)?.joinToString(" ") { it.text }
            ?: n.children.firstNotNullOfOrNull { k -> k.config.getOrNull(SemanticsProperties.Text)?.joinToString(" ") { it.text } }
            ?: ""
        return Target(tag, label)
    }

    /** Every enabled control in the merged tree, with where it stands. */
    private fun buttons(): List<Pair<Target, Rect>> =
        runCatching {
            beat = System.currentTimeMillis()
            rule.onAllNodes(SemanticsMatcher.keyIsDefined(SemanticsActions.OnClick)).fetchSemanticsNodes()
        }.getOrDefault(emptyList()).let { nodes ->
            runCatching {
                onMain {
                    nodes.filter { SemanticsProperties.Disabled !in it.config && it.boundsInRoot.width > 0f }
                        .map { target(it) to it.boundsInWindow }
                }
            }.getOrDefault(emptyList())
        }

    private fun screen(): Rect {
        val m = InstrumentationRegistry.getInstrumentation().targetContext.resources.displayMetrics
        return Rect(0f, 0f, m.widthPixels.toFloat(), m.heightPixels.toFloat())
    }

    private fun onScreen(r: Rect) = screen().deflate(1f).contains(r.center)

    private fun spot(t: Target): Rect? = buttons().firstOrNull { it.first == t && onScreen(it.second) }?.second

    private fun swipeUp() {
        runCatching { rule.onAllNodes(isRoot()).onFirst().performTouchInput { swipeUp() } }
        rule.waitForIdle()
    }

    /** A finger on that point of the window: whatever lies on top of the control gets it, as on a phone. */
    private fun tapAt(r: Rect) {
        val root = rule.onAllNodes(isRoot()).onFirst()
        val node = root.fetchSemanticsNode()
        val rootBounds = onMain { node.boundsInWindow }
        root.performTouchInput { click(r.center - rootBounds.topLeft) }
    }

    /** Every control whose centre is on screen, scrolling down a few times. */
    private fun targets(): List<Target> {
        val seen = LinkedHashSet<Target>()
        for (pass in 0 until 4) {
            for ((t, r) in buttons()) if (onScreen(r) && (t.tag.isNotEmpty() || t.label.isNotEmpty())) seen.add(t)
            if (pass < 3) swipeUp()
        }
        return seen.toList()
    }

    private fun walk(name: String, screen: String, args: List<String>, problems: MutableList<String>) {
        launch(args)
        settled()
        val list = targets().filter { t ->
            val k = (t.tag + " " + t.label).lowercase()
            neverTap.none { it in k } && quiet["$screen|${t.key}"] == null &&
                // WITH LOCATION ALLOWED the arrow only moves MapLibre's camera, which is
                // not in the tree this walk reads (the iPhone's pins are); without it
                // (CI's emulators) the arrow asks, and that is walked. 2026-11-27.
                !(t.key == "map-recentre" && locationAllowed())
        }
        if (list.isEmpty()) { problems.add("$name: no buttons found at all; did the screen open?"); return }
        val dead = ArrayList<String>()
        val unreachable = ArrayList<String>()
        for (t in list) {
            launch(args)
            // Reach it first (scrolling is not the answer looked for), read, then tap.
            var tries = 0
            while (spot(t) == null && tries < 5) { swipeUp(); tries++ }
            if (spot(t) == null) { unreachable.add(t.key); continue }
            val before = settled()
            val at = spot(t) ?: run { unreachable.add(t.key); null } ?: continue
            beat("$name: tap ${t.key}")
            tapAt(at)
            if (settled() == before) dead.add(t.key)
        }
        if (dead.isNotEmpty()) problems.add("$name: ${dead.size} button(s) changed nothing when tapped: ${dead.joinToString()}")
        // Found once and then not again is a flaky screen, not a dead button: said, not failed.
        if (unreachable.isNotEmpty()) println("ButtonWalk $name: could not reach again: ${unreachable.joinToString()}")
    }

    private fun walkAll(signedIn: Boolean) {
        val problems = ArrayList<String>()
        startWatchdog()
        // -e screens map,tree: only those (python3 scripts/android_walk.py --only ButtonWalk --screens map,tree).
        val only = InstrumentationRegistry.getArguments().getString("screens")?.split(",")?.filter { it.isNotBlank() }
        for ((name, args) in screens.filter { only.isNullOrEmpty() || it.first in only }) {
            val label = name + if (signedIn) " (signed in)" else " (signed out)"
            runCatching { walk(label, name, if (signedIn) args + "-signed-in" else args, problems) }
                .onFailure { e ->
                    // The root cause too (2026-11-27: a coroutine failure was cut before its cause).
                    var root: Throwable = e
                    while (root.cause != null && root.cause !== root) root = root.cause!!
                    android.util.Log.e("ButtonWalk", "$label failed", e)
                    problems.add("$label: ${e.message?.take(200)}" + if (root !== e) " | cause: ${root.javaClass.name}: ${root.message?.take(200)} at ${root.stackTrace.take(4).joinToString(" < ")}" else "")
                }
            Thread.interrupted() // a stall's interrupt belongs to the screen it stopped
        }
        if (stalls.isNotEmpty()) problems.add("stood still ${STALL_MS / 1000}s (stacks in logcat, tag ButtonWalkStall): ${stalls.joinToString()}")
        assertTrue(problems.joinToString("\n"), problems.isEmpty())
    }

    @Test fun everyButtonAnswersSignedOut() = walkAll(signedIn = false)

    @Test fun everyButtonAnswersSignedIn() = walkAll(signedIn = true)
}
