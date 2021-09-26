# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
#   взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
#   (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
import random


def get_jokes(n: int, flag=0):
    """
    :param n: number of jokes
    :param flag: 0 = free random, 1 = unique
    :return: result = str
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result = []
    if flag == 1:
        if n <= (len(nouns) or len(adverbs) or len(adjectives)):
            list_nons = random.sample(range(len(nouns)), n)
            list_adverbs = random.sample(range(len(adverbs)), n)
            list_adjectives = random.sample(range(len(adjectives)), n)
            for idx in range(n):
                result.append(f'{nouns[list_nons[idx]]} {adverbs[list_adverbs[idx]]} {adjectives[list_adjectives[idx]]}')
        else:
            return print('Данная операция невозможна, нет столько уникальных шуток')
    else:
        for idx in range(n):
            result.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return result


print(get_jokes(5, 1))
