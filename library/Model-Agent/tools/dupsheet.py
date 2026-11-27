import sys,glob,os
from PIL import Image,ImageDraw
d,out=sys.argv[1],sys.argv[2]
fs=sorted(glob.glob(d+'/shop_*_ink.png'))
cols=7; c=230
rows=(len(fs)+cols-1)//cols
W=Image.new('RGB',(cols*c,rows*(c+70)),(255,246,236))
dr=ImageDraw.Draw(W)
for i,f in enumerate(fs):
    im=Image.open(f).convert('RGBA')
    x,y=(i%cols)*c,(i//cols)*(c+70)
    t=im.resize((220,220),Image.LANCZOS); W.paste(t,(x+5,y+5),t)
    s=im.resize((48,48),Image.LANCZOS); W.paste(s,(x+5,y+228),s)
    dr.text((x+60,y+240),os.path.basename(f)[5:-8],fill=(60,40,70))
W.save(out)
