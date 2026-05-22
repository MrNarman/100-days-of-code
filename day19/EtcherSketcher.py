'''
w = forwards
s = backwards
d = clockwise
a = counter-clockwise
c = clear drawings
'''

from turtle import Turtle, Screen, resetscreen

tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_clockwise():
    tim.right(10)

def move_counter_clockwise():
    tim.left(10)

screen = Screen()
screen.listen()

screen.onkey(key= "w", fun= move_forward)
screen.onkey(key= "s", fun= move_backward)
screen.onkey(key= "c", fun= resetscreen)
screen.onkey(key= "d", fun= move_clockwise)
screen.onkey(key= "a", fun= move_counter_clockwise)

screen.exitonclick()