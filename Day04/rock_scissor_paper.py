# Day04 for 100Days4Python
# Project for Day04

import random

rock = "✊ "
scissors = "✌️"
paper = "🤚"
rsp = [rock, scissors, paper]

print("Welcome to Rock Scissor Paper")
user = int(input(f"[0] for {rock} | [1] for {scissors} | [2] for {paper}\nSelect one of them >>> "))
bot = random.randint(0, 2)
if user > 2 or user < 0:
  print("---Error.---")
else:
  print(f"You chose {rsp[user]}")
  print(f"Bot chose {rsp[bot]}")

  if user == bot:
    print("---Draw.---")
  elif (user == 0 and bot == 1) or (user == 1 and bot == 2) or (user == 2 and bot == 0):
    print("---Win.---")
  else:
    print("---Lose.---")