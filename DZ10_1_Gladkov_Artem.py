#1 Работа с матрицами (не выполнено, поплыл в постановке задачи....)
class Matrix:
    def __init__(self, list):
        self.list = list

    def create(self):
        for i in self.list:
            print(i)

    def __str__(self):
        return f'{self.list}'

    def __add__(self, other):
        return map(self.list + other.list)


matrix_list1 = [
    [12, 7, -1],
    [9, 0, 4],
    [3898, -888, 5]
]

matrix_list2 = [
    [775, -60, 25],
    [-9, 10, 74],
    [-3898, 888, -5]
]

x = Matrix(matrix_list1)
x.create()

print(x.__str__())


