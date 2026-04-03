from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.refresh()

    def update(self):
        self.score = self.score+1
        self.clear()
        self.refresh()
        
    def refresh(self):
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align="center", font=('Arial', 12, 'normal'))