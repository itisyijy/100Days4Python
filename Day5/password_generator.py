# Day5 for 100Days4Python
# Project for Day5
import random

decimal_list = ['0','1','2','3','4','5','6','7','9']
alphabet_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
symbol_list = [
  '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
  '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'",
  '<', '>', ',', '.', '?', '/', '\\', '|', '~', '`'
]

print("Welcome to the Password Generator!")
goal_alphabet = int(input("How many alphabets would you like in your PW? >>> "))      # desired number of alphabet
goal_decimal = int(input("How many decimal numbers would you like in your PW? >>> ")) # desired number of decimal
goal_symbol = int(input("How many symbols would you like in your PW? >>> "))          # desired number of symbol
goal_length = goal_alphabet + goal_decimal + goal_symbol                              # desired length of password

# my code
password = ""
pointer = -1      # pointer for selecting alphabet, decimal, or symbol
now_alphabet = 0  # pointer = 0 for alphabet
now_decimal = 0   # pointer = 1 for decimal
now_symbol = 0    # pointer = 2 for symbol

if goal_length < 1 or goal_decimal < 0 or goal_symbol < 0 or goal_length < goal_decimal + goal_symbol:
  print("Error.")
else:
  for length in range(0,  goal_length):
    pointer_options = [0, 1, 2]                 # make possible option for pointer
    if now_alphabet == goal_alphabet:
      pointer_options.remove(0)
    if now_decimal == goal_decimal:
      pointer_options.remove(1)
    if now_symbol == goal_symbol:
      pointer_options.remove(2)
    pointer = random.choice(pointer_options)
    if pointer == 1:                            # add selected character to password
      password += random.choice(decimal_list)   # use 'random.choice()' instead of 'list[random.randint()]'
      now_decimal += 1
    elif pointer == 2:
      password += random.choice(symbol_list)
      now_symbol += 1
    elif pointer == 0:
      password += random.choice(alphabet_list)
      now_alphabet += 1
  print(f"Your Password >>> {password}\nlength = {len(password)}")

# simple
password_list = []
for i in range(0, goal_alphabet):                     # choose alphabets randomly
  password_list.append(random.choice(alphabet_list))
for i in range(0, goal_decimal):                      # choose decimals randomly
  password_list.append(random.choice(decimal_list))
for i in range(0, goal_symbol):                       # choose symbols randomly
  password_list.append(random.choice(symbol_list))
random.shuffle(password_list)                         # use random.shuffle()
password = "".join(password_list)                     # [list] -> "string" by using "".join()
print(f"Your Password >>> {password}\nlength = {len(password)}")