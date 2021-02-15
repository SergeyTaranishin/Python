import re

def sum(List_hour) :
    """суммирование списка чисел"""
    sum = 0
    for i in List_hour:
        sum = sum + i
    return sum

with open('DZ_5_6.txt', encoding='utf-8') as file:
    list_text = file.readlines()

dic = {}
for n, value in enumerate(list_text):
    info = value.split(':')
    List_hour = [int(i) for i in re.split(r'[^0-9]', info[1]) if i != '']
    dic.update({info[0]:sum(List_hour)})
print(dic)