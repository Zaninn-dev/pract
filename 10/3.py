import matplotlib.pyplot as plt
import numpy as np

val = np.arange(2002,2013)
val1 = (16, 30, 43, 73, 110, 147, 172, 233, 318, 395, 433)

plt.bar(val, val1)
plt.xlabel('Месяц')
plt.ylabel('Количество')
plt.title('Продажи по месяцам')

plt.show()


