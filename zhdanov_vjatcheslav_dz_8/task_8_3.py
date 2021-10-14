# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
# @type_logger
# def calc_cube(x):
#    return x ** 3
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
#   можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
#   Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper_type_logger(*args):
        temp_str = f'{wrapper_type_logger.__name__}('
        for val in args:
            temp_str = temp_str + f'{val}: {type(val)}, '
        print(temp_str[:-2]+')')
        return func(*args)
    return wrapper_type_logger


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(3))
