class Pets:
    def __init__(self, name, animal, age, colour):
        self.name = name
        self.animal = animal
        self.age = age
        self.colour = colour

    def show_profile(self):
        print("Pet Name:", self.name)
        print("Animal:", self.animal)
        print("Age:", self.age)
        print("Colour:", self.colour)
        print()


pet1 = Pets("Buddy", "Dog", 5, "Brown")
pet2 = Pets("Luna", "Cat", 3, "White")
pet3 = Pets("Charlie", "Rabbit", 2, "Grey")
pet4 = Pets("Kiwi", "Bird", 1, "Green")

print("PET PROFILES")
print()

pet1.show_profile()
pet2.show_profile()
pet3.show_profile()
pet4.show_profile()