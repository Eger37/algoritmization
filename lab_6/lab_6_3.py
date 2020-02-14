# 3. Значення змінної x, що позначає деяку суму грошей в валюті p, замінити величиною
# цієї ж суми в гривнях.
# Сугак Даниїл Васильович 1 курс група 122Б
from enum import Enum


class Month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class Season(Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4


print(Season.Winter)

while True:
    while True:
        try:
            m = Month[input('month: ')]
            break
        except KeyError:
            print('wrong month')
    v = (m.value // 3 + 1) % 4
    print(Season(v))
    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
