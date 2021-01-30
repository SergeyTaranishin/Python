begin_km = float(input('Сколько км спортсмен может пробежать в первый день тренировок? '))
if begin_km == 0:
    print('Боюсь, тренировки тут не помогут!')
else:
    end_km = float(input('Сколько км спортсмен хочет пробегать в день после тренировок? '))
    day = 1
    while begin_km <= end_km:
        print(f'{day}-й день: {begin_km:.2f} км')
        begin_km = begin_km * 1.1
        day = day + 1
    print(f'{day}-й день: {begin_km:.2f} км')

    if day == 1:
        day_str = 'первый'
    elif day == 2:
        day_str = 'второй'
    elif day == 3:
        day_str = 'третий'
    elif day == 4:
        day_str = 'четвёртый'
    elif day == 5:
        day_str = 'пятый'
    elif day == 6:
        day_str = 'шестой'
    elif day == 7:
        day_str = 'седьмой'
    elif day == 8:
        day_str = 'восьмой'
    elif day == 9:
        day_str = 'девятый'
    elif day == 10:
        day_str = 'десятый'
    elif day == 11:
        day_str = 'одиннадцатый'
    elif day == 12:
        day_str = 'двенадцатый'
    elif day == 13:
        day_str = 'тринадцатый'
    elif day == 14:
        day_str = 'четырнадцатый'
    elif day == 15:
        day_str = 'пятнадцатый'
    elif day == 16:
        day_str = 'щестнадцатый'
    elif day == 17:
        day_str = 'семнадцатый'
    elif day == 18:
        day_str = 'восемнадцатый'
    elif day == 19:
        day_str = 'девятнадцатый'
    elif day == 20:
        day_str = 'двадцатый'

    if day > 20:
        print(f'На {day}-й день спотсмен достигнет своей цели пробегать не менее {end_km} км')
    else:
        print(f'На {day_str} день спотсмен достигнет своей цели пробегать не менее {end_km} км')

