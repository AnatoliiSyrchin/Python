import sys

if len(sys.argv) == 2:
    price = sys.argv[1]
else:
    print('add_sale.py должен иметь 1 параметр')
    sys.exit(1)

with open('bakery.csv', 'a', encoding='utf-8') as f:
    print(f'{price.ljust(10)}', file=f)
