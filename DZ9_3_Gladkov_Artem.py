#3 Работники и их доход
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        dict = {'wage': wage, 'bonus': bonus}
        self.income = dict['wage'] + dict['bonus']

class Position(Worker):
    def get_full_name(self):
        print(f'{self.surname} {self.name}')

    def get_total_income(self):
        print(self.income)

worker1 = Position('Иван', 'Иванов', 'бухгалтер', 50000, 10000)
worker2 = Position('Петр', 'Петров', 'продавец', 30000, 2000)
worker3 = Position('Игорь', 'Смирнов', 'программист', 800000, 327000)


worker1.get_full_name()
worker1.get_total_income()
worker2.get_full_name()
worker2.get_total_income()
worker3.get_full_name()
worker3.get_total_income()

print(worker2.position)







