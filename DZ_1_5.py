proceeds = float(input('Ввидите выручку фирмы за год в рублях: '))  # выручка
costs = float(input('Ввидите издержки фирмы за год в рублях: '))  # издержки

if proceeds > costs:
    profit = proceeds - costs  # прибыль
    print('Фирма получила прибыль за год:', f'{profit:.2f}', 'рублей')
    profitability = (profit/proceeds)*100     # рентабельность
    print('Рентабельность составила: %.2f' % profitability, '%')
    count_man = int(input('Сколько сотрудников работает в фирме?: '))
    print('Прибыль на одного сотрудника составила:', '%.2f' % (profit/count_man), 'рублей')

elif proceeds < costs:
    print('Фирма получила убыток за год:', '%.2f' % (costs - proceeds), 'рублей')
else:
    print('Фирма за год отработала в ноль')
