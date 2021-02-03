a_list = []
i = 1
pos = 0
# заполнение списка
while True:
    print('Текущий список:', a_list)
    value = input('Укажите значение для добавления в список (Для завершения введите "STOP"): ')
    if value.lower() == 'stop':
        break
    a_list.append(value)

# определение количества элементов списка
count = len(a_list)
if count == 0:
    print('Список пуст')
elif count == 1:
    print('Список из одного значения остаёься неизменным:', a_list)
else:
    if count % 2 > 0:    # нечётное
        while (2*i)+1 <= count:
            a_list.insert(pos, a_list.pop(pos+1))
            i += 1
            pos += 2
    else:
        while 2*i <= count:   # чётное
            a_list.insert(pos, a_list.pop(pos+1))
            i += 1
            pos += 2
    print('Результат:', a_list)
