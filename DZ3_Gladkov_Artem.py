#1 Создать функцию, переводящую числа с английского на русский

num_dict = {
    'null': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def  num_translate(number):
    for key,value in num_dict.items():
        if number in key:
            print(value)
    return None

num_translate('seven')
print()

#2* Переработать функцию num_translate для обработки числительных, начинающихся с большой буквы

def  num_translate_adv(number):
    for key,value in num_dict.items():
        if number in key:
            print(value)
        elif number.lower() in key:
            print(value.title())
    return None

num_translate_adv('Six')
print()

#3  Написать функцию, принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

def thesaurus(name1, name2, name3, name4):
    dict_sotr= {name1[0]:[],name2[0]:[],name3[0]:[],name4[0]:[]}
    for k,v in dict_sotr.items():
        if k in name1[0]:
            v.append(name1)
        if k in name2[0]:
            v.append(name2)
        if k in name3[0]:
            v.append(name3)
        if k in name4[0]:
            v.append(name4)
    print(dict_sotr)
    return (dict_sotr)

thesaurus('Иван','Петр','Мария','Илья')
print()

#4* Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.

#5 Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n):
    import random
    list_jokes=[]
    while n != 0:
        a = random.randint(0, len(nouns) - 1)
        b = random.randint(0, len(adverbs) - 1)
        c = random.randint(0, len(adjectives) - 1)
        list_jokes.append(nouns[a]+' ' + adverbs[b]+' ' + adjectives[c])
        n = n-1
    return(list_jokes)

print(get_jokes(5))
