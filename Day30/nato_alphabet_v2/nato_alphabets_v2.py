# Day30 for 100Days4Python
# Project for Day30 : NATO Alphabets Version 2

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# recursion
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()

# loop
while True:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
    else:
        print(output_list)
        break
    