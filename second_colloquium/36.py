# 36. Знайти суму додатніх елементів лінійного масиву цілих чисел.
# Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.

import numpy as np


def my_int_input(text_def):
    while True:
        try:
            input_num_def = int(input(text_def))
            break
        except ValueError:
            print('only digit')
    return input_num_def


a = np.zeros(10, int)
for i in range(10):
    a[i] = my_int_input(f"input number {i}: ")
print(f"Вхідний масив: {a}")

a = a[a >= 0]

print(f"масив додатніх елементів: {a}")
print(f"сума додатніх елементів лінійного масиву цілих чисел: {a.sum()}")
