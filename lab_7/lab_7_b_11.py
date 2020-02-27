# б) Задача. Визначити наймолодшого працівника і надрукувати відомості про нього.
# Поля структури: Прізвище, Рік народження, Посада, Зарплатня, Освіта.
# Сугак Даниїл Васильович 1 курс група 122Б


def my_input(text):
    while True:
        try:
            input_num = int(input(text))
            break
        except ValueError:
            print('only digit')
    return input_num


def new_worker(num):
    worker = {"surname": input(f"surname {num} of worker: "),
              "date_of_born": my_input(f"year of born {num} of worker: "),
              "post": input(f"post {num} of worker: "),
              "salary": my_input(f"salary {num} of worker: "),
              "education": input(f"education {num} of worker: "),

              }
    return worker


while True:
    workers = []
    cw = int(input('count of worker: '))
    if cw < 1 or cw > 10:
        print('Не правильное количество workers')
        continue

    # for i in range(1, cw + 1):
    #     workers.append(new_worker(i))
    workers = [{'surname': 'Petro', 'date_of_born': 1999, 'post': '122', 'salary': 1700, 'education': '122'},
               {'surname': 'Vano', 'date_of_born': 1980, 'post': '122', 'salary': 1700, 'education': '122'},
               {'surname': 'Danzo', 'date_of_born': 1975, 'post': '99', 'salary': 1800, 'education': '99'}]
    max_of_year = 0
    element = 0
    for i in range(0, len(workers)):
        y = workers[i].get('date_of_born')
        if max_of_year < y:
            max_of_year = y
            element = i
    print(workers[element])

    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
