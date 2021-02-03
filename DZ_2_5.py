my_list = [70, 50, 30, 30, 20]

print('Текущий рейтинг:', my_list)
number = input('Укажите новый рейтинг (натуральное число): ')

if number.isdigit() == False or int(number) < 1:
    print('Натуральные числа (от лат. naturalis «естественный») — числа, возникающие естественным образом при счёте '
          '(1, 2, 3, 4, 5, 6, 7 и так далее...)')
else:
    number = int(number)
    if number >= my_list[0]:
        my_list.insert(0, number)
    elif number <= my_list[len(my_list) - 1]:
        my_list.append(number)
    elif my_list.count(number) > 0:
        my_list.insert(my_list.index(number), number)
    else:
        i = 0
        while i <= len(my_list):
            if number < my_list[i] and number > my_list[i + 1]:
                my_list.insert(i + 1, number)
                break
            else:
                i += 1

    print(f'Результат: {my_list}')
