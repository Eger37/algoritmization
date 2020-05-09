# 3. Сформувати функцію для переведення натурального числа з десяткової системи
# числення у шістнадцятирічну.

# Сугак Даниїл Васильович 1 курс група 122Б

from memory_profiler import profile
from time import time
import sys

letter_for_16 = '0123456789ABCDEF'


def my_int_input(text_def):  # моя функция ввода целых чисел
    while True:
        try:
            input_num_def = int(input(text_def))
            break
        except ValueError:
            print('only integer')
    return input_num_def


@profile
def start_recursion(n_def):
    string_num_in_16_def = ''
    n_def, string_num_in_16_def = ten_to_sixteen_recursion(n_def, string_num_in_16_def)

    print(string_num_in_16_def[::-1])


def ten_to_sixteen_recursion(n_def,
                             string_num_in_16_def):  # Функция для перевода чисел из десятичной в шеснадцатиричную систему счисления
    # при помощи рекурсии
    k = n_def % 16
    string_num_in_16_def += letter_for_16[k]
    n = n_def // 16
    if n == 0:
        return n, string_num_in_16_def
    else:
        sys.setrecursionlimit(sys.getrecursionlimit() + 1)  # зміна межі рекурсії
        return ten_to_sixteen_recursion(n, string_num_in_16_def)


@profile
def ten_to_sixteen_iteration(n_def):  # Функция для перевода чисел из десятичной в шеснадцатиричную систему счисления
    # при помощи итераций
    string_num_in_16_def = ''
    while True:
        k = n_def % 16
        string_num_in_16_def += letter_for_16[k]
        n_def = n_def // 16
        if n_def == 0:
            break
    print(string_num_in_16_def[::-1])


print("Функция для перевода чисел из десятичной в шеснадцатиричную систему счисления при помощи рекурсии: ")

n = my_int_input("Введите число: ")

start = time()  # время во время старта
print(start_recursion(n))
stop = time()  # время во время остановки
print(f"Время роботы функции: {stop - start}\n")  # разница - это время работы этой фунции

print("Функция для перевода чисел из десятичной в шеснадцатиричную систему счисления при помощи итераций: ")
start = time()  # время во время старта
print(ten_to_sixteen_iteration(n))
stop = time()  # время во время остановки
print(f"Время роботы функции: {stop - start}")  # разница - это время работы этой фунции

# Итерационный метод ест меньше памяти, а рекурсия быстрее. Читабельность одинаковая. Реализация интереснее
# и чуть сложнее у рекурсии
