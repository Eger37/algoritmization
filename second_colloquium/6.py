import numpy as np

a = np.random.randint(-10, 11, 8)
print(a)
c = 0
for boredom in a:
    if boredom < 0:
        c += 1
print(f"Кількість відемних елементів: {c}")
