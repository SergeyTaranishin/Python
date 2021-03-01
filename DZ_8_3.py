def transformation(x, my_list):
    try:
        x = int(x)
        my_list.append(x)
        return x, my_list
    except ValueError:
        print(f'"{x}" не явлеется числом. Вводите дальше только числа:')


print('Вводите числа. Для завершения введите "stop":')
my_list = []
while True:
    x = input()
    if x.lower() == 'stop':
        break
    transformation(x, my_list)
print(f'Итоговый список чисел: {my_list}')




