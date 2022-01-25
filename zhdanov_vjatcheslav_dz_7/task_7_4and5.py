# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в
#   котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения —
#   общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
#   но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
# *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
#   в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#     {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
#
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import json
import os


def make_dict(walk_list):
    result_dict = {}
    for path_tuple in walk_list:
        for file_name in path_tuple[2]:
            path_file = os.path.join(path_tuple[0], file_name)
            size_file = os.stat(path_file).st_size
            root = 10 ** len(str(size_file))
            result_dict.setdefault(root, [0, []])
            result_dict[root][0] += 1
            file_extension = file_name[file_name.rfind('.') + 1:len(file_name)] if file_name.rfind('.') != -1 else ''
            if file_extension not in result_dict[root][1]:
                result_dict[root][1].append(file_extension)
    return result_dict


def write_file(input_dict: dict, input_name):
    separator = '/' if input_name.rfind('/') != -1 else '\\'
    input_name = input_name[input_name.rfind(separator)+1:len(input_name)]
    with open(f'{input_name}_summary.json', 'w', encoding='utf-8') as write_f:
        json.dump(input_dict, write_f)


def rdy_to_write(input_dict: dict):
    rdy_d = {}
    for key, value in sorted(input_dict.items()):
        rdy_d.setdefault(key, (value[0], sorted(value[1])))
    return rdy_d


folder = os.path.join('C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.1')
walk_folder = []
for el in os.walk(folder):
    walk_folder.append(el)
result = make_dict(walk_folder)
result = rdy_to_write(result)
write_file(result, folder)
for k, v in result.items():
    print(k, v)
