import numpy as np


def my_int_input(text_def):
    while True:
        try:
            input_num_def = int(input(text_def))
            break
        except ValueError:
            print('only digit')
    return input_num_def


a = np.zeros(5, int)
for i in range(len(a)):
    a[i] = my_int_input(f"input number {i}: ")

# a = np.array([1, 2, 3, 4, 5])
for i in range(len(a)):
    print(f"Корінь від {a[i]}: {np.sqrt(a[i])}")
    print(f"Квадрат від {a[i]}: {np.square(a[i])}")
    print()
