from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args)
        log = ''
        for arg in args:
            log += f'{arg}: {type(arg)}, '
        print(f'{func.__name__} ({log.strip(", ")})')
        return result

    return wrapper


@type_logger
def calc_multi(*args):
    """multiplication of numbers"""
    result = 1
    for i in args:
        result *= i
    return result


if __name__ == '__main__':
    help(calc_multi)
    print(f'{calc_multi(5, 7, 8.3) = } ')
