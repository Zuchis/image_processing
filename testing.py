from PIL import Image
from imageFunctions import *

im1 = imageThreshold('BarackObama.jpg',250)
im1.save("teste","JPEG")
