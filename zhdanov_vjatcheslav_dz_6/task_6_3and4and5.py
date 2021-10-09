# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
#   разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и
#   формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле
#   с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи
# *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
#   (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
#   Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные
#   данные в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи
# **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя
#   обоих исходных файлов и имя выходного файла. Проверить работу скрипта.

import sys
from itertools import zip_longest
users, hobby, new_file = sys.argv[1:]
if open(users).readable() and open(hobby).readable():
    with open(new_file, 'w', encoding='utf-8') as new_f:
        with open(users, encoding='utf-8') as users_f:
            with open(hobby, encoding='utf-8') as hobby_f:
                users_len = len([0 for _ in users_f])
                hobby_len = len([0 for _ in hobby_f])
                if users_len < hobby_len:
                    exit(1)
                users_f.seek(0)
                hobby_f.seek(0)
                for users_line, hobby_line in zip_longest(users_f, hobby_f):
                    new_f.write(f'{users_line.strip()}: '
                                f'{hobby_line.strip() if users_line is not None else users_line}\n')
