# Day12 for 100Days4Python
# Project for Day12

import random

EASY_LEVEL = 10
HARD_LEVEL = 5

print("""
 _____                 _____ _       _____           _
|   __|_ _ ___ ___ ___|_   _| |_ ___|   | |_ _ _____| |_ ___ ___
|  |  | | | -_|_ -|_ -| | | |   | -_| | | | | |     | . | -_|  _|
|_____|___|___|___|___| |_| |_|_|___|_|___|___|_|_|_|___|___|_|
""")
print("Guess Number Between 1 and 100")

def set_difficulty():
    difficulty = input("[EASY]-10 Attempts or [HARD]-5 Attempts >>> ").lower()
    if difficulty == "easy":
        turns = EASY_LEVEL
    elif difficulty == "hard":
        turns = HARD_LEVEL
    else:
        turns = 0
    return turns

def check_answer(guess, answer):
    if guess > answer:
        print("Too High.")
    elif guess < answer:
        print("Too Low.")
    else:
        print(f"You Win! The Answer is {answer}.")
        return 1
    return 0

guess = 0
attempts = set_difficulty()
answer = random.randint(1, 100)
print(answer)
while attempts:
    print(f"\nRemaining Attempts : [{attempts}]")
    guess = int(input("Make guess >>> "))
    if check_answer(guess, answer):
        break
    else:
        attempts -= 1
if not attempts:
    print("You Lose.")