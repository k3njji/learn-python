from tkinter import *

def miles_to_kilo():
    miles = float(input_box.get())
    km = miles * 1.609
    kilo_result['text'] = km

window = Tk()
window.title('Miles to Kilometer Converter')

input_box = Entry()
input_box.grid(column=1, row=0)

label = Label(text='Miles')
label.grid(column=2, row=0)

is_equal = Label(text='is equal to')
is_equal.grid(column=0, row=1)

kilo_result = Label(text='0')
kilo_result.grid(column=1, row=1)

kilo_label = Label(text='KM')
kilo_label.grid(column=2, row=1)

calculate = Button(window, text='Calculate', command=miles_to_kilo)
calculate.grid(column=1, row=2)

window.mainloop()