my_list = []
with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        s_line = line.replace('"', '').split()
        my_list.append((s_line[0], s_line[5], s_line[6]))

dict_for_count = {}
for tpl in my_list:
    if tpl[0] in dict_for_count:
        dict_for_count[tpl[0]] += 1
    else:
        dict_for_count[tpl[0]] = 1
for k, v in dict_for_count.items():
    if v == max(dict_for_count.values()):
        print(f"IP спамера: {k}, количество запросов: {v}")
