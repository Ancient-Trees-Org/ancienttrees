// Photographs from the phone, with the place the camera wrote into them.
//
// Measured on the emulator, 2026-11-18, with a photo carrying GPS (Baarn town hall):
// - Android's photo picker strips the GPS and refuses the original outright
//   ("Require Original is not supported for Picker URI"), with or without
//   ACCESS_MEDIA_LOCATION: every gallery photo arrived as "Where does it stand?";
// - Samsung Gallery through ACTION_PICK answered "error getting selected file";
// - the documents UI (ACTION_OPEN_DOCUMENT) hands the file with its GPS once the app
//   holds ACCESS_MEDIA_LOCATION ("Allow all" on Android's photos question; "limited"
//   with nothing selected does not grant it).
// So the documents UI, and the place asked for once, right after the first photo is
// chosen, when the question has a reason on screen (Hidde, 2026-11-18: "belangrijk
// dat we gps krijgen"). A refusal still lets the photo through: the flow asks where
// it stands, as before. The app never reads the library, only the files chosen.

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
import androidx.compose.runtime.setValue
import androidx.compose.runtime.rememberUpdatedState
import androidx.compose.ui.platform.LocalContext
import androidx.core.content.ContextCompat

class GalleryPick(private val max: Int) : ActivityResultContract<Unit, List<Uri>>() {
    override fun createIntent(context: Context, input: Unit): Intent =
        Intent(Intent.ACTION_OPEN_DOCUMENT)
            .addCategory(Intent.CATEGORY_OPENABLE)
            .setType("image/*")
            .putExtra(Intent.EXTRA_ALLOW_MULTIPLE, max > 1)

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
    var pending by androidx.compose.runtime.remember { androidx.compose.runtime.mutableStateOf<List<Uri>>(emptyList()) }
    val place = rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) {
        val chosen = pending
        pending = emptyList()
        handler(chosen)
    }
    val pick = rememberLauncherForActivityResult(GalleryPick(max)) { uris ->
        val prefs = context.getSharedPreferences("device", Context.MODE_PRIVATE)
        if (uris.isNotEmpty() && !mayReadPhotoPlace(context) && !prefs.getBoolean("photo_place_asked", false)) {
            prefs.edit().putBoolean("photo_place_asked", true).apply()
            pending = uris
            place.launch(Manifest.permission.ACCESS_MEDIA_LOCATION)
        } else {
            handler(uris)
        }
    }
    return { pick.launch(Unit) }
}
