'''
Відомі рік і номер місяця еародження людини, а також рік і номер місяця сьогоднішнього дня.
Визначити вік людини (число повних років і місяців). При визначенні числа повних місяців
дні місяця не враховувати, а використовувати різницю між номерами місяців. Наприклад, якщо
місяць народження - лютий, а поточний (сьогоднішній) місяць - травень, то число повних місяців
дорівнює трьом незалежно від дня народження і сьогоднішнього дня.
'''
days = range(1, 32)
months = range(1, 13)
years = range(1901, 2030)
while True:
    while True:
        try:
            d_born = int(input('day: '))
            if d_born not in days:
                print('Ми засуджуєм вашу кількість днів!')
                continue
            break
        except ValueError:
            print('ВІДРАХОВАНО')
    while True:
        try:
            m_born = int(input('months: '))
            if m_born not in months:
                print('Ми засуджуєм вашу кількість місяців!')
                continue
            break
        except ValueError:
            print('ВІДРАХОВАНО')
    while True:
        try:
            y_born = int(input('years: '))
            if y_born not in years:
                print('Ми засуджуєм ваш рік')
                continue
            break
        except ValueError:
            print('ВІДРАХОВАНО')
    if y_born % 4 == 0:
        february = 29
    else:
        february = 28
    months_list = [['Січень', 31], ['Лютий', february], ['Березень', 31], ['Квітень', 30], ['Травень', 31],
                   ['Червень', 30], ['Липень', 31],
                   ['Серпень', 31], ['Вересень', 30], ['Жовтень', 31], ['Листопад', 30], ['Грудень', 31]]
    if d_born > months_list[m_born - 1][1]:
        print(f'У цьому місяці {months_list[m_born - 1][1]} днів')
        continue

    while True:
        try:
            d = int(input('day: '))
            if d not in days:
                print('Ми засуджуєм вашу кількість днів!')
                continue
            break
        except ValueError:
            print('ВІДРАХОВАНО')
    while True:
        try:
            m = int(input('months: '))
            if m not in months:
                print('Ми засуджуєм вашу кількість місяців!')
                continue
            break
        except ValueError:
            print('ВІДРАХОВАНО')
    while True:
        try:
            y = int(input('years: '))
            if y not in years:
                print('Ми засуджуєм ваш рік')
                continue
            break
        except ValueError:
            print('ВІДРАХОВАНО')
    if y % 4 == 0:
        february = 29
    else:
        february = 28
    months_list = [['Січень', 31], ['Лютий', february], ['Березень', 31], ['Квітень', 30], ['Травень', 31],
                   ['Червень', 30], ['Липень', 31],
                   ['Серпень', 31], ['Вересень', 30], ['Жовтень', 31], ['Листопад', 30], ['Грудень', 31]]
    if d > months_list[m - 1][1]:
        print(f'У цьому місяці {months_list[m - 1][1]} днів')
        continue

    cd = d - d_born
    if cd < 1:
        m -= 1
        cd = months_list[m_born][1] - cd
    cm = m - m_born
    if cm < 1:
        y -= 1
        cm = 12 + cm
    cy = y - y_born
    print(f'days: {cd}, months: {cm}, years: {cy}')
    kek = input('Введіть щось для перезапуску, нічого - для завершення програми')
    if len(kek) >= 1:
        continue
    break
