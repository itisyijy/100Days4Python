# Day3 for 100Days4Python
# Conditional Statements, Code Blocks and Scope
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