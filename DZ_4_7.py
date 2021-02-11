from math import factorial


def fact(def_number):
    for element in range(1, def_number + 1):
        yield factorial(element)


try:
    number = int(input('Введите целое положительное число: '))
    for el in fact(number):
        print(el)

except ValueError:
    print('Нужно ввести целое положительное число!')
