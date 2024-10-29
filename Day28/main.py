# Day28 for 100Days4Python
# Day28 : Building Pomodoro App
from tabnanny import check
from tkinter import *
import winsound


# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
MIN_TO_SEC = 60
WORK_SEC = 25 * MIN_TO_SEC
SHORT_BREAK_SEC = 5 * MIN_TO_SEC
LONG_BREAK_SEC = 20 * MIN_TO_SEC
CHECK_MARK = "✔"

reps = 0
timer_id = None


# Alert
def alert_sound():
    winsound.Beep(3000, 500)


# Timer Button
def start_timer():
    alert_sound()
    if reps % 2 == 0:
        count_down(WORK_SEC)
        session.config(text="WORK", foreground=GREEN)
    elif reps % 8 == 7:
        count_down(LONG_BREAK_SEC)
        session.config(text="BREAK", foreground=RED)
    else:
        count_down(SHORT_BREAK_SEC)
        session.config(text="BREAK", foreground=PINK)
    
    
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer_id)
    session.config(text="Timer", foreground=GREEN)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# Countdown
def clock_style(num):
    if num < 10:
        num = "0" + f"{num}"
    return num
    

def count_down(count):
    global reps, timer_id
    count -= 1
    count_min = clock_style(int(count / 60))
    count_sec = clock_style(count % 60)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        timer_id = window.after(1000, count_down, count)
    else:
        reps += 1
        check_marks.config(text=f"{CHECK_MARK * (int(reps / 2) + (reps % 2))}")
        start_timer()


# UI
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=20, background=YELLOW)
window.minsize(width=390, height=400)

# UI : Label
session = Label(text="Timer", font=(FONT_NAME, 40, "bold"), background=YELLOW, foreground=GREEN)
session.grid(column=1, row=0)

check_marks = Label(font=(FONT_NAME, 20, "bold"), background=YELLOW, foreground=GREEN)
check_marks.grid(column=1, row=3)

# UI : Canvas Widget
canvas = Canvas(width=210, height=234, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(105, 117, image=tomato_img)
timer_text = canvas.create_text(110, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# UI : Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
