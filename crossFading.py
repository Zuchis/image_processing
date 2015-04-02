from PIL import Image
import numpy as np

im1 = Image.open('GeorgeWBush.jpg').convert("L")
im2 = Image.open('BarackObama.jpg').convert("L")
(l,h) = im1.size
out = Image.new(im1.mode,(l,h))
u = 0

for k in range (0,11):
    for j in range (0,h):
        for i in range (0,l):
            out.putpixel((j, i), ((1-u)*im1.getpixel((j,i))) + (u*im2.getpixel((j,i))))
    out.save("Fading" + str(k) + ".jpg","JPEG");
    u = u + 0.1
            
