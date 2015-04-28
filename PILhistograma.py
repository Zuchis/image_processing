from PIL import Image
import numpy as np
import time as tm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *


pil1=Image.open('lowContrast.jpg')
(l,h)=pil1.size
print(l,h)
n=pil1.histogram()
#print(h)
#b1=plt.bar(range(256),n)
#plt.show()

narray = np.asarray(n)
p=np.float32(narray)/(l*h)
print((l*h))
b2=plt.bar(range(256),p)
#ion()
plt.show()
subplot(3, 1, 1)
plot(range(256),p)
subplot(3,1,2)
plot(range(256),narray)

cp=np.cumsum(p)
subplot(3,1,3)
plot(range(256),cp)
plt.interactive(True)
