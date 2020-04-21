# 60. Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
# однакових чисел, що йдуть підряд в ньому.
import numpy as np

a = np.random.randint(0, 10, 10)
b0 = np.array([a[0] - 1])
b1 = np.array([a[-1] - 1])
c = np.concatenate((b0, a,b1), axis=0)
# print(b0)
# print(b1)
# print(a)
# print(c)
count = 1
mc = 1
for i in range(1, len(c)):
    if c[i] == c[i - 1]:
        count += 1
    else:
        mc = count
print(f"Найбільше число однакових чисел, що йдуть підряд в ньому: {mc}")