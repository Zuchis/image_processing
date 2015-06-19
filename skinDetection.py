import cv2
#import numpy as np
#from PIL import Image
# 77 <= Cb <= 127 and 133 <= Cr <= 173
img = cv2.imread('asian2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgYCC = cv2.cvtColor(img, cv2.COLOR_RGB2YCR_CB)
l,h,nChannels = img.shape
#imgYCC = np.zeros((l,h,3), np.uint8)
#imgYCC = Image.new("RGB",(l,h))
print (l,h)
#for i in range (0,l):
    #for j in range(0,h):
        #cr = imgYCC.item(i,j,1)
        #cb = imgYCC.item(i,j,2)
        #if (cb < 77 and cb > 127 and cr < 133 and cr > 173):
            #img.itemset((i,j,0),0)
            #img.itemset((i,j,1),0)
            #img.itemset((i,j,2),0)
for i in range (0,l):
    for j in range (0,h):
        r = (img.item(i,j,0)/255)
        g = (img.item(i,j,1)/255)
        b = (img.item(i,j,2)/255)
        y = (65.4810 * r) + (128.5530 * g) + (24.9660 * b) + 16
        cr = (-37.7745 * r) + (-74.1592 * g) + (111.9337 * b) + 128
        cb = (111.9581 * r) + (-93.7509 * g) + (-18.2072 * b) + 128
        if (cb < 77 and cb > 127 and cr < 133 and cr > 173):
            img.itemset((i,j,0),0)
            img.itemset((i,j,1),0)
            img.itemset((i,j,2),0)

#img = cv2.cvtColor(imgYCC, cv2.COLOR_YCR_CB2RGB)
#cv2.imshow('teste',imgYCC)
cv2.imshow('teste',img)
#imgYCC.save('teste',"JPEG")
cv2.waitKey(0)
