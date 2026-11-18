package app.ancienttrees.map

/**
 * Which of your trees a map opens on (Collect.swift MapFrame.densest on the iPhone).
 * All of them when they fit one view at the world's floor zoom; otherwise the
 * 40 by 60 degree window that holds the most of them, so a collection from Spain
 * to Japan opens on Japan's 43 trees rather than on the empty middle between them
 * (Hidde, 2026-11-17).
 */
object MapFrame {
    const val MAX_LAT_SPAN = 40.0
    const val MAX_LNG_SPAN = 60.0

    fun densest(points: List<Pair<Double, Double>>): List<Pair<Double, Double>> {
        if (points.size < 2) return points
        val latSpan = points.maxOf { it.first } - points.minOf { it.first }
        val lngSpan = points.maxOf { it.second } - points.minOf { it.second }
        if (latSpan <= MAX_LAT_SPAN && lngSpan <= MAX_LNG_SPAN) return points
        var best = points
        var bestCount = 0
        for (anchor in points) {
            val window = points.filter {
                kotlin.math.abs(it.first - anchor.first) <= MAX_LAT_SPAN / 2 &&
                    kotlin.math.abs(it.second - anchor.second) <= MAX_LNG_SPAN / 2
            }
            if (window.size > bestCount) {
                bestCount = window.size
                best = window
            }
        }
        return best
    }
}
