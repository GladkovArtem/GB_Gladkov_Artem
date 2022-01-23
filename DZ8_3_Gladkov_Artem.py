#3. Написать декоратор для логирования типов позиционных аргументов функции
def type_logger(func):
    def logger(*args):
        list_args = list(args)
        result = {}
        for i in list_args:
            result[i] = type(i)
            #print(f'{i}: {type(i)}')
        #return
        return print(f'{func.__name__} {result}')
    return logger

@type_logger
def calc_cube(x, y):
   return x ** 3+y

@type_logger
def print_text(*args):
   return args

calc_cube(5, 4)

print_text('Привет', 58 , 'Пока')
