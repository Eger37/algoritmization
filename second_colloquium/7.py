import numpy as np

a = np.random.randint(-20, 11, 12)
print(a)
for i in range(len(a)):
    if a[i] < 0:
        a[i] = 0
print(a)
