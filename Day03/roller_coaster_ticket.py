# Day03 for 100Days4Python
# Logical Operators -> True / False
		# A and B
		# C or D
		# not E
		# Roller Coaster Ticket Box
print("\nWelcome to the Roller Coaster!")
height = float(input("What is your height in cm? >>> "))
bill = -1

if height > 120.0:
	age = int(input("What is your age? >>> "))
	if age < 12:
		bill = 5
	elif age < 18:
		bill = 7
	elif 45 <= age <= 55:
		bill = 0
	else:
		bill = 12
	print(f"Ticket price is ${bill}")
	photo = input("Do you want to get photos? [Y/N] >>> ")
	if photo == "Y" or photo == "y":
		bill += 3
	print(f"Total price is ${bill}")
else:
	print("Sorry. Please come back and try again when you're taller.")