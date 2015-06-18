import cv2
import numpy as np
#from PIL import Image
# 77 <= Cb <= 127 and 133 <= Cr <= 173
img = cv2.imread('asian1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#imgYCC = cv2.cvtColor(img, cv2.COLOR_RGB2YCR_CB)
l,h,nChannels = img.shape
imgYCC = np.zeros((l,h,3), np.uint8)
print (l,h)
for i in range (0,l):
    for j in range (0,h):
        imgYCC[i,j,0] = (65.4810 * img[i,j,0]) + (128.5530 * img[i,j,1]) + (24.9660 * img[i,j,2]) + 16
        imgYCC[i,j,1] = (-37.7745 * img[i,j,0]) + (-74.1592 * img[i,j,1]) + (111.9337 * img[i,j,2]) + 128
        imgYCC[i,j,2] = (111.9581 * img[i,j,0]) + (-93.7509 * img[i,j,1]) + (-18.2072 * img[i,j,2]) + 128
        if (imgYCC[i,j,1] < 133 and imgYCC[i,j,1] > 173 and imgYCC[i,j,2] < 77 and imgYCC[i,j,2] > 127):
            imgYCC[i,j,0] = 0
            imgYCC[i,j,1] = 0
            imgYCC[i,j,2] = 0

img = cv2.cvtColor(imgYCC, cv2.COLOR_YCR_CB2RGB)
cv2.imshow('teste',img)
cv2.waitKey(0)
