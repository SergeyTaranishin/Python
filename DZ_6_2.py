class Road:

    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self._thickness = thickness
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна = '
              f'{length * width * 25 * thickness / 1000} тонн')


list_road = input('Укажите через пробел длину(м) и ширину(м) дороги, а также толщину(см) асфальта: ').split()
try:
    obj = Road(int(list_road[0]), int(list_road[1]), int(list_road[2]))
except ValueError:
    print('Данные введены некорректно')
