#2 Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.

def currency_rates(currency):
    currency= currency.upper()
    import requests
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    all_currency = response.text.split('</')
    cur='NumCode><CharCode>'
    val='Name><Value>'
    list_currency=[]
    for i in all_currency:
        if cur in i:
            list_currency.append(i[18:])
        if val in i:
            list_currency.append(i[12:])
    for i in list_currency:
        if i == currency:
            result = list_currency[list_currency.index(i)+1]
            result = result.replace(',','.')
            return float(result)
    return None

print(currency_rates('usD'))
print(currency_rates('EUR'))
print(currency_rates('EEEhrthhrt'))
print()

#3*  Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера

#4 Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().

import utils
utils.currency_rates('gbp')
utils.currency_rates('dnggdjhgjg')
utils.currency_rates('BRL')
print(utils.currency_rates('dkk'))
print(utils.currency_rates('usd'))
print(utils.currency_rates('EUR'))