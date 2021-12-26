#DZ_1.1
duration = 8863656
if duration//60 == 0:
    print(duration,'сек')
elif duration//60 > 0 and duration //(60 * 60)==0:
    print(duration//60,'мин',duration % 60, 'сек')
elif duration //(60 * 60) > 0 and duration //(24 * 60 * 60)==0:
    print(duration//(60 * 60),'час',duration//60 % 60,'мин',duration % 60,'сек')
else:
    print(duration // (60 * 60 * 24),'дн',duration //(60 * 60) % 24, 'час', duration // 60 % 60, 'мин', duration % 60, 'сек')
print()  #пробел между выводами разных заданий


#DZ_1.2
#Создать список, состоящий из кубов нечётных чисел от 1 до 1000
spisok_cubus=[]
for i in range(1,1001):
    if i%2!=0:
        spisok_cubus.append(i**3)
    i+=1
#print(spisok_cubus)

#задача а) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
summ_division_7=int()
for i in spisok_cubus:
    summ = int()
    a=i
    while a!=0:
        summ=summ+a%10
        a=a//10
    if summ%7==0:
        summ_division_7=summ_division_7+i
    i+=1
#print(summ_division_7)


#задача b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
new_spisok=[]
for i in spisok_cubus:
    new_spisok.append(i+17)
#print(new_spisok)

new_sum=int()
for i in new_spisok:
    summ = 0
    a=i
    while a!=0:
        summ=summ+a%10
        a=a//10
    if summ%7==0:
        new_sum=new_sum+i
    i+=1
#print(new_sum)


#задача c) * Решить задачу под пунктом b, не создавая новый список

new_sum2=int()
for i in spisok_cubus:
    summ = int()
    a=i+17
    while a!=0:
        summ=summ+a%10
        a=a//10
    if summ%7==0:
        new_sum2=new_sum2+i+17
    i+=1

#print(new_sum2)


#DZ_1.3 Склонение слова
procent_sclon = []
for i in range(1,101):
    procent_sclon.append(i)

for i in procent_sclon:
    if i==1 or i%10==1 and i!=11:
        print(i,'процент')
    elif i>=12 and i<=14:
        print(i, 'процентов')
    elif i==2 or i==3 or i==4 or i%10==2 or i%10==3 or i%10==4:
        print(i,'процента')
    else:
        print(i,'процентов')
