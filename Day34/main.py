# Day34 for 100Days4Python
# Project for Day34 : Trivia Quizzler Based on Day 17

from quiz_ui import QuizInterface
from quiz_data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
