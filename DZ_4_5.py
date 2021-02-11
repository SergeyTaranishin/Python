from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1001, 2)]
print(my_list)
print(f'Результат вычисления произведения всех элементов списка:\n{reduce(my_func, my_list)}')
