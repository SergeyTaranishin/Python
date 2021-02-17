class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.position}: {self.name} {self.surname}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'Доход: {total_income}')


obj_1 = Position('Иван', 'Иванов', 'Аналитик', 200000, 100000)
obj_1.get_full_name()
obj_1.get_total_income()

obj_2 = Position('Пётр', 'Петров', 'Инженер', 15000, 10000)
obj_2.get_full_name()
obj_2.get_total_income()
