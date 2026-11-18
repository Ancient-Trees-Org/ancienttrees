// Kit/CameraRoll.swift: a copy of every photograph taken with the app's camera, in
// the phone's own gallery (Pictures/Ancient Trees).
//
// Convention: iNaturalist saves each photograph its camera takes to the camera roll
// (CONVENTIONS.md 2026-09-11); Hidde, finding his Kyoto photographs only inside the
// app: "doe dit maar dit willen mensen". On Android 10 and up an app may add to its
// own folder in Pictures without any permission and never reads anything back, the
// same as iOS's add-only access. Older phones simply get no copy. The camera's own
// file is copied whole, so the place and time the camera wrote travel with it.

package app.ancienttrees.account

import android.content.ContentValues
import android.content.Context
import android.os.Build
import android.provider.MediaStore
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

object CameraRoll {
    /**
     * The phone's last fix written into the copy when the camera app wrote none, as
     * the iPhone's CameraRoll.keep sets the asset's location (Hidde, 2026-11-18:
     * "belangrijk dat we gps krijgen"). Never over a position the camera wrote.
     */
    @android.annotation.SuppressLint("MissingPermission")
    private fun withPlace(context: Context, raw: ByteArray): ByteArray = runCatching {
        val tmp = java.io.File.createTempFile("roll", ".jpg", context.cacheDir)
        try {
            tmp.writeBytes(raw)
            val exif = androidx.exifinterface.media.ExifInterface(tmp)
            if (exif.latLong != null) return@runCatching raw
            val lm = context.getSystemService(Context.LOCATION_SERVICE) as android.location.LocationManager
            val fix = listOf(android.location.LocationManager.GPS_PROVIDER, android.location.LocationManager.NETWORK_PROVIDER)
                .mapNotNull { p -> runCatching { lm.getLastKnownLocation(p) }.getOrNull() }
                .maxByOrNull { it.time } ?: return@runCatching raw
            // Only a fresh fix: a position from an hour ago is not where the shutter fell.
            if (System.currentTimeMillis() - fix.time > 10 * 60_000L) return@runCatching raw
            exif.setLatLong(fix.latitude, fix.longitude)
            exif.saveAttributes()
            tmp.readBytes()
        } finally {
            tmp.delete()
        }
    }.getOrDefault(raw)

    suspend fun keep(context: Context, raw: ByteArray) = withContext(Dispatchers.IO) {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.Q) return@withContext
        runCatching {
            val resolver = context.contentResolver
            val values = ContentValues().apply {
                put(MediaStore.Images.Media.DISPLAY_NAME, "ancient-trees-" + System.currentTimeMillis() + ".jpg")
                put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg")
                put(MediaStore.Images.Media.RELATIVE_PATH, "Pictures/Ancient Trees")
                put(MediaStore.Images.Media.IS_PENDING, 1)
            }
            val uri = resolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values) ?: return@runCatching
            resolver.openOutputStream(uri)?.use { it.write(withPlace(context, raw)) }
            values.clear()
            values.put(MediaStore.Images.Media.IS_PENDING, 0)
            resolver.update(uri, values, null, null)
        }
    }
}
