def division(a, b):
    """Деление аргумента A на аргумент B"""
    return round(a / b, 2)

print('*** Деление А на B ***')
a = float(input('Введите число А: '))
b = float(input('Введите число B: '))
if b == 0:
    print('На ноль делить нельзя!')
else:
    print('А / В = ', division(a, b))
