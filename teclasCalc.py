from ia636 import *
import numpy as np
from pylab import *
f = iaread('keyCalc.pgm') #('lena.pgm')[:3,:5]  # slice das 'n' primeiras linhas e 'm' primeiras colunas
iashow(f)
print(type(f))
print 'f=\n', f

H,W = f.shape
j = np.zeros( (H,) ) # vetor de W elementos
print(j)
for i in np.arange(H):
      j[i] = f[i,:].mean()
print 'g=\n', f.round(1)

g = np.zeros( (W,) ) # vetor de W elementos
print(g)
for i in np.arange(W):
      g[i] = f[:,i].mean()
print 'g=\n', g.round(1)

ion()



plt.show()
subplot(1,2,1)
plot(np.arange(W),g)
xlabel('Coluna')
ylabel('media dos tons de cinza')
title('media dos tons de cinza nas colunas')
subplot(1,2,2)
plot(np.arange(H),j)
xlabel('Linhas')
ylabel('media dos tons de cinza')
title('media dos tons de cinza nas linhas')
