#4,5,6 Склад оргтехники
import datetime
class Sclad:
    def __init__(self, name, adress, tel):
        self.name = name
        self.adress = adress
        self.tel = tel

class Org_technics:
    def __init__(self, type, model, color, price, guarantee):
        self.type = type
        self.model = model
        self.color = color
        self.price = price
        self.guarantee = guarantee

    def transfer_to_sclad(self, numbers):
        self.numbers = numbers
        try:
            self.numbers = int(self.numbers)
            if self.type == 'Printer':
                with open('sclad_printer.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{self.type}, {self.model}, {self.color}, {self.numbers}, {datetime.datetime.now()}\n')
            elif self.type == 'Xerox':
                with open('sclad_xerox.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{self.type}, {self.model}, {self.color}, {self.numbers}, {datetime.datetime.now()}\n')
            elif self.type == 'Scanner':
                with open('sclad_scanner.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{self.type}, {self.model}, {self.color}, {self.numbers}, {datetime.datetime.now()}\n')
            else:
                with open('sclad_other.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{self.type}, {self.model}, {self.color}, {self.numbers}, {datetime.datetime.now()}\n')
        except ValueError:
            print('Неоюходимо указывать число')

class Printer(Org_technics):
    def __init__(self, type, model, color, price, guarantee, printing_technology):
        self.printing_technology = printing_technology
        super().__init__(type, model, color, price, guarantee)

class Xerox(Org_technics):
    def __init__(self, type, model, color, price, guarantee, number_of_copies):
        self.number_of_copies = number_of_copies
        super().__init__(type, model, color, price, guarantee)

class Scanner(Org_technics):
    def __init__(self, type, model, color, price, guarantee, effect_pixel):
        self.effect_pixel = effect_pixel
        super().__init__(type, model, color, price, guarantee)

articul1 = Printer('Printer', '25373GGGD', 'white', 5999, 2, 'лазерная')
articul2 = Scanner('Scanner', '253752572', 'white', 1999, 1, '124*3277')

print(articul1.price)

articul1.transfer_to_sclad(5)
articul1.transfer_to_sclad(2)
articul2.transfer_to_sclad('7')


