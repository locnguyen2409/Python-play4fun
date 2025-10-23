class Car:
    def __init__(self, top_speed):
        self.top_speed = top_speed
        self.speed = 0

    def accelerate(self, change):
        self.speed += change
        if self.speed > self.top_speed:
            self.speed = self.top_speed
        if self.speed < 0:
            self.speed = 0

car = Car(149)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print("Current speed:", car.speed)
car.accelerate(-200)
print("Final speed:", car.speed)
