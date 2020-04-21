# 35. Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
# спаданню.
import numpy as np

a = np.array([1, 2, 3, 4, 6, 5, 9])
previous = a[0] - 1
sw = True
for i in a:
    if not i > previous:
        sw = False
        break
    previous = i
if sw:
    print("Масив упорядкований")
else:
    print("Масив неупорядкований")

b = np.array([1, 2, 3, 4, 6, 7, 9, 16])
previous = b[0] - 1
sw = True
for i in b:
    if not i > previous:
        sw = False
        break
    previous = i
if sw:
    print("Масив упорядкований")
else:
    print("Масив неупорядкований")
