import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100,endpoint=True)
ls = np.array([3,2,3,4])
f = np.poly1d(ls)
fn1 = np.polyder(f,1)
fn2 = np.polyder(f,2)
fm0 = f(x)
fm1 = fn1(x)
fm2 = fn2(x)

plt.subplot(1,3,1)
plt.plot(x,fm0,'r')
plt.title('Polynomial')

plt.subplot(1,3,2)
plt.plot(x,fm1,'b:')
plt.title('Frist Derivative')

plt.subplot(1,3,3)
plt.plot(x,fm2,'g.')
plt.title('Second Derivative')

plt.show()