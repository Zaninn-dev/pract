import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

x = np.linspace(-3, 3, 30)
y = np.linspace(-3, 3, 30)
X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, label='Поверхность')

fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, pad=0.1)

ax.contour(X, Y, Z, zdir='z', offset=0, cmap='viridis')

ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.set_zlabel('Ось Z')
ax.set_title('3D Параболоид с контурными линиями и шкалой')

plt.show()