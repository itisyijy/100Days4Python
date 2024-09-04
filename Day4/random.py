# Day4 for 100Days4Python
# Randomization -> in Python, Mersenne Twister
# https://docs.python.org/3/library/random.html

import random       # random module

random_integer = random.randint(1, 100)   # [a, b]
print(f"random.randint : {random_integer}")

random_decimal = random.random()                 # [0, 1)
print(f"random.decimal : {random_decimal}")
random_decimal *= 10                             # [0, 10)
print(f"random.decimal : {random_decimal}")

random_float = random.uniform(1, 10)      # [a, b) or [a, b] depending on rounding
print(f"random.float : {random_float}")