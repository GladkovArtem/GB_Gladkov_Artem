#7 Комплексные числа
class Numbers_complexus:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a + other.a}+{self.b + other.b}i'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b}+{self.a * other.b + self.b * other.a}i'



number1 = Numbers_complexus(12, 6)
number2 = Numbers_complexus(1, 15)
print(number1 + number2)
print(number1 * number2)




