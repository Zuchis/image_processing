import cv2
# 77 <= Cb <= 127 and 133 <= Cr <= 173
img = cv2.imread('paimei.jpg')
l,h,nChannels = img.shape
print (l,h)

for i in range (0,l):
    for j in range (0,h):
        r = float(img.item(i,j,0))/255
        g = float(img.item(i,j,1))/255
        b = float(img.item(i,j,2))/255
        y = (65.4810 * r) + (128.5530 * g) + (24.9660 * b) + 16
        cr = (-37.7745 * r) + (-74.1592 * g) + (111.9337 * b) + 128
        cb = (111.9581 * r) + (-93.7509 * g) + (-18.2072 * b) + 128
        if (cb < 77 or cb > 127 or cr < 133 or cr > 173):
            img.itemset((i,j,0),0)
            img.itemset((i,j,1),0)
            img.itemset((i,j,2),0)

cv2.imshow('teste',img)
cv2.waitKey(0)
