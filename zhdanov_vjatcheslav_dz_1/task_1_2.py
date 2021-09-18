#   Переменные
pool = 1000
increment = 17
arithmetic_root = 3
odd_number = 1
list_odd_number = [1]
denominator = 7
result = 0
result_increment = 0

#  Определение длинны списка если задавать значение отличные от 1000
if pool % 2 == 0:
    pool = pool // 2 - 1
else:
    pool = pool // 2

#  Создаем список кубов нечетных чисел
for idx in range(pool):
    check_multiplicity = 0
    odd_number += 2  # Получаем следующее число
    list_odd_number.append(odd_number ** arithmetic_root)  # Возводим в куб
    string_of_number = str(list_odd_number[idx + 1])  # Переводим число в строку для дальнейших операций
    for idx2 in range(len(string_of_number)):  # Проходим поэлементно по числу и суммируем его элементы между собой
        check_multiplicity += int(string_of_number[idx2])
    if check_multiplicity % denominator == 0:  # Проверка делиться ли без остатка
        result += check_multiplicity

for idx in range(len(list_odd_number)):
    check_multiplicity = 0
    list_odd_number[idx] += increment  # Прибавляем к кубу заданное значение
    string_of_number = str(list_odd_number[idx])  # Переводим число в строку для дальнейших операций
    for idx2 in range(len(string_of_number)):  # Проходим поэлементно по числу и суммируем его элементы между собой
        check_multiplicity += int(string_of_number[idx2])
    if check_multiplicity % denominator == 0:  # Проверка делиться ли без остатка
        result_increment += check_multiplicity

print('Результат "а" = '+str(result))
print('Результат "b" = '+str(result_increment))
