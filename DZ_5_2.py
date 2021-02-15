with open('DZ_5_2.txt', encoding='utf-8') as file:
    list_text = file.readlines()

for n, value in enumerate(list_text):
    print(str(n+1) + ' строка: ' + str(value.count(' ')+1)+' слов(а)' )
