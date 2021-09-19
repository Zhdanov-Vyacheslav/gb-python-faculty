# Урок 1 задача 2
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
if pool % 2 != 0:
    pool = pool // 2 + 1
else:
    pool = pool // 2

#  Создаем список кубов нечетных чисел
for idx in range(1, pool):
    check_multiplicity = 0
    odd_number += 2  # Получаем следующее число
    list_odd_number.append(odd_number ** arithmetic_root)  # Возводим в куб
    for number_element in str(list_odd_number[idx]):  # Проходим поэлементно по числу и суммируем его элементы
        check_multiplicity += int(number_element)
    if check_multiplicity % denominator == 0:  # Проверка делиться ли без остатка
        result += list_odd_number[idx]  # Не правильно понял задание, поправил

for idx, temp in enumerate(list_odd_number):
    check_multiplicity = 0
    list_odd_number[idx] += increment  # Прибавляем к кубу заданное значение
    for number_element in str(list_odd_number[idx]) :  # Проходим поэлементно по числу и суммируем его элементы
        check_multiplicity += int(number_element)
    if check_multiplicity % denominator == 0:  # Проверка делиться ли без остатка
        result_increment += list_odd_number[idx]  # Не правильно понял задание, поправил

print('Результат "а" = '+str(result))
print('Результат "b" = '+str(result_increment))
