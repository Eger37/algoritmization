import numpy as np

a = np.random.randint(-15, 31, 15)
print(a)
print(f"Максимальний елемент: {max(a)}")
print(f"Индекс максимального елемента: {(np.where(a == max(a)))[0]}")
