#3 Осуществить программу работы с органическими клетками, состоящими из ячеек.
class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        if self.number - other.number > 0:
            return self.number - other.number
        else:
            return f'Во второй клетке не больше ячеек, чем в первой'

    def __mul__(self, other):
        return self.number * other.number

    def __floordiv__(self, other):
        return self.number // other.number

    def make_order(self, format_number):
        i = self.number//format_number
        result2 = str
        while i != 0:
            result = '*' * format_number
            if i != self.number//format_number:
                result2 = f'{result2}\\n{result}'
            else:
                result2 = result
            i -= 1

        k = self.number % format_number
        if k > 0:
            plus = '*' * k
            result2 = f'{result2}\\n{plus}'

        return result2

x = Cell(12)
y = Cell(10)

print(x.__add__(y))
print(x.__sub__(y))
print(x.__mul__(x))
print(x.__floordiv__(y))

print(x.make_order(5))