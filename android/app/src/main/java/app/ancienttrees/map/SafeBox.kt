package app.ancienttrees.map

import app.ancienttrees.feed.ViewBox

/**
 * A box MapLibre accepts, whatever was asked (Hidde's Samsung, 2026-11-17: signing
 * in crashed the app with "latitude must be between -90 and 90"; My trees framed
 * collected trees from Europe to Japan, and the 1.4 margin carried the box past the
 * pole). MapKit clamps a region by itself; MapLibre throws. Latitudes stay inside
 * the Web Mercator band, and a box wider than the world is the world.
 */
fun safeBox(box: ViewBox): ViewBox {
    val south = box.south.takeUnless { it.isNaN() }?.coerceIn(-85.0, 85.0) ?: -85.0
    var north = box.north.takeUnless { it.isNaN() }?.coerceIn(-85.0, 85.0) ?: 85.0
    if (north <= south) north = (south + 0.0001).coerceAtMost(85.0)
    val whole = box.west.isNaN() || box.east.isNaN() || box.east - box.west >= 360.0
    return ViewBox(south, if (whole) -180.0 else box.west, north, if (whole) 180.0 else box.east)
}
