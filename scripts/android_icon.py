#!/usr/bin/env python3
"""Android's launcher icon and splash, made from the iPhone's 1024 app icon.

Hidde, 2026-11-17, on his Samsung: "when opening the app it shortly shows a very
pixelated logo". Android had one 192 px PNG; the system blew it up to the splash's
240 dp and cut it with a circle. Android wants an ADAPTIVE icon instead
(developer.android.com/develop/ui/views/launch/icon_design_adaptive): a 108 dp
background layer and a 108 dp foreground layer the launcher masks to its own shape,
of which a 66 dp circle is always shown, plus a single-colour layer for themed
icons; and the splash (developer.android.com/develop/ui/views/launch/splash-screen)
shows a 240 dp icon through a 160 dp circle.

The tree is lifted off the icon's cream ground by unblending: each pixel's alpha is
how far it stands from the cream, so the antialiased edge survives on any ground.

    python3 scripts/android_icon.py      # writes android/app/src/main/res
"""
import pathlib

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "ios/AncientTrees/AncientTrees/Assets.xcassets/AppIcon.appiconset/AppIcon.png"
RES = ROOT / "android/app/src/main/res"
DENSITIES = {"mdpi": 1, "hdpi": 1.5, "xhdpi": 2, "xxhdpi": 3, "xxxhdpi": 4}
# The tree's height as a share of each canvas. Launcher: 0.48 of 108 dp, the
# iPhone's proportion (the tree is 69 percent of the icon) on the 72 dp a launcher
# shows, well inside the 66 dp safe circle. Splash: 0.56 of 240 dp, inside its
# 160 dp circle.
LAUNCHER_SHARE = 0.48
SPLASH_SHARE = 0.56


def tree() -> Image.Image:
    """The tree alone, on transparency, cropped to its bounds."""
    im = Image.open(SRC).convert("RGB")
    bg = im.getpixel((4, 4))
    out = Image.new("RGBA", im.size)
    src, dst = im.load(), out.load()
    for y in range(im.height):
        for x in range(im.width):
            c = src[x, y]
            # Every colour of the tree stands at least 60 from the cream, so anything
            # that far is solid; only the antialiased rim, nearer, is a blend.
            dist = max(abs(ch - b) for ch, b in zip(c, bg))
            a = min(1.0, dist / 60)
            if a < 0.04:
                continue
            if a == 1.0:
                dst[x, y] = (*c, 255)
                continue
            fg = tuple(max(0, min(255, round((ch - (1 - a) * b) / a))) for ch, b in zip(c, bg))
            dst[x, y] = (*fg, round(a * 255))
    return out.crop(out.getbbox())


def placed(t: Image.Image, canvas_px: int, share: float, mono: bool = False) -> Image.Image:
    h = round(canvas_px * share)
    w = round(t.width * h / t.height)
    art = t.resize((w, h), Image.LANCZOS)
    if mono:
        alpha = art.getchannel("A")
        art = Image.new("RGBA", art.size, (0, 0, 0, 255))
        art.putalpha(alpha)
    canvas = Image.new("RGBA", (canvas_px, canvas_px), (0, 0, 0, 0))
    # The iPhone's tree sits a touch below the middle (its bounds 172 to 880 of 1024).
    canvas.alpha_composite(art, ((canvas_px - w) // 2, (canvas_px - h) // 2 + round(canvas_px * 0.01)))
    return canvas


def main():
    t = tree()
    full = Image.open(SRC).convert("RGB")
    for name, k in DENSITIES.items():
        d = RES / f"mipmap-{name}"
        d.mkdir(parents=True, exist_ok=True)
        placed(t, round(108 * k), LAUNCHER_SHARE).save(d / "ic_launcher_foreground.png", optimize=True)
        placed(t, round(108 * k), LAUNCHER_SHARE, mono=True).save(d / "ic_launcher_monochrome.png", optimize=True)
        # The legacy icon for launchers before Android 8: the iPhone's own, at 48 dp.
        full.resize((round(48 * k),) * 2, Image.LANCZOS).save(d / "ic_launcher.png", optimize=True)
        dd = RES / f"drawable-{name}"
        dd.mkdir(parents=True, exist_ok=True)
        placed(t, round(240 * k), SPLASH_SHARE).save(dd / "splash_tree.png", optimize=True)
    any_dpi = RES / "mipmap-anydpi-v26"
    any_dpi.mkdir(exist_ok=True)
    (any_dpi / "ic_launcher.xml").write_text(
        '<?xml version="1.0" encoding="utf-8"?>\n'
        "<!-- Made by scripts/android_icon.py from the iPhone's app icon. -->\n"
        '<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n'
        '    <background android:drawable="@color/ic_launcher_background" />\n'
        '    <foreground android:drawable="@mipmap/ic_launcher_foreground" />\n'
        '    <monochrome android:drawable="@mipmap/ic_launcher_monochrome" />\n'
        "</adaptive-icon>\n")
    bg = full.getpixel((4, 4))
    (RES / "values" / "colors_icon.xml").write_text(
        '<?xml version="1.0" encoding="utf-8"?>\n'
        "<!-- The iPhone app icon's cream (scripts/android_icon.py). -->\n"
        "<resources>\n"
        f'    <color name="ic_launcher_background">#{bg[0]:02X}{bg[1]:02X}{bg[2]:02X}</color>\n'
        "</resources>\n")
    print("icon and splash written")


if __name__ == "__main__":
    main()
