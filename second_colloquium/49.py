# 49. Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
# за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.


table = ["Геркулес", "Аполлон", "Промитей", "Одисей", "Тесей", "Персей", "Ахил", "Артеміда", "Ванша", "Вано"]
cost = [12, 14, 24, 12, 52, 34, 12, 754, 12, 745]
num = 754# ціна
idx = cost.index(num)
for i in  range(idx):
    print(f"Послуга: {table[i]}, Ціна: {cost[i]} грн")