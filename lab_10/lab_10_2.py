# 2. Сформувати функцію для обчислення цифрового кореню натурального числа.
# Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
# числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
# сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
# числа.

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
def start_cortex_recursion(n_def):  # функция для того, чтоб легче считать память
    return start_cortex_recursion(n_def)


def sum_recursion(n_def):  # Функция для нахождение суммы цифр в числе при помощи рекурсии
    if n_def < 10:
        return n_def
    k_def = n_def % 10 + sum_recursion(n_def // 10)
    return k_def


def start_cortex_recursion(n_def):  # Функуция нахождение цифрового корня при помощи рекурсии
    if n_def < 10:
        return n_def
    k_def = start_cortex_recursion(sum_recursion(n_def))
    return k_def


@profile
def cortex_iteration(n_def):  # Функция нахождение цифрового корня при помощи итераций
    str_digit_def = str(n_def)
    while len(str_digit_def) > 1:
        n_def = 0
        for i in str_digit_def:
            n_def = n_def + int(i)
        str_digit_def = str(n_def)
    return str_digit_def


print("нахождение цифрового корня при помощи рекурсии: ")
n = my_int_input("Введите число: ")

start = time()  # время во время старта
print(start_cortex_recursion(n))
stop = time()  # время во время остановки
print(f"Время роботы функции: {stop - start}\n")  # разница - это время работы этой фунции
print("нахождение цифрового корня при помощи рекурсии: ")
start = time()  # время во время старта
print(cortex_iteration(n))
stop = time()  # время во время остановки
print(f"Время роботы функции: {stop - start}")  # разница - это время работы этой фунции

# Итеративный метод требует меньше памяти, но медленее, чем рекурсия. Рекурсия читабельнее. Реализация рекурсии проще,
# но пришлось немного подумать, а над итеративный метод можно не думать, но писать дольше.
