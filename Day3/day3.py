# Day3 for 100Days4Python
# Conditional Statements, Logical Operators, Code Blocks and Scope

# Conditional Statements, if / else
print("--Conditional Statements--")

	# Comparison Operators -> True / False
		# >     # >=    # ==
		# <     # <=    # !=

	# Modulo Operator, %
		# calculate remainder. (e.g., 10 % 5 == 0, 10 % 3 == 1)
	# Odd-Even Check
print("Odd-Even Check")
number = int(input("ODD or EVEN >>> "))
if number % 2 == 1:
	print(f"{number} is ODD.")
else:
	print(f"{number} is EVEN.")

	# Nesting & elif
		#BMI 2.0
print("\nBMI 2.0")
height = float(input("Please enter your height in meter >>> "))
weight = float(input("Please enter your weight in kilograms >>> "))
bmi = weight / (height ** 2)
interpretation = ""

if bmi >= 35:
	interpretation = "Clinically Obese"
elif bmi >= 30:
	interpretation = "Obese"
elif bmi >= 25:
	interpretation = "Slightly Overweight"
elif bmi >= 18.5:
	interpretation = "Normal Weight"
else:
	interpretation = "Underweight"

print(f"Your BMI is {bmi:.2f}.\nStatus : {interpretation}.")

	# Multiple if
		# Leap Year
print("\nLeap Year Check")
year = int(input("Enter the desired year >>> "))
leap = False
if year % 4 == 0:
	leap = True
if year % 100 == 0:
	if year % 400 != 0:
		leap = False
if leap:
	print("Leap year")
else:
	print("Not leap year")

		# Pizzeria
print("\nThank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L >>> ")
pepperoni = input("Do you want pepperoni? Y or N >>> ")
extra_cheese = input("Do you want extra cheese? Y or N >>> ")
bill = 0
valid = True

if size != "S" and size != "M" and size != "L":
	valid = False
if pepperoni != "Y" and pepperoni != "N":
	valid = False
if extra_cheese != "Y" and extra_cheese != "N":
	valid = False

if valid:
	if size == "S":
		bill += 15
		if pepperoni == "Y":
			bill += 2
	else:
		if size == "M":
			bill += 20
		elif size == "L":
			bill += 25
		if pepperoni == "Y":
			bill += 3
	if extra_cheese == "Y":
		bill += 1
	if bill:
		print(f"Your final bill is: ${bill}.")
else:
	print("You've entered something wrong.")

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