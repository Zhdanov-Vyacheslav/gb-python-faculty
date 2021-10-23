# Реализовать класс Stationery (канцелярская принадлежность):
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
#   Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self):
        self.title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super().__init__()
        self.title = 'Pen'

    def draw(self):
        print(f'{self.title} draws')


class Pencil(Stationery):
    def __init__(self):
        super().__init__()
        self.title = 'Pencil'

    def draw(self):
        print(f'{self.title} draws')


class Handle(Stationery):
    def __init__(self):
        super().__init__()
        self.title = 'Handle'

    def draw(self):
        print(f'{self.title} draws')


base_class = Stationery()
base_class.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
