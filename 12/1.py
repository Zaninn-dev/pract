import pandas as pd

students = pd.DataFrame({
    'Студент': ['Анна', 'Борис', 'Виктор', 'Галина', 'Дмитрий'],
    'Математика': [5, 4, 3, 5, 4],
    'Физика': [4, 5, 3, 5, 4],
    'Информатика': [5, 4, 4, 5, 3],
    'Посещаемость': [90, 85, 70, 95, 80]
})

print("Исходные данные:")
print(students.head(3))

print(students[students['Математика'] == students['Математика'].max()])

students['Средний_балл'] = students[['Математика', 'Физика', 'Информатика']].mean(axis=1)

students = students.sort_values(by='Средний_балл', ascending=False)
print(students)

print(students['Посещаемость'].mean())

print(students[students['Средний_балл']>4])