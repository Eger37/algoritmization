# 31. Обчислити середнє арифметичне значення тих елементів одновимірного
# масиву, які потрапляють в інтервал від -2 до 10.
import numpy as np
import random

size = random.randint(1, 100)
# size = 10
print(f"size: {size}")
a = np.random.randint(0, 100, size)
print(f"Вхідний масив: {a}")

a = a[a > -2]
a = a[a < 10]
print(
    f"середнє арифметичне значення тих елементів одновимірного масиву, які потрапляють в інтервал від -2 до 10: {np.average(a)}")