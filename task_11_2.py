class MyDivZeroError(ZeroDivisionError):
    pass


number_1 = int(input('введите делимое: '))
number_2 = int(input('введите делитель: '))

try:
    if number_2 == 0:
        raise MyDivZeroError('нельзя делить на ноль')
    print(f'{number_1} / {number_2} = {number_1 / number_2}')
except MyDivZeroError as err:
    print(err)
