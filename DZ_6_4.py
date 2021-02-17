class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, turn):
        print(f'{self.name} повернула {turn}')

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.color} {self.name} превышение скорости')
        else:
            print(f'Скорость {self.name} {self.speed} ')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.color} {self.name} превышение скорости')
        else:
            print(f'Скорость {self.name} {self.speed} ')


class PoliceCar(Car):
    pass


granta = TownCar(140, 'Черная', 'Гранта', False)
bmw = WorkCar(240, '<Белая', 'BMW', False)
ferrari = SportCar(340, 'Красная', 'Ferrari', False)
logan = PoliceCar(140, 'Баклажан', 'Logan', True)

granta.go()
granta.turn('налево')
granta.show_speed()
granta.stop()
logan.show_speed()
ferrari.turn('направо')
ferrari.show_speed()
print(logan.is_police)
