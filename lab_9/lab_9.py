# Реалізувати програму, в якій кожен з алгоритмів сортування оформити як окрему
# функцію. Проілюструвати механізм використання параметрів різних типів. Забезпечити
# підрахунок числа необхідних порівнянь, числа обмінів і часу роботи кожної функції,
# сформувавши функції оцінки ефективності методів сортування. Підготувати єдині для
# всіх алгоритмів тестові вихідні дані:
# • згенерована послідовність псевдовипадкових чисел, достатня для оцінки
# швидкості роботи алгоритму сортування (близько 100000 цілих чисел);
# • вихідна послідовність псевдовипадкових чисел, відсортована будь-яким методом
# в порядку зростання;
# • вихідна послідовність псевдовипадкових чисел, відсортована будь-яким методом
# в порядку за спаданням;
# • забезпечити програмну можливість вибору введення вихідних даних з клавіатури
# до 30 вихідних чисел.
# Для програми привести лістинг з результати роботи:
# • вихідний масив (вивести на екран для випадку введення вихідних даних з
# клавіатури);
# • відсортований масив (для випадку введення вихідних даних з клавіатури один
# екземпляр відсортованого масиву вивести на екран);
# • показники функції оцінки ефективності методів сортування (вивести на екран).

# Виконати сортування масиву цілих чисел Ai,i = 0,N −1 в порядку зростання / за спаданням елементів.

# Найпростіші алгоритми сортування:
# • сортування бульбашкою (bubble sort);
# • сортування вибором (selection sort);
# • сортування вставками (insertion sort).
# Сугак Даниїл Васильович 1 курс група 122Б
from random import randint
from time import time


def my_int_input(text_def):  # моя функция ввода целых чисел
    while True:
        try:
            input_num_def = int(input(text_def))
            break
        except ValueError:
            print('only integer')
    return input_num_def


def bubble_sort(a_copy, up=True):  # сортировка пузырьком
    a_copy = a_copy[:]  # копирование списка, чтоб работать с копией
    comparisons = 0  # количество сравнений
    exchanges = 0  # количество обменов
    for i in range(len(a_copy) - 1):  # цикл проходится по всему списку, кроме последнего элемента
        for j in range(len(a_copy) - i - 1):  # цикл проходится по всему списку, кроме последнего элемента
            if a_copy[j] > a_copy[j + 1]:  # если следующий элемент меньше, то элементы меняются
                a_copy[j + 1], a_copy[j] = a_copy[j], a_copy[j + 1]
                exchanges += 2
            comparisons += 1
    if not up:  # проверяет в каком направлении сортировка
        a_copy = a_copy[::-1]  # если сортировка от большего к меньшему, то просто разворачивает список
    comparisons += 1
    print(f"Число порівнянь: {comparisons}")
    print(f"Число обмінів: {exchanges}")
    return a_copy


def selection_sort(a_copy, up=True):  # сортировка выбором
    a_copy = a_copy[:]  # копирование списка, чтоб работать с копией
    comparisons = 0  # количество сравнений
    exchanges = 0  # количество обменов
    for i in range(len(a_copy)):
        idx_min = i  # минимальный элемент, точнее его индекс
        for j in range(i + 1, len(a_copy)):  # цикл для поиска минимального элемента
            if a_copy[j] < a_copy[idx_min]:
                idx_min = j
            comparisons += 1
        a_copy[i], a_copy[idx_min] = a_copy[idx_min], a_copy[
            i]  # минимальный элемент перемещается влево
        exchanges += 2
    if not up:  # проверяет в каком направлении сортировка
        a_copy = a_copy[::-1]  # если сортировка от большего к меньшему, то просто разворачивает список
    comparisons += 1
    print(f"Число порівнянь: {comparisons}")
    print(f"Число обмінів: {exchanges}")
    return a_copy


def insertion_sort(a_copy, up=True):  # сортировка вставками
    a_copy = a_copy[:]  # копирование списка, чтоб работать с копией
    comparisons = 0  # количество сравнений
    exchanges = 0  # количество обменов
    for i in range(len(a_copy)):
        k = a_copy[i]  # вспомагательная переменная для временного хранения элемента
        j = i
        while (a_copy[j - 1] > k) and (
                j > 0):  # цикл для сдвига ячеек, пока не будет найдена подходящая
            a_copy[j] = a_copy[j - 1]
            j = j - 1
            comparisons += 2
            exchanges += 1
        comparisons += 2
        a_copy[j] = k  # обмен значений
        exchanges += 2
    if not up:  # проверяет в каком направлении сортировка
        a_copy = a_copy[::-1]  # если сортировка от большего к меньшему, то просто разворачивает список
    comparisons += 1
    print(f"Число порівнянь: {comparisons}")
    print(f"Число обмінів: {exchanges}")
    return a_copy


way = input("Введіть \"skip\", якщо ви не хочете вводити значення з клавіатури: ")
if "skip" != way:  # ручной ввод списка
    while True:
        stop = my_int_input("Введіть довжину списку: ")
        if stop > 30:
            print("список дуже довгий (максимальна довжина 30)!")
            continue
        break
    a = []
    for i in range(stop):
        a.append(my_int_input(f"Введіть наступне значення: "))
    print("Список:", a)
else:  # рандомна генерация списка
    a = []
    count_of_element = 10000  # длина этого списка
    for i in range(count_of_element):
        a.append(randint(0, 1000))

print("\n• сортування бульбашкою (bubble sort):")
print("В порядку зростання:")
start = time()  # время во время старта
a_output = bubble_sort(a)
stop = time()  # время во время остановки
print(f"Час роботи функції: {start - stop}")  # разница - это время работы этой фунции

print("\nЗа спаданням елементів:")
start = time()  # время во время старта
a_output = bubble_sort(a, up=False)
stop = time()  # время во время остановки
print(f"Час роботи функції: {start - stop}")  # разница - это время работы этой фунции

print("\n• сортування вибором (selection sort):")
print("В порядку зростання:")
start = time()  # время во время старта
a_output = selection_sort(a)
stop = time()  # время во время остановки
print(f"Час роботи функції: {start - stop}")  # разница - это время работы этой фунции

print("\nЗа спаданням елементів:")
start = time()  # время во время старта
a_output = selection_sort(a, up=False)
stop = time()  # время во время остановки
print(f"Час роботи функції: {start - stop}")  # разница - это время работы этой фунции

print("\n• сортування вставками (insertion sort):")
print("В порядку зростання:")
start = time()  # время во время старта
a_output = insertion_sort(a)
stop = time()  # время во время остановки
print(f"Час роботи функції: {start - stop}")  # разница - это время работы этой фунции

print("\nЗа спаданням елементів:")
start = time()  # время во время старта
a_output = insertion_sort(a, up=False)
stop = time()  # время во время остановки
print(f"Час роботи функції: {start - stop}")  # разница - это время работы этой фунции

if "skip" != way:
    print(f"Відсортований список: {a_output}")
