# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
#     Написать скрипт, который собирает все шаблоны в одну папку templates
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
#   (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
#   решена, например, во фреймворке django.

import os
import shutil

folder = 'my_project'
folder_for_files = 'templates'
folder_list = []
find_files = ('index.html', 'base.html')

for value in os.walk(folder):
    folder_list.append(value)
for path_tuple in folder_list:
    for file_name in path_tuple[2]:
        if file_name in find_files:
            path_for_copy = os.path.join(folder, folder_for_files, os.path.basename(path_tuple[0]), file_name)
            if not os.path.exists(os.path.dirname(path_for_copy)):
                os.makedirs(os.path.dirname(path_for_copy))
            if not os.path.exists(path_for_copy):
                shutil.copy(os.path.join(path_tuple[0], file_name), path_for_copy)
                print(f'Файл {os.path.join(path_tuple[0], file_name)}, скопирован в {path_for_copy}')
            else:
                print(f'Файл: {file_name} из {path_tuple[0]} уже в есть в {folder_for_files}')
