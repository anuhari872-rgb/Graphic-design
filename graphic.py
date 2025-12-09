import turtle
import colorsys

s = turtle.Screen()
s.setup(900, 700)
s.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(3)
t.hideturtle()

h = 0
for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.color(c)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(1)
    t.begin_fill()
    t.color(c)
    t.fillcolor(c)

    t.forward(100)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(100)

    t.end_fill()
    h += 0.005

turtle.done()
