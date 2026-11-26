// A tree only you have, still being added, kept on this phone until Save or
// Discard, so Android ending the app behind the camera does not take it with it
// (2026-11-26, after report 1686: the first photograph was rescued, but a draft
// open when the reader went for a further photograph lived in memory only, and
// the name, story and photographs went with the app). data/cross-device.json
// "draft-tree": an unsent draft is the device's (hard rule 11), gone the moment
// it is saved or discarded, and thrown away after a day.
//
// Plain files under filesDir/draft-tree/: draft.properties for the fields,
// lead.jpg and extra-<n>.jpg for the photographs. java.util.Properties, so the
// unit test runs without Android.

package app.ancienttrees.account

import java.io.File
import java.util.Date
import java.util.Properties

object DraftStore {
    /** How long an unsent draft stays worth handing back. */
    const val KEEP_MS = 24 * 60 * 60 * 1000L

    fun dir(filesDir: File) = File(filesDir, "draft-tree")

    fun save(filesDir: File, d: Collector.Draft, nowMs: Long = System.currentTimeMillis()) {
        val dir = dir(filesDir)
        runCatching {
            dir.mkdirs()
            dir.listFiles()?.filter { it.name.endsWith(".jpg") }?.forEach { it.delete() }
            d.jpeg?.let { File(dir, "lead.jpg").writeBytes(it) }
            d.extras.forEachIndexed { i, b -> File(dir, "extra-$i.jpg").writeBytes(b) }
            val p = Properties()
            p["id"] = d.id
            p["name"] = d.name
            p["lat"] = d.lat.toString()
            p["lng"] = d.lng.toString()
            p["taken"] = d.taken.time.toString()
            p["fixNote"] = d.fixNote
            d.place?.let { p["place"] = it }
            p["note"] = d.note
            d.species?.let { p["species"] = it }
            d.age?.let { p["age"] = it }
            d.girthCm?.let { p["girthCm"] = it.toString() }
            d.takenBasis?.let { p["takenBasis"] = it }
            p["extras"] = d.extras.size.toString()
            p["extraMonths"] = d.extraMonths.joinToString(",") { it?.toString() ?: "" }
            p["savedAt"] = nowMs.toString()
            val tmp = File(dir, "draft.properties.tmp")
            tmp.outputStream().use { p.store(it, null) }
            tmp.renameTo(File(dir, "draft.properties"))
        }
    }

    /** The draft left behind, when there is one and it is less than a day old; else null (and gone). */
    fun load(filesDir: File, nowMs: Long = System.currentTimeMillis()): Collector.Draft? {
        val dir = dir(filesDir)
        val f = File(dir, "draft.properties")
        if (!f.exists()) return null
        val d = runCatching {
            val p = Properties().apply { f.inputStream().use { load(it) } }
            val savedAt = p.getProperty("savedAt")?.toLongOrNull() ?: return@runCatching null
            if (nowMs - savedAt >= KEEP_MS || savedAt > nowMs + 60_000) return@runCatching null
            val n = p.getProperty("extras")?.toIntOrNull() ?: 0
            val extras = (0 until n).mapNotNull { i -> File(dir, "extra-$i.jpg").takeIf { it.exists() }?.readBytes() }
            val months = p.getProperty("extraMonths").orEmpty().split(",").map { it.toIntOrNull() }
            Collector.Draft(
                id = p.getProperty("id") ?: return@runCatching null,
                name = p.getProperty("name").orEmpty(),
                lat = p.getProperty("lat")?.toDoubleOrNull() ?: return@runCatching null,
                lng = p.getProperty("lng")?.toDoubleOrNull() ?: return@runCatching null,
                jpeg = File(dir, "lead.jpg").takeIf { it.exists() }?.readBytes(),
                extras = extras,
                taken = Date(p.getProperty("taken")?.toLongOrNull() ?: savedAt),
                fixNote = p.getProperty("fixNote").orEmpty(),
                place = p.getProperty("place"),
                note = p.getProperty("note").orEmpty(),
                species = p.getProperty("species"),
                age = p.getProperty("age"),
                girthCm = p.getProperty("girthCm")?.toIntOrNull(),
                takenBasis = p.getProperty("takenBasis"),
                extraMonths = extras.indices.map { months.getOrNull(it) },
            )
        }.getOrNull()
        if (d == null) clear(filesDir)
        return d
    }

    fun clear(filesDir: File) {
        runCatching { dir(filesDir).deleteRecursively() }
    }
}
