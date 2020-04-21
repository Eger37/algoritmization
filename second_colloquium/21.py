# 21. Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
# числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
# від 50 до 100.

import numpy as np


def my_float_input(text_def):
    while True:
        try:
            input_num_def = float(input(text_def))
            break
        except ValueError:
            print('only float')
    return input_num_def


zadane_chchislo = my_float_input(f"Введіть ціле число: ")
a = np.random.uniform(low=50, high=100, size=(20,))
print(a)
a = a[a < zadane_chchislo]
# print(a)
print(a.prod())
