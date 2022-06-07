import sys
from collections.abc import Mapping, Container
from sys import getsizeof
from random import random
import time


def deep_getsizeof(o, ids):
    d = deep_getsizeof
    if id(o) in ids:
        return 0

    r = getsizeof(o)
    ids.add(id(o))

    if isinstance(o, str):
        return r

    if isinstance(o, Mapping):
        return r + sum(d(k, ids) + d(v, ids) for k, v in o.iteritems())

    if isinstance(o, Container):
        return r + sum(d(x, ids) for x in o)
    return r


# Python 3.10.1 , x64
#1 по задаче ДЗ№3_3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

N = 10
E = []
print('sys N = 10000000 ', sys.getsizeof(N)) # 28 число
print('deep N = 10000000 ',deep_getsizeof(N, set())) # 28 число
print('sys пустой список', sys.getsizeof(E)) # 56 пустой список
print('sys пустой список', deep_getsizeof(E, set())) # 56 пустой список
turp1 = [0]*N
print('sys для массива с количеством N значений равных 0 ', sys.getsizeof(turp1)) #136: 56 +8*10 sys.getsizeof посчитал размер памяти для пустого списка и прибавил ссылки, но не прибавил размер 0
print('deep для массива с количеством N значений равных 0 ', deep_getsizeof(turp1, set())) #160: 56 +8*10+ 24 (для 0, с 1 числа занимают 28 байт)

for i in range(N):
    turp1[i] = int(random()*22)

print(turp1)
print('sys массива с рандомными значениями', sys.getsizeof(turp1)) #всегда 136:  56+8*10
print('deep массива с рандомными значениями', deep_getsizeof(turp1, set()))  #для массива [13, 15, 13, 13, 21, 19, 6, 11, 11, 19] 304: 56 + 8*10 + 28 *6 (6 разных значений, нет 0)
#алгоритм 1 с использованием range,len,del,insert, но без использования index
begin = time.perf_counter()
min_t = turp1[0]
print(sys.getsizeof(min_t)) #28 если первый элемент не 0, 24, если 0
min_i = 0
print(sys.getsizeof(min_i)) #24
max_t = turp1[0]
print(deep_getsizeof(max_t, set())) #28 если первый элемент не 0, 24, если 0
max_i = 0
print(deep_getsizeof(max_i, set())) #24

for i in range(len(turp1)):
    if turp1[i] > max_t:
        max_t = turp1[i]
        max_i = i
    if turp1[i] < min_t:
        min_t = turp1[i]
        min_i = i

del turp1[min_i]
print(turp1)
print('sys с удаленным 1 элементом', sys.getsizeof(turp1)) #всегда 136 (думал будет 128: 56+8*9)
print('deep с удаленным 1 элементом',deep_getsizeof(turp1, set()))  #3 варианта. Если удалился 0 и он был один в списке, то -24.
                                                                                # Если удалилось др.минимальное число и оно было 1 в списке, то -28.
                                                                                #Если удалился повторяющийся элемент, то задействованная память не изменилась.

turp1.insert(min_i, max_t)
del turp1[max_i]
turp1.insert(max_i, min_t)

print('sys вставка 1 элемента', sys.getsizeof(turp1)) #136 = исходному списку
print('deep вставка 1 элемента',deep_getsizeof(turp1, set())) # = исходному списку

# sys.getsizeof показывает большую погрешность, deep_getsizeof вычисляет задействованную память точно.

print()
dict_1 = {}
print('sys для пустого словаря', sys.getsizeof(dict_1)) #1
#print('deep для пустого словаря', deep_getsizeof({}, set())) #ошибка AttributeError: 'dict' object has no attribute 'iteritems'
alf = {'0': 0, '1': 1, '2': 2, '3': 3 , '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
alf_1 = {'0': 0}
alf_2 = {'0': 0, '1': 1, '2': 2,'3': 3 , '4': 4, '5': 5}
alf_3 = {'0': 0, '1': 1, '2': 2, '3': 3 , '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10}
print('sys для словаря c 1 ключом и значением', sys.getsizeof(alf_1)) #232
print('sys для словаря c 6 ключами и значениями', sys.getsizeof(alf_2)) # 360
print('sys для словаря c 11 ключами и значениями', sys.getsizeof(alf_3)) # 640
print('sys для словаря шестнадцетиричных чисел', sys.getsizeof(alf)) # 640

# как правильно прогнозировать выделение памяти для словаря не нашел. Независимые источники описывают процесс выделения памяти для dict так:
#Когда вы создаете пустой словарь, он предварительно распределяет память по частям для нескольких начальных ссылок, которые он может хранить.
# Поскольку словарь добавляет больше пар ключ-значение, ему требуется больше памяти.
# Но не с каждым добавлением; каждый раз, когда ему требуется больше места, он добавляет некоторый фрагмент памяти,
# который может вместить «X» пар ключ-значение, и после того, как количество «X» заполнено,  для словаря выделяется другой фрагмент памяти.
