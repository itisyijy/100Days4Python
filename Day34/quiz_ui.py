# Day34 for 100Days4Python
# Project for Day34 : Trivia Quizzler Based on Day 17

from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # use Type Hint
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Trivia Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text=f"Something to guess.",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280,
                                                     )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.score = 0
        self.scoreboard = Label(text=f"Score : {self.score}")
        self.scoreboard.config(background=THEME_COLOR, padx=20, pady=20, foreground="white")
        self.scoreboard.grid(column=0, row=0, columnspan=2)
        
        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.click_true)
        self.true_button.grid(column=0, row=2)
        
        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.click_false)
        self.false_button.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=f"{q_text}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def click_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def click_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
            self.score += 1
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)
