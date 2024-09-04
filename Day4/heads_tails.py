# Day4 for 100Days4Python
# Randomization
# Heads-Tails

import random

coin = random.randint(0, 1)
coin_guess = int(input("\nHeads or Tails?\n[0] for Heads, [1] for Tails >>> "))
result = False

if coin == 0 and coin_guess == 0:
  result = True
  print("The coin is heads")
elif coin == 1 and coin_guess == 1:
  result = True
  print("The coin is tails")
print(f"Your guess is {result}!")
