#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
def sum_mult(n):
    sum = 0
    mult = 1
    if type(n) == int and len(str(n))==3:
        while (n != 0):
            sum = sum + n % 10
            mult = mult * n % 10
            n = n // 10
        print('Сумма цифр трехзначного числа: ', sum)
        print('Произведение цифр трехзначного числа: ', mult)
    else:
        print('Трехзначное число не введено, попробуйте еще раз')

if __name__=='__main__':
    n = int(input('Введите трехзначное число: '))
    sum_mult(n)


#3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
def equation_of_a_straight_line(x1, y1, x2, y2):
    k = (y1-y2)/(x1-x2)
    b = y1-k*x1
    if b < 0:
        print(f'Уравнение прямой: y={k}x{b}')
    else:
        print(f'Уравнение прямой: y={k}x+{b}')

if __name__ == '__main__':
    x1 = int(input('Введите координату x первой точки: '))
    y1 = int(input('Введите координату y первой точки: '))
    x2 = int(input('Введите координату x второй точки: '))
    y2 = int(input('Введите координату y второй точки: '))
    equation_of_a_straight_line(x1, y1, x2, y2)




#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
def number_letter(l):
    import string
    if 0< l <=26:
        print(string.ascii_letters[l-1])
    else:
        print('Нет такой буквы')

if __name__ == '__main__':
    l = int(input('Введите номер буквы алфавита: '))
    number_letter(l)


#8. Определить, является ли год, который ввел пользователем, високосным или невисокосным
def leap_year(ly):
     if ly >0:
         if ly % 4 != 0:
             print('Невисокосный')
         elif ly % 100 == 0:
             if ly % 400 == 0:
                 print('Високосный')
             else:
                 print('Невисокосный')
         else:
             print('Високосный')
     else:
        print('Год не может быть отрицательным')

if __name__ == '__main__':
    ly = int(input('Введите год: '))
    leap_year(ly)

#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def average_number(c, d, e):
    if  c == d or c == e or d == e:
        print('Среднего числа нет, введены равные 2 или 3 числа')
    else:
        if d < c < e or e < c < d:
            print(c)
        elif c < d < e or e < c < d:
            print(d)
        else:
            print(e)

if __name__ == '__main__':
    c = int(input('Введите первое число: '))
    d = int(input('Введите второе число: '))
    e = int(input('Введите третье число: '))
    average_number(c, d, e)