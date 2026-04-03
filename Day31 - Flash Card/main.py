from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- BACKEND ------------------------------- #

data = []
current_card = None
known = []
flip_timer = None


def load_data():
    global data
    try:
        df = pd.read_csv('Day31 - Flash Card/data/words_to_learn.csv')
    except FileNotFoundError:
        df = pd.read_csv('Day31 - Flash Card/data/french_words.csv')

    data = df.values.tolist()


def next_card():
    global current_card, flip_timer

    if flip_timer:
        window.after_cancel(flip_timer)

    remaining = [x for x in data if x not in known]

    if len(remaining) == 0:
        canvas.itemconfig(card_title, text="Done!")
        canvas.itemconfig(card_word, text="All words learned")
        return

    current_card = random.choice(remaining)

    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card[0])

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card[1])


def mark_known():
    global current_card

    known.append(current_card)

    remaining = [x for x in data if x not in known]

    df = pd.DataFrame(remaining, columns=["French", "English"])
    df.to_csv('Day31 - Flash Card/data/words_to_learn.csv', index=False)

    next_card()

load_data()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="Day31 - Flash Card/images/card_front.png")
card_back_img = PhotoImage(file="Day31 - Flash Card/images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(
    400,
    150,
    text="Title",
    font=("Arial", 40, "italic")
)

card_word = canvas.create_text(
    400,
    263,
    text="Word",
    font=("Arial", 60, "bold")
)

canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="Day31 - Flash Card/images/wrong.png")
right_img = PhotoImage(file="Day31 - Flash Card/images/right.png")

wrong_button = Button(
    image=wrong_img,
    highlightthickness=0,
    command=next_card
)

wrong_button.grid(row=1, column=0)

right_button = Button(
    image=right_img,
    highlightthickness=0,
    command=mark_known
)

right_button.grid(row=1, column=1)

next_card()

window.mainloop()