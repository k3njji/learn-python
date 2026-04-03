from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.segments = []

    def createCar(self):
        # if len(self.segments) < MAX_CARS:
            if random.randint(1, 3) == 1:
                car = Turtle()
                car.shape("square")
                car.shapesize(stretch_wid=1, stretch_len=2)
                car.penup()
                car.color(random.choice(COLORS))
                car.goto(300, random.randint(-250, 250))
                car.setheading(180)
                self.segments.append(car)

    def move(self):
        for segments in self.segments:
            segments.forward(STARTING_MOVE_DISTANCE)
            self.ends()

    def ends(self):
        for segment in self.segments[:]:
            if(segment.xcor() <= -300):
                segment.hideturtle()
                self.segments.remove(segment)

    def levelUp(self):
        global STARTING_MOVE_DISTANCE
        global MOVE_INCREMENT
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

    def detect_collision(self, player):
        for segment in self.segments:
            if player.distance(segment) < 10:
                return True
        return False