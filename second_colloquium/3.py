import numpy as np

a = np.array(['Петров', 'Иванов', 'Штейн', 'Кобейн', 'Вейн', 'Румпельштильцхен'])
for i in range(len(a)-1,-1,-1):
    print(a[i])