"""
CIS 41A - Assignment 2
Name: David Rios
Date: 4-16-19
"""

import turtle

bob = turtle.Turtle()


def reset(t, h_align, v_align):
    t.penup()
    t.goto(h_align, v_align)
    t.pendown()


def cartesian(t):
    for i in range(4):
        reset(t, 0, 0)
        t.fd(500)
        t.penup()
        t.lt(90)


def square(t, length, h_align, v_align):
    reset(t, h_align, v_align)
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, sides, h_align, v_align):
    reset(t, h_align, v_align)
    sides = sides
    angle = 360/sides
    for i in range(sides):
        t.fd(length)
        t.lt(angle)


def triangle(t, length, h_align, v_align):
    polygon(t, length, 3, h_align, v_align)


def rectangle(t, length, height, h_align, v_align):
    reset(t, h_align, v_align)
    for i in range(2):
        t.fd(length)
        t.lt(90)
        t.fd(height)
        t.lt(90)


cartesian(bob)
square(bob, 50, -150, -150)
polygon(bob, 50, 9, -200, 50)
triangle(bob, 75, 50, 50)
rectangle(bob, 60, 120, 100, -200)

# Causes turtle to pause at the end
turtle.mainloop()
