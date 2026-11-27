import sys
from PIL import Image, ImageDraw, ImageFont
S=sys.argv[1]
def font(sz):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
        try: return ImageFont.truetype(p, sz)
        except Exception: pass
    return ImageFont.load_default()
def sheet(title, rows, out, W=2000):
    ims=[]
    for label,path in rows:
        im=Image.open(path).convert("RGB"); r=W/im.width
        ims.append((label, im.resize((W,int(im.height*r)))))
    H=110+sum(60+im.height for _,im in ims)
    c=Image.new("RGB",(W,H),(255,250,245)); d=ImageDraw.Draw(c)
    d.multiline_text((24,18),title,fill=(69,34,107),font=font(34),spacing=6)
    y=110
    for label,im in ims:
        d.text((24,y+12),label,fill=(69,34,107),font=font(30)); y+=60
        c.paste(im,(0,y)); y+=im.height
    c.save(out,quality=88)
b=S+"/bath/"; s=S+"/bow7/"
sheet("Bathtile bow, issue 948: before (main) and after (on the cap's top right corner, BowScale 0.51)",
 [("Before, front: Plain, Pink Royal, Gold, Gold Royal",b+"front_old.png"),("After, front",b+"front_hi.png"),
  ("Before, side",b+"left_old.png"),("After, side",b+"left_hi.png")], sys.argv[2])
sheet("Seven other cats whose bow moved, issue 948 (Pink Royal tier)\nLeft to right: Sherbet, Stardust, Rosette, Prism, Phoenix, Djinn, White Tiger",
 [("Before (main), front",s+"front_o7.png"),("After, front",s+"front_n7.png"),("Before (main), from above",s+"above_o7.png"),("After, from above",s+"above_n7.png")], sys.argv[3])
