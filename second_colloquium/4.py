import numpy as np

a = np.array(['Петров', 'Иванов', 'Штейн', 'Кобейн', 'Вейн', 'Румпельштильцхен'])
first_letter = input("Введіть першу літеру: ")
for i in a:
    if i[0] == first_letter:
        print(i)
