from PIL import Image
import numpy as np
from math import sqrt

im1 = Image.open ('lowContrast.jpg').convert("L")
(l,h) = im1.size
out = Image.new(im1.mode,(l,h))
E = 4
k0 = 0.9 # k0 has to be smaller than 1
k1 = 1.5
k2 = 2 # k2 has to be greater than k1

mG = 0
neighbor = 3 #this is where the neighborhood lenght is determined
for i in range (0,l):
    for j in range (0,h):
        mG += im1.getpixel((i,j))

mG /= (l*h)
devGpwr2 = 0

for i in range (0,l):
    for j in range (0,h):
        devGpwr2 += (im1.getpixel((i,j)) - mG) ** 2

devGpwr2 /= (l*h)
devG = sqrt(devGpwr2)
for i in range (0,l):
    for j in range (0,h):
        mS = 0
        devSpwr2 = 0
        for t in range (-1,neighbor-1):
            if (i+t >= 0) and (i+t <= l-1):
                for s in range (-1,neighbor-1):
                    if (j+s >= 0) and (j+s <= h-1):
                        mS += im1.getpixel((i+t,j+s))
                    else :
                        mS += 0
            else :
                mS += 0
        mS /= (neighbor ** 2)
        for t in range (-1,neighbor-1):
            if (i+t >= 0) and (i+t <= l-1):
                for s in range (-1,neighbor-1):
                    if (j+s >= 0) and (j+s <= h-1):
                        devSpwr2 += (im1.getpixel((i+t,j+s))- mS)**2
                    else :
                        devSpwr2 += 0
            else :
                devSpwr2 += 0
        devSpwr2 /= (neighbor ** 2)
        devS = sqrt(devSpwr2)
        #print "%5d %5d %5d %5d" %(mG,mS,devG,devS)
        if (mS <= (k0*mG)) and ((k1*devG) <= devS) and (devS <= (k2*devG)):
            out.putpixel((i,j), im1.getpixel((i,j))*E)
        else :
            out.putpixel((i,j), im1.getpixel((i,j)))

out.save("equalizedContrast.jpg","JPEG");
