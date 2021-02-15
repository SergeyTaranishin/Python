list_text = []
with open("DZ_5_1.txt", 'x') as file:
    while True:
        text = input()+'\n'
        if text == '\n':
            break
        else:
            list_text.append(text)
    print(f'Данные сохранены в файл: {file.name}')
    file.writelines(list_text)
