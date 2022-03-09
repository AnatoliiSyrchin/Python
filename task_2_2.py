my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# создаем список с кавычками
my_list_2 = []
for i in range(len(my_list)):
    if my_list[i].isdigit():
        my_list_2.append('"')
        my_list_2.append(f"{int(my_list[i]):02d}")
        my_list_2.append('"')
    elif my_list[i][1:].isdigit():
        my_list_2.append('"')
        my_list_2.append(f"{my_list[i][0]}{int(my_list[i][1:]):02d}")
        my_list_2.append('"')
    else:
        my_list_2.append(my_list[i])

# боремся с пробелом (странный способ. до другого не додумался)
# склеиваем в строку, разбиваем по ", обрезаем пробелы, проверяем на циферность, меняем на цифры без пробелов
my_list_3 = " ".join(my_list_2).split('"')
for i in range(len(my_list_3)):
    if my_list_3[i].strip().isdigit() or my_list_3[i].strip()[1:].isdigit():
        my_list_3[i] = my_list_3[i].strip()
print('"'.join(my_list_3))
