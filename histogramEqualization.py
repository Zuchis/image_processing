from PIL import Image
import numpy as np

im1 = Image.open ('lowContrast.jpg').convert("L")
(l,h) = im1.size
out = Image.new(im1.mode,(l,h))

his = im1.histogram()
print(his)
L = len(his)
p = []
fda = []
for i in range (0,L):
    p.append(his[i]/(l*h))

for i in range (0,L):
    fda[i] = 0
    for j in range (0,i):
        fda[i] += p[j]
    fda[i] *= (L-1)

for i in range (0,h):
    for j in range (0,l):
        pos = im1.getpixel((i,j))
        out.putpixel((i,j), fda[pos])

out.save('equalizedContrast.jpg',"JPEG");





