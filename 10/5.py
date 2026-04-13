import matplotlib.pyplot as plt

weight1 = [64, 55.8, 61.2, 60.45, 61]
height1 = [113.7, 157.7, 136, 148.9, 125.3]

weight2 = [61.9, 64, 62.1, 62.4, 63.6]
height2 = [135.1, 182.2, 195.9, 165.1, 125.1]

weight3 = [71.3, 70.8, 70, 71.1, 71.7]
height3 = [165.8, 192.8, 161.4, 181.1, 177.3]


plt.figure(figsize=(8, 6))

plt.scatter(weight1, height1, color='red', marker='o', label='Группа 1')
plt.scatter(weight2, height2, color='green', marker='s', label='Группа 2')
plt.scatter(weight3, height3, color='blue', marker='^', label='Группа 3')

plt.title('Соотношение массы и роста по группам')
plt.xlabel('Масса (кг)')
plt.ylabel('Рост (см)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6) 

plt.show()