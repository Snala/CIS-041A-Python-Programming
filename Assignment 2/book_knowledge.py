import turtle
from math import pi

bob = turtle.Turtle()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, sides):
    sides = sides
    angle = 360/sides
    for i in range(sides):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * pi * r
    n = int(circumference / 2) + 1
    length = circumference / n
    polygon(t, length, n)


square(bob, 50)
polygon(bob, 100, 9)
circle(bob, 100)
turtle.mainloop()
