# 11. Інформація про кількість деталей на автоматизованому складі зберігається в
# комп'ютері; номенклатура деталей визначається розміром і кольором. Скласти
# програму, яка виводить на екран вибіркові відомості про кількість усіх деталей заданої
# номенклатури, а також, при бажанні, про терміни і кількості надходжень деталей цієї
# номенклатури в відповідних партіях. Якщо деталі даної номенклатури відсутні на складі,
# або сталася помилка при введенні номенклатури, то про це програма повинна
# повідомляти оператору.
# Сугак Даниїл Васильович 1 курс група 122Б
import random


def my_input(text_def):
    while True:
        try:
            input_num = int(input(text_def))
            break
        except ValueError:
            print('only digit')
    return input_num


def my_int(text_def):
    while True:
        try:
            input_num = int(text_def)
            break
        except ValueError:
            print('only digit')
    return input_num


def new_detail(num_def):  # функция добавления детали
    detail_def = {"name": input_detail_name(),
                  "count": my_input(f"count of {num_def} detail: "),
                  "consignment": input_detail_consignment(),

                  }
    return detail_def


def new_detail_auto(num_def):  # функция для автоматического добавления детали
    colours_def = {1: 'red',
                   2: 'yellow',
                   3: 'blue',
                   4: 'green',
                   5: 'pink',
                   6: 'orange',
                   7: 'white',
                   8: 'brown',
                   9: 'black',
                   10: 'gray',
                   }
    detail_def = {"name": f'{colours_def[random.randint(1, 10)]}-{random.randint(1, 10)}',# выходит, что существуе 100 разнообразных деталей
                  "count": random.randint(0, 121),# 120 - это максимально количество деталей
                  "consignment": str(random.randint(1, 28)).zfill(
                      2) + ':' + str(random.randint(1, 12)).zfill(
                      2) + f':{random.randint(2018, 2020)}', #могут сгенерироваться партии из будущего
                  }
    return detail_def


def input_detail_name():# функция ввода названия детали
    colours = ['red', 'yellow', 'blue', 'green', 'pink', 'white', 'brown', 'black',
               'gray', ]  # цвета, которые могут испльзоваться в названии деталей
    while True:
        name_def = input(f"Введите название детали (colour-number of (0, 10)): ")
        if len(name_def.split('-')) == 2:
            if name_def.split('-')[0] not in colours or my_int(name.split('-')[1]) not in range(0, 11):
                print('Invalid item entered!')
                continue
        else:
            print('Invalid item entered!!!')
            continue
        break
    return name_def


def input_detail_consignment():# функция ввода партии детали
    while True:
        consignment_def = input(
            f"Введите номер партии в виде даты (считать, что после 28 числа партии не отправляются (dd:mm:year)): ")
        # проверки ввода номера партии: (сюда лучше не углублятся, в месяце 28 дней;))
        if len(consignment_def) != 10:
            print('batch number entered incorrectly!!!')
            continue
        if len(consignment_def.split(':')) == 3:
            if (my_int(consignment_def.split(':')[0]) not in range(1, 29) or my_int(
                    consignment_def.split(':')[1]) not in range(
                1, 13) or my_int(consignment_def.split(':')[2]) not in range(2018, 2021)):
                print('batch number entered incorrectly!')
                continue
        else:
            print('batch number entered incorrectly!')
            continue
        break
    return consignment_def


while True:
    details = []
    yes = input('Введите "yes" если хотите самостоятельно ввести детали')
    cw = my_input('Количество записей: ') # если используется рандомная генерация, то для того, чтоб программа нашла вашу деталь по номеру партии
    # нужно ввести довольно большое число (порядка миллиона)
    if yes == 'yes':
        for i in range(1, cw + 1):
            details.append(new_detail(i))
    else:
        for i in range(1, cw + 1):
            details.append(new_detail_auto(i))
    print(details)  # вывод списка всех деталей
    print("Ведите название требуемой детали: ")
    name = input_detail_name()

    yes = input('Введите "yes" если вам не интересен поиск по партиям')
    consignments = []# список интересующих партий (не политических партий)
    if yes != 'yes':
        co_count = my_input("Введите количесво интересующих васпартий")
        for co in range(co_count):
            consignments.append(input_detail_consignment())
    count = 0# количесво деталей, которые нужно найти
    selected_details = [] # Список деталей удовлетворяющих параметры поиска
    for i in details:
        if i['name'] == name:# Сравнение по имени партии
            if yes != 'yes' and i['consignment'] not in consignments:# Сравнение по номеру партии
                continue
            count += i['count']
            selected_details.append(i)
    print('Выбранные детали: ')
    print(selected_details)
    print(f'Количество выбранных деталей {count}')

    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
