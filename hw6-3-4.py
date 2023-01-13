import numpy as np
import matplotlib.pyplot as plt
# ls = np.array([1,0,2,0,0,1])
# f = np.poly1d(ls)
# fn = f([2,5])
# print(f)
# print(fn)

# fm1 = np.polyder(f,1)
# fm2 = np.polyder(f,2)
# print(fm1)
# print(fm2)

x1 = np.linspace(0,2*np.pi,100,endpoint=True)
x2 = np.linspace(-2,2,100,endpoint=True)
y1 = np.sin(x1) + x1**2
y2 = x2**3 + 2*x2**2 + 1
plt.plot(x1,y1,'r',x2,y2,'g')
plt.legend(['$y=sin(x)+x^2$','$y=x^3+2*x^2+1$'])
plt.show()