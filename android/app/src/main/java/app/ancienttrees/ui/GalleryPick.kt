// Photographs from the phone's own gallery app, with their place left in.
//
// Android's photo picker (PickVisualMedia) strips the GPS from every photograph it
// hands over, and on Hidde's Samsung it also refused photographs it could not fetch
// ("1 photo unavailable", 2026-11-17). A reader's tree goes live on a photograph and
// a GPS fix, so the place in the file is the one thing we cannot lose. The gallery
// app (ACTION_PICK on MediaStore) returns a MediaStore item, and with
// ACCESS_MEDIA_LOCATION Collector.read asks for the original, GPS included
// (MediaStore.setRequireOriginal). This is iNaturalist's route on Android for the
// same reason. A phone with no gallery app gets the system picker as before.

package app.ancienttrees.ui

import android.Manifest
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Build
import android.provider.MediaStore
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.PickVisualMediaRequest
import androidx.activity.result.contract.ActivityResultContract
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.rememberUpdatedState
import androidx.compose.ui.platform.LocalContext
import androidx.core.content.ContextCompat

class GalleryPick(private val max: Int) : ActivityResultContract<Unit, List<Uri>>() {
    override fun createIntent(context: Context, input: Unit): Intent {
        val gallery = Intent(Intent.ACTION_PICK)
            .setDataAndType(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, "image/*")
            .putExtra(Intent.EXTRA_ALLOW_MULTIPLE, max > 1)
        if (gallery.resolveActivity(context.packageManager) != null) return gallery
        return ActivityResultContracts.PickMultipleVisualMedia(maxOf(2, max))
            .createIntent(context, PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))
    }

    override fun parseResult(resultCode: Int, intent: Intent?): List<Uri> {
        if (resultCode != android.app.Activity.RESULT_OK || intent == null) return emptyList()
        val out = mutableListOf<Uri>()
        intent.clipData?.let { clip -> for (i in 0 until clip.itemCount) clip.getItemAt(i).uri?.let(out::add) }
        if (out.isEmpty()) intent.data?.let(out::add)
        return out.distinct().take(max)
    }
}

/** True once the app may read the place stored in a photograph (Android 10 and up). */
fun mayReadPhotoPlace(context: Context): Boolean =
    Build.VERSION.SDK_INT < Build.VERSION_CODES.Q ||
        ContextCompat.checkSelfPermission(context, Manifest.permission.ACCESS_MEDIA_LOCATION) == PackageManager.PERMISSION_GRANTED

/**
 * The gallery, asking first (once) for the photographs' place. Whatever the answer,
 * the gallery opens: without the permission the photographs simply arrive without it.
 */
@Composable
fun rememberGalleryPick(max: Int, onPicked: (List<Uri>) -> Unit): () -> Unit {
    val context = LocalContext.current
    val handler by rememberUpdatedState(onPicked)
    val pick = rememberLauncherForActivityResult(GalleryPick(max)) { handler(it) }
    val place = rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) { pick.launch(Unit) }
    return {
        if (mayReadPhotoPlace(context)) pick.launch(Unit) else place.launch(Manifest.permission.ACCESS_MEDIA_LOCATION)
    }
}
