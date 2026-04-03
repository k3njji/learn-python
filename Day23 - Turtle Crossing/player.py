from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(1.5 , 1.5)
        self.refresh()

    def refresh(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def moveUp(self):
        if self.heading() != 90:
            self.setheading(90)
        
        self.forward(MOVE_DISTANCE)
    
    def moveRight(self):
        if self.heading() != 0:
            self.setheading(0)
        
        self.forward(MOVE_DISTANCE)
    
    def moveLeft(self):
        if self.heading() != 180:
            self.setheading(180)
        
        self.forward(MOVE_DISTANCE)

    def moveDown(self):
        if self.heading() != 270:
            self.setheading(270)
        
        self.forward(MOVE_DISTANCE)

    def collide(self):
        pass