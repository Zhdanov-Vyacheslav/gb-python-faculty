# Константы
cons_day = 86400
cons_hour = 3600
cons_minute = 60
cons_second = 0
list_of_time = [' сек ', ' мин ', ' час ', ' дн ']


def main():
    code_result = 0
    list_result = ['0', '0', '0', '0']
    result = ''
    print('Select output option:\n'
          '1 = до минуты: <s> сек\n'
          '2 = до часа: <m> мин <s> сек\n'
          '3 = до суток: <h> час <m> мин <s> сек\n'
          '4 = в остальных случаях: <d> дн <h> час <m> мин <s> сек')
    option_result = int(input('Enter option: '))
    duration = int(input('Enter duration: '))
    while duration > 0:  # Пока число существет разбираем его на составляющие
        if duration >= cons_day and option_result > 3:
            day = duration // cons_day  # Делим без остатка секунды на константу и получаем кол-во нужных едениц
            duration = duration - day * cons_day  # Получаем оставшее кол-во секунд путем вычитания
            if code_result == 0:  # Узнаем старшенство для вывода результата
                code_result = 3
            list_result[3] = str(day)
        elif duration >= cons_hour and option_result > 2:  # Аналогично проверяем
            hour = duration // cons_hour
            duration = duration - hour * cons_hour
            if code_result == 0:
                code_result = 2
            list_result[2] = str(hour)
        elif duration >= cons_minute and option_result > 1:  # Аналогично проверяем
            minute = duration // cons_minute
            duration = duration - cons_minute * minute
            if code_result == 0:
                code_result = 1
            list_result[1] = str(minute)
        elif duration >= cons_second and option_result > 0:  # Аналогично проверяем, но
            second = duration  # т.к. мы вводим секунды, это меньшее значение и его не требуется делить и т.д.
            duration = 0  # Можно было сделать и вычитанием, но я сделал так...
            list_result[0] = str(second)
    while code_result >= 0:
        result = result + list_result[code_result] + list_of_time[code_result]
        code_result -= 1
    print(result)
    #  Для удобства проверки, сделал повтор
    input('press any key to restart')
    print(100 * '\n')
    main()


main()
