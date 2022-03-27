src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

temp_dict = {}
for i in src:
    temp_dict[i] = 1 if i not in temp_dict else 'not one'
result = [j for j in temp_dict if temp_dict[j] == 1]
print(f"{result = }")
