# Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему
#   номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование.
#   Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.

import sys
import shutil

file_name = 'bakery.csv'
trash_file = '_'+file_name
line, value = sys.argv[1:]
line = int(line)

with open(file_name, 'r', encoding='utf-8') as bakery_f:
    bakery_len = len([0 for _ in bakery_f])
    if line > bakery_len:
        sys.exit('Line is not found')
    with open(trash_file, 'w', encoding='utf_8') as temp_f:
        bakery_f.seek(0)
        for idx, bakery_line in enumerate(bakery_f):
            temp_f.write(f'{value}\n' if idx == line-1 else bakery_line)
        temp_f.seek(0)

shutil.move(trash_file, file_name)



