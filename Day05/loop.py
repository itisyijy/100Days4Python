# Day05 for 100Days4Python
# Loop Statement

  # For Loop with List
cities = ["New York", "Paris", "London"]
for city in cities:
  print(city)
  print("inside of loop")
print("outside of loop")  # indentation is important!

  # clone "max" function
numbers = [142, -123, 4, 8, 15, 16, 23, 42, 54, 67, 89, 102, 37, 58, 231]
negative_numbers = [-1, -3, -5, -7, -9, -12, -15, -18, -20, -25, -30, -35]

def my_max(my_iter):
    my_max = my_iter[0]
    for item in my_iter:
      if my_max < item:
        my_max = item
    return my_max

print("my_max() :", my_max(numbers))
print("max()    :", max(numbers))

  # For Loop with range()
for i in range(1, 10):    # range(a, b) -> [a, b)
  print(i)                # 1 2 3 4 5 6 7 8 9

for i in range(1, 20, 3): # range(a, b, c) -> [a, b), step = c
  print(i)                # 1 4 7 10 13 16 19

  # Series Sum, ∑
def series_sum(start, stop, step):
  total = 0
  for i in range(start, stop, step):
    total += i
  return total

print(series_sum(1,101,1))

