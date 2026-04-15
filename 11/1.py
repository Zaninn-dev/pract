import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
print(df.head(10))
print(df.columns)
print(df.describe())
print(df.loc[1, 'PassengerId'])
print(df.shape[1], df.columns)
