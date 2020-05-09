# 2. Сформувати функцію, що визначатиме чи є задане натуральне число простим.
# Простим називається число, що більше за 1 та не має інших дільників, окрім 1 та самого
# себе).

# Сугак Даниїл Васильович 1 курс група 122Б

from memory_profiler import profile
from time import time


def my_int_input(text_def):  # моя функция ввода целых чисел
    while True:
        try:
            input_num_def = int(input(text_def))
            break
        except ValueError:
            print('only integer')
    return input_num_def


@profile  # счётчик памяти. Чтоб хоть что-то увидеть нужно большоё количество итераций, рекурсий...
def start_recursion(n_def):  # функция для того, чтоб легче считать память и выводит на экран результат проверки
    # на простоту
    hz_def = simplicity_test_recursion(n_def)
    if hz_def == n_def:
        print("число простое")
    if hz_def != n_def:
        print("число не простое")


def simplicity_test_recursion(n_def,
                              k_def=2):  # Функция для проверки числа на простоту рекурсивно, возващает белевое значение
    if n_def % k_def == 0:
        return k_def
    k_def += 1
    return simplicity_test_recursion(n_def, k_def)


@profile
def simplicity_test_iteration(n_def):  # Функция для проверки числа на простоту итеративно
    k_def = 2
    while n_def % k_def != 0:
        k_def += 1
    if k_def == n_def:
        print("число простое")
    if k_def != n_def:
        print("число не простое")


print("Функция для проверки числа на простоту рекурсией: ")
n = my_int_input("Введите число: ")

start = time()  # время во время старта
print(start_recursion(n))
stop = time()  # время во время остановки
print(f"Время роботы функции: {stop - start}\n")  # разница - это время работы этой фунции

print("Функция для проверки числа на простоту итеративно: ")
start = time()  # время во время старта
print(simplicity_test_iteration(n))
stop = time()  # время во время остановки
print(f"Время роботы функции: {stop - start}")  # разница - это время работы этой фунции

# Итеративный метод и быстрее и меньше памяти ест. Оба варианта не сложны в реализации.
# У рекурсии чуть меньше читабельность
