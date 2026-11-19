#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news poster (1024x1024 PNG).

Deterministic: same input -> same bytes. No network, no clock, no randomness.
Run:  python3 draw.py            (writes entry.png next to this file)
"""

import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

NAVY = (10, 25, 48)
PANEL = (18, 42, 74)
PANEL_EDGE = (38, 74, 116)
GOLD = (242, 183, 5)
RED = (230, 57, 70)
WHITE = (245, 247, 250)
SOFT = (196, 209, 224)
MUTE = (140, 158, 180)
BLUE = (84, 160, 255)
PURPLE = (178, 132, 255)
GREEN = (74, 222, 158)
ORANGE = (255, 166, 66)
TEAL = (94, 234, 212)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


F_TITLE = font("DejaVuSans-Bold.ttf", 96)
F_DATE = font("DejaVuSans-Bold.ttf", 32)
F_KICKER = font("DejaVuSans-Bold.ttf", 24)
F_HERO_HEAD = font("DejaVuSans-Bold.ttf", 44)
F_HERO_SUB = font("DejaVuSans.ttf", 25)
F_TAG = font("DejaVuSans-Bold.ttf", 21)
F_CELL_HEAD = font("DejaVuSans-Bold.ttf", 27)
F_CELL_SUB = font("DejaVuSans.ttf", 21)
F_ALSO = font("DejaVuSans.ttf", 20)
F_FOOT = font("DejaVuSans.ttf", 19)
F_NUM = font("DejaVuSans-Bold.ttf", 30)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to a pixel width."""
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # thin gold rules, top and bottom
    d.rectangle([0, 0, W, 8], fill=GOLD)
    d.rectangle([0, H - 8, W, H], fill=GOLD)

    # ---- header ----
    d.text((44, 34), "THE WORLD IN ONE PICTURE", font=F_KICKER, fill=GOLD)
    d.text((40, 62), "WORLD NEWS", font=F_TITLE, fill=WHITE)
    d.text((44, 168), "WEDNESDAY  ·  18 NOVEMBER 2026", font=F_DATE, fill=GOLD)
    d.line([44, 216, W - 44, 216], fill=PANEL_EDGE, width=2)

    # ---- hero: top story ----
    hx0, hy0, hx1, hy1 = 44, 236, W - 44, 396
    d.rounded_rectangle([hx0, hy0, hx1, hy1], radius=14, fill=PANEL, outline=PANEL_EDGE, width=2)
    d.rectangle([hx0, hy0 + 14, hx0 + 8, hy1 - 14], fill=GOLD)
    d.rounded_rectangle([hx0 + 28, hy0 + 18, hx0 + 28 + 148, hy0 + 52], radius=8, fill=RED)
    d.text((hx0 + 44, hy0 + 24), "TOP STORY", font=F_TAG, fill=WHITE)
    d.text((hx0 + 28, hy0 + 66), "Xi & Putin meet in Shenzhen", font=F_HERO_HEAD, fill=WHITE)
    d.text((hx0 + 28, hy1 - 42),
           "Ahead of the first-ever Trump trilateral summit on Thursday.",
           font=F_HERO_SUB, fill=SOFT)

    # ---- grid: 2 x 3 stories ----
    stories = [
        ("1", "GULF ON EDGE", RED,
         "US sinks 5 Iranian tankers",
         "Iran fires on a US base in Kuwait as Gulf shipping is attacked."),
        ("2", "UKRAINE", BLUE,
         "Kerch Bridge struck again",
         "Kyiv's strikes shut the Crimea link; biggest POW swap agreed."),
        ("3", "US POLITICS", PURPLE,
         "Peltola flips Alaska seat",
         "Democrats take a projected 56-44 Senate majority."),
        ("4", "CLIMATE", GREEN,
         "COP31 in decisive phase",
         "Negotiators in Antalya race through 144 disputed items."),
        ("5", "TECH", ORANGE,
         "Nvidia chief Huang resigns",
         "Board accepts the CEO's exit; it will not reinstate him."),
        ("6", "WEATHER", TEAL,
         "Cyclone Akvan nears India",
         "Severe storm bears down on Odisha and Andhra Pradesh."),
    ]
    gx0, gy0 = 44, 416
    cw, ch, gap = 458, 152, 16
    for i, (num, tag, color, head, sub) in enumerate(stories):
        cx = gx0 + (i % 2) * (cw + gap)
        cy = gy0 + (i // 2) * (ch + gap)
        d.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=12, fill=PANEL,
                            outline=PANEL_EDGE, width=2)
        # number badge
        d.ellipse([cx + 16, cy + 16, cx + 56, cy + 56], fill=color)
        tw = d.textlength(num, font=F_NUM)
        d.text((cx + 36 - tw / 2, cy + 21), num, font=F_NUM, fill=(10, 25, 48))
        d.text((cx + 70, cy + 18), tag, font=F_TAG, fill=color)
        hl = wrap(d, head, F_CELL_HEAD, cw - 32)
        y = cy + 60
        for ln in hl[:1]:
            d.text((cx + 16, y), ln, font=F_CELL_HEAD, fill=WHITE)
            y += 34
        sl = wrap(d, sub, F_CELL_SUB, cw - 32)
        for ln in sl[:2]:
            d.text((cx + 16, y), ln, font=F_CELL_SUB, fill=SOFT)
            y += 26

    # ---- also strip ----
    ay0 = 916
    d.rounded_rectangle([44, ay0, W - 44, ay0 + 44], radius=10, fill=(13, 33, 60))
    also = "ALSO:  Dhoni retires from the IPL  ·  Pattinson is the new 007  ·  Jesse Jackson dies at 84"
    aw = d.textlength(also, font=F_ALSO)
    d.text(((W - aw) / 2, ay0 + 10), also, font=F_ALSO, fill=SOFT)

    # ---- footer ----
    d.text((44, 972), "Sources: Reuters  ·  AP  ·  AFP  ·  Al Jazeera", font=F_FOOT, fill=MUTE)
    tail = "18 NOV 2026"
    d.text((W - 44 - d.textlength(tail, font=F_FOOT), 972), tail, font=F_FOOT, fill=MUTE)

    img.save(OUT, format="PNG", optimize=True)


if __name__ == "__main__":
    draw()
    print("wrote", OUT)
