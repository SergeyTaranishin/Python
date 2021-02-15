from random import randint

def generate_and_sum(min,max,count) :
    """Генерация N случайных чисел и их суммирование"""
    list_num = []
    sum = 0
    for i in range(count):
        r = randint(min, max)
        list_num.append(str(r)+' ')
        sum = sum + r
        i += 1
    return list_num, sum

info = input('Укажите через пробел: min число, max число, количиство чисел >').split()

try:
    list_num, sum = generate_and_sum(int(info[0]), int(info[1]), int(info[2]))
    print('+ '.join(list_num), '=', sum)
    # запись в файл
    with open('DZ_5_5.txt', 'w') as my_file:
        num_str = ''.join(list_num)
        print(f'{num_str}\nСумма чисел = {sum}', file=my_file)
        print(f'Данные записаны в файл {my_file.name}')
except ValueError:
    print('Данные указаны некоректно!')




