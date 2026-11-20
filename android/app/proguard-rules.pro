# R8 for the release build (app/build.gradle.kts). MapLibre, AndroidX, Compose
# and Play's review library ship their own consumer rules; the app reads its
# feeds with Android's built-in org.json and finds nothing by reflection, so
# what is left is keeping a crash readable.

# Line numbers in crash traces; Play reads the mapping file the bundle carries.
-keepattributes SourceFile,LineNumberTable
-renamesourcefileattribute SourceFile

# MapLibre's native code calls back into Java by name.
-keep class org.maplibre.** { *; }
-dontwarn org.maplibre.**

# Our own classes keep their names (not their code: R8 still shrinks them), so a
# crash note from a phone reads as MyTreesKt.photo:950 without the mapping file,
# on any machine (account/ExitWatch.kt, Hidde 2026-11-20 after five crashes on
# build 3 arrived with no line).
-keepnames class app.ancienttrees.** { *; }
