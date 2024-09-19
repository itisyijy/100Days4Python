# Day04 for 100Days4Python
# Randomization & Lists

import random

names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

# option 1
print(f"{random.choice(names)} is going to buy the meal today!")

# option 2
if len(names) == 0:
  print("Error.")
print(f"{names[random.randint(0, len(names) - 1)]} is going to buy the meal today!")