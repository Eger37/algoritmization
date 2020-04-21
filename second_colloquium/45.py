# 45. Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
# яка містить довжини опор, які встановлюються через кожні R / 5 м.
import math


# from sympy import symbols, S

# import numpy as np
def my_int_input(text_def):
    while True:
        try:
            input_num_def = int(input(text_def))
            break
        except ValueError:
            print('only digit')
    return input_num_def


r = my_int_input("Введіть радіус криші R: ")
# dx = S(r) / S(5)
dx = r / 5
x = 0
i = 0
table = []
while x < 2 * r - dx:
    x = x + dx
    i += 1
    h = math.sqrt(x * (2 * r - x))
    table.append([i, h])
    # print(i, ' = ', h)

for l in table:
    print(f"Опора {l[0]} = {l[1]} М")
