import sys
from PIL import Image, ImageDraw, ImageFont
S, PREV, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
F = "/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf"
f1, f2, f3 = ImageFont.truetype(F, 44), ImageFont.truetype(F, 30), ImageFont.truetype(F, 24)
old = "Cozy Scrubby Pebble Pickle Koi Bamboo Coral Nimbus".split()
new = [("Clover", "Common"), ("Ghost", "Common"), ("Ooze", "Uncommon"), ("Glitch", "Uncommon"), ("Angler", "Rare"),
       ("Nebula", "Rare"), ("Dragon", "Epic"), ("Blaze", "Legendary")]
RC = {"Common": (120, 120, 120), "Uncommon": (60, 150, 80), "Rare": (60, 110, 200), "Epic": (150, 70, 190), "Legendary": (210, 140, 20)}
C = 300
W, H = 8 * C + 40, 80 + 230 + 70 + C + C + 120
im = Image.new("RGB", (W, H), (252, 241, 226)); d = ImageDraw.Draw(im)
d.text((20, 18), "Crate pets #883: before (top) and after", font=f1, fill=(70, 40, 70))
y = 80
for i, n in enumerate(old):
    p = Image.open(f"{PREV}/CleanACat_Pet_{n}.png").convert("RGB")
    w = p.width; p = p.crop((int(w * .22), int(w * .18), int(w * .78), int(w * .74))).resize((210, 210))
    im.paste(p, (20 + i * C + 45, y)); d.text((20 + i * C + 150, y + 214), n, font=f3, fill=(120, 100, 110), anchor="mt")
y += 260
d.line((20, y, W - 20, y), fill=(200, 180, 170), width=3); y += 20
for row, kind in ((0, "portrait_Pet_{}_ink.png"), (1, "icon_Pet_{}_ink.png")):
    for i, (n, r) in enumerate(new):
        p = Image.open(f"{S}/" + kind.format(n)).convert("RGBA").resize((C - 20, C - 20))
        im.paste(p, (20 + i * C + 10, y), p)
    y += C
for i, (n, r) in enumerate(new):
    x = 20 + i * C + C // 2
    d.text((x, y + 8), n, font=f2, fill=(70, 40, 70), anchor="mt"); d.text((x, y + 46), r, font=f3, fill=RC[r], anchor="mt")
d.text((20, H - 34), "Top of each pair: face portrait. Below: full look. Stars left off (they show at 2 and 3 stars).", font=f3, fill=(120, 100, 110))
im.save(OUT)
