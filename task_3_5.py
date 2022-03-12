from random import choice, randrange


def get_jokes(number, flag=False):
    """
    Генератор шуток

    :number: количество шуток
    :flag: возможность повтора слов
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "странный"]
    jokes = []
    if flag:
        for i in range(number):
            joke = f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"
            jokes.append(joke)
    else:
        if number > min(len(nouns), len(adverbs), len(adjectives)):
            return f"Максимум {min(len(nouns), len(adverbs), len(adjectives))} загадок"
        else:
            for i in range(number):
                joke = f"{nouns.pop(randrange(len(nouns)))} {adverbs.pop(randrange(len(adverbs)))}" \
                       f" {adjectives.pop(randrange(len(adjectives)))}"
                jokes.append(joke)
    return jokes


print(get_jokes(7, True))
