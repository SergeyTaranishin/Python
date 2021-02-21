from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def consumption(self):
        pass

class Clothes(MyAbstractClass):
    def __init__(self, type_clothes, value):
        self.type_clothes = type_clothes
        if type_clothes == 'coat':
            self.size = value
        else:
            self.Height = value
    @property
    def consumption(self):
        if self.type_clothes == 'coat':
            consumption = (self.size/6.5 + 0.5)
        else:
            consumption = (2 * self.Height + 0.3)
        return consumption


coat = Clothes('coat', 50)
costume = Clothes('costume', 5)

print(f'Расхода ткани для пальто: {coat.consumption:.2f} ед.изм.')
print(f'Расхода ткани для кастюма: {costume.consumption:.2f} ед.изм.')

