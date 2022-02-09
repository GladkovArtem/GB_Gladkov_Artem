#3 Класс-исключение для контроля типа данных элемента списка
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

list = []
a = input("Введите число: ")
while a != 'stop':
    try:
        if a.isdigit():
            list.append(a)
        else:
            raise OwnError('Нужно вводить только числа!')
    except OwnError as err:
        print(err)
    finally:
        a = input("Введите число: ")

print(list)




