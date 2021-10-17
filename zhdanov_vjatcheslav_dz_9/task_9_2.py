# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
#     дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
#
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def masses(self, masses, thickness):
        result = self.__length * self.__width * masses * thickness / 1000
        return f'{self.__length} m*{self.__width} m*{masses} кг*{thickness} см = {result} т.'


test = Road(5000, 20)
print(test.masses(25, 5))