#2 Класс-исключение, при делении на ноль
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = input("Введите числитель: ")
b = input("Введите знаменатель: ")

try:
    a = int(a)
    b = int (b)
    if b == 0:
        raise OwnError('На ноль делить нельзя!')
except ValueError:
    print('Нужно вводить только числа')
except OwnError as err:
    print(err)
else:
    print(f'Результат деления:', a/b)





