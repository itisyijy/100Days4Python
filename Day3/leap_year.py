# Day3 for 100Days4Python
# Conditional Statements, Code Blocks and Scope
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