# 59. Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
# чисел в ньому.
import numpy as np

a = np.random.randint(0, 10, 10)
print(a)
a = np.unique(a)
print(len(a))