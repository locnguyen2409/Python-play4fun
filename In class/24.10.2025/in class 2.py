class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        print("Some animal sound")

    def info(self):
        print(f"{self.name} is a {self.species}")

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion")

    def sound(self):
        print("Roar!")


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "Elephant")

    def sound(self):
        print("Trumpet!")


class Snake(Animal):
    def __init__(self, name):
        super().__init__(name, "Snake")

    def sound(self):
        print("Hiss!")

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the zoo!")

    def display_info(self):
        print(f"There are {len(self.animals)} animals in the zoo:")
        for animal in self.animals:
            animal.info()

    def make_sounds(self):
        print("All animals are making sounds!")
        for animal in self.animals:
            animal.sound()

z = Zoo()

z.add_animal(Lion("Lion"))
z.add_animal(Elephant("Elephant"))
z.add_animal(Snake("Snake"))

z.display_info()
z.make_sounds()
