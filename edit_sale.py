import sys

if len(sys.argv) == 3:
    line = int(sys.argv[1])
    price = sys.argv[2]
else:
    print('edit_sale.py должен иметь 2 параметра')
    sys.exit(1)

with open('bakery.csv', 'r+', encoding='utf-8') as f:
    if f.seek(0, 2) < line * 12 or line <= 0:
        print('нет такой записи')
        sys.exit(1)
    f.seek((line - 1) * 12)
    print(f'{price.ljust(10)}', file=f)
