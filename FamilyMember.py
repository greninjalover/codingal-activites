class FamilyMember:
    def __init__(self, eye_colour, height_cm):
        self.eye_colour = eye_colour
        self.height_cm = height_cm

    def showtraits(self):
        print("Eye Colour:", self.eye_colour)
        print("Height(cm):", self.height_cm)

class Kid(FamilyMember):
    def __init__(self, name, age, eye_colour, height_cm):
        self.name=name
        self.age=age

        super().__init__(eye_colour, height_cm)

    def showtraits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().showtraits()

child= Kid("Ramcharan",12 ,"Brown", 143)
child.showtraits()
