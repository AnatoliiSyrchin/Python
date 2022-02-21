my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i].isdigit():
        my_list.insert(i + 1, '"')
        my_list[i] = f"{int(my_list[i]):02d}"
        my_list.insert(i, '"')
    elif my_list[i][1:].isdigit():
        my_list.insert(i + 1, '"')
        operand = my_list[i][0]
        my_list[i] = f"{operand}{int(my_list[i][1:]):02d}"
        my_list.insert(i, '"')
print("список через for:")
print(my_list)  # смотрим, что кавычки на месте

my_list_2 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#  придумал ещё способ через while, но тут главное в индексах не запутаться
j = 0
while j < len(my_list_2):
    if my_list_2[j].isdigit():
        my_list_2.insert(j, '"')
        my_list_2[j + 1] = f"{int(my_list_2[j + 1]):02d}"
        my_list_2.insert(j + 2, '"')
        j = j + 3
    elif my_list_2[j][1:].isdigit():
        my_list_2.insert(j, '"')
        operand = my_list[j + 1][0]
        my_list_2[j + 1] = f"{operand}{int(my_list_2[j + 1]):02d}"
        my_list_2.insert(j + 2, '"')
        j = j + 3
    else:
        j += 1
print("список через while:")
print(my_list_2)  # смотрим, что кавычки на месте

my_string = ""  # новую строку делать вроде не запрещено
for idx in range(len(my_list)):
    if idx == len(my_list) - 1:  # если последний элемент списка, то просто склеиваем
        my_string += f"{my_list[idx]}"
    elif my_list[idx + 1].isdigit() or my_list[idx + 1][1:].isdigit():  # если следующий - число, то просто склеиваем
        my_string += my_list[idx]
    elif my_list[idx].isdigit() or my_list[idx][1:].isdigit():  # если элемент число, то просто склеиваем
        my_string += my_list[idx]
    else:  # в остальных случаях, склеиваем с пробелом
        my_string += f"{my_list[idx]} "
print(my_string)
