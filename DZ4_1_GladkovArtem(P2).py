#1 по задаче ДЗ№3_3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import random
import time

N = 10000000
turp1 = [0]*N
for i in range(N):
    turp1[i] = int(random()*22)
#print(turp1)

#алгоритм 1 с использованием range,len,del,insert, но без использования index
begin = time.perf_counter()
min_t = turp1[0]
min_i = 0
max_t = turp1[0]
max_i = 0
for i in range(len(turp1)):
    if turp1[i] > max_t:
        max_t = turp1[i]
        max_i = i
    if turp1[i] < min_t:
        min_t = turp1[i]
        min_i = i

del turp1[min_i]
turp1.insert(min_i, max_t)
del turp1[max_i]
turp1.insert(max_i, min_t)
#print(turp1)
print('time = ', time.perf_counter() - begin)  #время выполнения для 10 млн элементов 2,60059%. Если выводить на экран итоговый список, то время = 4,85854%

#алгоритм 2 с range и len, но без использования del и insert
begin = time.perf_counter()
min_t = turp1[0]
min_i = 0
max_t = turp1[0]
max_i = 0
for i in range(len(turp1)):
    if turp1[i] > max_t:
        max_t = turp1[i]
        max_i = i
    if turp1[i] < min_t:
        min_t = turp1[i]
        min_i = i

turp1[max_i], turp1[min_i] = turp1[min_i], turp1[max_i]
#print(turp1)
print('time = ', time.perf_counter() - begin)  #время выполнения для 10 млн элементов 2,54420%. Если выводить на экран итоговый список, то время = 2,49091%

#алгоритм 3 без использования del,insert,range,len но с использованием index
begin = time.perf_counter()
min_t = turp1[0]
min_i = 0
max_t = turp1[0]
max_i = 0
for i in turp1:
    if i > max_t:
        max_t = i
        max_i = turp1.index(i)
    if i < min_t:
        min_t = i
        min_i = turp1.index(i)

turp1[max_i], turp1[min_i] = turp1[min_i], turp1[max_i]
#print(turp1)
print('time = ', time.perf_counter() - begin) #время выполнения для 10 млн элементов 1,56361%. Если выводить на экран итоговый список, то время = 3,82579%

#алгоритм 4 без использования range,len но с использованием index ,del,insert,
begin = time.perf_counter()
min_t = turp1[0]
min_i = 0
max_t = turp1[0]
max_i = 0
for i in turp1:
    if i > max_t:
        max_t = i
        max_i = turp1.index(i)
    if i < min_t:
        min_t = i
        min_i = turp1.index(i)

del turp1[min_i]
turp1.insert(min_i, max_t)
del turp1[max_i]
turp1.insert(max_i, min_t)
#print(turp1)
print('time = ', time.perf_counter() - begin) #время выполнения для 10 млн элементов 1,80388%. Если выводить на экран итоговый список, то время = 3,83363%

# В итоге по скоросте работы оптимальным оказался алгоритм 3 без использования del,insert,range,len но с использованием index
# Однако, если требуется выводить результат на экран, то оптимальным получился алгоритм 1 с range и len, но без использования del и insert