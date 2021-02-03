mounth = input('Укажите номер месяца от 1 до 12: ')
if mounth.isdigit() == False or int(mounth) < 1 or int(mounth) > 12:
    print('!!! Просили ввести цифру от 1 до 12 !!!')
else:
    mounth = int(mounth)
    
    # вариант  dict
    calendar = {
        12: 'зима',
        1: 'зима',
        2: 'зима',
        3: 'весна',
        4: 'весна',
        5: 'весна',
        6: 'лето',
        7: 'лето',
        8: 'лето',
        9: 'осень',
        10: 'осень',
        11: 'осень'}
    print(f'{mounth}-ый месяц это {calendar.get(mounth)}')

    # вариант  List
    calendar = [12, 'зима', 1, 'зима', 2, 'зима', 3, 'весна', 4, 'весна', 5, 'весна', 6, 'лето', 7, 'лето', 8, 'лето',
                9, 'осень', 10, 'осень', 11, 'осень']
    print(f'{mounth}-ый месяц это {calendar[calendar.index(mounth) + 1]}')
