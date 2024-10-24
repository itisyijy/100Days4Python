# Day26 for 100Days4Python
# Day26 : Dictionary Comprehension -> only available in python

import random
import pandas

# Dictionary Comprehension : Create new dictionary from previous dictionary
# Pattern : new_dict = {new_key:new_value for item in list}
names = ['Li', 'Mia', 'Zoe', 'Finn', 'Yara', 'Jonathan', 'Alexander', 'Elizabeth', 'Gabrielle', 'Christopher']
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

# Pattern : new_dict = {new_key:new_value for (key,value) in dict.items()}
# Pattern : new_dict = {new_key:new_value for (key,value) in dict.items() if condition}
passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
print(passed_students)

# Loop through a data frame
players = {
    "name": ["Son", "Maddison", "Solanke", "Kulusevski", "Romero"],
    "number": [7, 10, 19, 21, 17],
}

players_df = pandas.DataFrame(players)
print(players_df)

for (key, value) in players_df.items():
    print(key)
    print(value)

# Loop through rows of a data frame
for (index, row) in players_df.iterrows():
    print(row["name"], row["number"])
