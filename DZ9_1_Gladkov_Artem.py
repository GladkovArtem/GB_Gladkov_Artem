#1 Светофор
class TrafficLight:
    def running(self):
        import time
        while True:
            self.color = 'Красный'
            print(self.color)
            time.sleep(7)
            self.color = 'Жёлтый'
            print(self.color)
            time.sleep(2)
            self.color = 'Зелёный'
            print(self.color)
            time.sleep(7)

x = TrafficLight()
x.running()
