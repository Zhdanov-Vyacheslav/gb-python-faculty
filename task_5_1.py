# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
#
n = 15

def nums_generator(max_nums):
    for num in range(1, max_nums + 3, 2):
        yield num if num <= max_nums else print('...StopIteration...')


if __name__ == '__main__':
    odd_to_15 = nums_generator(n)
    for _ in odd_to_15:
        print(_)



