class Car:
    def __init__(self, brand,color, mileage = 0, fuel = 100):
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.fuel = fuel
    def drive(self, distance):
        fuel_needed = distance * 0.5
        if fuel_needed > self.fuel:
            print("Not enough fuel")
        else:
            self.mileage += distance
            self.fuel -= fuel_needed
            print(f"Drove {distance} km")
            print(f"New mileage: {self.mileage} km")
            print(f"Remaining fuel: {self.fuel:.2f}%")
car1 = Car("Mercedes", "red")
car1.drive(100)
car1.drive(50)