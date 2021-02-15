# Предварительно устанавливался пакет translate
# pip install translate
from translate import Translator

# чтение данных из файла
with open('DZ_5_4.txt', encoding='utf-8') as file:
    list_text = file.readlines()

# формирование нового списка с переводом
list_text_new = []
for n, value in enumerate(list_text):
    node = value.split('-')
    trans = Translator(to_lang="russian")
    word_rus = trans.translate(node[0])
    list_text_new.append(f'{word_rus} - {node[1]}')

# запись в новый файл
with open('DZ_5_4_new.txt', 'w') as file_new:
     file_new.writelines(list_text_new)

print(f'Процесс выболнен. Данные записаны в файл {file_new.name}')




