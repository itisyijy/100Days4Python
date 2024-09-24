# Day14 for 100Days4Python
# Project for Day14 : Higher Lower

import os
import random
from game_data import data
from art import logo, vs

def clear_console():
    if os.name == 'nt': # For Windows
        os.system('cls')
    else:               # For Linux/macOS
        os.system('clear')

def is_answer(a, b):
    guess = input("Who has more followers? Type 'A' or 'B':").lower()
    if a.get("follower_count") >= b.get("follower_count") and guess == 'a':
        return True
    elif a.get("follower_count") <= b.get("follower_count") and guess == 'b':
        return True
    else:
        return False

def status(is_ongoing, score):
    clear_console()
    print(logo)
    if score and is_ongoing:
        print(f"You're right! Current score: {score}")
    elif not is_ongoing:
        print(f"Sorry, that's wrong. Final score: {score}")
    return is_ongoing

def higher_lower():
    score = 0
    is_ongoing = True
    a_side = data[random.randint(0, len(data) - 1)]
    while status(is_ongoing, score):
        b_side = data[random.randint(0, len(data) - 1)]
        while a_side == b_side:
            b_side = data[random.randint(0, len(data) - 1)]
        print(f"Compare A: {a_side['name']}, a {a_side['description']}, from {a_side['country']}.")
        print(vs)
        print(f"Against B: {b_side['name']}, a {b_side['description']}, from {b_side['country']}.")
        is_ongoing = is_answer(a_side, b_side)
        if is_ongoing:
            score += 1
        a_side = b_side

higher_lower()