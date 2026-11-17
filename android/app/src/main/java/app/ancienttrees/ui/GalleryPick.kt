// Photographs from the phone: Android's own photo picker, the standard route.
//
// Tried and dropped the same day (2026-11-17): Samsung Gallery through ACTION_PICK,
// to keep the GPS the picker may leave out; on Hidde's Samsung it answered "error
// getting selected file". The picker's "1 photo unavailable" is the picker failing
// to fetch a photograph that lives only in the cloud; the others come through. A
// photograph without its place gets "Where does it stand?" in the flow.

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
    override fun createIntent(context: Context, input: Unit): Intent =
        // ANDROID'S OWN PHOTO PICKER, the standard every app on the phone uses (AllTrails,
        // Google's guidance). Samsung Gallery through ACTION_PICK answered "error getting
        // selected file" on Hidde's Samsung (2026-11-17). A photograph that arrives
        // without its place gets the flow's "Where does it stand?" (FlowWalk's
        // aLibraryPhotoWithoutAPlaceAsksWhereItStands).
        ActivityResultContracts.PickMultipleVisualMedia(maxOf(2, max))
            .createIntent(context, PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))

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
    // No permission first: the picker needs none, and asking for the photographs'
    // place made Android ask for access to every photo (seen on the emulator).
    return { pick.launch(Unit) }
}
