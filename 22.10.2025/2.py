class Car:
    def __init__(self, brand,color, mileage = 0):
        self.brand = brand
        self.color = color
        self.mileage = mileage
    def drive(self):
        print(f"Brand {self.brand} {self.color} driving {distance}")
car1 = Car("Mercedes", "red")
car2 = Car("Honda", "blue")
car1.drive()
car2.drive()