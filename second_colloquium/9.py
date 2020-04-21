import numpy as np


def my_int_input(text_def):
    while True:
        try:
            input_num_def = int(input(text_def))
            break
        except ValueError:
            print('only digit')
    return input_num_def


a = np.zeros(13, int)
for i in range(len(a)):
    a[i] = my_int_input(f"Введіть температуру о {i + 8} годині: ")

print(a)
print(f"година, о котрій було вперше зафіксовано від'ємну температуру: {(np.where(a < 0))[0][0] + 8}")
