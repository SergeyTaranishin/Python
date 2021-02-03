i = 1
my_list = []         #список
my_tuple = tuple()   #кортеж
my_dict = {}         #словарь
a_next = 'д'
while a_next == 'д':
    name = input('Наименование: ')
    my_dict.update({'Наименование': name})
    price = float(input('Цена: '))
    my_dict.update({'Цена': price})
    quantity = int(input('Количество: '))
    my_dict.update({'Количество': quantity})
    units = input('Единицы измерения: ')
    my_dict.update({'ед.изм.': units})

    my_tuple = (i, my_dict)
    my_list.append(my_tuple)
    my_dict = my_dict.copy()

    a_next = input('Хотите добавить ещё один товар? д/н: ').lower()
    i += 1
list_name = []
list_price = []
list_quantity = []
list_units = []
i = 0
while i < len(my_list):       # через FOR хотел, но не получилось. На уроке расскажите подробнее про FOR, пожалуйста
    list_name.append(my_list[i][1].get('Наименование'))
    list_price.append(my_list[i][1].get('Цена'))
    list_quantity.append(my_list[i][1].get('Количество'))
    list_units.append(my_list[i][1].get('ед.изм.'))
    i += 1

new_dict = {'Наименование': list_name}
new_dict.update({'Цена': list_price})
new_dict.update({'Количество': list_quantity})
new_dict.update({'ед.изм.': list(set(list_units))})

print('Аналитика:', new_dict)
