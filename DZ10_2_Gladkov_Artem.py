#2 Одежда, расчет расхода ткани
class Clothes:
    def __init__(self, name, size_coat, suit_height):
        self.name = name
        self.size = size_coat
        self.height = suit_height

    @property
    def coat(self):
        v = self.size/6.5+0.5
        return round(v, 2)

    @property
    def suit(self):
        return self.height*2+0.3

    @property
    def result(self):
        return f'На {self.name} необходимо ткани: {self.suit+self.coat}'

articul1 = Clothes('Модный лук 1', 50, 185)
articul2 = Clothes('Модный лук 2', 48, 165)

print(articul1.coat)
print(articul2.height)
print(articul2.suit)
print(articul1.suit)
print(articul1.result)
print(articul2.result)






