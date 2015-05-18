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
    return im1

