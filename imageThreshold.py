from PIL import Image
import numpy as np

im1 = Image.open('BarackObama.jpg').convert("L")
(l,h) = im1.size
out = Image.new(im1.mode,(l,h))
T = 50

for k in range (0,4):
    for j in range (0,h):
        for i in range (0,l):
            if im1.getpixel((j,i)) >= T:
                out.putpixel((j, i), im1.getpixel((j,i)))
            else:
                out.putpixel((j,i), 0)
    out.save("Out" + str(k) + ".jpg","JPEG");
    T = T + 50

