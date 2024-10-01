# Day17 for 100Days4Python
# Day17 : True False Quiz

from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

# Write a for loop to iterate over the question_data
# Create a Question object from each entry in question_data
# Append each Question object to the question_bank
question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()