import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("blue")
t.pensize(3)
t.speed(3)

def draw_triangle(side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

draw_triangle(100)

t.penup()
t.goto(0, -58)
t.pendown()

t.setheading(0)
t.right(60)
draw_triangle(100)

t.hideturtle()
turtle.done()
#sorry maam this is the best i could do i tried my best i am so sorry
