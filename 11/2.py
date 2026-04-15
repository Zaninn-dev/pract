import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
print(df[df['Survived']==1])
print(df[(df['Survived']==0) & (df['Sex']=='female')])
print(df[df['Pclass']==1])
print(df[df['Age']<18])
print(df.groupby(df['Survived']==1)['Age'].mean())