import sys
import json

with open('users.csv', 'r', encoding='utf-8') as f, open('hobby.csv', 'r', encoding='utf-8') as f2, open(
        'users_hobby.json', 'w', encoding='utf-8') as f3:
    users = f.read().splitlines()
    hobby = f2.read().splitlines()
    if len(users) >= len(hobby):
        users_hobby = {users[i]: (hobby[i] if i < len(hobby) else None) for i in range(len(users))}
    else:
        sys.exit(1)
    json.dump(users_hobby, f3, ensure_ascii=False, indent=4)

with open('users_hobby.json', 'r', encoding='utf-8') as f:
    print(json.load(f))
