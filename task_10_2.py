from abc import ABC, abstractmethod


class Clothes(ABC):

    all_fabric = 0

    def __init__(self):
        self._fabric = 0

    @property
    def fabric(self):
        if not self._fabric:
            self._fabric = self.calculating_fabric()
            Clothes.all_fabric += self._fabric
        return self._fabric

    @abstractmethod
    def calculating_fabric(self):
        pass

    def __str__(self):
        if self.__class__ == Coat:
            return f'расход ткани на пальто {self.fabric:.2f}'
        else:
            return f"расход ткани на косстюм {self.fabric:.2f}"


class Coat(Clothes):

    def __init__(self, v):
        super().__init__()
        self.v = float(v)

    def calculating_fabric(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, h):
        super().__init__()
        self.h = float(h)

    def calculating_fabric(self):
        return 2 * self.h + 0.3


if __name__ == '__main__':
    coat_1 = Coat(32)
    coat_2 = Coat(48)
    suit_1 = Suit(1.8)
    suit_2 = Suit(1.65)
    print(coat_1)
    print(coat_2)
    print(suit_1)
    print(suit_2)
    print(f'всего потрачено ткани: {Clothes.all_fabric:.2f}')
