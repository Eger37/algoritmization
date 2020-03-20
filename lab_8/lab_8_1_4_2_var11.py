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


def new_detail(num_def):
    detail_def = {"name": input(f"name of {num_def} detail (colour-number): "),
                  "count": my_input(f"count of {num_def} detail: "),
                  "consignment": input(f"consignment of {num_def} detail (date dd:mm:year): "),

                  }
    return detail_def


def new_detail_auto(num_def):
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
    detail_def = {"name": f'{colours_def[random.randint(1, 10)]}-{random.randint(1, 10)}',
                  "count": random.randint(0, 121),
                  "consignment": str(random.randint(1, 28)).zfill(
                      2) + ':' + str(random.randint(1, 12)).zfill(
                      2) + f':{random.randint(2018, 2020)}',
                  }
    return detail_def


while True:
    details = []
    cw = my_input('count of different detail: ')
    colours = ['red', 'yellow', 'blue', 'green', 'pink', 'white', 'brown', 'black', 'gray', ]
    for i in range(1, cw + 1):
        # details.append(new_detail(i))
        details.append(new_detail_auto(i))
    # details = [{'name': 'red-12', 'count': 3, 'consignment': '02:07:2019'},
    #            {'name': 'blue-25', 'count': 3, 'consignment': '06:07:2019'},
    #            {'name': 'blue-12', 'count': 4, 'consignment': '06:07:2019'},
    #            {'name': 'blue-1', 'count': 1, 'consignment': '06:07:2019'},
    #            {'name': 'blue-3', 'count': 7, 'consignment': '06:07:2019'},
    #            {'name': 'green-13', 'count': 67, 'consignment': '07:02:2019'}]

    print(details)
    while True:
        name = input(f"input name of detail (colour-number of (0, 10)): ")
        if len(name.split('-')) == 2:
            if name.split('-')[0] not in colours or my_int(name.split('-')[1]) not in range(0, 11):
                print('Invalid item entered!')
                continue
        else:
            print('Invalid item entered!!!')
            continue
        break
    while True:
        consignments = ''
        yes = input('enter "yes" if you are not interested in searching by batch number')
        if yes == 'yes':
            break
        consignments = input(f"input consignment of detail (date dd:mm:year; date dd:mm:year; ...): ")
        new_consignments = consignments.split('; ')
        tr = False
        for consignment in new_consignments:
            if len(consignment) != 10:
                print('batch number entered incorrectly!!!')
                tr = True
                break
            if len(consignment.split(':')) == 3:
                if (my_int(consignment.split(':')[0]) not in range(1, 29) or my_int(
                        consignment.split(':')[1]) not in range(
                    1, 13) or my_int(consignment.split(':')[2]) not in range(2018, 2021)):
                    print('batch number entered incorrectly!')
                    tr = True
                    break
            else:
                print('batch number entered incorrectly!')
                tr = True
                break
        if tr:
            continue
        break
    count = 0
    selected_details=[]
    for i in details:
        if i['name'] == name:
            if yes != 'yes' and i['consignment'] not in consignments:
                continue
            count += i['count']
            selected_details.append(i)
    print('selected_details: ')
    print(selected_details)
    print(f'count {count}')
    # max_of_year = 0
    # element = 0
    # for i in range(0, len(workers)):
    #     y = workers[i].get('date_of_born')
    #     if max_of_year < y:
    #         max_of_year = y
    #         element = i
    # print(workers[element])

    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
