from ball import Ball
from platform import Platform
from scoreboard import Scoreboard
from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(800, 650)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
ball = Ball()
platformOne = Platform(-350, 0)
platformTwo = Platform(350, 0)
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(platformOne.moveUp, "w")
screen.onkey(platformOne.moveDown, "s")
screen.onkey(platformTwo.moveUp, "Up")
screen.onkey(platformTwo.moveDown, "Down")
move = random.randint(1, 4)

while True:
    time.sleep(0.02)
    screen.update()
    ball.move()

    if ball.ycor() > 310 or ball.ycor() < -310:
        ball.bounce_y()

    if ball.distance(platformTwo) < 20 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(platformOne) < 20 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 390:
        scoreboard.left_point()
        ball.reset_position()

    if ball.xcor() < -390:
        scoreboard.right_point()
        ball.reset_position()


screen.exitonclick()
