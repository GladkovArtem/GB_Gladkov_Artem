#1 Не используя библиотеки для парсинга, распарсить файл логов web-сервера nginx_logs.txt
#(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)

import requests
response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
list = response.text

with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    for line in list:
        f.write(line)

result=[]
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        new_list = line.split(' ')
        x = (new_list[0],new_list[5],new_list[6])
        result.append(x)

#2* (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.

import requests
from collections import Counter
response2 = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
list2 = response2.text

with open('nginx2_logs.txt', 'w', encoding='utf-8') as f:
    for line in list2:
        f.write(line)

result2=[]
with open('nginx2_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        new_list = line.split(' ')
        x = (new_list[0])
        result2.append(x)

count = Counter(result2).most_common(1)
print(count)

#3 Есть два файла. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
list_fio=[]
list_hobby=[]
with open('user.csv', 'r', encoding='utf-8') as f:
    for line in f:
        list_fio.append(line[:len(line)-1])

with open('hobby.csv', 'r', encoding='utf-8') as f:
    for line in f:
        list_hobby.append(line[:len(line)-1])

if len(list_fio) >= len(list_hobby):
    for i in range(len(list_hobby),len(list_fio)):
        list_hobby.append(None)
    result = dict(zip(list_fio, list_hobby))
    with open('dict_DZ6_3.py', 'w', encoding='utf-8') as f:
        f.write(str(result))
else:
    raise SystemExit(1)

print(result)

#6 Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
#show_sales.py add_sale.py bakery.csc
