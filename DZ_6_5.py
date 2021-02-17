class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


obj_pen = Pen('Ручка')
obj_pen.draw()
obj_Pencil = Pencil('Карандаш')
obj_Pencil.draw()
obj_handle = Handle('Маркер')
obj_handle.draw()
