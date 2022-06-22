#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random


M = 10
def mediana(a):
    med = sum(a)/len(a)    # находим среднее арифметическое объектов списка
    lst_min = []
    lst_max = []
    for i in range(len(a)): #разделяем исходный массив на два
        if a[i] < med:
            lst_min.append(a[i])
        else:
            lst_max.append(a[i])
    delta = len(lst_max) - len(lst_min)
    while abs(delta) != 1: #решение действительно только для массива с нечетным количеством ячеек.
        if delta > 0:      #если "правый" список больше, то медиана в нем, удаляем максимальный элемент пока длины массивов не будут различаться на 1 (минимум будет медианой)
            lst_max.remove(max(lst_max))
        else:              #иначе работаем с "левым" списком и максимальный элемент в нем (при разнице длин 1) будет медианой
            lst_min.remove(min(lst_min))
        delta = abs(delta) - 1
    if delta > 0:
        return min(lst_max)
    else:
        return max(lst_min)

numbers = [random.randint(-100, 100) for i in range(2 * M +1)]
print(numbers)
print(mediana(numbers))

#для проверки по отсортированному списку
def buble_sort(a):
    final = True
    while final:  # если массив будет уже отсортирован (не найдется меньшее значение), то завершаем цикл
        final = False
        for i in range(len(a) - 1):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                final = True
    return a

print(buble_sort(numbers))
print(numbers[M])