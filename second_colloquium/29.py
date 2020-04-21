# 29. Знайти кількість парних елементів одновимірного масиву до першого
# зустрінутого числа рівного наперед заданому числу а.
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

if zadane in a:
    a = a[:(np.where(a == zadane))[0][0]:]
    a = a[::2]
    print(f"парні елементи масиву до першого входження числа {zadane}: {a}")
    print(f"кількість парних елементів одновимірного масиву до першого заданого числа: {len(a)}")
else:
    a = a[::2]
    print(f"парні елементи масиву: {a}")
    print(f"Задане число не знайдене")
    print(f"кількість парних елементів одновимірного масиву: {len(a)}")
