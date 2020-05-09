# 3. Сформувати функцію для обчислення індексу максимального елемента масиву
# n*n, де 1<=n<=5.

# Сугак Даниїл Васильович 1 курс група 122Б

from memory_profiler import profile
from time import time
import sys
from random import randint


@profile  # счётчик памяти. Чтоб хоть что-то увидеть нужно большоё количество итераций, рекурсий...
def start_recursion(n_def):  # функция для того, чтоб легче считать память
    return looking_for_idx_of_max_recursion(n_def)


def looking_for_idx_of_max_recursion(arr_def, i_def=0, j_def=0, i_of_max_def=0,
                                     j_of_max_def=0):  # Функция для поиска индексов максимального елемента в двумерном масиве рекурсивно
    if j_def == len(arr_def[i_def]):
        i_def += 1  # индекс ряда
        j_def = 0  # индекс столбца
    if i_def == len(arr_def):  # если индекс ряда выйдет за пределы массива, списка
        return i_of_max_def, j_of_max_def
    if arr_def[i_def][j_def] > arr_def[i_of_max_def][j_of_max_def]:  # сравнение
        i_of_max_def = i_def  # индекс ряда макс элемента
        j_of_max_def = j_def  # индекс столбца макс элемента
    j_def += 1
    sys.setrecursionlimit(sys.getrecursionlimit() + 1)  # увеличивает лимит рекурсий
    return looking_for_idx_of_max_recursion(arr_def, j_def, j_def, i_of_max_def, j_of_max_def)


@profile
def looking_for_idx_of_max_iteration(
        arr_def):  # Функция для поиска индексов максимального елемента в двумерном масиве итеративно
    i_of_max_def = 0  # индекс ряда макс элемента
    j_of_max_def = 0  # индекс столбца макс элемента
    i_def = 0
    while i_def != len(arr_def):
        j_def = 0
        while j_def != len(arr_def[i_def]):
            if arr_def[i_def][j_def] > arr_def[i_of_max_def][j_of_max_def]:
                i_of_max_def, j_of_max_def = i_def, j_def
            j_def += 1
        i_def += 1
    return i_of_max_def, j_of_max_def


n = randint(1, 5)
a = []  # генерация списка при помощи рандома
for i in range(n):
    a_in = []
    for j in range(n):
        a_in.append(randint(-10, 11))
    a.append(a_in)
print("Рандомний список, матрица n*n елементов: ", a, "\n")

print("Функция для поиска индексов максимального елемента в двумерном масиве рекурсивно: ")
start = time()  # время во время старта
print(start_recursion(a))
stop = time()  # время во время остановки
print(f"Время роботы функции: {stop - start}\n")  # разница - это время работы этой фунции

print("Функция для поиска индексов максимального елемента в двумерном масиве итеративно: ")
start = time()  # время во время старта
print(looking_for_idx_of_max_iteration(a))
stop = time()  # время во время остановки
print(f"Время роботы функции: {stop - start}")  # разница - это время работы этой фунции
# Итеративный метод требует меньше памяти, а рекурсия быстрее. У цикла больше читабельность и его проще реализовать,
# но рекурсия круче.
