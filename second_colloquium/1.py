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
# print(f"Масив: {a}")
print("Масив: ")
for i in range(len(a)):
    if i == len(a) - 1:
        print(a[i], end="\n")
    else:
        print(a[i], end=", ")
print(f"Середнє значення масиву: {np.average(a)}")
