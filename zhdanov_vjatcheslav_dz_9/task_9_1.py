# Создать класс TrafficLight (светофор):
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
#     третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from itertools import cycle
from time import sleep


class TrafficLight:
    def __init__(self):
        self._color = (('красный', 7), ('желтый', 2), ('зеленый', 10))

    def running(self):
        cycler = cycle(range(len(self._color)))
        for idx in cycler:
            print(self._color[idx][0])
            sleep(self._color[idx][1])


traffic_light = TrafficLight()
traffic_light.running()

