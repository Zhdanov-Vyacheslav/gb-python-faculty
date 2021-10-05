# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
#   из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже
#   с файлами, размер которых превышает объем ОЗУ компьютера.

addr_list = []
count_list = []
with open('nginx_logs.txt') as open_log:
    while True:
        open_line = open_log.readline().strip()
        if not open_line:
            break
        remote_addr = open_line[0:open_line.find('-') - 1]
        if remote_addr not in addr_list:
            addr_list.append(remote_addr)
            count_list.append(1)
        else:
            count_list[addr_list.index(remote_addr)] += 1
spammer = ''
spammer_count = 0
for addr, value in zip(addr_list, count_list):
    if spammer_count < value:
        spammer_count = value
        spammer = addr
print(spammer, spammer_count)
