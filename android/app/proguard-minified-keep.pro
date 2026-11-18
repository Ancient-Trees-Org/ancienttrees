# Only for the "minified" build type (tests against the Play build's R8). The test APK
# leans on the app for the libraries it shares (Kotlin, coroutines, Compose, Guava's
# ListenableFuture ...), which R8 strips from the app where the app itself does not use
# a part; each one fails every test with NoClassDefFoundError. So every library stays
# whole here, and only the app's own code is shrunk and renamed exactly as for release:
# that is what this run is for (a class of ours R8 strips wrongly). Library-side R8
# faults are caught by the Play apk itself (scripts/android_release_walk.py).
-keep class !app.ancienttrees.**,** { *; }
-dontwarn **
