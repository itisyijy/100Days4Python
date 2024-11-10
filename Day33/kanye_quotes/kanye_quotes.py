# Day33 for 100Days4Python
# Day33 : Application Programming Interface, API

import requests
from tkinter import *


def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    quote = response.json()["quote"]
    print(quote)
    canvas.itemconfig(quote_text, text=f"{quote}")

    
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="./background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye West Says ...",
                                width=250, font=("Times New Roman", 20, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="./kanye_west.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
