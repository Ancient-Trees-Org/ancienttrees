// The species picker crashed on a stranger's phone on build 4 (2026-11-21,
// IndexOutOfBounds "Index 0 out of bounds for length 0"): a search that matched
// nothing gave groupedSection count 0, and it still read key(0) for its gap item.
// This drives groupedSection through a recording LazyListScope, no device needed.

package app.ancienttrees.ui

import androidx.compose.foundation.lazy.LazyItemScope
import androidx.compose.foundation.lazy.LazyListScope
import androidx.compose.runtime.Composable
import org.junit.Assert.assertEquals
import org.junit.Test

class GroupedSectionTest {
    private class Recorder : LazyListScope {
        val keys = mutableListOf<Any?>()

        override fun item(key: Any?, contentType: Any?, content: @Composable LazyItemScope.() -> Unit) {
            keys += key
        }

        override fun items(
            count: Int,
            key: ((index: Int) -> Any)?,
            contentType: (index: Int) -> Any?,
            itemContent: @Composable LazyItemScope.(index: Int) -> Unit,
        ) {
            repeat(count) { keys += key?.invoke(it) }
        }
    }

    @Test
    fun anEmptySectionDrawsNothingAndNeverReadsRowZero() {
        val rows = emptyList<String>()
        val scope = Recorder()
        scope.groupedSection(
            header = null,
            headerText = { "" },
            count = rows.size,
            key = { rows[it] },
            footer = { "" },
        ) {}
        assertEquals(emptyList<Any?>(), scope.keys)
    }

    @Test
    fun aSectionWithRowsStillDrawsItsGapRowsAndFooter() {
        val rows = listOf("Oak", "Yew")
        val scope = Recorder()
        scope.groupedSection(
            header = null,
            headerText = { "" },
            count = rows.size,
            key = { rows[it] },
            footer = { "" },
        ) {}
        assertEquals(listOf("gap-Oak", "Oak", "Yew", "f-Oak"), scope.keys)
    }
}
