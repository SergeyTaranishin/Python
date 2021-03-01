import time
import traceback


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


A = int(input('Введите делимое: '))
B = int(input('Введите делитель: '))

try:
    if B == 0:
        raise MyError('На ноль делить нельзя')
    else:
        print(f'{A} / {B} = {A / B}')
except MyError:
    with open('Error_log_8_2.txt', 'a', encoding='UTF-8') as file:
        file.write(time.strftime('%Y/%m/%d %X') + '\n' + traceback.format_exc() + '\n')
        print(traceback.format_exc())

print('Программа завершена')
