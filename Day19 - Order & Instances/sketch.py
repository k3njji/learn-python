from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def forw():
    timmy.forward(10)

def back():
    timmy.backward(10)

def turn_l():
    timmy.left(10)

def turn_r():
    timmy.right(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key = "w", fun=forw)
screen.onkey(key = "s", fun=back)
screen.onkey(key = "a", fun=turn_l)
screen.onkey(key = "d", fun=turn_r)
screen.onkey(key = "c", fun=clear)

screen.mainloop()