import sys

args = sys.argv[1:]
with open('bakery.csv', 'r', encoding='utf-8') as f:
    if not len(args):
        for line in f:
            print(line, end="")
    elif len(args) == 1:
        try:
            f.seek((int(args[0]) - 1) * 12)
        except ValueError:
            print('номер записи точно больше 0')
            sys.exit(1)
        for line in f:
            print(line, end="")
    elif len(args) == 2:
        try:
            f.seek((int(args[0]) - 1) * 12)
        except ValueError:
            print('номер записи точно больше 0')
            sys.exit(1)
        for i in range(int(args[1]) - int(args[0]) + 1):
            print(f.readline(), end="")
    else:
        print('show_sales.py может принимать максимум 2 параметра')
