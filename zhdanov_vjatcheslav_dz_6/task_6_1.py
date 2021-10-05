# Не используя библиотеки для парсинга, распарсить (получить определённые данные)
#   файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
#   получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
#
result = []
with open('nginx_logs.txt') as open_log:
    while True:
        open_line = open_log.readline().strip()
        if not open_line:
            break
        remote_addr = open_line[0:open_line.find('-') - 1]
        pos = open_line.find('"')
        request_type = open_line[pos + 1:open_line.find(' ', pos)]
        pos = open_line.find(' ', pos)
        requested_resource = open_line[pos + 1:open_line.find(' ', pos + 1)]
        result.append((remote_addr, request_type, requested_resource))
