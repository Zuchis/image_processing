import cv2
#import numpy as np
#from PIL import Image
# 77 <= Cb <= 127 and 133 <= Cr <= 173
img = cv2.imread('asian1.jpg')
imgYCC = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
#hist = cv2.calcHist([imgYCC],[2],None,[256],[0,256])
#print(hist)
#cv2.imshow('oi',imgYCC)
#cv2.waitKey(0)
l,h,nChannels = imgYCC.shape
print (l,h)
for i in range (0,l):
    for j in range (0,h):
        cr = imgYCC.item(i,j,1)
        cb = imgYCC.item(i,j,2)
        if (cr <= 135 and cr >= 180 and cb <= 85 and cb >= 135):
            imgYCC.itemset((i,j,0),0)
            imgYCC.itemset((i,j,1),0)
            imgYCC.itemset((i,j,2),0)

img = cv2.cvtColor(imgYCC, cv2.COLOR_YCR_CB2BGR)
cv2.imshow('teste',imgYCC)
cv2.waitKey(0)
