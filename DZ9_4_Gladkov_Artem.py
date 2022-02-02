#4 Реализуйте базовый класс Car
class Car:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction
    def go(self):
        if self.speed > 0:
            print(f'{self.name} {self.color} go')
        else:
            return
    def stop(self):
        if self.speed == 0:
            print(f'{self.name} {self.color} stop')
        else:
            return
    def turn(self):
        if self.direction.lower() == 'left':
            print(f'{self.name} {self.color} turn left')
        elif self.direction.lower() == 'right':
            print(f'{self.name} {self.color} turn right')
        else:
            return
    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name,is_police, direction)

    def show_speed(self):
        if self.speed > 60:
            print('OVER SPEED!!!')
        else:
            print(self.speed)



class SportCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name,is_police, direction)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)

    def show_speed(self):
        if self.speed > 60:
            print('OVER SPEED!!!')
        else:
            print(self.speed)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name,is_police, direction)


vaz2107 = TownCar(61, 'black', 'semerka', False, 'lEfT')
police = PoliceCar(244, 'blue', 'ford', True,'Right')
vaz2107.go()
vaz2107.stop()
print(vaz2107.is_police)
vaz2107.turn()

police.show_speed()
vaz2107.show_speed()

work = WorkCar(35, 'white', 'paz', False, '')
work.show_speed()
work.stop()
work.go




