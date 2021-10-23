# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
#     (метод __init__()), который должен принимать данные (список списков) для
#     формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в
#     виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix
#     (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки
#     первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

from itertools import zip_longest


class Matrix:
    def __init__(self, lists_of_list):
        self.matrix = lists_of_list

    def __add__(self, other):
        add_result = []
        for elm1, elm2 in zip_longest(self.matrix, other.matrix):
            add_temp = []
            for val1, val2 in zip_longest(elm1, elm2):
                add_temp.append((val1 if val1 is not None else 0) + (val2 if val2 is not None else 0))
            add_result.append(add_temp)
        return Matrix(add_result)

    def __str__(self):
        str_result = ''
        for el1 in self.matrix:
            for val1 in el1:
                str_result = str_result + str(val1) + ' '
            str_result = str_result[:-1] + '\n'
        return str_result
