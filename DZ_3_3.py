def my_func(a, b, c):
    """Вывод суммы максимальных 2-х чисел из 3-х"""
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    print('Сумма наибольших двух чисел =', sum(my_list))

a = float(input('Укажите первое число: '))
b = float(input('Укажите второе число: '))
c = float(input('Укажите третье число: '))
my_func(a, b, c)