# б) Задача. Визначити наймолодшого працівника і надрукувати відомості про нього.
# Поля структури: Прізвище, Рік народження, Посада, Зарплатня, Освіта.
# Сугак Даниїл Васильович 1 курс група 122Б


while True:
    surnames_l = ["Petro", "Danzo"]
    dates_of_borns_l = [1999, 1989]
    posts_l = ['122', '99']
    salarys_l = [1700, 1800]
    educations_l = ['122', '99']

    dates_of_borns = dict(zip(surnames_l, dates_of_borns_l))
    posts = dict(zip(surnames_l, posts_l))
    salarys = dict(zip(surnames_l, salarys_l))
    educations = dict(zip(surnames_l, educations_l))
    # print(dates_of_borns)
    # print(posts)
    # print(salarys)
    # print(educations)
    max_of_year = 0
    element = 0
    for i in dates_of_borns:
        y = dates_of_borns[i]
        if y == max(dates_of_borns_l):
            print(f'Name: {i}\n'
                  f'Date of born: {dates_of_borns[i]}\n'
                  f'Post: {posts[i]}\n'
                  f'Salary: {salarys[i]}\n'
                  f'Education: {educations[i]}\n'
                  )

    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
