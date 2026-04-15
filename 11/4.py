import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
df['child'] = df['Age'] < 18
print(df.groupby('Pclass')['Survived'].mean() * 100)
print(df.groupby('child')['Survived'].mean().idxmax())
print(df[df['Survived'] == 1]['Embarked'].value_counts)
print(pd.crosstab(df['Sex'], df['Survived']))