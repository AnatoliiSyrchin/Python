import sys

with open('users.csv', 'r', encoding='utf-8') as f, open('hobby.csv', 'r', encoding='utf-8') as f2, \
        open('users_hobby.txt', 'w', encoding='utf-8') as f3:
    for user in f:
        hobbies = f2.readline()
        if hobbies:
            print(f'{user.strip()}: {hobbies.strip()}', file=f3)
        else:
            print(f'{user.strip()}: {None}', file=f3)
    if f2.readline():
        sys.exit(1)

with open('users_hobby.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end="")
