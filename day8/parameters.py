# Day8 for 100Days4Python
# Functions with Inputs
# Arguments & Parameters

def greet(name):    # 'name' -> parameter, name of data
    print(f"Hello, {name}.")
    print(f"Buongiorno, {name}.")
    print(f"Bonjour, {name}.")
greet("Harrison")   # 'Harrison' -> argument, actual value of data

print("\n-------------------------------------------------")
def greet_with(name, location):                     # multiple parameter
    print(f"Hello, {name}.")
    print(f"What is it like to {location}?")
greet_with("Donald", "Washington")  # positional argument
greet_with("Washington", "Donald")  # positional argument
print("\n-------------------------------------------------")
greet_with(location="Washington", name="Donald")    # keyword argument
greet_with(name="Donald", location="Washington")    # keyword argument

# Project for Day8
# Caesar Cipher
