#1,2* Написать генератор нечётных чисел от 1 до n (включительно) не используя ключевое слово yield
#n=int(input('Введите число n: '))
n=58
gen_odd_numbers = (n for n in range(1,n+1) if n%2!=0)
print(*gen_odd_numbers)
print()


#3 Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б'
]

gen_tuple = ((tutors[i],None) if i >= len(klasses) else (tutors[i],klasses[i]) for i in range(len(tutors)))
print(gen_tuple)
print(*gen_tuple)
print()
#print(next(gen_tuple))


#4 Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 23, 17, 17, 18,0, 321]
gen_result = (src[i] for i in range(1,len(src)) if src[i]>src[i-1])
print(*gen_result)
print()


#5 Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result =(src[i] for i in range(len(src)) if src.count(src[i])==1)
print(*result)

