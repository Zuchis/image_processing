from PIL import Image
from imageFunctions import *

b = set()
for s in range (-2,3):
    for t in range (-2,3):
        b.add((s,t))
im1 = dilation('BarackObama.jpg',b)
im1.save("teste","JPEG")

im2 = imageThreshold('BarackObama.jpg',200)
im2.save("teste2","JPEG")
