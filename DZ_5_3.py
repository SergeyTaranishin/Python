def average_number(salaries):
    """Получение среднего значения из списка чисел"""
    sum = 0
    for i in salaries:
        sum = sum + i
    return sum/len(salaries)

# чтение данных из файла
with open('DZ_5_3.txt',  encoding='utf-8') as file:
    list_text = file.readlines()

# преобразование данных к списку вида [(N, {'Фамилия':Оклад})]
my_list = []
my_dic = {}
for n, value in enumerate(list_text):
    fio_cash = value.split()
    my_dic = {'Фамилия': fio_cash[0], 'Оклад': int(fio_cash[1])}
    my_list.append((n+1, my_dic))

# получение списка сотрудников с окладом < 20000
list_less_20000 = [i[1].get('Фамилия') for i in my_list if i[1].get('Оклад') < 20000]
print('Сотрудники с окладом < 20000:')
for n, value in enumerate(list_less_20000):
    print(f'{n+1}. {value}')

# получение средней зарплаты
salaries = [i[1].get('Оклад') for i in my_list]
print(f'Средний оклад: {average_number(salaries)}')