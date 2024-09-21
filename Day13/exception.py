# Day13 for 100Days4Python

# Project for Day13

# try & except
while True:
    try:
        age = int(input("How old are you? >>> "))
        break
    except ValueError:
        print("You have typed in an invalid valueㅁ. Please try again with numerical input(e.g., 19)")

if age > 18:
    print(f"You can drive at age {age}")