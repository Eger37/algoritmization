# 41. Змінній t привласнити значення істина, якщо максимальний елемент
# одновимірного масиву єдиний і не перевищує наперед заданого числа а.

import numpy as np
import random


def my_int_input(text_def):
    while True:
        try:
            input_num_def = int(input(text_def))
            break
        except ValueError:
            print('only digit')
    return input_num_def


zadane = my_int_input("Введіть число: ")
size = random.randint(1, 100)
# size = 10
print(f"size: {size}")
a = np.random.randint(0, 100, size)
print(f"Вхідний масив: {a}")

m = a.max()
a[(np.where(a == m))[0][0]] = a.min()

t = True
if m > zadane or m == a.max():
    t = False
print(f"t: {t}")
