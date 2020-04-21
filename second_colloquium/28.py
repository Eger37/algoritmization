# 28. Знайти кількість парних елементів одновимірного масиву.
import numpy as np
import random
size = random.randint(1,100)
print(f"size: {size}")
a = np.random.randint(0, 1, size)
a = a[::2]
print(f"кількість парних елементів одновимірного масиву: {len(a)}")