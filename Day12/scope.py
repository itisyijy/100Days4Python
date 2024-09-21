# Day12 for 100Days4Python
# Scope

number = 1          # Global scope

def increase_number():
    number = 2      # Local variables can be referenced in local scope only
    print(f"inside : {number}")

# Modifying Global Scope
def decrease_number():
    global number   # Avoid this approach
    number -= 1
    print(f"inside : {number}")

def add_ten(number):
    return number + 10  # Desirable approach

increase_number()               # print 2
print(f"outside : {number}")    # print 1
decrease_number()               # print 0
print(f"outside : {number}")    # print 0

number = add_ten(number)
print(f"outside : {number}")    # print 10

# Constant : MAKE UPPER CASE
PI = 3.141592

def print_pi():
    print(PI)
print_pi()