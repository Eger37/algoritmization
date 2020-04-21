# 18. Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
# масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.
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
for i in range(len(a)):
    a[i] = my_int_input(f"Введіть ціле число: ")

a = a[a < 0]
# print(a)
print(a.prod())
