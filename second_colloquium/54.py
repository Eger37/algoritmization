# 54. Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
# однаковими значеннями.
import random

l = []
for i in range(20):
    while True:
        try:
            num = int(input("Введіть наступне число: "))
            break
        except ValueError:
            print('only digit')
    l.append(num)
print(f"Масив: {l}")
s = set(l)
if len(l) != len(s):
    print("в ньому є елементи з однаковими значеннями")
else:
    print("в ньому немає елементів з однаковими значеннями")
