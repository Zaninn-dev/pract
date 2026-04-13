import matplotlib.pyplot as plt
import numpy as np

n_groups = 5
pm_means = (25, 34, 27, 36, 21)
m_means = (24, 37, 20, 32, 29)
f_means = (23, 32, 36, 39, 22)

index = np.arange(n_groups)
bar_width = 0.25  # Ширина одного столбца

plt.figure(figsize=(10, 6))

plt.bar(index, pm_means, bar_width, label='ПМ')
plt.bar(index + bar_width, m_means, bar_width, label='М')
plt.bar(index + 2 * bar_width, f_means, bar_width, label='Ф')

plt.xlabel('Группы')
plt.ylabel('Баллы')
plt.title('Баллы по группам и специальностям')
plt.xticks(index + bar_width, ('Группа 1', 'Группа 2', 'Группа 3', 'Группа 4', 'Группа 5'))
plt.legend()

plt.tight_layout()
plt.show()
