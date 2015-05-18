import numpy,Image
import matplotlib.pyplot as plt1
import matplotlib.image as mpimg
import matplotlib.cm as cm
import matplotlib.figure as fg
import pymorph as pm

#https://pythonhosted.org/pymorph/

a = raw_input("Repetições (Ero, Dil): ")
n = int(a)

img=mpimg.imread('lenaShort.jpg')
#print(type(img))

img2 = pm.binary(img,200)
#print(type(img2))

fig=plt1.figure()
#fig.suptitle('Erosão e Dilatação binária', fontsize=14, fontweight='bold')
plt1.subplot(1,4,1)
plt1.imshow(img, origin='down', cmap = cm.Greys_r)
plt1.title('original')

plt1.subplot(1,4,2)
plt1.imshow(img2, origin='down', cmap = cm.Greys_r)
plt1.title('Binaria')

imgDil=pm.dilate(img2)
if (n>1):
    for k in [2,n,1]:
        imgDil=pm.dilate(imgDil)
 
    
plt1.subplot(1,4,3)
plt1.imshow(imgDil, origin='down', cmap = cm.Greys_r)
plt1.title('Dilatada '+str(n)+' vez(es)')
plt1.interactive(True)
plt1.show()

imgEro=pm.erode(img2)
if (n>1):
    for k in [2,n,1]:
        imgEro=pm.erode(imgEro)

    
plt1.subplot(1,4,4)
plt1.imshow(imgEro, origin='down', cmap = cm.Greys_r)
plt1.title('Erodida '+str(n)+' vez(es)')
plt1.interactive(True)
plt1.show()
