from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
               'n','o','p','q','r','s','t','u','v','w','x','y','z',
               'A','B','C','D','E','F','G','H','I','J','K','L','M',
               'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    numbers = ['0','1','2','3','4','5','6','7','8','9']

    symbols = ['!','#','$','%','&','(',')','*','+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # data strcuture that are going to be sent
    new_data = {
        website:{
            'email': email,
            'password': password,
        }
    }

    if website == "" or password == "":
        messagebox.showwarning(
            title="Error",
            message="Website or Password cannot be empty"
        )
        return

    else:
        try:
            with open("Day29 - Password Manager/data.json", "r") as file:
                # dumping the data with json
                # json.dump(new_data, file, indent=4)
                # best practice is this one
                data = json.load(file)
        except FileNotFoundError:
            with open("Day29 - Password Manager/data.json", "w") as file:
                json.dump(data, file, indent=4)
        else:
            data.update(new_data)
            with open("Day29 - Password Manager/data.json", "w") as file:
                json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get()

    try:
        with open("Day29 - Password Manager/data.json", "r") as file:
                # dumping the data with json
                # json.dump(new_data, file, indent=4)
                # best practice is this one
                data = json.load(file)
    except FileNotFoundError:
         messagebox.showwarning(
            title="Error",
            message="No file was found"
        )
    else:
        if(data.get(website)):
            messagebox.showinfo(title='There is an entry', message=f'Email: {data[website]["email"]}\nPassword: {data[website]["password"]}')
            password_entry.delete(0, END)
            password_entry.insert(0, data[website]['password'])
        else:
            messagebox.showwarning(
                title="Website not Found",
                message="No email and password is recorded"
            )
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, height=200, width=200, highlightthickness=0)

logo = PhotoImage(file='Day29 - Password Manager/logo.png')

canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)

website_entry.focus()

search_button = Button(
    text="Search",
    width=14,
    command=search
)

search_button.grid(column=2, row=1)


email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

email_entry.insert(0, "example@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(
    text="Generate Password",
    command=generate_password
)
generate_button.grid(column=2, row=3)

add_button = Button(
    text="Add",
    width=36,
    command=save_password
)

add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()