# 2. Задача полягає у вивченні і реалізації алгоритмів пошуку для даних, підготовлених
# за допомогою функції моделювання випадкових чисел і текстів, підготовлених
# самостійно.
# Для кожного алгоритму необхідно підготувати тести, що підтверджують
# працездатність програми. Для всіх алгоритмів пошуку повинні бути приведені лістинги
# програм пошуку та лістинги результатів (номера позиції в вихідному масиві, починаючи
# з якого розташований елемент або фрагмент пошуку; кількості порівнянь по кожному
# алгоритму пошуку).
# Найпростіші алгоритми пошуку:
#  лінійний пошук;
#  бінарний пошук;
#  прямий пошук підрядка.
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


def line_search(a_def, x_def):
    print("array :")
    print(a_def)
    i_def = 0
    g_def = len(a_def)
    counter_def = 0
    while i_def < g_def and a_def[i_def] != x_def:
        counter_def += 2
        i_def += 1
    if i_def == g_def:
        print('Item', x_def, 'not found.')
        print('number of comparisons:', counter_def)
    else:
        print('Item', x_def, 'first found in position', i_def)
        print('number of comparisons:', counter_def)


def binary_search(a_def, x_def):
    a_def.sort()# сортировка массива
    g_def = len(a_def)
    print("array :")
    print(a_def)
    i = 0
    L = 0
    R = g_def - 1
    flag = True
    counter_def = 0
    while L <= R and flag:
        i += 1
        K = (L + R) // 2
        if a_def[K] == x_def:
            counter_def += 2
            print('Item', x_def, 'first found in position', K)
            print('number of comparisons:', counter_def)
            flag = False
        elif a_def[K] < x_def:
            counter_def += 3
            L = K + 1
        elif a_def[K] > x_def:
            counter_def += 4
            R = K - 1
    if flag:
        print('Item', x_def, 'not found.')
        print('number of comparisons:', counter_def)


def patter_search(text_def, pattern_def):
    i = -1
    j = 0
    counter_def = 0
    while (j < len(pattern_def)) and i < (len(text_def) - len(pattern_def)):
        counter_def += 2
        j = 0
        i += 1
        while j < len(pattern_def) and pattern_def[j] == text_def[i + j]:
            counter_def += 2
            j += 1
    if j == len(pattern_def):
        print('Pattern', pattern_def, 'first found in position', i)
    else:
        print('Item', pattern_def, 'not found.')
    print('number of comparisons:', counter_def)


while True:
    print(" лінійний пошук:\n")
    quesh = input(
        "Введите 'yes', если хотите ввести данные самостоятельно, в противном случае будет использоваться программная генерация: ")
    if quesh == 'yes':
        g = my_input('count of elements: ')  # длина массива
        x = my_input('required element: ')  # искомый элемент
        a = np.zeros(g, dtype=int)
        print("Ввод массива:")
        for i in range(g):
            a[i] = my_input("Введите целое число: ")
        line_search(a, x)  # вызов функции линейного поиска
    # g = my_input('count of elements: ')
    # x = my_input('required element (int 0-100): ')
    else:
        # Искомый элемент не присутсвует в массиве
        g = 20  # длина массива
        x = 15  # искомый элемент
        last = 15
        a = np.random.randint(0, last, g)  # (start, stop, len) генерация рандомного массива
        line_search(a, x)  # вызов функции линейного поиска
        print()
        # Искомый элемент присутсвует в массиве
        g = 20  # длина массива
        x = 2  # искомый элемент
        last = 10
        a = np.random.randint(0, last, g)  # (start, stop, len) генерация рандомного массива
        a[-1] = x
        line_search(a, x)  # вызов функции линейного поиска

    print("\n бінарний пошук:\n")
    quesh = input(
        "Введите 'yes', если хотите ввести данные самостоятельно, в противном случае будет использоваться программная генерация: ")
    if quesh == 'yes':
        g = my_input('count of elements: ')  # длина массива
        x = my_input('required element: ')  # искомый элемент
        a = np.zeros(g, dtype=int)
        print("Ввод массива:")
        for i in range(g):
            a[i] = my_input("Введите целое число: ")
        binary_search(a, x)# вызов функции бинарного поиска
    # g = my_input('count of elements: ')
    # x = my_input('required element (int 0-100): ')
    else:
        g = 20
        x = 12
        last = 10
        a = np.random.randint(0, last, g)  # (start, stop, len) генерация рандомного массива
        binary_search(a, x)# вызов функции бинарного поиска
        print()
        g = 20
        x = 2
        last = 10
        a = np.random.randint(0, last, g)  # (start, stop, len) генерация рандомного массива
        binary_search(a, x)# вызов функции бинарного поиска



    print("\n прямий пошук підрядка:\n")
    quesh = input(
        "Введите 'yes', если хотите ввести данные самостоятельно, в противном случае будет использоваться программная генерация: \n")
    if quesh == 'yes':
        text = input("Введите строку")
        pattern = input("Введите подстроку, которую нужно найти")
        patter_search(text, pattern)
    else:
        # Искомая подстрока присутсвует в строке
        text = "мама мыла раму"
        pattern = "раму"
        patter_search(text, pattern)
        print()
        # Искомая подстрока не присутсвует в строке
        pattern = "мамка"
        patter_search(text, pattern)
    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
