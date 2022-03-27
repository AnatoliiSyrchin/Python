def odd_nums(number):
    """Генератор нечётных чисел от 1 до заданного числа"""
    for i in range(1, number + 1, 2):
        yield i


if __name__ == '__main__':
    odd_nums_15 = odd_nums(15)
    print(next(odd_nums_15))
    print(next(odd_nums_15))
    print(next(odd_nums_15))
    print(next(odd_nums_15))
    print(next(odd_nums_15))
    print(next(odd_nums_15))
    print(next(odd_nums_15))
    print(next(odd_nums_15))
    print(next(odd_nums_15))
