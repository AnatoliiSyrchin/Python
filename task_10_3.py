class Cell:

    @staticmethod
    def check_other(other):
        if not isinstance(other, Cell):
            raise TypeError('должен быть тип Cell')

    def __init__(self, cells):
        if cells > 0:
            self.cells = cells
        else:
            raise ValueError('количество ячеек должно быть больше нуля')

    def __add__(self, other):
        self.check_other(other)
        sum_cells = self.cells + other.cells
        return Cell(sum_cells)

    def __sub__(self, other):
        self.check_other(other)
        sub_cells = self.cells - other.cells
        if sub_cells <= 0:
            return 'результат вычитания отрицательный'
        else:
            return Cell(sub_cells)

    def __mul__(self, other):
        self.check_other(other)
        mul_cells = self.cells * other.cells
        return Cell(mul_cells)

    def __floordiv__(self, other):
        self.check_other(other)
        floordiv_cells = self.cells // other.cells
        return Cell(floordiv_cells)

    def __truediv__(self, other):
        self.check_other(other)
        truediv_cells = self.cells / other.cells
        return Cell(truediv_cells)

    def __str__(self):
        return f'{self.cells} ячеек'

    def make_order(self, cells_in_row):
        row_count = self.cells // cells_in_row
        cells_string = f'во всех строках, кроме последней, {cells_in_row} звездочек\n'
        for _ in range(row_count):
            cells_string += '*' * cells_in_row + '\n'
        cells_string += '*' * (self.cells % cells_in_row)
        return cells_string


if __name__ == '__main__':
    cell_1 = Cell(25)
    cell_2 = Cell(10)
    print(f'cell_1 = {cell_1}')
    print(f'cell_2 = {cell_2}')
    print(f'cell_1 + cell_2 = {cell_1 + cell_2}')
    print(f'cell_1 - cell_2 = {cell_1 - cell_2}')
    print(f'cell_2 - cell_1 = {cell_2 - cell_1}')
    print(f'cell_1 * cell_2 = {cell_1 * cell_2}')
    print(f'cell_1 // cell_2 = {cell_1 // cell_2}')
    print(f'cell_1 / cell_2 = {cell_1 / cell_2}')
    print(cell_1.make_order(7))
