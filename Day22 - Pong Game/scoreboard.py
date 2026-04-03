from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.left_score}    {self.right_score}", align="center", font=("Courier", 30, "normal")) 

    def left_point(self):
        self.left_score += 1
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()