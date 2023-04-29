import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return np.exp(-x**2) * np.sin(y)

x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)

X, Y = np.meshgrid(x, y)

Z = f(X, Y)

plt.pcolormesh(X,Y,Z)
plt.colorbar()
plt.show()


