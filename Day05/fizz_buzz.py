# Day05 for 100Days4Python
# FizzBuzz with Loop

for i in range(1, 101):
  if i % 3 == 0 or i % 5 == 0:
    if i % 3 == 0:
      print("Fizz", end="")
    if i % 5 == 0:
      print("Buzz", end="")
    print("")
  else:
    print(i)