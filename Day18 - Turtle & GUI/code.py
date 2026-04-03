from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

# making a square
# head = 90
# for i in range(4):
#     timmy.forward(100)
#     timmy.setheading(head)
#     head+=90

# making a dashed line with many 
# for i in range(1, 51):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()

#     if(i%10 == 0):
#         timmy.left(72)

# making many different shape
# k = 3
# for i in range(3, 11):
#     for j in range(i):
#         timmy.forward(100)
#         timmy.left(360/i)
#     # k = k+1

# making a random walk
# timmy.pensize(4)
# direction = [0, 90, 180, 270, 360]
# for i in range(100):
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))

# making a spirograph
# headings = 0
# n = 36
# for i in range(36):
#     timmy.circle(120)
#     headings = headings + (360/n)
#     timmy.setheading(headings)


screen.exitonclick()