my_list = []
with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        s_line = line.replace('"', '').split()
        my_list.append((s_line[0], s_line[5], s_line[6]))
print(my_list)
