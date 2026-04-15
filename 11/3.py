import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
df['child'] = df['Age'] < 18
print(df['child'])
df['famaly_size'] = df['SibSp'] + df['Parch'] + 1
print(df['famaly_size'])
def xz(a):
    if a < 12:
        return 'child'
    elif 13 < a < 19:
        return 'Teen'
    elif 20 < a < 59:
        return 'Adult'
    else:
        return 'senior'
df['age_group'] = df['Age'].apply(xz)
print(df['age_group'])