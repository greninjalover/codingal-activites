
class Vehicle:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def show_details(self):
        print("Name:", self.name)
        print("Colour:", self.colour)


class Car(Vehicle):
    def __init__(self, name, colour, type, seats):
        super().__init__(name, colour)
        self.type = type
        self.seats = seats

    def show_details(self):
        super().show_details()
        print("Type:", self.type)
        print("Number of seats:", self.seats)


my_car = Car("Toyota", "Red", "SUV", 5)

my_car.show_details()

print(issubclass(Car, Vehicle))
