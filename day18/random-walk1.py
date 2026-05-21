import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
tim.pensize(5)
tim.speed("fastest")

def random_color():
    """
        generates rgb values for the random walk
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_tuple = (r, g, b)

    return color_tuple

angles = [0, 90, 180, 270]

for _ in range (200):

    tim.forward(20)
    tim.pencolor(random_color())
    tim.setheading(random.choice(angles))

screen = Screen()
screen.exitonclick()