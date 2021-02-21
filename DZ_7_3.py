class Cell:
    def __init__(self, size=1):
        try:
            self.size = int(size)    # int отбрасывает после запятой (на всякий случай)
        except TypeError:
            self.size = 0

    def __add__(self, other):                  # +
        x = (self.size + other.size)
        return x

    def __sub__(self, other):                  # -
        if (self.size - other.size) > 0:
            return self.size - other.size
        else:
            print(f'{self.size} - {other.size}? Так так не получится!')

    def __mul__(self, other):                  # *
        return self.size * other.size

    def __truediv__(self, other):              # /
        try:
            x = self.size // other.size
            return x
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
            return 0

    def make_order(self, x):       # x - количество клеток в ячейке
        i = 0
        whole = self.size // x     # количество получившихся ячеек
        last = self.size % x       # оставшиеся клетки
        while i < whole:
            print('*' * x)
            i += 1
        if last > 0:
            print('*' * last)

# создание клеток
obj_cell_1 = Cell()
obj_cell_2 = Cell(2)
obj_cell_3 = Cell()
obj_cell_4 = Cell(4)
obj_cell_5 = Cell()
obj_cell_6 = Cell(6)

# операции с клетками
obj_cell_7 = Cell(obj_cell_1 + obj_cell_2)
print(f'Клетка 7: размер - {obj_cell_7.size}')
obj_cell_7.make_order(1)

obj_cell_8 = Cell(obj_cell_3 - obj_cell_4)
print(f'Клетка 8: размер - {obj_cell_8.size}')
obj_cell_8.make_order(5)

obj_cell_9 = Cell(obj_cell_6 - obj_cell_5)
print(f'Клетка 9: размер - {obj_cell_9.size}')
obj_cell_9.make_order(2)

obj_cell_10 = Cell(obj_cell_7 * obj_cell_9)
print(f'Клетка 10: размер - {obj_cell_10.size}')
obj_cell_10.make_order(8)

obj_cell_11 = Cell(obj_cell_9 / obj_cell_8)
print(f'Клетка 11: размер - {obj_cell_11.size}')
obj_cell_11.make_order(5)

obj_cell_12 = Cell(obj_cell_9 / obj_cell_7)
print(f'Клетка 12: размер - {obj_cell_12.size}')
obj_cell_12.make_order(5)

obj_cell_13 = Cell(400)
print(f'Клетка 13: размер - {obj_cell_13.size}')
obj_cell_13.make_order(120)


