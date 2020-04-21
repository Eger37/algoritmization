# 56. Якщо в одновимірному масиві є три поспіль однакових елемента, то
# змінній r привласнити значення істина.
import numpy as np

a = np.random.randint(0, 10, 100)
print(a)
r = False
for i in range(len(a) - 2):
    if a[i] == a[i + 1] == a[i + 2]:
        r = True
print(f"r: {r}")
