# 26. Напишіть програму аналізу значень температури хворого за добу:
# визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
# температури виробляються шість раз на добу і результати вводяться з клавіатури у
# масив T.

import numpy as np


def my_int_input(text_def):
    while True:
        try:
            input_num_def = int(input(text_def))
            break
        except ValueError:
            print('only digit')
    return input_num_def


a = np.zeros(6, int)
for i in range(len(a)):
    a[i] = my_int_input(f"Введіть температуру {i+1} заміру: ")


print(f"Середнє значення температури: {np.average(a)}")
print(f"Мінімальне значення температури: {a.min()}")
print(f"Максимальне значення температури: {a.max()}")
