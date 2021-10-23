# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
#     Основная сущность (класс) этого проекта — одежда, которая может иметь определённое
#     название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
#     существуют параметры: размер (для пальто) и рост (для костюма).
#     Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
#     для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
#     Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, names):
        self.names = names

    @abstractmethod
    def sum_cloth(self):
        pass


class Costume(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    @property
    def sum_cloth(self):
        return 2 * self.h + 0.3


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    @property
    def sum_cloth(self):
        return self.v / 6.5 + 0.5


costume = Costume('name', 6)
coat = Coat('name', 6)
print(coat.sum_cloth + costume.sum_cloth)
