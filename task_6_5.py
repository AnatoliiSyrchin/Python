import sys

file_users, file_hobbies, result_file = sys.argv[1:]

with open(file_users, 'r', encoding='utf-8') as f, open(file_hobbies, 'r', encoding='utf-8') as f2, \
        open(result_file, 'w', encoding='utf-8') as f3:
    for line in f:
        line2 = f2.readline()
        if line2:
            print(f'{line.strip()}: {line2.strip()}', file=f3)
        else:
            print(f'{line.strip()}: {None}', file=f3)
    if f2.readline():
        sys.exit(1)

with open(result_file, 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end="")
