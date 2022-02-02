#4 Реализовать класс Stationery (канцелярская принадлежность).
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Пишет ручка')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Пишет карандаш')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Пишет маркер')

parent_stationery = Stationery('Канцеляркая принадлежность')
parent_stationery.draw()

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()

pen = Pen('Ручка Pilot')
print(pen.title)
pen.draw()
