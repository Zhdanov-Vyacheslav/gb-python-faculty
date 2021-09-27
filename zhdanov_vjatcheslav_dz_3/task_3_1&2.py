# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
#
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
#   необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную
#   работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


def num_translate(number):
    translate_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    key = 1 if number[0].isupper() else 0
    if number.lower() not in translate_dict:
        return None
    return translate_dict[number.lower()].title() if key == 1 else translate_dict[number.lower()]


print('Введите число на английском')
input_number = input()
print(num_translate(input_number))

