from PIL import Image
import numpy as np

im1 = Image.open ('lowContrast.jpg').convert("L")
(l,h) = im1.size
out = Image.new(im1.mode,(l,h))
print("width = "+str(l) + " height = "+ str(h))
his = im1.histogram()
print(his)
y = len(his)
p = []
fda = []
for i in range (0,y):
    p.append(his[i]/(float)(l*h))

print
print
print(p)

for i in range (0,y):
    fda.append(0)
    for j in range (0,i+1):
        fda[i] += p[j]
    fda[i]=int(np.around(fda[i]*(y-1)))

print
print
print(fda)

for j in range (0,h):
    for i in range (0,l):
        pos = im1.getpixel((j,i))
        out.putpixel((j,i), fda[pos])

out.save("equalizedContrast.jpg","JPEG");
