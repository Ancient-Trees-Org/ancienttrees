# The test APK of the "minified" build type (FlowWalk against the Play build's R8).
# Compile-time annotations the test libraries carry, never present at run time.
-dontwarn javax.lang.model.**
# The tests read the app by test tag, not by name; keep their own classes whole.
-keep class app.ancienttrees.** extends junit.framework.TestCase { *; }
-keepattributes *Annotation*
