import sys
from PIL import Image
out=sys.argv[1]; ims=[Image.open(p).convert("RGBA") for p in sys.argv[2:]]
h=max(i.height for i in ims); W=sum(i.width for i in ims)+10*(len(ims)-1)
c=Image.new("RGBA",(W,h),(236,236,236,255)); x=0
for i in ims: c.alpha_composite(i,(x,0)); x+=i.width+10
c.convert("RGB").save(out)
