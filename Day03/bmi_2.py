# Day03 for 100Days4Python
# Conditional Statements, Code Blocks and Scope
	# Nesting & elif
		# BMI 2.0
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