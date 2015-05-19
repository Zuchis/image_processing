from PIL import Image
from imageFunctions import *

b = set()
neighbor = 3
for s in range (-(neighbor/2),((neighbor/2)+1)):
    for t in range (-2,3):
        b.add((s,t))

im1 = dilation('BarackObama.jpg',b)
im1.save("Dilation","JPEG")

im2 = imageThreshold('BarackObama.jpg',200)
im2.save("binary","JPEG")

im3 = erosion('BarackObama.jpg',b)
im3.save("Erosion","JPEG")
