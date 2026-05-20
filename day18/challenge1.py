from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

i = 0
sides = [3, 4, 5, 6, 7, 8, 9, 10]
colors = ["red", "blue", "green", "yellow", "orange", "purple", "black", "cyan"]

for _ in range(len(sides)):
    angle_to_turn = 360/(sides[i])
    tim.pencolor(random.choice(colors))
    for _ in range (sides[i]):
        tim.right(angle_to_turn)
        tim.forward(100)
    i += 1

screen = Screen()
screen.exitonclick()
