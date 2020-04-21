import numpy as np

a = np.random.randint(100, 201, 20)
print(a)
a = a[::2]
print(np.sum(a))
