import turtle
turtle.Screen().bgcolor("turquoise")
turtle.Screen().setup(3000,4000,0,0)
polygon=turtle.Turtle()
sides=3600
angles=360/sides
length=1

for i in range(sides):
    polygon.forward(length)
    polygon.right(angles)

turtle.done()