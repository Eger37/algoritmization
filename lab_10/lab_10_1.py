# 1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
# натурального числа n.

# Сугак Даниїл Васильович 1 курс група 122Б
from memory_profiler import profile
from time import time
import sys


def my_int_input(text_def):  # моя функция ввода целых чисел
    while True:
        try:
            input_num_def = int(input(text_def))
            break
        except ValueError:
            print('only integer')
    return input_num_def


@profile  # счётчик памяти. Чтоб хоть что-то увидеть нужно большоё количество итераций, рекурсий...
def start_factorial_recursion(n_def):  # функция для того, чтоб легче считать память
    return factorial_recursion(n_def)


def factorial_recursion(n_def):  # функция для поиска факториала при помощи рекурсии
    if n_def == 0:
        return 1
    sys.setrecursionlimit(sys.getrecursionlimit() + 1)  # увеличивает лимит рекурсий
    return factorial_recursion(n_def - 1) * n_def


@profile
def factorial_iteration(n_def):  # функция для поиска факториала при помощи итераций
    factorial_def = 1
    for i in range(2, n_def + 1):
        factorial_def *= i
    return factorial_def


print("Запуск функции для поиска факториала при помощи рекурсии: ")
n = my_int_input("Введите число: ")

start = time()  # время во время старта
print(start_factorial_recursion(n))
stop = time()  # время во время остановки
print(f"Время роботы функции: {stop - start}\n")  # разница - это время работы этой фунции
print("Запуск функции для поиска факториала при помощи итераций: ")
start = time()  # время во время старта
print(factorial_iteration(n))
stop = time()  # время во время остановки
print(f"Время роботы функции: {stop - start}")  # разница - это время работы этой фунции

# Итерационный метод потребляет меньше памяти, но рекурсия работает быстрее. Обе реализации простые, но читабельность у рекусии больше.
