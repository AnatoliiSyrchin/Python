def thesaurus(*args):
    """делает словарь из имен сотрудников"""
    my_dict = {}
    for arg in args:
        key = arg[0]
        if my_dict.get(key) is None:
            my_dict[key] = [arg]
        else:
            my_dict[key].append(arg)
    return my_dict


print(thesaurus("Иван", "Петр", "Мария", "Илья"))
