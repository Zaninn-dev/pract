import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 50)

y1 = (-3 * x) + 15
y2 = x**3 - 5
y3 = np.sin(x * 3) / x

plt.plot(x, y1, label='y = x')
plt.plot(x, y2, label='y = x^3 - 5')
plt.plot(x, y3, label='y = sin(3 * x) / x')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Графики функций')
plt.legend()

plt.show()

