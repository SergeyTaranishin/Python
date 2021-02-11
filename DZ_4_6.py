from itertools import count, cycle

print('Первая задача:')
for el in count(3):
    if el > 8:
        break
    else:
        print(el)

print('Вторая задача:')
my_list = [1, 2, 3, 4, 5]
iter = cycle(my_list)
i = 1
while i <= len(my_list):
    print(next(iter))
    i += 1




