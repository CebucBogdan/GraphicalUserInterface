import turtle
from math import pi

bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n ,length):
    degrees = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(degrees)



def circle(t, r):
    circumference = 2 * pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)


def arc(angel):
    arc_length = 2 * pi * r * angel/360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

turtle.mainloop()