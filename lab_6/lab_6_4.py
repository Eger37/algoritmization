# 4. Робота світлофора для водіїв запрограмована таким чином: на початку кожної
# години протягом трьох хвилин горить зелений сигнал, потім протягом однієї хвилини -
# жовтий, протягом двох хвилин - червоний, протягом трьох хвилин - знову зелений і т. д.
# Розробити програму, яка вводить дійсне число t, що означає час в хвилинах, що
# минув з початку чергової години і визначає сигнал якого кольору горить для водіїв в цей
# момент.
# Сугак Даниїл Васильович 1 курс група 122Б

while True:
    while True:
        try:
            t = float(input('time: '))
            break
        except ValueError:
            print('only float')
    t %= 6
    if t < 3:
        print("горит зелёный")
    elif t < 4:
        print("горит жёлтый")
    else:
        print("горит красный")
    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
