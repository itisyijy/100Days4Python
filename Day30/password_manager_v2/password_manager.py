# Day29 for 100Days4Python
# Day29 : Password Manager

import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ------------------ PASSWORD GENERATOR ------------------ #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)
    password = "".join(password_list)
    
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# --------------------- SAVE PASSWORD -------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    line = f"{website} | {email} | {password}\n"
    
    if not (len(website) and len(email) and len(password)):
        messagebox.showerror(title="Oops!", message="THERE IS EMPTY FIELD.")
    elif messagebox.askokcancel(title="Are you sure?",
                                message=f"Website:\t{website}\nEmail:\t{email}\nPassword: {password}"):
        pyperclip.copy(password)
        with open("./data.txt", mode="a") as data:
            data.write(line)
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ----------------------- UI SETUP ----------------------- #


window = Tk()
window.config(padx=50, pady=50, background="white")
window.title("Password Manager")

# Logo image
canvas = Canvas(width=200, height=200, background="white", highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website: ", background="white")
website_label.grid(column=0, row=1, sticky="E")

email_label = Label(text="Email/Username: ", background="white")
email_label.grid(column=0, row=2, sticky="E")

password_label = Label(text="Password: ", background="white")
password_label.grid(column=0, row=3, sticky="E")

# Entry
website_entry = Entry(width=43)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")
website_entry.focus()   # on cursor

email_entry = Entry(width=43)
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")
email_entry.insert(index=0, string="username@email.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="W")

# Button
generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(column=2, row=3, sticky="W", padx=(4, 50))

add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")

# mainloop
window.mainloop()
