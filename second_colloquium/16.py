import numpy as np

a = np.random.randint(10, 51, 15)
print(a)
a = a[a % 7 == 0]
# print(a)
print(a.prod())
