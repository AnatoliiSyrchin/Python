prices = [57.8, 46.51, 97, 32, 45.5, 215.2, 12, 98, 663, 32.8, 66.99, 77.7, 15]

# выводим цены
for idx in range(len(prices)):
    price = f"{prices[idx]:.2f}".split(".")
    if idx != len(prices) - 1:
        print(f"{price[0]} руб {price[1]} коп", end=", ")
    else:
        print(f"{price[0]} руб {price[1]} коп", end=".\n")

print()
print(f"Изначальный id списка: {id(prices)}")  # id до изменений
prices.sort() # сортируем список по возростанию
print("Отсортированные цены:")
for idx in range(len(prices)):
    price = f"{prices[idx]:.2f}".split(".")
    if idx != len(prices) - 1:
        print(f"{price[0]} руб {price[1]} коп", end=", ")
    else:
        print(f"{price[0]} руб {price[1]} коп", end=".\n")
print(f"id отсортированного списка: {id(prices)}")  # id после изменений

print()
prices_2 = prices[::-1]  # сортируем список по убыванию
print("Цены отсортированные по убыванию:")
for idx in range(len(prices_2)):
    price = f"{prices_2[idx]:.2f}".split(".")
    if idx != len(prices) - 1:
        print(f"{price[0]} руб {price[1]} коп", end=", ")
    else:
        print(f"{price[0]} руб {price[1]} коп", end=".\n")
print(f"id отсортированного списка: {id(prices_2)}")  # id после изменений

print("5 самых дорогих: ")
for idx in range(4,-1,-1):
    price = f"{prices_2[idx]:.2f}".split(".")
    if idx != 0:
        print(f"{price[0]} руб {price[1]} коп", end=", ")
    else:
        print(f"{price[0]} руб {price[1]} коп", end=".\n")
