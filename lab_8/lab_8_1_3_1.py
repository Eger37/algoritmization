# 1. Напишіть програми, що виконують такі операції з масивами (використовувати
# вбудовані методи по роботі з масивами заборонено):
#  виведіть на екран елементи лінійного масиву (заданий користувачем) у
# зворотному порядку;
#  виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана
# користувачем).
#  виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
# Результати множення елементів занесіть до нової матриці та виведіть її на екран;
#  у матриці 4*4, що задана користувачем замініть всі від’ємні елементи на 0.
# Сугак Даниїл Васильович 1 курс група 122Б

import numpy as np


def my_input(text_def):
    while True:
        try:
            input_num = int(input(text_def))
            break
        except ValueError:
            print('only digit')
    return input_num


def input_array(number_of_columns_def=1, number_of_rows_def=1):
    array_def = np.zeros((number_of_rows_def, number_of_columns_def))
    i_def = 0
    while i_def != number_of_rows_def:
        j_def = 0
        while j_def != number_of_columns_def:
            new_element__def = my_input(f'значение элемента {i_def + 1} ряда, {j_def + 1} столбца: ')
            array_def[i_def, j_def] = new_element__def
            j_def += 1
        i_def += 1
    return array_def


def transpose_array(array_def):
    number_of_columns_def, number_of_rows_def = array_def.shape
    tr_array_def = np.zeros((number_of_rows_def, number_of_columns_def))
    i_def = 0
    while i_def != number_of_rows_def:
        j_def = 0
        while j_def != number_of_columns_def:
            new_element__def = array_def[j_def, i_def]
            tr_array_def[i_def, j_def] = new_element__def
            j_def += 1
        i_def += 1
    return tr_array_def


def matrix_multiplication(matrix_1_def, matrix_2_def):
    number_of_rows_1_def, number_of_columns_1_def = matrix_1_def.shape
    number_of_rows_2_def, number_of_columns_2_def = matrix_2_def.shape
    array_def = np.zeros((number_of_rows_1_def, number_of_columns_2_def))
    i_def = 0
    for n_def in matrix_1_def:
        col_count_def = -1
        while col_count_def != (number_of_columns_2_def - 1):
            col_count_def += 1
            b_def = -1
            z_def = 0
            for m_def in n_def:
                b_def += 1
                n_2_def = matrix_2_def[b_def]
                m_2_def = n_2_def[col_count_def]
                new_m_def = m_def * m_2_def
                z_def += new_m_def
            array_def[i_def, col_count_def] = z_def
            # print(b_def)
            # print(col_count_def)
        i_def += 1
    return array_def


while True:
    print(" виведіть на екран елементи лінійного масиву (заданий користувачем) у зворотному порядку;")
    g = my_input('count of elements: ')
    ar_1 = input_array(g)
    for k in range(ar_1.size - 1, -1, -1):
        print(ar_1[0, k])

    print(" виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана користувачем).")
    m = 3
    n = 3
    ar2 = input_array(n, m)
    ar2 = transpose_array(ar2)
    print(ar2)

    print(" виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність. Результати множення"
          " елементів занесіть до нової матриці та виведіть її на екран;")
    while True:
        number_of_rows_1 = my_input('введите количество рядов первой матрицы: ')
        number_of_columns_1 = my_input('введите количество столбцов первой матрицы: ')
        number_of_rows_2 = my_input('введите количество рядов второй матрицы: ')
        number_of_columns_2 = my_input('введите количество столбцов второй матрицы: ')

        if number_of_columns_1 != number_of_rows_2:
            print(
                'Ваши матрицы не перемножатся, ибо количество столбцов первой матрицы и количесво рядов второй '
                'матрицы не совпадают. Попробуйте перемножить другие матрицы')
            input('Нажимите Enter, чтобы продолжить')
            continue
        print('\nВвод первой матрицы: \n')
        matrix_1 = input_array(number_of_columns_1, number_of_rows_1)
        print('\nВвод второй матрицы: \n')
        matrix_2 = input_array(number_of_columns_2, number_of_rows_2)

        matrix_3 = matrix_multiplication(matrix_1, matrix_2)
        print('Результат умножения ваших матриц: ')
        print(matrix_3)
        break

    print(" у матриці 4*4, що задана користувачем замініть всі від’ємні елементи на 0.")
    m = 4
    n = 4
    ar4 = input_array(n, m)
    i = 0
    while i != n:
        j = 0
        while j != m:
            if ar4[i, j] < 0:
                ar4[i, j] = 0
            j += 1
        i += 1
    print(ar4)
    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
