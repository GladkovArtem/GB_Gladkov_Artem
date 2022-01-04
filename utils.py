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