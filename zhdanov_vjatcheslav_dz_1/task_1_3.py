numbers = 100

for idx in range(1, numbers):
    if idx // 10 != 1:
        if idx % 10 == 1:
            print(str(idx) + ' процент')
        elif idx % 10 == 2 or idx % 10 == 3 or idx % 10 == 4:
            print(str(idx) + ' процента')
        else:
            print(str(idx) + ' процентов')
    else:
        print(str(idx) + ' процентов')
