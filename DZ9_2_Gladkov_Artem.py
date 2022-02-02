#2 Дорога
class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

        weight_m2 = 25
        thickness = 5
        result = length * width * weight_m2 * thickness
        print(f'{result/1000} т.')

Road(20, 5000)


