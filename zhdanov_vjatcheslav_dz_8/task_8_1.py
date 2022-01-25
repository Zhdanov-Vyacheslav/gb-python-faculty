# Написать функцию email_parse(<email_address>), которая при помощи регулярного
#   выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает
#   их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в
#   регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?

import re
# Данная регулярка охватит основной спектр, но остается домен 1-го уровня
# решением может быть строгое ограничение почты из доменов "ru" и/или "com"
# Так же вместо [.][a-zA]+ сделать дополнительную группу и проверять её на сходства со списком
#   распарсив https://www.iana.org/domains/root/db, или что-то подобное
RE_E_MAIL = re.compile(r'^([a-zA-Z0-9][-a-zA-Z0-9._]+)@([a-zA-Z0-9][-a-zA-Z0-9._]+[.][a-zA]+)$')
user_email = 'username'
domain_email = 'domain'

print('Введите адрес почты')


def email_parse(e_mail_parse=input()):
    email_list = RE_E_MAIL.findall(e_mail_parse)
    if not email_list:
        raise ValueError(f'wrong email: {e_mail_parse}')
    else:
        email_dict = {user_email: email_list[0][0], domain_email: email_list[0][1]}
        print(email_dict)


email_parse()
