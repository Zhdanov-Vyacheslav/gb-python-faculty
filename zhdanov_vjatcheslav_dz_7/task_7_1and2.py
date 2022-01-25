# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
#   как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
#   можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
# *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
#     (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import yaml
import os

# Глобальные переменые для выгрузки структуры
temp_list_g = []
result_g = []
config = 'config.yaml'


def loop_open(structure):
    global temp_list_g, result_g
    for value in structure:
        if type(value) is dict:
            for key_d, value_d in value.items():
                temp_list_g.append(key_d)
                loop_open(value_d)
                temp_list_g.pop(-1)
        else:
            temp_list_g.append(value)
            result_g.append(temp_list_g.copy())
            temp_list_g.pop(-1)


def make_tree(path_l):
    for path in path_l:
        y = ''
        for x in path[:-1]:
            y += f'{x}/'
        if not os.path.exists(os.path.join(y[:-1])):
            os.makedirs(os.path.join(y[:-1]))
        if not os.path.exists(os.path.join(y + path[-1])) and path[-1] != '':
            file = open(os.path.join(y + path[-1]), 'w')
            file.close()
    return 'Выполнено'


with open(config, encoding='utf-8') as yaml_f:
    templates = yaml.safe_load(yaml_f)
loop_open(templates)
print(make_tree(result_g))
