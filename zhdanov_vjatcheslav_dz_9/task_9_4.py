# Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
#   turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
#   40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self):
        print('turn')

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Привышение скорости')
        return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Привышение скорости')
        return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True
