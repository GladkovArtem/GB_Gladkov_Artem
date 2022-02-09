#1 Работа с матрицами (не выполнено, поплыл в постановке задачи....)
class Matrix:
    def init(self, matrix_list):
        self.matrix = matrix_list

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        for row_matrix in range(len(self.matrix)):
            for row_num in range(len(other.matrix[row_matrix])):
                self.matrix[row_matrix][row_num] = self.matrix[row_matrix][row_num] + other.matrix[row_matrix][row_num]
        return Matrix.__str__(self)

list1 = [
    [1, 2, 3, 5],
    [4, 5, 6, 2],
    [9, 8, 7, 6]
]
matrix_a = Matrix(list1)
matrix_b = Matrix([[8, 5, 7, 3], [9, 2, 1, 7], [3, 6, 4, 9]])
print(matrix_a)
print(matrix_a + matrix_b)
