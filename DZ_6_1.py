import time


class TrafficLight:
    def running(self, time_start, color):
        self.__color = color
        print(color)
        while True:
            if color == 'Красный' and time.time() - time_start >= 7:
                color = 'Жёлтый'
                print(color)
                time_start = time.time()
            elif color == 'Жёлтый' and time.time() - time_start >= 2:
                color = 'Зелёный'
                print(color)
                time_start = time.time()
            elif color == 'Зелёный' and time.time() - time_start >= 10:
                color = 'Красный'
                print(color)
                time_start = time.time()


obj_a = TrafficLight()
obj_a.running(time.time(), 'Красный')
# светофор выключается только остановкой программы вручную!
