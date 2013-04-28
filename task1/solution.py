SIGNS = {
    (4, 20): 'Овен', (5, 20): 'Телец', (6, 20): 'Близнаци',
    (7, 21): 'Рак', (8, 22): 'Лъв', (9, 22): 'Дева',
    (10, 22): 'Везни', (11, 21): 'Скорпион', (12, 21): 'Стрелец',
    (1, 19): 'Козирог', (2, 18): 'Водолей', (3, 20): 'Риби'
}


def what_is_my_sign(day, month):
    for key, value in SIGNS.items():
        if ((key[0] == month and key[1] >= day) or ((key[0] == month+1 or
                                                     key[0] == month+11) and
                                                    key[1] < day)):
            return value
