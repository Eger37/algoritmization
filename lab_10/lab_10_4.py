# 1. Сформувати функцію для введення з клавіатури послідовності чисел і виведення
# її на екран у зворотному порядку (завершаючий символ послідовності – крапка)

# Сугак Даниїл Васильович 1 курс група 122Б

from memory_profiler import profile
from time import time
import sys


@profile  # счётчик памяти. Чтоб хоть что-то увидеть нужно большоё количество итераций, рекурсий...
def start_recursion():  # функция для того, чтоб легче считать память
    return input_list_recursion()


def input_list_recursion():  # функция ввода чисел и вывода их в обратном порядке при помощи рекурсии
    n_def = input("Введите число, если введёте точку, то ввод завершиться: ")
    if n_def != ".":
        try:
            n_def = int(n_def)
        except ValueError:
            print("Вы ввели не число!")
        sys.setrecursionlimit(sys.getrecursionlimit() + 1)  # увеличивает лимит рекурсий
        input_list_recursion()
    print(n_def)


@profile
def input_list_iteration():  # функция ввода чисел и вывода их в обратном порядке при помощи итераций
    l_def = []  # создаём пустой список, куда будем закидывать елементы
    while True:
        switch_def = False

        while True:
            try:
                n_def = input("Введите число, если введёте точку, то ввод завершиться: ")
                if n_def == ".":
                    switch_def = True
                    break
                n_def = int(n_def)
                break
            except ValueError:
                print("Вы ввели не число!")

        l_def.append(n_def)
        if switch_def:
            break

    l_def = l_def[::-1]  # разворачиваем список
    # for i in range(len(l_def) - 1, -1, -1):
    #     print(l_def[i])
    for i in l_def:  # выводим список
        print(i)


print("# функция ввода чисел и вывода их в обратном порядке при помощи рекурсии: ")
start = time()  # время во время старта
start_recursion()
stop = time()  # время во время остановки
print(f"Время роботы функции: {stop - start}\n")  # разница - это время работы этой фунции

print("# функция ввода чисел и вывода их в обратном порядке при помощи итераций: ")
start = time()  # время во время старта
input_list_iteration()
stop = time()  # время во время остановки
print(f"Время роботы функции: {stop - start}")  # разница - это время работы этой фунции

# если процесс ввода автоматизировать, то рекурсия работает быстрее. Цикл юзает меньше памяти.
# Цикл не читабелен, нужно было с другого сайта его списывать ;)
# Рекурсию делал сам и её проще и интереснее делать
