# Day3 for 100Days4Python
# Project for Day3

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island. Your mission is to find the treasure.")
left_right = (input("\nYou're at a cross road. Where do you want to go?"
                    "\n[left] or [right]? >>> ")).lower()
if left_right != "left":
	print("\nYou fall into a hole...\n-Game Over-")
else:
	wait_swim = (input("\nYou've come to a lake. There is an island in the middle of the lake."
	                   "\n[wait] for a boat or [swim] across? >>> ")).lower
	if wait_swim != "wait":
		print("\nYou are attacked by trout...\n-Game Over-")
	else:
		color = (input("\nYou arrive at the island unharmed."
		               "\nThere is a house with 3 doors. One [red], one [yellow] and one [blue]."
		               "\nWhich colour do you choose? >>> ")).lower
		if color == "yellow":
			print("\nYou win!")
		elif color == "red":
			print("\nYou are burned by fire...\n-Game Over-")
		elif color == "blue":
			print("\nYou are eaten by beasts...\n-Game Over-")
		else:
			print("\n-Game Over-")
