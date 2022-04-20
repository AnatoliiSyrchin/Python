class ComplexNumbers:
    def __init__(self, number):
        self.check_number(number)
        self.number = number

    @staticmethod
    def check_number(number):
        if type(number) != complex:
            raise ValueError(f'{number} не комплексное число')

    def __add__(self, other):
        if other.__class__ != ComplexNumbers:
            raise ValueError(f'{other} не экземпляр класса ComplexNumbers')
        return ComplexNumbers(self.number + other.number)

    def __mul__(self, other):
        if other.__class__ != ComplexNumbers:
            raise ValueError(f'{other} не экземпляр класса ComplexNumbers')
        return ComplexNumbers(self.number * other.number)


number_1 = ComplexNumbers(1 + 2j)
number_2 = ComplexNumbers(complex(2, 4))
print((number_1 + number_2).number)
print((number_1 * number_2).number)
