# 11.
# а) Дан текстовий файл f. Отримати копію цього файлу.

# Сугак Даниїл Васильович 1 курс група 122Б

with open('f.txt', 'r') as f:
    f_str = f.read()
with open('f_copy.txt', 'w') as f_copy:
    f_copy.write(f"{f_str}")
