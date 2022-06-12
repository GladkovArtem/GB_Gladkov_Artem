#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random
import operator


def merge_sort(a, compare=operator.lt):
    if len(a) < 2:
        return a[:]
    else:
        middle = int(len(a) / 2)
        left = merge_sort(a[:middle], compare)
        right = merge_sort(a[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result



numbers = [random.randint(0,50) for i in range(20)]
print(numbers)
print(merge_sort(numbers))