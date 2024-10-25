# Day27 for 100Days4Python
# Project for Day27 : mile to kilometer

from tkinter import *


def mile_to_kilo():
    kilo_result.config(text=f"{int(mile_input.get()) * 1.609}")

arial = ("Arial", 10)

window = Tk()
window.title("Mile to KiloMeter")
window.config(padx=10, pady=10)

is_equal_to = Label()
is_equal_to.config(text="is equal to", font=arial, padx=5)
is_equal_to.grid(column=0, row=1)

mile_input = Entry(justify="center")
mile_input.config(width=10, font=arial)
mile_input.grid(column=1, row=0)

kilo_result = Label()
kilo_result.config(text="0", font=arial)
kilo_result.grid(column=1, row=1)

mile_unit = Label()
mile_unit.config(text="Miles", font=arial, padx=5)
mile_unit.grid(column=2, row=0)

kilo_unit = Label()
kilo_unit.config(text="KM", font=arial, padx=5)
kilo_unit.grid(column=2, row=1)

convert_button = Button()
convert_button.config(text="Convert", font=arial, command=mile_to_kilo)
convert_button.grid(column=1, row=2)

window.mainloop()
