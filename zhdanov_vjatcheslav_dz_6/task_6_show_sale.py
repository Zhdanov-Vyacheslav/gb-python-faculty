# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
#   равный второму числу, включительно.

import sys

file_name = 'bakery.csv'
options = sys.argv[1:]
idx = 0
with open(file_name, encoding='utf-8') as open_f:
    if len(options) == 0:
        while True:
            open_line = open_f.readline()
            if not open_line:
                break
            print(open_line.strip())
    elif len(options) == 1:
        while True:
            open_line = open_f.readline()
            if not open_line:
                break
            idx += 1
            if idx >= int(options[0]):
                print(open_line.strip())
    elif len(options) == 2:
        while True:
            open_line = open_f.readline()
            if not open_line:
                break
            idx += 1
            if int(options[1]) >= idx >= int(options[0]):
                print(open_line.strip())
