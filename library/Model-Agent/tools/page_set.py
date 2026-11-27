import os, sys
B = "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/wtpr/assets/clean-a-cat/blender"
sys.path.insert(0, B)
from PIL import Image, ImageDraw, ImageFilter
import store_compose as sc
raw, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
W, H = 1920, 1080
BIG = os.environ.get("BIG_RAW", raw)
def RB(key):
    p = os.path.join(BIG, f"raw-{key}.png")
    return Image.open(p if os.path.exists(p) else os.path.join(raw, f"raw-{key}.png")).convert("RGBA")
def wide_close(key, seed, y0):
    """The square close up as wide as the frame, no fade: a 1080 high window of it starting y0 of the way down."""
    bg = sc.bubble_backdrop((W, H), seed=seed)
    art = RB(key).resize((W, W), Image.LANCZOS)
    bg.alpha_composite(art, (0, -int(W * y0)))
    return bg
def R(key): return Image.open(os.path.join(raw, f"raw-{key}.png")).convert("RGBA")
def save(im, name):
    im.convert("RGB").save(os.path.join(out, name)); print(name, os.path.getsize(os.path.join(out, name)) // 1024, "KB")
def square_big(key, seed, k=1.0, dx=0.0, dy=0.0):
    bg = sc.bubble_backdrop((W, H), seed=seed)
    side = int(H * k)
    art = R(key).resize((side, side), Image.LANCZOS)
    art = sc.soft_shadow_edges(art, 0.12) if False else art
    # fade the square's left and right edges so it sits in the wide backdrop
    m = Image.new("L", (side, side), 255); d = ImageDraw.Draw(m); f = int(side * 0.1)
    for i in range(f):
        a = int(255 * i / f); d.line((i, 0, i, side), fill=a); d.line((side - 1 - i, 0, side - 1 - i, side), fill=a)
    art.putalpha(Image.composite(art.getchannel("A"), Image.new("L", (side, side), 0), m))
    bg.alpha_composite(art, (int(W / 2 - side / 2 + dx * W), int(H / 2 - side / 2 + dy * H)))
    return bg
# A1: the cat in the foam, face blown up
save(wide_close("icon-spa", 4, float(os.environ.get("Y1", 0.08))), "home-1-cat-in-foam-1920x1080.png")
# A3: the stray in the box, close
save(wide_close("icon-box", 5, float(os.environ.get("Y3", 0.04))), "home-3-stray-in-box-1920x1080.png")
# A2: half muddy, half clean, closer and no words
def split_close(kk=1.45, top=0.03, title=False):
    size = (W, H); mid = W // 2
    bg = sc.bubble_backdrop(size); bg.paste(sc.mud_backdrop(size).crop((0, 0, mid, H)), (0, 0))
    dirty, clean = R("split-dirty"), R("split-clean")
    rm = dirty.width // 2
    art = clean.copy(); art.paste(dirty.crop((0, 0, rm, dirty.height)), (0, 0))
    box = art.getchannel("A").point(lambda a: 255 if a > 60 else 0).getbbox()
    reach = max(rm - box[0], box[2] - rm)
    art = art.crop((rm - reach, box[1], rm + reach, box[3]))
    solid = dirty.getchannel("A").point(lambda a: 255 if a >= 250 else 0).getbbox()
    k = H * kk / (solid[3] - solid[1])
    art = art.resize((int(art.width * k) // 2 * 2, int(art.height * k)), Image.LANCZOS)
    bg.alpha_composite(art, (mid - art.width // 2, int(H * top)))
    line = Image.new("RGBA", size, (0, 0, 0, 0)); lw = 8
    ImageDraw.Draw(line).rectangle((mid - lw - 3, 0, mid + lw + 3, H), fill=(40, 30, 60, 90))
    line = line.filter(ImageFilter.GaussianBlur(lw * 0.8))
    ImageDraw.Draw(line).rectangle((mid - lw, 0, mid + lw - 1, H), fill=sc.SPLIT_LINE + (255,))
    bg.alpha_composite(line)
    if title:
        t = sc.fit(sc.title_block(int(W * 0.62), lines=(("CLEAN A CAT", (255, 255, 255), (255, 132, 180)),), tilt=0), W * 0.6, H * 0.22)
        bg.alpha_composite(t, (mid - t.width // 2, int(H * 0.015)))
    return bg
save(split_close(1.05, 0.25, True), "detail-2-half-muddy-half-clean-1920x1080.png")
save(split_close(), "home-2-half-muddy-half-clean-1920x1080.png")
# A4: the title with one big cat
def title_cat():
    bg = sc.bubble_backdrop((W, H), seed=6)
    side = int(H * 1.12)
    art = RB("icon-spa").resize((side, side), Image.LANCZOS)
    m = Image.new("L", (side, side), 255); d = ImageDraw.Draw(m); f = int(side * 0.14)
    for i in range(f):
        d.line((i, 0, i, side), fill=int(255 * i / f))
    art.putalpha(Image.composite(art.getchannel("A"), Image.new("L", (side, side), 0), m))
    bg.alpha_composite(art, (W - side + int(W * 0.03), int(H * 0.03)))
    title = sc.fit(sc.title_block(int(W * 0.44)), W * 0.46, H * 0.92)
    bg.alpha_composite(title, (int(W * 0.235 - title.width / 2), int(H * 0.5 - title.height / 2)))
    return bg
save(title_cat(), "home-4-title-and-cat-1920x1080.png")
# B1: scrubbing a muddy cat with the sponge
save(wide_close("icon-a", 8, float(os.environ.get("YD", 0.06))), "detail-1-scrub-the-mud-1920x1080.png")
# B3: helpers at the wash stands
if os.path.exists(os.path.join(raw, "raw-thumb-busy.png")):
    save(sc.compose_lineup(raw, True, "thumb-busy"), "detail-3-helpers-at-work-1920x1080.png")
# C: icon A with the title
def icon_title():
    bg = sc.icon_spa(raw)
    title = sc.title_block(900, lines=(("CLEAN A CAT", (255, 255, 255), (255, 132, 180)),), tilt=0)
    title = sc.fit(title, 500, 120)
    bg.alpha_composite(title, (256 - title.width // 2, 512 - title.height - 8))
    return bg
save(icon_title(), "icon-a-with-title-512.png")
# B4 and B5: the counter and the crate (the renders are the whole frame, the sky see-through)
NEW = os.environ.get("NEW_RAW", raw)
def full_frame(key, seed, sparkles=()):
    bg = sc.bubble_backdrop((W, H), seed=seed)
    bg.alpha_composite(Image.open(os.path.join(NEW, f"raw-{key}.png")).convert("RGBA").resize((W, H), Image.LANCZOS))
    fx = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(fx)
    for fxr, fyr, r in sparkles:
        sc.sparkle(d, fxr * W, fyr * H, r * H, (255, 255, 255, 235)); sc.sparkle(d, fxr * W, fyr * H, r * H * 0.5, (255, 244, 176, 255))
    bg.alpha_composite(fx)
    return bg
if os.path.exists(os.path.join(NEW, "raw-thumb-counter.png")):
    save(full_frame("thumb-counter", 11), "detail-4-cats-waiting-at-the-counter-1920x1080.png")
if os.path.exists(os.path.join(NEW, "raw-thumb-crate.png")):
    save(full_frame("thumb-crate", 12, ((0.3, 0.2, 0.05), (0.7, 0.16, 0.04), (0.12, 0.3, 0.03), (0.9, 0.34, 0.035), (0.5, 0.07, 0.03))),
         "detail-5-pets-from-crates-1920x1080.png")
