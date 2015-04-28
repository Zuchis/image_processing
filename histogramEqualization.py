from PIL import Image

im1 = Image.open ('lowContrast.jpg').convert("L")
(l,h) = im1.size
out = Image.new(im1.mode,(l,h))
print("width = "+str(l) + " height = "+ str(h))
his = im1.histogram()
print(his)
y = len(his)
p = []
fda = []
for i in range (0,y):
    p.append((his[i]*(y-1))/(float)(l*h))

print
print
print(p)

for i in range (0,y):
    fda.append(0)
    for j in range (0,i+1):
        fda[i] += int(p[j])
    #fda[i]=int(fda[i]*(y-1))

print
print
print(fda)

for i in range (0,l):
    for j in range (0,h):
        pos = im1.getpixel((i,j))
        out.putpixel((i,j), fda[pos])

out.save("equalizedContrast.jpg","JPEG");
