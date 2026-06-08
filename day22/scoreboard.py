from turtle import Turtle

FONT_TYPE = "Courier"
FONT_SIZE = 65
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align= ALIGNMENT, font=(FONT_TYPE, FONT_SIZE, "normal"))
        
        self.goto(100, 200)
        self.write(self.right_score, align= ALIGNMENT, font=(FONT_TYPE, FONT_SIZE, "normal"))


    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()