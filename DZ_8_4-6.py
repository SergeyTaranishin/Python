# программа не завершена. Комментарии по тексту
class Warehouse:
    count = 0
    def __init__(self, square):
        self.square = square

class Office_equipment:
    count = 0
    list = []
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.place = 'склад'
        Office_equipment.count += 1
        Warehouse.count += 1

    def Move_to_Warehouse(self):
        if self.place == 'склад':
            print(f'{self.type} {self.model} уже на складе')
        else:
            self.place = 'склад'
            Warehouse.count += 1
        # действие осталось неотлаженым, так как не получилось на него передать объект

class Printer(Office_equipment):
    def __init__(self, type, model, price, color):
        Office_equipment.__init__(self, type, model, price)
        self.color = color
        self.id = self
        Office_equipment.list.append(self.__dict__)

class Scanner(Office_equipment):
    def __init__(self, type, model, price, format):
        Office_equipment.__init__(self, type, model, price)
        self.format = format
        self.id = self
        Office_equipment.list.append(self.__dict__)

class Xerox(Office_equipment):
    def __init__(self, type, model, price, speed):
        Office_equipment.__init__(self, type, model, price)
        self.speed = speed
        self.ID = self
        Office_equipment.list.append(self.__dict__)

obj_warehouse = Warehouse(1500)
obj_printer_1 = Printer('Принтер', 'HP107', 130, 'b/w')
obj_printer_2 = Printer('Принтер', 'HP108', 140, 'b/w')
obj_scanner_1 = Scanner('Сканер', 'CanoScan Lide 90', 100, 'A4')
obj_scanner_2 = Scanner('Сканер', 'CanoScan Lide 92', 110, 'A4')
obj_xerox_1 = Xerox('Ксерокс', 'CANON imageRUNNER C1225iF', 890, 25)
obj_xerox_2 = Xerox('Ксерокс', 'CANON imageRUNNER C1485iF', 1090, 35)

# попутки понять как вытащить ID объекта
# print(dir(0x0000023DA2CE6D00))
# print(str(obj_printer_1.id)[str(obj_printer_1.id).index(' at ')+4:-1])

while True:
    print(f'На складе: {Warehouse.count}          Всего:{Office_equipment.count}')
    for i, v in enumerate(Office_equipment.list):
        print(f'{i + 1}: {v}')
    print('Выберите оборудование для перемещения (цифра). 0 - завершение работы: ', end='')
    try:
        x = int(input())
        if x == 0:
            break
        print('Куда переместить? 1 - Склад, 2 - Организация: ', end='')
        try:
            where = int(input())
            if where == 1:
                # Тут я не успел найти решение. Мысль заключалась в том, что бы помещать объекты в справочник
                # со словарями, и потом их извлекать по указаному индексу X. Но как правильно помещать объект
                # в справочник/список и извлекать его я нашёл. (((
                # Программа осталась недоделаной. А были мысли дополнить атрибутом "количество оборудования" и при
                # переносе указывать количество... но не судьба (((
                pass
                # Move_to_Warehouse(str(Office_equipment.list[x-1].get('id'))[str(Office_equipment.list[x-1].get('id')).index(' at ')+4:-1])
        except ValueError:
            print('Нужно ввести число!')
    except ValueError:
        print('Нужно ввести число!')

