import sys, os
from PIL import Image, ImageDraw
out=sys.argv[1]; items=sys.argv[2:]   # label=path[,before]
rows=[]
for it in items:
    lab,p=it.split("=",1); ps=p.split(",")
    rows.append((lab,[Image.open(x).convert("RGBA") for x in ps]))
CW=300; W=150+CW*2+48+24+CW+80; H=CW*len(rows)+40
sh=Image.new("RGB",(W,H),(255,246,236)); d=ImageDraw.Draw(sh)
d.text((150,6),"before",fill=(60,45,70)); d.text((150+CW,6),"after (256), 48 px, 24 px, silhouette",fill=(60,45,70))
for i,(lab,ims) in enumerate(rows):
    y=30+i*CW; d.text((8,y+130),lab,fill=(60,45,70))
    new=ims[0]
    if len(ims)>1:
        b=ims[1].resize((256,256),Image.LANCZOS); sh.paste(b,(150,y+20),b)
    else: d.text((230,y+130),"(new)",fill=(120,110,120))
    a=new.resize((256,256),Image.LANCZOS); sh.paste(a,(150+CW,y+20),a)
    x=150+2*CW
    for px in (48,24):
        t=new.resize((px,px),Image.LANCZOS); sh.paste(t,(x,y+120),t); x+=px+16
    sil=Image.new("RGBA",new.size,(0,0,0,255)); sil.putalpha(new.getchannel("A")); sil=sil.resize((256,256),Image.LANCZOS)
    sh.paste(sil,(x+10,y+20),sil)
sh.save(out)
