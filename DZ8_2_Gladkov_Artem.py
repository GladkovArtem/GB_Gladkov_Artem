#2* Написать регулярное выражение для парсинга файла логов web-сервера

import re
import requests
response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
list = response.text

with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    for line in list:
        f.write(line)
new_list = list.split('\n')

for i in new_list:
    remote_addr = re.findall('\d+\.+\d+\.+\d+\.+[0-9]*', i)
    res = remote_addr[:1]

    date = re.findall(r'\[+.+\]', i)
    for x in date:
        res.append(x[1:len(x)-1])

    type = re.findall('\]+\s+\"+.+\s+\/', i)
    for t in type:
        res.append(t[3:len(t)-2])

    resource = re.findall('\s+\/+.+\/+.+\s+[H]', i)
    for r in resource:
        res.append(r[1:len(r)-2])

    response_code_size = re.findall('[0-9]+\s+[0-9]', i)
    for c in response_code_size:
        k = c.split(' ')
        for l in k:
            res.append(l)
        print(res)