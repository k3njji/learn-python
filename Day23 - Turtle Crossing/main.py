import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.moveUp, 'W')
screen.onkey(player.moveUp, 'w')

screen.onkey(player.moveLeft, 'a')
screen.onkey(player.moveLeft, 'A')

screen.onkey(player.moveRight, 'D')
screen.onkey(player.moveRight, 'd')

screen.onkey(player.moveDown, 'S')
screen.onkey(player.moveDown, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.createCar()
    car.move()

    if(player.ycor() == 280):
        player.refresh()
        car.levelUp()
        scoreboard.increase_level()

    if car.detect_collision(player):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()    