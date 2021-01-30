all_second = int(input('Укажите количество секунд (целое число): '))

hh = all_second // 3600
mm = (all_second - hh * 3600) // 60
ss = all_second - hh * 3600 - mm * 60

print(str(all_second),  'секунд в формате чч:мм:сс будет выглядеть так -', f'{hh:02}:{mm:02}:{ss:02}')