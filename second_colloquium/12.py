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
    a[i] = my_int_input(f"Введіть температуру  {i + 1} дня: ")

print(a)
av = np.average(a)
print(f"Днів придатних для купання (температура води від 17 градусів по Цельсію): {len(a[a > av])}")
