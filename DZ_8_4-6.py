# программа не завершена. Комментарии по тексту
class Warehouse:
    count = 0
    def __init__(self, square):
        self.square = square

class Office_equipment:
    count_all = 0
    count_office = 0
    list = []
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.place = 'склад'
        Office_equipment.count_all += 1
        Warehouse.count += 1

    def Move_to_Warehouse(self, ind):
        if self.place == 'склад':
            print(f'{self.type} {self.model} уже на складе')
        else:
            self.place = 'склад'
            Office_equipment.list[ind - 1].update({'Нахождение':'склад'})
            Warehouse.count += 1
            Office_equipment.count_office -= 1

    def Move_to_Office(self, ind):
        if self.place == 'склад':
            self.place = 'офис'
            Office_equipment.list[ind - 1].update({'Нахождение':'офис'})
            Warehouse.count -= 1
            Office_equipment.count_office += 1
        else:
            print(f'{self.type} {self.model} уже в офисе')

class Printer(Office_equipment):
    def __init__(self, type, model, price, color):
        Office_equipment.__init__(self, type, model, price)
        self.color = color
        Office_equipment.list.append({'Тип оборудования': self.type,
                                      'Модель': self.model,
                                      'Цена': self.price,
                                      'Цветность': self.color,
                                      'Нахождение': self.place,
                                      'ID': self})

class Scanner(Office_equipment):
    def __init__(self, type, model, price, format):
        Office_equipment.__init__(self, type, model, price)
        self.format = format
        Office_equipment.list.append({'Тип оборудования': self.type,
                                      'Модель': self.model,
                                      'Цена': self.price,
                                      'Формат': self.format,
                                      'Нахождение': self.place,
                                      'ID': self})

class Xerox(Office_equipment):
    def __init__(self, type, model, price, speed):
        Office_equipment.__init__(self, type, model, price)
        self.speed = speed
        Office_equipment.list.append({'Тип оборудования': self.type,
                                      'Модель': self.model,
                                      'Цена': self.price,
                                      'Скорость': self.speed,
                                      'Нахождение': self.place,
                                      'ID': self})

obj_warehouse = Warehouse(1500)
obj_printer_1 = Printer('Принтер', 'HP107', 130, 'b/w')
obj_printer_2 = Printer('Принтер', 'HP108', 140, 'b/w')
obj_scanner_1 = Scanner('Сканер', 'CanoScan Lide 90', 100, 'A4')
obj_scanner_2 = Scanner('Сканер', 'CanoScan Lide 92', 110, 'A4')
obj_xerox_1 = Xerox('Ксерокс', 'CANON imageRUNNER C1225iF', 890, 25)
obj_xerox_2 = Xerox('Ксерокс', 'CANON imageRUNNER C1485iF', 1090, 35)

while True:
    print(f'На складе: {Warehouse.count}          В офисе: {Office_equipment.count_office}          Всего:{Office_equipment.count_all}')
    for i, v in enumerate(Office_equipment.list):
        print(f'{i + 1}: {v}')
    print(f'Выберите оборудование для перемещения (число от 1 до {len(Office_equipment.list)}). 0 - завершение работы: ', end='')
    try:
        ind = int(input())

        if ind == 0:
            break
        elif 0 < ind <= len(Office_equipment.list):
            print('Куда переместить? 1 - Склад, 2 - Офис: ', end='')
            try:
                where = int(input())
                if where == 1:
                    Office_equipment.Move_to_Warehouse(Office_equipment.list[ind-1].get('ID'), ind)
                elif where == 2:
                    Office_equipment.Move_to_Office(Office_equipment.list[ind-1].get('ID'), ind)
                else:
                    print('Нужно ввести 1 или 2')
            except ValueError:
                print('Нужно ввести число!')
        else:
            print(f'Нужно ввести число от 1 до {len(Office_equipment.list)}')
    except ValueError:
        print('Нужно ввести число!')
