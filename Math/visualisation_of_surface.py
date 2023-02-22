import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definice funkce f(x,y)
def f(x,y):
    return 2*x**3 + x*y**2 - 5*x**2 + y**2

# Vytvoření 3D mřížky pro x a y
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# Spočítání hodnot z f(x,y) pro každý bod v mřížce
Z = f(X,Y)

# Vykreslení plochy

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.show()