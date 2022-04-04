from functools import wraps


def val_checker(check_func):
    def _val_checker(func):

        @wraps(func)
        def wrapper(arg):
            if check_func(arg):
                result = func(arg)
            else:
                raise ValueError(f'wrong val: {arg}')
            return result

        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """cubing a number"""
    return x ** 3


if __name__ == '__main__':
    help(calc_cube)
    print(f'{calc_cube(5) = } ')
