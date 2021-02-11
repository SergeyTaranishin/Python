from sys import argv
try:
    name_script, rate, hours, bonus = argv
    print(f'Заработная плата сотрудника = {float(rate) * float(hours) + float(bonus)} руб.')
except ValueError:
    print('Необходимо указать 3 параметра через пробел: ставка(руб/час) часы(кол-во) премия(руб.)')
