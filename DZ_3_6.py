import re   # Google

def int_func(text):
    """Приведение первых букв к заглавной букве"""
    return text.title()

text = input('Введите несколько слов через пробел из маленьких латинских букв: ')
if re.search(r'[^a-z ]', text):
    print("Ошибка ввода!")
else:
    print('Результат:', int_func(text))