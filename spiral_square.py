import turtle
turtle.Screen().bgcolor("turquoise")
turtle.Screen().setup(300,400)
pencils=turtle.Turtle()

size=0
side=6
angle=360/side

while True:
    for i in range(side):
        pencils.forward(size+1)
        pencils.left(angle)

        size=size-5
    size=size+1

turtle.done()    

    



