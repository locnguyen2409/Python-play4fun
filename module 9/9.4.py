import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
cars = []
for i in range (1,11):
    registration_number = f"ABC-{i}"
    max_speed = random.randint(100,200)
    cars.append(Car(registration_number, max_speed))
race_over=0
hour=0
while race_over:
    hour += 1
    for car in cars:
        speed_change = random.randint(-10,15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.travelled_distance > 10000:
            race_over = True
            break
print(f"\n Race finished in {hour} hours!\n")
print(f"{'Car':<10}{'Max Speed':<12}{'Current Speed':<15}{'Distance Travelled (km)':<25}")
print("-" * 65)
for car in cars:
    print(f"{car.registration_number:<10}{car.max_speed:<12}{car.current_speed:<15}{car.travelled_distance:<25.1f}")