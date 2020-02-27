# а) Дана непорожня послідовність слів з малих українських літер; між сусідніми
# словами - кома, за останнім словом - крапка. Вивести на екран в алфавітному порядку всі
# глухі приголосні букви, що входять в кожне непарне слово і не входять хоча б в одне
# парне слово.
# Сугак Даниїл Васильович 1 курс група 122Б
alf = 'а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ь, ю, я,'
letters = 'пхктшсчцф'
while True:
    true_letters = []
    unpaired = []
    paired = []
    while True:
        tr = False
        s = input('input послідовність слів з малих українських літер: ')
        if not s:
            print('порожня послідовність')
            continue
        for i in s:
            if i not in alf:
                tr = True
        if tr:
            print('послідовність слів з малих українських літер')
        if s[-1] != '.':
            print('No point at the end of the sentence!')
            continue
        break
    s = s.replace(' ', '')
    l_s = s.split(',')
    i = 0
    for i in l_s:

        if i % 2 == 0:
            paired.append(i)
        else:
            unpaired.append(i)
        i += 1
    for let in letters:
        tr_2 = True
        tr_3 = False
        for w in paired:
            if let not in w:
                tr_2 = False
        for w in unpaired:
            if let not in w:
                tr_3 = True
        if tr_2 and tr_3:
            true_letters.append(let)
    print(sorted(true_letters))
    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
