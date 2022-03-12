def thesaurus_adv(*args):
    """делает словарь из имен и фамилий сотрудников"""
    my_dict = {}
    for arg in args:
        people = arg.split()
        key_name = people[0][0]
        key_surname = people[1][0]
        if my_dict.get(key_surname) is None:
            my_dict[key_surname] = {key_name: [arg]}
        else:
            if my_dict[key_surname].get(key_name) is None:
                my_dict[key_surname][key_name] = [arg]
            else:
                my_dict[key_surname][key_name].append(arg)
    return my_dict


def sort_dict(some_dict):
    """сортировка словаря с вложенными словарями"""
    some_dict = dict(sorted(some_dict.items()))
    for key in some_dict.keys():
        some_dict[key] = dict(sorted(some_dict[key].items()))
        for value in some_dict[key].values():
            value.sort()
    return some_dict


my_dict = thesaurus_adv("Инна Серова", "Иван Сергеев", "Петр Алексеев", "Илья Иванов", "Аня Сидорова", "Анна Савельева")
print(my_dict)
print(sort_dict(my_dict))
