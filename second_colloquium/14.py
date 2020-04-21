import numpy as np

a = np.zeros(10)
print(a)
g = 9.81
for i in range(10):
    a[i] = (np.square(i + 1) * g) / 2
print(a)
