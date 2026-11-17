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
            resolver.openOutputStream(uri)?.use { it.write(raw) }
            values.clear()
            values.put(MediaStore.Images.Media.IS_PENDING, 0)
            resolver.update(uri, values, null, null)
        }
    }
}
