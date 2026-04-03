from turtle import Turtle

class Platform(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=4.5, stretch_len=0.6)
        self.goto(x, y)
        self.movement = False

    def moveUp(self):
        if self.ycor() < 275:
            self.goto(self.xcor(), self.ycor() + 30)
        
        self.movement = True

    def moveDown(self):
        if self.ycor() > -275:
            self.goto(self.xcor(), self.ycor() - 30)

        self.movement = False