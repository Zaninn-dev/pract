import numpy as np

zet = np.array([1,2,0,0,4,0])

for i in range(len(zet)):
    if zet[i] == 0:
        print(i)
