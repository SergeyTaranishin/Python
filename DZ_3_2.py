def info_man(name, surname, year, sity, email, phone):
    """"Сложение аргументов по заданному шаблону"""
    print(name +' '+ surname+' '+str(year)+'г.р. из г.'+sity+'. Email: '+email+' т.'+str(phone))

info_man(name='Сергей',surname='Таранишин', year=1982, sity='Самара', email='tar@mail.ru',phone=89649800948)