# from turtle import Turtle, Screen

# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color('blue')
# timmy.forward(100)

# print(my_screen.canvheight)
# print(timmy) 
# my_screen.exitonclick()

import prettytable

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"]
    ]
)

print(table)

