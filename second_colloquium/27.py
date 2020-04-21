# 27. Лінійний масив містить відомості про кількість опадів, що випали за
# кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість
# опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих
# місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.
import numpy as np

a = np.array([25, 40, 20, 30, 50, 250, 29, 35, 54, 11, 45, 40])
b = np.array(
    ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень", "Жовтень",
     "Листопад", "Грудень"])
print(f"Загальна кількість опадів за рік: {a.sum()} мм")
for i in range(12):
    print(f"середньомісячну кількість опадів у місяці {b[i]}: {a[i]} мм")

c = a[a < 30]
print(f"кількість посушливих місяців: {len(c)}")
print(f"найпосушливіший місяць року: {b[(np.where(a == a.min()))[0][0]]}")
