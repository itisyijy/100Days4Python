# Day26 for 100Days4Python
# Project for Day26 : NATO Alphabets

import pandas

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")
result = [nato_dict[letter.upper()] for letter in user_input if 'A' <= letter.upper() <= 'Z']
print(result)
