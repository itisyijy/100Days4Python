# Day7 for 100Days4Python
# Project for Day7

import random
import hangman_word_list
import hangman_ascii_art

print(hangman_ascii_art.logo)

lives = 6
word_list = hangman_word_list.word_list
stages = hangman_ascii_art.stages
chosen_word = list(random.choice(word_list))

placeholder = []
for i in chosen_word:
    placeholder.append("_")

display = placeholder
log = []
while display != chosen_word and lives != 0:
    print(" ".join(display))
    guess = input("Guess a letter >>> ").lower()
    if guess in display or guess in log:
        print(f"**********You've already guessed {guess}.**********\n\n")
        continue
    for index in range(len(chosen_word)):
        if guess == chosen_word[index]:
            display[index] = guess
    if guess not in chosen_word:
        lives -= 1
        log.append(guess)
        print(f"******* {guess} is not in the word. Lives -1*******")
    print(stages[lives])
    print(f"***************{lives}/6 Lives Left.***************\n\n")

print(f"***************ANSWER : {''.join(chosen_word)}***************")
if lives == 0:
    print("******************YOU LOSE*******************")
else:
    print("*******************YOU WIN*******************")
