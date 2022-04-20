class WrongElement(Exception):
    pass


my_list = []

element = input('введите число или "stop" для завершения: ')
while element != 'stop':
    try:
        if element.isalpha():
            raise WrongElement('вводить можно только числа')
        else:
            my_list.append(element)
    except WrongElement as err:
        print(err)
    element = input('введите число или "stop" для завершения: ')

print('Вы вводили:', end=' ')
print(*my_list, sep=', ')
