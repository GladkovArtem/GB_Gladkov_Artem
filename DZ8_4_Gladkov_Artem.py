#4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так
def val_checker(func):
    def callback(arg):
        if arg < 0:
            return f'ValueError: wrong val {arg}'
        else:
            return func(arg)
    return callback

@val_checker
def calc_cube(x):
    return x ** 3

print(calc_cube(-5))
print(calc_cube(5))
print(calc_cube(0))
print(calc_cube(-3))
