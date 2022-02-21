bad_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
            'директор аэлита']
for people in bad_list:
    words = people.split(" ")
    print(f"Привет, {words[-1].title()}!")
