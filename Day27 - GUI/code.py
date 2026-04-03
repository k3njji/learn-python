# unlimited argument
def add(*args):
    total = 0
    for n in args:
        total+=n
        print(n)
    
    return total

print(add(1, 2, 3, 4, 5, 6))

def calculate(n, **kwargs):
    print(kwargs)

    for (key, value) in kwargs.items():
        print(key, value)

    n += kwargs['add']
    n *= kwargs['multiply']
    return n

print(calculate(3, add=3, multiply=5))  

class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw['model']

car = Car(make='nissan', model='gtr')
print(car.model)

from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop() 