# 39. Дані про температуру повітря і кількості опадів за декаду квітня
# зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
# вигляді снігу за цю декаду.
import numpy as np

rainfall = np.array(
    [5, 9, 10, 2, 3, 18, 3, 4, 5, 8])
temperature = np.array(
    [15, 19, -10, 0, -13, 18, -13, 14, 15, -18])
snow = 0
rain = 0
for i in range(min(len(rainfall), len(temperature))):
    if temperature[i] <= 0:
        snow += rainfall[i]
    else:
        rain += rainfall[i]
print(f"кількість опадів, що випали у вигляді дощу: {rain}")
print(f"кількість опадів, що випали у вигляді снігу: {snow}")
