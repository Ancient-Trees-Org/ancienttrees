// Kit/SentAgo.swift: when a visitor's photograph was sent (Hidde, 2026-11-20:
// "aangeven hoelaat iets is gepost"; "A, met boomnaam"). Short on a tile
// ("2h", "3d"), written out under the hero and in the opened photograph
// ("2 hours ago"), month and year after four weeks ("Oct 2026"). ICU does the
// words in the phone's language, as Foundation does on iOS and Intl on the web.

package app.ancienttrees.ui

import android.icu.text.DateFormat
import android.icu.text.MeasureFormat
import android.icu.text.RelativeDateTimeFormatter
import android.icu.util.Measure
import android.icu.util.MeasureUnit
import java.time.OffsetDateTime
import java.util.Date
import java.util.Locale

object SentAgo {
    private enum class U { MINUTE, HOUR, DAY, WEEK }

    fun short(iso: String?, now: Long = System.currentTimeMillis()): String? {
        val t = millis(iso) ?: return null
        old(t, now)?.let { return it }
        val (u, n) = unit(t, now)
        val m = when (u) { U.MINUTE -> MeasureUnit.MINUTE; U.HOUR -> MeasureUnit.HOUR; U.DAY -> MeasureUnit.DAY; U.WEEK -> MeasureUnit.WEEK }
        return runCatching {
            MeasureFormat.getInstance(Locale.getDefault(), MeasureFormat.FormatWidth.NARROW).format(Measure(n, m))
        }.getOrNull()
    }

    fun long(iso: String?, now: Long = System.currentTimeMillis()): String? {
        val t = millis(iso) ?: return null
        old(t, now)?.let { return it }
        val (u, n) = unit(t, now)
        val r = when (u) {
            U.MINUTE -> RelativeDateTimeFormatter.RelativeUnit.MINUTES
            U.HOUR -> RelativeDateTimeFormatter.RelativeUnit.HOURS
            U.DAY -> RelativeDateTimeFormatter.RelativeUnit.DAYS
            U.WEEK -> RelativeDateTimeFormatter.RelativeUnit.WEEKS
        }
        return runCatching {
            RelativeDateTimeFormatter.getInstance(Locale.getDefault())
                .format(n.toDouble(), RelativeDateTimeFormatter.Direction.LAST, r)
        }.getOrNull()
    }

    private fun old(t: Long, now: Long): String? =
        if (now - t >= 28L * 86_400_000) runCatching {
            DateFormat.getInstanceForSkeleton("MMMy", Locale.getDefault()).format(Date(t))
        }.getOrNull() else null

    private fun unit(t: Long, now: Long): Pair<U, Int> {
        val s = maxOf(0L, (now - t) / 1000)
        return when {
            s < 3600 -> U.MINUTE to maxOf(1, (s / 60).toInt())
            s < 86_400 -> U.HOUR to (s / 3600).toInt()
            s < 7 * 86_400 -> U.DAY to (s / 86_400).toInt()
            else -> U.WEEK to (s / (7 * 86_400)).toInt()
        }
    }

    fun millis(iso: String?): Long? =
        iso?.takeIf { it.isNotBlank() }?.let { runCatching { OffsetDateTime.parse(it).toInstant().toEpochMilli() }.getOrNull() }
}
