import json

with open('DZ_5_7.txt', encoding='utf-8') as file:
    list_text = file.readlines()
    list_text.pop(0)

# создание словаря {фирма: float(прибыль).2}
# удаление пробелов в числах. Замена ',' на '.'
dic_firm = {}
for n, value in enumerate(list_text):
    info = value.split(';')
    profit = float((info[2].replace(' ', '')).replace(',', '.')) - float((info[3].replace(' ', '')).replace(',', '.'))
    dic_firm.update({info[0]: float('{:.2f}'.format(profit))})

# поместить словарь в справочник
new_list = []
new_list.append(dic_firm)

# подсчёт средней прибыли
list_average_profit = [dic_firm[i] for i in list(dic_firm) if dic_firm[i] > 0]

# добавить словарь среденй прибыли в справочник
new_list.append({'average_profit': sum(list_average_profit)/len(list_average_profit)})

print(f'Фирмы : прибыль, средняя прибыль:\n{new_list}')

with open('my_file.json', 'w') as file_json:
    json.dump(new_list, file_json, ensure_ascii=False)