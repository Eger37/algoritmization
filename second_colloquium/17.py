import numpy as np

a = np.random.uniform(low=100, high=200, size=(20,))
print(a)
a = a[1::2]
# print(a)
print(np.sum(a))
