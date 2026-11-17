// The bottom bar. On the iPhone (ios Screens/TabBar.swift) three places float in a
// grey capsule with the camera on its own disc beside it: Apple's iOS 26 tab bar.
//
// ANDROID TAKES ANDROID'S BAR (Hidde, 2026-11-17: "dat voelt als iOS specifiek",
// then "volg maar gewoon polarsteps en alltrails"). The tab bar is the platform's
// own control on both phones, so by Airbnb's line it takes each platform's form:
// docked to the bottom edge across the full width, 56 above the system bar, a word
// under every icon, the chosen place in the brand colour with a filled glyph and no
// pill behind it. Measured on his Galaxy S21 Ultra the same day: AllTrails and
// Polarsteps both draw exactly this, 56 high, white, five labelled items
// (CONVENTIONS.md "A tab bar on Android"). The places, glyphs, order and the camera
// stay the iPhone's; the camera is the fourth item with its word under it, because
// on a docked Android bar every item carries one.
//
// Glyphs are Material Symbols, the Android counterpart of SF Symbols. We never draw icons.

package app.ancienttrees.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.RowScope
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.navigationBars
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.windowInsetsBottomHeight
import androidx.compose.material3.Icon
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.semantics.selected
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import app.ancienttrees.R

object TabBar {
    /** The bar's height above the system bar: AllTrails' and Polarsteps' 56 on Android. */
    val HEIGHT = 56.dp

    /**
     * How deep the bar stands over what lies behind it, above the safe area: lists
     * and sheets keep this much room at their foot.
     */
    val floatDepth: Dp
        @Composable get() = HEIGHT

    /** The collect deed's tag: not a tab, intercepted, as on the iPhone. */
    const val COLLECT = 3
}

private data class TabItem(val title: Int, val outline: ImageVector, val filled: ImageVector)

/** The iPhone's accessibility identifiers, so the walk names the same controls. */
private val TAB_TAGS = listOf("tab-map", "tab-discover", "tab-my-trees")

private val ITEMS = listOf(
    TabItem(R.string.tab_map, Sym.Map, Sym.MapFill),
    TabItem(R.string.tab_discover, Sym.Search, Sym.Search),
    TabItem(R.string.tab_my_trees, Sym.Leaf, Sym.LeafFill),
)

@Composable
fun TabBar(selected: Int, select: (Int) -> Unit, collect: () -> Unit, modifier: Modifier = Modifier) {
    val brand = Brand.colors
    Column(modifier.fillMaxWidth().background(brand.ground)) {
        Row(Modifier.fillMaxWidth().height(TabBar.HEIGHT), verticalAlignment = Alignment.CenterVertically) {
            ITEMS.forEachIndexed { i, item ->
                val on = i == selected
                BarItem(
                    title = stringResource(item.title),
                    glyph = if (on) item.filled else item.outline,
                    on = on,
                    role = Role.Tab,
                    modifier = Modifier.semantics { this.selected = on }.testTag(TAB_TAGS[i]),
                ) { select(i) }
            }
            BarItem(
                title = stringResource(R.string.tab_collect),
                glyph = Sym.PhotoCamera,
                on = false,
                role = Role.Button,
                modifier = Modifier.testTag("tab-collect"),
                onClick = collect,
            )
        }
        // The bar's ground runs on behind the system's buttons, as AllTrails' does.
        Spacer(Modifier.fillMaxWidth().windowInsetsBottomHeight(WindowInsets.navigationBars))
    }
}

@Composable
private fun RowScope.BarItem(title: String, glyph: ImageVector, on: Boolean, role: Role, modifier: Modifier, onClick: () -> Unit) {
    val brand = Brand.colors
    val tint = if (on) brand.moss else brand.inkSoft
    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center,
        modifier = modifier
            .weight(1f)
            .fillMaxHeight()
            .clickable(role = role, onClick = onClick),
    ) {
        Icon(glyph, contentDescription = null, tint = tint, modifier = Modifier.size(24.dp))
        Spacer(Modifier.height(4.dp))
        Text(title, fontSize = 12.sp, fontWeight = if (on) FontWeight.SemiBold else FontWeight.Medium, color = tint, maxLines = 1)
    }
}
