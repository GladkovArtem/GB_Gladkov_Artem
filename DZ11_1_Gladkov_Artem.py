#1 Класс дата с валидацией
class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_parser(cls, date):
        list = date.split('-')
        day = int(list[0])
        month = int(list[1])
        year = int(list[2])
        return day, month, year

    @staticmethod
    def validation(date):
        list = Date.date_parser(date)
        if list[0] > 31 or list[0] < 0:
            print('Параметр "день" указан с ошибкой, исправьте')
        if list[1] > 12 or list[1] < 0:
            print('Параметр "месяц" указан с ошибкой, исправьте')
        if list[2] > 2022 or list[2] < 0:
            print('Параметр "год" указан с ошибкой, исправьте')


date1 = '32-13-1999'
Date.date_parser(date1)
Date.validation(date1)





