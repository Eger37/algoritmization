# 43. Задано два натуральних числа a і b. Змінній w привласнити значення
# істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
# і не кратний b.
import numpy as np
import random
a=4
b=5
size = random.randint(1, 100)
# size = 10
print(f"size: {size}")
ar = np.random.randint(-100, 100, size)
print(f"Вхідний масив: {ar}")
w = np.any(np.logical_and(a % a == 0, a % b != 0))
print(f"t: {w}")
