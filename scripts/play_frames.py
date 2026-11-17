#!/usr/bin/env python3
"""play_frames.py - the Google Play phone screenshots in the App Store's dress.

Hidde, 2026-11-17, looking at the bare Android screens on the Play listing:
"is dat hetzelfde wat we voor ios hebben gemaakt want dan hebben we zo'n mooi
achtergrondje enzo". So the panels are scripts/appstore_frames.py's: the cream
ground he chose on 2026-08-29, his captions in two weights, his opener
photograph. Three things differ, each forced by Play or by honesty:

  - 1080 x 1920 (9:16). Play refuses a long side over twice the short one, and
    9:16 at 1080 is what qualifies for its larger placements. The iPhone's
    1320 x 2868 is 2.17:1 and would be refused.
  - An Android phone around the screen, not an iPhone: an even black bezel, a
    punch-hole camera, the power and volume keys on the right. The listing
    shows what somebody on Android will hold.
  - The screens are Android's own, from the release build (play_shots.py).

    python3 scripts/play_shots.py      # raw screens into out/play/phone-*.png
    python3 scripts/play_frames.py     # framed panels into out/play/framed/
"""
import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import appstore_frames as af  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "out" / "play"
OUT = RAW / "framed"
HERO_PHOTO = ROOT / "out" / "appstore" / "0-hero.jpg"

W, H = 1080, 1920
GROUND = af.GROUNDS["cream"]

# The iPhone panels' numbers scaled to this canvas, then given the air the
# shorter canvas needs: 9:16 has less height under the caption than 6.9 inch.
CAPTION_TOP = 112
CAPTION_SIZE = 58
LINE_GAP = 10
DEVICE_TOP = 400
DEVICE_WIDTH = 860
BEZEL = 16
RAIL = 6
CORNER = 40

# His captions and his order (appstore_frames.PANELS, 1.0.3), for the screens
# Android has today; My trees and Add join when play_shots.py takes them.
PANELS = [
    ("phone-1-map", "Find remarkable old trees\nwherever you are"),
    ("phone-2-tree", "Read what makes it\nworth the walk"),
    ("phone-4-discover", "See which trees are\nat their best this month"),
    ("phone-3-city", "See every old tree\nin a city"),
]


def android(shot):
    """The screen inside an Android phone: even bezel, punch-hole, keys right."""
    w = shot.width + (BEZEL + RAIL) * 2
    h = shot.height + (BEZEL + RAIL) * 2
    body = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(body)
    d.rounded_rectangle([0, 0, w, h], radius=CORNER + BEZEL + RAIL, fill=(0x3A, 0x3D, 0x38))
    d.rounded_rectangle([RAIL, RAIL, w - RAIL, h - RAIL], radius=CORNER + BEZEL,
                        fill=(0x0B, 0x0D, 0x09))
    body.paste(shot, (RAIL + BEZEL, RAIL + BEZEL), af.rounded(shot, CORNER))
    # The punch-hole camera, centred in the status bar.
    r = 11
    cx, cy = w // 2, RAIL + BEZEL + 26
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0x05, 0x06, 0x05))
    # Power and volume on the right rail, as on a Pixel or a Galaxy.
    key = (0x2A, 0x2C, 0x28)
    unit = shot.width // 18
    for top, length in ((int(h * 0.17), unit * 2), (int(h * 0.27), unit * 3)):
        d.rounded_rectangle([w - RAIL + 1, top, w, top + length], radius=RAIL // 2, fill=key)
    return body


def panel(raw_path, caption):
    canvas = Image.new("RGB", (W, H), GROUND[0])
    draw = ImageDraw.Draw(canvas)
    y = CAPTION_TOP
    for i, line in enumerate(caption.split("\n")):
        f = af.font("Gabarito-ExtraBold.ttf" if i == 0 else "Gabarito-Regular.ttf", CAPTION_SIZE)
        draw.text(((W - draw.textlength(line, font=f)) / 2, y), line, font=f, fill=GROUND[1])
        y += CAPTION_SIZE + LINE_GAP
    shot = Image.open(raw_path).convert("RGB")
    shot = shot.resize((DEVICE_WIDTH, int(shot.height * DEVICE_WIDTH / shot.width)), Image.LANCZOS)
    keep = H - DEVICE_TOP + 40
    if shot.height > keep:
        shot = shot.crop((0, 0, shot.width, keep))
    device = android(shot)
    x = (W - DEVICE_WIDTH) // 2
    canvas.paste(device, (x - BEZEL - RAIL, DEVICE_TOP - BEZEL - RAIL), device)
    return canvas


def hero(photo_path, line):
    """appstore_frames.hero at this size: the photograph and his promise, low left."""
    canvas = Image.new("RGB", (W, H), GROUND[0])
    photo = Image.open(photo_path).convert("RGB")
    scale = max(W / photo.width, H / photo.height)
    photo = photo.resize((int(photo.width * scale), int(photo.height * scale)), Image.LANCZOS)
    canvas.paste(photo, ((W - photo.width) // 2, (H - photo.height) // 2))
    scrim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(scrim)
    reach = int(H * 0.55)
    for i in range(reach):
        d.line([(0, H - 1 - i), (W, H - 1 - i)], fill=(10, 14, 8, int(200 * (1 - i / reach) ** 1.3)))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), scrim).convert("RGB")
    draw = ImageDraw.Draw(canvas)
    size = 86
    f = af.font("Gabarito-ExtraBold.ttf", size)
    lines = line.split("\n")
    y = H - 300 - int(size * 1.08) * (len(lines) - 1)
    for i, text in enumerate(lines):
        af.draw_tracked(draw, 70, y, text, f, -size * 0.02, af.GOLD_HERO if i == 1 else af.CREAM)
        y += int(size * 1.08)
    return canvas


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    made = []
    if HERO_PHOTO.exists():
        hero(HERO_PHOTO, af.HERO_LINE).save(OUT / "0-hero.png")
        made.append("0-hero.png")
    for pos, (name, caption) in enumerate(PANELS, start=1):
        raw = RAW / f"{name}.png"
        if not raw.exists():
            print(f"skip {name}: no raw screen")
            continue
        fname = f"{pos}-{name.split('-', 2)[2]}.png"
        panel(raw, caption).save(OUT / fname)
        made.append(fname)
    print(f"{len(made)} panels in {OUT}: {', '.join(made)}")


if __name__ == "__main__":
    main()
