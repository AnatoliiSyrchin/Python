def num_translate_adv(number):
    number_translate = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }

    if number.istitle:
        if number_translate.get(number.lower()) is None:
            return None
        else:
            return number_translate.get(number.lower()).title()
    else:
        return number_translate.get(number)


print(num_translate_adv("Seven"))
