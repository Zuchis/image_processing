from PIL import Image

im1 = Image.open ('lowContrast.jpg').convert("L")
(l,h) = im1.size
out = Image.new(im1.mode,(l,h))
his = im1.histogram()
L = len(his)
p = []
for i in range (0,L):
    p+=[his[i]/(l*h)]

E = 4
k0 = 0.4 # k0 has to be smaller than 1
k1 = 0.02
k2 = 0.4 # k2 has to be greater than k1
mG = 0
devG = 0
neighbor = 3 #this is where the neighborhood lenght is determined
for i in range (0,l):
    for j in range (0,h):
        out.putpixel((i,j),im1.getpixel((i,j)))

for ri in range (0,L):
    mG += ri * p[ri]

for ri in range (0,L):
    devG += ((ri - mG)**2)*p[ri]

for i in range ((neighbor/2),l-(neighbor/2)):
    for j in range ((neighbor/2),h-(neighbor/2)):
        mS = 0
        devS = 0
        for t in range (-(neighbor/2),(neighbor/2)+1):
            for s in range (-(neighbor/2),(neighbor/2)+1):
                ri = im1.getpixel((i+t,j+s))
                mS += ri * p[ri]
        for t in range (-(neighbor/2),(neighbor/2)+1):
            for s in range (-(neighbor/2),(neighbor/2)+1):
                ri = im1.getpixel((i+t,j+s))
                devS += ((ri- mS)**2) * p[ri]
                        #print "%5d %5d %5d %5d" %(mG,mS,devG,devS)
        if (mS <= (k0*mG)) and ((k1*devG) <= devS) and (devS <= (k2*devG)):
            out.putpixel((i,j), int(im1.getpixel((i,j))*E))
       # else :
        #    out.putpixel((i,j), im1.getpixel((i,j)))

out.save("equalizedContrast.jpg","JPEG");
