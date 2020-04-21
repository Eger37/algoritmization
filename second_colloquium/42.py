# 42. Підрахувати кількість елементів одновимірного масиву, для яких
# виконується нерівність i*i<ai<i!
import math

import numpy as np

a = np.array(
    [15, 19, -10, 10, -13, 18, -13, 14, 15, -18, 109, -10, 1000, -13, 18, -13, 14, 15, -18])
c = 0
for i in range(len(a)):
    if i * i < a[i] and a[i] < math.factorial(i):
        c += 1
print(c)
