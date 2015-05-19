from PIL import Image

def imageThreshold(imageName,T):
    im1 = Image.open(imageName).convert("L")
    (l,h) = im1.size
    out = Image.new(im1.mode,(l,h))
    for j in range (0,h):
        for i in range (0,l):
            if im1.getpixel((j,i)) >= T:
                out.putpixel((j, i), im1.getpixel((j,i)))
            else:
                out.putpixel((j,i), 0)
    return out

def dilation(imageName,b):
    im1 = imageThreshold(imageName,200)
    n = (2**8)-1 # arrumar isso aqui
    a = set()
    c = set()
    (l,h) = im1.size
    for i in range (0,l):
        for j in range (0,h):
            if(im1.getpixel((i,j))>=200):
                a.add((i,j))
    for i in a:
        for j in b:
            c.add((i[0]+j[0],i[1]+j[1]))

    out = Image.new(im1.mode,(l,h))
    for i in range (0,l):
        for j in range(0,h):
            if (i,j) in c:
                out.putpixel((i,j),n)
            else:
                out.putpixel((i,j),0)
    return out

def erosion(imageName,b):
    im1 = imageThreshold(imageName,200)
    n = (2**8)-1 # arrumar isso aqui
    common = set()
    flag = 0
    a = set()
    c = set()
    (l,h) = im1.size
    for i in range (0,l):
        for j in range (0,h):
            if(im1.getpixel((i,j))>=200):
                a.add((i,j))
    for j in b:
        for i in a:
            c.add((i[0]-j[0],i[1]-j[1]))
        if flag == 0:
            common = c.copy()
            flag = 1
        else:
            common = common.intersection(c)
        c.clear()

    out = Image.new(im1.mode,(l,h))
    for i in range (0,l):
        for j in range (0,h):
            if (i,j) in common:
                out.putpixel((i,j),n)
            else:
                out.putpixel((i,j),0)
    return out
