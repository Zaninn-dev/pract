import numpy as np

array = np.full((8, 8), 1, dtype=int)

array[0::2, 1::2] = 5
array[1::2, 0::2] = 5

print(array)