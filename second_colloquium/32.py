# 32. Змінній t привласнити значення істина, якщо в одновимірному масиві є
# хоча б одне від’ємне і парне число.
import numpy as np
import random

size = random.randint(1, 100)
# size = 10
print(f"size: {size}")
a = np.random.randint(-100, 100, size)
print(f"Вхідний масив: {a}")
t = np.any(np.logical_and(a < 0, a % 2 == 0))
print(f"t: {t}")
