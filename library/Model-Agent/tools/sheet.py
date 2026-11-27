import sys
from PIL import Image, ImageDraw, ImageFont
src, out = sys.argv[1], sys.argv[2]
rows = [("dirty-front", "Muddy, tub close up"), ("dirty-play", "Muddy, play camera"),
        ("brushed-front", "Brushed (fluff on), tub close up"), ("brushed-play", "Brushed (fluff on), play camera")]
W, H, HEAD, LAB = 1200, 400, 70, 44
try:
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 34)
    g = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
except OSError:
    f = g = ImageFont.load_default()
sheet = Image.new("RGB", (2 * W + 30, HEAD + len(rows) * (H + LAB) + 20), "#FFF8EE")
d = ImageDraw.Draw(sheet)
d.text((10, 16), "Before (main)", fill="#3A3640", font=f)
d.text((W + 30, 16), "After (issue 791)", fill="#3A3640", font=f)
for i, (key, label) in enumerate(rows):
    y = HEAD + i * (H + LAB)
    d.text((10, y + 6), label + "   (Muffin, Inky, Rosette)", fill="#6B6252", font=g)
    for c, tag in enumerate(("B", "A")):
        im = Image.open(f"{src}/{tag}-{key}.png").convert("RGB").resize((W, H), Image.LANCZOS)
        sheet.paste(im, (c * (W + 30), y + LAB))
sheet.save(out, optimize=True)
print(sheet.size)
