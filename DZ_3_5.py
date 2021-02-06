summa = 0
i = ''

def my_func(summa, i=''):
    """Вывод суммы списка чисел с учётом суммы прошлой итерации"""
    list_num = []
    list_str = input('Введите несколько чисел через пробел. Q-завершение: ').split()
    for i in list_str:
        if i.upper() == 'Q':
            break
        list_num.append(float(i))
    summa = sum(list_num) + summa
    print(f'Общая сумма = {summa}') if (summa != 0 and i.upper() == 'Q') or i.upper() != 'Q' else ''
    return i.upper(), summa

while i != 'Q':
    i, summa = my_func(summa)