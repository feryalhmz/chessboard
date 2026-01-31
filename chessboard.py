import matplotlib.pyplot as plt
import numpy as np
dx,dy=0.015,0.05
x=np.arange(-4.0,4.0,dx)
y=np.arange(-4.0,4.0,dy)
X,Y=np.meshgrid(x,y)
extent=np.min(x),np.max(x),np.min(y),np.max(y)
Z1=np.add.outer(range(8),range(8))%2
plt.imshow(Z1,extent=extent,interpolation='nearest',cmap='binary_r',alpha=1)

def chess(x,y):
    return (1-x/2+x**5+y**6)*np.exp(-(-x**2-y**2))
z2=chess(X,Y)
plt.imshow(z2,extent=extent,interpolation='bilinear',alpha=0)
plt.title('Chessboard ')
plt.show()