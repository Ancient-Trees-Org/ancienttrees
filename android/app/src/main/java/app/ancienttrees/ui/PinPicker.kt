// A map you drag under a fixed pin, to say where something is. Ported from ios
// Screens/PinPicker.swift. Convention: Google Maps ("Move map to adjust") and
// Airbnb's location step: the MAP moves under a pin that never moves, so the
// thumb never covers what it aims at. Our trees nearby are drawn for context.
// An address field over the map (2026-11-26, as Airbnb's location step and
// Google Maps' "Add a missing place"): suggestions from the platform's own
// Geocoder, a pick flies the map there and the crosshair does the rest, so the
// coordinate still comes from the pin and never from the words.

package app.ancienttrees.ui

import android.location.Geocoder
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.BasicTextField
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.HorizontalDivider
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.compose.ui.focus.onFocusChanged
import androidx.compose.ui.graphics.SolidColor
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalFocusManager
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.sp
import app.ancienttrees.R
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.withContext
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.Icon
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberUpdatedState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.unit.dp
import app.ancienttrees.feed.Here
import app.ancienttrees.feed.Tree
import app.ancienttrees.feed.ViewBox
import app.ancienttrees.map.MoveRequest
import app.ancienttrees.map.TreeMapView

/** A box [metres] across, centred on [lat],[lng]. */
fun boxAround(lat: Double, lng: Double, metres: Double): ViewBox {
    val dLat = metres / 2 / 111_320.0
    val dLng = dLat / kotlin.math.cos(Math.toRadians(lat)).coerceAtLeast(0.01)
    return ViewBox(lat - dLat, lng - dLng, lat + dLat, lng + dLng)
}

@Composable
fun PinPicker(
    start: Here,
    trees: List<Tree>,
    spanMetres: Double,
    onMove: (Here) -> Unit,
    modifier: Modifier = Modifier,
    /** Presses of a locate control drawn over it (PlacePin's arrow): back to the person. */
    recentre: Int = 0,
) {
    val latest by rememberUpdatedState(onMove)
    // TreeMap.swift zoom(forMeters:): the span is laid across 375 points whatever
    // the phone, so a wider screen shows proportionally more. Fitting the span to
    // this screen's own width opened about 10 percent closer than the iPhone
    // (the review's place-pin row: "zoomed in much further").
    val widthDp = androidx.compose.ui.platform.LocalConfiguration.current.screenWidthDp
    val opening = remember { MoveRequest(1L, boxAround(start.lat, start.lng, spanMetres * widthDp / 375.0)) }
    var move by remember { mutableStateOf(opening) }
    Box(modifier) {
        TreeMapView(
            trees = trees,
            selected = null,
            onSelect = { },
            origin = start,
            located = true,
            dot = false,
            recentre = recentre,
            onView = { b -> latest(Here((b.south + b.north) / 2, (b.west + b.east) / 2)) },
            moveTo = move,
            modifier = Modifier.matchParentSize(),
        )
        // Dead centre, hanging from its point like a map pin: the tip marks the spot.
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            modifier = Modifier.align(Alignment.Center).offset(y = (-20).dp),
        ) {
            // mappin at 34 semibold: a pin on a needle, never the teardrop. The set's
            // own needle pin is keep (no ball-headed pin in it; data/android-parity.json).
            Icon(Sym.MapPin, null, tint = Brand.colors.moss, modifier = Modifier.size(45.dp))
            Box(Modifier.offset(y = (-3).dp).size(6.dp).shadow(2.dp, CircleShape).background(Brand.colors.moss, CircleShape))
        }
        AddressBox(
            onPick = { lat, lng ->
                move = MoveRequest(move.token + 1, boxAround(lat, lng, spanMetres * widthDp / 375.0))
                latest(Here(lat, lng))
            },
            modifier = Modifier.align(Alignment.TopCenter).padding(start = 16.dp, end = 16.dp, top = 12.dp),
        )
    }
}

/** One suggestion: the first part of the address line, and the rest under it. */
private data class Found(val title: String, val sub: String, val lat: Double, val lng: Double)

/**
 * The field and, while somebody types, the suggestions under it in the same card
 * (PinPicker.swift addressBox: 44 tall, radius 14, 12 inside, rows 56 tall).
 */
@Composable
private fun AddressBox(onPick: (Double, Double) -> Unit, modifier: Modifier = Modifier) {
    val brand = Brand.colors
    val context = LocalContext.current
    val focus = LocalFocusManager.current
    var query by remember { mutableStateOf("") }
    var typing by remember { mutableStateOf(false) }
    var results by remember { mutableStateOf(emptyList<Found>()) }
    var picked by remember { mutableStateOf("") }
    // The geocoder answered for the query as it stands (PinPicker.swift answered).
    var answered by remember { mutableStateOf(false) }
    val coordinate = typedCoordinate(query)

    LaunchedEffect(query) {
        val q = query.trim()
        answered = false
        if (q.length < 3 || q == picked || typedCoordinate(q) != null) { results = emptyList(); return@LaunchedEffect }
        delay(350)
        results = withContext(Dispatchers.IO) {
            runCatching {
                if (!Geocoder.isPresent()) return@runCatching emptyList()
                @Suppress("DEPRECATION")
                Geocoder(context).getFromLocationName(q, 5).orEmpty().map { a ->
                    val line = a.getAddressLine(0) ?: a.featureName ?: q
                    val head = line.substringBefore(", ")
                    Found(head, line.substringAfter(", ", ""), a.latitude, a.longitude)
                }
            }.getOrDefault(emptyList())
        }
        answered = true
    }

    fun pick(f: Found) {
        picked = listOf(f.title, f.sub).filter { it.isNotEmpty() }.joinToString(", ")
        query = picked
        results = emptyList()
        focus.clearFocus()
        onPick(f.lat, f.lng)
    }

    Column(
        modifier
            .fillMaxWidth()
            .shadow(6.dp, RoundedCornerShape(14.dp))
            .background(brand.surfaceMuted, RoundedCornerShape(14.dp))
            .border(1.dp, brand.hairline, RoundedCornerShape(14.dp)),
    ) {
        Row(
            verticalAlignment = Alignment.CenterVertically,
            modifier = Modifier.fillMaxWidth().heightIn(min = 44.dp).padding(horizontal = 12.dp),
        ) {
            Icon(Sym.Search, null, tint = brand.inkSoft, modifier = Modifier.size(20.dp))
            Spacer(Modifier.width(8.dp))
            Box(Modifier.weight(1f)) {
                BasicTextField(
                    value = query,
                    onValueChange = { query = it },
                    singleLine = true,
                    textStyle = sfStyle(fontSize = 16.sp, color = brand.ink),
                    cursorBrush = SolidColor(brand.moss),
                    keyboardOptions = KeyboardOptions(autoCorrectEnabled = false, imeAction = ImeAction.Search),
                    keyboardActions = KeyboardActions(onSearch = {
                        coordinate?.let { (la, lo) -> pick(Found(query.trim(), "", la, lo)) }
                            ?: results.firstOrNull()?.let { pick(it) }
                    }),
                    modifier = Modifier.fillMaxWidth().onFocusChanged { typing = it.isFocused }.testTag("pin-address"),
                )
                if (query.isEmpty()) Text(stringResource(R.string.pin_address_search), fontSize = 16.sp, color = brand.inkSoft)
            }
            if (query.isNotEmpty()) {
                val clear = stringResource(R.string.pin_address_clear)
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier.size(32.dp)
                        .clickable(role = Role.Button, onClickLabel = clear) { query = ""; picked = ""; results = emptyList() },
                ) { Icon(Sym.Close, clear, tint = brand.inkSoft, modifier = Modifier.size(18.dp)) }
            }
        }
        // Typed coordinates, one row straight there (PinPicker.swift, Google Maps' field).
        if (typing && coordinate != null) {
            HorizontalDivider(color = brand.hairline)
            val (la, lo) = coordinate
            val label = String.format(java.util.Locale.ROOT, "%.5f, %.5f", la, lo)
            Row(
                verticalAlignment = Alignment.CenterVertically,
                modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp)
                    .clickable(role = Role.Button) { pick(Found(label, "", la, lo)) }
                    .padding(horizontal = 12.dp)
                    .testTag("pin-address-coordinates"),
            ) {
                Icon(Sym.MapPin, null, tint = brand.moss, modifier = Modifier.size(22.dp))
                Spacer(Modifier.width(14.dp))
                Column(Modifier.weight(1f)) {
                    Text(label, style = sfStyle(fontSize = 16.sp, color = brand.ink), maxLines = 1)
                    Text(stringResource(R.string.pin_address_coords), fontSize = 12.sp, color = brand.inkSoft, maxLines = 1)
                }
            }
        } else if (typing && answered && results.isEmpty()) {
            // Nothing found says so, and what still works (PinPicker.swift pin-address-none).
            HorizontalDivider(color = brand.hairline)
            Text(
                stringResource(R.string.pin_address_none), fontSize = 15.sp, color = brand.inkSoft,
                modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp).padding(horizontal = 12.dp, vertical = 18.dp)
                    .testTag("pin-address-none"),
            )
        }
        if (typing && results.isNotEmpty()) {
            HorizontalDivider(color = brand.hairline)
            results.forEachIndexed { i, f ->
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp)
                        .clickable(role = Role.Button) { pick(f) }
                        .padding(horizontal = 12.dp)
                        .testTag("pin-address-$i"),
                ) {
                    Icon(Sym.MapPin, null, tint = brand.moss, modifier = Modifier.size(22.dp))
                    Spacer(Modifier.width(14.dp))
                    Column(Modifier.weight(1f)) {
                        Text(f.title, style = sfStyle(fontSize = 16.sp, color = brand.ink), maxLines = 1, overflow = TextOverflow.Ellipsis)
                        if (f.sub.isNotEmpty()) Text(f.sub, fontSize = 12.sp, color = brand.inkSoft, maxLines = 1, overflow = TextOverflow.Ellipsis)
                    }
                }
            }
        }
    }
}

/** "52.2101, 5.2902", with a space or a semicolon too; null for anything else or out of range. */
internal fun typedCoordinate(text: String): Pair<Double, Double>? {
    val parts = text.trim().split(',', ';', ' ').filter { it.isNotEmpty() }
    if (parts.size != 2 || parts.any { '.' !in it }) return null
    val la = parts[0].toDoubleOrNull() ?: return null
    val lo = parts[1].toDoubleOrNull() ?: return null
    return if (la in -90.0..90.0 && lo in -180.0..180.0) la to lo else null
}
