class Matrix:

    @staticmethod
    def check_matrix(matrix):
        if not matrix or not isinstance(matrix, list) or not isinstance(matrix[0], list):
            raise TypeError("должен быть список списков")
        len_row = len(matrix[0])
        for row in matrix:
            if not isinstance(row, list) or len(row) != len_row:
                raise TypeError("должен быть список списков одинаковой длины")
            for el in row:
                if not isinstance(el, (int, float)):
                    raise TypeError("все элементы должны быть числами")

    def __init__(self, matrix):
        self.check_matrix(matrix)
        self.matrix = matrix

    def __str__(self):
        matrix_str = ''
        for row in self.matrix:
            for el in row:
                matrix_str += str(el) + " "
            matrix_str += '\n'
        return matrix_str

    def __add__(self, other):
        if len(self.matrix[0]) != len(other.matrix[0]) or len(self.matrix) != len(other.matrix):
            raise TypeError('матрицы должны быть одинаковыми')
        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append(list(map(lambda x, y: x + y, self.matrix[i], other.matrix[i])))
        return Matrix(new_matrix)


if __name__ == '__main__':
    matrix_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix_2 = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    matrix_3 = [
        [100, 200, 300],
        [400, 500, 600],
        [700, 800, 900]
    ]
    my_matrix_1 = Matrix(matrix_1)
    my_matrix_2 = Matrix(matrix_2)
    my_matrix_3 = Matrix(matrix_3)
    print(my_matrix_1)
    print(my_matrix_2)
    print(my_matrix_3)
    print(f'my_matrix_1 + my_matrix_2 + my_matrix_3 = \n{my_matrix_1 + my_matrix_2 + my_matrix_3}')
