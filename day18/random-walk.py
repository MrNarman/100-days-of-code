from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(5)

pen_colors = [
    "red", "blue", "green", "yellow", "orange", 
    "purple", "pink", "brown", "black", "cyan", 
    "gold", "violet", "magenta", "cyan", "turquoise", 
    "limegreen", "skyblue", "navy", "maroon", "chocolate"
]
angles = [0, 90, 180, 270]

for _ in range (200):

    tim.forward(20)
    tim.pencolor(random.choice(pen_colors))
    tim.setheading(random.choice(angles))

screen = Screen()
screen.exitonclick()