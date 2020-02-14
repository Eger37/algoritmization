# 2. За датою d, m, y визначити дату наступного і попереднього дня. В програмі врахувати
# наявність високосних років.
# Сугак Даниїл Васильович 1 курс група 122Б

from enum import Enum


class converter(Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4


while True:
    while True:
        try:
            x = float(input('amount of money: '))
            break
        except ValueError:
            print('Only numbers')
    while True:
        try:
            p = converter[input('currency: ')]
            break
        except (KeyError, ValueError):
            print('Only letters')

    if p.name == converter(1).name:
        UAH = x * 24.52
        print(UAH)
    elif p.name == converter(2).name:
        UAH = x * 26.6
        print(UAH)
    elif p.name == converter(3).name:
        UAH = x * 1.07
        print(UAH)
    elif p.name == converter(4).name:
        UAH = x * 6.27
        print(UAH)

    answer = input('Restart? Yes - 1. No - other.')
    if answer == '1':
        continue
    else:
        break
