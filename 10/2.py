import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 500)

y1 = (-3 * x) + 15
y2 = x**3 - 5
y3 = np.sin(3 * x) / x


plt.figure(figsize=(10, 6))

plt.plot(x, y1, label='y = -3x + 15', color='red')
plt.plot(x, y2, label='y = x³ - 5', color='green')
plt.plot(x, y3, label='y = sin(3x) / x', color='blue')

plt.ylim(-50, 50)

plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Графики математических функций')

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle='--', alpha=0.6)

plt.legend()

plt.show()