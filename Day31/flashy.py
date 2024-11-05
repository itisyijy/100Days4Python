# Day31 for 100Days4Python
# Capstone Project : Flash Card Program

import random
import pandas
from tkinter import *

FONT = "Arial"
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}

# ---------------------- CSV ---------------------- #
try:
    words_file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data_file = pandas.read_csv("./data/frequency_words_es_en.csv")
    words_dict = data_file.to_dict(orient="records")
else:
    words_dict = words_file.to_dict(orient="records")


def known_word():
    next_card()
    words_dict.remove(current_card)
    pandas.DataFrame(words_dict).to_csv("./data/words_to_learn.csv", index=False)


# ---------------------- CARD --------------------- #


def flip_card():
    global current_card
    
    en_word = current_card["english"]
    card.itemconfig(card_img, image=card_back_img)
    card.itemconfig(card_title, text="English", fill="white")
    card.itemconfig(card_content, text=en_word, fill="white")
    

def timer():
    return window.after(3000, flip_card)


def next_card():
    global current_card, timer_id
    
    window.after_cancel(timer_id)
    current_card = random.choice(words_dict)
    es_word = current_card["español"]
    
    card.itemconfig(card_img, image=card_front_img)
    card.itemconfig(card_title, text="Español", fill="black")
    card.itemconfig(card_content, text=es_word, fill="black")
    print(es_word)
    timer_id = timer()


# -------------------- UI SETUP ------------------- #
# UI : Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# UI : Canvas
card = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_img = card.create_image(400, 263, image=card_front_img, )
card_title = card.create_text(400, 150, text="Español", fill="black", font=(FONT, 40, "italic"))
card_content = card.create_text(400, 263, text="gracias", fill="black", font=(FONT, 50, "bold"))
card.grid(column=0, row=0, columnspan=2)

# UI : Button
check_img = PhotoImage(file="./images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=known_word)
known_button.grid(column=1, row=1)

cross_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

timer_id = window.after(3000, flip_card)
next_card()

# UI : mainloop()
window.mainloop()
