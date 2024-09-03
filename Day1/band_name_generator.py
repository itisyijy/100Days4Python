# Day1 for 100Days4Python
# Project for Day1

#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.print("Welcome to the Band Name Generator.")
#4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line:
# Solution: https://replit.com/@appbrewery/band-name-generator-end

city = input("What's name of the city you grew up in?\n")
pet = input("What's name of your pet?\n")
band_name = city + " " + pet

print("Your band name could be \"%s\"" %band_name)